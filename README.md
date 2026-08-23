# AI Knowledge Repo

A structured archive of YouTube transcripts and articles about AI/LLM
development, agent/skill building, and prompt engineering — normalized into
consistent markdown so other AI workflows (agent/skill/prompt reviewers, RAG
tools) can read it, not just humans.

## What's in here now

<!-- BEGIN GENERATED STATS -->
66 docs (59 articles, 7 YouTube transcripts), ~219k words, all classified
and simplified:

| category | docs |
| --- | --- |
| techniques | 24 |
| tools | 14 |
| best-practices | 11 |
| prompts | 7 |
| skills | 6 |
| trends | 4 |

34 docs carry extracted techniques/prompts.
<!-- END GENERATED STATS -->

Regenerated from `index/manifest.json` by
`scripts/update_readme_stats.py`, which runs as a pre-commit hook — don't
hand-edit the block above. The manifest is the source of truth and carries
these counts under `generated_entries`, `categories`, and
`ste100_simplified`.

## How it's organized

```
raw/                        # gitignored — local-only source archive
  youtube/<slug>.md         # untouched copies of downloaded transcripts
  articles/<slug>.md        # untouched copies of downloaded articles
processed/
  <source_type>-<slug>.md   # normalized markdown, one file per doc, flat
index/
  manifest.json             # generated — read this first, not the tree
scripts/
  ingest.py                 # raw -> processed (no API calls, deterministic)
  enrich_and_simplify.py    # classify + summarize + STE100-simplify (LLM, cached)
  build_manifest.py         # processed -> index/manifest.json
  update_readme_stats.py    # manifest -> README "What's in here now"
.cache/                     # gitignored — enrich hash cache, regenerable
```

`raw/` is a local-only archive (gitignored) — it keeps your original
downloads so re-ingestion is always possible on the machine that has them,
but it is not committed, so a fresh clone starts from `processed/` alone.
`processed/` is flat (no category subfolders): a doc's category can change
on re-classification without moving/renaming files, and
`index/manifest.json` — not directory layout — is the intended way for an
agent to find things.

Each processed doc has the same five sections: `Summary`, `Key Takeaways`,
`Techniques / Prompts Extracted`, `Full Content`, `Source`. STE100
simplification only rewrites `Summary` and `Key Takeaways` — `Techniques /
Prompts Extracted` and `Full Content` are kept verbatim, so quoted prompts
stay usable rather than being paraphrased into different prompts.

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
controlled-language rewrite task; 2.5 Flash-Lite is retired for new API
keys as of Aug 2026). Override with `STE100_MODEL=<id>`.

## Day-to-day workflow

1. Drop new transcripts/articles into `raw/youtube/` or `raw/articles/`
   (copy, don't move, from wherever you exported them). Files must end in
   `.md` — anything else is skipped by the glob without comment.
2. `python scripts/ingest.py` — normalizes them into `processed/`, no API
   calls, safe to run anytime. Each doc is reported as `new`, `rewritten`,
   or `preserved`. Docs that have already been enriched are `preserved`:
   they keep their category/tags/summary and their Summary / Key Takeaways
   / Techniques sections, and only Full Content and Source are refreshed
   from `raw/`, so editing a raw file still propagates and re-triggers
   enrichment for that doc.
3. `git add processed` and commit. The pre-commit hook calls the LLM only
   on the `processed/*.md` files you just staged, rewrites them in place
   with category/tags/summary/takeaways/techniques filled in, and exits
   non-zero so you can review the diff.
4. Review the diff, `git add` again, commit again — same pattern as
   Black/Prettier autofix hooks.

Skip the hook for one commit with `STE100_SKIP=1 git commit ...`.

Stage everything you intend to commit *before* committing. Pre-commit
stashes unstaged changes while it runs, so a partially staged `processed/`
means the hook enriches the stale staged version rather than what's on
disk.

### Slug collisions

Two raw files can normalize to the same processed name (`AI Workflow.md`
and `ai-workflow.md` both become `article-ai-workflow.md`). `ingest.py`
reports this on stderr rather than silently overwriting: a `note` when the
two have identical content, and a `WARNING` naming both files when they
differ and one is genuinely lost. Rename one raw file to resolve it.

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

## Caching

`enrich_and_simplify.py` keys its cache (`.cache/ste100_hashes.json`) on a
hash of each doc's `Full Content`, so unchanged docs are never re-sent to
the LLM. Editing a raw file changes that hash and correctly re-enriches
just that doc.

The cache only tracks Full Content, so it cannot detect a doc whose
*enrichment* went missing while its body stayed the same — such a file
still looks cached and gets skipped. If docs ever show up as
`category: "uncategorized"` despite a populated cache, drop their cache
entries to force a re-run:

```bash
python - <<'EOF'
import json, pathlib, re
cache = json.load(open('.cache/ste100_hashes.json'))
for p in pathlib.Path('processed').glob('*.md'):
    if re.search(r'^category:\s*"uncategorized"', p.read_text()[:800], re.M):
        cache.pop(str(p), None)
json.dump(cache, open('.cache/ste100_hashes.json', 'w'), indent=2)
EOF
```

## Manifest schema

`index/manifest.json` has four summary keys — `generated_entries`,
`categories`, `ste100_pending`, `ste100_simplified` — plus `entries`.

Each entry carries: `id`, `title`, `source_type`, `source_url`, `author`,
`published`, `ingested`, `category`, `tags`, `summary`, `ste100_status`,
`ste100_model`, `path`, `word_count`, `has_extracted_techniques`. An agent
can filter/rank on these fields alone before ever opening a file.

Valid categories are `prompts`, `skills`, `best-practices`, `tools`,
`trends`, `techniques`.

## Script reference

```bash
python scripts/ingest.py [--raw-dir raw] [--out-dir processed]
python scripts/enrich_and_simplify.py [--all] [--estimate-only] [--out-dir processed]
python scripts/build_manifest.py [--out-dir processed] [--manifest index/manifest.json]
python scripts/update_readme_stats.py [--readme README.md] [--check]
```

`update_readme_stats.py --check` reports a stale block without writing,
for use in CI.

## Costs

STE100/classification calls are billed per-token against whichever provider
you set. Check `python scripts/enrich_and_simplify.py --all --estimate-only`
before any bulk run — it computes the estimate from the actual sizes of the
files that would be processed, not a guess.

For scale: enriching the full 66-doc backlog (~359k input tokens) cost
about $0.17 on Gemini 3.5 Flash-Lite. The per-model rates used for
estimates live in `PRICING` in `scripts/enrich_and_simplify.py` and are
approximate — check your provider's pricing page before a large run.
