---
id: "article_8bb79be3"
title: "27 Claude tips after 1,800 hours"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "best-practices"
tags: [claude, workflow, prompt-engineering, agent-management]
summary: "This document gives best practices for Claude usage based on practical experience. It covers context management, tool selection, and prompt strategies. Users learn how to reduce token costs and improve output quality."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

This document gives best practices for Claude usage based on practical experience. It covers context management, tool selection, and prompt strategies. Users learn how to reduce token costs and improve output quality.

## Key Takeaways

- Use Projects for repeated tasks with fixed material, and use empty chats for new ideas.
- Start difficult tasks with a powerful model, then switch to a cheaper model.
- Edit previous prompts instead of correcting mistakes in new messages to save context and tokens.
- Turn off unused Connectors to reduce token consumption.
- Start a new chat when conversations reach thirty to fifty turns to avoid performance degradation.
- Use voice notes to capture raw context without over-organizing.

## Techniques / Prompts Extracted

- Code an HTML-like infographic like the one I attached, but about [topic].
- Before answering, use the AskUserQuestion form to get more context from me if necessary.
- Build me an artifact that tracks [my habits / my client pipeline / my reading list], and make it save my data between sessions.
- Make it so there is a Claude coach inside I can talk to and it has the context of this artifact.
- Using Slack, Granola and Gmail, draft 3 different emails with 3 different tones about [...].
- Never write like this: [paste example].

## Full Content

# 27 Claude tips after 1,800 hours

> Source: https://ruben.substack.com/p/1800-hours-of-claude
> Saved: 2026-08-10
> Author: Ruben Hassid (Jul 29, 2026)

**1. Stop it with your Claude 'Projects'.** Projects remix answers from loaded files — great for repeated tasks with fixed material (client reports, standard procedures), bad for creative work since every answer echoes your own documents. Rule: Projects for repeated/fixed-material tasks, empty chats for new ideas.

**2. Fable-5-High first, then Opus-5-High.** Frame the problem with the most powerful model on your first prompt (Fable-5), then switch to a cheaper model (Opus 5, High) to continue without burning extra cost.

**3. Claude can't technically make images** — but it can generate HTML you export as an image. Upload a reference image with: "Code an HTML-like infographic like the one I attached, but about [topic]." Bonus: text is always spelled correctly, unlike image generators.

**4. Don't reply "no, that's wrong" — edit instead.** Corrections leave the wrong answer in context, and Claude keeps working around it (and you pay for it on every later message). Instead, go back to the prompt right before the bad answer, edit it, and save.

**5. Better yapping than typing.** Typing makes you over-organize and drop context. Talking for 10 minutes straight (goal, constraints, what you tried, contradictions — don't clean it up) gives much better raw material. End with: "These were messy voicenotes. Ask me clarifying questions if you didn't get something as a form."

**6. Turn off Connectors you're not using.** Every active Connector loads into every message whether used or not, costing extra tokens. Turn off anything you're not actively using.

**7. When Claude gets dumb, start a new chat.** Long conversations get slower and less sharp — Claude re-reads everything and has to reconcile contradictions. Rough guide: 30–50 turns is where it starts degrading; above 100, start fresh.

**8. Ask Claude to ask you questions.** Add: "Before answering, use the AskUserQuestion form to get more context from me if necessary." Produces tappable multiple-choice questions — a very underrated feature.

**9. Code is better than Cowork at everything** — it just looks scarier. Try it once via the "Code" tab, dictate a vibe-code request, and see what's possible even if you never master it.

**10. Cowork is for running many Claudes in parallel, without coding.** Its real feature is spawning multiple agents to attack one problem at once. Give it big, multi-part tasks ("prepare the full client onboarding: deck, welcome email, checklist") rather than small ones.

**11. Set up Cowork with a skill.** The `setup-cowork` skill interviews you and configures preferences, styles, and workflows — run `/setup-cowork` with "start".

**12. Send a screenshot instead of a description.** For design work (Claude Code, Claude Design, or plain Claude for HTML), start with an image — a competitor page, a dashboard you like, a napkin sketch — rather than describing it in words.

**13. Build your own mini-apps (artifacts).** Prompt: "Build me an artifact that tracks [my habits / my client pipeline / my reading list], and make it save my data between sessions." You get a shareable link.

**14. Invite Claude inside your mini-app.** Prompt: "Make it so there is a Claude coach inside I can talk to and it has the context of this artifact." Publish and share — a proposal analyzer, quiz, or tone-checker others can use without their own Claude account.

**15. Stay under 150 seats.** Premium seats ($100/seat/month) come with generous usage limits. Cross 150+ seats and you pay per usage regardless, which gets expensive fast.

**16. Combine Connectors together.** Example: connect Slack (what was said), Granola (what was decided), and Gmail (what was promised) and prompt: "Using Slack, Granola and Gmail, draft 3 different emails with 3 different tones about [...]."

**17. Share what you hate, not vague adjectives.** "Make it nicer/punchier" does little. Instead: "Never write like this: [paste example]." Draws an exact line not to cross.

**18. Open files in Google Drive** rather than downloading Claude-generated documents locally.

**19. Vibecoding won't make you rich by itself** — but next time you have an idea, build a rough version in an afternoon instead of writing a briefing doc, then bring that half-baked prototype to your technical team. Much more useful than a spec.

**20. Skills = repeated tasks, not creative work.** Best for "do this exact task this exact way" (reports, formats, recurring workflows). Worst for creativity — every loaded skill bloats context and narrows exploration. For pure creative tasks, consider incognito mode to eliminate context clutter entirely.

**21. Try Research mode.** It plans, reads dozens of sources, and returns a structured report. Toggle "Research" in the chat bar, ask a decision question, and let it run.

**22. Make your data interactive.** Paste numbers or a CSV and ask: "Make this an interactive chart" — renders right inside the chat.

**23. Don't write like an AI** — audit text against AI-detector patterns before publishing (see the author's companion piece on bypassing AI detectors).

**24. Ignore "loop engineering" and whatever new-technique name comes out next month.** Techniques matter once they become invisible (e.g., Chain-of-Thought → reasoning models you don't need to understand to benefit from). Focus on the job, not the jargon.

**25. Don't switch to ChatGPT.** Both are good; the author prefers Claude for writing/reasoning and the Premium team tier value. Exception: at 5,000+ employees, an open-source setup starts to make more sense.

**26. If you use Google, Claude is just as safe.** Modern AI providers (Claude, ChatGPT) are SOC-2 compliant and comparably safe to Google for business data. Caveat: Fable-5 has a data retention quirk — other models are fine.

**27. AI solved a math problem that stayed open for 80 years — because someone simply asked, with the right context.**

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
