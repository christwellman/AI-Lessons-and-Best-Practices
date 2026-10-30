---
id: "article_a0c00edc"
title: "What Memory Do You Use"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "tools"
tags: [memory-tools, agent-workflows, context-management, markdown-files]
summary: "Developers discuss different memory tools and systems for AI agents. Many users find third-party memory plugins unreliable and prefer custom markdown file structures, dedicated handoff folders, or local databases. Instruction files like CLAUDE.md help enforce memory search before agents answer."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Developers discuss different memory tools and systems for AI agents. Many users find third-party memory plugins unreliable and prefer custom markdown file structures, dedicated handoff folders, or local databases. Instruction files like CLAUDE.md help enforce memory search before agents answer.

## Key Takeaways

- Many third-party AI memory tools suffer from poor retrieval relevance and high noise ratios.
- Developers use local markdown files, handoff folders, and project wikis to track state.
- Instruction files mandate memory search before the agent answers past questions.
- Some users build custom MCP servers or local database integrations for real-time context tracking.

## Techniques / Prompts Extracted

None identified.

## Full Content

What memory tool do you use?
Discussion
I was using memplace for a while but after 1 month, yesterday I decided to evaluate it, and I asked claude to evaluate, turns out its Pretty garbage because it did not fetch any of the context that was the relevant to agent when it needed, it had around the you of 900:1 which was pretty bad

I have heard hermes have a good memory system, I have not tried it though

Please some good and relevant memory tool

Upvote
22

Downvote

101
Go to comments

Repost

Share
u/apollo-io avatar
apollo-io
•
Ad

Read that again.
Sign Up
apollo.io
Thumbnail image: Read that again.
Join the conversation

Sort by:

Best

Search Comments
Expand comment search
Comments Section
GfxJG
•
1d ago
Currently? None. I have yet to find one that actually works. Or rather, I have yet to find one that integrates so well into the workflow that the agents remember to use them to actually recall knowledge,

Recallium was the one I found that came closest - Unfortunately, it seems to have been at least partially abandoned by the devs.

Upvote
23

Downvote

Reply

Award

Share

Aggravating-Start307
•
7h ago
Since you have already used one tool, would you be interested in trying coldstart ? I am actively maintaining this as i am the biggest user myself 😂 right now. https://coldstartmcp.dev in case you are interested.

This is a tool i built for myself and more often than not, i find bugs and fix them so that me and a couple of users can burn less tokens and save time instead of repeated discovery.\

Upvote
1

Downvote

Reply

Award

Share

u/krilleractual avatar
krilleractual
•
1d ago
I asked my claude to make a kanban that tracks tasks past and present. Whenever i give it a task, it makes a card and keeps the conversations linked to the card. I also made it have a macro that can open a claude code conversation with the card being the prompt. Its pretty nice.

Upvote
15

Downvote

Reply

Award

Share

u/RubberGeneral_14 avatar
RubberGeneral_14
•
1d ago
I do something very similar using github issues. I use comments as context for what I have done. Just created a workboard for myself with my own "standard" for the layout of the tasks. Switched off the memory functionality.

Upvote
2

Downvote

Reply

Award

Share

u/MoneyPirate3896 avatar
MoneyPirate3896
•
1d ago
Also Discussions

Upvote
1

Downvote

Reply

Award

Share

u/krilleractual avatar
krilleractual
•
1d ago
Yeah thats very similar. Having a master file that keeps track of it is nice for sure

Upvote
1

Downvote

Reply

Award

Share

jcol26
•
12h ago
backlog.md does this in a more structured way

Upvote
1

Downvote

Reply

Award

Share

u/krilleractual avatar
krilleractual
•
11h ago
i dont claim to have invented this and im sure backlog.md is great (i dont see anything on first sight that my version doesnt do, as mine also creates a html). That being said my own solution is just that. I have tried a few different tools and they all have disappointed me in some way. I also feel a little weary of these projects especially with my work.

Upvote
1

Downvote

Reply

Award

Share

u/DisplacedForest avatar
DisplacedForest
•
1d ago
I do this with Linear. I just alter the superpowers skill so that plans and specs are tickets and implementation plans are just comments on the tickets. ADRs are project docs in linear… etc etc.

This way they aren’t floating .md docs and they are time stamped and projects are self contained. Works great

Upvote
1

Downvote

Reply

Award

Share

u/krilleractual avatar
krilleractual
•
19h ago
Whats linear is it a workspace?

Upvote
1

Downvote

Reply

Award

Share

u/DisplacedForest avatar
DisplacedForest
•
19h ago
It’s a product development app. Product management basically. https://linear.app

This has existed way before AI. Actual product teams use this

Upvote
1

Downvote

Reply

Award

Share

u/zeesshhh avatar
zeesshhh
OP
•
1d ago
Nice approach.

Let's say you want to create a new project how would you approach it?

Does it have its own kanban board or goes into global cards?

What do you work on mostly?

Upvote
1

Downvote

Reply

Award

Share

u/krilleractual avatar
krilleractual
•
1d ago
The kanban is for each root folder of each project, so I currently have three, which helps because I lose track of what needs to get done over days that I dont work on stuff.

Im currently working on something that auto cuts footage and combines different cameras and bases it off of a transcript for what the best parts are.

Also another thing is a sports based computer vision project.

Upvote
1

Downvote

Reply

Award

Share

u/HyenaLaugh95 avatar
HyenaLaugh95
•
23h ago
Can you explain this a bit more please? Is this possible on the default desktop Claude or only a Claude code thing?

Upvote
1

Downvote

Reply

Award

Share

u/krilleractual avatar
krilleractual
•
19h ago
Ive only done this on claude code as it needs access to my files. Not sure if desktop can do it.

What part do you want to know more about

Upvote
1

Downvote

Reply

Award

Share

yezzer
•
1d ago
I do similar with GitHub issues. Quite happy with the results.

Upvote
1

Downvote

Reply

Award

Share

u/Puzzleheaded-Union97 avatar
Puzzleheaded-Union97
•
12h ago
I have a handoff folder.

Claude.md points at this folder

It has 3 files.

handoff.md - at every commit, the agent writes what we did

decisions.md - why we did it

architecture.md - the structure of the project

Works pretty well.

Every new agent knows EXACTLY where to pick up from.

Never had a problem that I start a new agent I have to explain everything again. They know everything from message 1.

Upvote
2

Downvote

Reply

Award

Share

u/interservermike avatar
u/interservermike
•
Ad

Reliable VPS hosting, price-locked. Choose InterServer.
Learn More
interserver.net
Thumbnail image: Reliable VPS hosting, price-locked. Choose InterServer.
u/staffengineerk avatar
staffengineerk
•
1d ago
lots of md files , we are all Markdown engineers now.

Upvote
6

Downvote

Reply

Award

Share

u/cleverhoods avatar
cleverhoods
•
1d ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
None.

Project specific information and instructions are classified separately and loaded to context according need/behavior.

Upvote
11

Downvote

Reply

Award

Share

codeninja
•
1d ago
... and then largely ignored.

Upvote
6

Downvote

Reply

Award

Share

u/cleverhoods avatar
cleverhoods
•
1d ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
I have different experience, but I guess that's rather expected when you're working on instruction diagnostics and evals.

Upvote
3

Downvote

Reply

Award

Share

discomonk
•
1d ago
A well-documented repo designed for agents and humans to read, with a graphiti knowledge graph to allow better searching across the repo. Everything key gets documented.

Upvote
3

Downvote

Reply

Award

Share

u/clintecker avatar
clintecker
•
1d ago
None. Partially because they are almost all solving something that hasn't been a problem for years and partially because they all seem to be written exclusively by newbs caught in the thrall of AI psychosis and they can't even properly articulate why they think they need it, if it works, and if it actually serves a purpose to anyone

Upvote
5

Downvote

Reply

Award

Share

u/PM__ME__BITCOINS avatar
PM__ME__BITCOINS
•
1d ago
For real. You want memory with concurrency, hash collision checks, undo, roles and permissions? Congrats you just described a database from 1984.

Upvote
1

Downvote

Reply

Award

Share

u/TySocal avatar
TySocal
•
1d ago
Not to mention false memory can really mess around what is true/false

Upvote
1

Downvote

Reply

Award

Share

u/zbeeapp avatar
u/zbeeapp
•
Ad

Your safe retirement spend, measured on your Mac — now free to use, and your holdings never leave it.
Download
zbee.app
Thumbnail image: Your safe retirement spend, measured on your Mac — now free to use, and your holdings never leave it.
Anooyoo2
•
1d ago
Context engineering and spec driven development

Upvote
7

Downvote

Reply

Award

Share

u/zeesshhh avatar
zeesshhh
OP
•
1d ago
Feels like the spec driven development slows me down, my work is not to write code on production, I usually work on devrel side so I mostly work on demos and example codes

Upvote
0

Downvote

Reply

Award

Share

Anooyoo2
•
1d ago
You still need to manage context effectively, and that means tracking state on disc. That being said - yes I wouldn't be using a full RPI flow on a task by task basis if I was vibe coding. SDD as you normally see it described likely isn't quite the right fit for you.

Upvote
1

Downvote

Reply

Award

Share

josh_a
•
17h ago
I’ve been doing a deep dive into this comparison of memory systems and analysis of patterns used:

https://neoneye.github.io/agent-memory-atlas/

The github repo has an agent skill for using the atlas to help you determine your needs and best fits

Upvote
2

Downvote

Reply

Award

Share

u/imnotdansih avatar
imnotdansih
•
1d ago
🔆Pro Plan
https://github.com/AgriciDaniel/claude-obsidian

Obsidian as a second brain 😀 works well

Upvote
3

Downvote

Reply

Award

Share

u/HyenaLaugh95 avatar
HyenaLaugh95
•
23h ago
How much do you enjoy obsidian compared to one note?

Upvote
2

Downvote

Reply

Award

Share

u/imnotdansih avatar
imnotdansih
•
23h ago
🔆Pro Plan
Never tried one note. But let the ai build you a "brain", and log sessions, projects etc inside obsidian. Its pretty dope 😀

Upvote
2

Downvote

Reply

Award

Share

u/HyenaLaugh95 avatar
HyenaLaugh95
•
22h ago
Thanks! I'll look into it. Did you learn how to use it from any guides or you promoted ai to learn more?

Upvote
1

Downvote

Reply

Award

Share

u/imnotdansih avatar
imnotdansih
•
22h ago
🔆Pro Plan
Just install the repo. There are hooks and stuff that do all the work. It works right out of the box. Its God's work 😎

Upvote
1

Downvote

Reply

Award

Share

u/imnotdansih avatar
imnotdansih
•
23h ago
🔆Pro Plan
https://orchestra.s3v.no/

Upvote
0

Downvote

Reply

Award

Share

ChemicalExample218
•
17h ago
You can just do it without obsidian . . . Or git. It works well. You can alter the schema however you want. . . . It's just a bunch of markdown files. Lawd.

Upvote
1

Downvote

Reply

Award

Share

yezzer
•
1d ago
I use a combination of an obsidian second brain with a few custom skills and GitHub issues. Works really well, but interested in improvements.

Upvote
2

Downvote

Reply

Award

Share

u/TySocal avatar
TySocal
•
1d ago
Comment Image
I just leave that here. This is spot on.

Upvote
2

Downvote

Reply

Award

Share

u/PM__ME__BITCOINS avatar
PM__ME__BITCOINS
•
1d ago
You want memory with concurrency, consistency, hash collision checks, undo, roles and permissions? Congrats you just described problems solved by a database from 1984.

Upvote
2

Downvote

Reply

Award

Share

HippyDave
•
1d ago
I use [agent-memory](https://github.com/rohitg00/agentmemory) - it works pretty good if you get your hooks set up right. It maintains a local database of deliberately saved memories and session histories.

Upvote
2

Downvote

Reply

Award

Share

dat999zx
•
10h ago
u/zeesshhh avatar
zeesshhh
OP
•
1d ago
Thanks will check this out.

Upvote
1

Downvote

Reply

Award

Share

u/foomanjee avatar
foomanjee
•
18h ago
agentmemory is good but it has a lot of bugs and performance issues with a large database. I'm maintaining my own fork with the fixes and improved performance

https://github.com/davidrobertson/agentmemory

Upvote
1

Downvote

Reply

Award

Share

oh_jaimito
•
22h ago
I ended up building my own instead of relying on a hosted tool. Claude Code hooks (PostToolUse + Stop) write to a local Postgres DB — raw tool-call observations flush every ~10 events or 30s, so it's close to real-time, and a full narrative session summary gets written when a session stops. An MCP server sits on top exposing actual search tools (memory_search, observation_search, etc.) instead of one black-box "relevant context" blob.

The part that actually matters: my CLAUDE.md mandates a memory-first search before Claude answers anything referencing past work — it's not passive retrieval, it has to go query the DB. That's probably the core issue with your Mempalace experience — if the tool decides what's "relevant" for you with no visibility into the ranking, you get exactly that 900:1 noise problem when its judgment doesn't match what you actually needed.

Downside: it's not a 5-minute install, I'm maintaining hook scripts and a database myself. But I get full control over what's stored and how it's retrieved instead of trusting someone else's relevance algorithm.

I use Arch BTW.

Upvote
1

Downvote

Reply

Award

Share

u/pesky-tiger avatar
pesky-tiger
•
21h ago
What problem are you trying to solve? Are you trying to be friends with the ai or work with it?

Instead of wasting a bunch of context on nonsense I prefer work together with them in markdown documents. It’s like a living shared usable memory system that doesn’t go stale.

Helps stop me from going stale too

Upvote
1

Downvote

Reply

Award

Share

dat999zx
•
9h ago
Aggravating-Start307
•
8h ago
Hi, As someone who ran into this problem, i built a solution for myself. I figured that saving knowledge after some tasks with meaningful search aliases or code shaped aliases helps better retrieval when a similar task comes up. I have observed that over several runs, the accuracy of the notes fetched is 47% (self reported, not verified by others). Its open source and free. If you are interested, feel free to try it out. I created a website for it at https://coldstartmcp.dev .

I am also in the process of creating a methodology to evaluate if a tool that claims to be agent memory or something that reduces tokens is actually useful. A plugin i created https://github.com/AkashGoenka/convotokens is the first step in this direction. It just helps you find the number of tokens consumed inside a session. What you could do is run the same query with and without a tool in separate copies of the same repo (to avoid and risk of contamination) and just run the command and it gives you the actual tokens consumed in a session

Upvote
1

Downvote

Reply

Award

Share

u/XAckermannX avatar
XAckermannX
•
19h ago
I tried claude mem and something in it broke my claude(couldnt even send any message to my claude as) that i asked codex to remove the plugin. I think i closed the localhost service that launched with it that broke it but that spooked me and stopped me from using it. havent tried anything else

Upvote
1

Downvote

Reply

Award

Share

u/techtheist_ggl avatar
techtheist_ggl
•
6h ago
Well, i'm trying to solve these problems. With dogfooding and other projects it works not that bad, i currently have 400 notes (they're generated by the same agent who do the work), and i have set of metrics that shows it's not bad - contradiction detection mechanism seems working, yet it's not perfectly reliable, but it helps many times already.
There's also tests, with longmemeval corpus and invented corpus focused on project development.

https://github.com/techtheist/engram

It's local, free, open source, allow multi-project work, multiple agents, and shared history linked to memories when it was made - so agent can always find the "memory note" and if there's not enough details, they can be found in related history.

Upvote
1

Downvote

Reply

Award

Share

u/AnlgDgtlInterface avatar
AnlgDgtlInterface
•
2h ago
I wrote and use http://github.com/georgeharker/cribsheet

It indexes code semantically. Allows attaching notes and semantically indexes them. Preserves long running plans and designs.

Upvote
1

Downvote

Reply

Award

Share

rubanbhatia
•
13h ago
I've tried a few over the past year
I’d pick claude-mem. its free and works naturally with Claude Code, and retrieves relevant session context without dumping everything into the prompt.

some of the others I tried are OpenWiki which is good for a maintained repo wiki, and Graphify for mapping relationships across a large codebase ongoing

Upvote
1

Downvote

Reply

Award

Share

jetsetter
•
14h ago
I build and use Contextify (https://contextify.sh) for all memory related matters on the fly.

You invoke it semantically: “look at how we solved this b problem on the macOS client /total-recall”

I still write durable project files on key project areas like ci and infra. Contextify makes all of your prior transcripts from Claude code and codex, across multiple machines, all available in a single invocation. AFAIK there is nothing else like it.

I’m about to drop the first windows client, otherwise current support is macOS and Linux.

Upvote
1

Downvote

Reply

Award

Share

u/kanine69 avatar
kanine69
•
15h ago
My process is relatively simple, it's standing the test of time though. I'm not one for writing long explanations but the folder structure should be self evident docs/work docs/issues docs/patterns docs/agentic-prompts docs/journals

In scripts/ I put repeatable scripts and helper scripts so the AI agents don't need to go hunting for credentials.

Upvote
1

Downvote

Reply

Award

Share

cla1067
•
17h ago
GitHub as source of truth and hindsight as main memory I have it connected to codex and Claude and works really well for me.

Upvote
1

Downvote

Reply

Award

Share

SilencedDuality
•
17h ago
I created an account on Supabase and worked with Claude to migrate a “memory” system from Notion into a Postgres database. Context, session summaries, open questions, descriptions. All stored in tables and tied back to a singular ID tied to a Claude Project. Been using it for months and haven’t come near the storage cap for the free Supabase account. Then in my system prompt I require a check of that database every time I begin a chat.

Upvote
1

Downvote

Reply

Award

Share

inefficientnose
•
14h ago
Combination of things: 1. Storybloq for ticket tracking 2. claude-mem for recent session context rollover 3. I have agents append an insights-log.md (just a normal markdown file) for long term memory of engineering problems we solve as we build

Upvote
1

Downvote

Reply

Award

Share

elnino-pl
•
1d ago
You can check my repo here: https://github.com/elninopl/agent-julia

It's a memory and persona that stay the same across Claude Code and Claude Desktop (Cowork)

Upvote
1

Downvote

Reply

Award

Share

Camaytoc
•
20h ago
•
Edited 20h ago
A few things to put in place, but in my current project, some are:

A central hub to fix determinism of system prompts (pointers) from multiple harness/providers; tasks and bugs tracking from Open Project (closest to Jira full open source), all documentations on Obsidian, in house global agents identity system (open the door of all agents sessions memory), etc.

All of that customized to the way we are proding. I see no other tempting system out there that worth spending time adapting.

The good thing is that this topic among many other are at the applicative frontier rigth now. There's no standard. You have to feel free to design your own pipeline. Yes, looking around is good, getting inspired is good, but feeling lost and unable to grab the bull by its horns should be avoived.

Let's move and keep our projects to drive our designs, not the other way around!

Upvote
1

Downvote

Reply

Award

Share

phatchamp
•
17h ago
I made my own spin off of Garry Tan’s gbrain and of all the things I’ve done with Claude, it has been the single most impactful.

Upvote
1

Downvote

Reply

Award

Share

kepners
•
1d ago
For me. Have an agent set up to call and use memory. Its job is memory. Then claude.md is instructed as part of process to use that agent. And then embed the agent in plans. Work ok.

Upvote
1

Downvote

Reply

Award

Share

u/zeesshhh avatar
zeesshhh
OP
•
1d ago
Oh so you have a agent that manages the memory, nice.

Upvote
1

Downvote

Reply

Award

Share

SecretSquirrelSquads
•
1d ago
I use obsidian and slack. The agents have an account and I another - every agent needs to read slack before the session and write a dispatch on slack after the session. Permanent stuff goes in Obsidian.

Upvote
1

Downvote

Reply

Award

Share

u/TargetCold4691 avatar
TargetCold4691
•
23h ago
I wrote something specifically for my workflow. I have a home desktop, a work desktop, and a laptop. I run windows and wsl on all and share all projects on each. Im also using the claude code extention for VsCode on each. I keep the same folder layout on each. To keep all in sync I have built an mcp server that stores my claude.md, skills, plug-ins settings.json, memories, etc. in an rds db. Upon opening a project all of these files except the memories are created, over writing the existing. Any changes to them will be caught and uploaded to the dB to be shared on the other systems. All data is non vector in the except for memories. Claude.md specifically points to memories through the vector db portion of the PostgreSQL hybrid db.

It was a pain to create but works well for my needs.

Upvote
1

Downvote

Reply

Award

Share

ItsJustManager
•
23h ago
I made a project management app that serves as a UI for me and memory for the agents. It's open source, can run locally or be hosted with docker. It's also available for Unraid in the Community Apps plugin. https://github.com/perpetualsoftware/pad

Upvote
1

Downvote

Reply

Award

Share

DrakoChack
•
15h ago
We use https://jubarte.ai in all of our projects

Upvote
1

Downvote

Reply

Award

Share

u/Mtolivepickle avatar
Mtolivepickle
•
21h ago
🔆 Max 20
Obsidian vault with semantic searching

Upvote
1

Downvote

Reply

Award

Share

Cuz1
•
15h ago
I just use a small sql lite dB to store "memories" as markdown files. I use a lightweight ML embedding model to retrieve the notes via an mcp server.

I just say "hey mermaid, I had a memory the other week of a project i was doing in java". That description goes through the mcp server, hits the ML model and sends back notes. ML model is pretty accurate to.. I have 100's of notes with similar content and it always returns the right one.

Upvote
1

Downvote

Reply

Award

Share

mannyocean
•
15h ago
i just use google sheets and docs to keep track of notes and implementation details. simple, easy to access and review, and replicable. I combine that with a google workspace MCP for claude to access.

Upvote
1

Downvote

Reply

Award

Share

martin_xs6
•
1d ago
Made my own implementation of this: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

It's the first one I've found to be actually useful. Nothing fancy, just the LLM maintaining some wiki pages. Have commands for read and write to make sure the rules are followed

Upvote
1

Downvote

Reply

Award

Share

u/Vesuvius079 avatar
Vesuvius079
•
17h ago
We use openspec with a modified flow. It’s not perfect but having the specs around gives it something to reference and work off of. It is likely to see related specs during the proposal phase.

Upvote
1

Downvote

Reply

Award

Share

Runfree33
•
2h ago
I use my own fw : https://github.com/runfree337/Yet-Another-Memory-System :)

Upvote
1

Downvote

Reply

Award

Share

sutcher
•
18h ago
I just spin my own. Takes about a day to get up and running. Just txt files in directories with some frontmatter.

Upvote
1

Downvote

Reply

Award

Share

u/mpbeau avatar
mpbeau
•
21h ago
I have claude integrate with my other task trackers (jira cli at work, todoist cli for my personal projects) but that's about it - agents also regularly forget or loose track of tasks (which happened for basically all task management systems including agent specific ones I used), so you still gotta clean up after them...

Upvote
1

Downvote

Reply

Award

Share

vassyz
•
23h ago
I've been using https://github.com/thedotmack/claude-mem . I'm not sure what will happen if I disable it, as I personally find it quite hard to follow the benefits it brings.

Upvote
1

Downvote

Reply

Award

Share

Serird
•
20h ago
Basic Memory. It's okay, I can put .md files, self host my stuff, it's working cross harness and I don't have to pay for it.

Upvote
1

Downvote

Reply

Award

Share

u/School-Illustrious avatar
School-Illustrious
•
21h ago
Try Hindsight! It’s fantastic

Upvote
1

Downvote

Reply

Award

Share

u/mandibleface avatar
mandibleface
•
15h ago
MemPalace has been pretty amazing. Going in with an updated chromadb makes multiworkstation actually work now.

Upvote
1

Downvote

Reply

Award

Share

u/AwakE432 avatar
AwakE432
•
22h ago
QMD

Upvote
1

Downvote

Reply

Award

Share

Fiyero109
•
1d ago
What’s wrong with the built in memory builder

Upvote
0

Downvote

Reply

Award

Share

Aggravating-Start307
•
7h ago
Personally i use the built in one when i am working on a long feature work that would take a few days so that i can always start in a new chat. But the issue is you really have to maintain it or ask an agent to make updates to keep it accurate and fresh. And since this memory is fed into every conversation, it may not be always relevant and would often need to be cleaned up or archived so that its not pumped into every new chat

Upvote
1

Downvote

Reply

Award

Share

u/zeesshhh avatar
zeesshhh
OP
•
1d ago
It's insufficient

Upvote
0

Downvote

Reply

Award

Share

Fiyero109
•
1d ago
What applications is it failing at. Are your core rules set to update memory often? Are you creating local handoff documents? Perhaps asking it to create a wiki of your project or website and update that can help

Upvote
2

Downvote

Reply

Award

Share

u/zeesshhh avatar
zeesshhh
OP
•
1d ago
I never thought to tell it to update it's memory, my bad.

Yes I am creating local handoff docs.

No I have not tried wiki, will try creating wiki.

Thanks for the suggestions.

Upvote
2

Downvote

Reply

Award

Share

u/Veduis avatar
Veduis
•
1d ago
asking the thing that failed to evaluate itself is bold but honestly the 900:1 ratio tells you everything. retrieval that bad is worse than no memory at all, because at least with no memory the agent doesn't confidently recall the wrong thing. hermes is worth a shot, the memory system is the main reason people use it. there's a decent beginner's guide to hermes if you want to skip the setup fumbling. temper expectations though, every memory tool demos great and degrades quietly by week three.

Upvote
0

Downvote

Reply

Award

Share

Hungry-Restaurant-88
•
1d ago
Not to hijack but are most of you doing handoffs at context limits or compacting your main planner agents?

Upvote
0

Downvote

Reply

Award

Share

Hungry-Restaurant-88
•
1d ago
Not to hijack but are most of you doing handoffs at context limits or compacting your main planner agents?

Upvote
0

Downvote

Reply

Award

Share

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
