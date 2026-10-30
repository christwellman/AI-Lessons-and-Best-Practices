---
id: "article_b7d1bce3"
title: "My AGENTS.md file for building plans you actually read"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [planning-loop, ai-coding, agent-workflow, code-generation]
summary: "Use a four step planning loop to improve artificial intelligence code generation. Plan the approach with the artificial intelligence before you write any code. Execute the plan, test the result, and commit the code. This method stops hallucinations and makes the code better."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Use a four step planning loop to improve artificial intelligence code generation. Plan the approach with the artificial intelligence before you write any code. Execute the plan, test the result, and commit the code. This method stops hallucinations and makes the code better.

## Key Takeaways

- Plan the software approach with the artificial intelligence before you write code.
- Execute the task by asking the artificial intelligence to write code that matches the plan.
- Test the code together with unit tests or manual quality assurance.
- Commit the code and start the cycle again for the next piece.
- Planning forces clarity and stops the artificial intelligence from guessing your needs.

## Techniques / Prompts Extracted

-  CODE6
-  CODE2
-  CODE0
-  CODE3
-  CODE4
-  CODE5
-  CODE1

## Full Content

# My AGENTS.md file for building plans you actually read

Most developers are skeptical about AI code generation at first. It seems impossible that an AI could understand your codebase the way you do, or match the instincts you've built up over years of experience.

But there's a technique that changes everything: the planning loop. Instead of asking AI to write code directly, you work through a structured cycle that dramatically improves the quality of what you get.

This approach transforms AI from an unreliable code generator into an indispensable coding partner.

## The Plan Loop: A Four-Step Process

Every piece of code now goes through the same cycle.

![Plan Loop Diagram](https://res.cloudinary.com/total-typescript/image/upload/v1768312499/ai-hero-images/xovcskktfuk5pii70fxe.png)

**Plan** with the AI first. Think through the approach together before writing any code. Discuss the strategy and get alignment on what you're building.

**Execute** by asking the AI to write the code that matches the plan. You're not asking it to figure out what to build—you've already done that together.

**Test** the code together. Run unit tests, check type safety, or perform manual QA. Validate that the implementation matches what you planned.

**Commit** the code and start the cycle again for the next piece.

## Why This Matters

This loop is completely indispensable for getting decent outputs from an AI.

If you drop the planning step altogether, you're really hampering yourself. You're asking the AI to guess what you want, and you'll end up fighting with hallucinations and misunderstandings.

Planning forces clarity. It makes the AI's job easier and your code better.

## Rules for Creating Great Plans

Here are the key rules from my `CLAUDE.md` file that make plan mode effective:

```md
## Plan Mode

- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.
```

These simple guidelines transform verbose plans into scannable, actionable documents that keep both you and the AI aligned.

Copy them into your `CLAUDE.md` or `AGENTS.md` file, and enjoy simpler, more readable plans.

Or, run this script to append them to your `~/.claude/CLAUDE.md` file:

```bash
mkdir -p ~/.claude && cat >> ~/.claude/CLAUDE.md << 'EOF'

## Plan Mode

- Make the plan extremely concise. Sacrifice grammar for the sake of concision.
- At the end of each plan, give me a list of unresolved questions to answer, if any.
EOF
```

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
