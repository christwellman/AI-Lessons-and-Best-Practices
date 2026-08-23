---
id: "article_1284a7e5"
title: "18 Claude Settings That Change Everything"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "best-practices"
tags: [claude-settings, context-management, prompt-caching, api-optimization]
summary: "This document lists eighteen settings for Claude, Claude Code, and the API. These settings help users manage memory, context tokens, prompt caching, and cost. Most users do not use these settings by default."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

This document lists eighteen settings for Claude, Claude Code, and the API. These settings help users manage memory, context tokens, prompt caching, and cost. Most users do not use these settings by default.

## Key Takeaways

- Enable project-scoped memory and exclusion lists in Claude.ai to protect private topics.
- Use light extended thinking by default in Claude.ai.
- Keep integrations unloaded in Claude Code to save context tokens.
- Set per-project model overrides to match the task complexity.
- Place prompt caching breakpoints after the stable system prompt to save money.

## Techniques / Prompts Extracted

-  CODE0
-  CODE1
-  CODE2
-  CODE3
-  CODE4
-  CODE5
-  CODE6
-  CODE7
-  CODE8

## Full Content

# 18 Claude Settings That Change Everything

> Source: https://agent-cookbook.com/tutorial/18-claude-settings-that-change-everything-14-are-hidden-3-clicks-deep-4-arent-in
> Saved: 2026-07-31

> [!note]
> This is a third-party blog roundup (agent-cookbook.com), not official Anthropic documentation. Specifics — exact menu paths, numbers, and undocumented settings — are unverified; treat as a checklist to explore rather than a confirmed reference.

A punch list of 18 Claude/Claude Code/API settings the author says most people never touch, split into Claude.ai (8), Claude Code (7), and API/Console (3).

Key points:
- **Claude.ai:** turn on project-scoped Memory plus an exclusion list (topics like medical/salary that shouldn't leak across chats), use the inline "forget what you remembered about X" command, set Extended Thinking to "Light" by default, create Custom Styles as reusable output contracts (not just tone), fill in every Project's "instructions" field, switch web search citations to Footnotes mode if you ever copy answers elsewhere, and periodically prune Cowork's trusted-folders list.
- **Claude Code (`~/.claude/settings.json`):** use `enabledPlugins` and `mcpServers..enabled: false` to keep integrations installed but unloaded (each active one costs real context tokens); set per-project `model` overrides (haiku for docs, sonnet for infra, opus for core logic); a `hooks.SessionStart` hook can load only the current git branch's context file; `disableAllHooks: true` is a one-flip panic switch for diagnosing misbehaving hooks; raise `cleanupPeriodDays` from the 30-day default to keep more session history for memory/search.
- **API/Console:** `cache_control` breakpoints should sit right after the stable system prompt (not after the dynamic user message) to get real cache-hit savings — the article claims this cut one person's bill from $340/mo to $87/mo; `inference_geo` (US-only residency) reportedly adds a 10% premium on Opus-tier calls and should only be set if actually contractually required; set workspace- and feature-level rate limits separately so one runaway batch job can't starve a customer-facing feature.
- The author explicitly says four other toggles (Adaptive Reasoning override, skill auto-activation, mobile-to-desktop dispatch, per-workspace max_tokens ceiling) weren't worth recommending as defaults after testing.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
