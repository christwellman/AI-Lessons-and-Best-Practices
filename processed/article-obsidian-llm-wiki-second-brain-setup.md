---
id: "article_2dd65e7c"
title: "Building a Complete Personal Harness: LLM Wiki + Developer's Second Brain in Obsidian"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "best-practices"
tags: [obsidian, knowledge-base, agent-harness, second-brain]
summary: "You build a personal knowledge harness in Obsidian. You split the vault into strict zones with clear ownership rules. An LLM agent maintains the wiki zone while you drive the collaborative zone. You use a file system approach or plugins for integration."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

You build a personal knowledge harness in Obsidian. You split the vault into strict zones with clear ownership rules. An LLM agent maintains the wiki zone while you drive the collaborative zone. You use a file system approach or plugins for integration.

## Key Takeaways

- Divide the vault into four zones with strict write permissions.
- Keep Zone 1 immutable so the agent never edits original inputs.
- Let the agent own Zone 2 for concept pages and syntheses.
- Use Path 1 with direct filesystem and official skills as the best starting point.
- Require human confirmation before the agent writes to the wiki.
- Use git versioning as the primary safety net against agent mistakes.

## Techniques / Prompts Extracted

None identified.

## Full Content

# Building a Complete Personal Harness: LLM Wiki + Developer's Second Brain in Obsidian

> Source: https://medium.com/@roanmonteiro/building-a-complete-personal-harness-llm-wiki-developers-second-brain-in-obsidian-d7b61c7398ff
> Saved: 2026-06-17

A hands-on tutorial for setting up an Obsidian vault as an agent-maintained knowledge base, combining Karpathy's LLM Wiki pattern with a developer's second brain (ADRs, debriefs, projects). The core insight: split into two vaults and you lose cross-references; merge without discipline and it becomes garbage — the solution is strict zone separation enforced via CLAUDE.md.

## Vault Zones

- **Zone 0 — `CLAUDE.md`** (schema, not content): read every session, defines who can write where
- **Zone 1 — `raw/`** (your curated, immutable): web clips, papers, daily notes — agent NEVER edits this
- **Zone 2 — `wiki/`** (agent-maintained): concept pages, entity pages, syntheses, index — agent owns this, you rarely edit by hand
- **Zone 3 — `dev/`** (collaborative): ADRs, debriefs, projects, snippets — you drive, agent co-pilots

## Three Integration Paths

- **Path 1 — Direct filesystem + Steph Ango's official skills** ← recommended starting point; works offline, most debuggable, most portable
- **Path 2 — MCP via Local REST API plugin** (`127.0.0.1:27124`): unlocks Dataview, graph, palette commands; Obsidian must be open; `PATCH` preferred over `POST` due to overwrite bug in v3.6.x
- **Path 3 — `claude-obsidian` plugin**: 7 skills + 4 commands out of the box; quickest setup, least customizable

## Official Skills (kepano/obsidian-skills, 13.9k+ stars)

- `obsidian-markdown` — wikilinks, callouts, frontmatter (use always)
- `obsidian-bases` — `.base` files for dynamic tables/views
- `json-canvas` — canvas whiteboards (open JSON format)
- `obsidian-cli` — automate via `obsdmd` terminal commands
- `defuddle` — clean content extraction from URLs (strips ads/nav)

## Key Slash Commands

- `/wiki-ingest ` — fetch → save to `raw/clippings/` → identify concepts → **present plan and wait for confirmation** → execute
- `/wiki-query ` — grep candidates → focused read (max 10 files, wiki/ first) → answer with wikilink citations

## Critical Rules

- Agent presents plan before writing to wiki/ — human gate is mandatory
- ADRs follow MADR format in `dev/adr/ADR-NNNN-slug.md`; accepted ADRs are immutable except status change
- Debriefs are blameless; "Generalizable learning" section is the most important part
- `allowed-tools` in slash commands limits blast radius (no `Bash(rm:*)` = can't delete)
- Git versioning is the primary safety net — commit frequently, `git diff` catches agent mistakes
- Defense against prompt injection: CLAUDE.md rules + allowed-tools + plan review + git rollback

## Cost / Scale

- ~$20–50/month for 200–500 note vault with daily use
- Use `/wiki-query` (grep-first) rather than "read entire vault" to control token spend

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
