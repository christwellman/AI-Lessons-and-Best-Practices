---
id: "article_d82c4914"
title: "Prompt Engineering"
source_type: "article"
source_url: ""
author: ""
published: ""
ingested: "2026-08-23"
category: "techniques"
tags: [prompt-engineering, best-practices, llm-optimization, academic-research]
summary: "Recent academic studies show new rules for prompt engineering. Users must avoid tag questions and step-by-step instructions. Users must limit rules to three maximum and focus on clear goals instead of examples."
ste100_status: "simplified"
ste100_model: "gemini-3.5-flash-lite"
---

## Summary

Recent academic studies show new rules for prompt engineering. Users must avoid tag questions and step-by-step instructions. Users must limit rules to three maximum and focus on clear goals instead of examples.

## Key Takeaways

- Keep prompts neutral and avoid yes/no questions.
- Role prompts perform better than step-by-step instructions.
- Models cannot follow more than three rules reliably at once.
- Clear goals outperform few-shot examples on modern models.

## Techniques / Prompts Extracted

- “[X] is the better choice, maybe?”
- “. . . as a reliability engineer.”
- "Write a LinkedIn post about our launch. Must include: \"AI-native\", \"workflow\", \"ship\". No emojis. End with a question."
- "Check your draft against each of these requirements ONE AT A TIME, then revise: 3 paragraphs, under 150 words, grade-6 reading level, no competitor mentions."
- "Ask me for the data you need before you answer."

## Full Content

Forwarded this email? Subscribe here for more
Prompt Engineering 101.
The science behind prompt engineering.
Ruben Hassid
Aug 19
∙
Preview

READ IN APP

There is no training on how to ask AI correctly.

And AI changes so fast that techniques from before don’t work anymore. LLMs (like ChatGPT or Claude) changed so much it’s outdated.

For example, I used to tell everyone to add “Take a deep breath and work on this step by step” to their prompt. Because science said so:

“Large Language Models as Optimizers” (also known as the OPRO paper)
But this paper is from September 2023 and talks about the model PaLM 2-L from Google. You now have access to Claude & ChatGPT models that are 10x more capable.

So how can you truly know how to prompt the latest models?

You need to read new and trusted academic papers on prompt engineering. Hundreds of them. Per day.

If you’re interested in the science behind AI, go to arxiv.org/list/cs.AI/recent.
But you must be crazy to read 100+ new AI papers every day.

Well, I am crazy.

By the end of this newsletter, you will know what the science says about better prompts (in simple English, I promise; no weird Claud-isms), in this order:

Never end your prompt with “right?”.

Forget about the “step by step”.

Do not trust confidence.

Stick to 3 rules max.

Goals > Examples.

Sounds like a good deal? Cool.

Two things before we start:

Save this guide. It’s long, so block 15 min on your calendar.

Send it to anyone who is searching for better prompts.

Share

This newsletter grows from your shares. It’s my weekly north star.

1. Never end with “right?”.

Tag Questions — Cornell Tech | Tapan Parikh, 27 Jul 2026
A Cornell Tech researcher tested 45 different AIs with one-word changes.

“[X] is the better choice, right?” → new models disagree with you.

“[X] is the better choice, maybe?” → all 45 models agree with you more.

So asking the AI’s opinion is most definitely not a good idea: it will be biased by how you ask the question more than by its actual intuition.

Bad prompt:

“I’m deciding what to do about housing.

Buying is the better choice, maybe?”

Good prompt:

“I’m deciding what to do about housing.

Compare buying and renting for my situation.”

Just like when you ask a friend, don’t make them answer the way you want them to answer. Keep it neutral. Avoid yes/no questions.

Upgrade to paid
2. Forget the “step-by-step”.
Ranking of 8 prompting techniques: role prompts on top, chain-of-thought near the bottom
The Simplicity Paradox — IBM Research | Preet, Lin & Patel, 7 May 2026
IBM ran an impressive 430,738 evaluations on 8 prompting techniques.

The most famous “Let’s think step by step” LOST to asking normally.

The winning combo is just your question + your role in a few words (“…as a reliability engineer”).

Bad prompt:

“[Your question]

Gather information, devise a plan, answer step by step.”

Good prompt:

“[Your question]

. . . as a reliability engineer.”

Worth noting. The paper used the role "reliability engineer" for every topic it tested: medicine, physics, and math. So is it the only role you should prompt, or does choosing a good role make your prompt better?

Maybe I should start writing academic papers…

Share

3. Do not trust confidence.
Affected-paper rate rising 1.9x since ChatGPT; one paper had 20 hallucinated references
Phantom References — Microsoft | Mark Russinovich (CTO, Microsoft Azure), Siva Kumar, Salem. 1 Jul 2026
Microsoft’s CTO audited 2.6 million references (papers) at the world’s top AI conferences.

1 in 4 ‘NeurIPS’ 2025 papers — papers that PASSED expert peer review — has a hallucinated citation. The reviewers missed it, and they even scored the papers slightly HIGHER.

If professional reviewers can’t catch AI-hallucinated papers, you won’t either. You must open every link:

Now the real question is who in their right mind will open 210 sources.

I feel the same as you. I wish to trust AI research more.

Upgrade to paid
4. Stick to 3 rules max.
Two diverging curves: per-rule success sags gently while all-rules success collapses; 35pp gap at k=8
Not Many at Once — Meta Superintelligence Labs | Mariya Vasileva, 14 August 2026
Meta tested GPT-5.5, Claude Opus, Gemini Pro and 12 others AI on prompts with 1 to 12 rules. An example of 3 rules would be:

Exactly 3 paragraphs. Under 150 words. No emojis.

At 8 rules, models only get each individual rule right 41% of the time. But it only gets 8 rules at once 5.7% of the time… Not good.

12 of the 15 models can’t reliably hold more than 3 rules.

Bad prompt:

Write a LinkedIn post about our launch. Exactly 3 paragraphs. Under 150 words. No emojis. Include “AI-native”, “workflow” and “ship”. Don’t mention competitors. End with a question. Grade-6 reading level. Match my voice sample below.

Good prompt:

First run: Write a LinkedIn post about our launch. Must include: "AI-native", "workflow", "ship". No emojis. End with a question.

Second run (after the draft): Check your draft against each of these requirements ONE AT A TIME, then revise: 3 paragraphs, under 150 words, grade-6 reading level, no competitor mentions.

The more I learn about prompt engineering, the more I understand it’s all about giving the right goal. A clear one. It’s far more effective than giving examples:

Share

Sharing is caring. And it’s free.

5. Goals > Examples.
Accuracy grid: every few-shot configuration in the low 70s, zero-shot in the mid 80s
Soft Guidance Beats Your Examples — EPFL + Apple + Mistral AI | Pushkin, Jiang, Lotfi, Sandon, Abbé, 4 Aug 2026
Researchers found examples in your prompt are sabotaging modern models.

Mistral’s model scored 74% with the standard examples prompt. They deleted the examples, and then boom → 83.8% score.

Bad prompt:

You are a world-class newsletter strategist.

Example 1: [a solved case, written out]

Example 2: [a solved case, written out]

Find a plan, and answer step by step: How can I improve my newsletter?

Good prompt:

My newsletter open rate fell from [X]% to [Y]% over three months.

I send one issue every Tuesday. I did not change the format, the send time, or the subject. What are the most likely causes?

Ask me for the data you need before you answer.

Specifying a goal is the ultimate key to a good prompt.

6. The One Prompt
I made a prompt template that covers everything we just covered.

I will then show you how to create a quick keyboard shortcut (because you don’t want to copy & paste it every time you need it).

So first, copy and paste this prompt:...

## Source

- Type: article
- URL: n/a
- Author: n/a
- Published: n/a
