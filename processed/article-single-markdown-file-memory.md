---
id: "article_c9e3a52b"
title: "Single Markdown File Memory"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "tools"
tags: [memory, markdown, agent-storage, knowledge-base]
summary: "The author builds an open source tool named magpie. This tool saves all content that Claude reads or watches into local markdown files. The storage uses no cloud and works with Obsidian."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

The author builds an open source tool named magpie. This tool saves all content that Claude reads or watches into local markdown files. The storage uses no cloud and works with Obsidian.

## Key Takeaways

- Claude loses all learned data when a session ends.
- Magpie stores consumed data in a local folder of markdown files.
- The capture engine pulls an hour-long talk into files in four point four seconds.
- Developers plan to add a push lane via a hook for high-value memories.

## Techniques / Prompts Extracted

None identified.

## Full Content

built a plain-markdown memory for everything Claude reads and watches — example library in the repo
Skill Share
Long-time builder, first time contributor..

claude can watch videos and read whole sites now, but everything it learns dies with the session. i kept hitting that, so I'm building the fix in the open this week: magpie. everything it consumes lands in a folder of markdown you own, no cloud, no accounts, greppable, Obsidian-friendly.

the file contract and a full example library are up so you can see exactly what it keeps: github.com/DanRWilloughby/magpie

poke holes and give me ideas on how to improve this. if the files look wrong to you, I want to know now.

Upvote
7

Downvote

7
Go to comments

Repost

Share
u/flydotio avatar
flydotio
•
Ad

Give your agents real computers that remember, and only pay when they're awake.
Learn More
fly.io
Thumbnail image: Give your agents real computers that remember, and only pay when they're awake.
Join the conversation

Sort by:

Best

Search Comments
Expand comment search
Comments Section
[deleted]
OP
•
6d ago
has anyone else built something similar? would love to connect

Upvote
1

Downvote

Reply

Award

Share

Dan_at_jinn
•
5d ago
OP here: Todays build results: 4.4 seconds to pull an hour-long talk into the files. the whole capture engine just landed in the repo.

Upvote
1

Downvote

Reply

Award

Share

Alone-Biscotti6145
•
5d ago
Curious on why your OP account was deleted?

Upvote
1

Downvote

Reply

Award

Share

Dan_at_jinn
•
5d ago
I killed it and started over because I hadn't adjusted the username, and it's a new company handle. User Error.

Upvote
1

Downvote

Reply

Award

Share

Alone-Biscotti6145
•
5d ago
Gotcha, I was just curious, it got the better of me lol. What you built is how I started my memory system and it's evolved into much more over time. If you want to talk, reach out.

https://github.com/Lyellr88/marm-memory

Upvote
1

Downvote

Reply

Award

Share

Dan_at_jinn
•
5d ago
For sure. I was hesitant to do it but I had just opened the account, so figured, what the hell.

Nice project. Especially the deterministic LoCoMo eval bit. One question, your benchmark shows top-5 recall missing ~37% of the time, even when the agent asks. Have you considered a push lane via a hook so the highest-value memories don't depend on the model remembering to call smart_recall?

Upvote
2

Downvote

Reply

Award

Share

Alone-Biscotti6145
•
5d ago
I have this planned and spec'd out. I've just been deep into the indexing and graph, which I'm almost done with, so I plan on working on that next, automating the memory system. The knowledge graph and indexing are now fully automated. Working on improving the indexing so it can assist with larger refactors better.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
