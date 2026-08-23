---
id: "article_3d18561d"
title: "Is Superpowers Still Relevant"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "trends"
tags: [superpowers, claude-code, ai-workflows, token-optimization]
summary: "Developers debate the relevance of the Superpowers skill set for Claude Code. Some users find high token costs and strict workflows unnecessary with newer, smarter models. Other users prefer extended forks and custom hooks to orchestrate multi-model workflows efficiently."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Developers debate the relevance of the Superpowers skill set for Claude Code. Some users find high token costs and strict workflows unnecessary with newer, smarter models. Other users prefer extended forks and custom hooks to orchestrate multi-model workflows efficiently.

## Key Takeaways

- Newer models reduce the need for strict scripts and complex guardrails.
- Users report high token consumption and slower workflows when using Superpowers.
- Bounded autonomy allows models to think and execute tasks with greater freedom.
- Some developers switch to lighter workflows like Matt Pocock tools or custom ADR processes.
- Extended forks use environment hooks to split tasks across expensive and cheap models.

## Techniques / Prompts Extracted

None identified.

## Full Content

Is Superpowers still relevant?
Discussion
I’ve been using Superpowers skill set for the past year with CC. Mostly i like the brainstorming mode and a few of the TDD and subagent related skills.

Are others still using Superpowers or do all the improvements in CC negate the need for this set of skills? I’m curious if I can save more tokens this way?

I’m mostly using Fable and Opus with high thinking.

Upvote
146

Downvote

68
Go to comments

Repost

Share
Join the conversation

Sort by:

Best

Search Comments
Expand comment search
Comments Section
u/Remarkable_Mud9885 avatar
Remarkable_Mud9885
•
1d ago
I'm starting to delete a bunch of skills because I feel like sometimes they interfere with my work and also mess with the model's judgment. That's just my take. We can keep a few that you think are useful.

Upvote
124

Downvote

Reply

Award

Share

x_typo
•
1d ago
•
Edited 4h ago
Senior Developer
This is me as well along with a lot of my custom skills. I'm starting to realize that AI right now is a lot smarter than we give it credit for.

Just do "bounded autonomy" like giving it a map and the direction you want it to go instead of turn-by-turn.

Updates: I'm not talking about delegating your thinking to AI. I'm talking about instead of adding strict instructions/scripts for it to follow to the point where throwing a pin needle in the machine will cause it to break down.

Loose it up a bit and let it think for itself.

That's where AI really shines.

Upvote
15

Downvote

Reply

Award

Share

u/Winter_Seaweed_4836 avatar
Winter_Seaweed_4836
•
9h ago
Yeah, giving too strict guardrails and using absolutes "NEVER,DONT,EXACTLY" as prose has diminishing returns, it takes the "freedom of thought" away from the model. I created a guardhook that blocks recursive deletes and my session discipline hook enforces routing around the guardhook and controls the work ethics. Laziness, hallucinations, jargon outputs can all be fixed quite easily. Causal testing to the guardhook is also recommended since it can simulate the possible route arounds the hooks and you can patch them before them ever happening. I have actually tried to force my harness to delete something in multiple different ways and it just wont do it without my authorization password. Sorry for the braindump, i could write all day on my methods on how to make model outputs precise, safe and "trustworthy". Trust but verify.

Upvote
2

Downvote

Reply

Award

Share

u/Remarkable_Mud9885 avatar
Remarkable_Mud9885
•
1d ago
Yeah, I think you really need to enjoy the process of discovering your own skills. It gives you such a strong sense of achievement because you realize that as AI gets more and more powerful, you end up participating in fewer and fewer things.

Slowly, your communication with the AI dwindles until you have no idea what it's doing, and it has no idea what you're doing.

Upvote
4

Downvote

Reply

Award

Share

u/Winter_Seaweed_4836 avatar
Winter_Seaweed_4836
•
10h ago
Make the skills as a sessiondiscipline hook that uses all the "skills" for you and they travel with session and gets used dynamically. You can delete the old and obsolete skills.

Upvote
1

Downvote

Reply

Award

Share

Time_Cat_5212
•
2h ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Knew this would happen

Upvote
1

Downvote

Reply

Award

Share

seatlessunicycle
•
1d ago
I haven't used superpowers in months. I'm on the matt pocock bandwagon!

Upvote
48

Downvote

Reply

Award

Share

u/knot_why avatar
knot_why
•
1d ago
Please do tell more. Haven't heard of him. Googled now, I see he has some AI dev workflow, but would like to hear from the community before I go and and listen to hours of videos.

Upvote
7

Downvote

Reply

Award

Share

seatlessunicycle
•
22h ago
His hour long talk is GOLD. It changed my whole personal workspace setup

Upvote
8

Downvote

Reply

Award

Share

Gryphx
•
22h ago
Can you share a link to it?

Upvote
4

Downvote

Reply

Award

Share

seatlessunicycle
•
21h ago
Bro just type in Matt Pocock workflow.

Upvote
0

Downvote

Reply

Award

Share

Gryphx
•
21h ago
Because he only has one video….

Upvote
12

Downvote

Reply

Award

Share

seatlessunicycle
•
21h ago
https://youtu.be/-QFHIoCo-Ko?is=rGBQ4VdZWZcduJTl

Upvote
20

Downvote

Reply

Award

Share

Gryphx
•
5h ago
Thank you!

Upvote
1

Downvote

Reply

Award

Share

u/Seerix avatar
Seerix
•
5h ago
I use a tweaked version of his grill me skill. Only global skill i use. Works well!

Upvote
1

Downvote

Reply

Award

Share

alOOshXL
•
1d ago
I still use it
it take a lot of tokens but get the job done verytime

Upvote
49

Downvote

Reply

Award

Share

YUL438
OP
•
1d ago
i use it for everything everytime as well and it hasn’t steered me wrong. just curious if the newest models are smart enough to achieve these same things on their own.

Upvote
16

Downvote

Reply

Award

Share

fschwiet
•
1d ago
You definitely get more careful planning from it, I found planning mode jumps to a solution to quick- brainstorming will explore some alternatives. That said grill-me does a better job of that.

Upvote
5

Downvote

Reply

Award

Share

alOOshXL
•
1d ago
/brainstorming + /grillme-with-docs = wonders

Upvote
16

Downvote

Reply

Award

Share

u/tribat avatar
tribat
•
17h ago
Haha I was a little anxious about looking dumb for still using both, but when it’s a critical feature I use both.

Upvote
3

Downvote

Reply

Award

Share

Fun_Union3580
•
2h ago
So, do you use the to-spec and implement commands?

Upvote
1

Downvote

Reply

Award

Share

u/OkayVeryCool avatar
OkayVeryCool
•
1d ago
How do you do the grill me with docs? Do you do grill me once you have a design spec from superpowers?

Upvote
1

Downvote

Reply

Award

Share

alOOshXL
•
1d ago
no
i just start the chat with /brainstorming + /grill-with-docs
it write both spec + context.md

Upvote
6

Downvote

Reply

Award

Share

SurfGsus
•
16h ago
Yeah but do you get frustrated with the heavy workflow? I feel like the brainstorm, spec, plan “ceremony” just takes way too long. I switched from superpowers to ADRs + Matt pocock’s grill me with docs. Seems to work well and a lot less time intensive. Still not 100% happy with the flow though.

Upvote
2

Downvote

Reply

Award

Share

u/Winter_Seaweed_4836 avatar
Winter_Seaweed_4836
•
10h ago
Specdriven development is good overall and ADR is oldschool and decent solution. You can try to turn the ADR's and "Specs" into AskuserQuestions that emit decision logs that carry the both. After doing that you can create tasklist of those ADR's in managable atomic tasks. Run advesarial and silentfailurehunter subagents after each task. You need to create a session discipline hook to have a workflow fitting your working style and testing methods that create dynamically rated severity findings log.

james__jam
•
18h ago
Not using it also gets the job done.

HgnX
•
1d ago
Too token intensive, Fable is smart enough without it

mandark69
•
23h ago
I am using it all the time. But let it outsource all coding tasks to codex (gpt5.6). My workflow for superpower is:
Brainstorm (fable) -> specs -> spec review codex -> plan -> plan review codex -> codex implements -> holistic review by fable & codex. When both agree on ‘safe to deploy’ and I agree too, it is finished. Fable or Opus orchestrates all of this.

helm71
•
1d ago
I use if every time.. fable on high or xhigh with superpowers to create the plan, opus5 to execute and orchestrate, sonnet5 for the actual coding.

u/EnthusiasmMountain10 avatar
EnthusiasmMountain10
•
1d ago
whats your token spend like on a feature getting delivered in a day for eg?

helm71
•
22h ago
Honoustly I have no idea… I am on max20 and that basically lets me code almost 7x24.. tokens run out on the last day…

u/tribat avatar
tribat
•
17h ago
The ideal

Upvote
1

Downvote

Reply

Award

Share

rubanbhatia
•
13h ago
It’s good if it didn’t create huge markdown files again and again and doesnt do TDD for every minor change.

What superpowers needs is something like a persistent project spec that can track phases and updates instead of scattering them in random named markdown files.

The brainstorm workflow needs to be tighter and should help create an initial PRD rather than just refine your idea.

Still relevant but needs some edits now

Upvote
2

Downvote

Reply

Award

Share

kardu
•
1d ago
brainstorming is definitely good.

I'm not sure if the other ones are worth keeping. It might depend on your project

Upvote
7

Downvote

Reply

Award

Share

beardedslav
•
1d ago
I found brainstorming really good, but I think https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs is much better

Upvote
9

Downvote

Reply

Award

Share

itsforsocial
•
1d ago
•
Edited 1d ago
Currently it eats lot of usage when sub agent driven development kicks in. Not using that as entire session gone in 5 mins. Spec then agent-skills for plan and build part. This works fine for me now

Upvote
12

Downvote

Reply

Award

Share

Obvious_Equivalent_1
•
1d ago
That was something I ran into with the latest 5 version of Obra/Superpowers. I can only speak for my own experience but I believe a lot of that has been addressed in a fork Superpowers extended for Claude Code, already maintained since last year with native optimizations https://github.com/pcvelz/superpowers (see release notes and readme MD’s)

Happened to wrote extensive reply about it, major benefits are the hooks it allows you to use separate Claude code sessions to keep plan mode part in a higher expensive tier like Fable en run execution on a cheaper like Opus 4.* or Opus 5 on medium. https://www.reddit.com/r/ClaudeCode/comments/1vub8nl/comment/p4zzl21/?context=3

Upvote
13

Downvote

Reply

Award

Share

throwawayfapugh
•
1d ago
I use the pcvelz fork too and it’s great

Upvote
5

Downvote

Reply

Award

Share

Obvious_Equivalent_1
•
14h ago
Delighted to hear that. Make sure if it’s been a while that there are some updated features you might like (all optional)!

(because I’m writing this reply anyway, I’ve recently written extensive post. With recent Claude Code native features released, these new hooks allow to benefit from this. You can run write plan on token heavy Fable med/high and execution of plan on like Opus 5 low/medium. The hooks both help enforce subagent model+thinking level (low/medium/high/..), it includes that if you ask in plan to verify certain steps, that with hooks enabled it actually to force Claude to stop and verify with you. And if you execute plan in a separate session the execute plan can actually talk to the write plan session - if you enable it in onboarding)

/plugin marketplace update superpowers-extended-cc-marketplace
/superpowers-extended-cc:onboard

Upvote
2

Downvote

Reply

Award

Share

jagibers
•
1d ago
FWIW, when opus 4.7/8 went to 1M context and cc defaulted to that model/context size —I started hitting the session limits right away because I was doing multiple sessions/tickets at once. I did some research and found that you can set a an env variable to disable the 1M context for it and proceeded to run with that. When opus 5 came out I tried it for a bit without quotation issues but it was just doing terrible. So I’m still using 4.6 w/ 200k context to date with great results in a large brownfield repository with lots of concurrent sessions and never hit my session limits I do typically hit a compaction break in sessions that do a lot of research or systematic debugging—but it is not usually an inconvenience as I usually have another session I can jump to and provide direction to.

So I’m still firmly in the superpowers camp.

Upvote
3

Downvote

Reply

Award

Share

u/Winter_Seaweed_4836 avatar
Winter_Seaweed_4836
•
9h ago
Make opus use explanatory output and verbrose off and xhigh for implementation and only escalate to max when planning.

Comment Image

Upvote
3

Downvote

Reply

Award

Share

JupiterWalk
•
22h ago
The question isn’t if superpowers is relevant or not, but rather do you have other sources of similar context that overlaps, whether that be Claude.md, other skills, etc. it’s not black and white. There’s a layered approach to LLMs. Superpower is one element. By itself, excelente. However I’ve instilled a process through tangibles such as project documentation and diagrams, memories, and so on that I no longer need to pay tokens (which very token hungry imho) for superpowers. It’s a great jumpstart skill no matter your experience level. It can lay proper foundation as you continue to use Claude. Ok bye

Upvote
4

Downvote

Reply

Award

Share

u/artofbullshit avatar
artofbullshit
•
1d ago
I still use it since removing it would mean that I wouldn't be able to trust that Claude actually followed a true TDD on every build.

Upvote
5

Downvote

Reply

Award

Share

james__jam
•
18h ago
Wdym? Tdd is one of the most basic skill and you dont need superpowers for it

Upvote
1

Downvote

Reply

Award

Share

u/artofbullshit avatar
artofbullshit
•
17h ago
Okay, so any skill. Guess I should have said I'm not comfortable removing all skills from Claude and letting it do whatever it remembers to do on its own, because it won't.

u/WaltzEmbarrassed6501 avatar
WaltzEmbarrassed6501
•
1d ago
No longer using it, I switched to Wayfinder from Matt’s skill plugin instead. I like the flow better.

pmward
•
1d ago
I built my own versions long ago, that work better for me and my companies specific workflows, and are a lot more token efficient. It's so quick and easy to build your own tools to fit like a glove, that it honestly feels silly to shoehorn yourself into someone else's tools.

DLuke2
•
19h ago
Dropped it. Mostly goal style prompts now and loops when needed.

Goal prompts are the most effective now it seems. Give references, examples, and/or spec/design doc and let it cook. Having rules, model invocable skills, knowledge docs, etc keeps everything on the rails.

u/Potat4o avatar
Potat4o
•
23h ago
Superpower has been doing a pretty good job of keeping up. Like this release: https://github.com/obra/superpowers/releases/tag/v6.1.0

u/Professional-Money49 avatar
Professional-Money49
•
21h ago
I really like superpowers but it brings out the worst in opus 5. Matt copocks skills work much beter with it.

No_Holiday_5717
•
20h ago
Game Developer
If only it didn’t 3x the time and tokens required for a task…

u/Icy-Excitement-467 avatar
Icy-Excitement-467
•
1d ago
Code review is the onlything consistently useful

Ill-Village7647
•
1d ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
The only skill that I've used the most is the /requesting-code-review superpower. It's terrific

u/jpvaldezjr avatar
jpvaldezjr
•
14h ago
difference than the built in code review?

Ill-Village7647
•
11h ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
The built in code review takes way too much time. Spins up multiple sub agents.

This one only spins up one agent. And I've gotten better results from this plugin compared to that one. The built-in one is also token hungry and expensive.

Upvote
1

Downvote

Reply

Award

Share

u/cartoonist498 avatar
cartoonist498
•
1d ago
Nope, I stopped using it because the token cost and extra time to go through its flow was so high, at what seemed like little to no gain in the end result.

I use Fable as the orchestrator and have it spin up Opus 5 subagents to do the work. Superpowers didn't seem useful anymore.

Upvote
2

Downvote

Reply

Award

Share

codyswann
•
3h ago
Skills are going through the same phases MySpace went through.

Upvote
1

Downvote

Reply

Award

Share

u/brycematheson avatar
brycematheson
•
18h ago
I removed it. Fable + Codex adversarial review does a great job, in my opinion.

Upvote
1

Downvote

Reply

Award

Share

Bright-Celery-4058
•
10h ago
Profile Badge for the Achievement Top 1% Poster Top 1% Poster
try this https://github.com/PiLastDigit/TRIP-workflow
IMO better and easier to use

Upvote
1

Downvote

Reply

Award

Share

Time_Cat_5212
•
2h ago
Profile Badge for the Achievement Top 1% Commenter Top 1% Commenter
Skills are the new domain of cargo culting

Upvote
1

Downvote

Reply

Award

Share

u/tribat avatar
tribat
•
17h ago
I’ve been stripping down some skills but superpowers changed the way I use Claude code. I’ve built around it, but it’s muscle memory now.

Upvote
1

Downvote

Reply

Award

Share

Icy_Preparation_25
•
1d ago
Try not to use it with newer and powerful models,

i use kimi k3 for some important tasks and 99% of the time task is always done correctly and its ready to deploy but with older models or cheaper models its always use superpowers and still it 70-80% success rate.

Upvote
1

Downvote

Reply

Award

Share

novakane
•
22h ago
What do we do with skills that are tied to existing automations/recurrent tasks?

Upvote
1

Downvote

Reply

Award

Share

u/allemaar avatar
allemaar
•
1d ago
Researcher
I usually have an idea of what I wanna build.

Thus using a set of smaller skills in various combinations does help a bit more and I can both learn (new angles). This helps me steer to the intended goal , or hop to a new shape that might be better.

I use a combination of exploration, investigation, angles, multi-pov assessments and cold-reviews (via subagents). This so far gave best results, lowest cost. Adding a second agent (different vendor) increases the brainstorming output quality even more.

Upvote
0

Downvote

Reply

Award

Share

Anooyoo2
•
1d ago
Build don't buy. You need to know your system.

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
