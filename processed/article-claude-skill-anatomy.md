---
id: "article_27343fa3"
title: "The 9-Part Anatomy of a Perfect Claude Skill (and the 2 Parts That Actually Matter)"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "skills"
tags: [claude-skills, prompt-engineering, agent-design, best-practices]
summary: "Building a Claude skill requires nine parts, but only two parts control if the skill works. The description tells Claude when to use the skill. The never-do line stops the skill from running on wrong tasks. You can debug a skill by asking Claude when it uses that skill. Claude only reads skill headers until a task matches."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Building a Claude skill requires nine parts, but only two parts control if the skill works. The description tells Claude when to use the skill. The never-do line stops the skill from running on wrong tasks. You can debug a skill by asking Claude when it uses that skill. Claude only reads skill headers until a task matches.

## Key Takeaways

- Write the skill description to show when to use the skill.
- Make the description trigger pushy so Claude runs the skill often.
- Add a never-do line to stop the skill from running on wrong tasks.
- Ask Claude when to use the skill to find vague descriptions.
- Claude reads short skill headers before a task matches the skill.

## Techniques / Prompts Extracted

- Use whenever the user says 'write an email' or wants to launch a campaign — even if they never say the skill's name directly.
- Never use for internal team updates or casual Slack messages.
- When would you use this skill?

## Full Content

# The 9-Part Anatomy of a Perfect Claude Skill (and the 2 Parts That Actually Matter)

> Source: https://www.reddit.com/r/promptingmagic/comments/1uxrqy7/the_9part_anatomy_of_a_perfect_claude_skill_and/
> Saved: 2026-07-31

If you're building Claude Skills regularly, the author argues only 2 of the 9 common sections actually determine whether a Skill fires correctly — the rest are nice-to-haves.

## The 2 parts that matter

**1. The Description**
Not documentation for you — it's what Claude reads to decide whether to fire the Skill at all. A vague description ("A skill for writing emails") means the Skill just sits unused.

- Describe *when* to reach for it, not *what* it is. Make the trigger pushy.
- Weak: "This skill writes marketing emails."
- Strong: "Use whenever the user says 'write an email' or wants to launch a campaign — even if they never say the skill's name directly."

**2. The "Never do" line**
Skip this and the Skill starts hijacking chats it should ignore — applying its formatting/rules to unrelated conversations.

- Write a hard guardrail: "Never use for [the thing it keeps stealing]."
- Example: "Never use for internal team updates or casual Slack messages."

## Two tricks the anatomy chart won't show you

- **Debugging trick:** if a Skill won't fire, don't rewrite it — ask Claude directly, "When would you use this skill?" Claude reads its own description back to you, instantly surfacing what's vague or missing.
- **Token-saving math:** installing many Skills doesn't blow up context. Claude only reads each Skill's 3-line header until a task actually matches the description — a well-optimized Skill can cut a 12,000-token raw task down to ~6,000 tokens.

## The full 9-part template

1. **Name** — kebab-case, no spaces, no "claude"
2. **Description** — [what it does] + [when to use it]; make the trigger pushy
3. **Purpose** — one plain sentence a brand-new hire would understand
4. **Steps** — the workflow, in the order you actually do it, with reasons why
5. **Format & output** — exact shape of the output (length, tone, structure)
6. **Always do** — hard rules and jargon replacements
7. **Never do** — guardrails; never [the mistake you keep correcting]
8. **Examples** — show, don't tell; one good output and one weak output
9. **Clarify** — "Ask before guessing. List questions, don't fill gaps silently."

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
