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

Safe to re-run at any time: a processed doc that has already been enriched
(ste100_status "simplified") keeps its category/tags/summary and its Summary /
Key Takeaways / Techniques sections. Only Full Content and Source are refreshed
from raw/, so editing a raw file still propagates — and changes the Full Content
hash, which is what makes enrich_and_simplify.py reclassify it on the next pass.
"""
import argparse
import hashlib
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from _frontmatter import parse_frontmatter, build_frontmatter, slugify

MULTI_BLANK_RE = re.compile(r"\n{3,}")
HTML_TAG_RE = re.compile(r"<[^>]+>")
# Raw sources often carry trailing whitespace. Strip it here so ingest agrees
# with the trim-trailing-whitespace pre-commit hook — otherwise the two fight:
# the hook strips it from processed/, the next ingest restores it from raw/,
# which changes the Full Content hash and re-triggers a paid enrich pass.
TRAILING_WS_RE = re.compile(r"[ \t]+$", re.MULTILINE)
TRANSCRIPT_SECTION_RE = re.compile(r"^##\s*Transcript\s*\n+(.*)", re.DOTALL | re.MULTILINE)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)

# Must stay in sync with SECTION_RE in enrich_and_simplify.py — both scripts
# read/write the same section layout.
SECTION_RE = re.compile(
    r"## Summary\n\n(?P<summary>.*?)\n\n"
    r"## Key Takeaways\n\n(?P<takeaways>.*?)\n\n"
    r"## Techniques / Prompts Extracted\n\n(?P<techniques>.*?)\n\n"
    r"## Full Content\n\n(?P<full_content>.*?)\n\n"
    r"## Source",
    re.DOTALL,
)

# Frontmatter fields that enrich_and_simplify.py owns; ingest must never
# clobber these on a re-run. Everything else is re-derived from raw/.
ENRICHED_FM_KEYS = ("category", "tags", "summary", "ste100_status", "ste100_model")

STUB_SUMMARY = "_Pending enrichment — run scripts/enrich_and_simplify.py (or the pre-commit hook) to fill this in._"
STUB_TAKEAWAYS = "_Pending enrichment._"
STUB_TECHNIQUES = "_Pending enrichment. If the source has no reusable prompts/techniques, this will say \"None identified.\"_"


def clean_text(text: str) -> str:
    text = HTML_TAG_RE.sub("", text)
    text = TRAILING_WS_RE.sub("", text)
    text = MULTI_BLANK_RE.sub("\n\n", text)
    return text.strip()


def content_id(source_type: str, slug: str) -> str:
    h = hashlib.sha1(f"{source_type}:{slug}".encode()).hexdigest()[:8]
    return f"{source_type}_{h}"


def source_block(meta: dict) -> str:
    return (
        f"## Source\n\n- Type: {meta.get('source_type')}\n"
        f"- URL: {meta.get('source_url') or 'n/a'}\n"
        f"- Author: {meta.get('author') or 'n/a'}\n"
        f"- Published: {meta.get('published') or 'n/a'}\n"
    )


def merge_preserving_enrichment(existing: str, meta: dict, body: str):
    """Re-ingest an already-enriched doc without destroying the enrichment.

    Keeps the LLM-authored frontmatter fields and the Summary / Key Takeaways /
    Techniques sections, and swaps in freshly-ingested Full Content + Source so
    edits to raw/ still propagate. Returns None when the destination isn't
    enriched (or can't be parsed), meaning a plain overwrite is safe.

    Note this is what keeps the enrich cache honest: the cache keys on a hash of
    Full Content, so a raw edit changes the hash and the doc is re-enriched,
    while an unchanged raw file round-trips byte-identically and stays cached.
    """
    old_meta, _, _ = parse_frontmatter(existing)
    sections = SECTION_RE.search(existing)
    if old_meta.get("ste100_status") != "simplified" or not sections:
        return None

    merged = dict(meta)
    for key in ENRICHED_FM_KEYS:
        if key in old_meta:
            merged[key] = old_meta[key]
    # First-seen date, not last-ingested date — don't reset it on a re-run.
    merged["ingested"] = old_meta.get("ingested", meta["ingested"])

    return build_frontmatter(merged) + (
        f"\n## Summary\n\n{sections.group('summary')}\n\n"
        f"## Key Takeaways\n\n{sections.group('takeaways')}\n\n"
        f"## Techniques / Prompts Extracted\n\n{sections.group('techniques')}\n\n"
        f"## Full Content\n\n{body}\n\n"
        + source_block(meta)
    )


def warn_on_collision(dest: Path, source: Path, body: str, claimed: dict) -> bool:
    """Two raw files can slugify to the same processed name, in which case the
    later one silently overwrites the earlier. Warn instead. Returns True if
    this write clobbers a *different* document (i.e. real content loss).

    claimed maps dest -> (raw source, body) for everything written this run.
    """
    prior = claimed.get(dest)
    claimed[dest] = (source, body)
    if prior is None:
        return False

    prior_source, prior_body = prior
    if prior_body == body:
        print(
            f"  note: {source} and {prior_source} both map to {dest.name} "
            f"(identical content, nothing lost)",
            file=sys.stderr,
        )
        return False

    print(
        f"  WARNING: slug collision on {dest.name} — {source} overwrites "
        f"{prior_source}, and their contents DIFFER. One of the two is lost. "
        f"Rename one raw file.",
        file=sys.stderr,
    )
    return True


def write_processed(out_dir: Path, source_type: str, slug: str, meta: dict, body: str,
                    source: Path, claimed: dict):
    """Returns (dest, status) where status is 'new', 'rewritten', or 'preserved'."""
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{source_type}-{slug}.md"
    warn_on_collision(dest, source, body, claimed)

    content = status = None
    if dest.exists():
        content = merge_preserving_enrichment(
            dest.read_text(encoding="utf-8", errors="ignore"), meta, body
        )
        status = "preserved" if content else "rewritten"

    if content is None:
        status = status or "new"
        content = build_frontmatter(meta) + (
            f"\n## Summary\n\n{STUB_SUMMARY}\n\n"
            f"## Key Takeaways\n\n{STUB_TAKEAWAYS}\n\n"
            f"## Techniques / Prompts Extracted\n\n{STUB_TECHNIQUES}\n\n"
            f"## Full Content\n\n{body}\n\n"
            + source_block(meta)
        )

    dest.write_text(content, encoding="utf-8")
    return dest, status


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


def ingest_youtube(raw_dir: Path, out_dir: Path, claimed: dict):
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
        dest, status = write_processed(
            out_dir, "youtube", slug, meta, cleaned, item, claimed
        )
        print(f"[youtube] {item.name} -> {dest} ({status})")


def ingest_articles(raw_dir: Path, out_dir: Path, claimed: dict):
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
        dest, status = write_processed(
            out_dir, "article", slug, meta, cleaned, item, claimed
        )
        print(f"[article] {item.name} -> {dest} ({status})")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", default="raw")
    parser.add_argument("--out-dir", default="processed")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    out_dir = Path(args.out_dir)
    # dest -> (raw source, body) for every doc written this run, so two raw
    # files that slugify to the same name are reported rather than silently
    # overwriting each other.
    claimed = {}
    ingest_youtube(raw_dir, out_dir, claimed)
    ingest_articles(raw_dir, out_dir, claimed)


if __name__ == "__main__":
    main()
