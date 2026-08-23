#!/usr/bin/env python3
"""
update_readme_stats.py — Regenerate the "What's in here now" block in
README.md from index/manifest.json, so the counts in the docs can't drift
away from the actual contents of processed/.

Usage:
    python scripts/update_readme_stats.py [--manifest index/manifest.json]
                                          [--readme README.md] [--check]

Rewrites only the text between the BEGIN/END marker comments; everything
else in README.md is left alone. Writes nothing when the generated block is
already correct, so it doesn't churn the file on every commit.

Runs as a pre-commit hook after build-manifest (which regenerates the
manifest this reads). Exits 1 if it changed the file — same autofix
convention as the other hooks: review the diff, `git add`, commit again.
--check reports staleness without writing, for CI.
"""
import argparse
import json
import sys
import textwrap
from pathlib import Path

BEGIN = "<!-- BEGIN GENERATED STATS -->"
END = "<!-- END GENERATED STATS -->"


def humanize_words(n: int) -> str:
    if n >= 1_000_000:
        return f"~{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"~{round(n / 1_000)}k"
    return str(n)


def render_block(manifest: dict) -> str:
    entries = manifest.get("entries", [])
    total = len(entries)
    words = sum(e.get("word_count", 0) for e in entries)

    by_source = {}
    by_category = {}
    for e in entries:
        by_source[e.get("source_type", "?")] = by_source.get(e.get("source_type", "?"), 0) + 1
        by_category[e.get("category", "?")] = by_category.get(e.get("category", "?"), 0) + 1

    label = {"article": "articles", "youtube": "YouTube transcripts"}
    parts = [
        f"{count} {label.get(src, src)}"
        for src, count in sorted(by_source.items(), key=lambda kv: (-kv[1], kv[0]))
    ]
    breakdown = ", ".join(parts) if parts else "no docs yet"

    pending = manifest.get("ste100_pending", 0)
    state = (
        "all classified and simplified"
        if not pending
        else f"{pending} still pending enrichment"
    )

    # Wrapped to match the hand-written prose around it in the README.
    intro = textwrap.wrap(
        f"{total} docs ({breakdown}), {humanize_words(words)} words, {state}:",
        width=76,
    )
    lines = [BEGIN, *intro, "", "| category | docs |", "| --- | --- |"]
    # Highest count first, then alphabetically, so the table is stable.
    for category, count in sorted(by_category.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {category} | {count} |")

    with_techniques = sum(1 for e in entries if e.get("has_extracted_techniques"))
    lines += ["", f"{with_techniques} docs carry extracted techniques/prompts.", END]
    return "\n".join(lines)


def splice(readme_text: str, block: str) -> str:
    start = readme_text.find(BEGIN)
    end = readme_text.find(END)
    if start == -1 or end == -1 or end < start:
        raise SystemExit(
            f"error: could not find {BEGIN} / {END} markers in the README. "
            "Add them around the stats block, or this hook has nothing to update."
        )
    return readme_text[:start] + block + readme_text[end + len(END):]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="index/manifest.json")
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 if the README is stale, but don't write it")
    args = parser.parse_args()

    manifest_path, readme_path = Path(args.manifest), Path(args.readme)
    if not manifest_path.exists():
        print(f"{manifest_path} not found — run scripts/build_manifest.py first.",
              file=sys.stderr)
        return 1
    if not readme_path.exists():
        print(f"{readme_path} not found.", file=sys.stderr)
        return 1

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    original = readme_path.read_text(encoding="utf-8")
    updated = splice(original, render_block(manifest))

    if updated == original:
        return 0

    if args.check:
        print(f"{readme_path} stats block is stale — run "
              "python scripts/update_readme_stats.py", file=sys.stderr)
        return 1

    readme_path.write_text(updated, encoding="utf-8")
    print(f"Updated stats block in {readme_path}.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
