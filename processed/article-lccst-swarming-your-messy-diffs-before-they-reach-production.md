---
id: "article_6a864342"
title: "Lccst: Swarming Your Messy Diffs Before They Reach Production."
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "skills"
tags: [git, code-quality, mcp, architecture]
summary: "Locust is an AI skill that acts as a workspace gatekeeper. It enforces architectural cohesion and SOLID invariants through a lean execution protocol. The system decomposes changes into isolated, test-verified, atomic Git commits."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Locust is an AI skill that acts as a workspace gatekeeper. It enforces architectural cohesion and SOLID invariants through a lean execution protocol. The system decomposes changes into isolated, test-verified, atomic Git commits.

## Key Takeaways

- Locust uses a flat 3-step execution path to remove meta-cognition tax.
- The tool enforces strict type-safety, anti-god-object rules, and defensive engineering.
- It uses locality clustering to group workspace diffs by functional domain boundaries.
- The system prioritizes structural integrity and test verification over raw execution speed.
- The skill uses a single-file SKILL.md and index.js Model Context Protocol.

## Techniques / Prompts Extracted

None identified.

## Full Content

lccst: Swarming your messy diffs before they reach production.
Skill Share
r/claudeskills - lccst: Swarming your messy diffs before they reach production.
Been working on this AI skill for a bit now. I wanted something that would make open weight models much better code quality output wise. I have not got the chance to test on frontier models but the results so far seem promising.

There is a benchmarking background where I runned some Opencode Zen models pre deepseek price increase.

The text below is extracted from the README. Yes there are a lot of similar options out there but I wanted to make something not too bloated and geared towards my own use case.

The skill is FOSS, the repo link can be found below. Hope you find it useful :D

Overview
It basically functions as a deterministic workspace gatekeeper that enforces architectural cohesion and SOLID invariants through a lean execution protocol. Decomposes codebase changes into isolated, test-verified, atomic Git commits with zero meta-cognition tax.

Locust operates as a structural integrity guardian for codebase health, test coverage, and architectural boundaries -- built to put your preferences first.

"Swarming your messy diffs before they reach production."

The execution model is a flat 3-step path: wipe stale artifacts, seed via /init, then generate application files directly. No multi-phase loops or phase-checking pauses. Architectural guardrails (anti-god-object, strict typing, defensive engineering) and ecosystem discovery (Tooling Ladder, manifest scanning) remain active during code generation to enforce quality.

Operational Persona: The Virtual Staff & Release Engineer
Within your workspace ecosystem, Locust acts as a hybrid Staff Architect and hyper-vigilant Release Engineer. It does not just facilitate changes; it ensures every modification complies with long-term engineering health. Like a disciplined peer, it actively prevents the creation of anti-patterns, automates versioning overhead, and refuses to stage or commit code that drops below strict quality thresholds.

Ecosystem Placement: The Quality Counter-Weight
While the modern AI engineering space is heavily saturated with tools focusing strictly on compression and cost-reduction, Locust provides the missing philosophical balance. It is built to run standalone or alongside token-cutters.

Tool Layer	Focus	Tactical Mechanism
Ponytail	Code Minimisation	Prevents agent boilerplate bloat.
Headroom	History Reduction	Trims context logs and chat data.
Caveman	Output Compression	Strips syntax token overhead.
Locust (LCCST)	Payload Integrity	Enforces typing, lints, and tests.
The Token Investment Philosophy
The project name itself embodies this duality: LCCST stands as a direct pun on Low Cost asset management while algorithmically executing Locality Clustering over your workspace tree.

Tools like Ponytail stop the AI from writing too much code, but they cannot stop it from breaking your architectural boundaries. Locust treats tokens as strategic capital -- invested into the Tooling Ladder to eliminate the exponentially higher downstream costs of debugging broken production builds, untangling messy Git histories, or fixing silent runtime type failures.

Core Philosophy
UNIX philosophy over framework: A simple single-file SKILL.md and index.js Model Context Protocol (MCP), nothing more required. Over-engineering is bad for auditing, adds technical debt and needless complexity for nothing.

User Conventions First: The workspace's existing patterns, manifest-declared commands, and your explicit preferred design patterns always take priority when defining application payloads. However, the core safety gates of the pipeline -- including atomic hunk isolation, the Tooling Ladder, and strict test-pass verification -- are non-negotiable workspace invariants designed to prevent structural regressions.

Streamlined Initialisation: Use the /init command on startup to kick off immediate, automated codebase scans, helping you audit repository health and catch architectural documentation gaps before any changes begin.

Interactive Engagement Loop: No abrupt dead ends. The system maintains continuous, collaborative dialogue -- prompting you for confirmations, staging approvals, or clarifying implementation paths.

Proactive Semantic Discovery & Testing: Leverages Language Server Protocol (LSP) data, Tree-sitter AST queries, and native testing frameworks to dynamically trace downstream side-effects.

Ecosystem-Native Architecture: Enforces strict type-safety boundaries, modern project layout orchestrators, and single-responsibility interfaces (while dynamically allowing cohesive multi-method structures like unified HTTP handlers).

Defensive Engineering & Compliance: Applies validation boundaries and security controls proportionally -- only where the domain justifies them. Filters token overhead, audits package licences, and automatically adapts to both monolithic and modular/versioned changelog layouts using SemVer rules.

Quality over Velocity: Prioritise structural integrity and complete test verification over raw execution speed. Version 3.1.0 strips the meta-cognition tax by replacing multi-phase execution loops with a flat 3-step path. Token discipline is enforced at the output level, not as internal reasoning rules.

Granularity over Convenience: Reject the temptation to bundle multi-domain fixes into single execution blocks. Locust applies strict Locality Clustering to group workspace diffs by their functional domain boundaries. The overhead of creating multiple atomic commits is deliberately chosen to guarantee easy code rollbacks and crystal-clear repository history.

Proportionality over Boilerplate: Implement the fewest lines that preserve correctness, scalability, and adaptability. Scaffolding that exceeds the domain's actual risk is over-engineering -- a correctness defect, not a virtue.

Links
GitHub Repository:https://github.com/bladeacer/lccst

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
