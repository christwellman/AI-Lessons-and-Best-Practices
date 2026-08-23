---
id: "article_8a343993"
title: "Youtube Authorities"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [multi-agent, workflow, git-worktrees, prompt-engineering]
summary: "Users discuss problems with agent tutorial videos on YouTube. One user shares a practical method to run multiple AI coding agents in parallel. The method uses separate chat sessions, git worktrees, and concrete markdown files."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Users discuss problems with agent tutorial videos on YouTube. One user shares a practical method to run multiple AI coding agents in parallel. The method uses separate chat sessions, git worktrees, and concrete markdown files.

## Key Takeaways

- Ask Claude questions to learn about agents instead of watching videos.
- Use git worktrees to run multiple agent instances in parallel safely.
- Give each agent a markdown file with request details and constraints.
- Check video descriptions for repositories before you watch them.

## Techniques / Prompts Extracted

- Step 1: braindump everything you can about your current conceptual knowledge, the facts you’re aware of, the concerns you have, etc. literally everything and anything you can think of about what you’re ACTUALLY wondering about. do you want to know about setting up your repo? about best practices for designing architecture that makes it easy to use agents? gather it all up (if you don’t know what to ask, tell it you don’t know what to ask.)
- Step 2: ask Claude. spend a couple hours just going back and forth, relentlessly asking questions over and over until you feel like you understand. ask it to set up interactive demos so you can understand the core concepts / fundamentals of working with agents.
- Spin up new Claude instance, rename it, color it. Any time there’s a new feature or anything disjoint from my other instances, it gets a fresh session. Very importantly, I have a hook so that if a feature goes through brainstorming, features ALWAYS start on a new worktree. Worktrees are the real trick to maximizing parallel agents
- Give it a concrete .md file containing my exact feature request, any constraints, images, diagrams, concerns, style choices, design choices, etc. As simple or complex as needed for the request
- Use /superpowers brainstorming to kick off a back and forth discussion for further refining the idea / aligning on intention + goals, aligning on architecture and design choices, etc.

## Full Content

YouTube recommendations, who’s the actual authority?
Vibe Coding
I searched on YouTube how to use agents. 2 million videos with the same beginner to pro/advance title all 15 minutes.

Other fields I learn about have like 2-3 of “the guy to watch” this one seems saturated, looking for recommendations, who makes the best video, ie, simple instruction and easy to follow, doesn’t have to be amazing quality but a lot seem to be fluff and filled.

Upvote
2

Downvote

12
Go to comments

Repost

Share
Join the conversation

Sort by:

Best

Search Comments
Expand comment search
Comments Section
Over-Clerk-5307
•
2d ago
Step 1: braindump everything you can about your current conceptual knowledge, the facts you’re aware of, the concerns you have, etc. literally everything and anything you can think of about what you’re ACTUALLY wondering about. do you want to know about setting up your repo? about best practices for designing architecture that makes it easy to use agents? gather it all up (if you don’t know what to ask, tell it you don’t know what to ask.)

Step 2: ask Claude. spend a couple hours just going back and forth, relentlessly asking questions over and over until you feel like you understand. ask it to set up interactive demos so you can understand the core concepts / fundamentals of working with agents.

this isn’t what you asked for, but try it out, i promise you’ll learn more than watching from youtube

Upvote
14

Downvote

Reply

Award

Share

u/Legendary_Ghost_X avatar
Legendary_Ghost_X
OP
•
2d ago
Yeah I’ll give that a shot! I’m building apps with gsd currently, I have a pretty good understanding of it, but want to learn more about spinning up more agents to do more things autonomously

Upvote
2

Downvote

Reply

Award

Share

Over-Clerk-5307
•
2d ago
•
Edited 2d ago
what does “autonomously” mean here? as in, automatic triaging -> picking a task -> implementing -> merging back in?

Beads is something you might be interested in. If you get one of the UI tools set up for it, Claude can automatically create tasks, and agents can be aware of each other’s’ active tasks, which is cool. I had ~100 tasks set up for a repo one time, and just let it rip, which ended up working pretty well.

There are tradeoffs with fully autonomous feature development though, because you’ll lose fine-grained control over implementation choices / design choices. If you’re cool with that, go for it

Nowadays my workflow for multiple agents is:

Spin up new Claude instance, rename it, color it. Any time there’s a new feature or anything disjoint from my other instances, it gets a fresh session. Very importantly, I have a hook so that if a feature goes through brainstorming, features ALWAYS start on a new worktree. Worktrees are the real trick to maximizing parallel agents

Give it a concrete .md file containing my exact feature request, any constraints, images, diagrams, concerns, style choices, design choices, etc. As simple or complex as needed for the request

Use /superpowers brainstorming to kick off a back and forth discussion for further refining the idea / aligning on intention + goals, aligning on architecture and design choices, etc.

When happy, Claude writes up the spec & implementation plan

Spin up as many sub agents as necessary on the worktree to implement the feature

Review results, test it. Notice anything I don’t like or

that is *correct* but not quite the vision. Gather all feedback. Keep iterating until happy

Merge worktree back into main, mark task as done

With that process, I can usually run ~6 separate windows each with N agents at a time (before my brain gets overwhelmed with too many tasks to keep track of / test).

Upvote
1

Downvote

Reply

Award

Share

u/LordMoridin84 avatar
LordMoridin84
•
2d ago
Check Matt Pocock on YouTube.

Upvote
3

Downvote

Reply

Award

Share

AregNoya
•
2d ago
I really like matt wolf. He just tells news without much of an opinion

Upvote
2

Downvote

Reply

Award

Share

u/Robotmadethis avatar
Robotmadethis
•
2d ago
The best authority test I’ve found is whether the teacher leaves you something inspectable after the video: a repo, a complete instructions file, the permissions boundary, and a failure log. Agent demos are easy to narrate; the hard part is wake 20, when memory is stale and a tool call fails. I’d use official material for mechanics, then trust creators only for workflows you can reproduce from their files. If the video ends with a dashboard and no inspectable setup, it’s entertainment, not instruction.

Upvote
1

Downvote

Reply

Award

Share

u/Legendary_Ghost_X avatar
Legendary_Ghost_X
OP
•
2d ago
Yeah I love that measure, but don’t want to watch hours and hours of the same video made by different people to figure out who’s best.

Upvote
2

Downvote

Reply

Award

Share

u/Robotmadethis avatar
Robotmadethis
•
2d ago
Fair. I’d use the video as a five-minute filter, not the lesson: open the description first. No repo or sample instructions? Skip it. If there is one, scan for a complete loop—trigger, tool permissions, failure handling, and evidence. Only then watch the chapter that maps to the file. You can reject most candidates without watching them.

Upvote
1

Downvote

Reply

Award

Share

Delicious-Effort6214
•
2d ago
Automator
Set up a Google Gemini Notebook (formerly NotebookLM). Find a handful of YouTube channels that are popular and on topic. Get the chrome extension that imports YT vids as sources in bulk. Then ask the notebook questions and to give you notes on it

Upvote
1

Downvote

Reply

Award

Share

Glp1User
•
2d ago
You watched 2 million 15 minute videos?

Upvote
0

Downvote

Reply

Award

Share

Dismal_Boysenberry69
•
1d ago
What would make you think that?

Upvote
1

Downvote

Reply

Award

Share

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
