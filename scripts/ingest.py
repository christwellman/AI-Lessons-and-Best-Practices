#!/usr/bin/env python3
"""
ingest.py — Normalize raw YouTube transcripts / articles into structured,
frontmattered markdown under processed/ for consumption by downstream AI
workflows (agent/skill/prompt reviewers, RAG indexers, etc).

Usage:
    python scripts/ingest.py --raw-dir raw --out-dir processed

Raw layout (flat, matches what actually gets copied out of Downloads):
    raw/youtube/<slug>.md   — has "---" frontmatter (title/author/video URL)
                              plus a "## Transcript" section with the body.
    raw/articles/<slug>.md  — frontmatter is optional; body is the article,
                              title falls back to the first H1 or the filename.

Output: processed/<source_type>-<slug>.md, flat (no category subfolders —
category/tags live in frontmatter and get aggregated into index/manifest.json,
which is the thing downstream agents should actually read to find content).

Deliberately does NOT call an LLM or guess a category here — that stays a
fast, deterministic, offline pass. Classification, summarization, and STE100
simplification all happen in one shot in scripts/enrich_and_simplify.py
(the pre-commit hook), so every doc starts as category "uncategorized" /
ste100_status "pending" until that hook — or a manual batch run of it — has
processed it.
"""
import argparse
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

from _frontmatter import parse_frontmatter, build_frontmatter, slugify

MULTI_BLANK_RE = re.compile(r"\n{3,}")
HTML_TAG_RE = re.compile(r"<[^>]+>")
TRANSCRIPT_SECTION_RE = re.compile(r"^##\s*Transcript\s*\n+(.*)", re.DOTALL | re.MULTILINE)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)

STUB_SUMMARY = "_Pending enrichment — run scripts/enrich_and_simplify.py (or the pre-commit hook) to fill this in._"
STUB_TAKEAWAYS = "_Pending enrichment._"
STUB_TECHNIQUES = "_Pending enrichment. If the source has no reusable prompts/techniques, this will say \"None identified.\"_"


def clean_text(text: str) -> str:
    text = HTML_TAG_RE.sub("", text)
    text = MULTI_BLANK_RE.sub("\n\n", text)
    return text.strip()


def content_id(source_type: str, slug: str) -> str:
    h = hashlib.sha1(f"{source_type}:{slug}".encode()).hexdigest()[:8]
    return f"{source_type}_{h}"


def write_processed(out_dir: Path, source_type: str, slug: str, meta: dict, body: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{source_type}-{slug}.md"
    content = build_frontmatter(meta) + (
        f"\n## Summary\n\n{STUB_SUMMARY}\n\n"
        f"## Key Takeaways\n\n{STUB_TAKEAWAYS}\n\n"
        f"## Techniques / Prompts Extracted\n\n{STUB_TECHNIQUES}\n\n"
        f"## Full Content\n\n{body}\n\n"
        f"## Source\n\n- Type: {meta.get('source_type')}\n"
        f"- URL: {meta.get('source_url') or 'n/a'}\n"
        f"- Author: {meta.get('author') or 'n/a'}\n"
        f"- Published: {meta.get('published') or 'n/a'}\n"
    )
    dest.write_text(content, encoding="utf-8")
    return dest


def base_meta(source_type: str, slug: str, title: str, source_url: str, author: str, published: str) -> dict:
    return {
        "id": content_id(source_type, slug),
        "title": title,
        "source_type": source_type,
        "source_url": source_url or "",
        "author": author or "",
        "published": published or "",
        "ingested": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "category": "uncategorized",
        "tags": [],
        "summary": "",
        "ste100_status": "pending",
        "ste100_model": None,
    }


def ingest_youtube(raw_dir: Path, out_dir: Path):
    yt_dir = raw_dir / "youtube"
    if not yt_dir.exists():
        return
    for item in sorted(yt_dir.glob("*.md")):
        text = item.read_text(encoding="utf-8", errors="ignore")
        fm, body, _ = parse_frontmatter(text)

        title = (fm.get("title") or item.stem.replace("-", " ").title())
        title = re.sub(r"\.md$", "", title).strip()
        author = fm.get("author", "")
        url = fm.get("video", "")

        transcript_match = TRANSCRIPT_SECTION_RE.search(body)
        transcript = transcript_match.group(1) if transcript_match else body
        cleaned = clean_text(transcript)

        slug = slugify(item.stem)
        meta = base_meta("youtube", slug, title, url, author, "")
        dest = write_processed(out_dir, "youtube", slug, meta, cleaned)
        print(f"[youtube] {item.name} -> {dest}")


def ingest_articles(raw_dir: Path, out_dir: Path):
    art_dir = raw_dir / "articles"
    if not art_dir.exists():
        return
    for item in sorted(art_dir.glob("*.md")):
        text = item.read_text(encoding="utf-8", errors="ignore")
        fm, body, _ = parse_frontmatter(text)

        h1_match = H1_RE.search(body)
        title = fm.get("title") or (h1_match.group(1).strip() if h1_match else item.stem.replace("-", " ").title())
        cleaned = clean_text(body)

        slug = slugify(item.stem)
        meta = base_meta("article", slug, title, fm.get("url", ""), fm.get("author", ""), fm.get("published", ""))
        dest = write_processed(out_dir, "article", slug, meta, cleaned)
        print(f"[article] {item.name} -> {dest}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", default="raw")
    parser.add_argument("--out-dir", default="processed")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    out_dir = Path(args.out_dir)
    ingest_youtube(raw_dir, out_dir)
    ingest_articles(raw_dir, out_dir)


if __name__ == "__main__":
    main()
