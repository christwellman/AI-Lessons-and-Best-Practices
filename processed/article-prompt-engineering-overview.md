---
id: "article_798e452e"
title: "Prompt engineering overview"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "prompts"
tags: [prompt-engineering, best-practices, claude-models]
summary: "This document gives an overview of prompt engineering methods for Claude models. You must define success criteria and test prompts before you start. Use the listed techniques in order when you troubleshoot model performance."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

This document gives an overview of prompt engineering methods for Claude models. You must define success criteria and test prompts before you start. Use the listed techniques in order when you troubleshoot model performance.

## Key Takeaways

- Define clear success criteria before you start prompt engineering.
- Create empirical evaluations to test your prompts.
- Use a prompt generator if you do not have a first draft prompt.
- Select different models to improve latency or cost instead of prompt engineering.
- Try prompt engineering techniques in order from most broadly effective to specialized.

## Techniques / Prompts Extracted

None identified.

## Full Content

# Prompt engineering overview
---
Date: May 13, 2025
Tags: #Prompts
Summary:
Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=e07005ceab3c223cd9d7bf3e36b36090e0deb689

---
While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips).

##

[​

](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=e07005ceab3c223cd9d7bf3e36b36090e0deb689#before-prompt-engineering)

Before prompt engineering

This guide assumes that you have:

1. A clear definition of the success criteria for your use case
2. Some ways to empirically test against those criteria
3. A first draft prompt you want to improve

If not, we highly suggest you spend time establishing that first. Check out [Define your success criteria](https://docs.anthropic.com/en/docs/build-with-claude/define-success) and [Create strong empirical evaluations](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests) for tips and guidance.

[

## Prompt generator

Don’t have a first draft prompt? Try the prompt generator in the Anthropic Console!

](https://console.anthropic.com/dashboard)

---

##

[​

](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=e07005ceab3c223cd9d7bf3e36b36090e0deb689#when-to-prompt-engineer)

When to prompt engineer

This guide focuses on success criteria that are controllable through prompt engineering. Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model.

Prompting vs. finetuning

---

##

[​

](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=e07005ceab3c223cd9d7bf3e36b36090e0deb689#how-to-prompt-engineer)

How to prompt engineer

The prompt engineering pages in this section have been organized from most broadly effective techniques to more specialized techniques. When troubleshooting performance, we suggest you try these techniques in order, although the actual impact of each technique will depend on your use case.

1. [Prompt generator](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator)
2. [Be clear and direct](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)
3. [Use examples (multishot)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
4. [Let Claude think (chain of thought)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
5. [Use XML tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
6. [Give Claude a role (system prompts)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
7. [Prefill Claude’s response](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response)
8. [Chain complex prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts)
9. [Long context tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips)

---

##

[​

](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-prompting-secrets-exposed&_bhlid=e07005ceab3c223cd9d7bf3e36b36090e0deb689#prompt-engineering-tutorial)

Prompt engineering tutorial

If you’re an interactive learner, you can dive into our interactive tutorials instead!

[

## GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.

](https://github.com/anthropics/prompt-eng-interactive-tutorial)[

## Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.

](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
