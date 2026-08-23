---
id: "article_4d161406"
title: "How Do You Set Up Your Code Review"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [code-review, agent-swarm, prompt-engineering, llm-evaluation]
summary: "Generic code review prompts fail because they lack project intent and context. Effective AI review requires feeding the LLM the original specification, ticket description, and repo-specific policy files. Using a panel of different model families catches more defects than a single model."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Generic code review prompts fail because they lack project intent and context. Effective AI review requires feeding the LLM the original specification, ticket description, and repo-specific policy files. Using a panel of different model families catches more defects than a single model.

## Key Takeaways

- Feed the spec and plan to the review agent so it understands why the code exists.
- Provide the ticket or pull request description to catch logic errors that differ from requirements.
- Delete tool-catchable issues like formatting and type errors before running the LLM review.
- Run reviews in a fresh context session to prevent the writing agent from defending its own choices.
- Force a strict evidence format such as file, line, and concrete fix to remove useless prose.
- Use multiple model families to increase defect coverage because different models miss different bugs.

## Techniques / Prompts Extracted

None identified.

## Full Content

How do you set up your code review skill?
Question
I use a bunch of skills in my workflow for building web apps. Most of them work fine. The one I keep struggling with is code review.

I've tried a few things. The best setup so far was splitting review into three separate skills, each one focused on a different thing:

- Architecture decisions (Big picture only, no implementation details).

- Implementation details.

- Comments and tests.

This works better than what I had before, but I still don't get much out of it.

Has anyone found a review setup that actually helps?

Upvote
9

Downvote

16
Go to comments

Repost

Share
u/anthropic-ai avatar
anthropic-ai
•
Ad

The best projects start with great ideas. Claude Code helps you actually build them.
Sign Up
claude.com
Clickable image which will reveal the video player: The best projects start with great ideas. Claude Code helps you actually build them.
Collapse video player

0:00 / 0:00

Join the conversation

Sort by:

Best

Search Comments
Expand comment search
Comments Section
mxriverlynn
•
7d ago
you're on the right path, but slightly off in how those pieces are built

instead of a new skill for each of those areas, build a new custom agent definition for them, with reference files that outline what the review actually needs to look for

i have a single code-review skill, but i have 20+ agent definitions and several reference files that detail various aspects of what quality code looks like, and it works quite well

keep in mind, tho, that no amount of agentic code review will be able to completely reproduce the quality of review that a highly experienced engineering team can produce. we're not at that point yet. but you can cover the majority of technical issues and general software details and architecture and design.

the other thing you need to do, is ensure the review skill and agents have access to the same context that you do, for WHY the code was built, not just how

Upvote
4

Downvote

Reply

Award

Share

u/Ramii89 avatar
Ramii89
OP
•
7d ago
Thanks, this is useful.

One thing about my setup. I run the three parts in phases on purpose. If the big picture is wrong, there is no point looking at implementation details yet. So I fix that first, then move to the next phase. That's why they are separate skills and not one.

About the 20+ agents, how do you deal with speed and token cost? Do they all run every time, or does the skill pick a few based on what changed?

Upvote
2

Downvote

Reply

Award

Share

mxriverlynn
•
7d ago
that's a good point about the big picture, first. I'll have to do some experimenting with that and see if i can find some improvements in my setup

for the speed and cost: it can get expensive and take a long time, yeah. I've built in some ways to help keep that down. ultimately, providing the right context for the review is the best way to keep it reasonable, tho.

there's a "sizing" concept built in to any skill that uses an agent swarm like this. by default, the skills will take a quick look at what their digging into and try to figure out the right size / number of specialist agents to use. but you can also explicitly state small, medium, or large.

docs on sizing: https://github.com/testdouble/han/blob/main/docs/sizing.md

you can also add a .han/config.md file in your project root, or ~/.claude/ folder, and provide custom instructions for a specific skill, including the code review skill. this let's you limit the number of agents used to a specific subset, add custom agents, add reference files for specific needs, etc. i typically have a handful of custom rules for the the projects i work on. and being a consultant, it's important that I'm able to change settings depending on the project, like this.

docs on customizing config: https://github.com/testdouble/han/blob/main/docs/configuration.md

Upvote
3

Downvote

Reply

Award

Share

mxriverlynn
•
7d ago
if your interested in seeing how i built all this, here's my links:

https://github.com/testdouble/han/blob/main/han-coding/docs/skills/code-review.md - docs on the code review skill

https://github.com/testdouble/han/blob/main/docs/how-to/run-an-effective-code-review.md - how to do an effective code review

https://github.com/testdouble/han/tree/main/han-coding/skills/code-review - the skill definition and reference files

https://github.com/testdouble/han/blob/main/docs/agents/README.md - the full list of custom agent definitions that are available for my skills, including the code review skill

Upvote
2

Downvote

Reply

Award

Share

u/rafal_graniczny avatar
rafal_graniczny
•
6d ago
the biggest gain for me wasn't the prompt, it was narrowing the scope.

generic "review this diff" gives you style nits and confident nonsense. what actually works is a short repo-specific list of things that have bitten us before. ours is like 8 lines: auth checks on new endpoints, n+1s, migrations that lock, error paths that swallow. anything outside the list, it stays quiet.

two other things:

- feed it the ticket/PR description too, not just the diff. most real bugs are "this doesn't do what it was supposed to do", which is invisible from the diff alone.

- make it output questions, not fixes. "why is this cached here?" is more useful than a patch, because it forces the author to actually answer.

that last one changed how i think about review generally. the point isn't catching bugs, it's checking somebody understands the change. a reviewer who can't answer a basic question about the diff is a bigger risk than a missed null check.

Upvote
2

Downvote

Reply

Award

Share

u/Potential-Beat2841 avatar
Potential-Beat2841
•
7d ago
The reason splitting by topic didn't move the needle much: all three skills still review the diff against nothing. A reviewer with no statement of intent can only pattern-match style, so you get "consider adding error handling" forever. Feed it the spec and the plan the code was written from, and it can find the thing that actually matters — what's missing or what silently deviated from the plan. That's the one change that made review useful for me.

Four things that helped after that:

Delete everything a tool can catch. Formatting, unused imports, type errors, dead code — linter/tsc/tests. The skill should only look at what tooling structurally can't: does this satisfy the requirement, does it break an architectural constraint, which edge path is untested.

Review in a fresh context. Subagent or new session. An agent reviewing its own writing session defends its choices instead of auditing them.

Force an evidence format. file:line + which requirement/rule it violates + severity + concrete fix. No prose paragraphs. And explicitly permit "no blocking issues" as an output — otherwise it manufactures findings to seem useful, which is what makes people stop reading review output.

Severity gate. blocker / should-fix / nit. Only blockers stop the merge. Without this everything reads as equally urgent and you learn to ignore all of it.

The checklist itself should be repo-specific and versioned — derived from bugs you actually shipped, not generic best practices. Generic checklists produce generic reviews.

I ended up making review a fixed phase of the loop rather than a standalone skill: specify → plan → act → review → keep, where review reads the spec and the repo's policy files as its reference and reports against them. Open-sourced the structure if it's useful: github.com/a-lottes/aSPARK

Upvote
2

Downvote

Reply

Award

Share

Ethan
•
6d ago
I built this: https://www.npmjs.com/package/audit-tools

Long story short...

Install it via "npm i -g audit-tools"

You'll get a "/audit-code" command to use; run it

You'll also get a "/remediate-code" command to fix any of the issues you want to fix

Upvote
1

Downvote

Reply

Award

Share

u/iSharesOfficial avatar
u/iSharesOfficial
•
Ad

The Nasdaq-100 for long-term investors. Discover IQQ.
Learn More
ishares.com
Thumbnail image: The Nasdaq-100 for long-term investors. Discover IQQ.
u/VibeCodyH avatar
VibeCodyH
•
7d ago
I had the same issue so I just built my own. The basis is just more eyes are better. I have a list of some free models you can use in the readme. https://github.com/VibeCodyH/code-review-cadre

Upvote
1

Downvote

Reply

Award

Share

u/Ramii89 avatar
Ramii89
OP
•
7d ago
Thanks, I'll take a look.

Two questions.

Do you find several free models actually beat one good paid model? In my experience the free ones miss a lot, so I've been sticking with just one paid model.

And how do you deal with it when they disagree with each other? Do you read through everything yourself or does something merge the output first?

Upvote
1

Downvote

Reply

Award

Share

u/VibeCodyH avatar
VibeCodyH
•
7d ago
Not on their own, no. Individually the free ones miss more, you're right about that. But that's not the thing that matters. One paid model run once caps out at its own blind spot no matter how good it is, and that blind spot isn't random, it comes from the model family underneath. So running the same lineage twice just buys you one opinion twice.

The thing you're actually buying with a second (or third) reviewer isn't a higher score, it's a different set of misses. The biggest public measurement I've seen on this (Tony Stone's "A Single LLM Is an Incomplete Code Reviewer") found ~57% of confirmed defects were caught by exactly one model, and coverage went 47% at one reviewer, 72% at two, 89% at three. Take that as a direction not gospel, it's one preprint on one codebase. But it lines up with what I saw on my own repo: a candidate that scored worse than every model I already had still earned a seat, because it caught a bug all three incumbents missed. A leaderboard can't show you that.

That's the whole reason cadre exists actually. It doesn't tell you which model is best, it grades a panel against real bugs from your own git history and tells you which combo fails in different places. The number that picks your panel is one nobody can publish for you.

For the disagreements, there's a synthesis step that combines every reviewer's output into one report, and its hard rules are: keep every single-reviewer finding and flag who raised it, list each reviewer's verdict separately instead of averaging them, and never invent a finding no reviewer raised. A defect only one model caught is the reason the panel exists, so burying it into a consensus would defeat the point. So I read one merged report, but the disagreements are called out as disagreements rather than voted away.

Upvote
2

Downvote

Reply

Award

Share

u/generationalDebts avatar
generationalDebts
•
7d ago
Lmfao the amount of work vibe coding idiots will go through to avoid actually learning anything is hilarious.

Upvote
0

Downvote

Reply

Award

Share

u/gsari avatar
gsari
•
7d ago
I've opened up mine here: https://github.com/gsarig/skills/tree/main/skills/code-review so anyone curious can take a look or/and grab it to adopt on their own workflow.

The /code-review skill triages the change (line count, file types, security-sensitive paths) and recommends one of four review types, then dispatches to the matching child skill:

code-review-lite: Small, low-stakes code diffs (under ~500 lines, no security paths)

code-review-deep: Large diffs (500+ lines) or anything touching auth, crypto, SQL, migrations, secrets

code-review-infra: GitHub Actions, Terraform, Dockerfiles, docker-compose, IaC

code-review-content: Prose: markdown, docs, blog posts

Your choice is remembered per source in the project's .claude/code-review-state.json, so re-reviewing the same PR or branch skips the prompt. You can also invoke a child skill directly when you already know the depth you want.

Every review opens with a verdict line (✅ Approved / 🔴 Request changes / 💬 Comment) followed by numbered findings with severities (critical, medium, minor), plus separate sections for unrelated security concerns and project-wide observations. Shared mechanics (source detection, diff fetching, linter detection, output format) live in references/review-shared.md; general review principles live in references/review-checklist.md (grow it with your own lessons), and JS/TS-specific rules in references/js-security.md.

Upvote
1

Downvote

Reply

Award

Share

substance90
•
7d ago
No need for a dedicated code review skill in 2026. I just have claude use codex for reviews via headless mode.

Upvote
0

Downvote

Reply

Award

Share

u/generationalDebts avatar
generationalDebts
•
7d ago
LMFAO code review lol
---

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
