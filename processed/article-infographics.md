---
id: "article_9d7d5dd5"
title: "The Step-by-Step Guide to Making Infographics with AI"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [infographic-generation, claude-workflow, html-css-design, prompt-engineering]
summary: "This guide explains how to make infographics with Claude using HTML and CSS instead of generated images. You upload reference images and paste a design prompt to extract a design system. Then you review a visual preview before you add your content. This method gives you precise and easily editable results."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

This guide explains how to make infographics with Claude using HTML and CSS instead of generated images. You upload reference images and paste a design prompt to extract a design system. Then you review a visual preview before you add your content. This method gives you precise and easily editable results.

## Key Takeaways

- Use the Claude home tab for better results.
- Choose Opus or Fable as your model.
- Upload reference images to show the visual style.
- Review the design system preview before you generate the infographic.
- Edit the code directly to change colors and fonts easily.
- Reuse the same style for new topics by editing the prompt.

## Techniques / Prompts Extracted

-  CODE0
-  CODE1
-  CODE2
-  CODE3
-  CODE4

## Full Content

# The Step-by-Step Guide to Making Infographics with AI

> Source: https://ruben.substack.com/p/infographics
> Saved: 2026-08-10
> Author: Ruben Hassid (Aug 4, 2026)

## Overview

Ruben Hassid's guide to building infographics with Claude by treating them as code (HTML/CSS) rather than generated images. The pitch: images built this way are precise and editable — like an Excel sheet vs. a drawing — and the same reference-image + prompt workflow can be reused for any topic by just swapping the info.

## Key Points

- Use Claude's **home tab** (not the code tab — it overcomplicates infographics).
- Model choice: Opus or Fable. Opus is cheaper; Fable is pricier but better.
- Upload 1+ reference images showing the visual style you want — Claude reads images better than text descriptions of style.
- The core prompt (paste into Claude with reference images attached) has Claude act as design lead:
  - Extract a design system from the references: palette (4–6 named hex values w/ roles), typography (2–3 roles), spacing/radius/shadow rhythm, layout logic, and the one signature element.
  - Report findings in plain language, under 200 words, flagging inferences.
  - Ask 2–4 clarifying questions (via AskUserQuestion) only where references disagree or a real decision is open.
  - Write a `DESIGN_SYSTEM.md` (CSS variables, type scale, spacing/radius values, Google Fonts link, layout notes, signature element, and a "this design never does" list).
  - Build a `tokens-preview.html` showing swatches, type scale, and one example card — review before generating the real infographic.
- Once the design system preview looks right, paste in the content/info for the infographic (or ask Claude to research it) and generate.
- **Editing is easy**: ask Claude to change colors/fonts/etc. after the fact since it's real HTML/CSS, not a flattened image.
- **Reusing a style for a new topic**: go back to the original prompt, hit "Edit," and swap in new subject matter — the design system carries over.
- **Best reference sources**: Pinterest (search 1–2 word queries, click through related images to go deeper), and for web-design-specific references: Awwwards, Godly, CSS Design Awards, Dribbble, Refero.

## The Core Prompt (copy/paste)

```
You are the design lead on this project. I'm not a designer, and I make the final calls, so talk to me in plain language.

The attached reference images are the look I want. Study them together and extract the design system they share.

• Read the references. Identify: the palette as 4-6 named hex values with roles (background, surface, ink, accent, muted); typography for 2-3 roles (display, body, utility/label) — if a typeface isn't freely available, name the closest Google Font and say what it trades off; spacing rhythm, corner radius, border and shadow treatment, density; the layout logic; and the one signature element that makes this look recognizable.
• Report back in under 200 words, no jargon. For each choice, say what it is and what it does for the reader ("near-black text on warm off-white — calm, reads like print"). Flag anything you're inferring rather than actually seeing.
• Where the references disagree, or where a real decision is still open, ask me. Use the AskUserQuestion tool, 2-4 questions maximum, plain-language options with the trade-off spelled out. Don't ask me anything you can answer from the images.
• Then write DESIGN_SYSTEM.md: a :root CSS variable block, the type scale with concrete sizes and weights, spacing and radius values, the Google Fonts link tag, one paragraph on layout logic, the signature element, and a short "this design never does" list of the things that would break the look.
• Build tokens-preview.html — one page showing the swatches, the type scale, and one example card — so I can see the system before we use it. Screenshot it, compare against my references, fix whatever drifted.
• Don't design anything else yet. Fidelity to my references beats your own taste here. If you'd normally make a bolder choice, note it at the end as an option instead of using it.
```

## Workflow Summary

1. Go to Claude, home tab, select Opus (or Fable).
2. Upload reference images (from Pinterest, Awwwards, Dribbble, etc.) + paste the core prompt above.
3. Answer Claude's clarifying questions.
4. Review the `tokens-preview.html` design system preview — confirm it matches your references.
5. Paste in the content/info you want visualized (or have Claude research it).
6. Generate the infographic.
7. Iterate freely — change colors, fonts, layout — since it's real code, not a flat image.
8. To reuse the style for a new topic: hit "Edit" on the original prompt and swap the subject.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
