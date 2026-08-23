---
id: "article_b1b4de17"
title: "Management as AI Superpower"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "best-practices"
tags: [management, delegation, agentic-work, prompt-engineering]
summary: "Management skills drive success with AI agents more than clever prompts. Users trade human baseline time against probability of success and AI process time. Subject-matter experts use clear goals, evaluation, and feedback to guide AI tools."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Management skills drive success with AI agents more than clever prompts. Users trade human baseline time against probability of success and AI process time. Subject-matter experts use clear goals, evaluation, and feedback to guide AI tools.

## Key Takeaways

- Management and subject-matter expertise help users guide AI tools effectively.
- Delegation balances human time, success probability, and AI process time.
- Clear instructions and fast evaluation reduce wasted AI attempts.
- Traditional frameworks like requirements documents translate well into AI prompts.
- Abundant AI capability makes knowing what to ask for the scarce resource.

## Techniques / Prompts Extracted

None identified.

## Full Content

# Management as AI Superpower

> Source: https://www.oneusefulthing.org/p/management-as-ai-superpower
> Saved: 2026-08-10
> Author: Ethan Mollick (Jan 27, 2026)

## The experiment

Mollick ran a 4-day "build a startup from scratch" class at Wharton for executive MBA students — mostly non-coders juggling jobs as doctors, managers, and leaders. Using Claude Code and Google Antigravity for prototypes, plus ChatGPT/Claude/Gemini for idea generation, market research, positioning, pitching, and financial modeling, the teams got roughly an order of magnitude further in a couple of days than a full pre-AI semester used to produce — working core features (not just mockups), diverse ideas, and sharp market analysis. Lowering the cost of pivoting also let teams explore multiple directions instead of locking in early.

The surprising finding: it wasn't clever prompting that drove the results. It was that students already had management and subject-matter expertise — they knew how to tell the AI what they wanted.

## The equation of agentic work

Delegating to AI is a tradeoff across three variables:

1. **Human Baseline Time** — how long the task would take you to do it yourself
2. **Probability of Success** — how likely the AI is to meet your bar on a given attempt
3. **AI Process Time** — how long it takes to prompt, wait for, and evaluate the AI's output

You're trading "doing the whole task" against "paying the overhead cost" (possibly repeatedly, until the output is acceptable). The higher the Probability of Success, the fewer times you pay that overhead, and the more worth it delegation becomes. A task that takes an hour to do yourself but 30 minutes to check an AI attempt on is only worth delegating if success probability is high; a 10-hour task can justify several hours of back-and-forth with the AI even at lower success odds.

**Real-world evidence — OpenAI's GDPval study:** experienced professionals across fields (finance, medicine, government) were benchmarked against AI on real work, with expert judges scoring the results. Human Baseline Time averaged 7 hours per task. Early on, judges favored human work most of the time; by GPT-5.2, the model tied or beat human experts roughly 72% of the time, with AI Process Time (prompting + an hour of human review) far below the 7-hour baseline — netting real average time savings even accounting for cases where the AI failed and the task had to be redone by hand.

## Delegation as the new prompting

Three levers increase the Probability of Success and cut AI Process Time, and all of them are amplified by subject-matter expertise:

- **Better instructions** — clear goals the AI can execute against
- **Better evaluation and feedback** — fewer wasted attempts before the output is right
- **Faster ways to judge whether an attempt succeeded** — less time spent reviewing

When there's no specific target in mind, today's models can improvise impressively on their own (Mollick cites generating a full old-school adventure game — art, puzzles, and all — from a single open-ended prompt). But real delegation usually means you *do* have a specific outcome in mind, and that's where communication gets hard.

This is an old problem, not a new one — every field already has paperwork for it: software's Product Requirements Documents, film's shot lists, architecture's design intent documents, the Marine Corps' Five Paragraph Order (situation, mission, execution, administration, command), consulting engagement scopes. All of these translate well as AI prompts because they answer the same underlying questions: what are we trying to accomplish and why, where does delegated authority end, what does "done" look like, what specific and interim outputs are needed, and what should be checked before calling it finished. Specify these well and the AI — like a human report — is far more likely to deliver.

## Managing agents

Mollick notes that engineers at major AI labs increasingly describe their jobs as shifting from writing code to managing AI agents — coding was first because its outputs are cleanly verifiable (it either runs or it doesn't), but he expects the same shift elsewhere.

His framing: working with AI agents draws on Management 101 skills — explaining what you need, giving effective feedback, designing ways to evaluate work — arguably easier than crafting clever prompts, because it resembles working with people. The twist is that management has always assumed scarcity (you delegate because you can't do everything yourself and talent is expensive); AI flips that — capability is now abundant and cheap, and the scarce resource is knowing precisely what to ask for.

His students succeeded not because they were AI experts, but because years of scoping problems, defining deliverables, and recognizing a flawed financial model or medical report in their own fields gave them ready-made frameworks that doubled as prompts. The "soft skills" turned out to be the load-bearing ones — his read is that the people who thrive in an agentic-AI world will be the ones who know what "good" looks like and can articulate it clearly enough for an AI to deliver it.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
