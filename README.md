# AI Knowledge Repo

A structured archive of YouTube transcripts and articles about AI/LLM
development, agent/skill building, and prompt engineering — normalized into
consistent markdown so other AI workflows (agent/skill/prompt reviewers, RAG
tools) can read it, not just humans.

## How it's organized

```
raw/
  <slug>.md               # local scratch space, gitignored, not tracked
processed/
  <slug>.md                # normalized markdown, one file per doc, flat
index/
  manifest.json          # generated — read this first, not the tree
scripts/
  ingest.py               # raw -> processed (no API calls, deterministic)
  enrich_and_simplify.py  # classify + summarize + STE100-simplify (LLM, cached)
  build_manifest.py       # processed -> index/manifest.json
```

`processed/` is flat (no category subfolders): a doc's category can change
on re-classification without moving/renaming files, and
`index/manifest.json` — not directory layout — is the intended way for an
agent to find things.

**`raw/` is deliberately NOT a tracked archive.** The original design kept
raw sources permanently git-tracked as a safety net for future re-ingestion.
That was dropped as duplicative: `raw/` is gitignored local scratch space —
drop files in, run `ingest.py`, and the normalized `processed/*.md` is the
only thing that ends up in git. `ingest.py --delete-after-ingest` will even
remove each raw file once it's been written to `processed/`, if you don't
want raw copies lingering on disk either. Trade-off, made deliberately: if
the ingestion logic changes later, there's no raw archive to re-run it
against — only `processed/` output as it existed at ingest time.

Source type (YouTube vs. article) is auto-detected per file — a `video:`
frontmatter field or a `## Transcript` heading means YouTube, otherwise
article — so `raw/` is a single flat folder with no sorting step and no
"wrong folder" to put a file in.

## Why this differs from the original draft design

A few deliberate changes from the first design pass, made after looking at
real sample files:

- **No keyword-based categorization.** A naive keyword pass isn't reliable
  enough to trust, and running it as a *separate* pass from the LLM call
  would double API cost for no benefit. Every doc starts `category:
  uncategorized` from `ingest.py` and gets properly classified the first
  time `enrich_and_simplify.py` touches it.
- **STE100 only touches `Summary` and `Key Takeaways`.** The whole point of
  this repo is that other agents can review and reuse exact prompt/technique
  text. Simplifying `Techniques / Prompts Extracted` or `Full Content` would
  paraphrase prompts into different prompts. Those two sections are never
  sent through controlled-English rewriting — only extracted or copied
  verbatim.
- **Classification + summarization + STE100 rewrite happen in one LLM call**,
  not three. Same input tokens either way; one call halves the cost.
- **Manifest carries `summary`, `word_count`, `has_extracted_techniques`,
  `category`, `tags`** per entry — enough for an agent to decide "should I
  open this file" without opening it.
- **`processed/` has no category subdirectories** (see above) — the manifest
  is the index, not the filesystem.
- **`raw/` is gitignored scratch space, not a tracked archive**, and has no
  youtube/articles split — source type is auto-detected per file. See the
  callout above for the trade-off this accepts.

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

Default model is Gemini 3.5 Flash-Lite (cheapest capable option for a
controlled-language rewrite task, as of the current Gemini model
generation). Override with `STE100_MODEL=<id>`. Free-tier Gemini keys are
rate-limited (commonly 15 requests/minute) — `enrich_and_simplify.py`
retries with backoff on rate-limit errors, so a bulk run just goes slower
under a free-tier key rather than failing partway through.

## Day-to-day workflow

1. Drop new transcripts/articles into `raw/` (copy, don't move, from
   wherever you exported them — any mix of YouTube transcripts and
   articles, source type is auto-detected).
2. `python scripts/ingest.py` — normalizes them into `processed/`, no API
   calls, safe to run anytime. Add `--delete-after-ingest` if you don't
   want the raw copies kept around locally either.
3. `git add processed` and commit (there's nothing to add under `raw/` —
   it's gitignored). The pre-commit hook calls the LLM
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
