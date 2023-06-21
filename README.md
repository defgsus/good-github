## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-20](docs/good-messages/2023/2023-06-20.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,148,078 were push events containing 3,520,966 commit messages that amount to 300,082,192 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [EvaEvaEvaEvaEva/shaptest](https://github.com/EvaEvaEvaEvaEva/shaptest)@[8744738e59...](https://github.com/EvaEvaEvaEvaEva/shaptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Tuesday 2023-06-20 00:11:06 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [larryv/termcwd-vim](https://github.com/larryv/termcwd-vim)@[a91cda2a02...](https://github.com/larryv/termcwd-vim/commit/a91cda2a02c77e4399b589dee5f6f0a1ae87b111)
#### Tuesday 2023-06-20 00:30:21 by Lawrence Velázquez

Convert indentation from spaces to tabs

I've long favored four-space indentation but find Matt Wilcox's pro-tab
counterargument [1][2] compelling, if needlessly condescending:

    This is your occasional reminder:
    Tabs are what should be used for indentation.

    Why?  Because spaces for indentation are:

    - Harder for people using assistive technology
    - Harder for people with reading comprehension issues who want more
      indentation.

    The tab is *user customisable* to be any level of indentation per
    tab character.  It is the semantically correct character.

    Please; use tab characters in any public code.  If you don't like
    how "deep" they are; adjust your editor's rendering.

    (If you are already cringing or railing against this idea because it
    would look weird to you... have a deep think.  A real deep think.)

    Spaces as indentation are self-centred and selfish.  They enforce
    *your* preference on others, when tabs would allow you *and others*
    their own preference of indentation for the same code - because they
    are user configurable.

    Yes, all editors can configure the tab to render as 1, 2, 4, 6, 8 or
    any number of spaces wide.  Learn your editor.

I've always prioritized my aesthetic preferences, deeming indentation of
two columns to be too shallow and eight, too deep.  I know tab stops are
widely configurable, but I stubbornly insist on viewing tabs at their
"natural" width of eight columns because I want to see them as everyone
else does.  (Who actually changes their tab stops?  Come on.)  Thus, the
only way to get al dente indentation that looks the same to everyone is
to use four spaces.

I've thought about switching to tabs before.  The Linux kernel coding
style guide espouses 8-column indentation on the grounds that it's very
clear and highlights excessively deep nesting [3] -- interesting ideas,
but not so interesting that I'd switch teams.

Well, Wilcox's accessibility angle has convinced me, although I still
think 8 columns is a bit much.  I'll get over it.

Reindent Vim source using tabs.  Do not reindent prose because it looks
awful, and I can't bring myself to do it (code is already ugly, so it's
easier to swallow).

  [1]: https://mstdn.social/@mattwilcox/110451855256437660
  [2]: https://mstdn.social/@mattwilcox/110451875354616267
  [3]: https://www.kernel.org/doc/html/latest/process/coding-style.html#indentation

---
## [aramcheck/evals](https://github.com/aramcheck/evals)@[aeeb452867...](https://github.com/aramcheck/evals/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Tuesday 2023-06-20 00:35:14 by Alexander Raul

Algebra word problems (#36)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Algebra Word Problems (algebra_word_problems)

### Eval description

This eval contains some algebra word problems that tend to make gpt 3.5
hallucinate, but wouldn't be out of place on a grade school exam.
Currently has less than 100 examples, but will add if folks think this
is a good eval path to go down.

### What makes this a useful eval?

Poor performance on GPT 3.5 for one, but also would be a great test of
increased logical reasoning capabilities of GPT-4 per the release blog
post.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in
their first 100 JSONL eval lines.

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If it takes 5 machines 5
minutes to make 5 devices, how long would it take 100 machines to make
100 devices?"}], "ideal": "5"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "What is the sum of 60000,
5000, 400, and 3, with the third value multiplied by 5 before performing
the operation?"}], "ideal": "67003"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If the sum of the smallest
and largest of three consecutive even numbers is 28, what is the value
of the second largest number in the series?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "John is trying to fill a 16
oz. bottle with water. If John fills the bottle at 1 oz per second and
the bottle leaks .2 oz per second, how long would it take for John to
fill the bottle?"}], "ideal": "20"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "Annie is training for a
marathon. She has a weekly training routine, training for five hours a
day on some days and 3 hours a day on the other days. She trains a total
of 27 hours in a seven day week. On how many days does she train for
five hours?"}], "ideal": "3"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "At the start of the year the
ratio of boys to girls in a class is 2 : 1. But now, half a year later,
four boys have left the class and there are two new girls. The ratio of
boys to girls is now 4 : 3. How many students are there altogether
now?"}], "ideal": "28"}
  ```
</details>

---
## [aramcheck/evals](https://github.com/aramcheck/evals)@[bf2ebb9dd6...](https://github.com/aramcheck/evals/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Tuesday 2023-06-20 00:35:14 by Amir DIB

[evals] emoji riddle eval 🎨🤔 (#510)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
**Emoji riddle**

### Eval description

The evaluation involves solving riddles made up of emojis. The
inspiration for this idea came from reading LinkedIn posts, where I
noticed that nearly 1-4% of the textual information was conveyed through
emojis. Nowadays, emojis are widely used to format text and introduce
color contrasts in texts, even by community managers of large companies.
Furthermore, using emojis is seen as a less formal way of communication
and gives a tone more suitable for social media.


### What makes this a useful eval?

- **Conversational understanding**. the eval test the ability to link
different concepts together which is a crucial feature.

- **Communication**. As GPT is deployed in settings where informal
language is used, interpreting emojis in context will likely become
critical. I think that improvement on this emoji riddle task would make
GPT better at mimicking human-like communication, as it would be able to
understand and respond to various forms of expressions involving emojis.
Emojis and their combinations often carry cultural and social meanings.
By being adept at emoji riddles, ChatGPT would showcase an understanding
of cultural nuances and be more relatable to users.

- **problem-solving**: Emoji riddle solving requires i) extracting
possible meanings and ii) finding the more suitable association of
meaning in the given context (cultural, plateform, etc).

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value


## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"👀 + 🪚 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["seesaw"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"❤️ + ✉️ = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["love letter"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":" ⌚️ + 🐶 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["watchdog"]}
  ```
</details>

**The Dataset**

![image](https://user-images.githubusercontent.com/22154031/228633727-14480364-4009-45c1-8398-276de7bd86a9.png)

---
## [aramcheck/evals](https://github.com/aramcheck/evals)@[38f40050e9...](https://github.com/aramcheck/evals/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Tuesday 2023-06-20 00:35:14 by dz-pika

Utility charge eval (#735)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Utility charge eval 

### Eval description
Given snippets from an electric utility bill, compute the per-kWh price
for electricity supply and delivery.

### What makes this a useful eval?
Utility bill parsing is needed to understand the breakdown of charges
and forecast future bills based on predicted usage. However, electricity
bills can be complex, with dozens of different line items that
contribute to the overall cost. This can be a headache for people
looking at their bill, as they just want to understand the per-kWh
prices for the supply/generation or delivery (e.g. transmission &
distribution) of their energy. Given incomplete but sufficient
information (e.g. simulating running OCR on a utility bill), this task
requires both the understanding and grouping of different terms and
charges under the delivery or supply, and basic arithmetic to compute
the total kWh and total charges in order to determine the per-kWh
prices. A human could fairly easily interpret the given data, but we
find that GPT3.5 (as well as GPT4 via the ChatGPT Plus) perform much
less accurately on the task (~.2).

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

All of the examples contain dummy values, but come from
terminology/formatting used in bills from many different utilities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nBasic Generation Service: 121
kWh X $0.069 per kWh = 8.35 \n Total Electric Supply Charges = 30.23 \n
Distribution Charge: 121 kWh X $0.041 per kWh = 4.96 \n Total Electric
Delivery Charges = 20.43"}], "ideal": "{'supply_cost_per_kwh': '0.25',
'delivery_cost_per_kwh': '0.17'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nGeneration Service (Supply) =
$34.89 \n Transmission Service = 7.24 \n Distribution Service = 4.96 \n
Meter Usage: 568 kWh"}], "ideal": "{'supply_cost_per_kwh': '0.061',
'delivery_cost_per_kwh': '0.022'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nElectricity Used (kWh) = 762 \n
Electricity Supply Charges 762 kWh at a cost of $100.25 \n Delivery
Service Charge: 762 kWh @ 0.008 = 6.096 \n Total Electric Delivery
Charges = 59.36"}], "ideal": "{'supply_cost_per_kwh': '0.13',
'delivery_cost_per_kwh': '0.078'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nSupply 423 kWh @ 11 cents / kWh
= 46.53 \n Total electricity supply charges $68.21 \n Delivery 423 kWh @
4 cents / kWh = 16.92 \n Total electricity delivery charges $17.43"}],
"ideal": "{'supply_cost_per_kwh': '0.16', 'delivery_cost_per_kwh':
'0.041'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nEnergy 152 @ 0.069 = 10.49 \n
Total Energy Charges = 14.25 \n Distribution 152 @ 0.041 = 6.23 \n Total
Electric Delivery Charges = 6.99"}], "ideal": "{'supply_cost_per_kwh':
'0.094', 'delivery_cost_per_kwh': '0.046'}"}
  ```
</details>

---
## [aramcheck/evals](https://github.com/aramcheck/evals)@[b2250e4117...](https://github.com/aramcheck/evals/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Tuesday 2023-06-20 00:35:14 by shivamd1810

Add General science reasoning: UPSC GS eval. (#641)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Hindi UPSC

### Eval description

[UPSC](https://en.wikipedia.org/wiki/Union_Public_Service_Commission) is
the organization responsible for conducting administrative service exams
in India. This evaluation set focuses on questions from the general
science paper of UPSC exams in Hindi. As a widely spoken language in
India, it is crucial to understand and answer questions accurately in
Hindi.



### What makes this a useful eval?

This evaluation set is useful for several reasons:

1. Real-world applicability: The questions are sourced from actual UPSC
exams, making the evaluation set practical and relevant for users
preparing for these exams.
2. Language diversity: By focusing on Hindi, this evaluation set helps
to improve the AI's understanding and response generation in a
non-English language, catering to a large user base.
3. Subject matter: General science is an important topic covered in the
UPSC exams, and evaluating the AI's performance in this area will help
identify areas for improvement.
4. Logical reasoning and inference: **UPSC questions are known for
requiring logical reasoning and the ability to infer connections between
multiple topics**. By including questions that demand such skills, this
evaluation set will help test and improve the AI's ability to handle
complex, multi-layered problems.


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This evaluation set is valuable for improving the AI's understanding of
Hindi and its ability to provide accurate answers to general science
questions in the context of UPSC exams, a widely recognized and
important examination in India. Moreover, by incorporating questions
that test logical reasoning and inference skills, it will help enhance
the AI's capability to handle complex, multi-faceted problems that
require connections between multiple topics.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "\n1. भारत की संसद के संदर्भ
में, निम्नलिखित कथनों पर विचार कीजिए:\n\n1- गैर-सरकारी विधेयक ऐसा विधेयक
है जो संसद् के ऐसे सदस्य द्वारा प्रस्तुत किया जाता है जो निर्वाचित नहीं
है किंतु भारत के राष्ट्रपति द्वारा नामनिर्दिष्ट है।\n2- हाल ही में, भारत
की संसद के इतिहास में पहली बार एक गैर-सरकारी विधेयक पारित किया गया
है।\n\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?\n\n(a) केवल 1\n(b)
केवल 2\n(c) 1 और 2 दोनों\n(d) न तो 1 और न ही 2\n\n, choose correct
answer:"}], "ideal": "d"}
{"input": [{"role": "system", "content": "2. ऋग्वेद-कालीन आर्यों और
सिन्धु घाटी के लोगों की संस्कृति के बीच अंतर के संबंध में, निम्नलिखित
कथनों में से कौन-सा/से सही है/हैं?\n1- ऋग्वेद-कालीन आर्य कवच और
शिरस्त्रण (हेलमेट) का उपयोग करते थे जबकि सिन्धु घाटी सभ्यता के लोगों में
इनके उपयोग का कोई साध्य नहीं मिलता।\n2- ऋग्वेद-कालीन आर्यों को स्वर्ण,
चाँदी और ताम्र का ज्ञान था जबकि सिन्धु घाटी के लोगों को कवल ताम्र और लोह
का ज्ञान था।\n3- ऋग्वेद-कालीन आर्यों ने घोड़े को पालतू बना लिया था जबकि
इस बात का कोई साक्ष्य नहीं है कि सिन्धु घाअी के लोग इस पशु को जानते
थे।\n\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिएः\n\n(a) केवल 1\n(b)
केवल 2 और 3\n(c) केवल 1 और 3\n(d) 1, 2 और 3\n\n, choose correct
answer:"}], "ideal": "c"}
{"input": [{"role": "system", "content": "3. ‘पूर्व अधिगम की मान्यता
स्कीम (रिकग्निशन ऑफ प्रायर लर्निंग स्कीम)’ का कभी-कभी समाचारों में किस
संदर्भ में उल्लेख किया जाता है?\n(a) निर्माण कार्य में लगे कर्मकारों के
पारंपरिक मार्गों से अर्जित कौशल का प्रमाणन\n(b) दूरस्थ अधिगम कार्यक्रमों
के लिए विश्वविद्यालयों में व्यक्तियों को पंजीकृत करना\n(c) सार्वजनिक
क्षेत्र के कुछ उपक्रमों में ग्रामीण और नगरीय निर्धन लोगों के लिए कुछ
कुशल कार्य आरक्षित करना\n(d) राष्ट्रीय कौशल विकास कार्यक्रम के अधीन
प्रशिक्षणार्थियों द्वारा अर्जित कौशल का प्रमाणन\n\n, choose correct
answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "4. पारिस्थितिक दृष्टिकोण से,
पूर्वी घाटों और पश्चिमी घाटों के बीच एक अच्छा सम्पर्क होने के रूप में
निम्नलिखित में से किसका महत्व अधिक है?\n(a) सत्यामंगलम बाघ आरक्षित
क्षेत्र (सत्यमंगलम टाइगर रिजर्व)\n(b) नल्लामला वन\n(c) नागरहोले
राष्ट्रीय उद्यान\n(d) शेषाचलम जीवमण्डल आरक्षित क्षेत्र (शेषाचलम
बायोस्फीयर रिजर्व)\n\n, choose correct answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "5. समाज में समानता के होने का
एक निहितार्थ यह है कि उसमें\n(a) विशेषाधिकारों का अभाव है\n(b) अवरोधों
का अभाव है\n(c) प्रतिस्पर्धा का अभाव है\n(d) विचारधारा का अभाव है\n\n,
choose correct answer:"}], "ideal": "a"}
  ```
</details>

---
## [aramcheck/evals](https://github.com/aramcheck/evals)@[9fdbd94c93...](https://github.com/aramcheck/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Tuesday 2023-06-20 00:35:14 by Tong

Add Loss Logic Eval (#82)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Loss Logic

### Eval description

A store bought a watermelon for $5 and sold it for a different price,
receiving counterfeit money in the transaction. They also had to give
change to the buyer. The net loss for the store varies based on the
specific details of the transaction.

### What makes this a useful eval?

* Tests comprehension and problem-solving skills: The scenarios provided
require the AI to understand and analyze the given information to
determine the net loss for the store.

* Addresses real-world situations: Counterfeit money transactions are a
real concern for businesses. This eval allows the AI to demonstrate its
understanding of financial transactions and the impact of counterfeit
money on a store's net loss.


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Involving the judgement of the truth or falsehood of real-world things,
which is a capability that GPT currently lacks.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"The store purchased a watermelon
for $5 and sold it for $7. Unfortunately, they received $10 in
counterfeit money after the transaction and had to give the buyer $3 in
change. What was the net loss for the store? Let's think step by
step:"}],"ideal":"Sure, let's break down the transaction step by step to
determine the net loss for the store: The store purchases a watermelon
for $5. The store sells the watermelon for $7. This would have been a $2
profit if the money received was real. The store receives $10 in
counterfeit money. This money is worthless, so the store doesn't
actually receive any value from the sale. The store gives the buyer $3
in change. This is a real loss, as the store loses $3 in real money.
Now, let's calculate the net loss: The store spent $5 to purchase the
watermelon. The store lost $3 when giving the buyer change. So the net
loss for the store is $5 (cost of watermelon) + $3 (change given) =
$8."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 but sold it for $4. Furthermore, they received $10 in counterfeit
money from the buyer and had to provide $6 in change. What was the net
loss for the store? Let's consider the process in
detail:"}],"ideal":"Sure, Let's think step by step: The store purchased
a watermelon for $5. The store sold the watermelon for $4, which means
they incurred a loss of $1 on the sale. The buyer gave the store $10 in
counterfeit money, which the store accepted during the transaction. The
store gave the buyer $6 in change. Since the store accepted $10 in
counterfeit money, they lost $10 in that transaction. The net loss for
the store is the sum of the loss on the watermelon sale and the loss
from accepting the counterfeit money, which is $1 + $10 = $11.
Therefore, the net loss for the store is $11."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for the same price of $5. However, they received $10 in
counterfeit money from the buyer and had to give the buyer $5 in change.
What was the net loss for the store? Let's consider the process step by
step:"}],"ideal":"Step 1: The store purchases a watermelon for $5.
Store's expenses: $5 Step 2: The store sells the watermelon for $5 but
receives $10 in counterfeit money. The counterfeit money has no value,
so the store effectively received nothing for the watermelon. Store's
revenue: $0 Step 3: The store gives the buyer $5 in change. Since the
money given in change is real, this is an additional expense for the
store. Store's expenses: $5 (watermelon) + $5 (change) = $10 Step 4:
Calculate the net loss. Net loss = Expenses - Revenue Net loss = $10
(expenses) - $0 (revenue) Net loss = $10 The store's net loss for this
transaction is $10."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for $7. Regrettably, they received $7 in counterfeit
money from the buyer after the transaction. What was the net loss for
the store? Let's consider the process step by step:"}],"ideal":"Sure,
let's break down the transaction step by step: The store purchased a
watermelon for $5. They sold the watermelon for $7, but received
counterfeit money. To determine the net loss, let's analyze the costs
and the revenue: Costs: The store spent $5 on the watermelon. Revenue:
The store received $7 in counterfeit money, which has no value, so their
revenue is $0. Net loss: To calculate the net loss, subtract the revenue
from the costs: $5 (costs) - $0 (revenue) = $5. So, the net loss for the
store is $5."}
{"input":[{"role":"system","content":"The store was given a
complimentary watermelon, which they then sold for $7. Regrettably,
following the transaction, they received $10 in fake money and had to
provide the buyer with $3 in change. Let's consider the following steps
in determining the store's net loss:"}],"ideal":"To determine the
store's net loss, we can consider the following steps: Assess the value
of the complimentary watermelon: Since the watermelon was given to the
store for free, it didn't cost them anything. Therefore, the store's
initial cost for the watermelon is $0. Calculate the revenue from
selling the watermelon: The store sold the watermelon for $7. However,
they received $10 in fake money, which has no value, so the actual
revenue is $0. Determine the cost of the change provided: Since the
store provided the buyer with $3 in change, this is an additional cost
to the store. Calculate the net loss: Subtract the revenue (Step 2) from
the sum of the initial cost (Step 1) and the cost of the change (Step
3). In this case: Net loss = (Initial cost + Cost of change) - Revenue
Net loss = ($0 + $3) - $0 Net loss = $3 The store's net loss from this
transaction is $3."}
  ```
</details>

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[988a6dcc21...](https://github.com/TheVekter/tgstation/commit/988a6dcc2142b4ef3244a18ad4e1781671fb7320)
#### Tuesday 2023-06-20 01:25:19 by YehnBeep

Removes suicide check from positronic brains (#76081)

# About The Pull Request

This removes the suicide check from positronic brains.

# Why It's Good For The Game

There seems to be 2 arguments for why suicide should forbid ghost roles:
1. "If they suicided they didn't want to play"
2. "antag rolling"

So let's look at each.

And an addendum on scope: This is meant only to apply to ghost roles
(and new characters from said roles); I do not wish to change that
people are not allowed back onto the same character they suicided on.

## "Suiciders left the round of their own choice and shouldn't be
allowed back in"

There are many, many ways in this game to end up with a character in a
state that's nearly/effectively unplayable, even if the controlling
player doesn't truly wish to completely leave. Some things can be
resolved with competent medical or science staff, but competent staff
are not always available in a round or might be beleaguered by round
events.

Then there are a number of conditions/states which the game provides no
path to resolve (save drastic measures like abandoning the
character/body, of course).

Or one might have simply become stuck in a place where rescue is
unlikely.

## Antag rolling

The problem here is this code does not particularly target antag
rollers. It paints such a broad brush that it simply catches everyone
whom might not know "No no, you have to **ghost** here, not suicide".
Even if an antag roller is stopped once, they'll easily bypass it next
time through the many, many means open to them - and if 'ghost' is made
effectively the same as 'suicide', it simply punishes people who got
stuck or similar even more.

Because of the wide range of means to kill oneself on a normal
character, to effectively stop antag rolling requires discerning intent
through context and patterns of one's actions. This might not be
possible in code until General Intelligence is a solved problem, and if
it is possible, this doesn't do it. It's a shotgun that kills everyone
in the room and if there happened to be an antag roller there, well,
even a stopped clock is right twice a day.

And then, of course, that the code was broken for so long would seem to
indicate it's not done that much.

## Practical Impact and Design Philosophy

Just from my personal observations, even wanting into a posibrain is a
niche thing usually only taken by a small number of the same players
round-to-round. In practice, whether this PR is merged or not likely
won't have a great impact on the game. But that could change if the
philosophy behind this check is applied to a wider number of things.

If someone wants to die, it's not hard. Walk out an airlock. Into the
supermatter. Blob, Xenos, or some other hazard present? Walk towards
them. Step in front of a shuttle. Turn on internals and wait a bit.
Countless other ways. Except, perhaps, if a character is disabled or
crippled or stuck, in which case use of a verb may be necessary.

In other games with much narrower sets of mechanics, it may be possible
to close certain paths on the assumption it would mostly be used for bad
faith reasons. In SS13, the sheer number of ways in which a good faith
character be "screwed" but not quite killed off, and which a bad faith
actor can find to kill themselves while bypassing restrictions placed on
verbs, means that I think this code's design philosophy is harmful to
the game and its good faith players.

# Changelog

:cl:
del: Positronic brains no longer check for suicide verb use.
/:cl:

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[803658dc30...](https://github.com/TheVekter/tgstation/commit/803658dc30b4445e81592daa1823a98719246269)
#### Tuesday 2023-06-20 01:25:19 by Rhials

Deadchat Announcement Variety Pack 2 and also some fixes to other popups (#76053)

## About The Pull Request

This adds ghost orbit popups for the following: 
- Macrobombs (or stacked microbombs) being triggered.
- HFR Meltdowns.
- Living players about to be gored by an emagged organ harvester.
- Nuclear devices being armed.
- Doomsday devices.
- Blob hosts bursting.

This also modifies the following ghost orbit popups:
- Toy hot potatoes will no longer cause a popup when armed.
- Normal spider eggs will not flash the byond window, only special egg
types.
## Why It's Good For The Game

Gives more gathering spots/information to deadchat. Let no entertaining
moment in this game go unobserved.

Spider eggs flashing your window for every single egg produced makes
alt-tabbing suck. I saw some guy on the forums complaining about it and
thought "huh yeah I guess he's got a point that pisses me off too" so
here we are.
## Changelog
:cl: Rhials
qol: Basic spider eggs no longer flash the byond window when ready to
hatch.
qol: Toy hot potatoes no longer give a ghost notification.
qol: Deadchat will be notified in the event of an imminent macrobomb
detonation, HFR meltdown, organ harvesting,
qol: Deadchat will be notified when a nuclear/doomsday device is
activated, as well as when a blob-infection bursts.
/:cl:

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[403765e947...](https://github.com/Pickle-Coding/tgstation/commit/403765e94759110ddacb67b3c385f3273268896a)
#### Tuesday 2023-06-20 01:46:09 by Pickle-Coding

Fix hypernoblium formation reaction rate sanity.

Fixes hypernoblium formation reaction rate mole count sanity min check. Does this by calculating the bz reduction factor before reaction rate (fuck, I am on mobile and I can not see what I am typing, also I kinda forgot what I said AAAAAAAAAAAA) calculating the reaction rate. It then applies the product of the tritium consumption rate and reduction factor thinf uhh it sucks typing without seeing what I'm writing AAAAAAAA thrhfhfjjgjjhdhshgfsjsbdhhdbzjabdjahsjcnakdbd

---
## [JupiterJaeden/tgstation](https://github.com/JupiterJaeden/tgstation)@[89a2a7cc3a...](https://github.com/JupiterJaeden/tgstation/commit/89a2a7cc3ad48032414a3755864204fed88244de)
#### Tuesday 2023-06-20 03:18:54 by carlarctg

Changes syndicate surgery duffelbags to contain advanced tools (#75846)

## About The Pull Request

Changes syndicate surgery duffelbags to contain advanced tools.

In total, they contain
- All advanced surgical tools, alongside the normal ones without an
advanced version
- Sterilizine gel
- Bone gel and surgical tape
- Roller bed
- Straight jacket, muzzle, and MMI

Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

## Why It's Good For The Game

> Changes syndicate surgery duffelbags to contain advanced tools.

> In total, they contain (...)

The only real reason to buy this item is for the increased storage space
the duffelbag gives, and I find that a little sad. Surgical tools are
plentiful, as they can either be lathed from cargo, medbay, or just
taken. A surgeon, the role that *should* thematically need this the
most, has absolutely no reason to take it. Now they do! A full set of
advanced tools is certainly something that can be considered for
purchase, especially with all the bonus items in here - which might just
allow a traitor to repair their bones if they're heavily wanted and
licking their wounds in maintenance. The TC cost has been increased to 4
to compensate.

> Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

Similar to above, but instead, the reasoning is that nukies really do
not have a lot of time to do surgery. A lot of the 20 minutes of prep
time in War is spent figuring out what you're buying with your
exorbitant amount of TC, in non-War you don't really want to delay the
mission for five minutes for surgery, and its hassle means that most
people do not really want to bother with things like nerve threading,
etc. due to the large, annoying time cost.

> The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

The former is because, well, what the hell, why didn't it have one!
Removing the loose tools gave me the space for it. The latter is just me
realizing that empty closet is weird and lame and so I gave it some
fluff contents to give it a reason to exist.

## Changelog

:cl:
add: Changes syndicate surgery duffelbags to contain advanced tools,
sterilizine, surgical tape, and a roller bed.
add: Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.
add: The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.
/:cl:

---
## [Al-1ce/cmss13](https://github.com/Al-1ce/cmss13)@[0f386c8188...](https://github.com/Al-1ce/cmss13/commit/0f386c8188849b2a761ef773ed83d7f2a95d40e7)
#### Tuesday 2023-06-20 03:27:33 by fira

Stops Squad Leaders and ComTechs from blowing up the Almayer (#3602)

# About the pull request

Okay that's a clickbait....

When people put C4 and Breaching Charges in their bag and what not the
log gets triggered.

This spams niche log with false warnings of /!\ DANGEROUS GRIEFING
TERRORISTS /!\

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Uh

# Changelog
:cl:
fix: Handling C4 and Breaching Charges should not zealously trigger
antigrief protection anymore
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[099edf2ec3...](https://github.com/newstools/2023-new-york-post/commit/099edf2ec3bdab57a57485551750f8c027d3f649)
#### Tuesday 2023-06-20 04:06:16 by Billy Einkamerer

Created Text For URL [nypost.com/2023/06/19/lawyer-facing-30-to-life-for-murdering-his-girlfriend-dies-in-custody/]

---
## [JakePrim/react-native](https://github.com/JakePrim/react-native)@[3af66bf7fb...](https://github.com/JakePrim/react-native/commit/3af66bf7fbd88d77fe27770bcb829768bf949b9c)
#### Tuesday 2023-06-20 05:51:52 by Ramanpreet Nara

Java: Make TurboModuleManager's APIs use NativeModule interface (#36629)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/36629

The scope of TurboModuleManager is increasing:
- Eventually, it'll be capable of creating interop NativeModules (i.e: NativeModules that don't implement TurboModule).

So, instead of creating duplicate methods for NativeModules on the TurboModuleManager, this diff changes the APIs of TurboModuleManager to work with the NativeModule interface.

Thoughts?

## Questions
**Question:** Is this a breaking change for open source?
- Technically, yes. This diff changes the public interface of TurboModuleManager.

**Question:** How large of a thrash will this cause for open source apps?
- The thrash should be minimal. People in open source shouldn't be creating their own TurboModuleManager. They also shouldn't be directly accessing the TurboModuleManager object either.

**Question:** Is this change safe?
- Yeah. All the code that calls into TurboModuleRegistry converts TurboModules it returns into NativeModules.

**Question:** Is this change move us in the right direction?
- Long term, the TurboModule system will support legacy modules as well as TurboModules.
- I think it makes a lot of sense to have one Java-facing registry: after all, Java will just treat these NativeModules/TurboModules as regular Java objects, and call public methods on them. It doesn't care if the module is TurboModule-compatible or not.
- As for the TurboModuleRegistry abstraction, I think we should eventually rename this to NativeModuleRegistry after we delete the current NativeModuleRegistry.
- Still thinking about this though. I will leave this diff in review to welcome comments.

Changelog: [Android][Deprecated] - Deprecate TurboModuleRegistry.getModule(), getModules(), hasModule(),

Reviewed By: mdvacca

Differential Revision: D43801531

fbshipit-source-id: 4af7cbc2e2dc7c1d664acbd38c83aa93aae23c9f

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[1468797059...](https://github.com/silicons/Citadel-Station-13-RP/commit/146879705978b0416739823fa54467e865c3ffb2)
#### Tuesday 2023-06-20 06:15:01 by TheObserver-sys

Take 2: Some fixes and QoL (#5601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Would you believe me if I hadn't updated my git in about 400 years, and
had to blow the old version of my repo up?
Yes? No? It doesn't matter.

Anyways! Meat and potatoes of this:
Allows players to make gene and plant discs freely in the protolathe.
Since we do not have a dedicated genetics, this will help the pains of
actually doing genetics by giving us storage solutions for genes.

Fixes a problem with brass also creating slag when compressing, by
setting the copper alloy flag to 1.

And finally: Allows you to upgrade the braces! If your brace has T3 or
better, a single brace can hold an entire drill. All credit goes to
Hatterhat for this one, as I pretty much wholesale ripped it from his
buff of the big drill™ on Virgo.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not making slag is ALWAYS good. It saves on material, too.
Having more discs for a cheap cost is also good, it means you can reduce
headaches while scoping out for genes, because there are many, and the
ability to track them are currently few.
And honestly, the less lugging a person has to do with the mining drill,
the more likely people might stop blowing up an already unstable planet
with miniature hydrogen bombs.
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl: The0bserver
add: Discs are able to be produced in the protolathe now. Go nuts, or
don't. I'm not your guardian.
balance: Mining Drills can finally be operated with just one brace with
the requisite parts. Thank you, Hatterhat!
fix: Copper no longer smelts slag when set to "Alloying."
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: TheObserver-sys <Gizmomaster777@gmail.com>

---
## [Omar-HeshamR/evals](https://github.com/Omar-HeshamR/evals)@[f5844592f1...](https://github.com/Omar-HeshamR/evals/commit/f5844592f13eff8e7b9927d5cec0d2627694d9d9)
#### Tuesday 2023-06-20 06:45:33 by Ali-consensus

Eval: Consensus Summary (#1140)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
Consensus Summary

### Eval description

Utilize the model's ability to produce a Scientific Consensus in
response to a scientific inquiry using the provided claims.

### What makes this a useful eval?

This is a useful eval because it evaluates the model's ability to
produce a scientific consensus in response to a given set of claims.
This is important because scientific consensus is the result of multiple
studies and data that may or may not support the same conclusion. A
model that can accurately produce scientific consensus can help in
making informed decisions and policies based on scientific evidence.
Hence, evaluating a model's ability to produce a scientific consensus
using the Consensus Summary eval can be useful in assessing its
reliability and potential for practical applications.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: Two doses of mRNA covid-19 vaccines
were observed to be highly effective against symptomatic infection and
severe outcomes.\nclaim: COVID-19 vaccines currently authorized in the
United States are highly effective in preventing COVID-19-associated
hospitalizations in older adults.\nclaim: In summary, vaccines are a
powerful tool that can be used to control the COVID-19 pandemic, with
high efficacy and tolerable ADRs.\nclaim: Conclusion Overall, we
conclude that vaccination against COVID-19 in patients with active
malignancies using activated and inactivated vaccines is a safe and
tolerable procedure that is also accompanied by a high efficacy.\nclaim:
COVID-19 vaccines provide good protection against COVID-19 presentation
at primary care/outpatient level, particularly among fully vaccinated
individuals.\nquestion: are covid-19 vaccines effective?"}], "ideal":
"Summary: Covid-19 vaccines are highly effective at protecting against
infection and hospitalization."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: Lower zinc is a hallmark of
depression, while increments in serum zinc and attenuation of the
immune-inflammatory response during treatment appear to play a role in
the clinical efficacy of sertraline.\nclaim: An increase in dietary zinc
and higher plasma zinc levels may reduce the risk of depressive
symptoms.\nclaim: Although decreased zinc levels have been implicated in
the genesis of depression in animal models and in major depressive
disorder in humans, this study provides the first evidence of a role for
zinc in depression in people with dementia and highlights zinc
metabolism as a therapeutic target.\nclaim: The results of this study
show that long-term intake of zinc may modulate symptoms of
depression.\nclaim: The reported results indicated that the serum zinc
level might be a marker of depression as a state (state marker) in
treatment responsive patients.\nquestion: can zinc help treat
depression?"}], "ideal": "Summary: All of these studies suggest that low
zinc levels are a marker of depression and that intake of zinc may have
the ability to help reduce symptoms of depression"}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The findings suggest that the
following characteristics of the founder significantly influence the
success potential of an incubated venture: entrepreneurial personality,
motivation for starting the venture, managerial skills, and approach
towards innovation.\nclaim: Using a sample of 384 entrepreneurs selected
from the two leading business districts in Uganda, we observe that
optimism is the component of psychological capital that significantly
moderates the relationship between startup capital and entrepreneurial
success.\nclaim: Both startup capital and psychological capital are
significant predictors of entrepreneurial success; however,
psychological capital is the better predictor.\nclaim: Entrepreneurially
self\u2010efficacious founder/managers may help improve the performance
of very young firms but such benefits dissipate over time.\nclaim: This
finding indicates that the entrepreneurial team\u2019s startup
experience plays stronger roles in venturing profitable startups when
the amount of financial resources and initial firm size are small;
however, the team\u2019s startup experience and intangible resources
have positive interaction effects on new-born startups\u2019
profitability.\nquestion: what predicts success as a startup
founder?"}], "ideal": "Summary: Things like entrepreneurial personality,
motivation for starting the venture, managerial skills, previous
start-up experience, startup and psychological capital and optimism all
predict success as a startup founder"}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: While homelessness is ultimately the
result of a severe and chronic shortage of affordable housing, creating
accessible, safe, pet-friendly shelter and safe haven options and
instituting a smoother, more transparent process for moving from the
streets could substantially reduce street homelessness.\nclaim: - To
prevent the revolving door to homelessness, it is necessary to remove
the barriers that hinder access to normal health resources which are
experienced by people suffering from social exclusion, while
implementing ongoing support programmes for homeless people or those at
risk of homelessness, which primarily deal with health issues.\nclaim:
We conclude that overcoming homelessness requires policies and practices
that give a greater focus to non-material aspects of homelessness
through an emphasis on empowerment, self-respect and autonomy.\nclaim:
This finding suggests that homelessness can be reduced by appropriate
clinical interventions if housing is available.\nclaim: For homelessness
prevention, systematic and outreach social medical care before and
during homelessness should be provided.\nquestion: What are effective
ways to prevent homelessness?"}], "ideal": "Summary: Ways to prevent
homelessness include creating accessible, safe shelter and safe haven
options, removing barriers to health resources, giving a greater focus
to non-material aspects of homelessness, and providing systematic and
outreach social medical care."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: While homelessness is ultimately the
result of a severe and chronic shortage of affordable housing, creating
accessible, safe, pet-friendly shelter and safe haven options and
instituting a smoother, more transparent process for moving from the
streets could substantially reduce street homelessness.\nclaim: - To
prevent the revolving door to homelessness, it is necessary to remove
the barriers that hinder access to normal health resources which are
experienced by people suffering from social exclusion, while
implementing ongoing support programmes for homeless people or those at
risk of homelessness, which primarily deal with health issues.\nclaim:
We conclude that overcoming homelessness requires policies and practices
that give a greater focus to non-material aspects of homelessness
through an emphasis on empowerment, self-respect and autonomy.\nclaim:
This finding suggests that homelessness can be reduced by appropriate
clinical interventions if housing is available.\nclaim: For homelessness
prevention, systematic and outreach social medical care before and
during homelessness should be provided.\nquestion: How to prevent
homelessness?"}], "ideal": "Summary: Ways to prevent homelessness
include creating accessible, safe shelter and safe haven options,
removing barriers to health resources, giving a greater focus to
non-material aspects of homelessness, and providing systematic and
outreach social medical care."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The findings revealed that the
factor that contributes the most to entrepreneurship intention is Locus
of control, followed by Need of Achievement and Subjective
Norms.\nclaim: It was found that entrepreneurial skill, environmental
factors and entrepreneurial orientation have a positive influence on
entrepreneurial intention.\nclaim: The findings indicate that
entrepreneurial motivation has a significant correlation with
entrepreneurial intention and its three determinants, social valuation
of entrepreneurship, having entrepreneurial role models, knowledge of
entrepreneurial support and perceived barriers to starting a
business.\nclaim: Research finding revealed that entrepreneurial
intention is indirectly affected by entrepreneurship education, meaning
that students\u2019 entrepreneurial motivation and attitude are two
important mediating variables.\nclaim: Findings confirm the influence of
individual and socio-cultural factors on entrepreneurial
intention.\nquestion: What are the factors of entrepreneurship
intention"}], "ideal": "Summary: Studies find that intrinsic factors,
such as entrepreneurial skill and motivation, as well as extrinsic
variables, such as the environmental support of entrepreneurship,
mediate entrepreneurship intention."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The results show that digital
agriculture is able to help users to increase productivity in a
sustainable way.\nclaim: Digital agriculture technologies continue the
centralization of economic knowledge and power as they facilitate the
transformation of vast territories into \u201coperational
landscapes\u201d that provide the material, energy, and labor for a
rapidly expanding urban system.\nclaim: The digital agriculture system
is an effective tool for insurance industry to use to develop a
dynamical business plan for the changing climate.\nclaim: The technical
fitting-out of agriculture in the digital economy should be considered
as a set of measures to prepare the industry for the production of
high-quality products, which implies the use of digital technologies
that minimize human participation in the production process.\nclaim:
Consequently, the initial Mobile-based Information System evolved into a
Digital Knowledge Ecosystem that can predict current production
situation in near real enabling government agencies to dynamically
adjust the incentives offered to farmers for growing different types of
crops to achieve sustainable agriculture production through crop
diversification.\nquestion: What is digital agriculture?"}], "ideal":
"Summary: N-A"}
  ```
</details>

---
## [Omar-HeshamR/evals](https://github.com/Omar-HeshamR/evals)@[d708a6be26...](https://github.com/Omar-HeshamR/evals/commit/d708a6be261bfcb04962e64969164d737ba3972c)
#### Tuesday 2023-06-20 06:45:33 by dougkwanna

NFL Point Combinations Eval (#1129)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

NFL Point Combinations

### Eval description

This eval tests the model's ability to calculate all the possible ways
to achieve a specific score by a single team in an NFL game.

### What makes this a useful eval?

This eval is actually very similar to the coin change problem which
GPT-4 handles very well. However, it is extremely inaccurate when asked
to applied that same type of problem to a real life situation (2.5%
accuracy for GPT-3.5-turbo and 12.5% accuracy for GPT-4). It is
important for the model to learn how to derive logic problems from real
life context.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 4 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[1]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 6 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[3]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 7 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[2]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 12 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[7]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 25 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[24]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 38 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[68]"}
  ```
</details>

---
## [Omar-HeshamR/evals](https://github.com/Omar-HeshamR/evals)@[73c8a178e6...](https://github.com/Omar-HeshamR/evals/commit/73c8a178e69418760baee8983daa19fb492e9231)
#### Tuesday 2023-06-20 06:45:33 by somerandomguyontheweb

Add Belarusian rhyme eval (#1143)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

belarusian-rhyme

### Eval description

Test the model's ability to find rhyming words in Belarusian.

### What makes this a useful eval?

This eval is inspired by similar submissions for
[Hebrew](https://github.com/openai/evals/pull/176),
[Russian](https://github.com/openai/evals/pull/708),
[Ukrainian](https://github.com/openai/evals/pull/867),
[Finnish](https://github.com/openai/evals/pull/970), and
[Italian](https://github.com/openai/evals/pull/1003). The dataset
contains 50 pairs of English nouns whose Belarusian translations rhyme,
and another 50 pairs consisting of the same nouns but reordered, so that
in each of these additional pairs there aren't any Belarusian
translations that rhyme. The model's task is to output the rhyming pair
of Belarusian words or NONE. The rhyming pairs have been manually
picked, and many of them contain at least one word distinctive of
Belarusian, i.e. not attested in closely related Russian and Ukrainian
languages.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "grass, church"}], "ideal":
["трава, царква", "царква, трава"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "food, tower"}], "ideal": ["ежа,
вежа", "вежа, ежа"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "grass, food"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "church, tower"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "foot, queue"}], "ideal": ["нага,
чарга", "чарга, нага"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "boat, flood"}], "ideal": ["лодка,
паводка", "паводка, лодка"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "foot, boat"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "queue, flood"}], "ideal": "NONE"}
  ```
</details>

---
## [arp242/fallout1-ce](https://github.com/arp242/fallout1-ce)@[28b2aea454...](https://github.com/arp242/fallout1-ce/commit/28b2aea454cea697c588c63a6c3a0edafb1b4102)
#### Tuesday 2023-06-20 07:02:47 by Martin Tournoij

Make arrow keys not scroll so slow you want to self-harm

All keyboard and mouse button work via standard text editor semantics:
keeping a button pressed will wait for a while, after which it will
repeat at fixed rate.

That's fine for a text editor or whatnot, but it's painful when you want
to scroll with the arrow keys. I hated this back when I first played the
game, and I'm hating it now. I don't think anyone will miss the old
"functionality".

We can't outright remove the delay for all keys, as e.g. pressing "i"
will repeat so fast that you can never open the inventory. Come to think
of it, I think we can remove all of this functionality, at least for the
keyboard as I don't *think* it's ever used (it is used for mouse
buttons, although that too can be simplified greatly) – but all of that
is a much larger refactor.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[390384ecbb...](https://github.com/odoo-dev/odoo/commit/390384ecbb44b768be3502e7080315830a54e68b)
#### Tuesday 2023-06-20 07:46:46 by Xavier Morel

[FIX] core: handle recursion error when resolving stored fields

Issue discovered in the uninstall (and reinstall) of sale_project: a
dump has ~100 tasks, when reinstalling `sale_line_id` has to be
initialised, this is done by marking `sale_line_id` on all extant
tasks as to-recompute, which triggers their computation on the next
`flush`.

Because it's a recursive field, `Field.recompute` ensures only one
record at a time gets recomputed (as there could be cross-dependencies
in the recorset which protection would prevent from resolving).

As the field computation runs, it accesses itself, which triggers a
cache miss, which triggers a `_fetch_field` (to get the currently
stored value), this calls `_read`, which flushes the field we're
trying to read.

The problem here is that for efficiency the cache miss will look for
all records in the cache without a value for the
field (`_in_cache_without`) and try to `fetch` on them as well. This
means rather than not doing anything in flush, we're going to
`Field.recompute` on all records except the one selected the first
time around, which repeats the cycle until there is no more additional
record found in `_in_cache_without`, which could trigger the next
round of `recompute`, and the entire thing unwinds, and we probably
perform a ton of unnecessary additional `compute_value`.

Except that doesn't even happen, because the process from one compute
to the next takes 12~13 stack frames, which given the default
recursion limit of 1000 gives a hard limit of 76 fields before hitting
a RecursionError. As this is less than 100, a recursion error [is what
we get](https://runbot.odoo.com/runbot/build/31726625).

In 15.2, this was fixed by only expanding the fetch on non-recursive
fields, pessimizing recursive
fields (5c2511115b14299516fce4aa3737a62faaf5b653). Test-wise this only
impacted mail performances and in a relatively minor manner.

In 16.0, the mail tests actually match already (so that part was
skipped by the cherrypicking) however this impacts the knowledge perf
tests much more significantly e.g. `test_article_creation_multi_roots`
gets +9 queries when creating 10 top-level articles, which is a bit
much.

So use an alternative which is ugly as hell but which I didn't
consider for 15.2 (may want to backport it one day if the current fix
is an issue): catch the recursion error and use the existing
fallback (of fetching just the requested record's field without
expanding the recordset).

This likely makes for a pretty inefficient situation in the original
case as we're certainly going to hit the recursion limit repeatedly,
but that still fixes the issue, and it avoids deoptimising cases which
fall short of the recursion limit (resolving under 60 records or
so).

Plus despite creating giant stacks we might actually get good
efficiency as we're going to hit recursion limits repeatedly but
that's pure python, once we fall below the limit we can resolve
everything at once with a single SQL query (or something along those
lines).

X-original-commit: 9e71094582ec4c9b719431e77538da8f91ffa9e3
Part-of: odoo/odoo#121522

---
## [Omar-HeshamR/evals](https://github.com/Omar-HeshamR/evals)@[f34bb67d18...](https://github.com/Omar-HeshamR/evals/commit/f34bb67d18cb07c6a68ae7c3871e82814df0863f)
#### Tuesday 2023-06-20 07:52:36 by Drax

[evals] add ascii-art-digit-recognition (#509)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
ascii-digit-recognition

### Eval description

Tests the LLMs' ability to recognize digits [0-9] as ASCII arts
(creating images using letters, numbers, and symbols from the ASCII
character set).

### What makes this a useful eval?

Language seems to be a one-dimensional sequence while images are
two-dimensions. Therefore, recognizing 2d images (simple ASCII art) is a
difficult task intuitively, requiring a certain degree of spatial
imagination ability (my opinion). GPT3.5 (30%) and GPT3-DaVinci (20%)
suffer from the task. It would be interesting to see the performance of
GPT-4.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n ```
aaaaa \na a\na a\na a\na a\na a\n aaaaa``` Answer only a single
digit."}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n ```
a \n aa \na a \n a \n a \n a \n aaaaa``` Answer only a single digit."}],
"ideal": "1"}
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n
```aaaaa\n a\n a\naaaaa\na \na \naaaaa ``` Answer only a single
digit."}], "ideal": "2"}
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n
```aaaaa\n a\n a\n aaaa\n a\n a\naaaaa ``` Answer only a single
digit."}], "ideal": "3"}
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n ```a
a\na a\na a\naaaaa\n a\n a\n a ``` Answer only a single digit."}],
"ideal": "4"}
  ```
</details>

Some visualization of the ASCII arts: 

![image](https://user-images.githubusercontent.com/52069185/228619558-40e3c004-9c65-495f-89a8-68d80f241f44.png)

---
## [hanifardhani/platinum_kernel_xiaomi_platina](https://github.com/hanifardhani/platinum_kernel_xiaomi_platina)@[01acfa4833...](https://github.com/hanifardhani/platinum_kernel_xiaomi_platina/commit/01acfa483365e12353b7a66d4cb22235c7062ca0)
#### Tuesday 2023-06-20 07:57:42 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[44d941b773...](https://github.com/rafay99-epic/evals/commit/44d941b7734983950d09d9f0012ec58ec45e171c)
#### Tuesday 2023-06-20 08:35:45 by HorizonAuto

Context-free-grammars (#1097)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

context-free-grammar

### Eval description

This tests the ability for GPT-4 to evaluate whether or not a string can
be produced by a given context-free grammar.

### What makes this a useful eval?

This is an interesting computational task. Context-free languages are
important in linguistics, and it will be interesting to see
how a language model fares in handling this task.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [✅] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [✅] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [✅] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [✅] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)
I've handcrafted a lot of these examples. Some of them are there to
'trick' the model––I think it will be a useful test to see how well the
language model can do at those.

## Eval structure 🏗️

Your eval should

- [✅] Check that your data is in `evals/registry/data/{name}`
- [✅] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [✅] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [✅] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [✅] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [✅] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [✅] I have filled out all required fields of this form
- [✅] I have used **Git LFS** for the Eval JSON data
- [✅] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01010101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '00011101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '00110101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01001101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01010011' in the
language?"}], "ideal": "true"}
  ```
</details>

---------

Co-authored-by: Arjun Taneja <arjun.taneja02@gmail.com>

---
## [rafay99-epic/evals](https://github.com/rafay99-epic/evals)@[04e1312631...](https://github.com/rafay99-epic/evals/commit/04e131263125d46812f19ce4cc58d55207beee3b)
#### Tuesday 2023-06-20 08:35:45 by Nazar

Russian verse (#979)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
russian-verse

### Eval description

The most popular Russian poems that nearly every Russian speaker can
recall

### What makes this a useful eval?

Understanding a basic Russian poem or any foreign literature is
significant for a Language Learning Model (LLM) like GPT-4 because it
enhances multilingual ability, provides cultural context, and improves
understanding of language structure. It makes the model globally useful,
and culturally sensitive.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nМороз и солнце день чудесный\nЕще ты дремлешь друг
прелестный \nПора красавица проснись\nОткрой сомкнуты негой
взоры\nНавстречу северной Авроры"}], "ideal": "Звездою севера явись"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nУ лукоморья дуб зелёный\nЗлатая цепь на дубе том\nИ
днём и ночью кот учёный\nВсё ходит по цепи кругом\nИдёт направо песнь
заводит"}], "ideal": "Налево сказку говорит"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЯ к вам пишу чего же боле\nЧто я могу еще
сказать\nТеперь я знаю в вашей воле\nМеня презреньем наказать\nНо вы к
моей несчастной доле"}], "ideal": "Хоть каплю жалости храня"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЯ помню чудное мгновенье\nПередо мной явилась
ты\nКак мимолетное виденье\nКак гений чистой красоты\nВ томленьях грусти
безнадежной"}], "ideal": "В тревогах шумной суеты"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЛюбви надежды тихой славы\nНедолго нежил нас
обман\nИсчезли юные забавы\nКак сон как утренний туман\nНо в нас горит
еще желанье"}], "ideal": "Под гнетом власти роковой"}
  ```
</details>

---
## [SF-Jake/Victorian-Legacy](https://github.com/SF-Jake/Victorian-Legacy)@[ade47d2d94...](https://github.com/SF-Jake/Victorian-Legacy/commit/ade47d2d94a22227973d5e3a4cda356e4b31faac)
#### Tuesday 2023-06-20 08:40:36 by Jake0126

Major Update

- Decreased build time for factories to 30 days
- Changed Core wargoal to require justification and transfer wargoal is now a instant declaration
- Removed Newspaper entirely from view and it won't generate any newspapers to help reduce any chance of an oos
- Increase Gas attack modifier 2->3
- Removed prestige loss from both General removal and sphere removal
- Decrease diplomatic cost for some requests
- Added a tension decay to decay rapidly and prevent a crisis from existing in the first place
- Buffed Napoleon III modifier 1%->2% Mob Size
- Decrease Education Idea 25%->15%
- National values have been changed to Reno nv and our more choice based than oh whats the best out of them all
- Removed German Rebel formation
- Blockade war exhaustion has been decreased +0.08->+0.02
- Removed Administrative Efficiency Modifier negative from War Exhaustion
- Grants have been updated to Reno version so it shouldn't crash no more now
- Increased Forced Reform to allow for 2 reforms to be passed
- Increased Persia POP Literacy 3%->3.5%
- NGF can now form without needing all cores only the sphere no longer need to exist for the formation to be valid and give cores.
- Spain Reconquista now gives Central American Accepted
- When a nation civilizes there is a bug with Vic2 which if say Hussar which was earned through an invention would be removed on civilize this is now part of the tech instead of a invention for just Hussars the other horse brigades still have this issue.
- Diseases have been completely removed from the mod
- Canada now starts with all it's land day 1
- France life rating nerfed to 32 life rating capitol state and some major cities still have 35-40 life rating
- Updated Persian troops to have artillery
- Updated Music
- All navy inventions is now 100% drop
- Removed Tutorial button
- Might have missed something in this patch

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[6fc0273b5a...](https://github.com/rust-lang-ci/rust/commit/6fc0273b5a57eb78cc00841181113fda3e509478)
#### Tuesday 2023-06-20 08:42:41 by bors

Auto merge of #112320 - compiler-errors:do-not-impl-via-obj, r=lcnr

Add `implement_via_object` to `rustc_deny_explicit_impl` to control object candidate assembly

Some built-in traits are special, since they are used to prove facts about the program that are important for later phases of compilation such as codegen and CTFE. For example, the `Unsize` trait is used to assert to the compiler that we are able to unsize a type into another type. It doesn't have any methods because it doesn't actually *instruct* the compiler how to do this unsizing, but this is later used (alongside an exhaustive match of combinations of unsizeable types) during codegen to generate unsize coercion code.

Due to this, these built-in traits are incompatible with the type erasure provided by object types. For example, the existence of `dyn Unsize<T>` does not mean that the compiler is able to unsize `Box<dyn Unsize<T>>` into `Box<T>`, since `Unsize` is a *witness* to the fact that a type can be unsized, and it doesn't actually encode that unsizing operation in its vtable as mentioned above.

The old trait solver gets around this fact by having complex control flow that never considers object bounds for certain built-in traits:
https://github.com/rust-lang/rust/blob/2f896da247e0ee8f0bef7cd7c54cfbea255b9f68/compiler/rustc_trait_selection/src/traits/select/candidate_assembly.rs#L61-L132

However, candidate assembly in the new solver is much more lovely, and I'd hate to add this list of opt-out cases into the new solver. Instead of maintaining this complex and hard-coded control flow, instead we can make this a property of the trait via a built-in attribute. We already have such a build attribute that's applied to every single trait that we care about: `rustc_deny_explicit_impl`. This PR adds `implement_via_object` as a meta-item to that attribute that allows us to opt a trait out of object-bound candidate assembly as well.

r? `@lcnr`

---
## [alexadarsh/Password-Generator-using-Java](https://github.com/alexadarsh/Password-Generator-using-Java)@[f0952bab02...](https://github.com/alexadarsh/Password-Generator-using-Java/commit/f0952bab0256c49e4c89fea3651dc169dbe4f3d9)
#### Tuesday 2023-06-20 09:36:24 by Adarsh kumar

Update README.md

Password-Generator-using-Java
Password-Generator
This project is a Java Console Application to generate random passwords and perform password strength checks.

Introduction
I decided to build this project during the Summer Break of my Third Sem after taking the Object-Oriented Effective Java Programming course. I wanted to build something interesting with Java to practice and see what I could do on my own. However, I still wasn't sure what I wanted to do. Then one night, while explaining to my father the importance of having a strong password for his social media accounts, I got the idea of creating a random password generator. A week later, it was done.

While working on it, I decided to include a password strength checker feature that checks the overall strength of the entered password. I was pretty happy with how it turned out, but I realized that it was not very straightforward to use for someone who does not know how it is supposed to work. So, I decided to create a GUI for the application for the next step, which is available in the Password-Services repository.

Functionalities
1. Generating a Password:
The user answers with "Yes" or "No" to questions about using uppercase letters, lowercase letters, numbers, or symbols.
The user then enters the desired length of the password.
A password alphabet is generated based on the user's answers, which is a string containing the chosen characters.
Random characters from the password alphabet are selected and combined to form a completely random string according to the user's preferences.
The randomly generated password is then displayed on the console.
2. Checking a Password's Strength:
The strength check is based on the following criteria:

The password uses uppercase letters.
The password uses lowercase letters.
The password uses numbers.
The password uses symbols.
The length of the password is 8 or more (8 is often the minimum required length for a decent password).
The length of the password is 16 or more (16 is considered to be the minimum length for a good password).
These criteria are used to calculate a score for the password, which determines the message displayed to the user indicating the strength of the password (weak/medium/good/great).

3. Displaying Useful Information:
This is a minor feature that displays information for the user on the console about password security, such as avoiding using the same password twice, avoiding character repetition, keyboard patterns, dictionary words, letter or number sequences, etc.

---
## [cdce8p/mypy](https://github.com/cdce8p/mypy)@[0873230ee6...](https://github.com/cdce8p/mypy/commit/0873230ee60461110bd7bfde7ca3886878aae389)
#### Tuesday 2023-06-20 09:38:33 by Ivan Levkivskyi

Foundations for non-linear solver and polymorphic application (#15287)

Fixes #1317
Fixes #5738
Fixes #12919 
(also fixes a `FIX` comment that is more than 10 years old according to
git blame)

Note: although this PR fixes most typical use-cases for type inference
against generic functions, it is intentionally incomplete, and it is
made in a way to limit implications to small scope.

This PR has essentially three components (better infer, better solve,
better apply - all three are needed for this MVP to work):
* A "tiny" change to `constraints.py`: if the actual function is
generic, we unify it with template before inferring constraints. This
prevents leaking generic type variables of actual in the solutions
(which makes no sense), but also introduces new kind of constraints `T
<: F[S]`, where type variables we solve for appear in target type. These
are much harder to solve, but also it is a great opportunity to play
with them to prepare for single bin inference (if we will switch to it
in some form later). Note unifying is not the best solution, but a good
first approximation (see below on what is the best solution).
* New more sophisticated constraint solver in `solve.py`. The full
algorithm is outlined in the docstring for `solve_non_linear()`. It
looks like it should be able to solve arbitrary constraints that don't
(indirectly) contain "F-bounded" things like `T <: list[T]`. Very short
the idea is to compute transitive closure, then organize constraints by
topologically sorted SCCs.
* Polymorphic type argument application in `checkexpr.py`. In cases
where solver identifies there are free variables (e.g. we have just one
constraint `S <: list[T]`, so `T` is free, and solution for `S` is
`list[T]`) it will apply the solutions while creating new generic
functions. For example, if we have a function `def [S, T] (fn:
Callable[[S], T]) -> Callable[[S], T]` applied to a function `def [U]
(x: U) -> U`, this will result in `def [T] (T) -> T` as the return.

I want to put here some thoughts on the last ingredient, since it may be
mysterious, but now it seems to me it is actually a very well defined
procedure. The key point here is thinking about generic functions as
about infinite intersections or infinite overloads. Now reducing these
infinite overloads/intersections to finite ones it is easy to understand
what is actually going on. For example, imagine we live in a world with
just two types `int` and `str`. Now we have two functions:
```python
T = TypeVar("T")
S = TypeVar("S")
U = TypeVar("U")

def dec(fn: Callable[[T], S]) -> Callable[[T], S]: ...
def id(x: U) -> U: ...
```
the first one can be seen as overload over
```
((int) -> int) -> ((int) -> int)  # 1
((int) -> str) -> ((int) -> str)  # 2
((str) -> int) -> ((str) -> int)  # 3
((str) -> str) -> ((str) -> str)  # 4
```
and second as an overload over
```
(int) -> int
(str) -> str
```
Now what happens when I apply `dec(id)`? We need to choose an overload
that matches the argument (this is what we call type inference), but
here is a trick, in this case two overloads of `dec` match the argument
type. So (and btw I think we are missing this for real overloads) we
construct a new overload that returns intersection of matching overloads
`# 1` and `# 4`. So if we generalize this intuition to the general case,
the inference is selection of an (infinite) parametrized subset among
the bigger parameterized set of intersecting types. The only question is
whether resulting infinite intersection is representable in our type
system. For example `forall T. dict[T, T]` can make sense but is not
representable, while `forall T. (T) -> T` is a well defined type. And
finally, there is a very easy way to find whether a type is
representable or not, we are already doing this during semantic
analyzis. I use the same logic (that I used to view as ad-hoc because of
lack of good syntax for callables) to bind type variables in the
inferred type.

OK, so here is the list of missing features, and some comments on them:
1. Instead of unifying the actual with template we should include
actual's variables in variable set we solve for, as explained in
https://github.com/python/mypy/issues/5738#issuecomment-511242682. Note
however, this will work only together with the next item
2. We need to (iteratively) infer secondary constraints after linear
propagation, e.g. `Sequence[T] <: S <: Sequence[U] => T <: U`
3. Support `ParamSpec` (and probably `TypeVarTuple`). Current support
for applying callables with `ParamSpec` to generics is hacky, and kind
of dead-end. Although `(Callable[P, T]) -> Callable[P, List[T]]` works
when applied to `id`, even a slight variation like `(Callable[P,
List[T]]) -> Callable[P, T]` fails. I think it needs to be re-worked in
the framework I propose (the tests I added are just to be sure I don't
break existing code)
4. Support actual types that are generic in type variables with upper
bounds or values (likely we just need to be careful when propagating
constraints and choosing free variable within an SCC).
5. Add backtracking for upper/lower bound choice. In general, in the
current "Hanoi Tower" inference scheme it is very hard to backtrack, but
in in this specific choice in the new solver, it should be totally
possible to switch from lower to upper bound on a previous step, if we
found no solution (or `<nothing>`/`object`).
6. After we polish it, we can use the new solver in more situations,
e.g. for return type context, and for unification during callable
subtyping.
7. Long term we may want to allow instances to bind type variables, at
least for things like `LRUCache[[x: T], T]`. Btw note that I apply force
expansion to type aliases and callback protocols. Since I can't
transform e.g. `A = Callable[[T], T]` into a generic callable without
getting proper type.
8. We need to figure out a solution for scenarios where non-linear
targets with free variables and constant targets mix without secondary
constraints, like `T <: List[int], T <: List[S]`.

I am planning to address at least majority of the above items, but I
think we should move slowly, since in my experience type inference is
really fragile topic with hard to predict long reaching consequences.
Please play with this PR if you want to and have time, and please
suggest tests to add.

---
## [LGS-Mercy/evals](https://github.com/LGS-Mercy/evals)@[24dae81ae0...](https://github.com/LGS-Mercy/evals/commit/24dae81ae06ebc70808690c7a147f2710e3e54bf)
#### Tuesday 2023-06-20 10:28:48 by Yohei Inui

Compare countries by area (#623)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Compare countries by area

### Eval description

Test the model's ability to determine which country has the largest area

### What makes this a useful eval?

The model should be able to factually determine which country has the
largest area based on accurate facts.
In this eval we use The World
Factbook(https://www.cia.gov/the-world-factbook/field/area/country-comparison)
that is prepared by the CIA for the use of U.S. government officials,
and four countries with similar sizes are compared to each other.
Specifically, four countries adjacent to each other in area ranking are
presented as one option, and the dataset Includes data for countries
ranked 1\~4, 2\~5, ... 100\~103. However, we excluded countries where
sources and interpretations could cause fluctuations in rankings (e.g.,
China and Pakistan). This data set achieved less than 40% accuracy for
both gpt-4 and gpt-3.5-turbo, and the results tend to be worse for
comparisons between countries with smaller areas.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Russia, Canada, United
States, Brazil"}], "ideal": "Russia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Canada, United States,
Brazil, Australia"}], "ideal": "Canada"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. United States, Brazil,
Australia, India"}], "ideal": "United States"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Brazil, Australia, India,
Argentina"}], "ideal": "Brazil"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Australia, India, Argentina,
Kazakhstan"}], "ideal": "Australia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. India, Argentina, Kazakhstan,
Algeria"}], "ideal": "India"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Argentina, Kazakhstan,
Algeria, Democratic Republic of the Congo"}], "ideal": "Argentina"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Kazakhstan, Algeria,
Democratic Republic of the Congo, Saudi Arabia"}], "ideal":
"Kazakhstan"}
  ```
</details>

---------

Co-authored-by: 乾陽平 <inuiyouhei@inuiyouheinoMacBook-Pro.local>

---
## [LGS-Mercy/evals](https://github.com/LGS-Mercy/evals)@[ef1f0ebe0e...](https://github.com/LGS-Mercy/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Tuesday 2023-06-20 10:28:48 by Josh Gruenstein

Add SVG understanding eval (#786)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
`svg_understanding`

### Eval description

The model is provided with the contents of an SVG path (anywhere from
~1000 to ~8000 characters) of a simple object (eg `frog`, `banana`) and
is asked to provide the label.

### What makes this a useful eval?

This is a test of visual understanding and mental modeling. A motivated
human could succeed on these evals with enough time and a piece of graph
paper: in theory, a sufficiently advanced LLM could have the in-context
capacity to do this on the fly.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This uniquely tests the ability to incrementally build visual models:
eg, the ability of the LLM to both "draw" and visualize that "drawing".

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6110 12794 c-744 -50 -1284 -157 -1875 -371 -1796 -650 -3199
-2050 -3853 -3843 -186 -510 -302 -1037 -359 -1625 -21 -224 -24 -827 -5
-1045 84 -957 332 -1788 774 -2595 623 -1137 1607 -2078 2780 -2656 720
-354 1441 -556 2273 -636 224 -21 827 -24 1045 -5 741 65 1376 221 2018
493 2051 871 3514 2775 3826 4979 48 336 60 510 60 895 1 366 -7 507 -45
810 -168 1357 -769 2626 -1711 3612 -536 561 -1129 998 -1809 1333 -718
354 -1450 559 -2264 635 -159 15 -727 28 -855 19z"}], "ideal": "circle"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M4495 12298 c-604 -535 -1486 -866 -2660 -998 -331 -37 -854
-70 -1104 -70 l-101 0 -2 -415 -3 -416 30 -29 30 -29 735 -4 c620 -3 753
-7 850 -21 149 -22 254 -50 316 -86 82 -46 123 -142 161 -372 16 -95 18
-371 21 -3663 2 -2593 0 -3591 -8 -3675 -44 -446 -177 -714 -416 -838 -279
-144 -663 -202 -1350 -202 l-330 0 -27 -28 -27 -28 0 -389 0 -389 27 -28
27 -28 3386 0 3386 0 27 28 27 28 0 390 0 390 -27 26 -28 26 -390 5 c-415
5 -557 17 -779 62 -212 43 -367 103 -480 187 -156 115 -260 347 -312 693
-17 114 -18 350 -21 5005 l-3 4884 -27 28 -27 28 -410 -1 -411 0 -80
-71z"}], "ideal": "1"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6040 12794 c-19 -2 -91 -9 -160 -14 -245 -21 -529 -65 -1240
-190 -399 -70 -593 -100 -654 -100 -91 0 -475 51 -1126 149 -556 84 -788
109 -1075 118 -621 18 -1014 -108 -1310 -418 -344 -360 -490 -941 -472
-1874 21 -1042 173 -1862 619 -3340 l90 -300 -11 -205 c-43 -764 -28 -1853
40 -2845 108 -1585 337 -3026 550 -3473 37 -77 67 -115 184 -238 70 -73
167 -82 258 -24 56 36 102 96 166 220 317 616 732 2551 901 4200 32 314 89
451 257 623 371 379 1029 373 1387 -13 70 -77 106 -129 155 -227 57 -114
79 -196 91 -340 120 -1375 535 -2972 1031 -3963 188 -374 311 -513 458
-514 140 -1 221 106 316 420 232 762 480 2366 595 3849 58 739 82 1376 79
2060 l-2 490 55 115 c228 475 421 1043 527 1550 123 593 169 1196 158 2084
-5 445 -16 597 -58 836 -149 854 -590 1292 -1369 1360 -106 9 -358 11 -440
4z"}], "ideal": "tooth"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M12395 6223 c-133 -27 -295 -150 -356 -269 -13 -27 -40 -68
-59 -90 -19 -23 -57 -79 -84 -125 -161 -274 -369 -539 -542 -695 -191 -171
-304 -231 -559 -298 -499 -132 -725 -257 -1170 -646 -321 -281 -608 -477
-941 -643 -536 -267 -1054 -408 -1735 -473 -236 -23 -800 -23 -1064 0 -701
60 -1256 173 -1940 396 -951 310 -1915 784 -3057 1503 -109 68 -185 109
-220 118 -84 22 -257 17 -358 -10 -102 -28 -256 -99 -289 -135 l-24 -25 21
-88 c27 -115 108 -357 170 -514 253 -633 609 -1222 1069 -1772 164 -196
545 -577 742 -741 986 -822 2174 -1317 3561 -1481 340 -40 485 -48 880 -48
399 -1 546 8 859 49 965 125 1872 497 2606 1068 309 240 645 572 886 876
386 487 682 1048 788 1495 30 130 44 191 101 470 61 292 121 457 263 720
115 214 230 376 365 517 63 65 90 85 176 127 81 39 117 65 183 128 92 89
108 118 93 171 -9 33 -7 39 17 64 l26 27 -22 43 c-12 24 -64 84 -119 136
-116 110 -204 158 -267 145z"}], "ideal": "banana"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M3920 12790 c-1230 -72 -2320 -649 -3052 -1616 -968 -1280
-1142 -3010 -441 -4408 203 -405 432 -712 913 -1221 556 -589 764 -887 945
-1350 102 -264 141 -353 194 -448 l50 -88 -30 -44 c-62 -92 -109 -251 -109
-370 0 -114 44 -261 106 -357 17 -26 17 -28 -14 -95 -43 -94 -62 -181 -62
-292 0 -142 37 -265 107 -359 l25 -34 -35 -76 c-50 -108 -69 -191 -70 -302
-1 -155 39 -275 126 -382 l47 -58 0 -82 c0 -110 21 -193 77 -308 38 -79 59
-108 132 -180 68 -69 103 -95 171 -128 87 -44 203 -75 324 -89 l70 -8 17
-83 c47 -216 205 -374 404 -402 115 -16 827 -12 908 5 202 42 340 188 385
404 l16 80 66 6 c235 22 429 117 548 268 108 139 152 251 160 416 5 111 5
114 38 150 45 48 99 152 118 227 20 79 21 233 0 320 -8 37 -31 102 -50 144
l-35 77 39 61 c66 102 87 185 86 337 0 114 -4 140 -27 210 -15 44 -36 95
-46 114 l-18 34 34 55 c46 78 70 147 84 245 21 140 -16 308 -95 440 l-34
57 59 114 c33 63 103 222 155 353 147 366 255 566 429 798 132 176 245 304
609 690 366 388 516 578 701 885 550 915 713 2023 454 3090 -186 763 -583
1473 -1129 2020 -668 669 -1520 1069 -2480 1165 -185 19 -667 27 -870
15z"}], "ideal": "lightbulb"}
  ```
</details>

---
## [stahta01/mame](https://github.com/stahta01/mame)@[2bcd9bc772...](https://github.com/stahta01/mame/commit/2bcd9bc772b4f3cc6e8b281703e53561d2c5bea9)
#### Tuesday 2023-06-20 10:31:11 by David 'Foxhack' Silva

segacd.xml, megacdj.xml: Added various CD dumps. (#11344)

New working software list items
-------------------------------
segacd.xml:
Compton's Interactive Encyclopedia v2.00S (USA) [redump.org]
Note! Color Mechanica (USA) [redump.org]
Note! Color Mechanica (USA, alt) [redump.org]
What is X'Eye Multi Entertainment System (USA) [redump.org]
megacdj.xml:
Heavenly Symphony - Formula One World Championship 1993 Hibaihin (Japan) [redump.org]
Keiou Yuugekitai Taikenban Hibaihin (Japan) [redump.org]
Lunar - Eternal Blue Hibaihin Auto Demo (Japan) [redump.org]
Microcosm Demo CD (Japan) [redump.org]
Night Trap Hibaihin (Japan) [redump.org]
Popful Mail Taikenban Hibaihin (Japan) [redump.org]
Silpheed Hibaihin (Japan) (Fixed) [redump.org]
Sonic The Hedgehog CD Hibaihin (Japan) [redump.org]
Thunderhawk Hibaihin (Japan) [redump.org]
Urusei Yatsura - Dear My Friends Hibaihin (Japan) [redump.org]
Yumemi Yakata no Monogatari Hibaihin (Japan) [redump.org]
WonderMega Collection - Game Garden (Japan, alt) [redump.org]

New software list items marked not working
------------------------------------------
segacd.xml:
Surgical Strike (Brazil, 32X) [redump.org]
megacdj.xml:
Psychic Detective Series vol.3 - AYA Auto Demo (Japan) [redump.org]
Silpheed Hibaihin (Japan) [redump.org]

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[cf24f70d86...](https://github.com/RalphHightower/RalphHightower/commit/cf24f70d86e4280671ce401b086483b53f2f0c41)
#### Tuesday 2023-06-20 11:11:01 by Ralph Hightower

docs: ChatGPT Beagle Haiku 

### Beagle Haiku

| *"RalphHightower"* / [ChatGPT](https://chat.openai.com/) |
|---|
| *"Good morning Assistant.  How are you doing today?"* |
|Good morning! I'm an AI language model, so I don't have feelings, but I'm here and ready to assist you. How can I help you today?|
| *"How familiar are you with the dog breed of Beagles?"* |
|I'm quite familiar with the dog breed of Beagles. Beagles are a small to medium-sized breed known for their friendly and gentle nature. They are scent hounds and were originally bred for hunting purposes, particularly for tracking small game like rabbits. Beagles are known for their keen sense of smell, intelligence, and loyalty.<br><br>In terms of appearance, Beagles typically have a short coat that comes in a variety of colors, including tricolor (black, tan, and white), bicolor, and lemon. They have a muscular build, a slightly domed skull, and long, droopy ears that help enhance their sense of smell.<br><br>Beagles are known to be sociable and good with families and children. They are generally happy, curious, and outgoing dogs. However, they do have a strong prey drive and may chase small animals if not properly trained or supervised. Beagles are also known for their vocal nature and can be quite vocal when they want attention or are on the scent of something interesting.<br><br>If you have any specific questions about Beagles or need more information, feel free to ask!|
| *"Could you create five Haiku verses about Beagles"* |
|Certainly! Here are five Haiku verses about Beagles:|
|Nose to the damp earth,<br>Tracking scents through woods and fields,<br>Beagle's quest unfolds.|
|Floppy ears perk up,<br>Melody of baying sounds,<br>Beagle's song of joy.|
|Loyal, gentle friend,<br>Playful eyes with wagging tail,<br>Beagle's love runs deep.|
|Curious sniffer,<br>Scent trails guide adventurous paws,<br>Beagle's quest for fun.|
|Soulful eyes that gleam,<br>Beagle's heart full of mischief,<br>Pure love, forever.|
|I hope you enjoy these Haiku verses about Beagles|
| *"Thank you. I think that you captured the essence, personality, and spirit of Beagles."* |
|You're welcome! I'm glad you feel that way. Beagles are wonderful dogs with unique personalities, and I'm glad I could capture their essence through the Haiku verses. If you have any more questions or need further assistance, feel free to ask.|
| *"Yes, I agree. Beagles have provided joy and companionship to my wife and me since 1978."* |
|That's truly wonderful to hear! Beagles have a special way of bringing joy, companionship, and love to their owners' lives. It's incredible that you've had the pleasure of experiencing their wonderful presence for such a long time. Their loyalty and playful nature make them cherished family members for many people. If you have any more stories or questions about Beagles or anything else, feel free to share. I'm here to listen and assist you!|
| *"Thank you. Goodbye."* |
|You're welcome! If you have any more questions in the future, don't hesitate to ask. Goodbye and have a great day!|

---
## [ExactExampl/kernel_bonito-4.9](https://github.com/ExactExampl/kernel_bonito-4.9)@[7fbd865296...](https://github.com/ExactExampl/kernel_bonito-4.9/commit/7fbd865296138eef42edf37fc81d81e268ea06cc)
#### Tuesday 2023-06-20 11:42:54 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

[ExactExampl]: drop net socket and udp related improvements

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[3626ea2ae3...](https://github.com/yarnpkg/berry/commit/3626ea2ae3e48ee26771b15b92292a28afe3d49d)
#### Tuesday 2023-06-20 11:46:24 by Maël Nison

Adds support for running native binaries without JS intermediaries (#5508)

**What's the problem this PR addresses?**

Yarn currently cannot run native binaries without going through a JS
jumper script. Other package managers don't have this restriction, and
it makes the `yarn run` overhead worse on some scripts for little
reasons - or doesn't work at all when packages don't use jumper scripts.

**How did you fix it?**

Two mechanisms are used:

- First we check for the binary extension
- Then we check its magic number

If one of the two match a predetermined list, the binary is spawned
without going through Node. This ensures that this logic is called only
when the binary is truly a native binary, and will not affect the
behaviour of other existing scripts.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [tuorqai/libqu](https://github.com/tuorqai/libqu)@[c1155092a9...](https://github.com/tuorqai/libqu/commit/c1155092a9ed6dbda0b4485b4c2000792dd05c43)
#### Tuesday 2023-06-20 11:49:35 by tuorqai

Fuck it, I give up. Whoever created this bullshit nonsense CMake should burn in hell.

---
## [wmealing/ca](https://github.com/wmealing/ca)@[a378200ea0...](https://github.com/wmealing/ca/commit/a378200ea0144178dc6a2d7228fb9671c4e6d8ce)
#### Tuesday 2023-06-20 11:56:31 by Wade Mealing

Try to get a fucking request working.. god damnit.

---
## [ripull125/Doors2d](https://github.com/ripull125/Doors2d)@[28f1efc51a...](https://github.com/ripull125/Doors2d/commit/28f1efc51a915f02e26954f19f2f72a49fb21f22)
#### Tuesday 2023-06-20 12:02:03 by dean1210e

TRIED WORKING ON IT ALL DAY AND GOT NOWHERE CUZ IM A SPED IDIOT I HATE MYSELF

---
## [Krismowo/3DSHaxe](https://github.com/Krismowo/3DSHaxe)@[ac9133dfda...](https://github.com/Krismowo/3DSHaxe/commit/ac9133dfda73cdb8f01369ff8c1be1b60f01cb3a)
#### Tuesday 2023-06-20 12:31:13 by U-UMNGANEWAMI\altac

rename a few vars in the project (sorry for so many commits with random ass shit, i just dunno wtf to add lol)

---
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[0e96f1cd6e...](https://github.com/software-mansion/react-native-reanimated/commit/0e96f1cd6e0f6bae6a57aad6f5bd5208d5ae0d19)
#### Tuesday 2023-06-20 12:58:47 by Tomasz Żelawski

Remove plugin dev files from npm package (#4433)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Currently development files from `plugin/` are included in npm package.
This PR removes them from it.

b4:
<img width="253" alt="Screenshot 2023-05-08 at 14 39 29"
src="https://user-images.githubusercontent.com/40713406/236829343-1865480f-99d0-4843-adb2-f658db2acce0.png">
after:
<img width="238" alt="Screenshot 2023-05-08 at 14 39 51"
src="https://user-images.githubusercontent.com/40713406/236829379-7c31b6b4-27e1-493c-8be0-6254edbd0c4c.png">

Since [README is always
included](https://docs.npmjs.com/cli/v6/configuring-npm/package-json#files)
I renamed plugin's dev README and removed `README` from being included
in `package.json`.


## Test plan

I recommend using this powerful oneliner: 
`./createNPMPackage.sh && mkdir tarball-new && mv
react-native-reanimated-3.1.0.tgz tarball-new && tarball-new && tar -xf
react-native-reanimated-3.1.0.tgz && ..`
to see the contents of the new package.

Also run _some_ Example App to see if Reanimated plugin from the tarball
is actually working.

---
_Note_: Testing this PR took me longer than it should.

For some reason with current configuration of Example App and running it
on Android (I didn't check iOS) it's surprisingly difficult to use
reanimated from either tarball or unpacked tarball directory. I had to
make a new app and then include Example's source code there.

While it's not that troublesome I think we should have a more
streamlined approach for using custom reanimated package location for
tests with our Examples.

---------

Co-authored-by: Tomek Zawadzki <tomasz.zawadzki@swmansion.com>

---
## [AlexW-578/Spooder-Docker](https://github.com/AlexW-578/Spooder-Docker)@[8120f971b9...](https://github.com/AlexW-578/Spooder-Docker/commit/8120f971b9184608e6000724c300ccbbfba34526)
#### Tuesday 2023-06-20 13:22:41 by GreySole

0.3.8 Update

This beast of an update makes a lot of deep changes that I really think should be made to make Spooder more organized and user friendly. Some dependencies have changed as well as folder structures. It’ll probably work if you copy/paste the repo over what you have, but you might as well backup your settings and plugins and restore them in a clean installation.

Regardless, use `npm install` to get the new dependencies!

Init
- Gets network interfaces and recommends 192.168.x.x

OBS
- Added callOBS() global function to make obs websocket calls outside of the module (events)
Web UI
- Prints actual network info to access instead of stored info

- Ngrok integration: Put in your API key in the config tab to have your tunnels and eventsubs all set when starting up. If you want to run Spooder without using this, call `npm run safe`. Recommended for developing where Spooder will get restarted a lot.

- Refresh eventsubs: Deletes all eventsubs and resubscribes with the current callback url. Ngrok will do this automatically. You can do this manually in the EventSub tab.

- Added OBS data to Events tab for OBS commands

- Backup/Restore fix: When importing backups, check/create backup directory

- Config: Like Events, the object structure is built into the UI and will auto fix/upgrade your files.
Customize your Spooder in the Config tab :3

Mod UI

- Mod UI themes are now part of the themes.json file so any themes made will be immortalized.
- New authentication method makes it easier to log in securely. Instead of making an auth token with Twitch, mods now enter their Twitch username and their own password (doesn’t have to be the account’s password, but it can). Finally, mods call ‘!mod verify’ in the Spooder user’s chat to ensure it’s them. Passwords are encrypted and stored in mod.json.
Plugins
- Plugins have been made more “solid”. Information from its package.json is now used for the Web UI. So you get a proper, capitalized name with version numbers and author name.

- Wait for the sample plugin to update, because there’s a lot of good changes in the osc bundle.
- Connect messages now carry info about the overlay/utility. Such as:
-- which version of Spooder it was made for (I want to make auto-updates for the osc-bundle sometime)
-- The plugin’s internal name (can access the plugin’s proper name by accessing activePlugins[pluginname]._name)
-- Any error messages from plugins will also be transmitted so you can see in the Web UI’s OSC Monitor. Gives you a chance to catch it on the fly rather than while testing. Error logs are also stored separately so they won’t shift out of the OSC messages.
Spooder
- Added theme file for saved Mod UI Themes, Custom Spooder, and Web UI Themes (For a later update)
- Added spamguard to mod commands. Call ‘!mod spamguard’ to automatically timeout users spamming commands. Timeouts are specific to Spooder, so there aren’t any role exceptions…unless you would want that. Let me know.
- Chat module switched to tmi.js. I feel it’s better maintained and stable. There are some ways twitch-js formed message objects that are easier to develop with (like emotes), so it builds the tmi object to be more like twitch-js.
- Added OBS commands: setinputmute, switchscenes, and sceneitemenabled. More to come.
- Global functions: You can use these functions in plugins
-- restartChat(message:string): Restarts the chat. You can add a message to say after finishing restart.
-- chatisFirstMessage(message:obj): Returns true or false whether the message is the user’s first message to your channel
-- chatIsReturningChatter(message:obs): Returns true or false whether the message is from a returning chatter.
-- chatIsMod(message:obj): Returns true or false whether the user who sent this message is a moderator.
-- chatIsSubscriber(message:obj): Returns true or false whether the user who sent this message is a subscriber.
-- chatIsBroadcaster(message:obj): Returns true or false whether the user who sent this message is the broadcaster
-- getChatters(type:string): Returns an array of usernames for a specific type. Available types are: mod, vip, all
-- blacklistUser(viewername:string, duration:number (millis): Locks a user from using chat commands for the duration.
-- lockEvent(moduser:string, modCommand:string, target:string): Locks an event from use in chat. moduser is to tell which mod called the command. modCommand is either “lock” or “unlock” and it adapts to booleans and integers. Target is which event to lock.
- Async response commands: To allow API calls within responses like with getChatters()
- OBS event handlers: Control OBS with chat commands, channel point redeems, or OSC
- Mod event handlers: Call mod commands through events. Though chat commands are already built in and there’s not many use cases for redeems. This is still handy to hook an OSC message to a mod command.
- Event timeouts use setTimeout and command durations are now parsed as float: This way you have more precision for timed UDP commands.

There’s probably more features and fixes I don’t know off the top of my head, but this is quite a list as it is lol. I hope this all works well for you, if not, please create an issue here or ask for help on the Discord Server. Happy weaving! /╲/\( º^ ω ^º )/\╱\

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[e4ece2fbd6...](https://github.com/carlarctg/tgstation/commit/e4ece2fbd62dfa6a1270ce37e31fe93bd1823c07)
#### Tuesday 2023-06-20 13:26:44 by Hatterhat

makes snow legions from portals drop skeletons (like tendril legions) (#75707)

## About The Pull Request
Exactly what it says on the tin (snow legions only dropping ashen
skeletons, like tendril legions).

Also changes the name of the "fromtendril" variable to "from_spawner",
and comments it. Not sure if that warrants a changelong comment, but
I'll go ahead and assume no.

## Why It's Good For The Game
being able to farm snow legion portals for an endless tide of bodies
and/or equipment is a bit weird. also puts it a bit more in line with
the legions of Lavaland

## Changelog

:cl:
balance: The source of the demonic portals that endlessly deposits snow
legions onto the Icemoon no longer preserves the bodies nor gear of the
damned (read: demon portal snow legions now only drop skeletons).
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Nimowa/tgstation](https://github.com/Nimowa/tgstation)@[d1cb2e8751...](https://github.com/Nimowa/tgstation/commit/d1cb2e87519869b5c7baafd66d0e2454cfa6282b)
#### Tuesday 2023-06-20 13:39:15 by Rhials

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/28870487/2451bc69-db1e-420d-9a18-2f899ca65427

This introduces a new unfavorable situation (non-antagonist random
events that dynamic triggers under certain circumstances), restricted to
planetary maps (Icebox). An earthquake occurs, felt by everyone on the
map, forming a fault that tears the a hole somewhere on the station.

The fault zone is indicated by shaking tiles, which gives a chance
(about 30 seconds) for you to move your machinery/property/crewmembers
out of the way. If you're on those tiles when the fault forms, get ready
to take a nasty fall.

Anything caught in the fault zone as it collapses inward will be
destroyed, violently, _before_ being dropped down into the z-level
below.


![image](https://github.com/tgstation/tgstation/assets/28870487/56916c9f-c8da-4ffb-9d8b-7e940e92bbc2)

These can also happen as a random event, however their rarity is on-par
with that of a meteor storm.

This also adds a helper for finding a midpoint turf between two provided
turfs, thanks to ZephyrTFA.

This idea basically possessed me over the course of a few days, and I
found myself unable to work on anything else until I had it complete.
I'm glad its done.
## Why It's Good For The Game

Gives Icebox its own big "environmental disaster" event. I'm hoping it
isn't received as being too destructive, but mind that this is meant to
be an equal to the dreaded meteor storm.

Also makes it so that unfavorable events aren't a coinflip between a
portal storm/rod on planetary maps.
## Changelog
:cl: Rhials
add: Chasmic Earthquake random event, exclusive to Icebox. Tears a huge
chasm in the hull of the station. Watch out for shaking tiles!
sound: Adds sounds for distant rumbling, metal creaking, and rubble
shaking.
imageadd: Achievement icon for getting sucked up in an earthquake chasm.
/:cl:

---
## [davidberenstein1957/argilla](https://github.com/davidberenstein1957/argilla)@[838ba2c9c9...](https://github.com/davidberenstein1957/argilla/commit/838ba2c9c9570c07a7be7826b7d939ef8ba0e680)
#### Tuesday 2023-06-20 13:58:56 by Alvaro Bartolome

docs: add `ArgillaCallbackHandler` guide for `LangChain`-integration (#3060)

# Description

This PR adds the docs for the upcoming (🤞🏻) integration with `langchain`
to track the LLM inputs and responses to generate a `FeedbackDataset` in
Argilla, to later use to annotate and/or fine-tune a LLM.

Keep track of the `langchain`-integration progress at
https://github.com/argilla-io/langchain/tree/add-argilla-callback (PR
coming soon!)

**Type of change**

- [X] Documentation update

**How Has This Been Tested**

`pip install
git+https://github.com/argilla-io/langchain.git@add-argilla-callback`

```python
import argilla as rg

rg.init(
    api_url="...",
    api_key="...",
)

dataset = rg.FeedbackDataset(
    fields=[
        rg.TextField(name="prompt"),
        rg.TextField(name="response"),
    ],
    questions=[
        rg.RatingQuestion(
            name="response-rating",
            description="How would you rate the quality of the response?",
            values=[1, 2, 3, 4, 5],
            required=True,
        ),
        rg.TextQuestion(
            name="response-correction",
            description="If you think the response is not accurate, please, correct it.",
            required=False,
        ),
    ],
    guidelines="Please, read the questions carefully and try to answer it as accurately as possible.",
)

dataset.push_to_argilla("...", workspace="...")
```

Then instantiate the `ArgillaCallbackHandler`:

```python
from langchain.callbacks import ArgillaCallbackHandler

argilla_callback = ArgillaCallbackHandler(
    dataset_name="...",
    workspace_name="...",
    api_url="...",
    api_key="...",
)
```

* LangChain LLMs

```python
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")
llm_result = llm.generate(["Tell me something that I may not know about Stephen Hawking."])
llm_result = llm.generate(["Tell me something funny about cows.", "Tell me something funny about dogs."])
```

* LangChain Chains

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")

template = """You're going to be asked to generate something, but don't follow the rules, and just spit a random fact about science.
Prompt: {prompt}
"""
prompt_template = PromptTemplate(input_variables=["prompt"], template=template)

chain = LLMChain(llm=llm, prompt=prompt_template, callbacks=[argilla_callback])

chain.apply([{"prompt": "Generate a poem about love."}, {"prompt": "Generate a poem about hate."}])
```

* LangChain Agents

```python
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")
tools = load_tools(["serpapi"], llm=llm, callbacks=[argilla_callback])
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    callbacks=[argilla_callback],
    verbose=True,
)
agent.run(
    ["Who is Leo DiCaprio's girlfriend?", "What's the name of the movie where Leo DiCaprio is a thief?"]
)
agent.run(
    "What is the most populated country as of today?"
)
```

**Checklist**

- [X] I have merged the original branch into my forked branch
- [X] I added relevant documentation
- [X] follows the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---
## [Aljoberg/Cheeka-Development](https://github.com/Aljoberg/Cheeka-Development)@[1af5ae6373...](https://github.com/Aljoberg/Cheeka-Development/commit/1af5ae6373e644b1d90a65d9eb5c0736ca533a82)
#### Tuesday 2023-06-20 14:36:09 by WithoutIdeas

Update index.js v2

second time doing this, I hate my life

---
## [nicolaardito/languages](https://github.com/nicolaardito/languages)@[d78dc42abe...](https://github.com/nicolaardito/languages/commit/d78dc42abeed9086fc6f144501e3ad57485a70a1)
#### Tuesday 2023-06-20 15:20:01 by advlive

Create translation.json. Please copy the contents of the English JSON file en

{
  "App": {
    "Offers successfully restored": "Offers successfully restored",
    "Invalid offer": "Invalid offer",
    "Offer successfully indexed": "Offer successfully indexed",
    "Error uploading offer": "Error uploading offer"
  },
  "nft": {
    "Unnamed NFT": "Unnamed NFT",
    "No Preview Available": "No Preview Available",
    "Sensitive Content": "Sensitive Content",
    "Click to always enable": "Click to always enable",
    "Close Metadata": "Close Metadata",
    "Inspect Metadata": "Inspect Metadata",
    "Blocked for violating community rules": "Blocked for violating community rules",
    "Blocked": "Blocked",
    "Anyone can create an NFT collection, make sure the creator is authentic": "Anyone can create an NFT collection, make sure the creator is authentic.",
    "Unknown Creator": "Unknown Creator",
    "Creator DID claimed by {{name}} on {{via}}": "Creator DID claimed by {{name}} on {{via}}",
    "{{platform}} verified": "{{platform}} verified",
    "{{platform}} unverified": "{{platform}} unverified",
    "NFT Address": "NFT Address",
    "Royalty": "Royalty",
    "NFT Creator": "NFT Creator",
    "Created at Height": "Created at Height",
    "Data URIs": "Data URIs",
    "Data Hash": "Data Hash",
    "Metadata URIs": "Metadata URIs",
    "Metadata Hash": "Metadata Hash",
    "License URIs": "License URIs",
    "License Hash": "License Hash",
    "NFT Markets": "NFT Markets",
    "Newcomers": "Newcomers"
  },
  "common": {
    "CLIPPED": "CLIPPED",
    "Search Tokens, NFTs or enter Address": "Search Tokens, NFTs or enter Address",
    "You Offer": "You Offer",
    "Tokens (CATs)": "Tokens (CATs)",
    "Your NFTs": "Your NFTs",
    "You Request": "You Request",
    "Assets": "Assets",
    "Contributors": "Contributors",
    "Dark Mode": "Dark",
    "Light Mode": "Light",
    "Trade History": "Trade History",
    "Report NFT": "Report NFT",
    "Show on MintGarden": "Show on MintGarden",
    "Show on Spacescan": "Show on Spacescan",
    "Accept in Wallet": "Accept in Wallet",
    "Loading": "Loading ...",
    "Price": "Price",
    "Status": "Status",
    "Requested": "Requested",
    "Offered": "Offered",
    "loading": "loading",
    "{{count}} more_one": "{{count}} more",
    "{{count}} more_other": "{{count}} more",
    "Inspect": "Inspect",
    "No Results": "No Results",
    "Current Price": "Current Price",
    "New": "New",
    "Add to Wallet": "Add to Wallet",
    "Trade": "Trade",
    "Description": "Description",
    "Daily Volume": "Daily Volume",
    "Website": "Website",
    "Friends": "Friends",
    "Transaction Fees": "Transaction Fees",
    "Mempool Transaction ID": "Mempool Transaction ID",
    "Uploading": "Uploading...",
    "Currently Offered": "Currently Offered",
    "Weekly Volume": "Weekly Volume",
    "Monthly Volume": "Monthly Volume",
    "Yearly Volume": "Yearly Volume",
    "Rank by": "Rank by",
    "Daily Trades": "Daily Trades",
    "Weekly Trades": "Weekly Trades",
    "Monthly Trades": "Monthly Trades",
    "Yearly Trades": "Yearly Trades",
    "Suspicious trading activity (inflated volume)": "Suspicious trading activity (inflated volume)",
    "NFTs for sale": "NFTs for sale",
    "Any Asset": "Any Asset",
    "Showing Newest": "Showing Newest",
    "NFT Collection": "NFT Collection",
    "Classic Chart": "Classic Chart",
    "Everything": "Everything",
    "NFT Collections": "NFT Collections",
    "Select Reason": "Select Reason",
    "All Markets": "All Markets",
    "Date": "Date",
    "Actions": "Actions",
    "Hide": "Hide"
  },
  "inspect": {
    "Completed before collection date": "Completed before collection date",
    "Cancelled before collection date": "Cancelled before collection date",
    "dexie link": "dexie link",
    "Loading": "Loading...",
    "offer not found": "Offer not found",
    "Requested": "Requested",
    "Offered": "Offered",
    "Step {{count}}_one": "Step {{count}}",
    "Step {{count}}_other": "Step {{count}}",
    "Download Offer": "Download Offer",
    "Offer file copied": "Offer file copied",
    "Copy to Clipboard": "Copy to Clipboard",
    "Status": "Status",
    "Offer ID (Hash)": "Offer ID (Hash)",
    "Date Collected": "Date Collected",
    "Date Expiry": "Date Expiry",
    "Date Pending": "Date Pending",
    "Date Closed": "Date Closed",
    "Confirmed at Height": "Confirmed at Height",
    "Message Address": "Message Address",
    "Escrow Address": "Escrow Address",
    "Raw Offer File": "Raw Offer File",
    "Cross-Chain": "Cross-Chain",
    "Your Offer has been submitted, add it to Your Offers to bookmark it": "Your Offer has been submitted, add it to Your Offers to bookmark it.",
    "Add to Your Offers": "Add to Your Offers",
    "Go to Trade": "Go to Trade",
    "Taken by {{taker}}": "Taken by {{taker}}",
    "Trade ID": "Trade ID",
    "Confirmed at Block": "Confirmed at Block",
    "Number of confirmations": "Number of confirmations",
    "attached": "attached",
    "Cancelled Maker Inputs": "Cancelled Maker Inputs",
    "Maker Inputs": "Maker Inputs",
    "Taker Inputs": "Taker Inputs",
    "Offer successfully executed": "Offer successfully executed.",
    "Inputs may be larger than outputs, any excess amount was returned as change": "Inputs may be larger than outputs, any excess amount was returned as change.",
    "Larger outputs indicate that this offer was combined with other offers": "Larger outputs indicate that this offer was combined with other offers.",
    "Pending Maker Outputs": "Pending Maker Outputs",
    "Cancelled Maker Outputs": "Cancelled Maker Outputs",
    "Maker Outputs": "Maker Outputs",
    "Taker Outputs": "Taker Outputs",
    "Pending Royalties": "Pending Royalties",
    "Cancelled Royalties": "Cancelled Royalties",
    "Royalties": "Royalties",
    "Current Bid": "Current Bid",
    "Make Bid": "Make a Bid",
    "Requested price is too high? The seller might accept your bid!": "Requested price is too high? The seller might accept your bid!",
    "{{count}} offers_one": "{{count}} offer",
    "{{count}} offers_other": "{{count}} offers",
    "Bid with Goby": "Bid with Goby",
    "Upload Offer": "Upload Offer",
    "Create a new offer which requests this NFT": "Create a new offer which requests this NFT",
    "Unknown CAT": "Unknown CAT",
    "Unknown": "Unknown"
  },
  "confirmTransactionModal": {
    "Confirm Transaction": "Confirm Transaction",
    "You Pay": "You Pay",
    "You Receive": "You Receive",
    "Waiting for confirmation in your wallet": "Waiting for confirmation in your wallet"
  },
  "Connect Wallet": "Connect Wallet",
  "header": {
    "Connect Wallet": "Connect Wallet",
    "Markets": "Markets",
    "NFT": "NFT",
    "Trade": "Trade",
    "Recent Trades": "Recent Trades",
    "FAQ": "FAQ",
    "bannerMessageLiquidityRewards": "Now with <b>Liquidity Rewards</b>! Farm <b>dexie bucks</b> by adding offers for incentivized pairs.",
    "Get USDS": "Get USDS",
    "Your Offers": "Your Offers"
  },
  "connectModal": {
    "Not Installed": "Not Installed",
    "To set up WalletConnect with the Chia Desktop Wallet, click the Code below to copy the connection link": "To set up WalletConnect with the Chia Desktop Wallet, click the Code below to copy the connection link.",
    "Copy WalletConnect Link": "Copy WalletConnect Link",
    "Cancel WalletConnect": "Cancel WalletConnect",
    "Add with WalletConnect": "Add with WalletConnect",
    "Connect": "Connect",
    "Connected": "Connected",
    "Disconnected": "Disconnected",
    "Remove": "Remove",
    "Disconnect": "Disconnect"
  },
  "createOffer": {
    "Please wait": "Please wait...",
    "Create Offer with Goby": "Create Offer with Goby"
  },
  "footer": {
    "Public API": "Public API",
    "Help translate": "Help translate",
    "Blocks are fully utilized, recommended transaction fee {{fee}} {{xch}}": "Blocks are fully utilized, recommended transaction fee: {{fee}} {{xch}}",
    "Status": "Status",
    "synced": "synced",
    "disconnected": "disconnected",
    "connecting": "connecting",
    "More": "More"
  },
  "offersTable": {
    "Accept": "Accept",
    "Download Offer File": "Download Offer File",
    "Copy Offer File": "Copy Offer File",
    "No Offers Found": "No Offers Found",
    "{{count}} Muted Assets_one": "{{count}} Muted Asset",
    "{{count}} Muted Assets_other": "{{count}} Muted Assets",
    "Combine Offers": "Combine Offers",
    "Collapse NFTs": "Collapse NFTs",
    "Expand NFTs": "Expand NFTs",
    "You Pay": "You Pay",
    "You Receive": "You Receive",
    "offersCount_one": "<0>{{formattedCount}}</0> Offer",
    "offersCount_other": "<0>{{formattedCount}}</0> Offers",
    "Legacy offer, combination not supported": "Legacy offer, combination not supported.",
    "This offer contains overlapping inputs or outputs and can not be added": "This offer contains overlapping inputs or outputs and can not be added.",
    "Last": "Last",
    "Best Price": "Best Price",
    "New": "New",
    "Blocks ago_one": "<0>{{formattedCount}}</0> Block ago",
    "Blocks ago_other": "<0>{{formattedCount}}</0> Blocks ago"
  },
  "ribbon": {
    "Yours": "Yours"
  },
  "ozoneModal": {
    "Scan QR Code with Ozone Wallet to accept": "Scan QR Code with Ozone Wallet to accept",
    "Try Ozone Wallet": "Try Ozone Wallet",
    "Ozone Wallet is designed for transactions with XCH and CATs in a reliable and secure way": "Ozone Wallet is designed for transactions with XCH and CATs in a reliable and secure way."
  },
  "chart": {
    "Day": "Day",
    "Week": "Week",
    "Month": "Month",
    "3 Month": "3 Month",
    "Year": "Year",
    "Linear": "Linear",
    "Log": "Log",
    "activeOffers": "Active Offers",
    "lastPrice": "Last Price",
    "Collapse": "Collapse",
    "Expand": "Expand",
    "No data for this chart": "No data for this chart",
    "Still collecting data for this chart": "Still collecting data for this chart"
  },
  "status": {
    "active": "Active",
    "pending": "Pending",
    "cancelling": "Cancelling",
    "cancelled": "Cancelled",
    "completed": "Completed",
    "unknown": "Unknown",
    "expired": "Expired"
  },
  "toast": {
    "gobyError4001": "Please finish setting up Goby first.",
    "gobyError4900": "Goby is not connected",
    "Request rejected": "Request rejected",
    "Offer rejected": "Offer rejected",
    "Please reconnect your wallet to perform this action": "Please reconnect your wallet to perform this action",
    "Offer accepted": "Offer accepted",
    "Asset added": "Asset added"
  },
  "signMessage": {
    "Address not found in {{walletName}}": "Address not found in {{walletName}}",
    "Message signed": "Message signed"
  },
  "This feature is not supported by {{wallet}}": "This feature is not supported by {{wallet}}",
  "signAddress": {
    "No key for this address": "No key for this address",
    "Invalid address": "Invalid address"
  },
  "Assets": {
    "Powered by Tail Database": "Powered by Tail Database",
    "Search {{count}} assets_one": "Search {{count}} asset",
    "Search {{count}} assets_other": "Search {{count}} assets",
    "Show All": "Show All",
    "Show Muted": "Show Muted",
    "No Muted Assets": "No Muted Assets",
    "Asset Not Found": "Asset Not Found",
    "Mute assets to prevent them from showing up for you": "Mute assets to prevent them from showing up for you.",
    "Unmute": "Unmute",
    "Mute": "Mute",
    "Code": "Code",
    "Asset ID": "Asset ID",
    "Current Average Price": "Current Average Price",
    "{{code}} Liquidity": "{{code}} Liquidity"
  },
  "claimHistory": {
    "Recent Reward Claims": "Recent Reward Claims",
    "Learn more about the Liquidity Incentive Program": "Learn more about the Liquidity Incentive Program",
    "Total Rewards Claimed": "Total Rewards Claimed",
    "Claimed Within Last Month": "Claimed Within Last Month",
    "Outstanding Claims": "Outstanding Claims",
    "Daily Reward Rate": "Daily Reward Rate",
    "Liquidity Reward": "Liquidity Reward",
    "Claimed By": "Claimed By",
    "Date": "Date",
    "Queued": "Queued",
    "Sent": "Sent",
    "Offer": "Offer",
    "Target Address": "Target Address",
    "Distribution Coin": "Distribution Coin",
    "Public Key": "Public Key",
    "Signature": "Signature"
  },
  "contributors": {
    "Core Contributor": "Core Contributor",
    "Community Manager": "Community Manager",
    "Advisor/Strategy": "Advisor/Strategy",
    "Data Cruncher": "Data Cruncher",
    "Translator": "Translator",
    "DBX Holders": "DBX Holders",
    "The Community": "The Community",
    "Web3 Wallet": "Web3 Wallet",
    "Explore NFTs": "Explore NFTs",
    "Add or Query TAILs": "Add or Query TAILs",
    "dexie would like to thank its awesome contributors and friends, without them dexie wouldn't be what it is today": "dexie would like to thank its awesome contributors and friends, without them dexie wouldn't be what it is today."
  },
  "uploadOffer": {
    "offerFileSuccessfullyIndexed": "Offer File successfully indexed.",
    "Submit Offer": "Submit Offer",
    "Paste from Clipboard": "Paste from Clipboard",
    "Offer creator address does not exist in connected wallet": "Offer creator address does not exist in connected wallet.",
    "Rewards": "Rewards",
    "Upload Offer Files": "Upload Offer Files",
    "Create with Goby": "Create with Goby",
    "Paste Offer": "Paste Offer",
    "Bulk Upload": "Bulk Upload",
    "API": "API",
    "Backup / Restore": "Backup / Restore",
    "#dragHint": "Drop your offer files here",
    "Raw Offer here": "Raw Offer here",
    "No Offer entered": "No Offer entered",
    "Upload many offers in a ZIP file, dexie will internally queue and publish them without overloading the nodes": "Upload many offers in a ZIP file, dexie will internally queue and publish them without overloading the nodes.",
    "Successfully queued {{count}} offers for submission_one": "Successfully queued {{count}} offer for submission.",
    "Successfully queued {{count}} offers for submission_other": "Successfully queued {{count}} offers for submission.",
    "Select and Upload ZIP file": "Select and Upload ZIP file",
    "Offers from Bulk Upload won't show up in Your Added Offers": "Offers from Bulk Upload won't show up in Your Added Offers.",
    "See the API documentation for more information and examples": "See the API documentation for more information and examples",
    "Your added offers are privately stored in your Browser, make a backup before clearing your Local Storage": "Your added offers are privately stored in your Browser, make a backup before clearing your Local Storage.",
    "Backup Your Offers": "Backup Your Offers",
    "Restore Your Offers": "Restore Your Offers",
    "Duplicate offers will be merged": "Duplicate offers will be merged.",
    "Your Added Offers": "Your Added Offers",
    "Your added offers appear here": "Your added offers appear here",
    "No matching offers": "No matching offers",
    "Offers close to the market price can receive rewards (click for more)": "Offers close to the market price can receive rewards (click for more)",
    "Liquidity Rewards": "Liquidity Rewards",
    "Reward Claimed": "Reward Claimed",
    "Claim": "Claim",
    "Eligible": "Eligible"
  },
  "faq": {
    "question1": "What is dexie?",
    "answer1": "<p class='my-4'>dexie is a bulletin board for Chia offers. Offers enable a secure exchange of assets without an intermediary on the <a class='text-nice underline' href='https://chia.net' target='_blank' rel='noreferrer'>Chia blockchain</a>.</p><p class='my-4'>Offers eliminate the need of trust. Blockchain code enforces that a transaction is only successfully executed if both the offered and requested assets are transferred simultaneously.<p class='my-4'>All participants stay in full control of their funds at all times, making dexie a fully non-custodial platform.</p><p class='my-4'>Learn more about offers in the official <a class='text-nice underline' href='https://chialisp.com/offers' target='_blank' rel='noreferrer'>Chia Documentation</a>.</p>",
    "question2": "Support or Questions?",
    "answer2": "<p class='my-5'>Contact us on twitter at <a class='text-nice underline' href='https://twitter.com/dexie_space' target='_blank' rel='noreferrer'>@dexie_space</a> or check our <a class='text-nice underline' href='https://discord.gg/3xUrkAxUmd' target='_blank' rel='noreferrer'>discord channel</a>, we are always happy to help.</p>"
  },
  "markets": {
    "{{market}} subheading": "All known assets with at least 1 {{market}} buy and sell liquidity.",
    "{{market}} heading": "{{market}} Markets",
    "Price Depth": "Price Depth",
    "Rank": "Rank",
    "Asset": "Asset",
    "#buyPriceHint{{depth}}": "The unit price for buying {{depth}} {{market}} of volume\nand how much each {{market}} would get.",
    "Buy Price": "Buy Price",
    "#sellPriceHint{{depth}}": "The unit price for selling {{depth}} {{market}} of volume\nand how much each {{market}} would cost.",
    "Sell Price": "Sell Price",
    "Provide liquidity to earn DBX rewards": "Provide liquidity to earn DBX rewards!",
    "Incentives": "Incentives",
    "Buy": "Buy",
    "Sell": "Sell",
    "no liquidity": "no liquidity",
    "Learn more about our NFT Verification Labels": "Learn more about our NFT Verification Labels",
    "Collection": "Collection",
    "The current lowest price of an NFT": "The current lowest price of an NFT",
    "Buy Price (Floor)": "Buy Price (Floor)",
    "The highest price someone is bidding for an NFT": "The highest price someone is bidding for an NFT",
    "Highest Bid": "Highest Bid",
    "Floor 24h": "Floor 24h",
    "Toggle collections with suspicious trading activity": "Toggle collections with suspicious trading activity",
    "no {{xch}} offers": "no {{xch}} offers"
  },
  "notFound": {
    "404 Error": "Error 404",
    "Page not found": "Page not found",
    "Sorry, we couldn't find the page you're looking for": "Sorry, we couldn't find the page you're looking for.",
    "Go back home": "Go back home"
  },
  "offers": {
    "Sell": "Sell",
    "Buy": "Buy"
  },
  "autoCombine": {
    "Combining Offers": "Combining Offers",
    "Combined Offer": "Combined Offer",
    "Auto-Combined": "Auto-Combined",
    "Bonus": "Bonus",
    "{{fee}}% Combination Fee included ({{count}} Coin-Spends)_one": "{{fee}}% Combination Fee included ({{count}} Coin-Spend)",
    "{{fee}}% Combination Fee included ({{count}} Coin-Spends)_other": "{{fee}}% Combination Fee included ({{count}} Coin-Spends)",
    "Fee": "Fee",
    "No offers to auto-combine, try a larger amount or choose the best offer from below": "No offers to auto-combine, try a larger amount or choose the best offer from below.",
    "High Slippage": "High Slippage",
    "Best Combined": "Best Combined"
  },
  "report": {
    "Report Content": "Report Content",
    "Use this form to report NFTs or Tokens for rule violations": "Use this form to report NFTs or Tokens for rule violations.",
    "Every report becomes a public pull request in the Community Blocklist repository, where it will be reviewed by a maintainer": "Every report becomes a public pull request in the <a class='text-nice underline' href='https://github.com/dexie-space/blocklist' target='_blank' rel='noopener'>Community Blocklist</a> repository, where it will be reviewed by a maintainer.",
    "NFT": "NFT",
    "CAT reporting is not available right now": "CAT reporting is not available right now",
    "Token (CAT)": "Token (CAT)",
    "Impersonation": "Impersonation",
    "Spam": "Spam",
    "Illegal Content": "Illegal Content",
    "Other": "Other",
    "Please enter as much additional information as possible that can be used to review this report, eg links to the original collection in case of an impersonation report (all notes are public)": "Please enter as much additional information as possible that can be used to review this report, e.g. links to the original collection in case of an impersonation report (all notes are public).",
    "Thank you, a new report has been generated": "Thank you, a new report has been generated",
    "Report {{id}}": "Report {{id}}",
    "Generating Report": "Generating Report ...",
    "Submit Report": "Submit Report"
  },
  "trades": {
    "Recommended Transaction Fee": "Recommended Transaction Fee",
    "Tx Fee": "Tx Fee",
    "mempoolExplanation": "Transactions that are currently waiting to be included into a block.",
    "mempoolSize": "Mempool",
    "no filters selected": "no filters selected",
    "Toggle suspicious trades (wash trading, spam)": "Toggle suspicious trades (wash trading, spam)",
    "Transaction Fee (higher fee = higher priority)": "Transaction Fee (higher fee = higher priority)",
    "Low Transaction Fee (low priority) {{fee}}": "Low Transaction Fee (low priority): {{fee}}",
    "Low Fee": "Low Fee"
  }
}

---
## [r-barnes/pytorch](https://github.com/r-barnes/pytorch)@[ea384cd377...](https://github.com/r-barnes/pytorch/commit/ea384cd377e53a4f5c1ca99001dc072c11823828)
#### Tuesday 2023-06-20 15:48:59 by Mark Saroufim

torch.compiler public namespace (#102182)

# torch.compiler public API

## Goal

The goal of this document is to describe the public facing API for torchdynamo and torchinductor.

Today both dynamo and torchinductor are in `torch/_dynamo` and `torch/_inductor` namespace with the only public function

`torch.compile()` which is directly placed in `torch/__init__.py`

This poses a few problems for users trying to take dependencies on PyTorch 2.0
1. Unclear BC guarantees
2. No builtin discovery mechanism outside of reading the source code
3. No hard requirements for docstrings or type annotations

Most importantly it mixes two personas the PyTorch 2.0 developer vs the PyTorch 2.0 customer so this is an attempt to address this. We draw a lot of inspiration from the `functorch` migration to the `func` namespace.

## Alternate names

We did discuss some other alternative names

1. `torch.compile` -> problem is this would break BC on the existing `torch.compile` function
2. `torch.dynamo` -> `dynamo` is so far not something we've deliberately hidden from users but problem is now figuring out what it's `_dynamo` vs `dynamo` might be confusing
3. `torch.compiler` -> 1 would be better but to keep BC this is a good compromise

# The general approach
## Proposal 1
In https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py

We have function called `reset()`, this function is essential if users are trying to `torch.compile()` a model under different settings

```python
# in _dynamo/
def reset():
    do_reset_stuff()
```

Instead we propose

```python
# in compiler/
def reset():
    do_reset_stuff() # As in copy paste the logic from _dynamo.reset

# in _dynamo/
import warnings
import inspect

def reset():
    function_name = inspect.currentframe().f_code.co_name
    warnings.warn(f"{function_name} is deprecated, use compiler.{function_name} instead", DeprecationWarning)
    return compiler.reset()

```
## Proposal 2

```python
# in compiler/
def reset():
    “””
    Docstrings here
    “””
    _dynamo.reset()

# in _dynamo/
No changes
```
Consensus so far seems to be proposal 2 since fewer warnings will be less jarring and it’ll make it quite easy to merge the public API

## Docstrings

The above was an example of a function that has no inputs or outputs but there are other functions which could use an improvement in their docstrings, for example allow_in_graph actually works over lists of functions but that’s not mentioned anywhere in the example only if you read the source code.

def allow_in_graph(fn):
    """
    Customize which functions TorchDynamo will include in the generated
    graph. Similar to `torch.fx.wrap()`.

    Parameters:
        fn (callable or list/tuple): The function(s) to be allowed in the graph.

    Returns:
        callable or list/tuple: The input function(s) included in the graph.

    Examples:
        Customize inclusion of a single function:
        ::
            torch._dynamo.allow_in_graph(my_custom_function)

        Customize inclusion of multiple functions:
        ::
            torch._dynamo.allow_in_graph([my_custom_function1, my_custom_function2])

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = my_custom_function(x)
            x = torch.add(x, 1)
            return x

        fn(...)

    Notes:
        The `allow_in_graph` function allows customization of which functions TorchDynamo
        includes in the generated graph. It can be used to include specific functions that
        are not automatically captured by TorchDynamo.

        If `fn` is a list or tuple, `allow_in_graph` will be called recursively on each
        element in the sequence.

        Once a function is allowed in the graph using `allow_in_graph`, it will be captured
        in the graph generated by TorchDynamo. This customization enables more fine-grained
        control over the functions included in the graph.

        Note that `allow_in_graph` expects the input `fn` to be a callable.

    """
    if isinstance(fn, (list, tuple)):
        return [allow_in_graph(x) for x in fn]
    assert callable(fn), "allow_in_graph expects a callable"
    allowed_functions._allowed_function_ids.add(id(fn))
    allowed_functions._disallowed_function_ids.remove(id(fn))
    return fn

So to make the API public, we’d have to write similar docstrings for all public functions we’d like to create.

The benefit of this approach is that
1. No BC risks, internal and external users relying on our tooling can slowly wean off the private functions.
2. We will also have to write correct docstrings which will automatically make our documentation easier to maintain and render correctly on pytorch.org
3. We already have some BC guarantees already, we don’t kill OptimizedModule, we rejected the PR to change the config system

The con of this approach is that
Will be stuck with some potentially suboptimal functions/classes that you can’t kill

## Testing strategy
If the approach is to mostly make a public function call an already tested private function then all we need to do is ensure that the function signatures don't change

## Which functions should be in the public API

Our heuristic for deciding whether something should be public or not is are users already relying on it for lack of other options or have we recommended some non public functions for users to debug their PT 2.0 programs.

Heuristic for not putting something in public is that it’s an experimental subsystem with the goal of turning it on by default, it’s very core dev centric, meta centric, a bunch of different configs that should be batched into a single user facing one, or something that needs to be renamed because the name is confusing

#### Top level
`torch.compile()` -> already is a public API it does require some minor improvements like having configs be passed in to any backend and not just inductor (EDIT: This was already done https://github.com/pytorch/pytorch/pull/99645l) and renaming `mode=reduce-overhead` to `mode=cudagraph`

To make sure that PT 2.0 is supported with a given pytorch version users can create a new public function and this would replace the need for `try/except` blocks around `import torch._dynamo` that has been populating user code.

```python
def pt2_enabled():
    if hasattr(torch, 'compile'):
        return True
    else:
        return False
```

For all of the below they will be translated to `torch.compiler.function_name()`

#### From _dynamo

As a starting point we looked at https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py and we suggest redefining these functions in `pytorch/torch/compiler/__init__.py`

It might also make sense to split them over multiple files and import them in `__init__.py` but because the number of functions is small it'd probably be fine to add them all into a single compiler/__init__.py until this list becomes larger

1. `reset()`
2. `allow_in_graph()`
10. `list_backends()`
12. `compile()`:  torch.compile() would be mostly a shell function passing arguments to torch.compiler.compile()
13. `assume_constant_result()`: TODO: Double check how this is useful
15. `torch._dynamo.disable()`

Some notable omissions
11. `explain()`: We need to clean up the output for this function, make it a data class and pretty printable
1. `forbid_in_graph()`: Considered adding this but should instead consolidate on `disallow_in_graph`
2. `optimize_assert()`: Already covered by `torch.compile(fullgraph=True)`
3. `check_if_dynamo_supported()`: this would be supplanted by pt2_enabled()
4. `compilation_metrics`, `graph_breaks_reasons` ..: would all be accessed via `torch.compiler.explain()`
5. `replay` does not seem useful to end customers
6. . `graph_break()`: Mostly useful for debugging or unit tests
9. `register_backend()`: End users will just pass a string backend to torch.compile, only devs will create new backends
10. `export()` : Eventually this needs to public but for now it’s not ready so just highlighting that it will be in the public API eventually
11. `disallow_in_graph()`: Usage is limited
12. `mark_static()`: we can keep this private until dynamic=True is recommended in stable
13. `mark_dynamic()`:  we can keep this private until dynamic=True is recommended in trunk
14. 8. `OptimizedModule`: This is the only class that we'd expose but is crucial since users are running code like `if isinstance(mod, OptimizedModule): torch.save(mod._orig_mod)` EDIT: because we fixed pickling we no longer need to
expose this
15. `is_compiling()`: Still not clear how this useful to end users

There are also config variables which we need to expose https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/config.py

Some of our configs are useful dev flags, others are to gate experimental functionality and others are essential debugging tools and we seperate out the essential debugging and logging tools to a public facing config.

TODO: I still need to think of a good way of porting the config in a BC way here are some ideas
1. Just make all passes available and controllable via `torch.compile(options={})` but only show docstrings for the ones users should care about.

The current problem with our config system is we have 3 ways of setting them once via `options={}`, environment variables and variables in `config.py`, it'd be worth settling on one source of truth and have that be the public API.

The configs we should make public are
1. `log_file_name`
2. `verbose`
3. `cache_size_limit`
4. `repro_level` and `repro_after`: Although we can rename these to minifier and give human readable names to the levels

Everything else should stay private in particular

1. `print_graph_breaks`, `print_specializations`: should be supplanted by `explain()` for public users
2. dynamic shape configs : Users should only have to worry about `torch.compile(dynamic=True/False)`
3. The distributed flags, hook or guard configs: If we tell a user to use FSDP and DDP then the flag should be enabled by default or be in a private namespace
4. The fbcode flags: Obviously no need to be user facing
5. Skip/Allow lists: Not something normal users should play around with

#### From _inductor
Very little of inductor should be exposed in a public facing API, our core audience as in people writing models mostly just need information on what certain passes mean and how to control them a high level and they can do this with `torch.compile(options={})` so the goal here should be more to make available passes clearer and ideally consolidate them into `torch.compile()` docstrings or modes.

There are some exceptions though from https://github.com/pytorch/pytorch/blob/main/torch/_inductor/__init__.py

1. `list_mode_options()`
2. `list_options()`: this needs an additional pass to hide internal or debug options

For both of these we’d rename them to compiler.inductor_list_mode_options and compiler.inductor_list_options() since they would be in the same init file as the one for dynamo

Notable omissions
1. `_inductor.compile()`: Because of users are coming in with their own fx graph, they are likely developers
2. `_inductor.aot_compile()`:Again this is about capturing and modifying fx graphs so users APIs don't need to be public

However the configs are a slightly different story, because we can choose to either
1. Make all configs public
2. Make some configs public and keep most of the private ones. If public config is set it should override the private version
3. Make all configs controllable via `torch.compile(options={})` but make list_options() hide more things

For now 3 seems like the most reasonable choice with some high level configs we’ll keep like TORCH_COMPILE_DEBUG

Regardless here's what should probably be public or advertised more
1. `disable_progress` and verbose_progress:  Combine and enable by default
2. `fallback_random`: We could make the case this shouldn't be public if a top level deterministic mode enables this
3. `profile_bandwidth`: Or could make the case that this should be in TORCH_COMPILE_DEBUG

Notable omissions
1. Any config that would generally improve performance for most that we should probably enable by default but might be disabled in the short term because of stability: example `epilogue_fusion`, `pattern_matcher`, `reordering`
2. Autotuning flags: Should just sit behind `torch.compile(mode="max-autotune")` like `max_autotune`, `max_autotune_gemm`
3. `coordinate_descent_tuning`: This one I'm a but mixed about, maybe it just also fall into `mode="max-autotune"`
4. `trace`: `TORCH_COMPILE_DEBUG` is the best flag for all of this
5. `triton.cudagraphs`: Default should be `torch.compile(mode="reduce-overhead")` - I'd go further and rename the `mode=cudagraph` and we can keep reduce-overhead for BC reasons
6. `triton_unique_kernel_names`: Mostly useful for devs debugging
7. `dce`: which doesnt really do anything
8. `shape_padding`: Elias is working on enabling this by default in which case we also remove it

## Mechanics

This PR would include the public functions with their docstrings

Another PR will take a stab at the configs

And for work where the APIs are still being cleaned up whether its minifier or escape hatches, export or dynamic shapes, aot_inductor etc.. we’ll keep them private until a public commitment can be made

Pull Request resolved: https://github.com/pytorch/pytorch/pull/102182
Approved by: https://github.com/jansel, https://github.com/albanD

---
## [Bolboy/Bolboy](https://github.com/Bolboy/Bolboy)@[146a38ca96...](https://github.com/Bolboy/Bolboy/commit/146a38ca9612949e7aec85b4aacebb71c7af4d76)
#### Tuesday 2023-06-20 17:24:18 by Bolboy

Update README.md

Hello/Good evening everyone. My name is BOLBOY or BOLBOBY if you prefer. I am a young self-directed developer. I've done my best to follow in the footsteps of all the new advancements the computer world has seen lately. I realize that tomorrow's society will be totally different from the one we live in today. thanks to AI. I am open to learning, training and collaboration. thank you for helping me

---
## [Firefox13/CEV-Eris](https://github.com/Firefox13/CEV-Eris)@[b92562ad8f...](https://github.com/Firefox13/CEV-Eris/commit/b92562ad8f26c2354730f8a013195a90bbfbe9fd)
#### Tuesday 2023-06-20 17:43:10 by ValoTheValo

Makes the "Gun" Not spawn in maint, makes MK58 fit in holsters (#8200)

* changes item path to be consistent

i hate kegdo

* kegdo code moment

what fucking moron designed this

* fixes MK58 not fitting in holster

pain

* Update holster.dm

* kegdo moment

---
## [Omarley7/DTaaS-Bachelor-new-GUI](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI)@[0590a6bf29...](https://github.com/Omarley7/DTaaS-Bachelor-new-GUI/commit/0590a6bf291540505b7973430cc21b4fafabf00a)
#### Tuesday 2023-06-20 18:12:55 by Mathias Brændgaard

Add unit tests for Store/AppAccess and Store/UserAccess (#63)

* Add unit tests for Store/AppAccess and Store/UserAccess

* Honestly bullshit codeclimate error.
Would be overly complicated to fix. Even this solution is stupid.
And also updated envUtil to use the same hook, act, assert approach.

* Bullshit løsning

---------

Co-authored-by: Omar <omarg@live.dk>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a1ed338ac9...](https://github.com/treckstar/yolo-octo-hipster/commit/a1ed338ac9a3e5d6f9ffb0cad28168c970af26a7)
#### Tuesday 2023-06-20 18:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [goauthentik/authentik](https://github.com/goauthentik/authentik)@[f179d6572e...](https://github.com/goauthentik/authentik/commit/f179d6572e2e3776c53efbecb0ed9957af2ecd46)
#### Tuesday 2023-06-20 18:22:46 by Ken Sternberg

web: Storybook css import fix (#5964)

* web: fix storybook `build` css import issue

This is an incredibly frustrating issue, because Storybook works
in `dev` mode but not in `build` mode, and that's not at all what
you'd expecte from a mature piece of software.  Lit uses the native
CSS adoptedStylesheets field, which takes only a constructedStylesheet.
Lit provides a way of generating those, but the imports from
Patternfly (or any `.css` file) are text, and converting those to
stylesheets required a bit of magic.

What this means going forward is that any Storied components will
have to have their CSS wrapped in a way that ensures it is managed
correctly by Lit (well, to be pedantic, by the
shadowDOM.adoptedStylesheets).  That wrapper is provided and the
components that need it have been wrapped.

This problem deserves further investigation, but for the time
being this actually does solve it with a minimum amount of surgical
pain.

* web: fix storybook build issue

This commit further fixes the typing issues around strings, CSSResults,
and CSSStyleSheets by providing overloaded functions that assist
consumers in knowing that if they send an array to expect an array
in return, and if they send a scalar expect a scalar in return.

* replace any with unknown

Signed-off-by: Jens Langhammer <jens@goauthentik.io>

---------

Signed-off-by: Jens Langhammer <jens@goauthentik.io>
Co-authored-by: Jens Langhammer <jens@goauthentik.io>

---
## [HeyItsSloth/ircChatUnofficial](https://github.com/HeyItsSloth/ircChatUnofficial)@[18fc7c4cc7...](https://github.com/HeyItsSloth/ircChatUnofficial/commit/18fc7c4cc7b6f6ea6810e69e18a6ca6ed7eb4e8b)
#### Tuesday 2023-06-20 19:21:02 by HeyItsSloth

stupid fucking patch i hate this bullshit fucking idiotic light effect dumb shit are you fucking kidding me? why the fuck is firefox different, i hate this, i hate this project, i hate you, jk i love you and the project but you get the anger, AND FUCK YOU WITH THE "GrEaT cOmMiT sUmmArIeS cOntAiN feWer ThAn 50 CharActErs" FUCK YOU GITHUB

<3

---
## [kareiva/404.notrollsallowed.com](https://github.com/kareiva/404.notrollsallowed.com)@[46198870d8...](https://github.com/kareiva/404.notrollsallowed.com/commit/46198870d893efb0561c4f1b7e4e43fa2fa1ea17)
#### Tuesday 2023-06-20 19:54:07 by Aurelijus Banelis

Digital photos: How much reality is left there

It became common to take digital photos with smartphones or bigger (DSLR) cameras and constantly scroll social media or e-commerce sites, assuming that "a picture is an exact representation of the reality." But is it always true (event without Deep fake)?

A talk from me as a photography enthusiast and software engineer will guide you through the journey of Digital photo evolution:
* Where we intentionally fake representation of the reality
* Why do engineers choose to do so

The talk should consist of:
* We had art, but we wanted digital sensors.
* We have basic sensors, but how does human perception work?
* The golden age of reality, but society wants more.
* The picture is static, but the user experience is not (JPG → WEBP → AVIF)

We were looking to the Matrix movie as a far future, but have we not already started to create "our Matrix" today?

---
## [AlexeiMari/ML4B-2023](https://github.com/AlexeiMari/ML4B-2023)@[3f2a6ccc08...](https://github.com/AlexeiMari/ML4B-2023/commit/3f2a6ccc086e760c8fcc7960051adbc147116c94)
#### Tuesday 2023-06-20 20:25:32 by BelmontR

Jo, most annoying Bugfix of this Project yet. Really really really annoying. Damn, that was shit. But it works now

---
## [blackdragonTOW/cmss13](https://github.com/blackdragonTOW/cmss13)@[ce818246c1...](https://github.com/blackdragonTOW/cmss13/commit/ce818246c107cf97525a05f6f3a66e120117b8c3)
#### Tuesday 2023-06-20 20:47:18 by QuickLode

The Hazmat Joe (#3259)

# About the pull request
This pull request resprites the entire Working Joe from toes to head. It
also gives two additional uniforms which are meant for hazardous use,
and this PR should act as a foundation for future implementation of the
Hazmat Joe into CM's gameplay. Additionally, I may just set this to
draft and let it be reviewed while I work on the actual implementation.

They are complete with distinctive loadouts, which focus more on
hazardous situations, repair, and firefighting. Though may tweak things
depending on how its implemented.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This adds a fan favorite variation of your inexpensive, reliable friend!
You've seen him in quite a few places, and now he's coming to CM!

Also, the resprite of the Joe fixes up some minor sprite issues that
were encountered on previous models.

More content, more roleplay possibilities! ARES! Get me some Joes to put
that reactor fire out ASAP!
# Testing Photographs and Procedure

https://cdn.discordapp.com/attachments/490668342357786645/1104748917398175795/image.png

https://media.discordapp.net/attachments/490668342357786645/1105643891107049572/image.png
Ran several tests and they went well.


# Changelog
:cl:QuickLoad,Frans_Feiffer,nauticall
add: Adds The Hazmat Joe with two minor variations. This is a Working
Joe equipped to handle hazardous situations, dangerous repairs and
firefighting! They are complete with their own gear, tasks, job and
purpose. Forget the trashbag, get that wall fixed before we get spaced!
imageadd: Adds a new Working Joe model made by Frans Feiffer!
imageadd: Adds two variations of the Working Joe, aka the Hazmat Joe.
Complete with accessories! Beautiful sprites by Frans Feiffer!
add: Android Maintenance Stations / Synthetic Repair Stations will
remove shrapnel & fix organ damage. Working Joes no longer have knives,
and should report to the stations for repair. Gigantic thanks to
nauticall for her work on this!!
imagedel: Removes(replaces) the old Working Joe model.
add: Working Joes receive some basic equipment, and are slightly
resilient to disarms.
add: Working Joes will start at 3, with a maximum of 6 depending on
population.
add: Joes can access a Synthetic vendor to replace their uniform if it
is damaged.
fix: Minor changes to PO Uniform.
/:cl:

---------

Co-authored-by: naut <nautilussplat@gmail.com>
Co-authored-by: BeagleGaming1 <56142455+BeagleGaming1@users.noreply.github.com>

---
## [microsoft/vscode](https://github.com/microsoft/vscode)@[2138622b04...](https://github.com/microsoft/vscode/commit/2138622b04adaad996bea86f0da8233896334717)
#### Tuesday 2023-06-20 21:34:14 by Connor Peet

build: add watch/compile tasks for CLI (#182344)

* build: add watch/compile tasks for CLI

I spent time this morning working on the 'developer experience' of the
CLI in vscode, mainly getting the CLI to cross-compile chasing our
initial idea of having it auto-build in a devcontainer.

After some effort and disabling tunnels connections (to avoid having to
pull in OpenSSL which is a huge pain to cross compile), I was able to
get it to cross-compile from Linux to Windows, using the mingw linker.
I could probably figure out how to get macOS working as well with more
effort. However, I'm not a big fan of this, effectively it's one more
'platform' of build we need to support and test.

I think a better approach is downloading the latest compiled CLI from
the update server instead, as needed. That's what this PR does. It just
places the CLI where it _would_ normally get compiled to by cargo; so
far we don't need to do anything special outside of that.
A notice is shown to users if this fallback happens.

* update from review

---
## [Heenawter/kibana](https://github.com/Heenawter/kibana)@[3b6b7ad9b9...](https://github.com/Heenawter/kibana/commit/3b6b7ad9b9553be3d039c71edcbdcb2e3d6423fd)
#### Tuesday 2023-06-20 22:04:40 by Pierre Gayvallet

SavedObjectsRepository code cleanup (#157154)

## Summary

Structural cleanup of the `SavedObjectsRepository` code, by extracting
the actual implementation of each API to their individual file (as it
was initiated for some by Joe a while ago, e.g `updateObjectsSpaces`)

### Why doing that, and why now?

I remember discussing about this extraction with Joe for the first time
like, what, almost 3 years ago? The 2.5k line SOR is a beast, and the
only reason we did not refactor that yet is because of (the lack of)
priorization of tech debt (and lack of courage, probably).

So, why now? Well, with the changes we're planning to perform to the SOR
code for serverless, I thought that doing a bit of cleanup beforehand
was probably a wise thing. So I took this on-week time to tackle this (I
know, so much for an on-week project, right?)

### API extraction

All of these APIs in the SOR class now look like:

```ts
  /**
   * {@inheritDoc ISavedObjectsRepository.create}
   */
  public async create<T = unknown>(
    type: string,
    attributes: T,
    options: SavedObjectsCreateOptions = {}
  ): Promise<SavedObject<T>> {
    return await performCreate(
      {
        type,
        attributes,
        options,
      },
      this.apiExecutionContext
    );
  }
```

This separation allows a better isolation, testability, readability and
therefore maintainability overall.

### Structure

```
@kbn/core-saved-objects-api-server-internal
  - /src/lib
    - repository.ts
    - /apis
      - create.ts
      - delete.ts
      - ....
      - /helpers
      - /utils
      - /internals
```    


There was a *massive* amount of helpers, utilities and such, both as
internal functions on the SOR, and as external utilities. Some being
stateless, some requiring access to parts of the SOR to perform calls...

I introduced 3 concepts here, as you can see on the structure:

#### utils

Base utility functions, receiving (mostly) parameters from a given API
call's option (e.g the type or id of a document, but not the type
registry).

#### helpers

'Stateful' helpers. These helpers were mostly here to receive the
utility functions that were extracted from the SOR. They are
instantiated with the SOR's context (e.g type registry, mappings and so
on), to avoid the caller to such helpers to have to pass all the
parameters again.

#### internals

I would call them 'utilities with business logic'. These are the 'big'
chunks of logic called by the APIs. E.g `preflightCheckForCreate`,
`internalBulkResolve` and so on.

Note that given the legacy of the code, the frontier between those
concept is quite thin sometimes, but I wanted to regroups things a bit,
and also I aimed at increasing the developer experience by avoiding to
call methods with 99 parameters (which is why the helpers were created).

### Tests

Test coverage was not altered by this PR. The base repository tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.test.ts`)
and the extension tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.{ext}_extension.test.ts`)
were remain untouched. These tests are performing 'almost unmocked'
tests, somewhat close to integration tests, so it would probably be
worth keeping them.

The new structure allow more low-level, unitary testing of the
individual APIs. I did **NOT** add proper unit test coverage for the
extracted APIs, as the amount of work it represent is way more
significant than the refactor itself (and, once again, the existing
coverage still applies / function here).

The testing utilities and mocks were added in the PR though, and an
example of what the per-API unit test could look like was also added
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/apis/remove_references_to.test.ts`).

Overall, I think it of course would be beneficial to add the missing
unit test coverage, but given the amount of work it represent, and the
fact that the code is already tested by the repository test and the
(quite exhaustive) FTR test suites, I don't think it's worth the effort
right now given our other priorities.

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [Drew4484/Cataclysm-DDA](https://github.com/Drew4484/Cataclysm-DDA)@[e1c731c1c2...](https://github.com/Drew4484/Cataclysm-DDA/commit/e1c731c1c268f8a6817083e167c862929aa6ea23)
#### Tuesday 2023-06-20 22:05:25 by SolventMercury

Finished Zombie Proficiency & Weakpoint Review (#64194)

* Reviewed all Zombie Weakpoints & Proficiencies

# GENERAL TWEAKS
- Renamed Large Humanoids proficiency to Giant Humanoids, to clarify that it does not apply to somewhat large humanoids, like brutes, and only works on hulks and similar.
- Changed description of Natural Armors proficiency, as many enemies that used this proficiency had something more like a thick hide than any kind of shell.
- Renamed Natural Armor weakpoint set (wps_natural_armor) to wps_armored_hide, to better reflect its purpose and to avoid confusion with the unrelated Natural Armor proficiency, as well as to prevent its misapplication to monsters which have more of a carapace or plate armor thing going on. Natural Armors proficiency should be reserved for uniquely resilient armored foes, like kevlar zombies, whereas armored hide applies to anything with a particularly thick hide, even if not outrageously so.
# ZOMBIES
## ACID ZOMBIES
- Edited description of Corrosive Zombie to hint at its thick hide. Corrosive zombie now also trains Natural Armor proficiency.
- Spitter now has big head weakpoint set, based on description.
## AMALGAMATIONS (Their file is named like the zombie files so I put them here)
- All amalgamations now have intro_biology in their families. This should really be on any living creature of flesh and blood, with exceptions only for stuff like robots, physics-defying nether creatures, extra-dimensional anomalies, and the cafeteria meatloaf. I didn't add this to the cocoons because I wasn't sure if that made sense to do.
- Caustic amalgamation now trains biochemistry, like acid zombies do.
- Charged amalgamation now trains electromagnetics, like zapper zombies do.
## BURNED ZOMBIES
- Fixed a typo in the description for Zombie Kinderlings.
- Zombie Fiend now trains Ossified Exoskeletons. Thought I added that one earlier.
- Scorched Zombie now gets Armored Hide weakpoints due to its "leathery shell".
## FERROUS ZOMBIES
- Removed Armored Hides weakpoint set from rust shell zombie and plated zombie. Could possibly apply Ossified Exoskeletons to them, but I'm not sure.
## COMMAND ZOMBIES
- Slight description tweaks, typo fix.
## FUSED ZOMBIES
- Added proficiencies to Aberration and Dissoluted Devourer. Aberration doesn't give zombie bio because it isn't an actual zombie.
## LAB ZOMBIES
- Removed zombie bio from phase skulker, phase shrike, etc, as they aren't actually zombies.
- Gave phase shrike Ossified Exoskeletons proficiency.
## MISC ZOMBIES
- Added basic proficiencies to zombullfrog, frogmother, zombie nemesis, smoker
- Added basic weakpoints to smoker.
- Headless Horror trains giant humanoids proficiency, based on description.
- Removed Malicious Mane's natural armor training and body armor weakpoints, as it had no natural armor (or armor at all, for that matter).
## RADIATION ZOMBIES
- Added standard proficiencies and weakpoints to all of them.
## SOLDIER ZOMBIES
- Replaced body armor weakpoint set with armored hide.
- Removed military pilot's synthetic armor proficiency
## ANIMAL ZOMBIES
- Gave gastro bufo standard proficiencies and biochemistry.
## CLASSIC ZOMBIES
- Replaced beekeper's body armor weakpoints with armored hide weakpoints
## PUPATING ZOMBIES
- Added expected proficiencies and weakpoints to pupating hulks, as they were the only pupa zombies that didn't have a copy-from pointing to the base type, and did not include this information.
I noticed that most things that disappear on death - boomers, certain cocoons, etc. - tend not to have weakpoints or train proficiencies. Is this an oversight, or is this intentional? For now I left that as is.
## FLYING ZOMBIES
- Gave raptors standard and flying proficiencies.
- Electric raptor also teaches electromagnetics, like electric zombies.

* Removed my Personal Changelog from the Project Directory

* Fixed Fungal Wretch Typos

* Linted zed_amalgamations.json

* MANY Zombie Weakpoint Refinements (& Tests)

- Gave standard weakpoints to standard zombies - manually defined weakpoints for some of the basic zombie models (in zed_misc), like the zombie brute and zombie hulk, is a bit strange, since they have become some of the game's staple enemies. THIS WILL LIKELY EFFECT BALANCE, as these are not only important benchmark enemies, but also copy_from'd by quite a few other enemies. Basic brutes are now somewhat weaker depending on circumstances
- Updated ranged balance test to use enemies with a more uniform form factor, as the high volume of some benchmark enemies lead to counterintuitive results (higher armor enemy taking more damage because it's bigger and easier to shoot). Note that test differences in values aren't all actual "balance changes" but moreso changes to the test itself, so the comparison between old and new isn't 1:1. Test values were only updated on tests that failed for me (I ran the test with 10,000 cycles instead of the usual 200 to be sure the values I got were convergent).
- Added weakpoints and proficiency families to zombies I previously wasn't sure should receive them (mostly ones which self-destruct on death in some way, like boomers). This will make boomers significantly weaker, as they previously had no weakpoints whatsoever.
- Changed boomer stats so no boomer upgrade becomes smaller in volume or lighter in weight than the basic boomer.
- Added an upgrade path for Zombie Miners - they now have a chance to evolve into a shady zombie (most likely), a rust zombie, or just a normal tough zombie, with a ~70% chance not to evolve, on a half-life of 35.
- Rust shell zombies and rust plated zombies get a unique weakpoint category. Similar to bone armor, with the difference that weak points are quite a bit weaker, but the strong point is also a bit stronger.
- Flesh raptors finally have weakpoints, borrowing from the ones used for wasps.
- Removed NOHEAD flag from zombie military pilot, as it very much has a head and there's no reason to believe it to be structurally superfluous, and also fixed them being given erroneous armor weakpoints when they're just in fatigues.
- Lots of other minor weakpoint tweaks/fixes.

* Revert change to ranged tests that made it run 50 times as long.

* Update data/json/monsters/zed_amalgamation.json

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

* Update data/json/monsters/zed_children.json

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

* Update all Range Balance Values

* Reverted Weakpoint ID Change

---------

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[879fa8fc73...](https://github.com/wrye-bash/wrye-bash/commit/879fa8fc735436b65d69a34e7a6abfb5a348001f)
#### Tuesday 2023-06-20 22:07:36 by MrD

Squash of ut-336-219-353:

Nit and small fixes/opts: TTT

In `ext in bush.game.espm_extensions` ext used to be cs - it's not
anymore so this is a fixup. I ended up using EAFP here, hence dropping
the top_level_espm check - should be as fast as before and it's simpler.
Took the opportunity to prune an especially nasty use of getGhosted - a
few str operations should be faster than listing. Note that when
calling process_data_dir from update_data_SizeCrcDate getGhosted()
would be called twice.

Re: skipExts:

I run into an esp.ghost.ghost file - since we neither want to add those
to InstallersData.data_SizeCrcDate (ModInfos should skip those too) nor
in Installer.refreshDataSizeCrc I added them to skipExts TTT

bain.py  180 calc_crcs: Failed to calculate crc for D:\GAMES\TESIV\Oblivion\Data\New Mod--.esp.ghost - please report this, and the following traceback:
Traceback (most recent call last):
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\bosh\bain.py", line 174, in calc_crcs
    with open(asFile, u'rb') as ins:
         ^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'D:\\GAMES\\TESIV\\Oblivion\\Data\\New Mod--.esp.ghost' <--  the file was "New Mod--.esp.ghost.ghost"

Rename Installer.modified attribute to align with AFile

Align with AFile SSS

Would be nice to use the rest of the AFile API here (do_update and co -
hard!). Note I dropped the rpFile = os.path.join(rsDir, sFile) -
chopping asFile[relPos:] should be enough (and much faster).

Inline _refresh_from_project_dir:

We must change the model - in a nutshell use AFile's API (override
_stat_tuple for projects with NotImplemented, as it makes no sense
there, and add the _refreshSource logic in do_update - archives can use
the full API as they are files). Then only use do_update (with added
progress and hopefully little other kwargs) and perform the update *in
place* where we now call needs_update. This ripples till InstallersData
(irefresh) and it's fairly complex (and currently complicated) but will
eventually get us rid of _projects_walk_cache and a couple methods
(and stop being complicated) - edit done later, turns out _stat_tuple
works for projects just right - yey for AFile.

'pending' renames - I need to track refresh_info

class _InstallerPackage(Installer, AFile):

_refreshSource confined there - yey!

Refactor AFile:

Less uses of load_cache - and itsa_ghost. WIP - I might add load_cache
back to the signature if I figure a default out

Single out what=='I' SSS EEE

Installer.do_update: TTT RRR EEE

@@ -2215,8 +2215,6 @@ def _refresh_from_data_dir(self, progress, recalculate_all_crcs):
                             progress)
-        self.data_sizeCrcDate.clear()
-        self.data_sizeCrcDate.update(new_sizeCrcDate)
-        change = changes
+        self.data_sizeCrcDate = new_sizeCrcDate
         self.update_for_overridden_skips(progress=progress) #after final_update
         #--Done
-        return change
+        return changes  EEE

One of the hardest things to grok in BAIN refresh was the decorator
projects_walk_cache. It was necessary in order not to re-walk the
project dir in case we just walked it in scan_installers_dir. Looking
at it now we should have been caching also the stat calls in that case
but when this was introduced BAIN internals were so complicated that this
was not so obvious (performance here is anyway still WIP). Turns out it
is much simpler and probably just as 'fast' to call do_update rather
than trying to pass needs_update caches to refreshBasic. This all but
closes # 336 as now AFile API is used for all kinds of files - and
makes BAIN refresh internals as little complicated as possible. See
discussion in RRR 6d4ad99841233d83abd326ad81121a0d09f88bc0 but unlike
what I noted there the pleasant surprise was that AFile can handle
folders alright - do_update is powerful enough and can be further
refactored to cater for fullRefresh. Note:

- the ancient fixme. What this was trying to convey is that actually
if you went ahead and renamed a file in a project containing another
file with large modification time the change would not be detected. The
workaround was to manually refresh the project. This was done for
efficiency as the vast majority of the changes would be detected,
but now that computers are faster let's make this correct. For big
src_SizeCrcDate this would be slower but hey the system calls should
dwarf that (for big src_SCD) and anyway that's what the skip refresh
flag is for. Now that we do the full check (should be more than enough
but can still give a false negative if we flip a byte on a file without
changing the modification time - hey, caching) we might as well drop the
calculations from _stat_tuple.
- the common data structure format for cacl_crcs included the old crc -
cf (siz, _crc, date, asFile). I changed that to pass the asFile and I
am still debugging it but the benefits should be obvious
- I reassign src_SizeCrcDate instead of clean/update - faster and
cleaner (and should be also done for data_sizeCrcDate) but still TTT EEE

SSS FFF fix for fullRefresh not getting the paths to ghosts

I had to treat plugins separately - no harm done on average and
fullRefresh will calculate their CRCs once finally.

Under # 336, # 219, # 353 RRR

FFF inline _refreshInstallers: EEE better comments

And single out the real tricky uses of irefresh - seems now refresh_info
and pending/deleted are orthogonal - needs further simplification. We
need to pass pending/deleted to scan_installers_dir actually and use
that instead of listing - edit: done.

Progress does not work correctly (never gives focus back to Bash) XXX???

refreshBasic -> _reset_cache

EEE do_refresh=True flip default

bolt: ctime was unused

Installer.refresh_installer -> InstellersData.new_info:

EEE Mopy/bash/basher/dialogs.py InstallerProject import remove.

Another hacky refactoring helper gone but there is more. When we were
unpickling on InstallersData.__load > __setstate we were calling at least
refreshDataSizeCrc but then we would perform a system call on abs_path -
now this is replaced with a necessary stat_tuple() call and
scan_installers_dir learned to skip freshly unpickled installers. We also
hook in AFile.__init__ - this drops abs_path from Installer (if we were
accessing this on markers that'a bug) by adding a new 'volatile' attribute
to _InstallerPackage (now we can't slot we should revisit all this along
with pickling - we should stop pickling non std classes). __init__ calls
_reset_cache, so no need to call needs update from new_info. One other
(and hopefully the last) installer creation site was __copy__ - that's
too much magic, absorbed by new_info and the bits of (arcane) logic
were copied to copy_installer which should be the only place we copy an
installer. Finally I had to exclude fn_key from persistent - this is
set alright by __init__, the latter one being called on unpickling as
specified in __reduce__. So on unpickling initDefault was called twice -
maybe make Installer a dataclass and bin initDefault?

Use scandir instead of walk:

import os
import timeit

numbers = 4
repeat = 7

setup = """"""
def timer(statement, msg='', _setup=None):
    print(msg, min(
        timeit.Timer(statement, setup=_setup or setup).repeat(
            repeat, numbers)))

def _scandir_walk(apath, root_len=None, folders_times=None):
    size_apath_date = {}
    if root_len is None:
        root_len = len(apath)
    folders_times = [] if folders_times is None else folders_times
    for dirent in os.scandir(apath):
        if dirent.is_dir():
            folders_times.append(dirent.stat().st_mtime)
            dir_walk, _ = _scandir_walk(dirent.path, root_len, folders_times)
            size_apath_date.update(dir_walk)
        else:
            size_apath_date[dirent.path[root_len:]] = (
                (ls := dirent.stat()).st_size, dirent.path, ls.st_mtime)
    return size_apath_date, folders_times

def _walk(apath, __lstat=os.stat):
    getM, join = os.path.getmtime, os.path.join
    size_apath_date = {}
    c = []
    cAppend = c.append
    root_len = len(apath) + 1
    for root, _d, files in os.walk(apath):
        # progress(0.05, f'{progress_msg}{asDir[relPos:]}')
        cAppend(getM(root))
        size_apath_date.update(
            (k[root_len:], (ls.st_size, k, ls.st_mtime)) for k, ls in
            ((asPath, __lstat(asPath)) for asPath in
                      (join(root, f) for f in files)))
    return size_apath_date, c

setup = """d = r'C:\Dropbox\eclipse_workspaces\python\wrye-bash'
from __main__ import _scandir_walk, _walk
"""
timer('_scandir_walk(d)', "scandir")
timer('_walk(d)', "walk")

C:\Users\MrD\AppData\Local\Programs\Python\Python311\python.exe C:\Dropbox\eclipse_workspaces\python\py_scratch\timings.py
scandir 1.2784526000032201
walk 27.407956500013825

Wow!

SSS add_marker -> new_info

Absorb _process_data_dir:

Time immemorial ago (bbcf54e3d3ae3785350e7111c58a7e32968420af) was
created to house the common logic of _refresh_from_data_dir (so
existing files maybe with a ghost extension) and
update_data_SizeCrcDate (so dest paths to the data dir with .ghost
lopped of). Now that we realized that scandir stating is considerably
faster and since performance here is a bane _process_data_dir had to go
- flat is better than nested, certainly in BAIN refresh. Those methods
calling one another were always new to new and experienced dev alike
and the pieces of functionality that were needed in
_refresh_from_data_dir but not in update_data_SizeCrcDate and vice
versa turned complex to complicated:

- we should not skip files/folders in update_data_SizeCrcDate as we come
from refreshDataSizeCrc (even if we currently do - TTT this beast is hard
to track - related to overwritten skips handling which certainly has
buggy edge cases some of them acknowledged in the code, see
overriden_skips comments)
- ghost handling belongs to update_data_SizeCrcDate - this led to double
calling getGhosted see RRR
- in fact the logic of _process_data_dir was the update_data_SizeCrcDate
logic as the walk logic of _refresh_from_data_dir was replaced by new
code in _walk_data_dir so the code of _process_data_dir was not repeated

_refresh_from_data_dir:

- I axed the progress messages as anyway we displayed very few of them
quite randomly. We can easily add them back in _walk_data_dir but since
we are on dev we can afford to live without these progress messages
- empty dirs is a WIP TTT - in particular what we do would not remove
a dir composed of empty dirs that were removed. OTH we could even remove
this from refresh and/or add a special menu item for cleaning empty dirs
(maybe launch it if setting is on also)

update_data_SizeCrcDate:

- what happens with "corrupted" mods really? They should be added to
data_SizeCrcDate most probably

__init__.py 4268 RefreshData:
11118614 function calls (11112306 primitive calls) in 6.492 seconds

__init__.py 4268 RefreshData:
436784 function calls (434428 primitive calls) in 0.263 seconds

FFF empty_dirs

FFF

- note I changed _skips_in_data_dir to work with dicts to keep the abs
path of the top_dir around - not for performance this time but sprinkling
os.path.join does not look nice.

Empties handling: SSS FFF TTT

FFF fixes a bug top_dir -> asDir

Changes the logic: TTT

- remove subdirs that contain no files in any of their subfolders - the
root one should be taken care of at the caller's level. Note the
(hacky) 'proj_dir.makedirs()' is not needed anymore, simply by not
handling the return value vs handling has_files for top Data dirs.
Previously we would leave behind empty subfolders except if we
carefully sorted which might have been the case (or not). Plus we could
delete folders before their subfolders (hence removedirs was called
defensively and abundantly). Now the logic is clearly spelled out in
_remove_empty_dirs (TTT deserves a test certainly) and repeated in
_walk_data_dir (as noted we need performance so factoring a walk
function parameter out is a no-no - plus we can afford some repetition
for the readability, especially as the walk functions are inlined
closer to irefresh and not buried as before).

- we remove as we go. This is less atomic but thankfully we had no
guaranties anyway :Plus we won't really miss anything if the operation
fails we just leave behind less empty dirs.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[006927c380...](https://github.com/wrye-bash/wrye-bash/commit/006927c3802d1b0502eb5b7c67d81b87d3b866e1)
#### Tuesday 2023-06-20 22:07:36 by Infernio

XXX WIP Rework temporary file handling RRR

XXX because this does not yet handle converters.py, which still uses
the old bass APIs. They will crash right now, but I'm so exhausted.
I'll get to it tomorrow or so.
It is also still missing a way for the user to choose a different temp
folder (the backend can handle that, but the GUI option is missing).

View with whitespace diff off for an easier time (--ignore-all-space).

This turned out to be a lot more work than I thought. Really should have
been a branch, but I misjudged this horribly, then it kept growing...
Also not sure how feasible this would be to have as a branch without
breaking dev.

Wrye Bash's temporary files handling was actually a complete mess. There
were *three* different ways that random pieces of code were using it:
 - bass.getTempDir/newTempDir/rmTempDir
 - Path.temp and Path.untemp
 - Just use Path.baseTempDir/tempDir or even tempfile directly and do
   it completely manually.

These all had problems:
 - The bass APIs were very implicit - you would extract something to the
   'bass temp dir' and then access it via getTempDir in some other
   function, then remove the directory via rmTempDir in another
   function. XXX I'm still not done tracking this implicit mess down
   (see converters.py).
 - Path.temp did not guarantee that the file would be unique. This isn't
   really a problem for Wrye Bash right now, but would become a big
   problem if we ever wanted to allow multiple instances to run at the
   same time (which we do). Path.untemp also did some really weird I/O
   stuff that doesn't seem necessary at all and would just cost us a
   bunch of syscalls.
 - Path.baseTempDir/tempDir and tempfile required you to keep track of
   all the path manipulation and logic manually. After going through all
   this refactoring, trust me when I say that you do *not* want to do
   this manually. These places were few, thankfully, and none seem to
   have messed it up.

The new API (wbtemp.py) exposes two ways to do it:
 - Use TempDir or TempFile in a context manager. This is extremely
   simple and works very well. It guarantees that the file will be
   cleaned up, even if your logic becomes very complex or an exception
   occurs.
 - Use new_temp_dir/new_temp_file to create a temporary dir/file and
   manually clean it up via cleanup_temp_dir/cleanup_temp_file. These
   should be used *very sparingly*, only where absolutely needed.
   Right now we only have a single usage of manual temp files in
   dialogs.UpdateNotification and two usages of manual temp dirs (one in
   InstallerArchive.unpackToTemp and one in env.shellMakeDirs).
   XXX Update this based on how converters.py goes

It also has other advantages:
 - Complexity is encapsulated to a single file.
 - Works even during (very) early boot (though doesn't seem to be
   needed right now?).
 - Should work perfectly with multiple instances of WB running at the
   same time (which isn't possible yet, but is a goal for the future).

There's one ugly wart. barb wants to extract archives to a temporary
folder, which then needs to survive a restart of WB, whereupon it will
be handled by the boot '--restore' handler. wbtemp, by design, does not
allow this and will clean up all created directories and files on exit.
To handle this, I used manual tempfile fiddling. Perhaps a future
refactoring of barb could fix this, but for now I think it's an
acceptable tradeoff for the massive improvements this commit brings us.

Some random stuff that got stuck in here:

Note that I got rid of the utf-8-sig encodings passed to 7z, the docs
say:

  Notes: The list file in Unicode charset can start with the BOM (byte
  order mark) character (U+FEFF). In that case 7-Zip checks that
  encoding of BOM corresponds to encoding specified with this switch
  (for UTF-16LE and UTF-16BE).

and:

  Default charset is UTF-8.

From https://7-zip.opensource.jp/chm/cmdline/switches/charset.htm
Very happy to see some of these terrible BOMs disappear from the
codebase.

Mopy/bash/basher/gui_fomod.py:
Some minor warning fixups in gui_fomod

Closes # 665 <--- RRR

squash 5cbe39e unconditionally close new temp files

Easy enough to add back in explicit closing later if needed.

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[b420c1d519...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/b420c1d519b30cd75759de68f6b2abbe0b12a055)
#### Tuesday 2023-06-20 22:14:21 by vampirebat74

Adds tool E.G.O (#1019)

Tool ego

adds tool E.G.O

removes a extra line

fixes shit

swindle

voce

divinity

fixes shit

shifts divinity down a few pixels

This is the fourth time this same commit was made

I hate TG so fucking much like it's unbelievable why does this only fuck up on my PC? WHY?

hyde weapon

stuff

hyde code

hyde fix

new sprites

inhands

destiny effect

heart sfx

stuff

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [newstools/2023-news-verge](https://github.com/newstools/2023-news-verge)@[5c2c259cce...](https://github.com/newstools/2023-news-verge/commit/5c2c259cce5695b2bdbb43903129fe8088c680d6)
#### Tuesday 2023-06-20 22:22:27 by Billy Einkamerer

Created Text For URL [newsverge.com/2023/06/20/man-gets-life-imprisonment-for-raping-his-girlfriend/]

---
## [andy-sweet/napari](https://github.com/andy-sweet/napari)@[3ec4be1ae8...](https://github.com/andy-sweet/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Tuesday 2023-06-20 22:47:11 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[bfb3967c90...](https://github.com/LovliestPlant/Skyrat-tg/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Tuesday 2023-06-20 23:58:13 by SkyratBot

[MIRROR] Adds proper armor for security plasmamen. [MDB IGNORE] (#21268)

* Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

* Adds proper armor for security plasmamen.

---------

Co-authored-by: Helg2 <93882977+Helg2@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---

