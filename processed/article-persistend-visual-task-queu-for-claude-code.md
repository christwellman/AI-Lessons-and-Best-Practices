---
id: "article_14f86756"
title: "Persistend Visual Task Queu For Claude Code"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "tools"
tags: [claude-code, task-queue, workflow, terminal]
summary: "Claude Queue is a local visual task tracker for Claude Code. It uses a markdown file to track active, queued, blocked, and done tasks. New inputs during execution go into the queue automatically. Finished tasks include short notes about the changes and checks."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Claude Queue is a local visual task tracker for Claude Code. It uses a markdown file to track active, queued, blocked, and done tasks. New inputs during execution go into the queue automatically. Finished tasks include short notes about the changes and checks.

## Key Takeaways

- Use a local markdown file to track tasks in a single session.
- Type  CODE0  to get the tool.
- Add new tasks to the queue while the agent works.
- View the live tracker in a second terminal pane by typing qw.
- Read plain-English logs on finished tasks to see what shipped.

## Techniques / Prompts Extracted

None identified.

## Full Content

Persistent visual task queue for Claude Code so you stop losing track of what it actually got done
Workflows
I use Claude Code in the terminal and two things kept bugging me:

In long sessions I'd lose track of what actually got done vs what I just talked about. It all scrolls away.

I like to keep throwing new tasks at it while it's working, and those mid-flight ones were easy to lose track of.

So I made Claude Queue. You type /queue and it turns a plain queue.md into a real work list. Claude works one task at a time until it's all done or blocked, and anything you type while it's running gets added to the queue instead of lost in the mix. Each finished task gets a short plain-English note of what changed and how it checked it, so you can actually see what happened.

You watch it in a second terminal pane (type qw): active, queued, blocked, done, with the summary sitting on each finished task.

(And yea, Claude Code has native Tasks now that persist across sessions too. This is the visual layer on top of that idea: a readable* *queue.md* *in your repo, a live tracker pane, and a plain-English log of what actually shipped.)

Snag it here:
https://github.com/dannygreer/claude-queue

r/BuildWithClaude - Persistent visual task queue for Claude Code so you stop losing track of what it actually got done
Standard-library Python. No accounts, no services, nothing to pip install. The queue is just a markdown file in your repo. Free, MIT.

Only works with Claude Code in the terminal, not the desktop or web app, since the tracker's a terminal program. Feedback welcome.

Upvote
5

Downvote

5
Go to comments

Repost

Share
u/anthropic-ai avatar
anthropic-ai
•
Ad

Claude Code doesn’t just write code. It helps you think through trade-offs and build with confidence.
Sign Up
claude.com
Thumbnail image: Claude Code doesn’t just write code. It helps you think through trade-offs and build with confidence.
Join the conversation

Sort by:

Best

Search Comments
Expand comment search
Comments Section
u/WearyArtistDoomer avatar
WearyArtistDoomer
•
4d ago
Not to be a downer but isn’t this just an issue tracker, but confined to your local machine?

I use linear for the same purpose. There are a lot of alternatives ofc.

Upvote
2

Downvote

Reply

Award

Share

habeebiii
•
3d ago
I don’t want to make tickets for 10 tiny unrelated things or aspects of an existing ticket

Upvote
2

Downvote

Reply

Award

Share

danny_greer
OP
•
3d ago
Good question. I’m a linear user too. I actually had this written up in the GH link but I think that link got pulled out of the post. Trying here: https://github.com/dannygreer/claude-queue

“How this is different from an issue tracker

Issue trackers like Linear, Plane, or Jira manage the big picture: epics and issues you plan over days and weeks. Keep doing that where you already do it.
Claude Queue works at a different altitude. It lives inside a single Claude Code session, where you pound tasks into the agent as fast as you think of them. It keeps a running list so nothing you asked for gets dropped, and every finished task leaves a short note on what changed, so you can look back and see what actually got done.
The point is to stay in flow. You keep firing ideas at Claude instead of babysitting a checklist or scrolling back to figure out where things landed.”

Upvote
2

Downvote

Reply

Award

Share

Wobbly_skiplins
•
3d ago
🚀 First-Wave Builder
Use Git, don’t let Claude pile up changes! Whenever you have made a significant change, commit that change. If you’re not sure about the direction you’re going, make changes on a branch.

Upvote
2

Downvote

Reply

Award

Share

Ok_Industry_5555
•
4d ago
☕ 57-Hour Session
Nice work!!

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
