#!/usr/bin/env python3
"""
ingest.py — Normalize raw YouTube transcripts / articles into structured,
frontmattered markdown under processed/ for consumption by downstream AI
workflows (agent/skill/prompt reviewers, RAG indexers, etc).

Usage:
    python scripts/ingest.py [--raw-dir raw] [--out-dir processed] [--delete-after-ingest]

Raw layout: flat raw/*.md files, any mix of YouTube transcripts and
articles. Source type is auto-detected — a "video:" frontmatter field or a
"## Transcript" heading means youtube, otherwise article — so there's no
folder to sort into and no way to put a file in the "wrong" place.

raw/ is local scratch space, not a tracked archive (see README): it's
gitignored, and --delete-after-ingest removes each source file once it's
been written to processed/, for people who don't want raw copies lingering
on disk either.

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


def write_processed(out_dir: Path, slug: str, meta: dict, body: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{slug}.md"
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


def detect_source_type(fm: dict, body: str) -> str:
    if fm.get("video"):
        return "youtube"
    if TRANSCRIPT_SECTION_RE.search(body):
        return "youtube"
    return "article"


def ingest_file(item: Path, out_dir: Path, delete_after: bool):
    text = item.read_text(encoding="utf-8", errors="ignore")
    fm, body, _ = parse_frontmatter(text)
    source_type = detect_source_type(fm, body)

    if source_type == "youtube":
        transcript_match = TRANSCRIPT_SECTION_RE.search(body)
        content_body = transcript_match.group(1) if transcript_match else body
        source_url = fm.get("video", "")
    else:
        content_body = body
        source_url = fm.get("url", "")

    h1_match = H1_RE.search(body)
    title = fm.get("title") or (h1_match.group(1).strip() if h1_match else item.stem.replace("-", " ").title())
    title = re.sub(r"\.md$", "", title).strip()
    cleaned = clean_text(content_body)

    slug = slugify(item.stem)
    meta = base_meta(source_type, slug, title, source_url, fm.get("author", ""), fm.get("published", ""))
    dest = write_processed(out_dir, slug, meta, cleaned)
    print(f"[{source_type}] {item.name} -> {dest}")

    if delete_after:
        item.unlink()
        print(f"  deleted raw source: {item}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", default="raw")
    parser.add_argument("--out-dir", default="processed")
    parser.add_argument(
        "--delete-after-ingest", action="store_true",
        help="delete each raw file once it's been written to processed/ — raw/ is local scratch space, not a tracked archive",
    )
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    out_dir = Path(args.out_dir)
    for item in sorted(raw_dir.glob("*.md")):
        ingest_file(item, out_dir, args.delete_after_ingest)


if __name__ == "__main__":
    main()
