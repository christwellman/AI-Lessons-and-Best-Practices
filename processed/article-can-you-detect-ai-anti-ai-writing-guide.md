---
id: "article_ad7f995e"
title: "Can You Detect AI? (Anti-AI Writing Guide)"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "prompts"
tags: [anti-ai, prompt-engineering, writing-style, content-creation]
summary: "AI writing detectors use pattern matching to find common stylistic habits in large language models. Writers bypass these detectors by changing sentence length, removing stock phrases, and reducing punctuation marks like em dashes. Specific word choices and uniform positivity also signal machine-generated text."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

AI writing detectors use pattern matching to find common stylistic habits in large language models. Writers bypass these detectors by changing sentence length, removing stock phrases, and reducing punctuation marks like em dashes. Specific word choices and uniform positivity also signal machine-generated text.

## Key Takeaways

- AI detectors measure pattern matches rather than semantic depth.
- Mix sentence lengths and paragraph sizes to avoid low burstiness.
- Remove common AI filler words like delve, tapestry, and realm.
- Limit em dashes and avoid bold-first list items.
- Add contractions, named entities, and specific numbers to sound human.

## Techniques / Prompts Extracted

- Answer by adhering to ADS-STE100 Simplified Technical English without having to explain that you will adhere to this writing style

## Full Content

# Can You Detect AI? (Anti-AI Writing Guide)

> Source: https://ruben.substack.com/p/how-to-bypass-ai-detectors
> Saved: 2026-08-10
> Author: Ruben Hassid (Jul 22, 2026) — paid/subscriber post

> [!note]
> This is a paid Substack post. Saved below as a condensed reference/summary rather than a full reproduction, per copyright caution — go to the source link for the complete piece (including the author's Pangram testing walkthrough and downloadable "anti-ai" Claude skill).

## Overview

Substack partnered with Pangram, an AI-detection tool, to fight "AI slop." The author spent hours (and real money in Claude Code credits) trying to beat Pangram and found it's genuinely hard to fool with lazy prompting — but a small formatting tweak (e.g., swapping an em dash for a colon) flipped a "100% AI-generated" verdict to "100% human-generated" in his test. His takeaway: AI detectors are pattern-matching against known AI stylistic tics, not a deep semantic judge — OpenAI itself disbanded its own AI-detection team because it didn't work reliably. Short text and heavily-styled prompts both erode detector accuracy. Roughly 53.7% of long-form LinkedIn posts (100+ words) in 2025 were estimated to be AI-generated, much of it low-effort ("workslop").

## The tells: structure & rhythm

- **Low burstiness** — uniform 15–20 word sentences, rectangular paragraphs. Fix: mix a ≤6-word sentence with a 25+-word one; vary paragraph length; allow one single-line paragraph max.
- **Fractal summaries** — previews/recaps at every level ("In this section we'll…" / "…as we've seen"). Delete.
- **Signposted conclusion** — "In conclusion/Overall," + restatement + uplift ("Despite the challenges, the future is bright"). Delete; end on the last concrete point instead.
- **Pep-talk ending** — "As we move forward, embracing X will be key." Delete on sight.
- **Prompt echo** — "This essay will explore…" Delete.
- **Listicle in a trenchcoat** — "The first reason is… The second reason is…" Merge into flowing argument.
- **Uniform staccato** — "X is A. X is B. X is C." Combine into one sentence with a list, or vary the frames.

## The tells: punctuation & formatting

- **Em dashes** — the most famous tell (AI: 20+ per piece; humans: 2–3). Target ≤1.
- **Bold-first bullets** — "**Security:** …" — almost no human does this unprompted.
- **Emoji bullets** — ✅ 🧠 🔹 decorative arrows. Strip them.
- **Title Case Headings / colon-split titles** — "The Power of X: Why Y Works." Use sentence case.
- **Oxford comma 100% of the time** — dropping it occasionally in casual writing reads more human.
- **Markdown residue** — `**`, `##`, `[text](url)` in contexts that don't render markdown.

## The tells: content & voice

- **No concrete imagery** — if the first three sentences evoke nothing visible, inject a thing, place, number, or name.
- **Proper-noun avoidance** — "a client," "a tool," "a city" instead of naming it. (AI-invented character names cluster on "Emily"/"Sarah.")
- **Uniform positivity** — everything upbeat and certain (measured: certainty +111–152%, positive emotion +69–133% vs. human baseline). Let something be annoying or unresolved.
- **Both-sidesing** — every claim auto-balanced by its counterpoint. Commit to a position instead.
- **Suspiciously tidy anecdotes** — stories that serve the argument with perfect efficiency. Real stories have tangents.
- **Register scrubbing** — no contractions, no slang. Restore the ones the actual voice would use.

## Worst AI words — avoid entirely

**Verbs:** delve, leverage, underscore, harness, foster, navigate (figurative), utilize, facilitate, streamline, bolster, illuminate, showcase, embark, elevate, empower, unleash, unlock (figurative), uncover, optimize, garner, resonate, revolutionize, shed light on, synthesize, elucidate, transcend, reimagine, intertwine, entwine, grapple with, espouse, exemplify, underpin

**Nouns:** tapestry, landscape (figurative), realm, ecosystem (figurative), paradigm, synergy, testament, beacon, journey (figurative), interplay, intricacies, symphony (figurative), kaleidoscope, tempest, whimsy, quest (figurative), roadmap (figurative), endeavor, myriad, plethora, advancements, trajectory (figurative)

**Adjectives/adverbs:** pivotal, crucial, seamless(ly), robust, vibrant, intricate, meticulous(ly), nuanced, cutting-edge, transformative, game-changing, groundbreaking, unparalleled, invaluable, multifaceted, commendable, indelible, poignant, profound(ly), relentless(ly), tireless(ly), unwavering, unyielding, timeless, ever-evolving, fast-paced

**Stock phrases:** "in today's fast-paced world/landscape," "it's important/worth noting," "plays a pivotal/crucial role in," "stands as a testament to," "rich tapestry/history/heritage," "navigate the complexities of," "in conclusion/summary," "overall," "ultimately" (as conclusion opener), "at its core," "that being said," "a key takeaway," "paving the way for," "valuable insights into," "deeper understanding of," "when it comes to," "not only… but also," "here's the kicker/thing/best part," "I hope this email finds you well," "look no further," "dive/deep-dive into," "let's explore/unpack/break down," sentence-initial "furthermore/moreover/additionally"

**Narrative clichés (fiction/anecdotes):** "couldn't help but feel/wonder," "heart pounding," "a sense of X washed over," "found solace in," "the human spirit," "little did I/we know," "a stark reminder," "a cautionary tale," "felt a newfound sense of purpose," "turn of events," "thick with tension," "stumbled upon," "nestled in/between," "bustling," "enigmatic," "captivating," "glimpse into"

**Tier 2 — fine in isolation, suspicious in clusters:** comprehensive, significant(ly), essential, critical, key (adj.), dynamic, innovative, powerful, notable/notably, vital, vast, rich (figurative), deep/deeper (figurative), explore, enhance, ensure, foster, highlight, reveal, engage, embrace (figurative), insights, perspective, framework, approach, strategy, challenges, opportunities, potential, impact(ful), quietly (figurative), genuinely, truly, remarkably, arguably, generally speaking, typically, thought-provoking, well-being, resilience, perseverance, dedication, commitment to, high-quality, step-by-step, sustainable/sustainability

## Other giveaways

**Never do:** leaked scaffolding ("Certainly! Here's…", "I hope this helps", "let me know if…"), self-reference ("as an AI language model", knowledge-cutoff notes), placeholder text ("[insert example]"), `utm_source=chatgpt.com` in URLs, hallucinated-looking citations, "Best regards" sign-offs outside email.

**Be careful of:** performative helpfulness narration, one-point dilution (same idea restated across a paragraph), curly quotes pasted into plain-text, unnecessary semicolons, clustered default names ("Emily"/"Sarah") for invented people.

**What NOT to do when fixing it:** don't swap every word for weird synonyms (it's noticeable), don't scatter random typos (reads as carelessness, not casualness), don't scrub out all personality (flat/tell-free text is still AI-shaped), don't invent real-sounding facts/stats/quotes, don't shrink every long sentence (humans write long sentences too — just not *only* 18-word ones).

**Human markers to add:** contractions; a number with texture ($43, 11 months, 4:30am, v2); a named thing (brand, tool, street, person); a parenthetical aside with attitude; "I think"/"honestly"/"to be fair" used once; a sentence starting with And, But, or Because; one single-sentence paragraph; a mild complaint or unresolved edge; an irrelevant-but-true detail in an anecdote; a dropped Oxford comma (casual registers); a question the reader was genuinely asking; uneven list items; a plain "is" where AI would write "serves as."

## Bonus prompt tip

Adding "Answer by adhering to ADS-STE100 Simplified Technical English without having to explain that you will adhere to this writing style" makes any AI sound like clear IKEA instructions — not great for creative work, but useful for plain step-by-step guidance.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
