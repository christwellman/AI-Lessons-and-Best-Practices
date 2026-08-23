---
id: "article_cd5a77e8"
title: "7 Ways To Cut Your Claude Code Token Usage In Half"
source_type: "article"
source_url: ""
author: "Sean Kochel"
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [token-optimization, claude-code, context-window, cost-reduction]
summary: "This video covers seven strategies to reduce token usage and context window size in Claude Code. The author explores tools and methods for auditing waste, using terse language, managing intent layers, clearing context via handoffs, maintaining markdown files, querying code graphs, and proxying terminal outputs."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

This video covers seven strategies to reduce token usage and context window size in Claude Code. The author explores tools and methods for auditing waste, using terse language, managing intent layers, clearing context via handoffs, maintaining markdown files, querying code graphs, and proxying terminal outputs.

## Key Takeaways

- Audit session startup waste using the Token Optimizer tool to identify heavy skill definitions and MCPs.
- Use the Caveman skill to force terse, basic output language and cut output token usage.
- Manage project context in existing codebases by adding intent layer markdown files to directories.
- Use handoff skills to store research summaries and clear the context window before starting new implementation tasks.
- Keep Claude markdown files under 300 lines and focus on motivational intent, non-obvious tooling, and verifiable rules.
- Deploy code review graphs to let Claude query a structural graph instead of reading files in chunks.
- Use the RTK CLI proxy tool to filter, group, and deduplicate terminal command outputs before Claude reads them.

## Techniques / Prompts Extracted

- /token-optimizer
- /caveman
- explain how our app manages context summarization
- /intent-layer
- handbook
- code review graph build
- brew install RTK
- RTK gain
- RTK help

## Full Content

# 7 Ways To Cut Your Claude Code Token Usage In Half

**Author:** Sean Kochel

## Transcript

I've had a lot of requests for this
video topic. How do we stop burning
tokens so quickly? This problem comes
back, I think, to three core areas:
waste at session startup, input token
waste, and output token waste. So, in
this video, I'm going to go through
seven ways to chop down your context
window size to something more
reasonable. I'll go through each tactic,
talk about what it is, and show you how
to do it in a real project. Starting
with the most important piece, auditing
where your waste currently lives. So,
you can't really solve that what you do
not know is a problem. And this first
tool called Token Optimizer helps us
identify what is actually eating up our
context window. So, the way that we get
started with this is pretty simple. We
can come down here, and we can copy this
Claude code command, and then we can hop
down into our terminal, start up Claude,
and install the plugin. So, first we're
going to add the marketplace, and then
we are going to actually add the plugin.
So, once this thing is installed on our
machine, we can come through, and we can
run this command for Token Optimizer.
So, what this thing is going to do is
it's going to run through, it's going to
look at all of your session history,
it's going to look at your Claude code
setup on your machine, and it's going to
try and determine where exactly your
tokens get used. So, while that's
running, if we were to go look at the
GitHub repo to see exactly what it's
doing, it's running six different review
agents. So, it's going to look at your
Claude markdown file, any sort of memory
markdown file you have, it's going to
look at all of your skills, your MCPs,
your custom slash commands, and then any
sort of like settings and more advanced
things like your hooks and general like
Claude code settings. So, if we were to
pop in then and look at like, "Well,
what are each of these sub agents
doing?" They're basically receiving this
command to go through and read certain
aspects of each of these things. So, for
example, the Claude markdown auditor is
moving through and it is finding the
Claude markdown file and it's measuring
certain things like the line count, how
many tokens roughly we estimate that
that Claude markdown file is using, and
then it's identifying optimization
targets. Now, I will say the one
downside of a tool like token optimizer
is that a lot of these things that it is
doing right now could be done
deterministically. Like we could have a
script, for example, that actually
counts the total number of skills, the
total amount of front matter overhead.
All of these things could actually be
calculated with a basic script. So, this
is going to consume more tokens than it
needs to, but if you're only running
this as like a one-off audit, it's
really not the end of the world. Okay,
so now that that whole process is done
running, what it does is it actually
spins us up a dashboard where we can
look at the findings in a like kind of
easy to navigate way. So, we can see in
this case, we have about 25,000 tokens
in this case that get loaded up on
session start. Now, for a lot of people,
this number is significantly larger,
which is obviously a problem. So, if we
were to come down, for example, and try
to look at this based on like where does
that actually go, we have around 1,000
tokens coming straight from our Claude
markdown file. We have about 9,000,
which is crazy, coming from our skill
files. 750 come from {slash} commands
and 450 are coming from MCPs and tools.
So, for example, if we were to pop in
and look at these skills and think
through like, well, why is this using so
many tokens? Every single skill
definition that you have, the name and
the description, gets loaded in when
Claude starts a new session. The reason
it does that is because it needs to
understand if, based on the definition
and description of this tool, is it
something that should actually be used
right now. Now, the reason that I have
82 different skills is I'm building a
plugin library, so I have a lot of these
skills installed globally on my
computer. But, if you're somebody that
tests a lot of different skills, this is
something that you're going to want to
come in and address. Same thing with the
MCP tool. So, most likely the case that
between your skills and your MCP tools,
you have a big chunk of tokens being
used. Now, there's a lot of other stuff
that you can come in here and explore
that makes it really easy to move
through and disable skills, look at
things based on the severity, look at
things based on your habits, and
generally look at trends across how you
use things. So, if you really want to
optimize your token usage, you have to
know where you're starting. But, what do
we do from here? Like, if we've
identified this, this is just looking at
the things that happen, for the most
part, when a new session starts. But,
what do we do from there? How can we cut
down on our token usage as we are
actively building things? So, the next
tool up is actually a very simple skill
from Matt Pocock, and it is called
Caveman. So, we've seen a lot of
different implementations of this. The
main idea behind it is that you tell
Claude Code to essentially talk like a
caveman, talking very basic, terse,
short language to cut out all of the
filler and stories that language models
like to spin up about things. Because
the reality is that results in a lot of
token waste. Now, the thing that is
really valuable about Matt Pocock's
library, specifically compared with
other implementations of this, is that
it's optimized to keep full technical
accuracy. So, what that means is if
there's important technical language
that is needed to explain what is
happening, it's not going to cut that
stuff down, but it is going to
communicate it in a very direct,
straightforward way. So, maybe an
example is you ask Claude Code to
explain what database connection pooling
is. It's going to say, "Pool equals
reuse DB connection, skip handshake,
fast under load." Right? So, instead of
spinning up some narrative that consumes
like a ton of tokens, it's going to be
very direct and to the point. So, an
example of how we might use this could
be something like {slash} caveman,
explain how our app manages context
summarization. So, in the case of our
app, it is a chat-based recipe companion
that often needs to summarize
conversations, and we have some built-in
functions for that. So, let's see how
the caveman can explain how that works.
So, after like about 40 seconds, we can
see that it's come through, and it's
given like a very basic summary of how
this works. So, for example, it fetches
the context summary from the database,
loads the last 20 messages, injects it
as part of the system prompt, and then
this is what Claude sees. And so, we can
see it's a very direct explanation of
exactly how things work, and this is
realistically all Claude could needs in
order to understand how it actually
works. So, if you're moving through and
doing like a lot of planning, this is a
great tool to consider using. So, if we
were to scroll down, for example, and
just look at the usage on this one, it
took about 40 seconds and 42 cents worth
of Opus 4.7 credits. And if we were to
pop back in and run this in another
chat, saying explain how our app manages
context summarization, we can see how
there's like a lot more narrative being
formed around some of these things. So,
for example, if a summary already
exists, it prompts Claude Sonnet to
merge the existing summary with the
latest assistant response, capped at 500
words. Like, most of this sentence is
not needed in order to explain how it
actually functions. Now, if we were to
scroll down, we can see it took a little
bit longer, and it was about like 20
percent more expensive on the token cost
to give us this explanation. So, this is
like a very straightforward example of
how that works, but it's a very powerful
tool to consider using. Now, the skill
itself claims to cut token usage by
about 75%. I haven't seen that in my
testing, but even like a 30-40%
reduction in tokens being used,
especially output tokens, is a huge win.
Because realistically, this was just one
pass of the planning phase. If we are
now continuing this conversation and
going through multiple passes, those
types of token savings will really
compound over time. So, if you want to
get a lot more mileage out of each of
your sessions without wasting tokens
needlessly, this is a great tool to
consider using. But this is really only
solving the problem of output tokens.
So, what do we do about input tokens?
Because a massive amount of waste
actually takes place before the model
even responds to you. So, one big
problem that I get asked about a lot is
specifically how to manage this stuff in
the context of an existing codebase. A
lot of YouTube tutorials in particular
tend to focus on like greenfield things
showing you some new tool and building
something from the ground up, but they
often don't look at like how do you
manage this type of stuff in a project
that you already have. And Intent Layers
is one tool that can really help us save
on tokens in an existing project. So, we
can install the skill and then come down
into our terminal and actually run the
command {slash} intent layer. So, the
reason this thing works is that
generally speaking, when Claude code
starts up a new session, it doesn't
really have much context at all about
things that have already happened inside
of the project. And what that means is
when you ask it a question, it needs to
spend time and tokens trying to
understand the actual grounding of the
project, reading files, basically trying
to understand based on what you have
just asked which files and functions are
even relevant. It will try to read those
things in chunks, send it back to their
APIs, and then try to start building a
plan from there. And the problem with
that is that number one, that is a token
intensive procedure, and number two, it
might not necessarily gather all of the
context about what you know about your
project and how it works and the caveats
and edge cases that you've run into
before. So, basically the way that this
works is that it's going to look at all
of your app directories and it's going
to try to parse out and understand how
many tokens are inside of that
directory. Now, anytime there are more
than roughly 20,000 tokens, it's going
to put a nested Claude markdown or agent
markdown file in that directory that
gives a lot of detail about what is
inside of it and how it's meant to
actually work. So, now that this thing
is done running, we can see that we have
this new update inside of our projects
agents.markdown file. We have this
intent layer section which has a listing
of like the primary pieces of our app
architecture and where everything lives
and the types of rules that will be
found inside of those sections. And then
we have this global invariants section.
What are things about our project that
aren't immediately clear simply by
reading the code. So, an example of like
one of those conventions might be that
any error that affects billing and
authenti- cation must go through our uh
century configuration. So, we can
actually capture those errors and get
notified when they're happening. Now,
the thing that's really cool about this
is that it's creating a separate agent
markdown file that will be read by
Claude code or Codex or whatever anytime
you go to work in one of these areas.
So, say for example, we were going to
make an update to our Stripe payments.
Well, when the session starts and this
file gets read, it's going to know that
it needs to read this specific file
first. So, what lives inside of this
file? If we were to go into our project
and actually look at this new file
that's been created, it's giving a very
token efficient explanation of
everything inside of this directory and
what specific files handle what specific
things. And so, one example might be
like in the anti-pattern section,
something that a language model might
decide to do is to maybe manually call
the Stripe API in order to like work
around some sort of bug that you don't
even realize it's trying to make this
work around as it is building. And so,
we can give an instruction that it's
never allowed to bypass this get or
create Stripe customer function, which
is actually what handles the logic for,
in this case, creating a new customer.
So, similarly, if we're to look inside
of like our main app directory, we have
this agent markdown file, and it's again
going to explain how everything works.
What is the logic of the route grouping?
How does the middleware actually work in
the app? What are the important patterns
or conventions that should be followed?
And then, what are our related context
files that you should be aware of if you
are again working with any of this. So,
this is probably the easiest to
implement, yet highest impact, thing on
this list, especially if you are working
on an existing project. And so, in a
bit, I'll show you another tool that
solves a similar problem in a different
way, but first, let's talk about how we
can manage the context that gets
generated in the middle of a
conversation. So, one convention that
most good AI coding skills and plugins
follow is having scratchpad systems in
place. Meaning, we generate a bunch of
context, we keep what matters, and then
we move it into the next stage of the
conversation, typically with a clear
context window. And so, especially with
these 1 million token context windows,
you can spend a lot of money very
quickly if you are not paying attention,
which is why I tend to limit the usage
of those windows to 25 to 30%. So, one
example of a skill that can really help
us out with this, again, comes from Matt
Pocock's skill library, and it's called
handoff. And so, I personally find a lot
of the time that compacting a
conversation is not really the thing I
would want to do. I just want to have a
detailed summary where I can completely
clear the session and just move into a
new chat to to implement on the thing
that I just spent time brainstorming
around. So, let's say for example that
we want to improve the rate limiting
inside of our app, and a really helpful
pattern is to go out and explore or
research the problem domain first. Then,
based on those findings, we can start
building a plan out for how we want to
actually fix this thing or address the
thing that we're researching. So, after
about 5 minutes, our research is
complete, and we have these takeaways
for how we could consider putting rate
limiting in place in our app. So, we
have some documentation here. What are
the libraries we would use? What are the
critical rules we would need to follow?
What are the different algorithms we
could consider using for how the rate
limiting is going to actually like go?
Now, let's say for whatever reason,
maybe we continue this chat, and we
continue to aggregate more context, or
we just need to be able to store this
output for a later implementation. We
can just come through and run this
handoff command, and then it's going to
ask us, "What is the next session going
to be used for?" And we could say,
"Implementing rate limiting, or rather,
building a plan for implementing rate
limiting in our app." And so, now that
this handoff command is complete, we can
see that we've transferred over all of
that context that we just spent time
generating, and we can now kick off a
new session in order to actually
implement anything that we found inside
of this that we would want inside of our
project. So, scratchpad systems like
this are great, but one thing people
really don't talk about enough is the
slow death caused by a bad Claude
markdown file. So, a lot of conventions
that people use inside of their Claude
markdown file are honestly like kind of
old and out of date, and I think this is
something where like engineers that use
AI coding tools are really good about
having disciplined Claude markdown
files. And people that are more of like
the vibe code first, they don't really
give the Claude markdown file the type
of justice it deserves. So, the
consensus today is that these things
should be pretty light, less than 300
lines long, but there's also like very
specific things that they should include
inside of them. The first thing is
motivational intent or like a project
one-liner. The thing with language
models is that they will inevitably face
a situation where there's ambiguity in
what needs to be done. And when they
have motivation of your project or your
intent behind anything that you're
doing, they tend to hit the mark of good
a lot more easily. So, having a
one-liner inside of your cloud markdown
file that explains the purpose of your
project and the motivation behind it is
really valuable. The second thing is any
non-obvious tooling. So, language models
are actually really good at seeing
patterns and knowing the things that are
obvious based on what is in your project
already, but anything that is not
obvious or are like package-specific
considerations based on your project
setup are the types of things that
should be documented in your project.
So, for example, if you use Next.js to
build your apps, a lot of the training
data of current models is based on
out-of-date Next.js documentation. And
so, this is an example where you would
want to specifically tell it the version
that you are using and known constraints
or differences in that version in the
context of your project. So, we can
actually see an example of this inside
of that agent markdown file that we
created earlier with intent layers,
where proxy.typescript is the new
middleware for Next.js. And so, the
reason something like this is important
when you're going through and you were
building things that touch that
middleware layer, something like Claude
code will go out there without this type
of instruction and try to tell you that
you don't actually have a middleware
file in place and then invent one,
create one on the fly, and then next
thing you know, you've got a bunch of
errors inside of your app, things aren't
hooked together the right way, and it
generally becomes a huge pain in the
ass. Number three, a concise
architectural map. Now, this doesn't
mean having like diagrams explaining
where everything is. Again, a tool like
Claude code or Codex is going to be
really good at inferring things based on
the structure of your project. So,
anything that deviates from the norm is
going to be super valuable to document.
And by the way, if you want an example
template of one of these files, I will
link to one in the description below
this video. And so again, we can see a
version of that inside of this intent
layer output. Rules with verifiable
instructions. So, for example, instead
of saying write clean safe code, saying
something like parameterize all SQL
queries. Hard constraints and
anti-patterns, which again is something
that we saw inside of those nested
Claude markdown files in our project
earlier, again with the intent layer
system. So, an example of that might be,
"Don't add a new public route inside of
our app without updating the is public
path handler, or else people are going
to get redirected to login." Pointers to
deeper documentation about specific
things. So, for example, inside of these
areas, if your Claude markdown file is
getting too large, so you're starting to
get past this 300 line limit, you can
start breaking some of those things down
into rule directories that get linked to
and called when they need to be read.
But also, that intent layer system is a
perfect example of pointing to deeper
docs inside of the code base. And then
last but not least, gotchas and tribal
knowledge. It's inevitable that as
you're building things, you will run
into errors, run into issues that you
have to work around, and you want to
make sure those things are documented so
they they do not resurface later on in
time. So, putting all of these things
together makes for a really strong
Claude markdown file. And the thing that
is interesting about this structure is
it's all based around this idea of
documenting things that aren't going to
be obvious to the model, because they've
come a long way in being able to
recognize patterns. And so, the real
intent of this file is to tell it
anything that it couldn't know by just
inferring it from the code or the
structure of your project and then
generally telling it other things that
are just simply not obvious. So all of
those old conventions about how to name
files and folders and all of that type
of stuff is honestly a little bit of a
waste. So this one is pretty simple
conceptually, but you just need to be
disciplined about it to actually get it
right and grow this file over time. The
founder of Cloud Code updates his Cloud
Markdown file on a weekly basis. And so
that's something that all of us should
be doing too. But like I said earlier,
we have another method for pointing
Claude to specific files and functions
that we want it to be aware of in a
little bit of a better way. And so what
I was talking about are code graphs. Now
this concept of a code graph is starting
to get a lot of traction. That's why we
see a lot of libraries attempting to do
the same exact thing right now. If you
were to go look at GitHub's trending
repos, there are probably three of them
that are trending over the last day,
week, or month that are all trying to
solve this same problem. How do we give
a AI coding tool more contextual
understanding of the actual structure of
our code base and where certain types of
things actually lives. So the reason
people are making these tools is that
the way that Cloud Code like kind of
works right now is that when you ask her
a question, it needs to read all of your
files in chunks and it tries to gather
context about the problem that it is
being asked to solve. And honestly, it's
it's pretty good at doing that, but we
can always try to do things better and
that is what these code review graphs
attempt to do. So instead of it having
to read files in chunks, it's instead
going to query a graph that sits in
between Cloud Code and your code base.
So if we were to install this thing and
then come down into our project, we
could type in the command code review
graph build and we can see very quickly
that it has indexed and built a graph of
our entire project. So, for example, if
we were to come down now that this is
installed and ask a question like how
does forking inside of our app work, we
can see that instead of just reading
files, it is using this code review
graph MCP server. And so, the reason
that this is a little bit different than
how Claude Code would work out of the
box is that it finds the like original
files that we're talking about in this
context, but now since it has like a a
graph understanding of the code base,
meaning all of the different functions
and the different imports and how
they're related to each other, it can
very quickly go from this fork action
file to all of the different children
and all of the different other files
that call it. So, it's able to very
quickly come to an understanding about
how something works and the exact flow
and order of things because again, it
has a knowledge graph of the code base.
It has a deeper like semantic
understanding of how the code base is
actually structured and what connects to
what. And that is not something that
Claude Code actually has. And so, a lot
of people claim that there's big token
savings with tools like these and I
think you tend to get like some degree
of token savings, but the biggest thing
that I have found using tools like this
is that it can retrieve similar context
a lot faster. And the reason for that is
instead of having to again like read
files in chunks and try to understand
how everything is connected, it's just
told how everything is connected. Now,
the thing that's really cool about this
is as you move through and actually make
changes to your code base, you're making
commits, it's going to update this graph
over time and it can actually help you
understand better how other files might
be impacted by what you're doing. So,
for example, it will run a blast radius
analysis, which means anytime you change
a file, it's going to look at every
single other file that calls it or is
dependent on it or tests it. And then
our AI models can read those files
specifically and determine if there's
something that needs to be done. So, I
haven't experienced 49 times fewer
tokens. I have experienced a little bit
of token efficiency when you're doing
larger tasks, but the biggest thing that
I have noticed is that it tends to be a
lot faster at getting to a solution with
really good accuracy, meaning it's
finding the same types of things that
Claude code would eventually find. So,
last up on this list is another one that
is really easy to implement and has a
surprisingly big impact on your token
efficiency. And so, this app is called
RTK, and it is basically a tool that
sits in between your command line and
Claude code, and it cleans up all of the
outputs to that terminal that Claude
code would otherwise read. So, for
example, when Claude code is running
like a list everything in this directory
command or it's trying to read
everything in a file or search for files
or run a get status command or a get
diff command or run tests inside of your
project, it's reading the output of all
of those commands. And so, the result of
that is that you can honestly waste a
lot of tokens by having Claude code just
read outputs that it doesn't actually
have to read. And so, the way that you
install this, the simplest way, is to
just use Homebrew and type in brew
install RTK, and it from there will work
pretty much out of the box. So, just to
show you an example of this, if we were
to come down into my terminal and run
RTK gain, these are the token savings
from using this tool just in the time
that I have been recording this video
that we've all been watching. 192,000
tokens saved by using this tool. And the
reason for that is that I had to clean
up one of my work trees before I ran
that intent layer skill that we looked
at, and that required running a lot of
get diffs and helping me manage
different conflicts in my merges and
running all of those like get status
commands and the get diff commands and
reading the files. That is something
that would have taken like a ton of
tokens. And in this case, we were able
to cut down on about 160,000
tokens by simply using this RTK command
as a proxy. Now, the way that this thing
works is that it sets up a hook inside
of your coding agent. So, anytime it
sees that it's going to try to use a
command like get status, it is instead
going to use that RTK command. So, as an
example, if we wanted to see like what's
the difference between our current
development branch against some other
branch that we have, it's now proxying
through this RTK command in order to
gain an understanding of whatever it is
that we're asking. So, in this case,
it's running RTK get log instead of the
conventional get log. And so, all of
these commands are again like proxying
through this RTK library. And what that
means is that we're going to be saving a
lot of tokens by filtering out
information that isn't necessary really
for Claude code to see. And we can
always override it if we need to. So,
there's really four ways that this thing
works. Uh number one is smart filtering.
So, if there's any sort of like just
general noise like comments or white
space or boilerplate inside of an
output, it's going to filter that out so
that Claude code doesn't need to waste
input tokens on reading it. It can
aggregate similar items together. So,
for example, maybe your terminal is just
dumping the same 500 error over and over
and over and over again, it can group
those things together and then just tell
Claude code how many times it's
happening. In the case of things like
get logs, it can keep the relevant
context and then truncate or cut out
like really long descriptions or
redundant information. Again, it can be
overwritten if it needs to be to go
gather that info if it's really
important. And then kind of similar to
what I described in grouping, it can
deduplicate things. So, if it has
repeated log lines, it can just show
that one time with the count of how many
times that thing is happening. So, these
are like the four primary strategies
that get applied to every single command
that gets used. And so, if you want to
see how much this is actually being
effective for you, again, you can run
this RTK gain command, and this is going
to show you exactly how many tokens it
saved you through those four methods
like the filtering and the grouping and
all of that stuff. And the thing that's
pretty cool about this, if we were to
come down and do RTK help, we can
actually rewrite commands and customize
this if we ever encounter something that
is outside of the scope of what it has
been trained on by default, we can move
through and build our own commands,
which is pretty cool. So, there you have
it, seven tools that will really help
you cut down on the amount of tokens
that you are using. So, of the tools on
this list that we went through, there
are four of them that I actually use on
a daily or weekly basis. The RTK proxy
that we just went through, the intent
layer tool, and then both of Matt
Pocock's caveman and handoff skills. I
use those on a weekly basis to really
help cut down on my token usage. There
will be a link to that Claude markdown
file that I mentioned earlier in the
description below, but that's it for
this video. I will see you in the next
one.

## Source

- Type: article
- URL: n/a
- Author: Sean Kochel
- Published: n/a
