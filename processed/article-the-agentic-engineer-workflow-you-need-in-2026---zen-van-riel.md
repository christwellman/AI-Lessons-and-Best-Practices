---
id: "article_a49a410c"
title: "The Agentic Engineer Workflow You Need In 2026"
source_type: "article"
source_url: ""
author: "Zen van Riel"
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [agentic-workflow, git-worktree, context-management, code-quality]
summary: "The author shares a parallel coding agent workflow using four terminals with different effort levels. Engineers manage context windows by using compact or clear commands when conversation history grows too large. Git work trees allow independent work streams without branch conflicts across parallel windows. Professional engineering standards require architectural oversight and human review rather than uncritical code generation."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

The author shares a parallel coding agent workflow using four terminals with different effort levels. Engineers manage context windows by using compact or clear commands when conversation history grows too large. Git work trees allow independent work streams without branch conflicts across parallel windows. Professional engineering standards require architectural oversight and human review rather than uncritical code generation.

## Key Takeaways

- Run multiple parallel coding agent windows with different effort levels for different tasks.
- Reset or compress the context window when the AI response time increases or context drifts.
- Use Git work trees to prevent shared Git context conflicts across parallel agent sessions.
- Combine automated AI code reviews with human review to ensure long-term code quality.
- Apply software engineering book patterns instead of generic prompts to guide agent code structure.

## Techniques / Prompts Extracted

- Scope out five potential features we can work on.
- Explore the code base to tell me which languages are used.
- Create a test issue in  this URL.

## Full Content

# The Agentic Engineer Workflow You Need In 2026

**Author:** Zen van Riel

## Transcript

I've shaped AI code on real engineering
teams across enterprises and startups
with code reviews, production users, and
full accountability for everything that
I merge. Today, I'm going to show you
what my agentic engineering coding
workflow looks like, which relies on
real engineering practices. I will show
you my parallel setup for any coding
agents while sharing stories from our
real engineering experience that will
teach you how to speed up programming
work while preventing AI code from
hurting you in the future. First, I want
to show you how I work with coding
terminals. In my case, I'm going to show
you a shortcut that I have here that
launches four Claude code windows by
just typing T.
And the reason why I create four Claude
code windows is because very often
there's an opportunity to parallelize
some work with AI code, but not too
much. I'm not going to pretend like I'm
running 50 agents at the same time. My
mental capacity is pretty much at four
parallel work streams. This is just what
I've discovered after working on
multiple bigger projects together with
real teams. And in my case, to
understand my workflow, let's imagine
that we're working on this application
together. This is a bit of an auctioning
demo app that's developed in both Python
as well as Java.
Now, these four terminals are not the
same. If you've got a keen eye, you can
already see that here in the top left we
have Claude code with high effort. Here
on the top right is high effort as well,
but on the bottom left and bottom right
it's medium and low effort respectively.
And I'm doing this for a good reason.
Some work that you need to delegate to
an AI agent will take a long time to
complete because it's a big batch of
work. For example, I can start a new
plan session in here and say, "Scope out
five potential features we can work on."
I'm just giving it the opportunity to
explore, be creative. Now, on the bottom
right, I can now ask a much simpler
question.
Explore the code base to
tell me which languages are used.
And because this one is using low
effort, it will be done much faster with
the agentic loop. So, now you can see
that the top left is still going,
whereas on the bottom right, we already
have an answer to our question. It's
using Java, Python, HTML, and a little
bit of SQL. So, based on this, I know
where certain tasks need to go in my
work stream.
As we work in a chat, you will see that
eventually the current context window is
printed here on the bottom right. And
this is very important because as your
context window fills up, not only will
the AI take longer to respond, but also
it will eventually start to drift away
from the intended context of the
conversation. So, you might be super
familiar with this, but of course, you
can just run something like compact or
of course clear to start your
conversation from a fresh context
window. And here too, as you work with
these AI tools, you'll get a feeling for
when you need to reset the context
window. There is not one magic answer to
this. It depends on the complexity of
your project, the complexity of your
current piece of work. This is the whole
point of being an agentic engineer. You
need to just get a feeling for when to
compress your context window. If you
want to get access to my workflow,
including all of the scripts to launch
these windows, check out the link in the
description down below. You might be
wondering why I'm not talking about
specific planning techniques like
spectrum development or the B map
method, or why I'm not talking about the
difference between being a context
engineer, a prompt engineer, and an
agentic engineer. And to be honest, it's
because I think that a lot of these
things are just gimmicks that don't
really stand the test of time. Just
think about all of the different AI
projects that have become so popular
over the past 3 years. How many of those
projects are still relevant today? I'm
not saying that things like spectrum
development are a fad, but I do think
that anything that does work will just
be rolled up into something like Claude
code as time goes by. Like how Claude
code now has a good way to just keep
track of to-do's. You don't really have
to screw around anymore and do that
yourself with markdown files. And this
is honestly just the thing that I've
learned. I'm just awaiting the hype and
anything that survives three to four
months is probably really good patent to
apply. And you're not going to see
anything in this video that won't be
relevant anymore in six months. I'm only
going to show you principles that will
stand the test of time. So, another
aspect that's really important to
understand is how do you get your code
to a high quality? If you are an indie
hacker or even in some cases a
freelancer, code quality might not be
the most important thing because you are
not necessarily accountable for code
quality. Of course, if you're creating
your own business software, eventually
your customers will get into trouble if
you're the one creating the bugs. But at
that point, you could just vibe code to
fix, right? Well, in the professional
world, this doesn't really work because
you've got a team that you need to work
together with. If you create 10,000
lines of code in an hour time, how you
ever going to get that code into
production? Are some commands that I use
that really help me out. One example of
this is this smell command. And this
command is based on a couple of
engineering patterns that I found super
helpful from books that I read many,
many years ago including clean code as
well as architectural design patterns,
specifically design patterns for good
software development.
So, the smell command, for example,
refers to the clean code book. And clean
code is a book that I'll definitely
recommend you to buy, but of course, the
concepts are already part of the
language model, but it can help to kind
of push it into that direction by
reminding it of a couple of concepts
like this. And this way, you can
actually make sure that it follows the
patterns from those engineering books.
And to be completely honest, you can
choose to ignore my advice and go out
there and look at a prompt repository
that has 60,000 stars on GitHub and just
copy-paste all of that and use prompts
that say, "You are a senior engineer,
code and do not make any mistakes." It's
completely up to you. But if you want to
get serious with indentic engineering,
why don't you just apply the patterns
from really good engineering books that
have already been used to create some of
the best software in the world. In any
case, if you want to make a start with
that, check out the link in the
description below. Now, how about AI
code reviews? What do I do there? Well,
I actually do often connect GitHub to
all kinds of AI code review platforms,
whether it's a specific host of platform
like the newer Cloud Code Reviews or
just some self-created loop where I
create some kind of pipeline that just
automatically checks for my code using
something like the headless mode of
Codex. It doesn't really matter what you
do here, but I do think it's important
to have at least some kind of AI review
in your pull requests. The most
important thing though is that you don't
just rely on that, but you still combine
it with human review. And in fact, I
also have a couple of commands that I
often run to do some of the AI code
reviews before I create a pull request
out of it. Now, I'm not going to share
those commands with you. Why not? Well,
because there is not one command that
fits all. The right review command
depends so much on what you're building.
It depends on the programming language,
the complexity of the work, how many
human reviewers are even on your project
and what their preferences are, what the
code style is that your team agreed on.
There is not one size fits all. Speaking
of creating a pull request, how do I
connect to external services using my
coding agent? For example, it's super
simple for me to just take this GitHub
URL, go to Cloud Code, even the
low-effort one, and say, "Create a test
issue in
this URL."
It just already knows how to call the
GitHub CLI and I'm already authenticated
to it. So, there's no authentication
mechanism that Cloud Code is aware of
directly. The credentials are already
injected as part of my authentication
workflow that I went through when I set
up the GitHub CLI. And you can click on
it to go to it directly and there you
go. Nowadays, there's a big discussion
on whether MCP servers are really useful
for this, whether you should use a skill
that defines how an API should be
called, or whether you should just use a
CLI as is.
You can, of course, just use the bash
tool. And with bash, you can basically
execute
any kind of arbitrary script. So, you
can use bash to execute, say, a simple
Python script that calls a web API.
Maybe if the API is simple enough, you
can, for example, use curl to make a
direct web request. Or you could use
some kind of special CLI. For example,
GitHub has a CLI that you can use to
create issues, create pull requests,
etc. So, you can simply create and use a
bash tool. What you can also do, of
course, is you can rely on an MCP
server. And MCP servers were really
popular 1 1/2 years ago. I think they're
still very relevant, but you need to
understand when to use each service.
Personally, if you're using a very
common platform like GitHub or, let's
say, Jira, then there already a lot of
bash tools that you can use that even
the LLMs might not already know about.
When it comes to MCP servers, this is
really where it can connect with unknown
internal services much better. For
example, you have a coding agent that
you want to connect to some internal
diagnostic system, then an MCP server
can be quite useful. But even here,
I think the nuance of using an MCP
server or not really comes down to how
simple of an operation you need. If you
just need to execute a single command,
then bash makes a lot of sense, but
there are still MCB servers that I
really like. I really like Coptic 7, for
example, because with Coptic 7, you can
pull in the latest documentation for
your programming language or your
framework of choice. And of course, you
can do this with the web search skill as
well in Cloud Code, but it's much less
specialized. It will just do a generic
web search, and then it might return
something relevant, whereas with Coptic
7, there's a very specific back end that
will search the web, but it will also
cut up the documentation and present it
to the language model in the most
efficient format. Similarly, with
Serena, you can connect any coding agent
to a language server of choice, which
will often make search operations much
more efficient. So, here too, there is
not a definitive answer whether you need
bash or MCB servers. It just depends on
intuition. Intuition you can only
develop when you create interesting
systems with these AI agents. Now, I
wanted to talk a little bit about my
experience using AI coding at a
freelancing gig, at a smaller startup
scale, and even at the enterprise level,
because I've done AI coding at all three
now, and I will say that my experience
has been wildly different.
Let me start by explaining how I felt
when I was a freelancer at a couple of
side gigs that I did next to my regular
job. Well, these gigs were creating
proof of concepts, MVPs, and when you're
starting off on your project, well,
that's when you can really feel like you
are some kind of god developer, because
you're able to just be so productive in
the beginning and just push out so many
lines of code. And when you're creating
proof of concept,
there's not really a lot of people that
you need to give accountability to.
You're not having to show your code to a
development team every single day. Sure,
at the end of the project period, you
might need to improve the code base a
bit, add tests, etc., but it's really
not the same as working inside of a
software development team every single
day.
Regardless of whether you're working at
a startup or an enterprise, when you're
creating code with AI, the code needs to
be reviewed. Now, depending on what kind
of company you're working for, their
reviewing process is partially manual,
partially AI augmented, but in any case,
if you come to other developers with
10,000 lines of code every single day, I
can guarantee you that things aren't
going to end very well.
Either they're going to send you back to
create smaller scale pull requests,
or you're all going to suffer from
longer-term bugs caused by AI code that
was generated too quickly.
Now, here's where I have to face the
reality of things. I feel like the
people who are doing the best with the
agentic coding aren't screaming from the
rooftops that they're five times more
productive. They might see 30 to 60%
performance gains, and to be fair, they
might be really fast on certain cases,
like creating one-off scripts to test
something in production. But in general,
these people are benefiting from real
production gains without all of the hype
that is unsustainable. Because again, if
you're working on real projects, you
will find that the coding portion of the
engineering job is actually not that
much anymore. This is not saying that
you don't have a job anymore.
Engineering is much more than just
coding, but it is a shift in how you
need to distribute your daily work time.
Oh, now, one more thing about my Claude
status line that I really want to share.
I also have the name of the current
working branch. You can see here that
I'm on the main branch, and if I, for
example, ask Claude Code to check out to
a random branch,
you will see that whatever Claude Code
chooses will also show up here on the
status line. So, it's going to do check
out to a completely random branch name,
totally fine by me.
And once it runs this command, you can
see that this branch shows up here. The
only problem with this approach is that
the Git context is shared between these
four different Cloud Code windows. So,
if I for example say hi here, you will
see that my branch name will update to
the current branch. There you go. This
can work. You can still do parallel work
in the same branch, but eventually it
will get messy quickly. And this is
where you can create a Git work tree.
With a Git work tree, you basically
create a temporary copy of your code of
sorts that allows you to work in
completely independent work streams. So,
even if Cloud Code might be iterating on
the same files, for example, if you ask
Cloud Code to generate three different
approaches to the same problem,
you can still achieve that without any
conflicts by using Git work trees. And
you can of course ask Cloud Code to
create a work tree for you. In this
case, let's for example create a work
tree called branch
work tree test.
You can see here that it switches the
branch name to work tree branch work
tree test. And I even have a bit of an
indicator here that shows that this is a
proper work tree. Oh, and now I'm
actually lacking the room here to show
my context, but this isn't a problem
because these windows are actually
resizable. So, I can resize the window
like so to get the full context again.
And just to show you what this work tree
looks like in my file explorer, I'm
going to open Visual Studio Code. And
that what I can do is in my Cloud
folder, you have this work trees folder.
And you can see that branch work tree
test is kind of just a copy of the
entire repository. And of course, once
you're done with this work tree, you can
fully delete it because you don't want
your disk to be full of copies of your
code, right? So, for example, you can
just say exit and delete the
WT.
It'll understand that I'm talking about
a work tree just fine.
So, now it's cleaning up the work tree.
Go back to Visual Studio Code.
And the work tree is gone.
Just knowing how to use a work tree is a
big power move. Just remember that when
you create a new work tree, you might
have to reinstall the project
dependencies again, depending on what
programming language you use. Here too,
it all depends on your project. There's
not one trick that will work. But if you
do find yourself having to install
dependencies every time a work tree is
created, well, that's exactly when you
should create a reusable skill or
command that will be called every time a
work tree gets created. Maybe you can
even customize my scripts to create a
work tree whenever you start Cloud Code.
If that's your preferred workflow, you
should really get creative and customize
it to your own needs. I also remember
working in a much more complex
repository where I was able to create a
brand new feature in just two days. So,
I thought I'm going to create the pull
request, get it merged in by the end of
the week, and we'll be all set. The
thing is though, I got quite a lot of
pushback from more experienced engineer
in the pull request because while my
code was functional, it lacked a lot of
long-term architectural thinking. And I
have to admit, when I actually read the
code because I only skimmed it because I
wanted to create AI code faster, I
realized that this engineer was totally
right. It missed the bigger picture and
it was going to cause a lot of bugs in
longer term. So, when you're thinking
about the agentic engineering, it's not
so much just about the tools that you
choose to use, it's also about mindset.
What kind of engineer do you want to be?
Do you want to be a vibe coder who
pushes thousands of lines of AI code to
production every single day? Or do you
want to be an AI native engineer,
someone who benefits from the
productivity gains of AI, but also knows
when to fix systems when they really go
down, and can actually master the full
stack? Of course, I'm a little bit
biased. You probably know which type of
engineer I prefer to be, but it's up to
you, and it's definitely good to think
about it. If you want to get started
with agentic engineering, you can check
out the resources in the description
down below, or check out, of course,
more of my videos where I cover many
more topics like this.

## Source

- Type: article
- URL: n/a
- Author: Zen van Riel
- Published: n/a
