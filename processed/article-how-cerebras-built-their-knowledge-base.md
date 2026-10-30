---
id: "article_d422ea20"
title: "How We Built Our Knowledge Base"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [knowledge-base, retrieval, slack, reranking, embeddings]
summary: "The internal knowledge base connects people and systems to useful information. The system extracts data from existing platforms without forcing migration. A hybrid search approach combines full-text search, embeddings, inverse document frequency, and age decay. An LLM distillation step normalizes Slack threads into structured documents before embedding."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

The internal knowledge base connects people and systems to useful information. The system extracts data from existing platforms without forcing migration. A hybrid search approach combines full-text search, embeddings, inverse document frequency, and age decay. An LLM distillation step normalizes Slack threads into structured documents before embedding.

## Key Takeaways

- The system extracts data directly from existing platforms without migration.
- A single Postgres table holds embeddings, summaries, and metadata.
- Full-text search catches exact tokens like error strings and host names.
- Embedding search connects paraphrases that share no vocabulary.
- Reciprocal rank fusion combines results from multiple parallel retrieval lists.
- Projects scope search results to specific teams and data sources.

## Techniques / Prompts Extracted

None identified.

## Full Content

# How We Built Our Knowledge Base

> Source: https://www.cerebras.ai/blog/how-we-built-our-knowledge-base
> Saved: 2026-08-10

Employees ask Cerebras's internal knowledge base more than 15,000 questions every day. It's become one of the most widely adopted internal tools at the company since launching 3 months ago — used by humans, automations, and agents.

With teams spanning data center operations, chip design, hardware, training, inference, and cloud platform, and hundreds of new employees joining every year, the same questions kept flooding Slack: "Where can I find X?" "Who is the expert in Y?" "What is Z?" Cerebras Knowledge was built to connect people and systems to useful information.

**Pipeline shape:** Sources (Slack, wiki, code, incidents) → LLM extractors (distillation) → embeddings (pgvector, 3072-dim, HNSW) → six retrieval lists run in parallel → fusion + rerank (RRF, K=60 → LLM rerank) → synthesis (answer + citations).

## Meeting data where it lives

Finding information inside an organization is hard because data is scattered across tools, and the "let's put everything in one platform" fix rarely works in practice. Information is generated wherever it's convenient: suggested edits in a doc, Slack threads, code references in GitHub, status metadata in Jira. Discussing a pull request in Google Docs would be a terrible experience.

So the team designed a system requiring minimal change to existing behavior — extracting data from each platform directly rather than forcing migration.

## Anatomy of a knowledge base

The knowledge base provides three things:

1. A platform for collecting and storing internal data.
2. A platform for querying that data.
3. A layer enforcing authentication and authorization, with auditing and analytics.

At the core is a single Postgres table holding embeddings, raw summaries, and metadata from many sources. The system continually ingests data and maintains a query-ready datastore. Every source — Slack threads, netlists, wiki pages, custom databases — lands in the same embeddings table, queryable through the same interface (document, embedding, metadata: source + timestamp), accessible via MCP, web UI, or agents. One connector per source; each defines what the data is, how to connect, and how often to fetch it.

## Slack

Slack was the most important — and hardest — source, since it's where the most up-to-date engineering discussions happen.

**Why plain embeddings weren't enough:**
- Information density varies enormously: "hey yeah sure mike" and a detailed kernel explanation are both messages.
- Message length skews results — shorter messages frequently beat longer, more detailed ones in cosine similarity.
- Meaning often depends on surrounding conversation.

**The hybrid approach — four techniques, each covering the others' weaknesses:**
- **Full-text search** catches exact tokens embeddings blur: error strings, flag names, host names. A pasted literal error message should win over "semantically similar" noise.
- **Embedding search** catches paraphrase — connecting "restore hangs after manifest load" to an answer about "checkpoint stalls on the NFS mount" that shares no vocabulary.
- **Inverse document frequency (IDF)** separates signal from filler. A short message with a rare config flag deserves to rank; "sounds good, thanks!" scores near zero once term rarity is weighted in.
- **Age decay** reflects that Slack answers expire — when two threads answer the same question, the newer one wins ties.

No single scorer is trusted alone; each produces its own ranked view, fused at query time (see Reranking below).

### Socket Mode ingestion

A Slack bot runs in Socket Mode, receiving every message event over a persistent WebSocket — real-time updates without polling and burning API rate limits. Each event is acknowledged immediately, deduplicated by stable event ID, and queued for ingestion.

The ingest consumer never saves a message in isolation — it resolves the full thread (parent + every reply) and re-fetches the whole conversation from the Slack API, writing it back as one row. A reply to an existing thread re-pulls the parent and siblings, so stored content, participants, and last-activity timestamp always reflect the complete conversation. Every channel is its own data source, allowing per-channel ingestion frequency tuning (e.g., a busy incident channel ingested more often).

### Threads and messages

Raw Slack text is keyword-searchable immediately via a Postgres full-text (GIN) index. For useful vector search, an LLM distillation step extracts structured data from the full thread:

- A one-line question an engineer would actually search for
- A short summary
- The resolution
- Systems and code references mentioned

Example: a thread about a checkpoint restore stall gets distilled into `{question, summary, resolution, systems: ["checkpoint restore", "NFS"], code_refs: ["CKPT_PREFETCH"]}`. This normalized document — not the raw transcript — is what gets embedded (question + summary + resolution + systems + code references), stored with source (`slack_thread`), source_id, a 3,072-dim embedding, and metadata (channel, authors, time). Accuracy increased significantly once the thread was normalized into a consistent format instead of embedding the raw transcript directly.

### Bursting

Even with thread-level summaries, important messages inside long threads sometimes weren't represented. A "burst" is a run of consecutive messages from the same author; individual bursts are embedded with the thread topic prepended as context, since the real answer sometimes lives in one tangent message whose vocabulary never made it into the summary.

To keep low-signal data out, a burst must clear a threshold before embedding:
- Contains a relatively rare token (IDF ≥ 4.0)
- Combined burst is at least 200 characters
- One or more messages in the burst have reactions (a social-proof boost)

Qualifying bursts are embedded and stored alongside the thread-level record.

## Code repositories

The team initially debated whether embedding code was even necessary — with tools like Claude Code, "grep is all you need" felt plausible. After research (including Cursor's findings on semantic search in large codebases) they decided to try it, across many internal repos, some larger than 40 GB. The main challenge was keeping embeddings current efficiently.

**CocoIndex** (an open-source document embedding framework specializing in codebases) was adopted. For each repo, code is split using language-specific regex boundaries ordered coarse to fine — trying class-level boundaries first, falling back to methods, then smaller blocks if a chunk is still too large. A single file may generate multiple embeddings at different specificity levels (file-level and function-level).

CocoIndex tracks sync metadata in Postgres, so on each commit it re-embeds only changed chunks rather than recomputing the whole repo — helped by sync state and embedding store living in the same database. As codebases grew, repository onboarding moved into config files teams submit themselves, including file-path allowlists/denylists.

## Custom data sources

Some teams already had their own databases and didn't want to migrate data into Slack or a doc system just to participate. Custom sources are handled as plugin scripts: a team opens a PR with a small Python module that reads from its system and emits rows shaped like the embeddings table, plus a matching data source entry. As long as it writes into the shared schema, the rest of the stack works unchanged — no special-casing elsewhere.

## Planning and tool fan-out

For every query, a short planning pass has an LLM decide which tools/sources likely matter. Main tools:

- `subsystem_index` — per-file LLM summaries
- `search` — the unified vector pipeline across Slack, wiki, code, and other sources, merged and reranked internally
- `search_slack` — direct Slack retrieval
- `search_code` — ripgrep over source repos
- `recent_prs` — recent pull requests relevant to the question
- `who_knows` — people with demonstrated expertise on a topic

The planner works over a compact description of what's indexed (projects, sources per project, what each source answers well). Given the query and active scope, it emits tool selections the executor fans out in parallel, normalizes into a common evidence format, and passes to a final synthesis LLM.

## Reranking

A document can rank high just by sharing vocabulary with the query while answering a different question. Before reranking, incompatible result lists are combined via **reciprocal rank fusion (RRF)**: for every document, add `weight / (60 + rank)` for each list it appears in (default weight 1.0, smoothing constant 60). The smoothing constant makes consensus matter more than one strong vote — a document ranking near the top across several retrievers can beat one that's #1 in only one list.

Duplicate chunks are merged to one source, per-file result caps applied, yielding a diverse top twenty. The original query plus those candidates go to a small reranker model, which scores each 0–10; the top ten are kept.

Once ranking is final, context is added back to winners — e.g., matching a wiki section pulls in the two neighboring sections so headings, preconditions, and caveats split apart by chunking aren't lost. The output of `search` is a rich evidence packet: fused across retrievers, deduplicated at the source level, reranked against the actual question, then expanded with surrounding context.

## MCP

The MCP integration exposes retrieval building blocks as direct tools rather than hiding them behind one "answer this question" endpoint — intentionally simple and as LLM-free as possible so clients can query cheaply and quickly. Each tool maps to one retrieval primitive (`search_slack`, `search_code`, `search`, `who_knows`) with narrow, structured, stable inputs/outputs, callable from any client or agent without embedding extra orchestration logic in the tool itself.

Most tools run one query pipeline (vector search, lexical search, ripgrep), apply lightweight scoring heuristics, and return raw evidence rows. Claude Code, or any MCP-compatible agent, becomes the orchestration engine — deciding which tools to call, in what order, and how to assemble results. The retrieval layer itself doesn't depend on those LLM decisions to serve requests.

## Web UI

The web UI uses the same tools, but wraps them in a complete pipeline that runs end to end per question, owned by the UI agent:

- **Planner** — a lightweight LLM pass inspects the query and active project, chooses which retrieval tools to invoke (`search`, `search_slack`, `subsystem_index`, etc.)
- **Executor** — fans those calls out in parallel, gathers results, normalizes into a shared evidence schema with scores, recency, and source hints
- **Synthesis** — a final LLM pass takes the typed evidence bundle and original question, producing the answer with citations, caveats, and cross-source synthesis

From the user's perspective it's just "ask a question, get an answer" — under the hood it's the same planner → executor → synthesizer pattern MCP clients can recreate explicitly.

## Organization

As the corpus grew, "search everything everywhere" stopped being useful — compiler-team engineers didn't want infrastructure runbooks in their results, and vice versa.

**Projects** are the primary way to scope search: a named bundle of data sources (specific Slack channels, code repos, internal databases, doc spaces) relevant to a team or initiative. Projects are lightweight — the same data source (e.g., a shared incidents channel or central platform repo) can be referenced by multiple projects instead of being duplicated.

During onboarding, users pick or create a default project matching how they work (e.g., ML training infrastructure, Compiler, Data Center Operations). That default scopes queries automatically, so a new engineer gets high-signal answers without first learning which channels, repos, or doc spaces matter.

## Final thoughts

The knowledge base works because it meets people where information already lives instead of forcing everything into one rigid system. Combining multiple search techniques surfaces evidence quickly, producing a search experience flexible enough for real company data but structured enough to stay useful as Cerebras keeps growing.

## References

1. Malkov and Yashunin, [Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs](https://arxiv.org/abs/1603.09320), arXiv:1603.09320 / IEEE TPAMI 2018.
2. Anthropic, [Introducing Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval), 2024.
3. Cormack, Clarke, and Büttcher, [Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods](https://dl.acm.org/doi/10.1145/1571941.1572114), SIGIR 2009.
4. Li et al., [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://arxiv.org/abs/2501.05366), arXiv:2501.05366, 2025.
5. Anthropic, [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp), 2025.
6. Liu et al., [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172), arXiv:2307.03172, 2023.
7. Anthropic, [Use XML Tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags).
8. Salesforce/Slack Engineering, How Slack AI Processes Billions of Messages.
9. Improving Agents, Best Nested Data Format.
10. Cursor, [Improving Agent with Semantic Search](https://cursor.com/blog/semsearch), 2025.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
