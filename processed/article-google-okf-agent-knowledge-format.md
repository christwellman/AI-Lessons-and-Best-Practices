---
id: "article_e1e5cb01"
title: "Google Cloud Released OKF — Think MCP, But for Knowledge Instead of Tools"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [knowledge-format, agent-context, markdown, graph]
summary: "Google Cloud publishes the Open Knowledge Format version zero point one. This format uses markdown files to store static knowledge for agents. The system forms a knowledge graph with standard links. Agents read these files to get context without loading all data."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Google Cloud publishes the Open Knowledge Format version zero point one. This format uses markdown files to store static knowledge for agents. The system forms a knowledge graph with standard links. Agents read these files to get context without loading all data.

## Key Takeaways

- An OKF bundle is a directory of markdown files.
- Each file represents one concept and uses a YAML frontmatter block.
- Concepts cross link to form a knowledge graph.
- The only required frontmatter field is a non empty type.
- Consumers must tolerate unknown types and broken links.
- Use an optional index file for progressive disclosure.

## Techniques / Prompts Extracted

None identified.

## Full Content

# Google Cloud Released OKF — Think MCP, But for Knowledge Instead of Tools

> Source: https://www.reddit.com/r/WebAfterAI/comments/1u6mge2/google_cloud_just_released_okf_think_mcp_but_for/
> Saved: 2026-07-31

On June 12, 2026, Google Cloud published the Open Knowledge Format (OKF) v0.1 — not a runtime, SDK, or MCP competitor, but a plain convention for writing static knowledge (tables, metrics, runbooks, APIs) as markdown files so any agent can read it.

Key points:
- An OKF "bundle" is just a directory of markdown files. Each file is one "concept," identified by its file path (`tables/orders.md` → concept `tables/orders`), with a small YAML frontmatter block plus a markdown body. Concepts cross-link via normal markdown links, forming a knowledge graph.
- The only required frontmatter field is a non-empty `type`. `title`, `description`, `resource`, `tags`, `timestamp` are recommended but optional; consumers must tolerate unknown types, missing fields, and even broken links.
- Feels similar to existing patterns like Obsidian vaults, `AGENTS.md`, or a repo of `index.md` notes an agent reads first — OKF just standardizes the shared rules so different tools can read the same bundle without a translation layer.
- Status check: this is v0.1, labeled Draft, with only Google's two reference implementations (a BigQuery-to-OKF enrichment agent, and a self-contained HTML bundle visualizer) plus three sample bundles. Useful today as a tidy, portable way to version-control agent context; the "universal lingua franca" ambition depends on adoption that hasn't happened yet.
- Repo: `github.com/GoogleCloudPlatform/knowledge-catalog` — spec (`okf/SPEC.md`) fits on one page.

## Three ways to use it

1. **Turn tribal knowledge into a bundle your agent reads first** — one concept file per gnarly table/metric/runbook, cross-linked, with your agent instructed to consult the bundle before acting. Same value (and limits) as a well-kept docs folder — nothing reads OKF automatically, you have to wire your agent to load it.
2. **Generate a bundle from a database/codebase, then ground it** — mirrors Google's reference pattern: draft one concept per table/module, then run a second pass adding citations back to authoritative sources. Caution: a model documenting a schema will confidently invent wrong column meanings/join keys — never ship generated concepts unreviewed, and treat citations as required even though the spec makes them optional.
3. **Consume a bundle without blowing the context window** — use an optional `index.md` per directory (plain listing, no frontmatter) so an agent navigates the graph via progressive disclosure instead of swallowing the whole folder. Only helps if your retrieval step actually reads the index first rather than globbing every `.md` file.

Recommended starting point: hand-author a small 5-file bundle for one messy corner of a system (workflow 1) before investing in generation-at-scale or a consumption pipeline.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
