---
id: "article_7ee39bf1"
title: "What nobody tells you about writing agent skills (PostHog)"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "skills"
tags: [agent-skills, progressive-disclosure, skill-maintenance, prompt-engineering]
summary: "PostHog shares five lessons on writing agent skills that work. The lessons cover progressive disclosure, avoiding over-specification, preventing skill rot, asking the agent for feedback, and choosing when to write a skill."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

PostHog shares five lessons on writing agent skills that work. The lessons cover progressive disclosure, avoiding over-specification, preventing skill rot, asking the agent for feedback, and choosing when to write a skill.

## Key Takeaways

- Agents have limited context. Load skill information only when relevant.
- Write skill names and descriptions to show when the agent must use them.
- Do not write overly prescriptive steps. Define goals, constraints, and hidden context instead.
- Separate durable structure from volatile content to prevent skill rot.
- Ask the agent questions to improve skills based on past runs.
- Only write skills for repetitive tasks that agents handle badly by default.

## Techniques / Prompts Extracted

- Audit existing skills through a progressive-disclosure lens (are names/descriptions discoverable? properly split?).
- Rewrite skills to be less prescriptive — give the goal and tools, not the exact path.
- When patching a skill ad hoc, look for a way to prevent future rot instead (point to a URL, regenerate a section).
- Ask an agent to review your last 30 days of work and surface skill candidates worth packaging (with a full prompt template provided in the source).

## Full Content

# What nobody tells you about writing agent skills (PostHog)

> Source: https://x.com/posthog/status/2084345938089316582
> Saved: 2026-08-06

PostHog has published 226 skills internally (187 SKILL.md files across 28 products) and shares five hard-won lessons on writing skills that actually work for agents.

## Key points

- **Master progressive disclosure.** Agents only have so much context — skills should load info only when relevant, not dump everything up front. The skill's name/description should signal *when* to reach for it (not just what it is); PostHog's SQL skill example: first sentence = when to load, middle = when to use, last = what it does. Too many skills or bloated descriptions hurt agent performance (cites a Databricks finding that agents increasingly pick the wrong skill as more are added). Sections within a skill should also route to sub-files (schemas, examples) rather than inlining everything.

- **Skills aren't just code — don't over-specify.** Overly prescriptive step-by-step skills break the moment reality doesn't match. Be precise about: the *goal* (what "done" looks like, with self-verification steps), *constraints/guardrails*, and *context the agent can't derive* (data locations, which tool to use). Stay ambiguous about: exact steps, anticipated failure modes, and runtime specifics (line numbers, file lists, versions) — let the agent's intelligence handle those.

- **Skills rot — prevent it proactively.** Three principles: (1) split durable structure from volatile content — hand-write what rarely changes, reference what drifts; (2) point to a single source of truth (e.g., docs URLs) rather than duplicating content; (3) regenerate skills from a stable base rather than patching repeatedly, which clouds focus over time. PostHog's "context mill" pipeline (source docs → assembly → versioned release) automates this at scale.

- **Ask the agent questions instead of just issuing demands.** Before/after building a skill, ask: "What can you do to help?", "What do you need to do better?", "Based on the last run, how can this skill improve?" The agent knows things you don't — available tools, context access, what broke last run.

- **Not everything deserves a skill.** Costs (context + maintenance) mean you should only write one for work that: (1) you do repeatedly — "have you done it 3 times and will you do it 3 more?"; (2) agents handle badly by default; (3) needs context models don't have out of the box (e.g., nested/non-obvious data schemas); (4) can run on autopilot as a scheduled loop.

## Try-this prompts included in the piece

- Audit existing skills through a progressive-disclosure lens (are names/descriptions discoverable? properly split?).
- Rewrite skills to be less prescriptive — give the goal and tools, not the exact path.
- When patching a skill ad hoc, look for a way to prevent future rot instead (point to a URL, regenerate a section).
- Ask an agent to review your last 30 days of work and surface skill candidates worth packaging (with a full prompt template provided in the source).

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
