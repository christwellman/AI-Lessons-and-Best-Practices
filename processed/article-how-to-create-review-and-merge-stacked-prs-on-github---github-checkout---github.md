---
id: "article_0510ce1d"
title: "How to create, review, and merge stacked PRs on GitHub | GitHub Checkout"
source_type: "article"
source_url: ""
author: "GitHub"
published: ""
ingested: "2026-08-23"
category: "tools"
tags: [github, stacked-prs, cli, version-control]
summary: "GitHub introduces stacked pull requests to help developers break large features into smaller reviewable parts. Developers can manage stacks using the web user interface or the new command line extension. Multiple pull requests in a stack merge into the main branch with a single click."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

GitHub introduces stacked pull requests to help developers break large features into smaller reviewable parts. Developers can manage stacks using the web user interface or the new command line extension. Multiple pull requests in a stack merge into the main branch with a single click.

## Key Takeaways

- Stacked pull requests allow developers to split large features into smaller connected changes.
- Developers can install the stack extension with the GitHub command line tool.
- Each pull request in a stack can have a different code owner for review.
- Developers can merge an entire stack of pull requests with one click.
- GitHub Copilot can add new branches and make changes within specific layers of a stack.

## Techniques / Prompts Extracted

- GH extension install github/gh-stack
- GH stack
- GH stack add
- checkout
- GH stack submit

## Full Content

# How to create, review, and merge stacked PRs on GitHub | GitHub Checkout

**Author:** GitHub

## Transcript

What's really cool about stacked PRs
that it pushes all of those changes at
once and just again makes it really easy
for you to land your entire stack in one
click.
>> Stacked PRs are here. This has been one
of the most requested workflows for
ages. Take a big change and break it
apart into smaller PRs that build on
each other. Today, I'm joined by Sameen
Karim, senior product manager for the
stacked PRs team, and he's going to show
you how to use it. Welcome, Sameen.
>> Really excited to show you all about
GitHub stacked PRs. Makes it a lot
easier to take your large changes, break
them into small reviewable pull requests
that you can land faster.
>> Amazing. Well, let's get into it.
>> The way stacked PRs works is that you
have your pull requests as you know and
love them in GitHub today, but now you
can group them together into a stack.
So, for example, if I have a large
feature that I'm working on and I have
my database changes, my API endpoints,
my front-end code, what I can do is I
can very easily split that up into a
series of PRs that are stacked on top of
each other. Uh and what's really great
is that instead of having uh sort of one
giant PR where all of this code can be
difficult to review, requires multiple
code owners to comment on, you can have
these very focused PRs that have again
just that specific set of changes. And
for example, if my database changes are
approved and ready to go, I can go ahead
and merge those while I'm still waiting
for the front-end team to approve my
other changes. It makes it really easy
to review large sets of code, but also
makes it really easy for you to ship
your features uh piece by piece as soon
as they're ready.
>> So, you mentioned that we can get create
stacks from the UI, so from github.com,
but then also now we have this CLI that
we can use with GH. And for folks who
maybe haven't installed GH yet or are in
an older version, can you walk us
through what we need to do to be able to
use the CLI on our terminals?
>> Installing the stack extension is really
straightforward. So, uh GH stack is just
an extension on top of the existing GH
CLI. So, all you need to do is go into
your terminal and type in GH extension
install github/gh-stack.
But, for people who are on the most
recent versions, they should just be
able to type in GH stack and it will
sort of
automatically
start the process.
>> I can still go through the same flow I
do when I open up pull requests, right?
So, what's the difference? And like,
you're going to start the request from
the CLI now or how are you kicking off
the stack process?
>> So, the great thing about stacks is that
you can use the CLI that we're shipping
called GH stack, but you can also go
ahead and just create PRs, stack PRs via
the UI as well. So, to start a a stack
from the CLI, all you have to do is go
ahead and initialize your stack. I can
go ahead and start naming my branches.
And I've started working on my stack and
I can go ahead and for example, make the
changes that I would like to do.
And then uh commit my changes.
And then
as soon as I'm ready to start working on
the next layer of my stack, I can simply
do GH stack add.
Start working on that and then, you
know, rinse and repeat. Continue to work
on the additional changes. And what's
great here is as you're continuing to
work on the stack, you can continue to
build it. So, I'm going to go ahead and
switch to another stack that I was
working on previously.
>> And you're switching the stacks by the
name the branch that it was it was
given?
>> Yes, exactly. So, you can switch stacks
both by the branch name, but you can
also actually just simply type in
checkout and here you can get a list of
all of the stacks that you have locally.
As you can see, I've been doing a lot of
testing. There's a lot of things that we
I have I've got going on here,
but I can easily sort of search and then
use that to switch to the stack that I
want to use. So, now once you're in the
stack, one of the great things that you
can do is you can very easily see
all the branches that you're working
with in your stack,
and you can even pop open this nice
little TUI where you can even use your
mouse clicks to see all of the files
changed, all of the branches and commits
between all of the the branches and PRs
in your stack. So, let's say I have a
stack that I'm already working on here.
I've got my database changes, my API
endpoints, and my front-end code. And
one of the reviewers has said that, you
know, I'm missing a unit test. So, I
really should be working on that. So,
you know, it's not a blocking change,
but I definitely should go ahead and do
that. So, let me go ahead and ask
Copilot, "Hey, can you go ahead and
write some tests for me and create it as
a new branch at the top of the stack?"
And what's great is that Copilot
knows exactly how to work with stacked
PRs. So, it'll be able to understand all
the operations and run all the commands
to be able to not only add branches to
my stack, but as I make changes, for
example, if I asked it to make changes
with the API, it will know to switch to
the API branch, make the changes there.
So, to keep again all your changes kind
of self-contained within each of the
layers of the stack. When you're again
trying to
ship these really large changes that
would have required multiple PRs or been
very difficult to review, it's a lot
easier with stacked PRs. And one of the
big pieces of feedback that people have
really liked is that with stacked PRs,
you can have
again a group of PRs where each PR has
its own code owner. So, for example,
your database changes can be approved by
the database team, the front-end team
can be the code owner approval for the
front-end changes, and it makes it a lot
easier to go through code review. All
right, looks like Copilot is done. It's
created my new branch, so I can go ahead
and now look at
what it has created.
And I can see here that there's a new
test branch. And what I'll also see is
that when I go ahead and view this
stack,
there is no PR yet open for this new
branch. So, I'm ready to go ahead and
submit a PR. So, I can just go ahead and
run GH stack submit. And as I do that,
you'll see the screen that'll pop up
that will then allow us to customize the
title of the PR, the description,
and if you have a PR template, for
example, it will pull that in here. But
right now I'll just go ahead and and
sort of stick with this default template
that I have. I can decide whether I want
to publish it as ready or draft. And
then I can go ahead and click submit.
So, now if I go into GitHub,
you'll be able to see is I can go ahead
and open this PR.
And now you'll see that my stack that
previously had three pull requests now
has four pull requests.
And
I'm just waiting for my tests to finish.
Looks like they just finished. And if,
you know, I needed approvals for any of
my reviewers,
I would have seen those requirements
here, but it looks like in this case all
the PRs are ready to go. All my CI is
passing, and it's ready for the magic
moment when we want to merge all of
these pull requests. And this is one of
the truly most exciting parts about
stacks in my opinion, which is that you
can merge multiple pull requests at
once. In this case, I've got four pull
requests. I can choose whichever merge
method I want. I personally love squash
merge. Uh so, if we go ahead and click
squash merge right here, it's going to
go ahead and merge all four of those
PRs, where each PR is going to be one
squashed commit on my main branch. So,
now I've merged all of my PRs, and
what's great is I can go into main now,
and there I will see that each of those
PRs have landed as a squashed commit all
at the exact same time on my main
branch. What's really cool about stacked
PRs is that it pushes all of those
changes at once, and just again, makes
it really easy for you to land your
entire stack in one click.
>> I cannot wait to continue to try it and
keep experimenting with it.
Uh where can people give you feedback
about stacked PRs and their experience
with it?
>> Yeah, absolutely. We have a discussion
post that's all linked to the change log
for this release, so definitely feel
free to hop in there and give us any
feedback. And I'm also available on X or
Twitter. Uh my handle is @SamirKarim.
Uh please, would love any feedback.
We're looking to continue to improve
this. There's a lot more we have in
store for stacked PRs. So, would love to
hear all of your feedback, and we love
building with the community.
>> Samir, before you go, can you give us a
little bit of a, I guess, teaser of
what's next for stacked PRs?
>> Oh, yes, absolutely. So, we've got a
number of exciting things coming up for
stacked PRs. There's a lot more
improvements we're continuing to make to
the stack CLI, so, you know, expect to
see a lot more improvements there. We're
going to be introducing support for
forks, so for open-source contributors,
one of the things that we're going to be
introducing is for contributors to be
able to create stacks of PRs for their
contributions as they have a fork repo
into the the main repo. And we're also
just overall redesigning the entire PR
experience actually. So, we have a
couple things that you already can see
here that are make it easy for you to
navigate your stack. We are really
investing in making it as easy as
possible for you to review your stack of
changes, see all of your your comments,
the discussion, checks, diff, everything
all in one place. So, it's not really
just stacks, but the entire PR
experience that is going to be getting a
lot of love and we can't wait to show
you guys what we have in store.
>> Thanks so much for coming by Sameer and
showing us the new stack PRs. I can't
wait to see what's next.
>> Awesome. Thank you for having me.
>> And that was your first look at GitHub
stack PRs.
Please let me know in the comments, have
you been waiting for this feature? Are
you going to try it? Don't forget to
like and subscribe. Push those changes
to main and I'll catch you on the next
release.

## Source

- Type: article
- URL: n/a
- Author: GitHub
- Published: n/a
