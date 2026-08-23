# AI Knowledge Repo

A structured archive of YouTube transcripts and articles about AI/LLM
development, agent/skill building, and prompt engineering — normalized into
consistent markdown so other AI workflows (agent/skill/prompt reviewers, RAG
tools) can read it, not just humans.

## How it's organized

```
raw/
  youtube/<slug>.md     # untouched copies of downloaded transcripts
  articles/<slug>.md    # untouched copies of downloaded articles
processed/
  <source_type>-<slug>.md   # normalized markdown, one file per doc, flat
index/
  manifest.json          # generated — read this first, not the tree
scripts/
  ingest.py               # raw -> processed (no API calls, deterministic)
  enrich_and_simplify.py  # classify + summarize + STE100-simplify (LLM, cached)
  build_manifest.py       # processed -> index/manifest.json
```

`raw/` is a local-only archive (gitignored) — it keeps your original
downloads so re-ingestion is always possible on the machine that has them,
but it is not committed, so a fresh clone starts from `processed/` alone.
`processed/` is flat (no category subfolders): a doc's category can change
on re-classification without moving/renaming files, and
`index/manifest.json` — not directory layout — is the intended way for an
agent to find things.

## Setup

```bash
pip install pre-commit google-genai   # or openai / anthropic, see below
pre-commit install
```

Set an API key as an environment variable (never commit it):

```bash
export GEMINI_API_KEY=...        # default provider
# or: export OPENAI_API_KEY=... STE100_PROVIDER=openai
# or: export ANTHROPIC_API_KEY=... STE100_PROVIDER=anthropic
```

Default model is Gemini 2.5 Flash-Lite (cheapest capable option for a
controlled-language rewrite task). Override with `STE100_MODEL=<id>`.

## Day-to-day workflow

1. Drop new transcripts/articles into `raw/youtube/` or `raw/articles/`
   (copy, don't move, from wherever you exported them).
2. `python scripts/ingest.py` — normalizes them into `processed/`, no API
   calls, safe to run anytime. Docs that have already been enriched keep
   their category/tags/summary and their Summary / Key Takeaways /
   Techniques sections; only Full Content and Source are refreshed from
   `raw/`, so editing a raw file still propagates and re-triggers
   enrichment for that doc.
3. `git add raw processed` and commit. The pre-commit hook calls the LLM
   only on the `processed/*.md` files you just staged, rewrites them in
   place with category/tags/summary/takeaways/techniques filled in, and
   exits non-zero so you can review the diff.
4. Review the diff, `git add` again, commit again — same pattern as
   Black/Prettier autofix hooks.

Skip the hook for one commit with `STE100_SKIP=1 git commit ...`.

## First-time bulk backlog run

Don't run hundreds of docs through `git commit` — a full pass can take
minutes and a slow hook gets bypassed in practice. Instead, after
`ingest.py` has populated `processed/`:

```bash
# see the cost before spending anything
python scripts/enrich_and_simplify.py --all --estimate-only

# then actually run it
python scripts/enrich_and_simplify.py --all
python scripts/build_manifest.py
git add processed index
git commit -m "Bulk-enrich initial backlog"
```

`--all` processes every uncached file in `processed/`, not just staged
ones, and is meant to be run directly, not through git.

## Manifest schema

`index/manifest.json` entries carry: `id`, `title`, `source_type`,
`source_url`, `author`, `published`, `ingested`, `category`, `tags`,
`summary`, `ste100_status`, `ste100_model`, `path`, `word_count`,
`has_extracted_techniques`. An agent can filter/rank on these fields alone
before ever opening a file.

## Costs

STE100/classification calls are billed per-token against whichever provider
you set. Check `python scripts/enrich_and_simplify.py --all --estimate-only`
before any bulk run — it computes the estimate from your actual staged file
sizes, not a guess.
