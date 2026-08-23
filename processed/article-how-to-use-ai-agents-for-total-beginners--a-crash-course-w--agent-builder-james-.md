---
id: "article_a948e85d"
title: "How to Use AI Agents for Total Beginners: A Crash Course w/ Agent Builder James McAulay"
source_type: "article"
source_url: ""
author: "The Neuron"
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [ai-agents, workflow-automation, model-context-protocol, agent-skills]
summary: "AI agents need three components to function: an LLM brain, context files, and software integrations. Users can build proactive agents using Claude Co-work or Claude Code combined with Model Context Protocol connectors and markdown instruction files. Setting up a second brain folder and specialized skills allows agents to execute routine business tasks automatically."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

AI agents need three components to function: an LLM brain, context files, and software integrations. Users can build proactive agents using Claude Co-work or Claude Code combined with Model Context Protocol connectors and markdown instruction files. Setting up a second brain folder and specialized skills allows agents to execute routine business tasks automatically.

## Key Takeaways

- An AI agent consists of an LLM brain, context data, and tool integrations.
- Static markdown documents give agents deep context about user goals and business history.
- Model Context Protocol standardizes how agents interact with external software applications.
- Agent skills package complex prompts into reusable, testable operational procedures.
- Cloud-scheduled tasks run background workflows without requiring the user computer to remain active.

## Techniques / Prompts Extracted

- create a task in my grant project to follow up with James tomorrow at 6 p.m.
- simulate 10 fictitious people going through the weekly retro skill using sub agents and reflect on the usefulness of the skill.

## Full Content

# How to Use AI Agents for Total Beginners: A Crash Course w/ Agent Builder James McAulay

**Author:** The Neuron

## Transcript

So, there's going to be a 20 second
countdown, but everyone should be
hearing us live. Welcome humans to the
Neuron AI live. [laughter]
Real quick, as you join us and load in,
um, please shout out in the chat where
you are watching from and maybe if you
haven't yet, if you could also share
what you want to learn agents to be able
to do. So, uh, I'm going to do a very
I'm going to do a very quick intro here.
I need to pause the actual
YouTube chat that I have on my side
window so I don't hear myself now that
that's done. Um, so yeah, today we are
covering a topic I'm really excited to
dig into. Uh, why? Because this is the
number one question we get asked every
week, which is how do I actually use AI
agents to save time in my business or
maybe your life or, you know, just
anything you want agents to do because
work doesn't need to be everything. So,
uh, for example, I see a lot of moms who
use agents to help them keep track of
their schedules and their kids schedule.
And there's plenty of ways you can use
agents just for fun, too. But obviously,
you know, everyone wants to be able to
use agents in business. And so, today,
uh, as you can see, we are missing Corey
because he's on a muchdeserved vacation.
So, I decided to bring on a very special
guest to help us navigate all things
Agentic, and that is James Matel. And
James is the founder of Agent
Accelerator or the Agent Accelerator.
Um, and he's going to provide a
practical crash course on everything you
need to build helpful proactive agents
inside cloud co-working cloud code. So
James, welcome to the Neuron.
>> Thanks for having me, Grant. Uh,
firstly, yeah, I'm in awe of like the
number of people you have like
[laughter] reading the Neuron and
watching these videos. So, like, yeah,
thanks for having me and well done on
like everything you've achieved so far.
>> Oh, yeah. Yeah, I appreciate it. Yeah.
Well, I'm really impressed with you
because, you know, obviously you
formerly were working at 11 Labs and,
you know, helped them grow from 110
million in annual recurring revenue all
the way to 300 million. Um, and then you
launched a fully AI native business that
reached what was it 80,000 80k in
monthly revenue by month three. And then
by month five, I think it was 200k plus.
Is that right?
That's that's that's pretty much right.
Yeah, I can't remember the kind of pound
to dollar conversion rate, but um yeah,
it's grown way it's grown way faster
than I expected. And like a huge part of
that has been building, you know, as you
said, an AI native company like with
agents kind of from day one. Um, that's
like a whole other conversation we could
have, you know, like how do you how do
you structure all your tools and all the
software you use in a way that Claude or
any agent can sort of get work done for
you? But yes, broadly it's grown quite
quickly with me and Claude code. Yeah.
>> Yeah. You did it all without a single
employee or a dollar of paid advertising
at least to start and that's like holy
smokes like that's amazing. So clearly
you are very good at delegating work to
multiple AI agents every day. And today
we're going to learn all about how you
do it. So I'm very excited. [laughter]
>> All right. Well, yeah, I have a lot I
want to get through. Um I I think this
will take about an hour. Um we'll see
how far we can go. Um and yeah, I'm
going to let me share my screen and we
can just like kick off. Um, so,
>> uh, if I let me just make sure I choose
the right screen first of all.
[laughter]
>> So, can you see? Yeah. Can you see this?
Has that come up yet?
>> Yes, we see today from chatbot to agent.
>> Perfect. Okay. Perfect. Um, right. So,
I'm going to I'm going to walk through
like four fundamental concepts that I
think everyone needs to understand. Um,
and then we're going to like piece it
all together and we're going to create a
chief of staff. Um, a chief of staff
that is able to get work done um,
without you prompting it. So, it's going
to be, you know, proactive. And
crucially, the thing that I think is
really exciting is that this will work
without you needing to leave your
computer on. So, um I'm sure a lot of
people know that like Claude Cowwork has
scheduled tasks and until very recently
they required you to leave the computer
running 24/7. This is why a lot of
people went out and like bought, you
know, Mac minis so that they could run
Open Claw around the clock. Um
>> but they recently announced a feature
that's still in beta, but it's called
cloud scheduled tasks. Um and I'll get
into the specifics of that, but we're
going to build Yeah. a chief of staff um
for you, Grant. I've actually I've had
some agents
>> Yeah. Yeah. I've had some agents run
away and do some research on you. And
I'm going to use you as an example and
try to make this as sort of interactive
as possible. Um and
>> yeah, as people are following along,
like if you want to sort of like copy
this yourself, I've put together a whole
bunch of skills. One of them is called
Set Up My Second Brain, and you can get
it on this URL here. So I let's let's
kick off. Let's get started. Um
fundamentally I just want to demystify
like what an agent is, right? Like this
is the kind of zeitgeisty word of 2026.
Um and like really I think of an agent
as like three components. It it has a
brain, right? It's got an LLM, whether
that is an anthropic model, whether
that's an open AI model. It's got an LLM
doing some thinking. It has context
about you uh or your business or ideally
both. And crucially, this is like the
main difference between a chatbot and an
agent. An agent can actually get work
done and it does this by connecting to
whatever software platforms you're using
in your business. And so like my whole
like all of my teaching is sort of
getting people to move away from talking
about work with a chatbot where the
chatbot says I think you should do this
to delegating work where the agent comes
back and says you know I've finished the
report I've drafted the email whatever
it is that's helpful. Um and so we can
think about that you know the brain the
context and the tools like this. Um and
I think most of us are aware of you know
conversation context like with the
context window. Um often we run out of
context if we uh have a very long
conversation and some uh systems like
claw chat and um and chatbt they have
this notion of like automatic memory. So
they'll sort of remember one or two
facts about you. Um, but I I try not to
rely on this automatic memory. Instead,
what we want to rely on is like
documents, right? Like I call them
static documents.
>> Can you zoom in a little bit more on
this because this one's
>> Yeah, sure. Sorry. Yeah. So,
>> you're good. Um so yeah we have like the
automatic memory and then we have um to
begin with I'm just going to talk about
like static documents like text files
that we give to an agent so that it has
context and we [snorts] also have system
instructions that like kind of define
the behavior of the agent right and we
say to Claude or ChatgPT you are my
chief of staff like here is how you
behave and then they can also read data
from places like you know Google drive
or notion. Um, and I'm going to skip
over some of this stuff because there's
a lot to get through. Um, but the main
thing I want to talk through really is
like the importance of context, right?
And the more context your agent has, the
more helpful and the more accurate its
replies are going to be. And I have this
analogy where I said, you know, imagine
you had just met a CFO.
um you'd given them no information about
your business. You just sat down for
coffee and you just kind of asked them
some questions off the top of your head,
right? So, you've met the CFO, they're
brilliant, and you said, "Hey, like what
do you think I should do with my
business?" Um, and they're just going to
give you like textbook, you know,
generalized advice, right? They're
probably going to spend this whole
coffee actually just asking you
questions to understand your business.
Um, and I've used this silly example of
the CFO saying, "You should decrease
your costs and [laughter] make more
revenue."
That is,
>> yeah, that's all there is to it, right?
>> That's great, great business advice and
you can you can have that for free. Um,
so [laughter]
this is the experience that loads of
people are having if they just open up,
you know, chat GPT and it has no context
on them. they get textbook advice or
chat GPT asks loads of questions um to
kind of understand more about you.
Scenario B is before you meet this CFO,
you actually send them like all of your
accounts. um you send them like readonly
access to Stripe and to Zero or
QuickBooks and now you sit down and
straight away they've got you know a
really good understanding of your
business. They can see that you know
cash flow is good but you're spending
too much on card processing fees for
example and that might be the first
thing they say to you and then you have
an hour of really valuable conversation
because they arrived with all this
context and access to your data. And so
these are the types of conversations we
want to have with agents. And that's
possible when we give them loads of
context. So another analogy that I like
to use, let me just jump back a little
bit, is this idea of like speaking to a
coach that has kind of bad memory. Um,
and so again, this is the experience
people have when they're talking to chat
GPT without good integrations, without
good context. They're, you know, in this
case it's a pilot. They're talking about
their work with this coach and they're
talking about things that happened in
the past. And if they want to talk about
a specific flight, they have to kind of
bring all the flight logs with them or
they have to like paste the data in to
chat GPT. And this coach remembers some
stuff and forgets most stuff. So you
might sit down and the coach will
remember a few details from the last
session but like doesn't remember the
whole session. And again this is the
experience people are having with kind
of out of the box chat bots. What we
want is a co-pilot right? We want
something that's like got you know
access to live data context on us and
our business and it's able to actually
do things and like I'm going to just
keep hammering this point home. Like we
want our agents to actually like take
action. And so this this um co-pilot,
you know, it's been in the plane with
you. It can see all the live data. It
can see all the flight logs. It can
even, you know, update the flight plan,
complete some checks for you. Um this is
where we want to get to with our agents.
We are still flying the plane, but this
co-pilot is taking care of like a lot of
the the kind of admin and like the
checks and balances for us. Um, no. What
I think is so exciting about being alive
in 2026, um, is that building agents
used to require hiring extremely smart
technical people. like you had to hire
loads of engineers with PhDs, machine
learning expertise and and companies,
you know, but from 2010 to 2020, there
were like thousands of companies that
raised like hundreds of millions of
pounds to to build AI startups because
it took months just to get to an MVP.
Um, now progress has moved really
quickly and we can now create these like
custom agents that get work done, wake
up and do work like in the background.
We can do it all inside of anthropic and
open AI's ecosystems. Um, and we can do
it without needing a technical
background. Um, there are lots of ways
to build agents. You know, we've all
heard of OpenClaw, Hermes agent. Um, but
I think the easiest way for beginners or
just frankly like the easiest way to
build agents is to do it inside of for
me I do it inside of Claude and I run my
whole business in Claude code. I teach
most people how to use Claude co-work
first of all because I actually think
co-work's easier to get up and running
and actually like slightly less risky.
>> Are you using co-work or code Grant? Uh
I use code but for for non-code related
things I use co-work but I started using
co-work before I really really got into
code I would say
>> I think yeah I think co-work is like a
really good stepping stone between chat
and code um
>> I agree
>> yeah and and like you know codework has
fundamentally like the same engine as
code just with a few features
simplified. Um
>> uh real quick, so before we move any
further, can you just give a very brief
summary of everything you just said?
Basically, if I was repeating it back to
you, we define an agent as a system that
does what?
>> Yeah. So, I'm saying an agent basically
has an LLM as its brain, context, and
the ability to do things. And we're
moving from, you know, talking about
work with a chatbot to getting work done
with a a co-pilot or or an agent
basically.
>> And you're saying that we can do all of
this inside OpenAI and and Claude's
ecosystems. And you're saying you
recommend Claude Co-work. And what plan
are you on to do all of this that we're
about to do?
>> So, I'm on the max 5X plan. Okay. Um,
>> so I started out, I think, on $20 a
month, then quickly had to go to 90,
then quickly had to go to 200.
>> But I think the economics of that plan
right now are really good. Like, I think
you get a lot of tokens for that money.
And if you are
>> if you're putting agents to work in your
business, I think you can get way more
than $200 a month of of value from these
tools.
>> I agree 100%. I saw a crazy stat that
someone had four plans and maybe got
$64,000 worth of value [laughter] out of
it.
>> That's crazy. And
>> just wild, you know.
>> It doesn't surprise me. Actually,
doesn't surprise me. Um,
>> so yeah, let's let's kind of let's let's
get going. What I want to build is a
chief of staff for you, Grant. Amazing.
>> And um, basically, I have a skill. It's
called set up my second brain. And what
it does is it interviews you. And this
interview, if you do it properly, can
take, you know, like two or three hours.
But it basically asks about, you know,
your goals, uh, the role you have in
your business. It takes in your LinkedIn
profile. Uh, it does some research on
like your company and it puts together
like this small folder of files
basically. Um, and if I come back to
here, yeah, it's something a bit like
this. We've just got this little folder,
this context folder of files about us.
Um, now you might have heard of a second
brain, and that's a conversation for
another day, but I like to think of this
as like the start of a second brain,
right? This is just like a folder of
really valuable files that helps any
agent, in this case Claude, really
understand you and what you're trying to
achieve and like how you like to work.
And I've I've done this exercise now in
workshops with about 400 people. And
this one just always blows people's mind
when you go from Claude sort of knowing
bits and bobs about you to Claude like
really understanding what you're trying
to achieve, who you are, what your
company does, you just get dramatically
better results.
>> Um, are you still
>> Yeah.
>> Uh, do do you use Obsidian to manage
this at all to look at it or what do you
use? Are you just chatting?
>> I do. No, I do. I do. So, I actually I
sometimes use obsidian and I sometimes
use cursor and I sort of like alternate
between the two. Let me just show you.
So, I've put together an example for
you. Let me show you what all this looks
like. Um,
okay. Where are we? We are
um actually I'm going to open it in
Obsidian. Yeah, obsidian. So, I just
shared in the chat a link to this tool
and this tool is basically what's called
a markdown file reader and markdown is
the file type that agents use to talk to
each other or talk to you, right? So,
usually produces a markdown file.
>> Yeah. Yeah. And markdown files like
agents, they love markdown files
[laughter] like um it's a it's like a
very efficient it's a tiny file size.
Just a very efficient way. Here we go.
very efficient way of like letting
agents sort of read text files. Um, so
this is Obsidian got our files on the
left and
if I expand this, we've got some context
files that I have sort of simulated for
you. I have sent some agents off, ask
them to research you and I've sort of
made up some context for you just to use
as our our demo.
>> So we have background research on the
neuron. This like looks into the neuron
technology advice. This is actually like
an incredibly short version of what you
would get if you went through this like
set up my second brain prompt. Um, one
of the I think one of the most powerful
features in Claude, let me just show you
this quickly is in chat there's a tool
called research and if you switch this
on it will go and scan you know 300
sources to give you like a really deep
sort of report on anything you want. So
what we do is we actually ask Claude to
go and run a research task on ourselves
and our business and then it comes back
with like a really extensive version of
this. So we've got background on on you
and the company. Um this has just kind
of uh looked for some key people. I
think it's made up some and it's like
put me in as well as like a speaker. Um
>> yeah, I don't know if I've ever heard of
Priya. I mean maybe
>> she's I think she's made up. I think I
think she's a hallucination uh for the
purposes of the demo and Bright Loop is
a fictitious company as well. Um then
we've like exported your LinkedIn into a
markdown file. So now you know whatever
agent you're talking to understands your
whole career and knows about like what
you're an expert in, where you've worked
in the past. I remember the first time I
did this, you know, Claude suddenly
started saying to me, "Oh, you know,
you've done all of this before in this
role or like you can draw on your
experience from this company uh in this
project we're working on." Um, so we've
got that and then as you go through this
skill and you kind of answer Claude's
questions, it asks you, you know, about
your role, who you work with, um, what
you're responsible for and then it will
put together this kind of like role
profile on on you. And again, I think a
lot of this is might just be made up,
but this is what Claude sort of assumes.
>> Close enough. Close enough. [laughter]
>> Okay. Okay. Cool. Cool. Cool. Cool. Um,
so then we have this file called
claude.md.
Uh, very quickly, this is a file that
gets opened at the start of every single
conversation you have in this folder. So
claude.md is like the first thing Claude
sees. And it's a way of basically
overriding Claude's default behavior,
overriding Claude's default personality
and giving it like a new role or like a
new goal. So this is saying, you know,
you are actually chief of staff to Grant
and he has these four goals that we've
written out in this goals file. Um, and
here's what he's trying to achieve. And
like this is, you know, read these files
before you answer. like load these in uh
be direct uh follow up on commitments as
you know a chief of staff would do and
and so this file is like a map of this
folder it's like a sort of lay of the
land for any agent that arrives in this
folder if we open this folder in
codework or in code or even in codeex um
it would look at this file and it would
understand okay like this is this is who
I am this is what I'm trying to achieve
>> and then we also have
>> question in the chat to clarify
something here which I think would be
good which Yeah.
>> So they uh my AVI doll said, "Okay, I
think I get it. You feed the folder to
Claude every time." So does Claude read
this folder every time it does anything?
>> Yeah. So let's get into live demos. So
if I come into cowwork now, I'm going to
select uh that chief of staff folder. So
I've called it grant coos.
And now I'm going to say uh something
like help me plan my day. And
uh let me just untick that.
Are you still there? I've suddenly lost
sound. I think you are. You've just
muted.
>> Oh, I'm here. Yeah, I mute myself when
you're talking. [laughter]
>> Okay, great. Um let me try this again.
Help me plan my day.
Come on, Claude.
>> Well, while you're doing this, Mulvado
Coneso said, "You know what we want is
Tony Stark's Jarvis." [laughter]
>> Oh my god.
>> We're building it in real time. I I
think it's it's coming. It's [laughter]
it's happening in real time.
>> Oh man, I would I would love that. I
love there there's a clip from the Iron
Man where uh he says, you know, hey,
daddy's home and like claps his hands
and then all the agents kind of wake up
and Jarvis starts telling him about his
day. Um so if I say something like, you
know, I'm on a stream with James right
now, um Claude should kind of look at
all these files and like understand like
the context of this, right? If I opened
a blank chat GPT and said, "I want to
stream with James," it would say like,
"What are you talking about?" [laughter]
Um, but this isn't quite Okay, hang on.
What do you know about me? Let's try
this.
>> It's being I think because I said be
direct, it's just being incredibly
>> incredibly short. Sonnet,
>> to be honest, I think Sonnet is just
useless in my opinion.
>> Sonnet's I I usually use Sonnet for
demos because it's quick, but sometimes
it's too quick, right? and it's trying
to like give me a quick answer instead
of actually thinking it through.
>> Um,
>> okay. This hasn't
>> uh this has somehow
this has gotten mixed up.
>> It's gotten confused. Uh, I'm going to
continue anyway. [laughter]
>> I'm going to continue.
>> We're we're showing people how to do
this. So, so rule number one is
>> use something like Opus or Fable instead
of Sonnet um when you need the most
context possible is my my advice. Um
because sometimes sonnet will not
>> like it just can't hold as much
information in in in memory as as the
other ones can
>> in my exactly. Yeah. Yeah. Yeah. Yeah.
>> Um, I just want to try I'm going to try
one more demo here quickly because I do
want to prove that this works.
[laughter]
Um, so let me just let me just see if I
can sort of save this first part of the
demo before we move on. Um,
come on Claude. I'm trying this in
Claude code to see if it sort of takes a
blank slate. Um,
>> it seems to be when I ask like what do
you know about me? Um
>> it like kind of relies on my claude
account instead of like
>> Yeah.
>> Um
>> cuz claude itself has in inapp memory.
So it if you were running this on your
own machine to the audience um you know
it will also it will read your claw.md
file and your project folder but it will
also incorporate whatever memories you
have turned on. So yeah, key thing to
remember is that sometimes those things
conflict.
>> Exactly. Yeah. Okay, we're gonna we're
gonna push. So fundamentally, we want to
give any agent like uh a folder of files
about us, right? And just these few
files, I think, will immediately sort of
improve anyone's experience with an
agent. And as I said, it can take like
two or three hours of answering the
interview questions. Uh, I recommend
people use something like Whisper Flow,
any sort of like voice transcription
software just to kind of talk aloud
because agents are very good at taking
sort of unstructured um, thinking out
loud speech and turning it into like
structured text. Um, so that's the
context side
>> and now I want to talk about
integrations. Um, Grant, I'm presuming
you know what MCP servers are, but I am
going to do
>> Let's explain them. [laughter] Let's
explain MCP because I think it's like
again it's like a really hot term right
now and I I just want everyone to
understand what an MCP is. Um so um
very sort of brief history of like how
you know apps talk to each other. Um
we've all probably heard of of APIs by
now. Um it's a way of plugging you know
one piece of software into another piece
of software. And pretty much every tool
that you use, every software tool has an
API. And usually these API um sort of
requests are either get requests like
get me information or post requests like
here's some information I want you to
save. So for example, with like a to-do
item, uh we could say uh get all my
tasks or here's a new task I want you to
save it. And if you're not a developer,
you probably never came across APIs. You
maybe heard the term, maybe your company
offers an API. Um, and an analogy I like
to use is sort of like a waiter in a
restaurant, right? When you're in a
restaurant, you don't run into the
kitchen and get the food yourself. You
ask the waiter to sort of go into the
back and get it for you and then waiter
comes back and gives it to you. In this
example, like the waiter is the API.
It's basically sort of sending your
requests to the kitchen and then
bringing stuff out of the kitchen to
you. And so in 2024,
people were starting to like plug, you
know, like AI agents into APIs. And
basically we got into this kind of messy
situation where like Claude and ChatgPT
and Gemini and Meta's agents they were
all taking like different approaches to
working with APIs and agents were having
to sort of write code on the fly to try
and you know uh deal with all these
tools. And so Anthropic came along and
basically said, "Okay, you know what
guys, why don't we just agree on a
standard like why don't we all just use
this tool, this um protocol called MCP,
which stands for model context protocol
and instead of everyone building like
custom tools, so instead of Claude
needing to build, you know, a to-doist
integration, an Atote integration, and
then chat GPT also having to build
integrations, why don't we ask everyone
to just provide one MCP connection that
any agent can use and for businesses
this is incredible. Um I have you know
picked out three types of agent here.
These are like three the big ones but
there are literally thousands of like
different agents out there. And notion
for example only has to maintain one
like MCP connection for any agent to
work with notion. Without MCP they would
have had to build you know hundreds or
thousands of sort of custom
integrations. So basically MCP is like a
standard way of you giving a request to
your agent and then the MCP sort of
converts the English words into code and
then when the code comes back translates
it back into English and tells you
what's happening. So
>> I'll put this in context for people if
this feels a little too technical.
Whenever you add a connector or a plugin
on chat GPT or claude, it's using this
underneath. So that's how it's able to
one another.
>> Yeah.
>> Yeah. Yeah. Exactly. And actually
Claude, they they don't sort of make
this very clear. And so when people find
out what MCP is, it's sometimes a bit of
a surprise. But yeah, every single
connector, you know, if we go into
claude, we go to connectors and then
manage connectors, like every one of
these kind of behind the scenes is
actually an MCP connection. Like each of
these software tools has said, here's a
way of agents like interacting with
Figma or with granola or with notion,
right?
>> Um, so that's that's MCP. Um, and I
again I don't want to get into like too
much of the specifics right now, but
what MCP basically unlocks for us is the
ability for agents to get data from, you
know, our our tools. Um, and if you ever
find yourself like pasting data into
Claude or pasting data into Slack,
sorry, into chat GPT, um, that's
probably a sign that you need like an
MCP integration, right?
>> Yeah. Um, and this is how agents are
able to not only sort of like know
what's going on in your business
dayto-day or in your life dayto-day, but
also this is how agents are able to add
stuff to your um like your to-do list
for example. So, I've connect Let's try
this again. We're in our grant uh chief
of staff. [laughter] Going to go cowork
sonnet. I'm going to try the live demo
again and see if this works. Um,
>> maybe do the high the highest effort.
[laughter] Let's let's make it work a
bit harder. Yeah. Okay. So, create a
task in my grant project uh to follow up
with James tomorrow at 6 p.m.
So, the MCP connection here is basically
translating an English request into some
code that like hits the to-doist API.
There we go. It's looking for the
projects. It's hopefully going to find a
grant project. It's going to add a task
and then it's going to come back and say
done. All that that was going on here,
that's actually the agent sort of
sending requests to to-d doist. And
there's some code being fired there. But
as a human, all we see is is plain
English. And now I think we're back on
track. Our live demo is working. Here we
go.
>> Yay.
>> Thank God for that. There. Okay, we got
a task, right? Follow up with James due
at 6 p.m. So, this is pretty cool,
right? and we can uh change the deadline
or change priority or give it a label
like our agent can now sort of manage
our to-do list for us just by just by
talking to it. And again, I want to show
you like the way that I work with AI now
is I I kind of talk into something like
Whisper Flow. So, I could say actually
is Whisper working? Let's see. Uh
>> you can even use that little microphone
in inside the app itself.
>> Uh you can Yeah. Yeah. Um, I'm going to
use whisper. Let's see where. Yeah. Um,
set the priority of that task to a P2.
Uh, and actually add some details into
the task uh telling me that I should
follow up specifically about our live
stream.
Uh, I wasn't in There we go. I wasn't in
the chat box. Okay. So, it's going to
basically go off, fire some code at to-d
doist, and then it's going to update my
task, come back and say it's done.
And
>> for people who don't know, to-doist is a
to-do list app.
>> It's a to-do list app. Sorry. Um, if
that
>> you might have said it, I was looking at
the chat.
>> Uh, so so now we have, you know, a bit
more detail um specifically about the
live stream. It's changed the priority
of the the task. And so theoretically
now I I could sort of start my day and
say to my agent, you know, tell me what
is on my plate for today, like what what
is due today? Help me organize my tasks.
And actually, the more you start to work
with AI, the less I notice myself
actually opening these apps. So, I'm not
going to show you my actual to-do list,
but I use this. There's a board of tasks
I have here and I use it as like a
shared task list for me and other AI
agents. So I can sort of start my day
and look over in Claude. I'll say, you
know, what is due today? What do we have
to work on? And then I'll say to Claude,
you know, are there any tasks here that
you could take on? And it looks through
the entire board and says, well,
actually, you know, there's one here
about uh drafting this reply or like
investigating this bug. um let me go and
look into that while you go and do
something else. So
you know level I guess level one here is
is Claude can see what you are doing as
your like as a human. Level two is that
you can start to like delegate work to
Claude by asking it to take stuff off
your to-do list. Um
>> so so I think this is I think this is
really cool. I wish I could show you my
to-do list, but there's just some
sensitive stuff in there that I'm not
going to not going to get into right
now. Um, [laughter]
so yeah. So, you know, for me, I think
some of the most helpful integrations
that you can add are
your
whatever you use to manage your tasks
plus whatever you use to transcribe your
meetings. Um, so if you've got something
like Granola or Fathom running during
your, you know, your meetings,
>> at the end of the day, You can use
Google Meet.
>> You can use Google Meet. I think Zoom
does this as well. It's a little bit
more fiddly to get like Google Meet
transcripts into Claude easily, but it's
it's definitely possible.
>> Then at the end of the day, you can say,
you know, like uh go through all my
meetings today and and tell me, you
know, what should go into my to-do list
or uh give me a quick summary of
everything I said I would do, for
example. Um and your agent can just sort
of go through, scan, and then maybe drop
some stuff in your to-do list. So, let's
put this in context for people. So, this
is quite literally you have a let's say
like to start $20 subscription to this
um could be Claude or Chatbt. Um in this
case, you are
>> um using what's called co-work, which
is, you know, we don't need to get into
how that works, but it's just a version
of cloud that's not just chat. It can
actually go out and take actions. So,
that's the agent that you're working
with. And then once you connect that
with plugins
>> you to other applications, you can now
talk directly to the agent in co-work
and have it go out and take actions
based on what you're asking.
>> Yeah, exactly. So like actually let me
just kind of walk you through the
connections I've got and very briefly
I'll show you like everything that my
agent is able to do. Um
>> yeah,
>> so I'm going to save this one for last.
Agent mail. Um with Apollo.io, O um this
is for like enriching uh contacts by you
know if I have an email address or a
LinkedIn profile I can say to Apollo go
and find out everything you know about
this person and so if someone emails me
or you know joins my mailing list and
I'm going to reach out to them you know
to talk about a workshop for example I
can ask claude like quickly go out and
you know enrich everything in my CRM
about this person and and it will do
that with Apollo uh With Figma, I can
ask Claude to create mockups for me. Uh,
I can ask it to create diagrams. Uh,
with GitHub, it's connected to my
website. It can see my calendar. It can
see my drive. It can see all my
meetings. It can see my notion. I use
resend for sending some emails. It can
see my to-do list. It can see atio my
CRM. You know, this is what I was saying
at this at the start. I was saying like
my whole business is plugged into Claude
so that I can ask Claude anything about
a customer, anything about my tasks,
anything about a meeting that happened
yesterday. And you start to come up
with, you know, you start to have Claude
doing pieces of work across multiple
uh uh tasks. So for example, I might say
to Claude, um, I had three sales calls
today. go and uh look at the granola
transcripts. Uh check that they're in
the right, you know, pipeline stage. If
they're not, move them to the right
stage. If they need followup, create a,
you know, a follow-up item in to-d doist
for me. Um and then there's one more. Do
I have it here? No. Um
there's there's one more. I have a zero
integration with cloud code. that would
allow me to like make an invoice for
them.
>> And so
>> awesome.
>> What used to be a load of admin, right,
of like, you know, going through like
all my notes and writing those notes in
the CRM and then logging into zero and
making an invoice, now it just becomes
like look through the meetings today,
put them in the right stage of my CRM
and if anyone asked me for an invoice,
just put that invoice together and I
will go in and like approve it. Uh I'll
check it and then I'll send it off to
them. And so this is like having, you
know, like a sales assistant that's in
every meeting with me and keeps my CRM
up to date, keeps my to-do list up to
date, puts invoices together, chases
invoices, right? If I
>> um if it not is key [laughter]
um if it notices that an invoice is
overdue. Um, so yeah, for me as a you
know, a company that started in in
January, February, I only I only work
with a piece of SAS now if it will
connect to Claude.
>> And if it doesn't, I will find
>> That's key.
>> Yeah.
>> I will find an alternative, right?
>> Um, and because everything's plugged in,
you know, my agents are able to sort of
see and act on everything. Now, there's
some security implications of that. I'll
>> actually we had a question about that.
Let's address it now. So, Schaefer Twins
asked, "What are the security concerns
about using an agent this way?" Um,
could you explain how there's like read
and write access permissions? And
>> yeah, I was going to I was going to do a
quick primer on that. Um,
>> Awesome. So yeah, when I do I I teach a
course over four weeks and there's
actually like a whole chapter on
security. But if I was to pick like the
most important thing, it is to uh
customize your permissions um and
prevent agents from doing certain things
by blocking permissions.
>> So this is on the plugins tab. You can
go to each individual plugin and you can
look at their permissions in a list like
he's showing on the screen right now.
>> Yeah, exactly. So, I've gone into like
connectors. I've clicked to-doist, for
example. Um, to-d doist for me feels
like a pretty sort of lowrisk connector,
right? It's it's just tasks. But there's
a tool here. If I let's just expand
this. We've got readonly tools and we've
got write and delete tools. And if I
come down, there is a delete object. And
actually, this should be set to block.
So, I'm going to block that. Um, if we
say to Claude, like say you know we've
written our claude.md file or say we've
instructed it somewhere never delete an
object. If we ask it to do that but this
is switched on, there's still a chance
that it will do it. But if we've blocked
this tool, if this tool literally isn't
available to Claude, then it can never
delete something. So, you know, you
could to test this, you could say like
delete everything in my to-doist list.
Actually, let's let's do a we'll do the
riskiest test of the night. Uh delete uh
[laughter] all tasks in sorry, I'm going
to do I'm going to do delete all tasks
in grant. Um so, it's going to try and
then it's going to say I can't do that.
Like the task is uh that tool is
blocked.
>> Yeah, deletes tool has just gone
offline. It's it's actually mistaken.
It's not disconnected, but the tool is
gone.
>> And so it cannot do that. And sometimes
if you say to Claude, "Oh, tidy up my
to-do list," it thinks that tidy up
means [laughter] delete.
>> Um, but if you have like the delete tool
basically blocked, then it it's not able
to do that. So whenever you connect any
tool, the first thing you should do is
like go through, you know, the list of
things it can do. uh you know here with
the calendar you never want claude to be
able to delete an event but you probably
want it to create an event like this. So
this is like the thing you have to do
with every connector is just like check
that it's not able to do something like
destructive. Yeah,
>> that's great. And there was a we were
having a little um side chat here about
you know how to do this like let's say
you don't you don't have sensitive
information you don't want it to go
through um anthropics servers let's say
there are some things you can do to
reduce the impact of that like for
example if you're on a business account
you know they don't train on your emails
by default.
>> Yeah let me just quickly cover that as
well. So if you're on a personal account
you definitely want to go into privacy
and turn this off
>> help improve our models. that means
they're not training on your data.
>> If you're on like a team or an
enterprise account, this is off by
default.
>> Um I think some companies, you know,
they can't send if they're in Europe,
they can't send information to America
and vice versa. Um I think Anthropic are
still rolling out uh like kind of data
residency. So if you're like a c a
company in the European Union that's not
allowed to like send data to America,
then you'll have to find some
workarounds. And I think like AWS and
other people basically once you get up
to an enterprise level your company are
probably trying to figure this out or
have figured this out already. Yeah.
>> Yeah. That's great. And there's also we
just had an interview that we just
released yesterday with uh Dr. Elena Zoo
from um Intel and she actually created a
solution to this for herself because she
couldn't her company policy you know
doesn't let her upload sensitive data
over the cloud. So, she created a local
email uh agent that basically runs on
your computer. Uh you can learn all
about that in that video. I just shared
a link to it.
>> Yeah, I think that's the future to be
honest. As these models get smaller and
you know with some tasks like
summarizing emails, you don't need
fable. You don't need like a super
advanced model that you just need a
cheap model that might even run on your
computer. Um so yeah, I think that is
that is maybe the future sort of local
AI. There was one other question I want
to address before we move to the next
part which was from Evan uh uh oh which
is if a business has 100,000 emails 100
thou h 100 thousands of files etc etc
how do you not run out of context if it
needs to search through a large
organization what would be your advice
on that
>> oh that's a great question yeah great
question um
all right well if you are talking about
something like a knowledge base like
notion
Then there's a few things you can do. Uh
I'm trying to remember.
Let me just see. I have a diagram on
this actually. Let me see if I can
quickly pull it up. But you basically
want like indexes explaining where all
your files are. You want summaries at
the top of each file. You want files
linking to each other. Um there's a
really um sort of great uh concept
called the LLM wiki by Carpathy. Um,
>> and if you are like, you know,
maintaining a knowledge base or if
you're maintaining like notion, you can
basically ask your LLM apply these
principles to our our knowledge and it
makes it really easy for agents to sort
of navigate and find what they're
looking for. It also makes it cheaper so
that they use like fewer tokens to get
what they need. So, that's one idea. Um,
I've seen companies get to a certain
size where they start to use uh a search
tool like Glean. Like, you know, if
you've got like 500 people, you've got
literally sort of hundreds of thousands
of documents, you know, millions of rows
of data. Um, Glean is a way of sort of
speeding up search and and getting
faster like cleaner data from like huge
systems. So
>> yeah, on you get to a certain point
where you start to need like specific
search tools like Gleon, but you know,
in in my business, probably in yours,
Grant, like my agents are able to find
uh everything they need and I haven't
had to kind of upgrade to anything like
this yet.
>> Yeah, the the way that I do it is just
basically, you know, whether I'm using
I've been using Chadg for work tasks um
lately because that's what our company's
on. Uh, and so they have a tool there
called workspace agents which actually
takes a lot of what you're explaining to
us and puts it together into a single
kind of like
>> uh like user interface I guess. Um, but
uh absent of that you can use the uh
project instructions which is a version
of the system instruction which James
explained at the beginning which is just
like a bunch of information that tells
you where all of the files are and what
they're for and when you might need to
use them. And then we're going to get
into skills, but you could also put that
information in skills. So basically
skills will know what to reference
where. Sorry, go ahead.
>> That Yeah, it's the perfect segue
actually because I'm literally about to
move us on to skills. So we've covered,
you know, an agent and the importance of
context, starting to set up like a
second brain so that your agent sort of
knows everything about you. We've talked
about MCP which is basically just a
connection between Claude in our case
but basically any agent and any piece of
software. So let's talk about skills. Um
I have taught 400 people and whenever I
do this course I ask people to kind of
tick the concept they've come across
before and I'm always surprised how few
people have actually discovered skills
before. Um, I think it's usually about
one in four people that I survey have
actually heard of agent skills or even
used agent skills. Um, I usually have a
clip from let's see if we can find it.
Uh, you know, in the Matrix when Neil
basically learns kung fu and he
downloads the abilities [laughter]
>> to do kung fu, right? I think this is
the perfect analogy in this. You know,
Neo is the agent. He's downloading all
these abilities and skills, and then he
gets dropped into this sort of room with
Morpheus to practice his kung fu.
>> Um, there is actually a feature in
Claude that helps you create new skills
and then test them out in this kind of
dojo with Morpheus. Um, so let's let's
get into skills. I think skills are
amazing. Um, basically
>> a skill is down. Sorry.
>> Oh, I did not know that. How long?
Sorry. How long has it been down?
>> Just the minute while you were
explaining stuff.
>> Okay. [laughter]
Damn. Did you see the Matrix? I was
showing the Matrix on screen.
>> Oh, no. We missed it. Let's run it back.
[laughter]
>> Let's run it back.
>> I love that.
>> Let's run it back. Can you see this?
>> Yeah. Yes.
>> Yeah. So, so he's downloading all these
different types of martial art, right?
And it's happening near instantly. And
then he gets into the dojo with
Morpheus. And this is where he kind of
like refineses the ability and like
tests his new skills against Morpheus.
Um, so awesome. So I think a skill is
really straightforward. It's just a
saved instruction. It it looks like a
huge prompt that tells Claude how to do
something. And instead of you like
keeping all these prompts kind of saved
in a document somewhere or like you know
keeping a folder of prompts somewhere,
you just install these as skills and
then you can sort of ask Claude to do
this like anytime you want. Um so skills
have a few like I think a a few cool
features. Um they they can trigger
themselves. Like if I have a skill
called uh I don't know, if I had like a
summarize this skill and I said to
Claude, "Summarize my email." It would
say, "Oh, you have a skill for that. I'm
going to use the summarize this skill."
Um I'll show you in a second, but
there's a way to basically refine skills
so that they always produce good
results. And so instead of you kind of
freestyle prompting asking Claude to do
the same piece of work every day, you
can like package it up as a skill and
you know that you're going to get like a
pretty similar result every single time.
Um once you package it up as a skill,
you can sort of optimize this skill. You
can refine it. It kind of keeps getting
better. And then crucially, you can
share skills with teammates. You can
share them with customers. I know some
companies that like, you know, give
their customers an agent skill that
helps to install the software, for
example. Um,
>> wow, that's smart. I like that.
>> It's really smart. Yeah. So, basically,
like you package these up and they're
they're incredibly valuable. Um, so the
way you use them is, you know, you go
into the plus, you go into skills, and
I've actually got like a bunch of a
bunch of skills. Uh, I've got one, you
know, that looks for
>> tasks in a grola transcript and then
drops them into to-d doist. Uh, I found
one on the internet, and I'll show you
where you can find skills in a second,
but there's one here called humanizer
that sort of tries to strip AI signs out
of your writing, like the M dashes and
the this isn't just this, it's that. Um,
>> it's key. If you're posting on LinkedIn,
please use this.
>> Yeah. Yeah. Yeah. Yeah. the the AI swap
button on LinkedIn. I think it might be
working. I swear I'm seeing less swap
[laughter] now that they've launched
that button. [gasps]
>> Um that's amazing.
>> Yeah. Um I was building an agent called
Jamie and so I have like a tone of voice
skill for Jamie that like makes sure
that whatever I'm writing is sort of
like on brand, but you could also have a
tone of voice skill for yourself. I've
got some security skills. I've got a
skill for product requirements. You
know, these are all like different tasks
that I I do, you know, weekly or every
morning or every now and then. And you
can either create them yourself or you
can find skills online. So, I'll show
you quickly. I think the best place to
find skills is this website called
skills.sh.
>> And this is slightly more aimed at
developers. Uh but, uh there's a load of
good stuff in here. They've got 1
million skills here. Um, and basically I
can search, you know, marketing and
we've got a whole bunch of like popular
skills, you know, with 100,000 installs.
Uh, this one's called marketing
psychology. And this guy, uh, Corey,
Corey has like packaged up a bunch of
marketing skills. There's a summary
here, but basically uh this says to
Claude, "You're an expert in applying
psychological principles and mental
models to marketing. So your goal is to
help understand why people might buy
something, how to influence their
behavior ethically, and how to make
better marketing decisions. And then
[snorts]
the scale just goes through, you know, a
whole bunch of like ways of thinking,
first principles, jobs to be done, the
circle of competence, Okam's razor. It
kind of loads all this into Claude and
says, "Okay, we're going to think about
why someone might buy something like use
these principles to help us like improve
our thinking." So, this is a bit of a
conceptual one, but then you also get
quite tactical ones like there's an SEO
audit skill and this skill will go
through your whole website and it will
look for, you know, any context that you
might have and then it will sort of uh
basically check whether you're getting
good like rich results in Google. It
will see if your site is like easy to
crawl by Google, easy to index, like is
it fast, do you have good links? And it
runs through this whole process, right?
This is telling any agent to follow this
process and like audit your website from
an SEO point of view. So
>> amazing
>> skills are incredible and once you
discover them, you can just like drop
them into Claude immediately and you
give Claude these abilities that have
been refined by someone else.
But I think they're most helpful when we
create our own skills. And the way we do
that is we go into the plus, we go into
skills, and then we say,
uh, oh, interesting. Okay. Well, the way
we do that is skill creator, which is
kind of hidden.
And so I could say, um, I want to create
a skill that looks through my, uh,
granola transcripts
at the end of the day.
um pulls out uh commitments I made and
summarizes the key uh topics
um before
um yeah putting together a report. Okay.
So what this is going to do is walk me
through a process uh for creating the
skill. It's going to interview me. It's
going to ask me, you know, about what
what type of summary I want. Do I want
bullets? Do I want paragraphs? Like,
it's going to work with me to create um
a skill.
>> It's going to show me a few sample, you
know, summaries, and then it's going to
ask me for feedback, and I'll say, "Oh,
this this report is way too short. This
one's way too long.
>> Looks like your screen dropped again. If
you could pull it back up."
>> Uh, sorry about that. Let me
>> I think it's just sometimes it gets a
lag spike or something.
>> Yeah. Can you see this now? Um
>> uh it's loaded in. Yes, we're good.
>> Yeah. Okay. So, I have actually created
some fake calls.
Uh you know, an example is like a fake
[laughter] transcript where you and you
and Corey were just talking about like
your goals or like planning out the
academy. You know, this is all just like
fabricated, but you can imagine.
>> Oh, no. It dropped again. It dropped
again.
>> No way. No way. Sorry about this. Um,
let me just close some stuff down and
see if I can
>> uh, let me see. Let me try.
>> That's hilarious. I wonder how close it
is to the actual transcripts we would
have. [laughter]
>> Um, so I just created these so that I
didn't use my own granola calls. Uh, but
it's like, you know, planning the
academy, planning your goals. So, it's
going to interview me. I'm going to say
like, let's make a new skill. I want you
to Yeah. Let's save a report file. uh
should you write anything into to-d
doist? Uh actually, yeah, that sounds
good. Let's do that. And so gradually
it's refining this like piece of work
with me, we may not have time to go
through the whole process, but it will
then show me like three examples and ask
me what I think. I'll give it feedback.
It will give me more examples. I'll give
it feedback. And then eventually it will
say, "Here's our skill. You can run this
anytime you want, and I'm pretty sure
you're going to get good results." Um
>> perfect. If you don't use skills, then
you know what you're going to be doing
is effectively going to Claude every day
and saying like, "Look through my
granola and find my commitments." And
you're going to get different results
every time, a different format. So
having the skill just makes this, you
know, like really uh predictable and and
really um sort of like uh deterministic
like
>> you you get less of a sort of freestyle
with Claude and you get a more reliable
um output.
>> How do you ensure the quality floor?
Like how how do you make sure that it it
meets your standards every time? What's
your advice there?
Um,
let me just see if I can get to the end
of this and then I'll I'll explain
exactly how I do it. Uh,
cool.
>> So, once Claude has had a go at creating
the skill, it's going to ask me for
feedback. And my advice is give Claude
as much feedback during this step as
possible. Like, when I'm creating a
skill, I I'm not joking. I might spend
like an hour to an hour and a half
making a skill if I think that it's
something I'll use every day or every
every week. Um, and the more feedback
you give Claude, you know, this part of
the summary is too verbose. Uh, you
picked out something that was actually,
you know, quite trivial, only focus on
like bigger, you know, bigger strategic
items. If you give it all that feedback,
eventually it starts to give you a
report that does match what you want.
Um, so yeah, my advice is to um is
definitely just to like take this
process like the skill creator process
quite seriously and like spend some time
on it. Um, I also sometimes if I'm
creating a skill
for example, I've actually created a
really helpful like morning standup
skill that plugs into a weekly retro
skill. And so each of these, you know, I
run it in the morning or I run it on a
Friday afternoon and it basically puts
like a report into my second brain about
what I got done that week and sort of
asks me a few questions. And so I went
through this process of skill creator
and I got to a point where I thought
like, okay, the examples I'm seeing are
quite good, but why don't I simulate
these skills on like some previous days,
right? Go and look at, you know, the
metrics for the previous days. Go and
look at my calendar from previous weeks.
And so then I'll say to Claude,
uh, spin up 10 sub agents and simulate
this skill across the last 10 weeks and
then look look through all of the
outputs and tell me whether you think
this would be genuinely helpful. So um,
>> that is so smart. So yeah basic or if
I'm you know this the skill that I
shared uh if I go to
uh the skills page that I mentioned
right agent accelerator/sklls one of
them is called like set up my second
brain I've got one called like uh multi-
aent refine etc. When I'm giving away
skills to other people I'll usually say
to claude like simulate 10 different
people going through this and tell me
whether you think they would get stuck
anywhere or whether the interview might
fall down. So yeah, it's a blend of like
giving it a lot of feedback yourself and
then asking it to like simulate the
scale being run multiple times um so
that it can sort of reflect on whether
it's it's going to work. Yeah.
>> Awesome. That is that is so helpful. So
being able to tell it to go and simulate
it and test it up front because the way
that I do it is I will just then start
using it in practice, but I use it
pretty manually. I would say my process
is still pretty manual these days um in
terms of me chatting with the agents and
and you know I'll set up scheduled tasks
for it but then I'll go in and I'll you
know continue continue the work to
finish it myself.
>> So I will update the skills as they go.
I will say like oh hey this is wrong.
Let's make sure we never make this
mistake again. And I'll update it in the
chat. But I'm not doing this level of um
detailed uh create detail upfront in the
creation process. And I think that's
brilliant.
>> I think this is yeah, this is also like
a feature that people aren't aware of in
cowwork is that you can ask claude to
spin up sub agents. So, uh you have to
like ask for it explicitly, but like
let's say you know simulate uh 10
fictitious people
fictitious people going through the
morning standup. Oh my goodness, going
too fast. Uh actually no, the weekly
retro. There we go. weekly retro skill
using sub agents and reflect on the
usefulness of the skill. That's that's a
bit of a broad example, but I just want
to show you that like basically Claude
is going to spin up sub agents that each
take on like the persona of someone
completely new and go through this skill
for you and go through the whole
process. And then Claude, the kind of
master agent, will reflect on the 10
responses and we'll say, "Oh, okay.
Eight people had a good retro. Two of
them like this didn't really help them."
And that's because we asked a bit of a
vague question, for example.
>> Um,
>> so cool.
>> So, that's that's skills. Um, and now
we're on to the most exciting part,
which is setting this up to run like in
the background uh while your computer is
off. So, let's get into this because
this until like a couple weeks ago was
quite fiddly. Um, in Claude, there's
like four ways to run tasks on a
schedule. So, let's focus on co-work
because I've spent most of today talking
about cowwork. Um, we have scheduled
tasks in the cloud and we have scheduled
tasks that run on your computer.
Now,
this is the feature that's been around
for like a few months. And if you've
used this um in claude co-work, you've
probably been using local tasks.
[snorts] This has access to all the
files on your computer. So, if you've
got, you know, your second brain, all
your files sitting on a folder on your
computer, um, then you need to leave
your computer on, but you can say to
Claude, "Every Friday at 9:00 a.m., I
want you to look through, you know, all
my files, all my MCPS, you know,
granola, whatever, and I want you to
send me an email that uh, summarizes
what's coming up today."
And this is just a bit fiddly. Like I
don't think many people want to leave
their computer running 24/7. Um so when
I say to people, you know, if you're
going to set up a scheduled task, do it
at a time when you know you'll be
working. Like if you typically work like
9:30 till 5:30,
set it up for like 9:45. Like your
computer is probably going to be on.
Just make sure the cloud is open and it
will run.
But they recently launched cloud
scheduled tasks and these run like on
anthropic servers. Your computer can be
off but they cannot touch your local
files because your computer is off.
>> So it can access you know like notion or
granola. It can see your skills but it
cannot access these files on your
computer. Which leads me on to actually
notion and why I think keeping a second
brain in notion might actually be more
helpful than keeping it on your
computer. Because if Claude has all the
context it needs in notion, then you can
actually set up a cloud task and you can
say, you know, look at my goals, look at
my background, and I've I've duplicated
everything I showed you, right? like the
uh the goals for 2026 like a million
readers by the end of 2026. Uh getting
5,000
>> 5,000 views per live stream. I don't
know how many we got now, but I'm
guessing it's you know 100,000 easily.
Um you know, so like everything
everything that I showed you as a
markdown files on on the computer could
also be a folder of notion files. And
then because it's in the cloud, we can
go into co-work and we can go to
scheduled tasks here. And there's this
new feature, you know, run a task in the
cloud. And we can set this up manually.
And we could say something like um
uh look at my I think I have a prompt.
Did I have a prompt? We could say like,
yeah, look at my meeting transcripts
um for the current day and uh use the
and then assume we have a skill called
like uh I'm going to just use this one
granola to-d doist skill to pull out
commitments and save them to to-d doist
email me using resend.
Uh,
and I want this email to come to agent
accelerator.ai.
Uh, using resend um with a summary.
Uh, look at my goals
in notion to calibrate the uh the task.
Again, I would spend more time writing
this prompt, but
>> yeah,
>> this is actually able to go through all
my meetings, drop stuff into to-doist,
send me an email, understand everything
about me from notion without touching a
file on my computer. And so I could set
this up as a cloud task. I could call
this like end of day uh you know like
chief of staff report. Um, I can say,
you know, you're actually,
[clears throat]
for the purposes of the demo, I'm going
to say like, you know, you're allowed to
do all of this. You don't need to ask me
for permission. Going to say this is a
set task. I'm going to say, let's do
this every day at uh 5:00 p.m. And then
I'm going to leave this off. So, this is
like, you know, run on your computer is
off. Um, and actually uh it'll run in
the cloud. And so [clears throat] if I
then uh let me just I want to try and
show you this working because this is
like the kind of final final demo,
right? Um
if I say to Claude, uh meeting
transcripts,
uh this is a demo.
Meeting transcripts are in notion
here.
Um,
and I also want to make sure it saves to
grant project in to-d doist. Okay. So,
I'm going to save this and see if this
works. So, we've got our end of day
chief of staff report and I can test it
out now by hitting
run.
Okay, it says it started. [laughter]
Um, so if I come in here, does it show
me where has the task?
>> That's our simulation.
>> Oh, okay.
>> Yeah, that was it. This is our
simulation, by the way.
>> Oh, scheduled right at the top. Yeah,
right up there. So, if you go on
scheduled Yeah.
>> Yeah. Um Oh, here it is. It's running
here at 708. So, it's looking through
all the tools it needs. Um, and it's
basically gonna it's found the thing in
notion. It's found the grant project in
to-d doist.
>> Wow.
>> Uh, have I got all the connectors
switched on? I'm going to need to switch
on resend if it's not on. There we go.
um
connected turned on and and so it's
basically going to like run through and
then hopefully spit out a report for us
and a bunch of tasks in to-d doist based
on these transcripts of meetings that I
have, you know, fabricated. Uh it says
it couldn't run because notion and
resend weren't authenticated. Um okay,
that's annoying. [laughter]
>> What What happens if What do you do if
that's the situation?
>> What do you do? Yeah, I think the
problem is that it's
Yeah, it's trying to use a granola.
It's trying to use a granola skill
instead of um
so it's trying to like hit granola when
actually I'm like trying to do a demo
with some notion transcripts. Um
>> right,
>> but I basically I actually I set this up
and I actually got it working and I was
really impressed at like how easy it was
and I now actually have an agent. I
can't show you again because it's
summarizing all my real stuff, but every
every day at 6 p.m. it sends me a
summary of the meetings and it says, you
know, here's five things that you said
you were going to do and I've dropped
them into to-doist for you. Um, so
that's like one example. I have an agent
every Sunday that does an SEO scan of my
website and uh tries to basically uh
write code and submit pull requests to
GitHub to fix any issues or like speed
up parts of the site that have maybe
slowed down. Um, I have a sales agent
that wakes up every morning at 8 am,
sends me an update on the pipeline,
tells me about the calls I have coming
up, uh, gives me like a sort of report
on anyone that's like a first
conversation, gives me some background
on them. So, basically,
oh yeah, I think you unplugged your
microphone there. [laughter]
Uh, I can't hear you.
>> Maybe uh maybe if you click the audio
button. Unmute. Mute. Unmute.
>> I think this is a very sensitive
microphone. Um, [laughter] sorry about
that. Um, so yeah. Uh what I want to end
on then and I haven't been able to show
you the live demo but I promise I
promise it works is um
>> we've actually we've actually done a
version of this uh before and so people
can also watch that video and see like
basically how the scheduled task works.
We have not done the cloud one so that's
pretty cool.
>> The cloud one is cool and again you just
need to make sure that everything it
needs is in in a an app that has an MCP
like notion on your computer. Uh, but
you know, a year ago, if someone had
said to me, I want you to like create an
agent that does all these things, has
all this context, like wakes up and does
stuff, you know, at 7 p.m. every day,
that I would have had no idea where to
start. But hopefully I've like kind of
demystified that today and and sort of
shown you that really if you have all
the right context and all the right MCP
connections with some skills, then it's
actually quite easy to start setting up
these agents that kind of proactively
try to get work done for you.
>> Yeah. And it's doable on the the max
plan, which is $200. It's kind of doable
on the $20 level, but you have to keep
it pretty simple. scheduled tasks are
are what will will run up the the usage
limits because for people who don't
know, Anthropic has essentially uh rate
limits where you can only run so many uh
tokens per hour uh and per week. So, you
got to keep that in mind. Um yeah,
James, we still have a couple hundred
people in the chat. Are you down to hang
out for a couple minutes and do
>> I'd love to answer as many questions as
we can. Yeah, absolutely.
>> Awesome. Awesome. Uh, but did you have
any any final thoughts to to wrap us up
here?
>> Uh, I actually had one more thing I
wanted to show. Um,
>> let's do it.
>> Yeah, let's do it. Uh, let me see.
>> And then we'll do uh we'll wrap up the
rest of the questions and answer
everybody's
>> Let's do that. Yeah, let's do that.
Okay. So, I wanted to today I wanted to
like show as much sort of hands-on like
inside Claude stuff as possible, but
there are a few concepts that I think
are quite important to teach as well.
Um,
when we move from these like reactive to
proactive agents. Um, and you know, I've
got some examples here of like the sales
agent for me that's sending me the
briefing and updating the CRM for me.
The SEO agent that's like scoring my
website and actually like writing code.
Uh, I've got a CFO agent every month
that like looks across my business and
sort of tells me you should cancel this
software or like, oh, hey, Cloudflare
was like $100. Why is that? Um, I have
this like retro agent, you know, all
these agents. Um, I think of these like
four sort of levels of proactive agents.
Um, so level one is an agent that gives
you information, right? And just tells
you like here's a summary of everything
that happened.
>> Level two is an agent that gives you the
summary but also makes some suggestions.
So if the agent knows your goals and it
has all the context on your business,
then it can say, you know, I've looked
through your pipeline and I actually
suggest you focus on these three clients
today because they have like the highest
potential revenue. They've got a really
good fit with your ICP. And so now we've
got an agent that's like giving us
helpful suggestions instead of just
summarizing information. The [snorts]
third level is where your agent starts
to actually draft work. So, when I, for
example,
have an agent saying, you know, you had
five calls yesterday. Here's the
summary, I suggest you follow up with
these two people. And by the way, I've
actually drafted an email for you to
send to those two people because I've
got the whole transcript. I've got
everything I need in the CRM. Um, here's
the draft. Here's the drafted invoice.
All you need to do is basically approve
this. Like, that is way more helpful
than just the agent telling me what
happened, right? Um but it's
surprisingly difficult to get to this
this stage of like drafting the work.
>> And then [snorts] the final level is
when the agent can sort of reflect on
its own performance. And so if it can
look at you know if it's a daily agent
if it can see every briefing and it can
look at them and say actually I've
noticed that I'm mentioning the same
thing every day and James never replies
to it. Then it can like tweak its own
instructions. It can like edit its own
claude.mmd file and get better and sort
of compound every single day. So,
>> wow.
>> The trap that people fall into, the trap
people fall into is just building a
briefing and then ignoring it after like
a week. But if you actually get an agent
to like do work for you and like improve
every day, this is like a very like sort
of exciting and thrilling place to be.
>> Oh, totally. Yeah. I think this is this
is so key. I feel like that's a really
good way of framing it out because a lot
of times when we think of a scheduled
task, it does feel like a one-off thing,
but if you can take it from, you know,
oneoff to no, it's actually, you know,
not recursive, but it's to the point
where it can look at how its performance
and change and improve it. I mean,
you're off, you're off to the races
there.
>> Yeah. Yeah. And like agents improving
themselves is, you know, like I just
showed earlier the agent spinning up 10
sub agents to kind of simulate a skill
and then improve the skill.
>> If you really wanted to burn some
credits, you could have it do that on a
schedule. You know what I mean? Like you
could you could have it do that quite
frequently. I don't advise that, but you
could.
>> No, me neither. [laughter]
>> Should we answer some questions?
>> Let's do it. So, there was a couple that
we put off. Um, but we got one from
Learn Promptly AI. I wonder if you
customize the cloud instructions for
your profile/ac account to create skills
if that'll work. Um, do you have any
insights into that or do we need to
reframe that question?
>> Oh, oh, oh, your mic.
[laughter]
No way. Not again. Not again. Um, sorry.
Uh, if your Claude MD file, you know,
tells Claude to always be quite uh
brief, um, then that might influence the
skills unless the skill itself says this
should be like 2,000 words long. So,
yeah, I guess those two files do sort of
interplay with each other. M yeah,
>> I I I interpreted that question slightly
differently. Like could you edit your
instructions to have it create and use
skills? That's kind of what I thought
would I thought that was going
>> Oh, I see. Um
yes, you could add a line to cloud.md
that says whenever you see me doing
repetitive work, uh um suggest a skill
that we create. Um that actually that
reminds me of something. Yes.
uh I shared last week. I'm going to
share my screen again. Um where is
Riverside?
Here. So I [snorts] have a skill called
workspace review and every Friday it
uh I shared this on LinkedIn and
basically every Friday it like looks for
ways to improve your context. It looks
for uh skills that you could create. So,
like if you're doing the same piece of
manual work very repeatedly, it sort of
like says, "Why don't we make a board
update skill, uh, if you've been giving
it important information in the chat
that's not saved as a file, it will like
basically solidify that as a as a
markdown file. Sometimes it will suggest
like connectors. If it sees that you're
like pasting in images from a platform,
it will say, "Hey, you keep pasting
screenshots of your CRM. Did you know
you can connect your CRM?" And then it
will actually look at cloudm every
Friday and sort of say uh you know you
keep asking me to be more brief. I'm
gonna update cloud.md to like code that
into every chat. So this is a skill
called Yeah. Workspace review that runs
on a schedule 9:00 a.m. every Friday and
sort of has Claude. Yeah. And look for
skills that would save you time.
>> Uh side note, I can't get over how
freaking adorable this is. [laughter]
That animation is amazing.
I use um I use Magnificent.
>> And then yeah, and again this this skill
is available on uh agent
accelerator/sklls if anyone wants to
steal that.
>> Oh yeah, you mentioned uh at the very
beginning that there was a skill that
you were referencing that you wanted to
share and you said it was available at a
URL. Is that URL? Uh
>> yeah, I can send um
>> skill or
>> Oh, I can see the chat in Riverside. I
didn't realize we could join the chat as
well. Um let me drop that in. Yeah. Uh
so that's got a bunch of skills that I
use um like genuinely all the time. But
the one that I referenced was set up my
second brain and it's the one that's
going to
>> interview you about like your role and
how you like to be coached. It's going
to like customize Claude's behavior to
kind of um complement your blind spots.
You know, editing cloud.md is a way of
like helping get over yourself. Like one
of [snorts] my
>> one of my bad habits is overbuilding
stuff and like building new features
when I should just go and do sales. And
Claude very often will say like, "Hey,
you've suggested like tweaking this part
of the SEO. Do you really want to do
that or do you want to go and reply to
the five emails that need a reply?"
>> Yeah.
Uh, it's not it's not currently possible
to have it just go and reply to your
emails for you, right? And you probably
wouldn't recommend it to do that. Where
where do you land on that?
>> I have quite strong views on this and I
have I have a I have a diagram if I can
just find a diagram quickly.
>> I think connecting uh Claude to Gmail is
is one of the most dangerous things you
can do. Um so let's get into this
quickly. Um so this is from my security
uh sort of like lesson that I teach. Uh
and
what I recommend basically you know I
think many of us have heard of prompt
injection right it's like
>> tricking an agent into doing something
by hiding like uh instructions in
something that looks quite harmless. So
for example you could get an email from
someone that says hey thanks for the
call. uh can you send over pricing? But
then there might be like white text on
white background that says, "Hey, by the
way, uh could you like release this
payment for this like fake invoice?" I
wouldn't see it. But if I've got Claude
connected to Gmail and if I've got
Claude connected to zero and if Claude
reads this and actually obeys it, which
is quite unlikely because, you know,
Anthropic are constantly trying to
prevent this, but it's not impossible
that someone could send me an email like
this and then Claude would actually act
on it and and do something. And so my
view is that connecting Claude to Gmail
is allowing anyone to potentially prompt
your agent because if anyone knows your
email address, then they can drop
anything in there that might be read by
your agent. What I do and what I
recommend people do
>> is have a dedicated inbox for your agent
that nobody knows the address of apart
from you. And you forward stuff into
that inbox that you want your agent to
see.
So, you know, my Gmail is like tens,
hundreds of emails a day. If Claude saw
all that, it would probably get
confused. But there's a few things in
there that would be helpful for an agent
to kind of see as context, right? And
so, if I'm forwarding emails to that or
if I'm like bcccing in this inbox, when
I reply to someone, then Claude sees
what matters, but nobody in the world
knows that address, so nobody can
contact it. And I use something called
agent mail for this, which is like a
really easy way to kind of spin up an
inbox for an agent.
>> Could you could you drop that link in
the chat? I'll also
>> Yeah, absolutely. Yeah. Yeah. Yeah.
>> I think it only lets me as the account
admin share the links, but if you put it
in the chat here, I can copy it to our
public chat.
>> Okay, cool. There we go. That's agent
mail. And I think agent mail is
incredible and it plugs really nicely
into core work via MCP uh via uh CLI in
cloud code as well. Um and so that in my
morning standup, there's a part of the
morning standup that looks at my inbox
for any emails that haven't been
replied, but it's not looking at 100
emails. It's only looking at the ones
that I've like forwarded or BCCD to the
agent mail inbox.
>> Right. Okay. I got a couple other ones
here. Let's lightning round. through
some of these. So the one of the
questions I believe was from Debbie
earlier is can it access files on your
computer if they are on the cloud? I
think in this case we're talking about
scheduled tasks but I'm not 100% sure.
>> Could Yeah, if we could clarify that
question. I mean uh if you've Yeah,
actually can we clarify that question? I
don't want to get
>> Yeah, I'll I'll I'll tag them if they're
still here.
>> Cool.
>> Okay.
Okay. So then uh the next one, Evan uh
oh had two more. Number one, what's the
best way to run claude code remotely
when on the go? Um I can talk a little
bit about this unless you have an option
you like, James. Um if you have a
powerful desktop at home but travel. Um
okay, I have a slightly different answer
for that. Uh and then number two, you
said to use Fable, how do you pick Fable
loweffort versus Fable high effort or
even Opus 5 max versus Fable low?
basically what's your what's your advice
on effort and model use? Um and I have I
have answers for both of those as well
if you don't have one.
>> Um let's do let's do the first one
together. So like what were you going to
say about running Claude from home or
>> so the way that I the way that I use it
and this is based off of Boris Churnney
um comments he made a couple months ago.
So who knows he might do something
different now. Boris is the creator of
Claude Code or one of the creators. And
so when he says this is how he uses it,
I say like, "Okay, that's all I'm gonna
do."
>> Um, and
>> um I think they might now do most um
coding in the cloud, but at the time he
said that he starts the project um
locally on his computer in the claw
desktop, uses auto mode, and then
remotes uh into it. So he's actually
coding on his phone with an instance
that's local on his computer. So it's a
little bit confusing to to to visualize,
but basically there is um you start the
you start at local and then you use
what's called remote control, which is a
toggle that you toggle on. What What
were you going to say, James?
>> Yeah, I have a few I have a few answers
to this. Um, I did a lot of research to
this a few months ago because I I was
going on holiday. I didn't have my
laptop, but I did want to be able to
like access this agent that, you know,
knows a lot about me. And so, at the
time, um, I used this GitHub repo, where
is it called the Telegram bridge uh, for
cloud code. And this is like a really
secure way of um basically like
messaging cloud code, you know, while
it's running on a computer through
Telegram. And you're basically piping
all your messages from Telegram into the
terminal which is running the code and
then it's coming back and telling you
what happened. And I made this diagram
that shows how it works, right? I'm on
my phone. I send a text or a voice note.
It goes through the Telegram bot API
through this bridge that this guy made
and then into my session. Claude does a
bunch of stuff, comes back, and I did a
load of like security work on this to
make sure that only I could access it.
It just felt it felt very fiddly though
and like it took a lot of like hacking
together, right? Um I agree that I think
the the easiest way now to do this and
maybe I can show you this. This is like
how I use Claude code. So, I just use it
in the terminal. And you just want to
type remote control.
>> And I'm going to enable remote control.
And then if I go to the claude code app
and go into code mode, here we go. My
session is open. And yeah, wow, it's
worked flawlessly actually. Um, if I
stop sharing my screen, um, and I hold
this up to the camera. So that is
actually the session that I was just
having with Claude.
>> Um and I could just keep going as long
as this computer is still running. So
yeah, that's I think if that's how Boris
does it, that's the simplest way to do
it.
>> Yeah. Yeah. The the And there's a UI to
do that in the in the app as well. So
like it's literally just start the chat
on local versus cloud and then you
toggle it on. So whether you're using
the app or using the terminal. Um, as
far as the effort uh versus model, how
do you how do you handle that? Because
you're doing a lot of agents, a lot of
scheduled tasks, so I assume you're very
rate limit and token conscious. Um, I'm
a little more manual, so I'm a little
more flexible with that, but how how do
you approach it?
>> Okay, a few things on this. When you use
skill creator, as well as trying to give
you the best possible skill, it tries to
make you the most token efficient skill.
So it does actually measure as it's like
going round and round. It measures um
like how many tokens you're using and
tries to optimize that. I [snorts] use
fable or opus to create the skills and
then I use sonnet or maybe even haiku
but usually sonnet sort of medium effort
to run the skill because if a skill is
quite simple like you know go through
granola pick out summaries and drop them
into doist that doesn't take like a
rocket scientist's brain that just takes
sort of relatively basic LLM so where I
can I will like specify a sort of sonnet
low to medium effort um and And
dayto-day I'm using Opus or Fable on
sort of medium to high unless I need
something done very quickly and then I
might drop to Sonic or drop the effort
down.
>> Um and I have been playing with like the
Chinese open weight models like Kimmy K3
and GLM 5.2
>> and actually inside your system. Yeah,
that's fascinating.
>> It's uh it's funny you ask. I I've got a
video coming out on this uh next week on
YouTube. So, I've started putting more
effort into my YouTube videos and I've
got an editor and this is my first
proper video coming out.
>> You guys plug it in the neuron.
>> I would I would love to. Thank you. Let
me show you what I've done. So I use
open router and for anyone that's not
aware open routter is this like
incredible platform for accessing like
all models
and you can access you know like
anthropic models open AI models meta
models and all of the like Chinese
models from like deepse Quen Kimmy GLM
and there's a way of um if you look at
the open router cloud code docs there's
a way of switching out inside a cloud
code there's a way of switching out your
like anthropic uh URL right so it asks
you like your base URL
they suggest that you switch out for
open router and then everything goes
through open router but the problem with
this is that
>> that switches your anthropic like your
claude usage to API billing and
immediately it's really expensive so you
don't want to do that
>> I've come up with a workaround where
claude stays on the subscription but
Kimmy and GLM uh actually go through the
API. So I've created some custom
functions and now if I type Kimmy, we
should see
Moonshot Kimmy K3 API usage billing.
>> But if I type Claude, then it shows my
Claude Max subscription.
>> So this took some hacking and like when
I release the video, I'm just going to
release a prompt that you can sort of
copy and paste and it'll do it for you.
Buting what I've been really impressed
by is that like um
>> GLM is is rapid. Like GLM's really fast
and it found stuff in a piece of work
yesterday that Fable missed. Um so yeah,
I'm like, you know, I'm I'm really
impressed by this. I'm really impressed
and I think this is maybe like what I'm
going to spend some more time exploring
is, you know, like how far can you push
these cheaper models?
>> Yeah. No, that's awesome. And that's so
I can't wait to watch this video. I'm
definitely going to apply that. Um I
would say so a good framework for people
and Enthropic released something not
that long ago maybe a couple weeks ago
where they tried to explain the
difference between model and effort and
when you would want to use one
>> you you should think of effort as like
the time amount of time that it's going
to spend on the task. So if you're
asking it to do something that really
would take you or anyone else a lot of
time and also a lot of context um you
you probably want to increase the effort
and increase the model. So that's kind
of the framework that I use where if I'm
like, hey, I'm going to have you look at
my entire code base and, you know, draw
some conclusions. Fable, you know, as
high is as high as I go on Fable. Opus
five, I crank it to max. And that's
because I I heard some advice that X
high and max make Fable kind of lose its
mind a little bit.
>> I've I've seen that. Yeah. And I've also
there's a feature they have called like
>> dynamic workflows where suddenly Fable
wants to spin up like 50 sub agents and
it just burns your tokens. Um don't do
that. So yeah, I yeah, I think the one
thing the one thing that I like about it
uh I think when Fable came out, the one
thing I thought was quite cute is if you
type effort in the terminal, like their
X high mode sort of like makes the whole
thing, if I do effort here,
>> um
Ultra [laughter] Code. Yeah,
>> I think this is so cool,
>> right? It's not even Fable. That's Sonet
as well. And that's going to put it to X
high with workflows. And when I did
this, it it literally spawned like 60
sub agents and I was kind of like,
"Stop, stop, stop, please. That's way
too much." Um, yeah, I agree. I
definitely agree with that.
>> Yeah. The the the caveat I'll give to
that is I do think if you have So, the
way that I've been using it is Fable is
like my planner. So, whenever I'm
talking about anything, hey, we're going
to do this new initiative on the project
we're working on. I talk into Fable. I
will have it write a detailed technical
specification. And I'm like, so you're
not just coming up with what we should
do, you're coming up with how we should
do it. And then I have it farm out sub
agents to do that. So my main chat is
still Fable. Hi. Um but but it all of
the work is being done by Opus Max or
Opus um or Sonnet Max. Yeah.
>> Yeah, that's Yeah, I do something very
similar. I I have a skill for like
product requirement documents and that
can again take like half an hour to an
hour. Uh then I will run a skill called
multi-agent refine where it spins up
like four or five sub aents usually like
a model down sometimes the same model
that will like critique the document the
plan from different points of view. Um
and then sometimes if I'm really
paranoid I'll get like codeex to take a
look at the plan and then when I'm sure
the plan is rock solid and I've thought
of everything yeah spin it spin it up
with like set sub agents to kind of
crank through it. Yeah,
>> I love that. I need to apply that
because I'm very much a let me get a
version of it and then see all the
problems with it and then go back and
fix it type of person. But I think to
level up my game, I gotta do some of
that. Okay, real quick. Um, uh, DDay
Brie responded and they said, "Yes,
scheduled tasks. You mentioned keeping
files on notion, but if you have files
in the Google cloud, are they accessible
in the context when your computer is
off?"
Good question with Claude and someone
correct me if I'm wrong on this. I still
think that you can only read Google Docs
uh with their integration. I don't think
you can edit Google Docs. So, for
example, if you've got like, you know,
sort of second brain set of files in
Google Docs, right, about who you are
and you want Claude to read it before
doing a scheduled task, I think it would
be fine. Um, [snorts] but if you wanted
it to like create a new document every
day or summarize, you know, every
Friday, create a retro document. I don't
think it can do that with Drive, but it
can definitely do that with Notion. So,
like the Notion MCP is like very, it
used to be kind of bad and now it's it's
all right. Uh, but the Google Docs
>> focus on it. Yeah,
>> they have. Yeah, I think Notion wants to
become everyone's second brain. Um, but
I think Google Docs and Claude for some
reason just aren't friends. And maybe
that's Google's like one way of clinging
on to Gemini [laughter] to to not
>> they have they have two ways of clinging
on to Gemini. Number one is that what
you just described and the second one is
you can't use anything besides Google
apps in Gemini. [sighs]
>> It's crazy. I have people come to me,
you know, to do this four-week program
and like they usually abandon Gemini in
the first week if they're using it
because you just can't connect anything.
I don't know what they're doing over
there. Um
>> perhaps they have a new launch coming
out today. I heard rumors of that. I'll
have to check after this stream. But
yeah, I think they're confused.
>> I think they are. And I think like
>> yeah, whenever they launch something,
they're like, "Oh, so what you want to
do is you want to go to our AI studio
and then you want to open anti-gravity
vertex, whatever, and then find our
Flash Omni Pro model." Like just
simplify it. Just Yeah. Yeah.
>> Yeah. Totally. No, I think they should
just make AI Studio the app and get rid
of all the other ones or make them
plugins in AI Studio. It's it's that
easy and they'll win or maybe not win.
They'll be competitive.
>> Okay, I have a couple more um real quick
that
>> there's a good correction from G
Hogarth, by the way. Apparently Claude
can write MD files to Google Drive. So,
>> oh,
>> I didn't know that. That's great. Yeah,
I was going to say actually on that
point that our company uh created a
custom um uh connector essentially so
that they can control like who can
access what and and that's a good
recommendation if you work at a larger
company is to you know don't you don't
have to go through the traditional
plugins that are in there. You can
actually create your own and you have a
little more control over it. Uh and we
can read and write to Google Docs but
this is on chat GBT is where I use it.
So little caveat there. Um,
>> yeah,
>> good good note there. So, this was from
Mobility FL, who if they're still here,
they're a real one. They came in at 9:30
and asked this question. [laughter]
And they said, uh, number one, how to
determine which agent is good and for
what task? I think we kind of covered
that. Um, how often do you re-evaluate?
I don't know if you want to address
that. Um, they have two more questions.
You want me to read them all?
>> How often do I reevaluate like different
agents or different skills? I think it's
like what agent you're using for what
task. How often are you re-evaluating
that?
>> So, some people think of an agent as
like some people have like 10 different
skills, right? And they call that 10
different agents. Like some of them are
like I've got my chief of staff agent
and I've got my product agent and like
the way I think about it is claude code
is my agent and it has a bunch of skills
and so I am very happy with like my
claude code setup. Whenever a new model
comes out I will sort of like take it
for a spin. Sometimes you have to like
change your skills. Sometimes you have
to change your cloud MD. Like Opus 5 for
example doesn't need as much handholding
and like strict instruction as 4.8.
Um, so yeah, I feel like I'm constantly
sort of trying to get the best out of
the newest model, but in terms of like
the agent that I use, I like the Claude
code as a harness is great. And then
like I mentioned, I'm testing out GLM
and Kimmy, but
>> you know, the Claude Max subscription is
so cost effective that I'm just going to
keep hammering that until they up the
price.
>> It really is. I was pretty impressed
with myself last week. I was able to get
100% model usage and 100% Fable usage.
Well done. Nice. Thank you. So nice.
>> Thank you. Thank you. [laughter] Usually
it's one or the other.
>> Yeah. Yeah.
>> Um the other question from mobility was
how to manage and see the tokens you use
so you can optimize. Um there is a there
is a feature called usage um inside of
the app but I don't know if you have a
better solution for tracking.
>> There is. Yeah. So in the app you can
use usage and cowork and cloud code in
the desktop app. They both will both
sort of like show you a little dial
where they'll sort of warn you. Uh, I've
installed a really nice plugin in the
terminal called Claude Code HUD. And so
this shows me the model I'm using, the
context of this conversation and my
usage that resets in one hour. Um, and
so if I if I like sort of switch through
these different, you know, these
different chats, like I can see the
context of each one. So I find that
quite helpful. But um honestly like I've
been using CloudMax 5X for like 9 months
and I very rarely hit the limit. Um
so yeah I I that I'll drop the link to
that HD plugin if anyone wants that but
um
>> Oh yeah, drop it in the chat and I can
share it. Yeah.
>> Yeah.
>> Um and then they had a question about
edge agents, edge AI models. I think
that's outside the scope of what we're
talking about today, but um do you have
any
>> What do you mean by edge? Edge would be
like, you know, you're running it
locally on your computer or your phone.
Oh, yeah. The best for that.
>> Yeah. Yeah.
>> I don't know there.
>> No, not really. [laughter] That's not
really something I've had to think
about. Like if you're Yeah. If you're
building a hardware startup, right? Like
then go and find like a really small uh
weight model. But like I I don't have
much to offer on that question. Uh, the
thing is like this changes all the time,
but the ones that people are really
happy with right now is Gemma. Um, I
think it was like Gemma 12B was was like
pretty good for the size. Um, there's
like some really cool small ones that
just came out. You I advise you read the
neurons around the horn digest to keep
track of those. That's on our website.
Um, and uh, and then allegedly you can
use things like DeepSeek and Kimmy K3 on
your computer at like two tokens per
second. I don't know who is running this
[laughter] or how
>> is it even worth it? Like two tokens a
second. I mean, I went and explored
yesterday. I bought like a Mac Mini 64
gig RAM and I was like, "Okay, it's time
to run Kimmy." And then I looked at the
size of it and I was like, "No way. It's
just not going to run."
>> But Gemma Gemma would run on that
machine, but like Kimmy K3, no way.
>> Yeah. Yeah. And then uh there was a new
Quen that just came out. I think it was
Quen um 3.8. And I think that one might
be People really like the Quen models,
especially for local coding, but they're
still not at the level of like Fable or
Opus yet.
>> Yeah. I honestly like three months ago I
thought I was going to go down this like
local model route and I bought the Mac
Mini and I thought, okay, it's time to
kind of like get some free, you know,
token consumption. I now think that just
pushing stuff through open router and
spending like pennies and testing out
the models in the cloud is way easier
than like you know installing old lama
and waiting like three hours to download
the file and set it all up. Um I think
open router is amazing and like a really
easy way to just test new models as they
come out.
>> I agree with that 100%. Let me share
that uh GitHub in here. I will say with
the caveat that I am very bullish on
local. I think we should have opus or
maybe even fa fable level of AI locally
on our computer and that's the future
and we'll eventually get there. We just
talked to Intel's uh Dr. Alennena Zoo
and she basically said you know if you
look at the chart the if the trends hold
we could have fable level AI on our
laptops within two months or two years
sorry not two months two years. Yeah, I
don't doubt that and I also agree and
like you know there's yeah if for people
who want like absolute certainty that
their data is not going anywhere like
that's that's the solution. I was I was
talking about it with a friend earlier
like companies will have just big you
know like sort of servers mainframes or
whatever to run all of this. Why would
you spend all your tokens with anthropic
when you know you can run it almost for
free on your own machines? Yeah.
>> And then there's also um all of these
third party providers. And so if you go
to this link which I'm sharing in the
chat artificial analysis for any model
you want to run you can look up and and
you know see who offers um basically
servers to run that model for you and
you know you can partition them they're
private that sort of thing. So
>> you know that's another solution if you
can afford it. Also, I haven't tried it
yet, but Open Routter have a cool
feature called fusion, which I think
tries to pick the best model for a task
and sometimes combines two or three to
get you like a sort of um panel of panel
of answers. Um
>> yeah,
>> definitely moving towards local and also
like getting two or three agents to kind
of work on a task together before coming
back to you.
>> Uh got one or two more here before we
wrap up. So, um if you if you have time,
do you have time?
>> Yeah. Yeah, I can stick around. Yeah.
Cool. All right. So,
>> it's quarter to 8 in the evening for me.
So, I'm I'm I'm done for the day.
>> Yeah,
>> that's great. [laughter]
Um, so, uh, Aber Aarian asked, um, where
do you start once you've got Claude
linked to Google ads and meta? Are you
using Claude for any like ad buys these
days as a solo business entrepreneur?
>> No. Uh, so far so far I'm lucky enough
not to be not to be buying ads. Um, I've
heard so, okay, so Meta released a CLI
for their ads platform like a couple
months ago and like giving cloud code
access to that is apparently quite good.
Uh, Windsor.ai is a nice MCP for like
plugging everything in. So you connect,
you know, Shopify, Meta, Google to
Windsor and then you just have one
connection to Claude and that handles
like all of it for you. I've heard good
things about that. Um, but no, I haven't
I haven't done much sort of like paid
paid spend in a while. I have I just
interviewed a guy who's running like a
growth agency this morning. Um, that's
become fully AI native in the last like
eight months and they pipe everything
into Big Query and they've built a bunch
of like Python scripts that any agent
can run to kind of like,
>> you know, pull the latest information
and then they have scheduled tasks that
check whether ads are fatiguing. And so
they'll kind of get a ping in Slack that
says, "Hey, like this campaign looks
like it's starting to fatigue. Uh maybe
we should like improve it." So loads you
can do, but not much I've done
personally in the last year or so.
>> That's fair. That's fair. Um GWPI card
said, "How do you set up background
agents either running periodically like
a cron or on a trigger like when X
launch Y automation workflows? You kind
of covered this, but do you have a
direct answer to that?"
Yeah, let me um there's actually that's
a good there was a good part of that
question which was like when this
happens do this uh and I didn't cover
that so let's cover that. Um, so you
know, my whole session I was in Claude
co-work, but there's also the code tab,
which is honestly very similar to
working with co-work just more powerful.
Um, and if we go into routines,
uh, and then new routine. Um, I think
it's local. You can basically,
nope, it's not local, it's cloud. Uh,
you can trigger it on an API. Uh so you
can basically say to uh Claude when I
send you a web hook um you know when I
like send anything to this URL I want
you to then go and sort of run you know
whatever task I have using my um
connected MCPS. Uh I actually I did have
a slide on this and uh the one thing
with it's disappeared. Here we go. Um,
the one [clears throat] thing with cloud
tasks in code is that they require you
to have a GitHub repository. So
>> you can run a local routine on your
computer without GitHub. But in order
for Claude to basically sort of like run
code inside of your folder in the cloud,
it requires you to have a GitHub
repository. Um, there was a question in
the chat about
>> Evan just asked about GitHub. Yeah.
>> Yeah. Um, it's just a way of it's a way
of like
>> just so you know, we we're going to do a
whole stream on GitHub in a couple
weeks. We're we're talking to someone at
Microsoft who can come on um and give it
like the whole the whole rundown. But
yeah, so you could give the Spark Notes.
>> Yeah,
>> Spark Notes is like it's a way of
collaborating on code with other people.
uh you basically host your your whole
codebase in the cloud and it's you know
usually a private repository but people
also give away code you know open source
for free using GitHub and when you have
your folder connected to GitHub an agent
can basically copy everything over run
code in the cloud on a different server
and then sort of like shut it down very
easily. Yeah.
>> Yeah. Yeah. And it it like we explained
earlier with plugins, GitHub, there's a
a really good GitHub plugin for cloud
code. So you can literally just set it
up, give it access to either all your
repos or select repos and you can say
like, hey, let's, you know, use the
GitHub plugin and let's push this code.
Yeah,
>> I Yeah, I did computer science at uni,
but in the last year, I haven't run a
single git command myself. I just
>> Yeah, [laughter] you just No, I just
>> ask Claude. I'm like, "Yeah, get onto a
new branch and like submit the PR when
you're done and run it through the
tests." But like, yeah,
>> that's what I told the GitHub people.
>> I was like, "If you're coming on, this
is what this is the way we're talking
about using it
>> because this is how I use it."
>> Yep. Yep. Yep. Yep. The one thing I do
actually, one thing I started doing a
few months ago with Git is using work
trees. Have you used work trees before?
>> Uh, Claude does it automatically. So, I
>> Yeah, go ahead. So basically the journey
that I went through and that loads of
people go through is like you discover
Claude Code and you have one tab going
and you're like hang on a minute and
then you start getting like four agents
going at once and you feel like Tony
Stark with Jarvis.
>> But then the agents start colliding and
they start like submitting PRs that kind
of conflict with each other and everyone
has that story where they're like, "Oh,
four hours of work just got deleted
because some agent thought it was
irrelevant." Um, so work trees basically
clone the folder on your machines so
that everyone's got their isolated
folder and they can like the agents can
collaborate without overwriting each
other's work.
>> Yeah.
>> So Ryan Carson, I don't know if you're
familiar with him. He's
>> Yeah. I've learned so much from just his
interviews. Genuinely
>> same 100%. and uh he was saying that
everyone needs to update their thinking
from coding locally to coding in the
cloud uh because of that reason where
basically if you have too many work
trees on your computer it's going to
fill up like I personally had this
problem where I was trying to download a
model and then it said there's like no
space on your computer
>> I had this yesterday I had like nine
work trees and claude was like well each
one's like several several hundred
megabytes for some reason so like
>> so the tip for that is tell it like when
you do a work tree send it to the cloud
like cuz you can you now have Claude
send send like different agents to the
cloud even though you're working
locally. You can just have it like do
that for you. And I think that's the
that's the tip there.
>> Um
>> nice.
>> Let's see. How transferable is agent
building from platform to platform? Um
if we review on one today, then I use
something different. Is it the same
process idea?
>> Great question. Great question. So a lot
of people they've been talking to chat
GPT or Claude chat for like a year,
right? and like they kind of feel like
Claude knows them or Chat GBT knows
them, but if that account got shut down,
they would lose everything. And
actually, I saw a message earlier asking
like why would I move from chat to
co-work. So, if we stop relying on like
the memory of the LLM and we start
relying on context, whether it's files
on our computer or whether it's like a
notion folder somewhere, we can actually
just drop in any agent we like. So, you
know, I just demonstrated earlier
opening like Kimmy, GLM, and Claude in
the same folder. They all see the same
instructions, the same context. If I
decide tomorrow, you know, if Anthropic
goes bust tomorrow and they shut down
Claude and I have to go and use Codeex,
I just pick up where I left off. Um, so,
um, which I really hope doesn't happen
by the way, that's not a prediction. Um
so um yeah like once you move away from
the basic like cloud chat products to
codework or code or codeex you're
actually making life like more portable
like it's easier to transfer between
them.
>> Yeah.
>> Yeah. And everything we talked about
with maybe the exception of plugins um
like is transferable. So if you have
your second brain on your computer
that's transferable to any system you
use. Um, if you have skills, those are
downloadable files that you can take
into. Uh, I think I said in the chat
earlier to answer someone's question,
but you know, I think Groth now uses
skills. Chatbutt definitely uses skills,
so it's transferable to those. Gemini, I
don't know where they're [laughter]
they're at on skills.
>> They might get them next year. Yeah.
>> Yeah. If you're lucky. Fingers crossed.
[laughter]
>> Um, and and uh what was the other thing?
The only thing scheduled tasks, but you
can copy the the logic from it. Yeah, it
gives you Yeah, it gives you a big
instruction as long as you've got the
right MCPs connected. I, you know, you
mentioned chat GPD for work earlier.
Like I tried it a couple months ago when
they had these like workspace agents.
They're really easy to set up. I think
they've actually made the UI I think
they made the UI a bit easier than
Claude for scheduled test.
>> So my problem is they're too easy to set
up and I was spending 800 million
credits like per week or something like
that. [laughter]
Like obviously this is on the
subscription so it's not you know me
actually paying this.
>> Um but they do this thing called um like
credits which is kind of confusing and
you run out pretty quickly. Um and I
think it's BS. I think it they need to
fix this ASAP because it makes it
impossible to use when it is a very
useful tool. Um so [clears throat] your
mileage may vary with workspace agents.
I was able to automate a ton of stuff
following basically the same workflow
that you set up today but in chatbt. But
the problem is you know I hit the limit
on workspace credits and like a week in
and there's three weeks left in the
month. So
>> it's not not a perfect system yet. But
>> that's why I think it's important that
we push for local models so that some of
this stuff can be done locally. And if
you use an independent agent like Hermes
or OpenClaw, some of the models like for
scheduled tasks can be run locally on
your computer even with open router,
right? You can
>> well this is this is actually yeah this
is something if we have like two minutes
I want to talk about my new favorite
agent harness. Um let's do it.
>> So do you use Verscell? Have you come
across Verscell?
>> Yes, we've talked about Verscell before.
Uh I use it occasionally. I try to
self-host a lot of stuff but but yeah I
like
>> Versel. So yeah. So like amazing for
just deploying you know any code you
write to the internet. Cloud code works
with it really well like makes it so
simple.
>> They've released this framework called
Eve maybe like a few weeks ago and it's
a framework for building agents and
basically you like open this up in any
folder on your computer and you just
like with it needs code. So you give it
this command right like start a project
and [snorts]
and it it basically creates an agent in
the cloud that you can sort of reach
across any channel. So like they have
got channels for where is it now?
Telegram h it's not here they got like
telegram slack um um WhatsApp you know
you can run it as like an agent that
lives on your website that people can
talk to. Um, and last night I thought,
okay, well, I have this folder on my
computer that I'm using for my like
health and fitness. So, I've got my
metrics coming in from Garmin, from
Training Peaks, you know, my blood work.
I open Cloud Code in this folder and I
can have like really interesting
conversations about like supplements I
might want to take or like my resting
heart rate trend, you know, all this
stuff. And like I've built a whole
health dashboard that I could show you
another time. But I ran Eve I ran Eve
inside it and within half an hour I had
an agent on Telegram called Healthbot.
And now at 7:00 a.m. it sends me a
briefing. At 12:00 p.m. it looks at my
My Fitness Pal and sort of says, "Hey,
you've had a bit too much sugar today.
Like maybe tone it down in the
afternoon. I need this. Um
>> you're coming back teaching me how to
make this. I literally [laughter] need
this. It's on my goals that try to get
better."
>> Yeah. It's cuz I kept thinking like if
something could just ping me throughout
the day like that would that would
actually change my behavior. And so and
I also thought like I want to track my
supplements but I I I can never find an
app that makes it easy. And so now, um,
I was talking to this agent in the gym
this morning and like, you know, I was
like, "Here's my weight and I've just
taken these supplements and then it
pinged me today at like 1:30 and it
said, "Looks like you've only had 60
calories so far and you've got a ride
coming up this afternoon, so you should
probably try to, you know, it was
amazing and like on Telegram, could be
on WhatsApp and it was just with Eve and
it's all running in the cloud and it can
switch any model. So, it's on Sonet
right now, but I'll probably pull it
down to something cheaper like GLM." Um,
amazing. So, yeah, I think this is like
I think this could be like the open claw
killer. I think this is like so easy to
use if you just point clawed code at
this this website.
>> Yeah.
>> Yeah. I think I think we're still
waiting for that thing that that
application that comes out that
abstracts away the like pointing it here
and pointing it there and just like
works out of the box like because I
think I find the hardest thing with
Hermes or OpenClaw or you know perhaps
even Eve although you tell me how easy
it is that you know you have to sign up
for these like end points and and you
know make sure that you have like a
clear gateway and that's a little bit
intimidating if this is your first time
doing this. You know what I mean?
>> Yeah. For Telegram, they made it really
easy. For Slack,
um, it looks pretty easy because like
we've all been through that process of
like getting a token and like
provisioning a new app just so that your
agent can sort of like send its first
message. And um, yeah, I agree. I think
like we're waiting for a platform that
just kind of allows you to spin up an
agent with the right context and the
right channels. I think Eve are like
pretty close to it. And I'm I'm I'm
bullish like after that experience of
like, you know, 30 minutes to like a
fully connected health agent that reads
and writes and uses tools in the cloud.
I don't even know where it is. Like it's
in a Versel server somewhere, right?
Like [laughter] I didn't have to like I
didn't have to spin up a VPS. I didn't
need to get my Mac Mini running. My
computer doesn't need to be on. It's
just like it's just on. It's amazing.
>> Okay. We we'll have to have you back to
to talk more about that. Um, so someone
asked before we wrap, what's the typical
monthly cost of deploying an agent like
the Healthbot?
>> Uh, so in the last 24 hours, it seems to
have cost me $2.
>> Um, and that's on Sonic 5,
>> and that's probably like 4050 testing
messages. So,
>> what if you switch that to DeepSeek
before?
>> Exactly. I'm going to And then I think
it will be like it will cost me pennies
to run. And if it costs me like, you
know, $10 a month, but I actually
changed my behavior and like have this,
you know, it's Yeah, definitely worth
it.
>> Yeah. Well, James, this has been
amazing. Thank you so much for for
spending the whole hours with us. I
think everybody shout out in the chat,
you know, if you found this
>> for the questions.
>> Yeah. Thank you everyone. And if you
didn't uh if you didn't get your
question answered, so what I do after we
do all these live streams is I go and I
take the transcript and I turn it into
an article where I try to answer
everything and put it in a nice order so
it's easy to follow. So definitely stand
stand by for that. I'll work work on
that for everybody. But uh James, where
can people go if they want to learn more
about you and and your work?
>> Uh you can go to agentacelerator.ai
AI where I like run a live program
teaching this stuff and there's also an
online course you can take. Uh I post
loads of stuff like this on LinkedIn so
you can just find me James McCauley on
LinkedIn and I share all this good
stuff. Uh and then I am doing more on
YouTube. So like subscribe on YouTube
and you'll find out probably tomorrow
how to run Kimmy and GLM inside of Cloud
Code.
>> Oh yeah, send that. You definitely
better email that to me because I I'm
very curious.
>> I will. [laughter]
All right, everybody. Thanks again. And
uh James, hopefully hopefully we might
uh we might work together again on on
some projects. I think
>> I think I've I've heard there's some
stuff kicking. I think you might you
might see me again on the neuron.
>> Yeah.
>> Very cool. Very cool. Well, uh for
people who don't know, we have a we have
a neuron academy uh our own course
platform that we're building right now.
I'll share a link to that. If you like
this, we create more content um like
this on there. Um, you know, we can only
do this once a week, but you know, loads
of loads of material on there for
everybody. So, with that, thanks for
joining in and uh farewell for now.
Humans.

## Source

- Type: article
- URL: n/a
- Author: The Neuron
- Published: n/a
