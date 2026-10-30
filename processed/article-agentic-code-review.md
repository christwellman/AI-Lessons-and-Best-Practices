---
id: "article_bf70ade9"
title: "Agentic Code Review"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "best-practices"
tags: [agentic-code-review, ai-coding-bottleneck, pull-request-management, engineering-process]
summary: "AI tools increase code volume but delivered value stays low. Reviewers now face high code churn and missing intent. Teams must tier review effort by risk and capture agent reasoning in decision logs."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

AI tools increase code volume but delivered value stays low. Reviewers now face high code churn and missing intent. Teams must tier review effort by risk and capture agent reasoning in decision logs.

## Key Takeaways

- Four studies show AI boosts raw output four times but real value grows only ten to twelve percent.
- Code churn, incident rates, and unreviewed pull requests increase sharply.
- Base review depth on blast radius, code lifespan, and team size.
- Capture agent reasoning in a decision log to help reviewers.
- Run two different AI reviewers to catch more distinct bugs.
- Humans shift focus from reading every diff to owning accountability.
- Require intent statements and test output before you review code.

## Techniques / Prompts Extracted

None identified.

## Full Content

# Agentic Code Review

> Source: https://addyosmani.com/blog/agentic-code-review/
> Saved: 2026-07-31

Addy Osmani argues that as coding agents get better and faster, the engineering bottleneck has shifted from writing code to reviewing it — and most teams haven't adjusted their process to match. 2026 data (Faros AI, CodeRabbit, GitClear, GitHub) all point the same direction: AI massively increases code volume and churn, but delivered value barely moves, and a growing share of PRs merge with zero human review.

Key points:
- Four independent 2026 studies agree: AI coding boosts raw output ~4x but real delivered value only ~10-12%; code churn, incident rates, and defect rates are all sharply up, and PRs merging with zero review rose ~31%.
- How much review a change needs depends on blast radius, how long the code lives, and how many people need to understand it — solo/no-user projects can lean on tests and defer deep review; large teams with many users need the full tiered process.
- The real shift: an agent's reasoning (why it made a choice) is usually discarded once the diff is produced, so reviewers are reconstructing intent that was never written down. Capturing that reasoning as a decision log largely fixes this.
- Running two AI reviewers with different designs (e.g., Greptile + Sentry Seer) catches far more distinct bugs than any single tool — in one 146-PR study, no two of four reviewers ever flagged the same line.
- The human role is moving "up" from reading every diff to owning accountability, judging whether a change is even the right one to build, and gating high-blast-radius paths — not disappearing, but changing shape.
- Practical recommendations: tier review effort by risk not by author, fast-fail large/sprawling agent PRs before sinking review time in, require evidence (intent statement, test output) before reviewing, keep PRs small, and scrutinize test-file changes especially closely (agents sometimes "fix" a broken test by rewriting the assertion).

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
