#!/usr/bin/env python3
"""
build_manifest.py — Rebuild index/manifest.json from processed/**/*.md. This
is the file other AI workflows (agent/skill/prompt reviewers, RAG loaders,
retrieval tools) should read to decide what's relevant, instead of scanning
or opening every file in the repo.

Usage:
    python scripts/build_manifest.py [--out-dir processed] [--manifest index/manifest.json]
"""
import argparse
import json
import re
from pathlib import Path

from _frontmatter import parse_frontmatter

SECTION_RE = re.compile(
    r"## Summary\n\n(?P<summary>.*?)\n\n"
    r"## Key Takeaways\n\n(?P<takeaways>.*?)\n\n"
    r"## Techniques / Prompts Extracted\n\n(?P<techniques>.*?)\n\n"
    r"## Full Content\n\n(?P<full_content>.*?)\n\n"
    r"## Source",
    re.DOTALL,
)


def build_entry(md_file: Path) -> dict:
    text = md_file.read_text(encoding="utf-8", errors="ignore")
    meta, _, _ = parse_frontmatter(text)
    entry = dict(meta)
    entry["path"] = str(md_file)

    sections = SECTION_RE.search(text)
    if sections:
        full_content = sections.group("full_content")
        techniques = sections.group("techniques").strip()
        entry["word_count"] = len(full_content.split())
        entry["has_extracted_techniques"] = techniques not in (
            "", "None identified.",
            "_Pending enrichment. If the source has no reusable prompts/techniques, this will say \"None identified.\"_",
        )
        # summary field on frontmatter is authoritative once enriched; fall
        # back to the body Summary section for older/partially-enriched docs.
        if not entry.get("summary"):
            entry["summary"] = sections.group("summary").strip()
    else:
        entry["word_count"] = 0
        entry["has_extracted_techniques"] = False

    return entry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="processed")
    parser.add_argument("--manifest", default="index/manifest.json")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    manifest_path = Path(args.manifest)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    entries = [build_entry(f) for f in sorted(out_dir.glob("*.md"))]

    manifest = {
        "generated_entries": len(entries),
        "categories": sorted({e.get("category", "") for e in entries if e.get("category")}),
        "ste100_pending": sum(1 for e in entries if e.get("ste100_status") == "pending"),
        "ste100_simplified": sum(1 for e in entries if e.get("ste100_status") == "simplified"),
        "entries": entries,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Wrote {len(entries)} entries to {manifest_path}")


if __name__ == "__main__":
    main()
