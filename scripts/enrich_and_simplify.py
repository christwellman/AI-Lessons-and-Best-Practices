#!/usr/bin/env python3
"""
enrich_and_simplify.py — Pre-commit hook (and manual batch tool): one cheap-LLM
call per changed/new processed/*.md doc that:
  1. classifies it (category + tags),
  2. writes a short Summary and Key Takeaways directly in ASD-STE100-style
     Simplified Technical English,
  3. pulls out any reusable prompts/techniques VERBATIM (never paraphrased —
     STE100 never touches Techniques or Full Content, since rewording a
     prompt makes it a different prompt).

Why one call instead of separate classify + simplify passes: it's the same
input tokens either way, so combining halves the API calls and cost for no
quality loss on a task this size.

Design notes:
- Hash-cached on the Full Content body, keyed by path — unchanged docs never
  re-call the API, whether run as a hook (staged files only) or in --all
  batch mode (every uncached file, for the one-time backlog run — this is
  meant to be invoked directly, not through `git commit`, since a full
  backlog pass can take minutes).
- Frontmatter, code fences, inline code, and URLs are stripped to
  placeholders before the prompt is sent (cuts tokens on link-heavy docs)
  and restored after — the model never sees or touches them.
- Autofix pattern: rewrites the file in place, then exits 1 so you review
  the diff and re-stage, same as Black/Prettier.
- STE100_SKIP=1 bypasses the hook entirely.
- --estimate-only computes the one-time backlog cost from real file sizes,
  no API calls.

Env vars:
    STE100_SKIP=1                              skip the hook entirely
    STE100_PROVIDER=gemini|openai|anthropic     (default: gemini)
    STE100_MODEL=<model id>                     override default model
    GEMINI_API_KEY / OPENAI_API_KEY / ANTHROPIC_API_KEY
"""
import argparse
import json
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

from _frontmatter import parse_frontmatter, build_frontmatter

CACHE_PATH = Path(".cache/ste100_hashes.json")

SECTION_RE = re.compile(
    r"## Summary\n\n(?P<summary>.*?)\n\n"
    r"## Key Takeaways\n\n(?P<takeaways>.*?)\n\n"
    r"## Techniques / Prompts Extracted\n\n(?P<techniques>.*?)\n\n"
    r"## Full Content\n\n(?P<full_content>.*?)\n\n"
    r"## Source",
    re.DOTALL,
)

DEFAULT_MODELS = {
    # gemini-2.5-flash-lite is retired for new API keys as of Aug 2026;
    # gemini-3.5-flash-lite is the current cheap-tier equivalent. Pinned
    # (not "-latest") so behavior/cost don't shift under you silently.
    "gemini": "gemini-3.5-flash-lite",
    "openai": "gpt-4o-mini",
    "anthropic": "claude-haiku-4-5",
}

# Rough per-M-token USD pricing (input, output) for --estimate-only. Verify
# against the provider's current pricing page before a large run — this is
# only ever used for a cost estimate shown to the user before they spend
# anything, never for billing.
PRICING = {
    "gemini-3.5-flash-lite": (0.30, 2.50),
    "gpt-4o-mini": (0.15, 0.60),
    "claude-haiku-4-5": (1.00, 5.00),
}

CATEGORIES = ["prompts", "skills", "best-practices", "tools", "trends", "techniques"]

SYSTEM_PROMPT = f"""You analyze one document (a YouTube transcript or article about AI/LLM
development, agent/skill building, or prompt engineering) for an AI knowledge
repo. Other AI agents will read your output to review and improve their own
prompts, skills, and agents — so precision matters more than style.

Respond with ONLY a single JSON object, no markdown fences, no commentary:
{{
  "category": one of {CATEGORIES},
  "tags": [2-5 short lowercase-hyphenated tags],
  "summary": "2-4 sentences in ASD-STE100 Simplified Technical English",
  "key_takeaways": ["3-7 bullet strings, each in ASD-STE100 style"],
  "techniques": ["exact verbatim quotes of any reusable prompts, skill
                  patterns, or techniques found in the text — copy them
                  EXACTLY, do not paraphrase. Empty list if none exist."]
}}

ASD-STE100 rules for "summary" and "key_takeaways" ONLY (never rewrite
"techniques" — those must stay verbatim):
- One meaning per word; use the simplest common word consistently.
- Active voice only. Simple tenses (present, simple past, simple future).
- One instruction or fact per sentence. Max ~20 words per sentence.
- No idioms, no filler phrases.
- Never remove a fact, number, condition, or qualifier that changes meaning.
- Do not alter text inside \x00CODE#\x00 placeholders — copy them through as-is
  if you use them in a quote.
"""


def get_staged_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True, check=True,
    )
    return [f for f in result.stdout.splitlines() if f.startswith("processed/") and f.endswith(".md")]


def get_all_files(out_dir: str):
    return [str(p) for p in sorted(Path(out_dir).glob("*.md"))]


def load_cache():
    return json.loads(CACHE_PATH.read_text()) if CACHE_PATH.exists() else {}


def save_cache(cache):
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2))


def body_hash(body: str) -> str:
    return hashlib.sha256(body.encode()).hexdigest()


def protect(text: str):
    placeholders = {}
    counter = [0]

    def stash(match):
        key = f"\x00CODE{counter[0]}\x00"
        placeholders[key] = match.group(0)
        counter[0] += 1
        return key

    text = re.sub(r"```.*?```", stash, text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", stash, text)
    text = re.sub(r"https?://\S+", stash, text)
    return text, placeholders


def restore(text: str, placeholders: dict) -> str:
    for key, val in placeholders.items():
        text = text.replace(key, val)
    return text


def restore_in_value(val, placeholders: dict):
    if isinstance(val, str):
        return restore(val, placeholders)
    if isinstance(val, list):
        return [restore_in_value(v, placeholders) for v in val]
    return val


def call_llm(provider: str, model: str, content: str) -> str:
    if provider == "gemini":
        from google import genai
        from google.genai import types
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        resp = client.models.generate_content(
            model=model,
            contents=content,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0,
            ),
        )
        return resp.text.strip()

    if provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": content},
            ],
            temperature=0,
            response_format={"type": "json_object"},
        )
        return resp.choices[0].message.content.strip()

    if provider == "anthropic":
        import anthropic
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        resp = client.messages.create(
            model=model, max_tokens=4096, temperature=0,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": content}],
        )
        return resp.content[0].text.strip()

    raise ValueError(f"Unknown provider: {provider}")


def parse_json_response(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(json)?\n", "", raw)
        raw = re.sub(r"\n```$", "", raw)
    return json.loads(raw)


def render_section(items) -> str:
    if not items:
        return "None identified."
    return "\n".join(f"- {item}" for item in items)


def process_file(path: Path, provider: str, model: str, cache: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, _, fm_block = parse_frontmatter(text)
    sections = SECTION_RE.search(text)
    if not fm or not sections:
        print(f"  skip (no frontmatter/section match): {path}")
        return False

    full_content = sections.group("full_content")
    h = body_hash(full_content)
    cache_key = str(path)
    if cache.get(cache_key) == h:
        print(f"  cached, no change: {path}")
        return False

    protected, placeholders = protect(full_content)
    raw_response = call_llm(provider, model, protected)
    result = parse_json_response(raw_response)
    result = {k: restore_in_value(v, placeholders) for k, v in result.items()}

    fm["category"] = result.get("category", fm.get("category", "uncategorized"))
    fm["tags"] = result.get("tags", [])
    fm["summary"] = result.get("summary", "")
    fm["ste100_status"] = "simplified"
    fm["ste100_model"] = model
    new_fm_block = build_frontmatter(fm)

    new_summary_section = result.get("summary", "")
    new_takeaways_section = render_section(result.get("key_takeaways", []))
    new_techniques_section = render_section(result.get("techniques", []))

    new_sections = (
        f"## Summary\n\n{new_summary_section}\n\n"
        f"## Key Takeaways\n\n{new_takeaways_section}\n\n"
        f"## Techniques / Prompts Extracted\n\n{new_techniques_section}\n\n"
        f"## Full Content\n\n{full_content}\n\n"
        f"## Source"
    )
    new_text = (
        new_fm_block
        + text[len(fm_block):sections.start()]
        + new_sections
        + text[sections.end():]
    )

    path.write_text(new_text, encoding="utf-8")
    cache[cache_key] = h
    print(f"  enriched: {path} -> category={fm['category']}")
    return True


def is_cached(path_str: str, cache: dict) -> bool:
    path = Path(path_str)
    if not path.exists():
        return False
    sections = SECTION_RE.search(path.read_text(encoding="utf-8", errors="ignore"))
    if not sections:
        return False
    return cache.get(path_str) == body_hash(sections.group("full_content"))


def estimate_cost(files, provider: str, model: str):
    price_in, price_out = PRICING.get(model, (0.10, 0.40))
    total_chars = 0
    counted = 0
    for f in files:
        path = Path(f)
        if not path.exists():
            continue
        sections = SECTION_RE.search(path.read_text(encoding="utf-8", errors="ignore"))
        if not sections:
            continue
        total_chars += len(sections.group("full_content")) + len(SYSTEM_PROMPT)
        counted += 1
    input_tokens = total_chars / 4
    output_tokens = counted * 400  # ~400 tokens of JSON output per doc, rough
    cost = (input_tokens / 1_000_000) * price_in + (output_tokens / 1_000_000) * price_out
    print(f"Files to process: {counted}")
    print(f"Estimated input tokens:  ~{input_tokens:,.0f}")
    print(f"Estimated output tokens: ~{output_tokens:,.0f}")
    print(f"Estimated cost ({model}): ~${cost:.4f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="batch mode: process every uncached file in --out-dir, not just staged ones")
    parser.add_argument("--out-dir", default="processed")
    parser.add_argument("--estimate-only", action="store_true", help="print cost estimate for the files that would be processed, call no API")
    args = parser.parse_args()

    if os.environ.get("STE100_SKIP") == "1":
        print("STE100_SKIP=1 set, skipping.")
        return 0

    provider = os.environ.get("STE100_PROVIDER", "gemini")
    model = os.environ.get("STE100_MODEL", DEFAULT_MODELS.get(provider))

    files = get_all_files(args.out_dir) if args.all else get_staged_files()
    if not files:
        print("No files to process.")
        return 0

    cache = load_cache()
    uncached = [f for f in files if not is_cached(f, cache)]

    if args.estimate_only:
        estimate_cost(uncached, provider, model)
        return 0

    changed_any = False
    print(f"Running enrich-and-simplify via {provider}:{model} on {len(uncached)} file(s) ({len(files) - len(uncached)} cached)...")
    for f in files:
        path = Path(f)
        if not path.exists():
            continue
        try:
            if process_file(path, provider, model, cache):
                changed_any = True
        except Exception as e:
            print(f"  ERROR on {f}: {e}", file=sys.stderr)
            save_cache(cache)
            return 1

    save_cache(cache)
    if changed_any and not args.all:
        print("\nFiles were enriched and modified in place.\nReview the changes, then `git add` them and commit again.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
