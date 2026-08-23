---
id: "article_c1c5e81d"
title: "I Tried 100+ Claude Code Skills. These 6 Are The Best."
source_type: "article"
source_url: ""
author: "Tech With Tim"
published: ""
ingested: "2026-08-23"
category: "tools"
tags: [claude-code, mcp-servers, ai-agents, developer-tools]
summary: "The author tests and selects six useful skills and tools for Claude Code. These additions improve software development, deployment, web scraping, writing tone, tool management, and security auditing."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

The author tests and selects six useful skills and tools for Claude Code. These additions improve software development, deployment, web scraping, writing tone, tool management, and security auditing.

## Key Takeaways

- GStack provides twenty-three skills for building software products and managing startup workflows.
- Hostinger MCP server allows users to manage virtual private servers and deploy websites directly from the terminal.
- Firecrawl enables scalable web crawling and data extraction while bypassing CAPTCHAs and rate limits.
- Humanizer skill rewrites AI text to remove common markers like m-dashes and make output sound natural.
- Composio connects thousands of third-party apps through a single MCP server to save token context.
- VibeSec skill audits codebases for security vulnerabilities and prevents insecure coding practices.

## Techniques / Prompts Extracted

None identified.

## Full Content

# I Tried 100+ Claude Code Skills. These 6 Are The Best.

**Author:** Tech With Tim

## Transcript

I've tried hundreds of Claude code
skills. In this video, I'm going to show
you the six most useful and give you a
full tutorial on how to set them up and
configure them. All these skills add
additional features and capabilities to
Claude code and I guarantee one of them
will be useful to you. So, stick around
and let's dive in. Okay, so the first
skill that I have is actually a set of
skills and this is a full repo called G
stack which comes from Garry Tan, the
president and CEO of Y Combinator. If
you look through here, there's actually
23 different skills that are included in
this kind of bundle that he's created
and this is effectively his solution to
being able to create software products
using Claude. There was a lot of
different skills that are bundled inside
of here. I'm not going to go through all
of them, but I'll just explain this is
essentially for founders and CEOs, first
time Claude code users, tech leads and
staff engineers. And if you want to read
through the whole kind of methodology
and how he came up with it, it's
included in the read me here. Now, I'm
going to show you how to install it, but
the key skills that he's mentioning to
run here at least to test it out is the
office hour skills, plan CEO review,
/review, and then QA. Now, this is
specifically designed for again, people
who want to build software products. So,
if you want to write code, if you want
to build a startup, if you want to build
something useful for even yourself or
your mom, this is a great skill kind of
bundle to download and set up. If you
scroll through here, you'll get a full
list of all of the skills that are
included. So, you can see office hours,
plan CEO review, review, investigate,
design, QA only, etc. And again, this is
built by Garry who's kind of an expert
in building software products and
investing in them given that he's the
CEO of Y Combinator. Okay, so how do you
actually set this up inside of Claude
code? Well, if you go to this link, I'll
leave it in the description, there's a
large paragraph here that you can just
copy. So, if we just copy this paragraph
right here, we can just go and open up
Claude code. In my case, what I did is
just went in the terminal and just typed
Claude and then I'm literally just going
to paste this inside of here. I also put
auto mode on just so it can do
everything itself and go ahead and press
enter and you're going to see here that
what it will do is go, download, set all
of this up. We'll wait a second and then
I'll show you some basic usage. Okay, so
it's just asking me to proceed. I'm
going to say yes.
Proceed, and then it should go with
these steps. Okay, so it's almost done
adding it here. You can see a list of
all of the skills that's going to set up
for me. So, I'm just going to go yes,
create the clawd.md,
and it's going to list out all of the
skills that are available. And then
boom, it says, "Okay, we're all good
here. We've created this list, and now I
can start using them." So, what I'm
going to do is I'm just going to get out
of this, and I'm going to change into a
directory where I have some kind of
coding project going on, or at least a
new one where I want to create
something, and I'll show you the basic
usage. Okay, so I just opened clawd here
in a coding project I have, which is
like some internal accounting software
that I'm using. And again, we'll go
through the quick start. So, the first
command we can run is the office hours
command. So, we're going to go slash
office hours like that, and then we can
describe what it is that we want to
build in terms of a new feature, the
overall application, and then GStack
will take over. So, I'm going to say,
"Hey, I would like to build an internal
accounting software for my YouTube
business where I'm tracking invoices,
expenses, and just generally kind of the
financial health of my business."
Okay, and let's see what we get. So, you
can see now it's kind of prompting me to
ask like, "What's the pain? Why am I
actually building this application?" You
know, I can submit this answer, and it's
going to go through and start to
understand better why I'm actually
building this. Now, after that, we could
go on, and we could use the slash plan
CEO review, the plan engineering review,
the review, the QA command. I'm not
going to show all of them cuz that's
going to take a really long time. It
could be a full video. But, the point is
if you're building something, you can
use all of these different skills, and
it's really going to make sure that you
build something that's actually useful
and that's validated rather than just a
random vibe coded project. Anyways,
that's GStack. Play around with it. It's
very cool. Have a look at the repo. It's
pretty well explained. Now, let's move
to the next one. Now, the next feature
that I want to add here is related to
deployment. Now, a lot of times I'm
building apps with clawd code, and then
what I want to deploy them, I actually
need to leave the terminal. I need to go
buy VPS. I need to spin up some hosting,
whatever. Now, rather than doing that,
you You actually bring that full
functionality into clawd code, so you
can simply just say, "Hey, deploy my
application. Hey, put it on this URL.
Hey, spin up a new VPS for this API."
And it will just automatically be
handled. Now, this is obviously
specifically for developers, but it's a
really good skill, and I'm going to show
you how to add. Now, the way that I'm
going to do this is by adding the
Hostinger MCP server as well as the
Hostinger Agent skills. In order for
this to work, you will need a Hostinger
account, and you're going to have to
have some kind of VPS. Now, you can
actually purchase it directly from the
terminal, but because I have a
partnership with Hostinger, if you go to
the website, I'll leave a link to it in
the description, the plan that you're
probably going to want to go with is the
business plan here, which is as low as
$4 per month. And with this, you're able
to deploy up to 50 websites, you get a
free domain, you can deploy manage
Node.js applications. And again, we can
connect this directly to CloudCode,
which I'm going to show you how to do.
So, I can just say, "Hey, go deploy my
site to this URL," which I'll give you a
live demo of. So, if you're interested
in having a virtual private server
connected to CloudCode that you can
deploy to and use from the terminal,
what you can do this is just go to that
link. You can put in the duration that
you want. And then again, because I have
the partnership, you can put in the code
TechWithTim, and that will give you an
additional 10% off any plan as long as
it's 12 months or above in duration.
Then, if you want a domain, so for
example, maybe I want my name, you know,
timbersika.com or something, I can type
that in here, and I can actually get
that 1 year for free. So anyways, I'm
going to proceed with this, and then
once I have the VPS, I'm going to show
you how to connect all of the tools to
CloudCode where it can automatically
deploy, set up, spin up the websites,
etc. Now, once you subscribe to this
flow, it's going to ask you, you know,
what domains you want to use, and it's
going to try to prompt you to deploy a
site right away. You actually don't need
to do that. What you can do for now is
just get out of this onboarding flow.
You'll still have everything created
just waiting for you to kind of finish
it here. And then what we can do is go
over to API. Now, from API here, it
shows you directly how to add the MCP
configuration to CloudCode, so we can
literally just copy this config right
here from the API page. We can go to
Cloud, and we can say, "Add this MCP
server to my configuration."
Okay? And then I'm just going to paste
in the config, and then go ahead and
press on enter, and it should be able to
automatically change the MCP config to
add the MCP server. Now, while it's
doing that, you'll notice that it needs
an API token here to connect to your
hosting or account. So, if we just go
here to the API page, we can generate a
new token. So, I'm just going to call
this
I don't know, Claude Code, give it an
expiry of whatever you want. In my case,
I'm just going to go never expires, and
then I'm going to generate that and copy
it, and obviously don't leak it to
anyone. Okay, so it looks like it's all
added here. Now, what we need to do is
we need to update this here to be our
token. There's many different ways to do
this. For example, you can just directly
edit this file here if you know how to
do that. You can set this as an
environment variable, or what we can do
if we're lazy and we don't really care
too much about the security is just tell
Claude Code to add the token for us. So,
I'm going to do that even though this is
not best practice and not recommended
because I'm going to delete the token
afterwards. Hey, can you please add this
token to the MCP config? And then I'm
just going to paste the token. Don't
worry, I'll delete this afterwards, and
then hit enter, and it should add it for
me and then connect. Okay, so now we
just need to restart Claude Code in
order for the MCP server to work. So,
I'm just going to type {slash} new, and
then {slash} MCP, and you'll see the
Hostinger MCP is connected with 118
different tools that we can use. So,
what I can do now is just directly tell
it to deploy site or create a new VPS or
whatever. So, for example, I'm going to
say, "What can you do with the Hostinger
MCP server? Give me a quick summary."
Okay, let's see what we get. Okay, so
you can see that we can create a VPS, we
can manage snapshots, we can buy a
domain, we can check the availability,
we can DNS, whatever. So, we can do all
of this stuff directly now from Claude
without actually having to go over to
the UI. Now, what I'm going to say is,
"What domains do I have available?" And
for your case, you should get one,
right? Because if you signed up with
that plan, you would have gotten one for
free, or you can purchase additional
ones from Hostinger. It's going to give
me the list here, and then I'm just
going to tell it to make a super simple
website and deploy so you can see how it
works. Okay, so you can see we have a
few different domains available here.
So, what I can do now is something like
this and just say, "Hey, can you create
a super simple website that just says,
'Hi, my name is Tim.' and deploy that to
timrasica.com?"
Boom, press enter and it should just be
able to do that. And again, we now
handle all of the deployment directly
from Claude. We don't need to go to a
third-party source and we can just
deploy a site, spin up a VPS, all from
the terminal. Okay, so it says it's
live. Let's go now to the URL and let's
check it out and see if it works. And
there, "Hi, my name is Tim." Right?
Super simple, that's just what I asked
it to do, but it deployed it, it's live,
it's working, all from the terminal.
That is the Hostinger MCP server. And
just to note that this is only going to
work once you register your domain. So,
what I actually did here is just from
the UI, I went to my domains, right? I
just had a look at the domains that I
had and I just made sure I registered
this because you do need to say who owns
the domain, the contact info, all of
that kind of stuff. And then you'll
actually be good to kind of push the
site, deploy it, etc. Anyways, let's
move on to the next one. So, the next
skill I want to have a look at here is
Firecrawl. Now, Firecrawl allows your AI
agent to crawl and scrape the web. While
Claude code by default can access the
web and it can search for things, it
often time will get rate limited,
blocked, have, you know, a CAPTCHA
pop-up or something that it can't pass.
And Firecrawl essentially solves all of
those problems. So, it will just be able
to go and automate the web for you
significantly better than the built-in
features in Claude. It will be able to
bypass any of those security features
that the websites have. So, for example,
you can just scrape all of the HTML
that's on a page, which allows you to
automate more tasks, whatever, crawl
things, and just search more efficiently
than if you were using the built-in
skills in Claude. Now, Firecrawl is free
to use, you get a set number of credits
and you need to pay if you want more.
Now, in my case, I don't use that many,
so I don't need to pay. But, of course,
if you're using it a lot, you will need
to upgrade and buy a few additional
credits. Now, the way that you can set
this up is you can just make a free
account on the site. I'll leave a link
to it in the description. And then, what
you can do is just copy this skill file
right here. So, if you just go to the
main page, there should be a skill file,
and then you can literally just open up
Claude. So, let's go to Claude right
here, and you can say, "Hey, can you add
this skill for me?" And then boom, you
could just paste in the skill, go ahead
and press on enter, and it should
automatically add it for you, and then
it will tell you anything you need to uh
what do you call it here? Set it up,
install, etc. So, you can see if you
actually look up in the skill definition
here that it has this NPX-Y Firecrawl
CLI thing. So, it's actually telling it
how to install it, which it should do
automatically for you. Okay, so it looks
like the skill is added. Now, I'm just
going to go {slash} new just to refresh
the context here, and I'm going to paste
in a prompt just to demonstrate to you
how this works. So, I'm just going to
type {slash} Firecrawl here to initiate
the skill. I'm then going to paste in a
prompt. The prompt that I have is go to
the YC companies directory and crawl
every AI startup page, and then extract
the following. Now, while this might
work with the built-in Claude browser,
Firecrawl is going to do this a lot
faster. It's going to do it at scale,
and it's significantly better at
crawling and scraping and giving you the
data that you actually want. So, if you
want to do something larger, right, like
get every single company, not just a
simple web search or going to one single
page, then that's where this really
comes in and allows you to just more
efficiently and more effectively
actually grab context on the web, which
can be very difficult to do. So,
anyways, I'm going to press enter, and
let's see the result that we get. Okay,
so this just finished. It scraped over
300 different pages, took about 10
minutes to run, and you can see that it
gave me a full markdown file here with
the 20 top companies. Uh it talks about
hiring, founders, what they do. If we
scroll down, we can see the series that
they're in. Um I think it should talks
about fund raising as fund raising as
well. I'm not sure. But, the point is it
did this all directly just from Claude
code without me having to step in. And
in terms of Firecrawl, this used 312
credits. I now have 822 remaining, and I
believe you get 1,000 credits per month
or something for free. So, I didn't have
to pay for this, and I used maybe what,
30% uh in one of these uses for 300
different pages, which well, makes
sense. Anyways, guys, that's Firecrow.
Let's move on to the next one. The next
skill on my list is a very simple one,
and this is just a humanizer skill. Now,
all this does is just make the output
the Claude code gives you sound more
like a human. So, you use this obviously
if you want to write an email, or you're
going to write a response, or you want
to make a social media post, whatever,
so that it doesn't sound like an AI
generated this. Now, setting up this
skill is super basic. There's a Git repo
right here. I'll leave a link to the
description, and if you just go to the
Claude code installation, we can
literally just copy the two lines that
it has right here, and we can just say,
"Hey, can you add this skill? Here is
the
instructions." And just paste it, and it
should just add it automatically for us,
then we can test it out. Okay, so it
says it's installed, and then what I can
do is just use the skill by going
{slash} humanizer, and let's actually
just take this text. Let's copy it and
paste it here and see if it can humanize
it. Nice, and then you can see it gives
us the final rewrite, and it looks a
little bit more human installed. It
looks at this and runs this humanizer.
Put in any text, and it'll flag the
stuff that screams LLM, like m-dash
abuse and recycled words. And notice
that it's using the word stuff, it's
using like lowercases, right? It's
dropped the kind of m-dash that's very
common whenever Claude code is
generating text. And again, super
useful. I use this all of the time.
That's how you add it. Then the next
skill I have for you is one of my
personal favorites. It's not really a
skill, it's more of just kind of like a
tool that you can add that makes Claude
a lot more useful, and that is Composio.
Now, if you work in Claude a lot, you
probably end up connecting a lot of your
different tools. Maybe you connect your
Google Drive, maybe you connect Gmail,
maybe you connect Notion, or Facebook
Ads, or Meta Ads, or whatever. And when
you start adding all of these different
tools, it can actually bloat the context
quite quickly in Claude. So, Claude has
like, you know, 100,000 tokens, which is
representing the 200 different tools
that you've connected. It also means
that sometimes the tools can disconnect.
If you switch over to another machine,
it can be a huge pain to reconnect to
all of them. And Composio you fixes all
of those problems. What you do is you
just connect Composed you to Claude Code
and then inside of Composed you you can
connect all of the individual tools that
you want to use and anytime Claude Code
needs to use one of those tools, rather
than having to have them all listed out
and potentially making a mistake or
viewing hundreds at the same time, it
can just call Composed you, search for
the correct tool and then get the
response back. So not only is this more
token efficient, but also just works a
lot better with higher accuracy because
it's discovering tools on demand and
just connecting them a lot easier rather
than what is it? Having all of them
already kind of loaded, installed and
showing up in the prompt every single
time. So let me show you what I mean. If
I go to Composed you here, I'll leave a
link to it in the description. You want
to go to the for you one by the way cuz
you can also use it to like build AI
agents. So from Composed you if you just
go to the home page here and then you go
to connect apps, you can connect all of
the different apps that you want to use.
So for now let me just connect Gmail for
example. Let's go here, you'll see
there's a whole list of tools and then I
can just connect my accounts and I can
actually connect multiple from this one
page. Okay, so I've just added my Gmail
here. You can see that it's connected.
If I want I can connect multiple which
is also a nice feature of this and then
you can just go through and connect
literally thousands of different
applications from one page so that you
don't need to have a building connector
skill whatever in Claude. You can just
connect anything directly from here.
Then what you're going to do once you
connect everything is just go to
install. From install you can go to
either Claude Co-work, Claude Code,
whatever. I'm going to go to Claude Code
and then I'm literally just going to
copy this prompt that it has here. It
also has my user API key and I'm just
going to paste this here and say, "Hey,
can you add this to my MCP config or can
you add this skill or whatever?" And
here I'm just going to paste this and it
should automatically add it for me and I
guess yeah, it's going to use kind of
the terminal CLI or whatever to connect
this. Now one thing to note here when
you're using Composed you is that this
is free to use. However, I think you get
like 20,000 tool calls per month and
then if you go over that you will need
to pay. I've never gotten anywhere close
to that. Um, and I guess if you're using
it super heavily, then it's like 20
bucks a month or something, but anyways,
don't worry, it's quite free to use, I
would say, compared to a lot of the
other tools. So, let's wait for this to
finish and let's see if it works. Okay,
so it finished installing now. I'm just
going to make a new session and then
you'll see that if I actually go Compose
your CLI, this is now a skill that's
added to Claude Code. So, let me use the
Compose your CLI tool here and then I'm
just going to say something like, "Grab
my three most recent emails, but don't
expose any sensitive and just give me a
summary of what they are."
Okay, and it should be able to use this
now. If it doesn't, just make sure you
have Compose your added to path. You can
just tell, uh, what is it, Claude Code
to do that. You can see now it's going
to use Compose your to execute this tool
call and it should give me the result.
And this again is much more token
efficient than having all of the tools
loaded in at once because what will
happen is it will execute it, it will
get the result, and then what will
happen is the result will come back
actually already parsed, so we don't get
all of this random data that Claude Code
needs to run through. And you can see
the boom, we get the three emails here,
um, giving us kind of a summary of what
they are and that is actually what is in
my email. Okay, that is Compose Of
course, this becomes a lot more useful
when you add more tools to it. I'm just
using a demo workspace for here, but in
my real Compose I have like 50 different
tools connected and it works extremely
well and I use it inside pretty much all
of my AI tools because then once you
connect the tools here, you can just go
and you can connect this to any tool and
you don't need to reconnect all of the
different tools here. You just go to
Codex, you do the same configuration we
just did for Claude, and now all of the
stuff you've connected is just connected
in Codex. I got a new machine, boom,
install it there. All of my connections
exist, which is why I like this. But
let's move to the last skill. So, the
last skill on my list here is the Vibe
Sec Skill. Now, what this says is, "Stop
vibe coding vulnerabilities into
production." And essentially what this
is is a skill that will look for any
vulnerabilities, any security issues in
the applications that you build. So, you
should run this skill before you deploy
something to production to do kind of a
full audit of your code base and make
sure that everything is secure and that
you don't leak an API key or have
unauthenticated access to your data or
something like that. So, in terms of
installing it, I'll leave a link to the
repo in the description. Like always,
I'm super lazy, so I'm just going to
literally copy the instructions that it
has for Claude code and I'm just going
to go here and paste this and say, "Can
you please add this to my Claude code
skills?" And we'll just let it
automatically run and add it for us.
Okay, so just added the skill right here
and just said I need to restart Claude
code. Now again, I'm inside of my Tim
accounting application, which is
actually deployed right now. So, what
I'm going to do is just run the skill,
Vibe Sec skill, and let's see what we
get for this repo. Now, the idea behind
this skill is that it's going to be used
while you're building the app. So, while
you can use it to audit the app, which
is what I'm doing right now, you should
install it before you start building and
then it's kind of teaching Claude code
how to actually think through all of the
vulnerabilities and not make the mistake
in the first place. So, in my case, I
didn't have this skill before. So, now
you can see it's going to go through and
have all of these steps, which is
probably going to take a few minutes to
run. But, the point is once you add it,
then you should just get more secure
applications. Of course, you still want
to review the code, but generally it's a
really simple thing to add to reduce a
lot of the risk that you might have when
you're Vibe coding apps. Okay, so you
can see there is a lot of
vulnerabilities here that it detected in
my application. So, it's going to go
ahead and fix them now automatically for
me. But, again, good thing I ran this
because I actually had this app deployed
and there's all kinds of issues that I
just didn't notice because I was
literally just Vibe coding this. So,
that is Vibe Sec, great skill to add and
definitely something you need in the
Vibe coding era. So, anyways, guys, with
that said, that's going to wrap up this
video. Those are the six skills that I
personally found the most useful. Of
course, there are hundreds of other ones
that are also very useful to add in
Claude code, but I guarantee one of
these, you know, will make sense in your
workflow and that you should probably
consider adding. Let me know if you
enjoyed this video. If you did, make
sure to leave a like, subscribe, and I
will see you in [music] the next one.

## Source

- Type: article
- URL: n/a
- Author: Tech With Tim
- Published: n/a
