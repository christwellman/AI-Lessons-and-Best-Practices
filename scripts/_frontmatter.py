"""Shared minimal YAML-frontmatter helpers used by ingest.py, build_manifest.py,
and enrich_and_simplify.py. Deliberately not a real YAML parser (no pyyaml
dependency) — only the small subset of syntax these scripts themselves write:
quoted strings, bracketed lists, null, and bare numbers/URLs.
"""
import re

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
KV_RE = re.compile(r'^(\w+):\s*(.*)$')


def parse_frontmatter(text: str):
    """Returns (meta: dict, body: str, frontmatter_block: str).
    frontmatter_block is the raw '---\\n...\\n---\\n' text, or '' if absent.
    body is everything after the frontmatter block (or the whole text)."""
    match = FRONTMATTER_RE.search(text)
    if not match:
        return {}, text, ""
    meta = {}
    for line in match.group(1).splitlines():
        kv = KV_RE.match(line)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith('[') and val.endswith(']'):
            inner = val[1:-1].strip()
            val = [v.strip() for v in inner.split(',') if v.strip()] if inner else []
        elif val == "null":
            val = None
        meta[key] = val
    return meta, text[match.end():], match.group(0)


def build_frontmatter(meta: dict) -> str:
    lines = ["---"]
    for key, val in meta.items():
        if isinstance(val, list):
            lines.append(f"{key}: [{', '.join(val)}]" if val else f"{key}: []")
        elif val is None:
            lines.append(f"{key}: null")
        else:
            escaped = str(val).replace('"', '\\"')
            lines.append(f'{key}: "{escaped}"' if isinstance(val, str) else f"{key}: {val}")
    lines.append("---\n")
    return "\n".join(lines)


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-")[:80]
