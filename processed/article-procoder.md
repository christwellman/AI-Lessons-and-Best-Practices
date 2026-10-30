---
id: "article_16823ab8"
title: "Procoder"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [agent-governance, workflow-enforcement, code-quality, senior-dev-layer]
summary: "Procoder is an engineering discipline layer for AI coding agents. It enforces a structured software development workflow with blocking controllers. The tool uses a P-CONTROL principle where the binary computes data, the agent reasons, and the agent changes the code."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Procoder is an engineering discipline layer for AI coding agents. It enforces a structured software development workflow with blocking controllers. The tool uses a P-CONTROL principle where the binary computes data, the agent reasons, and the agent changes the code.

## Key Takeaways

- AI coding agents often skip planning, testing, security checks, and review steps.
- Procoder uses blocking controllers to stop progression when specifications or tests fail.
- The tool follows the P-CONTROL principle so the binary never modifies source code directly.
- Procoder supports multiple coding agents through a single Go binary with no runtime dependencies.
- A self-learning loop records bugs and updates permanent rules or tests to prevent future failures.

## Techniques / Prompts Extracted

None identified.

## Full Content

I built Procoder: a senior developer layer for AI coding agents — and it replaces Superpowers, Ponytail and Serena in my workflow
Skill Share
r/claudeskills - I built Procoder: a senior developer layer for AI coding agents — and it replaces Superpowers, Ponytail and Serena in my workflow
I’ve been using coding agents heavily for a while now, and I’ve become convinced that the biggest problem isn’t their ability to write code anymore.

They’re actually getting very good at that.

The problem is everything around writing the code.

Understanding what should actually be built. Challenging an incomplete spec. Making a proper implementation plan. Keeping scope under control. Testing what was changed. Checking security and maintainability. Reviewing its own work. Making sure “done” actually means done. And learning from bugs instead of making the same class of mistake again three weeks later.

Basically, all the boring discipline you’d expect from a good senior developer.

I was already using tools like Superpowers, Ponytail and Serena to help with parts of this, and I liked a lot of what they did.

But I ended up with multiple tools, multiple sets of instructions, overlapping functionality and different concepts all trying to influence the same coding agent.

So I built Procoder.

And at this point, it’s become much more than the original idea.

Procoder is basically an engineering discipline layer around your coding agent.
Instead of:

prompt → code → "done"

I’m trying to enforce something much closer to:

understand → spec → plan → implement → test → check → review → fix → verify → release → learn

The important part is that a lot of this isn’t just another 2,000 lines of instructions telling the AI what it should do.

There are actual controllers that can refuse.

If the spec still has open questions, spec check can block.

If the implementation plan contains placeholders, plan check can block.

If acceptance criteria aren’t satisfied, the todo/story can’t close.

If tests weren’t actually executed, they’re not green.

If formatting, linting, secrets, CI, infra or documentation checks fail, the gate isn’t clean.

If something couldn’t be checked:

unchecked != passed.

And before a release, Procoder checks the version, changelog, git tree, quality gate and test suite before telling the agent it’s ready.

It doesn’t make the changes itself either.

Procoder follows a principle I call P-CONTROL:

Procoder computes → agent reasons → agent changes

The binary never silently modifies your source code behind the agent’s back.

It also replaces the three separate tools I was using before
I didn’t just take inspiration from Superpowers, Ponytail and Serena. My goal was to absorb the parts I found valuable so I wouldn’t need to run them alongside Procoder anymore.

From Superpowers, Procoder covers things like structured implementation planning, task classification, systematic debugging, evidence before declaring something done and TDD practices — but adds controllers that can actually refuse progression instead of only advising the agent.

From Ponytail, it incorporates things like the build ladder, deliberate technical-debt markers, over-engineering review and the idea of having one engineering instruction system that works across agents.

And from Serena, Procoder provides code intelligence through ctags + SCIP: symbol search, references, callers, impact analysis, unused symbols, entry points, cross-file rename and project memory — without needing to keep an MCP server running.

There are deliberate differences too. For example, I didn’t adopt Serena’s symbol-level write tools. Procoder can compute something like a rename and give the agent the diff, but the agent remains responsible for actually changing the code.

Then I went quite a bit further.
Procoder now has a complete quality chain around the agent:

spec interviews and validation

implementation planning

milestones, epics and user stories

sprint management with scope control and carry-over

acceptance-criteria-based TODOs

real test execution using the project’s native test runner

formatting across Go, Python, JS/TS, Rust, C/C++, Java, Kotlin, Swift, Ruby, Dart, C#, shell, etc.

linting and best-practice checks

secret scanning and security checks

dependency and maintainability checks

CI checks

Docker, Terraform, Kubernetes and Helm checks

documentation health

GitOps discipline

code indexing and symbol navigation

pre-PR self review

release control

technical debt tracking

codebase auditing/onboarding

But one of the parts I find most interesting is the self-learning loop.

Let’s say a bug gets through all of this and is found during review or after release.

Fixing that bug isn’t enough.

Procoder asks:

Why was this class of bug able to escape our process?

The lesson gets recorded, and the adaptation should become something permanent: a lint rule, review rule, regression test, rubric entry, etc.

So over time the engineering process itself should improve.

It’s also not tied to Claude Code.
I originally built around Claude Code, but I didn’t want my engineering workflow coupled to whichever coding agent happens to be best this month.

Procoder currently supports Claude Code, Cursor, Windsurf, Cline, Kilo Code, Roo, Kiro, Codex CLI, Copilot CLI, Gemini, OpenCode and anything that reads AGENTS.md.

It’s a single Go binary with no runtime dependencies, including no npm dependency and no network requirement at hook time, so it can also work in air-gapped environments.

Everything project-specific lives in .procoder/ as normal editable files, and the repository’s configuration always wins over Procoder’s defaults.

The project is completely open source under Apache 2.0:

https://github.com/azrtydxb/procoder

For Claude Code, getting started is:

/plugin marketplace add azrtydxb/procoder

/plugin install procoder

/procoder:init

I’m putting this out there because I think we’re reaching the point where the interesting problem with coding agents isn’t just:

“How do we make the model write better code?”

It’s:

“How do we give an autonomous coding agent the engineering discipline and guardrails of a good senior developer?”

That’s what I’m trying to build with Procoder.

I’d especially like feedback from people already using Superpowers, Ponytail, Serena, or people who’ve built elaborate CLAUDE.md / AGENTS.md workflows of their own.

What parts of your software development process do your coding agents still routinely skip, fake, forget, or get wrong?

Those are exactly the things I want Procoder to make enforceable.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
