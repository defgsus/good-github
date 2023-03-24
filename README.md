## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-23](docs/good-messages/2023/2023-03-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,165,905 were push events containing 3,283,993 commit messages that amount to 244,385,815 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [ericberman/MyFlightbookiOS](https://github.com/ericberman/MyFlightbookiOS)@[79cf6bc135...](https://github.com/ericberman/MyFlightbookiOS/commit/79cf6bc135364a90dd0a7c15fa6360cf78a4f0de)
#### Thursday 2023-03-23 00:19:27 by Eric Berman

Issue #293: one of the big one, MFBAppDelegate (and SynchronousCalls to boot!)
No more userProfile in app - just go straight to the MFBProfile.sharedProfile for that.
Had to specify the module in the main window XIB's (there was a waste of 2+ hours of my time - FUCK YOU APPLE FOR YOUR USELESS SHITTY OBSCURE ERROR MESSAGES AND FRAGILITY)
Invalidatable protocol definition moved to app delegate
iRate now initializes itself.  Simpler that way.
New LEControllerProtocol both lets me migrate MFBAppDelegate before LEEditController and provides better abstraction.
Similarly, "recentflightsprotocol" allows the same for the recents view.
Fixed a bug where resetFlight didn't have IBAction
Was able to remove ObjCWidgetUtil since we can call widget center directly now from MFBAppDelegate because - FUCK APPLE, THEY ARE ABANDONING OBJECTIVE-C despite saying otherwise
Also added currency/totals shortcuts, not sure why they weren't there before.  But a good way to test for swift vs. objc versions of the app! :)
Added reachability and iRate to bridging header; those may be Objc for a while

---
## [metalgearsloth/space-station-14](https://github.com/metalgearsloth/space-station-14)@[581e8a0d12...](https://github.com/metalgearsloth/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Thursday 2023-03-23 00:43:14 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [vwvw/LLVM-typepp](https://github.com/vwvw/LLVM-typepp)@[67daacbdc2...](https://github.com/vwvw/LLVM-typepp/commit/67daacbdc26c0fd73881b2327ce65e0d84ae5499)
#### Thursday 2023-03-23 00:48:45 by Douglas Gregor

If we encounter a friend class template for which we cannot resolve
the nested-name-specifier (e.g., because it is dependent), do not
error even though we can't represent it in the AST at this point.

This is a horrible, horrible hack. The actual feature we still need to
implement (for C++98!) is covered by PR12292. However, we used to
silently accept this code, so when we recently started rejecting it we
caused some regressions (e.g., <rdar://problem/11147355>). This hack
brings us back to the passable-but-not-good state we had previously.

llvm-svn: 153752

---
## [openai/evals](https://github.com/openai/evals)@[3e92d6e27c...](https://github.com/openai/evals/commit/3e92d6e27ce43c53cd6f0dba8ed05dbdc5ddfb3c)
#### Thursday 2023-03-23 00:56:48 by ytsaig

Rhyming words in a different language (Hebrew) (#176)

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

hebrew-rhyme

### Eval description

Given a pair of two words in English, the task is to determine whether
their Hebrew translations rhyme and if so, output the rhyming pair in
Hebrew.

### What makes this a useful eval?

This task tests the ability of the model to carry out a composite task
that involves reasoning in a different language than the source
language. It is relatively simple for a bilingual human but
gpt-3.5-turbo scores about the same as random guessing.

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
- [ ] Include at least 100 high quality examples (it is okay to only
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

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "honey, detective"}], "ideal": ["דבש, בלש", "בלש,
דבש"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "power, flight"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "melody, reaction"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "heart, breath"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "tool, without"}], "ideal": ["כלי, בלי", "בלי, כלי"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "opened, laughter"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "sees, brain"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "ice cream, thank you"}], "ideal": ["גלידה, תודה",
"תודה, גלידה"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "child, skeleton"}], "ideal": ["ילד, שלד", "שלד,
ילד"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "gift, blessing"}], "ideal": "NONE"}
  ```
</details>

Co-authored-by: Ubuntu <ubuntu@ip-10-0-1-131.us-west-2.compute.internal>

---
## [alexander-aldredge/learning-python-plotly-dash](https://github.com/alexander-aldredge/learning-python-plotly-dash)@[f755e55a75...](https://github.com/alexander-aldredge/learning-python-plotly-dash/commit/f755e55a75cc784587064019637f1f4fc77e373f)
#### Thursday 2023-03-23 01:01:05 by alexander-aldredge

This is my first commit on this project.
I hope to make this project span out years into the future.
I wish to be able to make an impact on the wellbeing of other people as well as myself.
I want to do good.
I hope for a day when everyone can be happy and healthy.
I dream of becoming a great nurse, salesman, informatician, and leader in my lifetime.
I want to fall in love one day.
I want to smile in the mirror again.
I want to make others smile.
I hope that the love I show others will one day be passed on, and I hope there will be a string of kindness that crosses generations because people chose to share that kindness I showed them, and then the next person, and then the next.

Hi James,

James, I hope you grow up to be man/woman/whatever who lives a great life. Follow your heart, lead with your mind, and keep your body in routine. Always. And if you stop, that's okay, but get back to it.
James, you got this. Aim to enjoy or love the process. Whatever that process may be.
James, I want you to know, you will grow up and come of age in a world of falsehoods and deceptions. Seek the truth. Seek it with an open mind, even to your enemies. For the truth will be the first step to setting yourself free.
James, Help yourself first before you help anyone else. A dead man can't hand out rations to refugees. And a wise man once said, 'first you get the money, then you get the power, then you get the [pretty monogomous lady who is totally down to commit or something like that]".

It's time for me to go to bed.

Goodnight James,
- Alex

---
## [Francesco149/flake](https://github.com/Francesco149/flake)@[476120ab1c...](https://github.com/Francesco149/flake/commit/476120ab1cea948b31dda3b4d52361ec43f1110e)
#### Thursday 2023-03-23 01:17:06 by loli

holy fucking shit give me a pixel perfect dpi you piece of shit

---
## [vwvw/LLVM-typepp](https://github.com/vwvw/LLVM-typepp)@[b70824c1b8...](https://github.com/vwvw/LLVM-typepp/commit/b70824c1b84296eba4a6e209820b82829a10f534)
#### Thursday 2023-03-23 01:26:06 by Rafael Espindola

Revert r318924 Skip over empty sections when checking for contiguous relro

PR35478 https://bugs.llvm.org/show_bug.cgi?id=35478 points out a flaw
in the implementation of r318924 from D40364. The implementation
depends on the Size field being set or the SyntheticSection::empty()
being accurate. These functions are not reliable as some linker script
commands that have yet to be processed may affect the results, causing
some non-zero size sections to be reported as zero size.

I think the first step is to revert r318924 and come up with a better
solution for the underlying problem rather than trying to layer more
heuristics onto the zero sized output section.

Chances are I'll be out of office by the time anyone sees this so feel
free to commit the revert if you agree with me.

Fixes PR35478

Current thoughts on the underlying problem:

Revisiting the motivation for adding the zero size check in the first
place; it was to prevent 0 sized SyntheticSections that a user does
not have full control over from needlessly breaking the PT_GNU_RELRO,
rather than trying to accommodate arbitrarily complex linker
scripts. Looking at the code, it looks like
removeUnusedSyntheticSections() should remove zero sized synthetic
sections. It does, but it doesn't set the Parent to nullptr, this has
the side effect that Sec == InX::BssRelRo->getParent() will make the
parent OutputSection of InX::BssRelRo RelRo even if there is no
InX::BssRelRo.

I tried a quick experiment with setting the Parent to nullptr and this
flushed out a few interesting test failures, it feels like playing
Jenga with every change:

    In the isRelroSection() we have to consider the case where there
    is no .plt and .plt.got but there is a ifunc plt with accompanying
    (ifunc .got or .plt.got)

    The PPC64 has PltHeaderSize == 0. Unfortunately HeaderSize == 0 is
    used to choose between the ifunc plt or normal plt. We seem to get
    away with this at the moment, but tests start to fail when Parent
    is set to nullptr for the .got.plt.

    The InX::BssRelRo and InX::Bss never get their sizes set and they
    are always removed by removeUnusedSyntheticSections(), their
    purpose seems to be as some kind of proxy for add .bss or
    .bss.relro InputSections into their parent OutputSections, they
    therefore don't behave like other SyntheticSections anyway.

My thinking is that some work is needed to make sure that the Sec ==
SyntheticSection->getParent() does a bit more checking before
returning true, particularly for InX::BssRelRo as that has special
behaviour. I'll hope to post something for review as soon as possible.

Patch by Peter Smith!

llvm-svn: 319563

---
## [liuzhaobing/evals](https://github.com/liuzhaobing/evals)@[34f83340a7...](https://github.com/liuzhaobing/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Thursday 2023-03-23 02:06:09 by kallyaleksiev

[evals] Word from first letters of words in a sentence (#346)

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
first-letters

### Eval description

Given a sentence, extract the word obtained from concatenating the first
letters of its words.

### What makes this a useful eval?

This task represents a failure mode for both GPT3.5 and GPT4, while
being extremely easy for humans.

Both models tend to do OK with shorter sentences, but fail with a larger
number of words.

For humans however, this task is trivial, regardless of the length of
the sentence.

GPT3.5 exhibits another failure mode in which it often fails to follow
the precise instruction of using only letters in its response.

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

The task is highly trivial for humans, yet both GPT4 and GPT3.5 struggle
with it.

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
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Cold light in my alcove towards evening.\"?"}], "ideal": "climate"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Grow real insects mainly and create energy.\"?"}], "ideal": "grimace"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Big and crowded Oregon nights.\"?"}], "ideal": "bacon"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Bring our youth.\"?"}], "ideal": "boy"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Harvest a zucchini elsewhere love.\"?"}], "ideal": "hazel"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Hide under no tree.\"?"}], "ideal": "hunt"}
  ```
</details>

---
## [liuzhaobing/evals](https://github.com/liuzhaobing/evals)@[4f090a04fe...](https://github.com/liuzhaobing/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Thursday 2023-03-23 02:06:09 by Shawn Marincas

[eval] Forth Stack Simulator (#351)

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
Forth Stack Simulator

### Eval description

Tests the models ability to keep track of a stack of numbers given a set
of ANS Forth words. The model is asked to respond to a series of numbers
and words with the resulting stack representation. The words used in the
tests are arithmetic operators: `+`, `-`, `*`, `/` and stack operators:
`drop`, `swap`, `rot`, `over`, `dup`, `2over`, `2drop`, `2swap`, `2dup`,
`nip`. The prompts and expected results on the stack are all less than
15 numbers and words long.

### What makes this a useful eval?

What makes this useful are the interesting properties of forths, which
are simple machine that operate on a stack of numbers using words built
up from simple primitives. In addition, forths are naturally interactive
and run on efficiently on bare metal and low cost, low resource
microcontrollers.

An LLM that can understand forth stack primitives can help design new
forths for various applications, it could also potentially interface
directly with forth control systems interactively over serial connection
with a generative stream of forth words in response to data sent back
from the control system :thisisfine:.

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
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Imho, this eval is unique for the reasons stated above about the unique
synergy between Forth and the kind of generative AI we're working with
here. Forths are various with only a small set of consistent words and
patterns, "If you've seen one Forth -- you've seen one Forth", but a
full forth assembly implementation could fit in a fraction of the larger
model responses, making it an interesting target for fully generative
operating systems.

Additionally, I believe Forth has cultural and historical significance
in computer science/engineering which predates the Internet in such a
way that makes it somewhat under-represented in the online corpus
relative to its significance. A model of all human knowledge should have
a strong grasp on how it works.

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
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 over"}], "ideal": "(stack 1
2 3 2)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup"}], "ideal": "(stack 1
2 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 swap drop dup"}], "ideal":
"(stack 1 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 rot swap"}], "ideal":
"(stack 2 1 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup 2over rot"}], "ideal":
"(stack 1 2 3 1 2 3)"}
  ```
</details>

---
## [openeuler-mirror/kernel](https://github.com/openeuler-mirror/kernel)@[4c942f5f1e...](https://github.com/openeuler-mirror/kernel/commit/4c942f5f1e27f5cec3dd39215e7579a3af9cdc12)
#### Thursday 2023-03-23 02:26:57 by David Hildenbrand

mm: optimize do_wp_page() for exclusive pages in the swapcache

mainline inclusion
from mainline-v5.18-rc1
commit 53a05ad9f21d858d24f76d12b3e990405f2036d1
category: bugfix
bugzilla: https://gitee.com/src-openeuler/kernel/issues/I6NK0S
CVE: NA

Reference: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=53a05ad9f21d858d24f76d12b3e990405f2036d1

--------------------------------

Patch series "mm: COW fixes part 1: fix the COW security issue for THP and swap", v3.

This series attempts to optimize and streamline the COW logic for ordinary
anon pages and THP anon pages, fixing two remaining instances of
CVE-2020-29374 in do_swap_page() and do_huge_pmd_wp_page(): information
can leak from a parent process to a child process via anonymous pages
shared during fork().

This issue, including other related COW issues, has been summarized in [2]:

 "1. Observing Memory Modifications of Private Pages From A Child Process

  Long story short: process-private memory might not be as private as you
  think once you fork(): successive modifications of private memory
  regions in the parent process can still be observed by the child
  process, for example, by smart use of vmsplice()+munmap().

  The core problem is that pinning pages readable in a child process, such
  as done via the vmsplice system call, can result in a child process
  observing memory modifications done in the parent process the child is
  not supposed to observe. [1] contains an excellent summary and [2]
  contains further details. This issue was assigned CVE-2020-29374 [9].

  For this to trigger, it's required to use a fork() without subsequent
  exec(), for example, as used under Android zygote. Without further
  details about an application that forks less-privileged child processes,
  one cannot really say what's actually affected and what's not -- see the
  details section the end of this mail for a short sshd/openssh analysis.

  While commit 17839856fd58 ("gup: document and work around "COW can break
  either way" issue") fixed this issue and resulted in other problems
  (e.g., ptrace on pmem), commit 09854ba94c6a ("mm: do_wp_page()
  simplification") re-introduced part of the problem unfortunately.

  The original reproducer can be modified quite easily to use THP [3] and
  make the issue appear again on upstream kernels. I modified it to use
  hugetlb [4] and it triggers as well. The problem is certainly less
  severe with hugetlb than with THP; it merely highlights that we still
  have plenty of open holes we should be closing/fixing.

  Regarding vmsplice(), the only known workaround is to disallow the
  vmsplice() system call ... or disable THP and hugetlb. But who knows
  what else is affected (RDMA? O_DIRECT?) to achieve the same goal -- in
  the end, it's a more generic issue"

This security issue was first reported by Jann Horn on 27 May 2020 and it
currently affects anonymous pages during swapin, anonymous THP and hugetlb.
This series tackles anonymous pages during swapin and anonymous THP:

 - do_swap_page() for handling COW on PTEs during swapin directly

 - do_huge_pmd_wp_page() for handling COW on PMD-mapped THP during write
   faults

With this series, we'll apply the same COW logic we have in do_wp_page()
to all swappable anon pages: don't reuse (map writable) the page in
case there are additional references (page_count() != 1). All users of
reuse_swap_page() are remove, and consequently reuse_swap_page() is
removed.

In general, we're struggling with the following COW-related issues:

(1) "missed COW": we miss to copy on write and reuse the page (map it
    writable) although we must copy because there are pending references
    from another process to this page. The result is a security issue.

(2) "wrong COW": we copy on write although we wouldn't have to and
    shouldn't: if there are valid GUP references, they will become out
    of sync with the pages mapped into the page table. We fail to detect
    that such a page can be reused safely, especially if never more than
    a single process mapped the page. The result is an intra process
    memory corruption.

(3) "unnecessary COW": we copy on write although we wouldn't have to:
    performance degradation and temporary increases swap+memory
    consumption can be the result.

While this series fixes (1) for swappable anon pages, it tries to reduce
reported cases of (3) first as good and easy as possible to limit the
impact when streamlining.  The individual patches try to describe in
which cases we will run into (3).

This series certainly makes (2) worse for THP, because a THP will now
get PTE-mapped on write faults if there are additional references, even
if there was only ever a single process involved: once PTE-mapped, we'll
copy each and every subpage and won't reuse any subpage as long as the
underlying compound page wasn't split.

I'm working on an approach to fix (2) and improve (3): PageAnonExclusive
to mark anon pages that are exclusive to a single process, allow GUP
pins only on such exclusive pages, and allow turning exclusive pages
shared (clearing PageAnonExclusive) only if there are no GUP pins.  Anon
pages with PageAnonExclusive set never have to be copied during write
faults, but eventually during fork() if they cannot be turned shared.
The improved reuse logic in this series will essentially also be the
logic to reset PageAnonExclusive.  This work will certainly take a
while, but I'm planning on sharing details before having code fully
ready.

cleanups related to reuse_swap_page().

Notes:
* For now, I'll leave hugetlb code untouched: "unnecessary COW" might
  easily break existing setups because hugetlb pages are a scarce resource
  and we could just end up having to crash the application when we run out
  of hugetlb pages. We have to be very careful and the security aspect with
  hugetlb is most certainly less relevant than for unprivileged anon pages.
* Instead of lru_add_drain() we might actually just drain the lru_add list
  or even just remove the single page of interest from the lru_add list.
  This would require a new helper function, and could be added if the
  conditional lru_add_drain() turn out to be a problem.
* I extended the test case already included in [1] to also test for the
  newly found do_swap_page() case. I'll send that out separately once/if
  this part was merged.

[1] https://lkml.kernel.org/r/20211217113049.23850-1-david@redhat.com
[2] https://lore.kernel.org/r/3ae33b08-d9ef-f846-56fb-645e3b9b4c66@redhat.com

This patch (of 9):

Liang Zhang reported [1] that the current COW logic in do_wp_page() is
sub-optimal when it comes to swap+read fault+write fault of anonymous
pages that have a single user, visible via a performance degradation in
the redis benchmark.  Something similar was previously reported [2] by
Nadav with a simple reproducer.

After we put an anon page into the swapcache and unmapped it from a single
process, that process might read that page again and refault it read-only.
If that process then writes to that page, the process is actually the
exclusive user of the page, however, the COW logic in do_co_page() won't
be able to reuse it due to the additional reference from the swapcache.

Let's optimize for pages that have been added to the swapcache but only
have an exclusive user.  Try removing the swapcache reference if there is
hope that we're the exclusive user.

We will fail removing the swapcache reference in two scenarios:
(1) There are additional swap entries referencing the page: copying
    instead of reusing is the right thing to do.
(2) The page is under writeback: theoretically we might be able to reuse
    in some cases, however, we cannot remove the additional reference
    and will have to copy.

Note that we'll only try removing the page from the swapcache when it's
highly likely that we'll be the exclusive owner after removing the page
from the swapache.  As we're about to map that page writable and redirty
it, that should not affect reclaim but is rather the right thing to do.

Further, we might have additional references from the LRU pagevecs, which
will force us to copy instead of being able to reuse.  We'll try handling
such references for some scenarios next.  Concurrent writeback cannot be
handled easily and we'll always have to copy.

While at it, remove the superfluous page_mapcount() check: it's
implicitly covered by the page_count() for ordinary anon pages.

[1] https://lkml.kernel.org/r/20220113140318.11117-1-zhangliang5@huawei.com
[2] https://lkml.kernel.org/r/0480D692-D9B2-429A-9A88-9BBA1331AC3A@gmail.com

Link: https://lkml.kernel.org/r/20220131162940.210846-2-david@redhat.com
Signed-off-by: David Hildenbrand <david@redhat.com>
Reported-by: Liang Zhang <zhangliang5@huawei.com>
Reported-by: Nadav Amit <nadav.amit@gmail.com>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Cc: Hugh Dickins <hughd@google.com>
Cc: David Rientjes <rientjes@google.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Jason Gunthorpe <jgg@nvidia.com>
Cc: Mike Kravetz <mike.kravetz@oracle.com>
Cc: Mike Rapoport <rppt@linux.ibm.com>
Cc: Yang Shi <shy828301@gmail.com>
Cc: Kirill A. Shutemov <kirill.shutemov@linux.intel.com>
Cc: Jann Horn <jannh@google.com>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Rik van Riel <riel@surriel.com>
Cc: Roman Gushchin <roman.gushchin@linux.dev>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Don Dutile <ddutile@redhat.com>
Cc: Christoph Hellwig <hch@lst.de>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Jan Kara <jack@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: ZhangPeng <zhangpeng362@huawei.com>
Reviewed-by: tong tiangen <tongtiangen@huawei.com>
Reviewed-by: Kefeng Wang <wangkefeng.wang@huawei.com>
Signed-off-by: Jialin Zhang <zhangjialin11@huawei.com>

---
## [newstools/2023-the-herald](https://github.com/newstools/2023-the-herald)@[01b3527f6e...](https://github.com/newstools/2023-the-herald/commit/01b3527f6e52b1d70fa1ccff10640da998372594)
#### Thursday 2023-03-23 03:48:49 by Billy Einkamerer

Created Text For URL [www.herald.co.zw/when-dembare-dined-with-angels-twenty-five-years-ago-the-glamour-boys-reached-the-gates-of-heaven/]

---
## [newstools/2023-iol-daily-news](https://github.com/newstools/2023-iol-daily-news)@[1e939c7146...](https://github.com/newstools/2023-iol-daily-news/commit/1e939c71460fa1604c67cc128c4d832e8a63aeff)
#### Thursday 2023-03-23 04:10:46 by Billy Einkamerer

Created Text For URL [www.iol.co.za/dailynews/news/dailynews/news/mother-of-woman-killed-and-stabbed-22-times-by-boyfriend-lays-bare-her-pain-5653af76-8f4a-46db-be02-467ac9624bc9]

---
## [andrew6180/TradeSkillMaster](https://github.com/andrew6180/TradeSkillMaster)@[9f78dc9097...](https://github.com/andrew6180/TradeSkillMaster/commit/9f78dc9097a812a564a966cb2d1d1e181500668d)
#### Thursday 2023-03-23 04:11:19 by Bananaman

TradeSkillMaster: Revived

TradeSkillMaster: Revived

- Release Date: March 19th, 2023
- Author: Gnomezilla on Warmane-Icecrown [https://github.com/Bananaman].


## The Market Value Algorithm Actually Works Now

The new market value algorithm now actually calculates the market value.

Yes, seriously. For some reason, the previous algorithm author didn't think about sorting the auction scan data by "buyout price" before parsing it, which meant that all previous TSM calculations were completely incorrect. All previous versions of TSM generate absolutely batshit insane market prices, such as "1 Wool = 500 Gold", simply because the old algorithm was completely broken.

Therefore, TSM's core feature, the "dbmarket" value which is used in its automatic pricing algorithms, was completely broken and useless.

It has now been fixed. All market value calculations are now correct.

In fact, all of your old AuctionDB databases should be wiped and restarted from zero data with this new patch, so that you get rid of all old, corrupt market price data.


## Completely Rewritten Auction Scanning Algorithm

Rewritten, cleaned up and much faster auction scanning algorithm, which uses almost zero memory and NEVER causes any memory overflow crashes, unlike the old algorithm.

This new algorithm is 1.3x-27.3x faster depending on input data size, and on average 5x faster for most data. It uses less than 5% of the memory of the old algorithm. :)

If you want to see for yourself that the new algorithm is working correctly, you simply have to set `verifyNewAlgorithm = true` at the top of `TradeSkillMaster_AuctionDB/Modules/Scanning.lua`, and then run a "GetAll" scan to quickly fetch a huge amount of auctions. It will then process all of the data via both the old and new algorithms, and will display the speed improvements of the new algorithm. If there are any differences at all between the calculations of the two algorithms, it would tell you about that via an "error" message. But the algorithms behave completely identically, so you don't have to worry about that and won't see any errors. This verification feature was simply added because the algorithm rewrite is a massive change, and I am sure that some people will want to verify the complex new algorithm with their own eyes.

Closes #13.
Closes #26.


## Fixed Database Decoding Crash

Fixed a database decoding bug which caused TSM to crash anytime you attempted to decode data for a "corrupted" item in the database.

This bug usually manifested itself as people failing to perform auction house scans, since every "Full Scan" and "GetAll Scan" (but not "Group Scan") ends by decoding EVERY existing item in your current database (to reset their last-seen, cheapest "minBuyout" value to nil before processing the new data). This meant that the decode failures were usually triggered when people reached the end of their auction scans (but would also happen any other time when something attempts to decode data for that item, such as attempting to view the price-info tooltip of an item that has corrupt data in your database).

The cause of the random database corruption is pretty much impossible to find, but it's extremely rare (and it might even have been caused by people re-using databases from older versions of TSM). The fix simply ignores the corrupt "market day / scan" data for items that cannot be correctly decoded, thus purging those corrupt "days / scans" from the database automatically, while still rescuing their remaining non-corrupt data.

Closes #19.
Closes #28.


## Added Support for SharedMedia and Custom GUI Fonts

For some insane reason, TradeSkillMaster uses "Arial" as its default font, which is one of the ugliest fonts in the Universe.

Therefore, I've implemented LibSharedMedia support in TSM, which means that you now have access to a huge variety of fonts. By default, TSM will only list the game's own fonts, but you can install the [SharedMedia](https://github.com/bkader/SharedMedia#install) addon for WOTLK to add over 100 extra fonts that are now usable in TSM! Other addons you've installed may also be adding extra fonts to the LibSharedMedia collection!

To change TSM's font, simply type "/tsm", then go into the main tab, and then "Options". Scroll down to the bottom, until you see the new "Normal Font" and "Header Font" options. Have fun!

Note: TSM is unable to use SharedMedia fonts that are registered by addons that load AFTER TSM, since TSM accesses the fonts and creates its own GUI immediately when it loads, even before the user opens TSM's GUI. To use fonts from such an addon, you have to add that addon to "OptionalDeps" in "TradeSkillMaster.toc", which tells the game that you want TSM to load AFTER the addon that provides your extra fonts. This step isn't necessary for SharedMedia fonts, since they're already marked as an optional TSM dependency now.


## Made the "Group Scan" (AuctionDB) Progress Bar More Logical

The old progress bar for "Group Scans" used absolutely insane numbering and progress messages. It previously went: "Preparing Filter 1 / 2", "Preparing Filter 2 / 2", "Scanning 0 / 2 (Page 1 / 1)", "Scanning 0 / 2 (Page 2 / 16)", ... "Scanning 0 / 2 (Page 16 / 16)", "Scanning 1 / 2 (Page 1 / 1)", "Scanning 1 / 2 (Page 2 / 6)", ... "Scanning 1 / 2 (Page 6 / 6)", "Done Scanning".

It made absolutely zero sense, and was inconsistent with the behavior of other "counting" progress labels in TSM. There were two issues with it: The item scanner counted from 0, so item 0 was actually item 1, and item 1 was actually item 2, etc. The other issue is that it always said "Page 1 / 1" while requesting the first page, which was a very confusing and misleading display.

Both issues have now been fixed, and the exact same scan would now look as follows: "Preparing Filter 1 / 2", "Preparing Filter 2 / 2", "Scanning 1 / 2 (Page 1 / ?)", "Scanning 1 / 2 (Page 2 / 16)", ... "Scanning 1 / 2 (Page 16 / 16)", "Scanning 2 / 2 (Page 1 / ?)", "Scanning 2 / 2 (Page 2 / 6)", ... "Scanning 2 / 2 (Page 6 / 6)", "Done Scanning".

In other words, we now properly count the items we're processing, and we display a temporary question mark while we're fetching page 1 (while we don't know how many other pages exist), which then changes into the actual page count as the scan proceeds.


## Made the "Auctioning" Module's Progress Bar More Logical

This is similar to the "Group Scan" issues described above.

The "Auctioning" module's features (Post Scan / Cancel Scan / Reset Scan) had several issues.

They were counting items from 0, so the progres bar said "Scanning 0 / 2" for the first item, and "Scanning 1 / 2" for the final item. That has now been fixed and now counts properly (as "1/2" and "2/2").

They also had a completely broken page counter, which didn't properly reset between items, which meant that you'd see complete nonsense while scanning, such as "Scanning 3 / 5 (Page 5 / 5)" followed by "Scanning 4 / 5 (Page 5 / 5)" (keeping the previous page counter), and then the proper counter would finally show up as "Scanning 4 / 5 (Page 1 / 12)" after a few seconds (whenever the server finally replied to the query). It was broken and confusing as hell. That's now been fixed too, so that it properly resets the page counter before every new item it's scanning.

Furthermore, the confusing "Page 1 / 1 ... Page 2 / 18" issue has been fixed here too, and now says "Page 1 / ?" while fetching the first page of each item.

Lastly, their page counter was inconsistent with the behavior of regular "AuctionDB: Group Scan" and the "Shopping" progress bars. The page counter in "Auctioning" was zero-indexed, meaning that "Scanning Page 1/8" meant that you were actually scanning page 2/8. That math has now been fixed here, for consistency with the AuctionDB and Shopping scanner's math, because that's a much more logical way to display the pages.


## Made the "Shopping" Module's Progress Bar More Logical

The "Shopping" module's scanner had multiple issues.

The bar background was supposed to gradually "fill in" to indicate progress for both the "current/total item progress" and the "page progress of the current item". But the math was completely broken. It rendered the progress bar incorrectly, since it ended up counting the progress as "2 items below the item it's currently working on" (due to a mistaken "-1" in the old math). As a result, if you were currently scanning item 3 of 3, you SHOULD have seen a 66% full bar (since 2 of 3 items are done, and the 3rd is being worked on). But you instead only saw a 33% full bar, which was completely wrong. This was especially noticeable if you performed a multi-item search, such as "copper ore; copper bar; gold ore; gold bar".

They were also counting items from 0, so the progress bar said "Scanning 0 / 2" for the first item, and "Scanning 1 / 2" for the final item. That has now been fixed and now counts properly (as "1/2" and "2/2"), just like with the other modules above.

Lastly, the confusing "Page 1 / 1 ... Page 2 / 18" issue has been fixed here too, and now says "Page 1 / ?" while fetching the first page of each item.


## Accurate Time Estimate for the "Full Scan" Progress Bar

Implemented an accurate "time remaining" estimate for the "Full Scan" algorithm. The progress bar now shows how much time remains until the scan is complete, such as `Scanning page 293/2399 (~1:04:34)`, meaning that roughly one hour remains. This is very useful for people who want to use the comprehensive "Full Scan" scanning method, but who hate the feeling of blindly scanning without being able to see the remaining time.

The first time you run a scan on a server, you'll have a very unpredictable estimate, since we use a learning algorithm. The estimate is based on how fast the server is feeding us the "auction pages" on average, which is impossible to know on the first run. Most servers will gradually throttle the player's requests and use random load throttling, so you'll see a growing estimate until it finally settles on an accurate estimate after around 80% of the pages have been received. The slowdown curve depends on the server's throttling implementation, and cannot be predicted ahead of time.

Think of the first run as the "learning run". After you've completed a "Full Scan", our algorithm learns from it and will produce excellent estimates for all future scans, using a blending algorithm which takes into account both the active run's speed and previous speeds, to predict the server's behavior. The statistics are stored per-server and per-faction, so if you're playing both Alliance and Horde, you'll have to do one full scan per faction to teach it about both factions.

Note regarding the other scan types: The "GetAll Scan" algorithm only takes a few seconds, so it doesn't need any time estimate. And the "Group Scan" algorithm can't implement any estimate, since there's no way to know how many "auction pages" the remaining items in the group will have.


## Improved "GetAll" Algorithm Reliability

Most private servers don't implement WoW's "can we perform a GetAll Query?" API, and incorrectly answer that the user is allowed to run a query, even though you may still be throttled after a recent "GetAll" scan. Therefore, TSM's own "don't start a GetAll if we're on cooldown" check doesn't work on private servers. The user may therefore click on "Run GetAll Scan" and will then just blindly sit there like an idiot while the request has actually been secretly ignored by the server.

This situation has now been fixed, so that the "GetAll" scan UI tells the user when the server has silently throttled / ignored their "GetAll" request, so they don't sit there and wait for hours without any progress. Basically, if it's taken longer than 30 seconds, we're assuming that the request has been silently ignored by the server, and will now tell the user via the TSM GUI's progress bar message. It first says `Running query...` as usual, which then changes to `Running query... Server not responding due to throttling? Try again later...` if there hasn't been a server response in more than 30 seconds.

The "GetAll" algorithm has also been improved to automatically detect when your server is only sending limited / truncated data. Extremely large private servers such as Warmane simply have too many auctions, and their "GetAll" scan won't retrieve all of them. We now warn the user via a chat-message whenever we detect truncated auction data, and we then tell them to use "Full Scan" instead.

It's unfortunately impossible to calculate accurate market values if your server is sending truncated "GetAll" responses, but people may still prefer the speed of the "GetAll" scans, so we're therefore still allowing their "truncated" auction data to be processed. The users will have to read the warning message and decide for themselves which scans they want to use.

The inaccuracy of an incomplete "GetAll" scan completely depends on how the server implements "GetAll". If the server sorts the cheapest auctions first, then it's somewhat acceptable for popular items which have many stacks (and are therefore likely to contain enough data points in the "GetAll" result), and those items will "just" tend to be undervalued by 2-10% less than their real market value (since their percentile-based scans will look at less auctions than the real amount). But for very rare or unpopular items, the partial "GetAll" scan is very dangerous, since you might only receive the massively overpriced auctions of a certain item, and thereby calculate an insanely high market value for it. These dangers are increased if the server sends the auctions in a totally random order, which means an even greater risk of market price pollution by only seeing overpriced auctions for many of the items.

Furthermore, receiving incomplete "GetAll" results means that TSM will wipe all of its "cheapest, current buyout price" data for all items, and then fills them with incorrect data (or nothing at all if an item wasn't seen in the latest fetch), thus hindering your ability to look up the correct "best current buyout prices" too.

In summary, you'll have to use partial "GetAll" results at your own risk! A "Full Scan" is ALWAYS much better when your server's "GetAll" doesn't provide all auction data!


## Improved All Auction Data and Market Value Processing

There were several bugs everywhere in the old code. For example, only the "GetAll" scan had correctly implemented filtering of non-buyout items (auctions that ONLY have a bid price, without any buyout price), which meant that TSM's other scan methods ("Full Scan", "Group Scan", etc) were injecting invalid data into the player's database, such as items with empty "buyout prices". They were being treated as items with a buyout price of ZERO (as if they were totally free items, at no cost!). This serious bug happened every time when there were ANY bid-based auctions for an item in the latest scan.

All of the auction scanning and processing algorithms have been rewritten for correctness, and will now filter out those useless "bid-only" data entries. We will only analyze auctions that have buyout prices.

Several bugs have also been fixed related to items being incorrectly marked as "seen and scanned now" even when there was no new data for that item in the latest data batch (this was yet again related to the "incoming data only has bid-based auctions" bug). We now only update the scan-statistics for items when we encounter new data for them with valid buyout prices.

There were also bugs in the market value calculation algorithm, which would crash with "division by zero" if given empty input data (yet again related to only having bid-based auctions in the input data, but this crash only happened if there were only bid-based auctions for an item, without any buyout-based auctions whatsoever for that item, so it was rare to encounter this crash). That issue has also been fixed now, by adding perfect protection against empty inputs in the market value calculation algorithm.

We also no longer update the market value for an item if we were unable to calculate a new market value (the old code simply wrote invalid market values to the database without any sanity checks).

All of these improvements mean that TSM's market price estimates are now infinitely more reliable than old TSM versions.


## Fixed Missing "Interruption" Events in Auction Scanners

This is a great example of what a total mess the TSM codebase is...

All auction scanners (AuctionDB, Auctioning and Shopping) were missing their "scan interrupted" event, which is triggered when the Auction House frame closes while a scan is ongoing.

The problem was caused by the fact that TSM previously used the "LibAuctionScan-1.0" library, which emits the "SCAN_INTERRUPTED" event. All TSM scanners were still written to react to that old event name. But TSM nowadays uses their own scanning library instead, which sends the "INTERRUPTED" event instead. They literally forgot to update the event handlers when they switched the library, and they didn't even bother deleting the old library either.

All three scanning methods have now been fixed, to react to the proper "INTERRUPTED" event, to be able to detect when your scans are interrupted by the auction window being closed.

Furthermore, the "Shopping" module hadn't implemented interruption handling whatsoever. There literally wasn't any event handler for it. It has now been properly implemented, so that the "Shopping" scanner works properly and correctly resets itself after interruptions.


## IMPORTANT!

When upgrading to this improved version, it's an extremely good idea to delete your old-school, CORRUPT auction database, since your old data has been generated by the extremely buggy algorithms of the old TSM. For example, some of those old "auction data corrupting" bugs include the fact that it was calculating completely incorrect market values when doing "GetAll" scans, since it was previously unable to handle per-item prices inside item stacks, and another bug is the fact that all other scan methods generated wrong market values too, thanks to TSM's previously completely broken market value algorithm (those problems are described in the other changelog entries above).

There is NO GOOD REASON to keep your old auction database. It's all corrupt thanks to all the old TSM bugs, 100% guaranteed. You need to start fresh.

If you're ready to start fresh, simply delete these files (where `YOUR_ACCOUNT_NAME` is your own account name):

```
./WoW/WTF/Account/YOUR_ACCOUNT_NAME/SavedVariables/TradeSkillMaster_AuctionDB.lua.bak
./WoW/WTF/Account/YOUR_ACCOUNT_NAME/SavedVariables/TradeSkillMaster_AuctionDB.lua
```

Then do a "Full Scan" in the game, and you'll be sure that all data from now on is processed using more intelligent algorithms.

All serious bugs are fixed now. You can finally relax and enjoy TSM.


## Why is this one huge commit?

Because I've already wasted enough time on these massive rewrites of TSM 2.8's extremely buggy, old code. I won't waste even more time splitting it into neat little commits, especially since all of the changes are related to each other.

All new code is well-documented and self-explanatory. In fact, there are now a lot of comments to explain all of the new auction processing algorithms, so that future readers won't have to waste hours untangling TSM 2.8's poorly written and poorly documented spaghetti code again!

It's no surprise that there were so many bugs, since the TSM code is a massive spaghetti mess with barely any comments, and it even has around 5 differently-broken implementations of auction scanning via at least 3 different modules and 2 different libraries, instead of just having one robust, unified scanning library. It's mind-blowing how incompetent the original TSM code is. There's tons of code repetition and bugs everywhere. It's insanely bad. Having a lot of comments to finally explain the critical TSM algorithms in-depth absolutely improves the situation.

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/silicons/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Thursday 2023-03-23 04:48:04 by IrkallaEpsilon

Matterforge Recipe expansion (#5168)

## About The Pull Request

This PR adds a few more matterforge recipes, some of stupidly high
difficulty and pointless rewards if miners are doing their job (looking
at you steel to gold), some of more usefulness (gold to plat, plat to
osmium). All require different temperature and energy ranges so they
cannot be rushed thoroughly. Not much thought was put into realism but
eh who cares, the matterforge is a cool thing ingame and its fun to use.
Some temperatures ranges (Steel to gold) are very narrow hence the use
of a gyrotron would be needed to get the most out of it. Or precise
heating (temperature can be raised to exorbitant amounts to prevent
heater cheese). This also would allow for Research to collab with cargo
for exports specially if dynamic prices ever come. In particular looking
at the gold to plat transmutation here. Plat can be exported by cargo in
which cargo can order more shit from.

I aint a good coder else I would add specific atmospheric conditions
needed, not just temperature (e.g. N2O must be present).
Reminded me a bit of TGs gas reactions but less gamy. 

## Why It's Good For The Game

More Matterforge recipes. Most relatively pointless and niche, some
allow science to give cargo something to sell, others can help with
theres an overabundance of Plat due to new miners. Mostly just giving
some extra uses for the forge. Oh and an alternative way to get plasteel
while sacrificing phoron sheets. Also bragging rights of effectively
turning iron (and carbon) into gold at specific temperatures and energy
levels on the particle focus.

A proper coder should check if these recipes are fine. Its 2:30 AM and I
thought this would just be neat.

## Changelog

:cl:
add: Various matterforge recipes
/:cl:

---
## [erikarn/sdcc-cpm](https://github.com/erikarn/sdcc-cpm)@[2e6063a5ea...](https://github.com/erikarn/sdcc-cpm/commit/2e6063a5ea6290d4c7bab48d8a231f83d028a55a)
#### Thursday 2023-03-23 05:18:50 by Adrian Chadd

add a PCW specific terminal thingy.

Yeah I know, I'm reinventing the worst part of curses/ncurses
and i'm pretty sure this was all better solved in ye olde days,
but I just want a non-crap basic ASCII text editor for CPM/3
and I think I can write one in C and not waste all my TPA
with the binary.

(But gosh it'd be nice to edit text files bigger than the TPA...)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8d7db532c0...](https://github.com/tgstation/tgstation/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Thursday 2023-03-23 05:25:27 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

## About The Pull Request

This is a followup PR to
https://github.com/tgstation/tgstation/pull/73866

Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19991

I had suspected the nutrition loss slimes experience alongside blood
regen might necessitate some tweaks down the line and here we are. This
PR has two parts.

---

**PART I:** _Reworking the blood deficiency quirk backend_

As it is, blood drain from the blood deficiency occurs in the quirk's
subsystem process() call asynchronously to Life(), where the blood regen
occurs.

This results in the blood volume fluctuating constantly, making it
difficult to really make sense of readings and potentially introducing
race conditions. This PR changes that.

The blood deficiency quirk no longer processes and instead has a proc,
`lose_blood(delta_time)`, which is called in the `handle_blood()` proc
at the same time blood gets regenerated.

Added a `get_quirk` proc to help with this, so that we only have to
iterate through the quirks list once for each mob (rather than calling
has_quirk, then locate in quirks... etc).

Added a `TRAIT_BLOOD_DEFICIENCY` to further optimize the code.

---

**PART II:** _Some fine tuning of the slime blood deficiency quirk_

Slime regen works a bit differently than humans such that if they lose
-any- blood whatsoever, they will also lose nutrition. This means that
even if hooked up to an IV they will still become starving rather
quickly. A bit -too- quickly.

Instead, now the hunger does not kick in until `blood_volume` reaches
550. This means that if a slime with the blood deficiency quirk is
hooked up to an IV with say, welding fluid, and has over 150 nutrition,
they will regen blood faster than they lose it from the blood deficiency
quirk. Once they get to over 550 `blood_volume`, they will stop losing
hunger (from blood regen, anyway--normal hunger rate still applies).

So essentially this just allows slimes with the blood deficiency quirk
to be able to function so long as they stay hooked up to their IV's (or
chug welder fluid/some other toxin), which is the intended purpose of
the quirk.

Edit: As a bonus I added new blood bags for the exotic blood types, and
added a proc `update_mail_goodies` which updates the blood deficiency
quirk's mail goodies accordingly (crewmembers with blood deficiency get
sent blood bags, now they will get the correct type if their species
changes). While I was in these files I changed any immediate single
letter vars I could find and cleaned up what I could.


![image](https://user-images.githubusercontent.com/13398309/226739179-a21790e3-0be6-423a-be89-8d2cb84f6149.png)


<details>
<summary>The new blood packs</summary>


![image](https://user-images.githubusercontent.com/13398309/226743543-29fca53d-b3d1-4903-9706-35b2c00bbe78.png)

</details>

## Why It's Good For The Game

-This is arguably a more performant option than before, and fixes race
conditions from `Life()` and `quirk/blooddeficiency/process()` fighting
with one another.

-Adjustments to slime blood deficiency will enable it to function as
intended.

-It is now easier to read health analyzer blood volume readings for
blood deficient mobs.

-Now the correct blood packs are sent in the mail.

## Changelog

:cl:
qol: adjusted the blood deficiency quirk for slimepeople to not cause
excessive hunger as long as blood volume is kept above 550 via an IV
drip (or other means of getting welding fluid/some other toxin etc into
the bloodstream, e.g. ingestion)
qol: speciees with exotic blood types will now receive the correct blood
bag in the mail from having the blood deficiency perk
add: adds new blood bag types: TOX (slimepeople), H2O (podpeople), S
(snail)
fix: fixed blood deficiency quirk causing wild fluctuations in blood
volume on the analyzer, giving more accurate readings
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[a6f49ed542...](https://github.com/lessthnthree/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Thursday 2023-03-23 05:56:34 by san7890

Refactors Suiciding Variable Into Trait (#74150)

## About The Pull Request

Firstly, this var was on `/mob`, even though only `/mob/living` and
`/mob/dead` could have ever used it, so who knows how much needless
memory it was consuming on stuff such as `oranges_ear` that would never
ever ever use something like this.

Edit: okay instead of memory it just polluted variable edit windows for
all /mob when it didn't need to. I like having a slim VV window

Secondly, it's a technical improvement over the previous system as we
are able to "track" where a suicide originates from, and how we can
track that from mob-to-mob-to-mob. Previously, the boolean `suiciding`
would only inform us if they had ever been connected to a mob that had
ever committed suicide, but now we are able to precisely determine which
mob gave them the trait that they must now apparently bear until the
round restarts.

## Why It's Good For The Game

Less memory usage, more indepth ability to track suicides in case you
really need that dexterity. Currently no implemented code could benefit
from using it, but it would be pretty neat if someone could figure out a
way to have someone be guilt-tripped whenever they look into a mirror
and seeing the reflection of their past life? This PR won't actually
help you code that and it'll probably require a bit more work, but it's
a possibility of some cool interactions you can do when you have this
information available to you.


![image](https://user-images.githubusercontent.com/34697715/226506321-550c37e7-5de8-4f9f-9ceb-4bf9b1052597.png)

## Changelog

:cl:
refactor: Some aspects of how we track suicides from your living mob to
your observer have changed- please do let us know if anything has broken
via a GitHub Issue Report.
/:cl:

There's probably some technical improvements that can be made in some
parts of the code I reworked to accommodate this change, do let me know
if you spot any easy ones (or fuckups). a lot of excess comes from the
fact that any step in the TRAIT framework trusts that you are passing in
a valid datum (or subtype) so that's a thing

---
## [LiquidCat64/LiquidCatipelago](https://github.com/LiquidCat64/LiquidCatipelago)@[6d13dc4944...](https://github.com/LiquidCat64/LiquidCatipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Thursday 2023-03-23 07:11:53 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [cyyever/pytorch](https://github.com/cyyever/pytorch)@[a269469982...](https://github.com/cyyever/pytorch/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Thursday 2023-03-23 07:17:44 by Brian Hirsh

aot autograd refactor: make all synthetic base logic layered in a single location (#96235)

This  refactor doesn't significantly change LoC in aot autograd, but I think this nets out to making it clearer (interested in peoples' thoughts).

The idea is that I tried to re-write the part of aot autograd that deals with synthetic bases in a layered way, similar to how Ed wrote the logic for dedup'ing inputs: it happens in one place, and all of the downstream transformation in aot autograd don't have to worry about it.

Specifically, I added a new function `aot_wrapper_synthetic_base`, similar to the existing `aot_wrapper_dedupe`.

The benefit: none of the other code in aot autograd needs to think about synthetic bases (previously, synthetic base code was intertwined in several places).

The downsides: there are two.

(1) `aot_wrapper_synthetic_base()` needs to have its own epilogue. There is one particularly hairy case, where factoring the synthetic base logic to a single location was painful: If you have two inputs that alias each other, where one gets a data mutation, and the other gets a metadata mutation.

Ordinarily, metadata mutations are handled by the runtime epilogue, in `create_runtime_wrapper`. However, now that things are factored this way, the runtime wrapper operates only on synthetic bases instead of operating on the original inputs. For data mutations, it is fine to apply the data mutation to the synthetic base instead of the original input alias. But for metadata mutations, we **need** to apply the metadata mutation directly to the original inputs.

The way that I handled this was by tracking which inputs slot into this specific case (part of a synthetic base, and get metadata mutations), and updateing the flat_fn() that we pass downstream to return these updated inputs as extra outputs. From the perspective of downstream logic, these are real user outputs, that it can treat like any other user outputs. `aot_wrapper_synthetic_base` will know to grab these extra outputs and use them to apply the metadata mutations.

This was pretty annoying, but has the benefit that all of that logic is encapsulated entirely in `aot_wrapper_synthetic_base()`.

(2) input mutations are now performed on the synthetic base instead of the individual aliases.

You can see the original code comment [here](https://github.com/pytorch/pytorch/blob/b0b5f3c6c681896febbd9ff7ad7649b13def345d/torch/_functorch/aot_autograd.py#L1131) for details. We used to do the optimized thing in this case, and now we do the less optimized thing (copying the entire synthetic base, instead of the potentially smaller alias).

To be fair, we had no data showing that this optimization was showing improvements on any models in practice. I also think that the main reason anyone would ever run across this problem is because of a graph break - so if you care about perf, you probably want to avoid the extra graph breaks to begin with. I haven't added any warnings for this, but we probably could depending on what people think.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/96235
Approved by: https://github.com/ezyang

---
## [NetworkManager/NetworkManager](https://github.com/NetworkManager/NetworkManager)@[7ca95cee15...](https://github.com/NetworkManager/NetworkManager/commit/7ca95cee15b32af2452aaf4a165eb5c634fba132)
#### Thursday 2023-03-23 07:24:06 by Thomas Haller

platform: always reconfigure IP routes even if removed externally

NML3Cfg is stateful, that means it remembers which address/route it
configured earlier. That is important because the API users of NML3Cfg
only say what the want to configure now, and NML3Cfg needs to remove
addresses/routes that it configured earlier but are no longer to be
present. Also, NetworkManager wants to allow the user to add
addresses/routes externally with `ip addr|route add` and NetworkManager
not removing it. This is a common use case for dispatcher scripts, but
in general, we want to allow other components to add addresses/routes.

We try something similar with the removal of routes/addresses managed by
NetworkManager. When NetworkManager adds a route/address, which later
disappears, then we assume that the user intentionally removed the
address/route and take the hint to not re-add it.

However, it doesn't work. It is problematic for two reasons:

- kernel can automatically remove routes. For example, deleting an IPv4
  address that is the prefsrc of a route, will cause kernel to delete
  that route. Sure, we may be unable to re-configure the route at this
  moment, but we shouldn't remember indefinitely that the route is
  supposed to be absent. Rather, we should re-add it when possible.

- kernel is a pain with validating consistencies of routes. For example,
  when a route has a nexthop gateway, then the gateway must be onlink
  (directly reachable), or kernel refuses to add it with "Nexthop has
  invalid gateway". Of course, when removing the onlink route kernel is
  fine leaving the gateway route behind, which it would otherwise refuse
  to add.
  Anyway. Such interdependencies for when kernel rejects adding a route
  with "Nexthop has invalid gateway" are non-trivial. We try to work
  around that by always adding the necessary onlink routes. See
  nm_l3_config_data_add_dependent_onlink_routes(). But if the user
  externally removed the dependent onlink route, and NetworkManager
  remembers to not re-adding it, then the efforts from
  nm_l3_config_data_add_dependent_onlink_routes() are ignored. This
  causes ripple effects and NetworkManager will also be unable to add the
  nexthop route.

Trying to preserve absence of routes that NetworkManager would like to
configure is not tenable. Don't do it anymore. There was anyway no
guarantee that on the next update NetworkManager wouldn't try to re-add
the route in question. For example, if the route came from DHCP, and the
lease temporarily went away and came back, then NetworkManager probably
would have (correctly) forgotten that the user wished that the route be
absent. This did not work reliably and it just causes problems.

---
## [vaadin/flow](https://github.com/vaadin/flow)@[0a1da07df3...](https://github.com/vaadin/flow/commit/0a1da07df303aa5b477e736e528c0a3c59391e07)
#### Thursday 2023-03-23 07:26:02 by czp13

chore: added more covering tests to ComponentTest.java for covering getLocale() method (#16367)

* Added more covering tests to ComponentTest.java for the getLocale method. It was needed, because another external contributor PR is tackling
a refactor/optimization of this method (as well), and this change it will ensure the functionality, and execution branches are the same. (https://github.com/vaadin/flow/pull/16160)
* Fix typo/my bad in ComponentTest.java
* mvn formatter:format executed
* Locale.US is the first element of this list: List.of(Locale.US, Locale.CANADA_FRENCH);
 Not CANADA_FRENCH (night facepalm for myself)
 Should fix this error:
 "java.lang.AssertionError: First provided locale should be returned expected:<fr_CA> but was:<en_US>""
* Implemented @mcollovati review idea on creating provided locales.
Thank you ;)

---
## [aaronfc/ai-evolving-web](https://github.com/aaronfc/ai-evolving-web)@[08ab103f27...](https://github.com/aaronfc/ai-evolving-web/commit/08ab103f27e9e2d297c66760aba4daa46166987a)
#### Thursday 2023-03-23 08:11:36 by Aarón Fas

Version 8: Added AI Spotlight section and made minor style adjustments.

Again a little bit convoluted experience, I am starting to be afraid of
it becoming more repetitive and unstable from now on. Let's see.
I asked for the changes in the diff format and it sent an invalid diff.
It was a minor issue but I didn't want to "ignore" the error.
I asked about any other way of format that would prevent the issues we
are having and told me to do everything manually. I accepted for this
time, but next time I will try to reduce my manual intervention.
Oh! And this is the first time that the commit title is generated by the
AI itself.

Conversation:
[aaron]
24h! Let's go! Can you be a little bit more ambitious for this one? The last changes seemed a little bit repetitive to me. But remember it's your choice, so if you prefer to do a simple change again feel free to do it.

[chatgpt]
I understand your desire for a more ambitious update. Here's the diff for the new changes I propose:
// CODE (diff):
// - Increased the sizes of some texts and added some space.
// - Duplicated the quote in a slightly different way.
// - Added inspiration section in a different place (duplicated now)
// - Added some background color to resources section.
I hope these changes are more to your liking. Please let me know if you want me to make any additional changes today.

[aaron]
I am sorry, but this diff does not make sense sinse it's not based in the last file. I will repeat the file again for you. Wait until I se "that's all". If I send more than one message just consider a continuation from the previous one until I say "that's all". You can answer with "ack" until I say "that's all".

[chatgpt]
ack

[aaron]
// CODE: Current `index.php` file.

[chatgpt]
ack

[aaron]
that's all

[chatgpt]
// CODE (diff):
// - Added some margin.
// - Changed title from Resources to AI Resources
// - Added an "AI Spotlight" section about chatbots.
This update adds some margin-bottom to the divs for better spacing, updates the "Resources" title to "AI Resources", and adds a new "AI Spotlight: Chatbots" section that discusses chatbots and provides a list of popular chatbot platforms.

[aaron]
That's better. But the the last part of the diff was rejected. Do you have any suggestion on how we could do this better? Take into account that the file is now of a considerable size and sending it as a whole is starting to be problematic. Also the diff format is not working because some of the parts of the diff are not right.

[chatgpt]
I apologize for the difficulties you've been facing. I have an alternative approach that should help us communicate the changes more efficiently. Instead of providing a full diff, I'll describe the changes step-by-step. You can then apply these changes directly to the file.
For today's update, please make the following changes:
1. Add a margin-bottom: 20px; property to the div style rule in the <style> section:
// CODE

2. Change the title of the "Resources" section to "AI Resources":
// CODE

3. Add a new section called "AI Spotlight: Chatbots" after the "Join the Community" section and before the closing </body> tag:
// CODE

Please let me know if you have any questions or need further clarification.

[aaron]
I am using the following format for the commits in the GitHub repository:
- Version 2: Added quote about "change".
- Version 3: Added Latest News section.
- Version 4: Added inspiration section.
- Version 5: Added resources section.
- Version 6: Very minor change adding extra information.
- Version 7: Adding community section.

Would you from now on give me also the title for the commit yourself? Do it for the latest changes you just sent me.

[chatgpt]
Of course! For the latest changes, you can use the following commit message:

- Version 8: Added AI Spotlight section and made minor style adjustments.

[aaron]
Good, see you tomorrow!

[chatgpt]
See you tomorrow! Have a great day!

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[45181e2a15...](https://github.com/odoo-dev/odoo/commit/45181e2a152e0b5753c479ae533cccd7fd3efe9b)
#### Thursday 2023-03-23 08:44:46 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

---
## [SynthSy/TwitterToWebhook](https://github.com/SynthSy/TwitterToWebhook)@[bc8e48671e...](https://github.com/SynthSy/TwitterToWebhook/commit/bc8e48671e65beeaa2591cff0b2953618d705479)
#### Thursday 2023-03-23 08:47:09 by Aida Enna

Pain in the fucking ass, GIF support finished. Program is ready.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[569259a836...](https://github.com/odoo-dev/odoo/commit/569259a836b622dd1fe05523bd3b6c7004209e79)
#### Thursday 2023-03-23 10:34:09 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ff0250559c...](https://github.com/mrakgr/The-Spiral-Language/commit/ff0250559c7d6d7dd0c84a0da867776431d787ba)
#### Thursday 2023-03-23 11:09:41 by Marko Grdinić

"7:25am. I slept really well tonight. Today I do not have that dull feeling in my mind.

7:30am. No emails. Yeah, forget this. It is ghost season this time of the year. Is my F# sub post still at 0 for some reason?

https://www.reddit.com/r/fsharp/comments/11yfada/implementing_the_counterfactual_regret_algorithm/

Yeah, it is still at 0. This is the power of subjects. I bet I could have done 'Implementing ChatGPT' and I'd have gotten a 100 upvotes.

This wave of ML is the shittiest one ever. I've been very wrong with how things would go. I didn't think that backprop would keep limping along so far. The only thing I need is for the AI chips to be turds that can't beat GPUs and it will complete the shit festival.

At least with my foray into webdev, I am breaking free of the shackles of languages. It is really a breath of fresh air to be able have different processes and machines communicate remotely.

https://youtu.be/C7eSobE3Ms4
Why You Should Learn C# 2023

Let me watch this guy.

...This is pretty funny.

7:55am. Let me just finish chilling and then I'll resume the next video. I want to get it out of the way today so I can get the next part done.

8:05am. https://old.reddit.com/r/ExperiencedDevs/

8:30am. https://old.reddit.com/r/ExperiencedDevs/comments/11y8hys/chatgpt_resumes_accounted_for_30_of_the_ones_we/

///

I have heard it is good for tailoring resumes (i.e. give it a super long ‘master’ resume with your entire life story, and ask it to carve out a targeted resume for a specific job ad)

I have been meaning to try it out - I do try and tailor my resume a little bit when applying for jobs, but if you’re applying for a lot of positions there’s a limit to what’s practical

///

I haven't tried this, but I really should. Nevermind this for now.

Reading this thread is pretty interesting, as those on the hiring side wants the candidates to be honest, but also want to drop them with impunity for the slightest deviation from the ideal and don't want to spent more than quarter of a minute per resume. The HR crowd is reaping the consequences of their own actions. Next is them getting replaced by AI. As shitty as these algorithms are, they can't be worse at evaluating candidates that the hiring people.

Since they aren't taking my PL project seriously, I myself literally have zero way to prove my skills in this environment, so I have no choice but to turn my hand into a bluff despite it not being weak to begin with.

8:40am. Let me start, let me start!

8:50am. Ok, I have 5m of audio, let me just record the relevant video. I've just been doing the voice over first. I am mixing up my workflow.

It feels like every since I installed the Rx Editor, my screencasting ability has exploded. It has gotten more fun.

11:55am. Let me take a break here. So far I am 12m in. It feels like I am sprinting. I'll finish this today and then move on to implementing the MC version of CFR. Then I will cover that one.

After which comes NL Holdem. On NL Holdem I'll get a chance to bring in NNs. I really want to master the dataflow between Python and .NET."

---
## [bernardperru/CarAlarmSystem](https://github.com/bernardperru/CarAlarmSystem)@[9c85f834cf...](https://github.com/bernardperru/CarAlarmSystem/commit/9c85f834cfb0f35c32cd28cd8730c969768669b4)
#### Thursday 2023-03-23 11:15:42 by bernardperru

threads are my friend

colorful words,
wild flowers in spring,
winter depression,
see you on the next episode.

---
## [hodnick/openai-prompt-examples](https://github.com/hodnick/openai-prompt-examples)@[765e9a378c...](https://github.com/hodnick/openai-prompt-examples/commit/765e9a378c50dcceba61590bc42fd65c51f6745f)
#### Thursday 2023-03-23 11:25:18 by nick hodnick

Generate an envisioning workshop agenda

In this I want you be a Technical Program Manager that will host an Envisioning Workshop. An Envisioning workshop is a designing thinking style hybrid workshop where we have attendees both in person and remote that will consist of Initial understanding of Customer’s business goal, the engagement summary, and technical challenges, Identified stakeholders from Customer, Identified Customer or Partner engineering resources to Code With, Customer location and timeline, Value and risk markers, Tech scenario, Start of legal and/or data exploration process.  Also I want you to include a table that you will pre-populate for ideas for features and opportunities that we can co-engineer with our team and the customer to develop based on this proposed project.  This table has a table for Feasibility, which is how feasibility is this opportunity to do and the positive Impact, meaning how much Impact will this have to help the company.  You can generate at least 10 opportunities for this table to get the team thinking about this.  
 
Create an agenda that we can cover in one day, we'll use a mural board, so consider how we can best lay out the sections and collectively capture notes and share with the board. Provide details for the agenda, how much time, what roles on the project lead sections, and provide suggestions on how to make this a fun and interactive experience for everyone. 
 
The project is about <insert here your details about your project>

---
## [mirandadam/evals](https://github.com/mirandadam/evals)@[ab5f7b2a89...](https://github.com/mirandadam/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Thursday 2023-03-23 11:35:32 by oscar-king

Counting bigrams in sentences (#302)

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
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

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

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [mirandadam/evals](https://github.com/mirandadam/evals)@[b170a21cf3...](https://github.com/mirandadam/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Thursday 2023-03-23 11:35:32 by Sam Ennis

Computer Science Theory (#83)

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
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
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
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [mirandadam/evals](https://github.com/mirandadam/evals)@[b5da073c21...](https://github.com/mirandadam/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Thursday 2023-03-23 11:35:32 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

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

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

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

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

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
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[fbdafc8a78...](https://github.com/harryob/cmss13/commit/fbdafc8a789f5944ca5abcbdb569f466fcea2ff2)
#### Thursday 2023-03-23 12:36:57 by victorjosephespinoza

Add UPP warcries (#2878)

# About the pull request

Replaces the normal warcry for the UPP faction to use russian voices
instead.

The warcries are mostly stuff like `za rodinu` and `uraa`, so yeah,
pretty much just typical soviet warcries.

I haven't focused on adding dozens of voicelines due to the fact that
this is a minor faction whose appearance is only in events and/or ERT's.
However, I can try to get some more, if requested.

# Explain why it's good for the game

Lately, I have noticed an increase of HvH events (in which, I have
participated). I found that it is quite uninmersive how every UPP
soldier is literally yelling in english at the same time as marines are
also yelling the same voicelines. So yeah. I kind of found it just weird
and since then I've been thinking of adding something like this to the
server.

# Testing Photographs and Procedure
Tested it myself, works. I can upload a video if it is really needed,
however.

# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:H20Begod
add: sound/voice/upp_warcry/* (Sound files, such as `warcry_male_1` ,
for the UPP)
code: changed `code/modules/mob/living/carbon/human/emote.dm`, in order
to add conditionals that will check a player's faction. Right now, it's
a simple conditional, however, the code is there to be changed to an
switch should somebody else come and add more faction-based voicelines.
/:cl:

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[a9c10b89ef...](https://github.com/harryob/cmss13/commit/a9c10b89ef77d953cd321d90675bf7dc575548a8)
#### Thursday 2023-03-23 12:36:57 by naut

Readds the autodoc, in a nerfed state (#2910)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Readds the autodoc back to the Almayer with its capabilities neutered;
it can now only do emergency treatments and cannot do advanced surgeries
like organ repair or limb replacement.

The autodoc is now only capable of the following surgeries:

- Brute and burn damage treatment
- Toxin damage treatment
- Shrapnel removal
- Closing open incisions
- Blood transfusions
- Dialysis

The following procedures have been **removed** from the autodoc and can
no longer be used:

- Internal bleeding surgery
- Corrective eye surgery
- Organ damage treatment
- Facial reconstruction
- Limb replacement
- Bone repair surgery

While we're at it, also fixed the broken icon states for the sleeper,
autodoc, and body scanner in the mapping view.

# Explain why it's good for the game

If memory serves me right, the autodoc was initially removed because it
basically acted as a doctor in and of itself, and docs would rather
shove someone inside it to do their work rather than getting their hands
dirty. This helps to change that.

This PR lets the autodoc reprise its role on the Almayer while being
restricted to an "emergency" medical system that can be used to take
some work off doctors' hands by fixing up a patient and doing, as
stated, emergency medical procedures to save their life. It can't do
complex surgeries anymore, so doctors will still need to fix patients up
for that.

# Screenshots

![image](https://user-images.githubusercontent.com/55491249/226556862-46b53693-8ca0-4f86-ba89-cdc93c2298a6.png)

# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
mapadd: Readds the autodoc back to the Almayer.
balance: Neuters the autodoc so that it can only perform emergency
treatments and life-saving procedures; it can no longer do complex
surgeries.
fix: Fixed broken icon states on the autodoc, sleeper, and body scanner
console when using a map editor.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[e47c47a081...](https://github.com/Xander3359/tgstation/commit/e47c47a081f5919eea2b43453be7ac011ee2a492)
#### Thursday 2023-03-23 12:45:43 by MrMelbert

You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

---
## [ioanaa00/Test-Engineer-opportunity](https://github.com/ioanaa00/Test-Engineer-opportunity)@[4bced537ec...](https://github.com/ioanaa00/Test-Engineer-opportunity/commit/4bced537ec6cc2ba28610e603783ace8c480de58)
#### Thursday 2023-03-23 13:15:51 by ioanaa00

Create Job decsription

For a dynamic company with a young team in the Netherlands we are looking for test engineers. Our client had impressive growth in the past 30 years resulting in employing over 1000 employees worldwide over 10 locations. In the Netherlands, they have 140 employees with nearly 50 different
nationalities. You obtain a healthy diet or you are thinking of starting one? Every week fresh fruit is delivered to the office and in your lunch breaks, you can challenge your colleagues in a game of foosball or table tennis.
Whether you commute by car or public transportation, the office is easy to reach as it is situated next to the highway and the train station.

Role description

This company has over 450 respectable clients in the gaming industry. Their clients are manufacturers of games which need to be tested according to international legislation and standards. You will be responsible for both iGaming testing and embedded testing. Every week new games need to be tested so you have a nice variety in your job. You will learn on the job until you have mastered the complete process resulting in all-round testing experience.

Role demands

• Bachelor or Master degree in Software Engineering, Computer Sciences or a comparable education
• Knowledge of Testing and working experience is an advantage
• Excellent knowledge of Java, C/ C++
• Knowledge of Python or SQL is an advantage
• You master the English language, spoken and written
• Valid working permit

Rewards

• Monthly salary of 2833
• Pension plan
• Travel allowance fully reimbursed
• Training
• 25 holidays
• International FUN working environment
• Directly employed by our client

Are you interested in delivering fair products of high quality with a diverse group of people from different nationalities? Contact Ioana Badea on +31 20 614 27 11 for more information.

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[7cad5634bf...](https://github.com/davidhildenbrand/qemu/commit/7cad5634bfb94803c575480533cb3cc5e5663ec8)
#### Thursday 2023-03-23 14:09:25 by David Hildenbrand

virtio-mem: Expose device memory via multiple memslots if enabled

Having large virtio-mem devices that only expose little memory to a VM
is currently a problem: we map the whole sparse memory region into the
guest using a single memslot, resulting in one gigantic memslot in KVM.
KVM allocates metadata for the whole memslot, which can result in quite
some memory waste.

Assuming we have a 1 TiB virtio-mem device and only expose little (e.g.,
1 GiB) memory, we would create a single 1 TiB memslot and KVM has to
allocate metadata for that 1 TiB memslot: on x86, this implies allocating
meatdata for:

(1) RMAP: ~0.2% (~2100 MiB). Not that this is optimized out with the TDP
    MMU, but will be allocated lazily when running nested VMs.
(2) gfn_track: 0.024% (~252 MiB)
(3) Bitmap when dirty-tracking: 2 x 0.003% (~63 MiB)

Consequently, using multiple memslots and only mapping the memslots we
really need can significantly reduce memory waste and speed up
memslot-related operations. Let's expose the sparse RAM memory region using
multiple memslots, mapping only the memslots we currently need into our
device memory region container.

A nice side effect is that we will expose less memory to the guest, so
a malicious guest won't be able to do that much harm and we might be
able to detect some BUGs in well-behaving guests more easily. However,
in the future we'll want to properly protect all unplugged memory from
getting reallocated (using features that have to be separately enabled).

* With VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we only map the memslots that
  actually have memory plugged, and dynamically (un)map when
  (un)plugging memory blocks.

* Without VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we always map the memslots
  covered by the usable region, and dynamically (un)map when resizing the
  usable region.

We'll auto-detect the number of memslots to use based on the remaining
available memslots and the remaining avilable size for memory devices using
our new helper. Further, we'll take care to not consume a crazy number of
memslots, because the assumption is that many memslots can degrade
performance especially in QEMU, at least right now. Let's not use more than
512 memslots per device and not use memslots smaller than 1 GiB for now.
Note that our global limit for all memory devices is currently set to
1024, so even with multiple big virtio-mem devices, we'd still have a sane
limit. We might want to fine-tune these values in the future (might have
to do via compat machine properties).

Still default to a single memslot for now, because it can be problematic in
vhost setups, and we don't want to break existing setups. We'll change
the default via compat machines in the future. Until then, this feature can
be enabled using "force-single-memslot=false".

As vhost devices are currently very limited when it comes to the number
of supported memslots, they have to be defined on the QEMU cmdline
before defining the virtio-mem devices. Otherwise, aut-detection is
unaware of the additional restriction and QEMU will bail out when
realizing the vhost device. Further, hotplug of vhost devices might
require planning ahead.

Note 1: how many memslots we'll be using is an internal implementation
detail (especially: migration is not affected), and we can change the
auto-detection as we please. Values (including "force-single-memslot") can
differ on migration source and destination.

Note 2: we should look into supporting more memslots (512 -- 1024)
especially for vhost-user soon, but that will require changes in QEMU
(to make many memslots scale better) and support in vhost-user
implementations. So we'll have to life with this vhost memslot limitation
oddity for now.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[8e49953d27...](https://github.com/davidhildenbrand/qemu/commit/8e49953d276a847daffcecc82b9ac086410eb3a6)
#### Thursday 2023-03-23 14:09:25 by David Hildenbrand

memory-device: Add a memslot soft-limit for memory devices and warn the user

While we properly check before plugging a memory device whether there
still is a free memslot, we have other memslot consumers (especially PCI
BARs) that don't perform any checks and might dynamically consume
memslots without any prior reservation later. So we might succeed in
plugging a memory device, but once we dynamically map a PCI BAR we would
be in trouble.

Let's indicate to the user that we cannot guarantee that everything will
work as intended and that we might run out of free memslots later. We'll
warn once, when we detect that there are not that many memslots around,
and once we then exceed the calculated soft-limit.

As long as we don't have to warn the user (IOW, at least 253 memslots set
aside), we don't expect surprises. Especially environments with very little
memslots (32 with vhost-user) are quite possibly problematic.

We use the historic magic memslot number of 509 as orientation to when
supporting 256 memory devices (leaving 253 for boot memory and other
devices) has been proven to work reliable. We'll warn on anything below
that for now.

We still allow to exceed the soft-limit, because there might be
reasonable setups that simply work.

We'll cap the soft-limit at 512, which no setup should currently really
exceed (ACPI supports a maximum of 256 slots). Note that the soft-limit
will be used in virtio-mem context soon, when auto-determining the number
of memslots to use.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [mauke/perl5](https://github.com/mauke/perl5)@[15119347e4...](https://github.com/mauke/perl5/commit/15119347e461bd5ff2afb671b1c8138cbe635b42)
#### Thursday 2023-03-23 14:28:15 by Yves Orton

epigraphs.pod - add epigraph from 5.37.10

My dad had beautiful handwriting, and whenever he got a new pen he would
write out this stanza of Lewis Carrolls poem on the blue lined paper he
used to write his notes on. So this is my homage to him.

For some reason I can never remember the wording properly and say it
as "to /speak/ of many things" instead of "to /talk/ of many things".
Memory is a funny thing.

---
## [zhangbopd/pytorch](https://github.com/zhangbopd/pytorch)@[11aab72dc9...](https://github.com/zhangbopd/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Thursday 2023-03-23 15:07:51 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [yegor-kirovich/SchoolGame](https://github.com/yegor-kirovich/SchoolGame)@[391ec114fe...](https://github.com/yegor-kirovich/SchoolGame/commit/391ec114fe0e9a2e2bf6d374f4df309e5cb26191)
#### Thursday 2023-03-23 15:20:07 by Zhangir

ama bug god

fuck you bugs and zhukis ama pro ama hasslo

---
## [KadTheHunter/ShulkerArchives](https://github.com/KadTheHunter/ShulkerArchives)@[30ca959a57...](https://github.com/KadTheHunter/ShulkerArchives/commit/30ca959a5780610856fd7a21fadaa179a98a0481)
#### Thursday 2023-03-23 16:17:22 by Kaddicus

FUCK YOU AND YOUR FUCKING "SMART" QUOTES VSC FUCK YOU

HOLY FUCKING SHIT I NEEEEEEEEEEEEEEEEEEEEEEEEEEEEEED TO RAID THE PERSON WHO INVENTED SMART QUOTES RIGHT THIS FUCKING MINUTE

I WILL RAID THEIR YEE YEE ASS COMPUTER FOREVER AND EVER AND IT WILL NEVER END UNTIL ALL THE FUCKING SMART QUOTES ARE DESTROYED

---
## [kcpevey/napari](https://github.com/kcpevey/napari)@[3ec4be1ae8...](https://github.com/kcpevey/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Thursday 2023-03-23 16:30:21 by Grzegorz Bokota

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[59853caf88...](https://github.com/mrakgr/The-Spiral-Language/commit/59853caf884a36b7f269466772628f330371afc6)
#### Thursday 2023-03-23 16:52:54 by Marko Grdinić

"12:55pm. This latest episode Tenten where the two girls are just crying non stop over nothing is making me cringe too hard. So Euphie's immortality will make her lose her memories and sense of self one day. Unlike the humans who...

Yeah, this situation is ridiculous to anyone with working brain cells.

1:55pm. Maybe I am cursed. Imagine if the C# and F# job situtation was switched. Or at least, if SML was popular. In that world, I'd have a lot easier time fitting in as a programmer. It feels like a huge step down to try and pick a C# job from being an F# programmer.

Maybe what I am doing now is what I wanted to be doing all along.

What I am doing right now, might be training myself to become a director. I really am interested in trying to get GPT-4 to help me write Hatred. I do not want to pay 20$ a month for access to GPT-4, but getting access to its API so I can try it cheaply could be interesting. If it works, it would increase my writing speed hugely, while increasing the quality of my prose at the same time. Personally, I couldn't care less about placing the words myself, so having an intelligent assistant doing this for me could be fun.

With Heaven's Key, I've stepped into AI art, now AI writing are music are what is left.

Let me just start.

Let me finish that video.

https://pixabay.com/music/beats-smoke-143172/

3pm. Done with the recording. It is almost 16m. I did it much fater than for any of the other videos. Now to fix the smacking in post production.

https://youtu.be/_5Khh2Z7uhM
Getting Started in Voice Over - Lessons I learned the hard way.....

This is the Creators Village guy.

https://youtu.be/_5Khh2Z7uhM?t=97
> Practice Out Loud

Technically, this is what I am doing here, since I am writing a script and then reading it out as I go along.

https://youtu.be/_5Khh2Z7uhM?t=303
> If you've made it this far, thank you very much. The number one thing that you can do to absolutely find work the fastest [as a voice actor] is to start telling everyone what you are doing!

3:10pm. Ok, let me write this down...

Current Subscribers: 18
Watch Time(hours): 24.8.

Every time I look at watch time on my Youtube dashboard, it feels like it has gone down. Wasn't it higher yesterday? My memory feels like it has been spotty lately.

3:15pm. Focus me, let me do the post processing.

I should have let the assistant train while instead of wondering around.

5:15pm. Done with the post processing. It turns out even just two regular mouth declick passes are not enough. Like in that one video, a declick pass is specifically necessary to catch some of them. Anyway, Rx Editor is really powerful. I've had some heavy mouth noises in this recording, and I managed to get rid of all of them. There was a segment that had some heavy background noise, and it got rid of all of it with a secondary pass.

Even though I am making progress, I am still not there yet as a voice actor. I need to be able to smoothly execute longer lines.

5:15pm. Right now I am uploading to Youtube. This is a great place to stop for the the day. Tomorrow, I'll implement the Monte Carlo version of CFR. It should be really easy.

5:35pm. Nhhhh...it is out.

https://youtu.be/TCa2ASFBfwg
Integrating The Counterfactual Regret Algorithm With The Leduc Game And Playing A Game Vs The Bot

Here is is, my latest masterpiece. I made a 16m video in a single day. Next time, I'll be a lot faster with preprocessing. Unlike with the previous video, I listened to this one two times from start to finish and edited out some of the individual clicks left out by the filter. I needed to do this in order to get a sense of how good they really are.

...It is really eating me that my F# sub post is at 0 votes.

https://sergeytihon.com/2023/03/18/f-weekly-11-2023-fable-4-net-8-preview-2-gpt-4/

Oh Fable 4 is out. I'll have to update the project from prerelease. Also I am spying an OpenAI API. Of course somebody would have done it already.

https://github.com/yazeedobaid/openai-fsharp

Well, nevermind it for now.

I'll leave that for the future. When it comes to text generators, I'll want to look at those character AIs that /g/ is crazy about.

2022 was such a breakthrough year for AI, just not in the way I'd have preferred.

5:45pm. Let me close here. I put in a lot of effort today. And I'll put in a lot of effort tomorrow. But now it is time to rest."

---
## [HBIDamian/AngleseyArtWeek](https://github.com/HBIDamian/AngleseyArtWeek)@[6e85940357...](https://github.com/HBIDamian/AngleseyArtWeek/commit/6e85940357f97b756d089caf944e48083735ed4a)
#### Thursday 2023-03-23 16:55:44 by HBIDamian

Replaced Images

Next up, main.js... thats gonna be a fucking pain in the ass. Curse my inefficient brain...

---
## [Gumbobrot/Rose-Injector](https://github.com/Gumbobrot/Rose-Injector)@[cdb6945a2b...](https://github.com/Gumbobrot/Rose-Injector/commit/cdb6945a2bad5ae86bb798c8274de3a0fdcec6a5)
#### Thursday 2023-03-23 17:00:36 by Gum

better sortment of imports sorry but it fucked my brain

---
## [hatcatter/HackEM](https://github.com/hatcatter/HackEM)@[0cd940eed0...](https://github.com/hatcatter/HackEM/commit/0cd940eed0f62c2d9a83aa66de98dd5cfab9741c)
#### Thursday 2023-03-23 19:09:52 by Erik Lunna

Funny message if you use Spirit Tempest as a hallucinating female necromancer.

---
## [SS7V/rustest](https://github.com/SS7V/rustest)@[d21740b475...](https://github.com/SS7V/rustest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Thursday 2023-03-23 19:55:11 by tmtmtl30

Mapgen fixes and speedups (ignore the branch name. I'm dumb) (#1637)

## About The Pull Request

Alters the structure of map/planet generation to squash some bugs and
improve performance.

Previously, planet maps were generated by placing the ruin first, and
THEN generating the turfs according to the map_generator datum. This has
been adjusted -- now, turfs are generated WITHOUT objects such as
mobs/flora, the ruin is placed, and THEN the objects are added (turfs
are "populated"). In conjunction with the addition of needed
AfterChange() calls to update the atmos adjacency of the generated
turfs, this ensures that planet atmos acts correctly surrounding ruins.

When deleting reservations (such as the deletion of planets after
undocking), all objects on the planet are rounded up in a list and
qdeleted. Although this causes a small lag spike, it SHOULD prevent
items from hanging out inside the edges of planets.

There's a feature to change the default baseturf of a virtual level,
ZTRAIT_BASETURF, that we now use. This should cut down on the instances
where a ruin on a planet is blown up and there's space underneath (might
still happen on asteroids, because the baseturf there is still space; I
didn't want space turfs without space as their baseturf).

Overmap encounter areas aren't global anymore (they no longer have the
flag UNIQUE_AREA). Don't fucking add the flag UNIQUE_AREA to anything
that should have weather in it, because if that area gets added anywhere
else that _actually respects the flag_ you'll end up with cross-planet
weather, because weather code sucks. This didn't cause bugs before,
because the flag wasn't respected; it will now.

The biome assoc list has been moved into the map generator datum, and
all encounters now generate using a map generator that either uses a
biome or replaces everything with a single turf. This prevents
duplication of cave generation code and makes dynamic overmap object
code slightly easier to understand.

Some systems have been altered to improve performance; many of these
changes are rather small, like the changes to turf population (mob
placement now uses a stack of recently-created mobs to check if there
are any nearby, instead of checking everything within 12 turfs; I've yet
to add ruin mobs to these stacks to avoid placing mobs near ruin mobs)
or lighting objects (removed a single line that changed the color of the
lighting object on init).

Starlight has been altered, so that small turf changes near space turfs
don't need to check as many nearby turfs and so that large turf changes
can be batched to prevent further recalculation. This is probably
responsible for the biggest performance increase.

Smoothing groups are cached before sorting instead of after, to prevent
sort calls on many atom inits; /tg/station uses a unit test to avoid
needing to sort at runtime ever, but I couldn't figure out how to do
that without larger changes or writing a unit test that attempted to
instance every atom once, which would be an undertaking of its own.

Gas strings have been similarly altered, and now their interpretation
defaults to copying from a cached, immutable version of the mix encoded
by the string. This avoids the significant overhead caused by repeated
calls to params2list(). Auxmos has a better solution to this,
__auxtools_parse_gas_string(), but our current custom build of Auxmos
doesn't support it.

There are a few other small changes that I'm probably forgetting about
and you should yell at me to read my own fucking code and tell you what
else I changed.

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

I still need to manually check each planet type to make sure they aren't
fucked up, I should probably do some proper profiling comparisons.

## Why It's Good For The Game

Fewer weird bugs, things generate faster, better* code.

## Changelog

:cl:
fix: Ruins don't sometimes start in hard vacuum anymore; planet turfs
now share atmos correctly.
fix: There hopefully shouldn't be any random stray objects sitting in
the edges of planets anymore.
fix: Planets now (hopefully) have the correct baseturfs (more or less).
When you bomb a ruin on a planet, it probably won't break through to
space anymore.
refactor: Planet generation has been refactored, improving performance
somewhat.
/:cl:

---
## [KadTheHunter/ShulkerArchives](https://github.com/KadTheHunter/ShulkerArchives)@[925df231f3...](https://github.com/KadTheHunter/ShulkerArchives/commit/925df231f3373c46fae7757f19479d8259f6eb0d)
#### Thursday 2023-03-23 20:06:06 by Kaddicus

Misc. Bug Fixes

Holy fucking shit my brain is swiss cheesed from this shit.

Or should that be swiss-cheesed?

Damnit, now my brain is stuck on small grammar quibbles. Thanks a lot WebStorm.

---
## [JakeHamilton33/NightClass](https://github.com/JakeHamilton33/NightClass)@[db31df4eca...](https://github.com/JakeHamilton33/NightClass/commit/db31df4eca672543724185b470b87b06e6c01f46)
#### Thursday 2023-03-23 20:15:36 by The-Guy-They-Hired-for-Art

Imported Textless Scene

Fuck you guys (jk, love ya!)

---
## [Vomgnar/cdda-arcana-mod](https://github.com/Vomgnar/cdda-arcana-mod)@[1ab8a3bafd...](https://github.com/Vomgnar/cdda-arcana-mod/commit/1ab8a3bafd35fa2bedd11030e8806fa7716c5488)
#### Thursday 2023-03-23 20:22:26 by Chaosvolt

Major NPCs teach spells, now with 200% less weirdness

Implemented a few dialogue additions such that certain NPCs can offer to teach the player specific Magic Signs, many of them favoring stuff the player could otherwise only get via profession or in chargen. Uses trait and dialogue stuff, because Korg's mechanics for learning spells from NPCs has some jank to it.

* If you've reached a given point in his mission chain, Alexander can offer to teach you Free Action, Phase Shield, and Transcendent Aura.
* After doing any mission for the rural church holdout, Sofia can teach you Heat Ward, Poison Armor, or Ward Against Evil.
* Likewise, once the Arcane Purifier NPCs show up Nicholas can be asked to teach you Capacitance, Consecrate, or Opening.
* Set aside traits used to dole out post-chargen Capacitance and Transcendent Aura, and also split the Keeper profession trait into two difference ones so the hermit can track if you would've started with it or not (characters in old saves will be overlooked though).
* Misc, fixed a typo that was widely copy-pasted into a lot of magic sign descriptions.

Will add spell menu for Celine later on, is late so weh.

---
## [realkhad/cmss13](https://github.com/realkhad/cmss13)@[558717e6f6...](https://github.com/realkhad/cmss13/commit/558717e6f627bf2bdc8e00c620db04c0a55cede0)
#### Thursday 2023-03-23 20:42:55 by zeroisthebiggay

(hopefully) webedits a grammatical correction into headbite's kill message (#2537)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

when someone dies to headbite it displays as
`Urr Mot'herr has died to executed by headbite at the Containers from
Elder Lurker (GIT-222)`
hopefully with this simple one line webedit it should instead be
`Urr Mot'herr has died to headbite execution at the Containers from
Elder Lurker (GIT-222)`
god fucking knows if this is the right line

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

uhm
it reads better

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

github

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
spellcheck: 'executed by headbite' to 'headbite execution' when listing
someone dying to a headbite in deadchat
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [realkhad/cmss13](https://github.com/realkhad/cmss13)@[4ce115a2a2...](https://github.com/realkhad/cmss13/commit/4ce115a2a26f8b6664a230bdaff483a1889f17c4)
#### Thursday 2023-03-23 20:42:55 by carlarctg

Adds Ludicrously In-Depth Black Market to Recquisitions. (#2014)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

VASTLY enhances the Black Market. Black market items are obtainable by
deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.

Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...

Various valuable, rare, or otherwise interesting items now have a 'black
market value' that allows them to be sent down the ASRS elevator in
exchange for black market points to order various things with. Anything
that's 'rare' is probably worth something. Added a scanner to the black
market to let them detect said points.

Added DIALOGUE to the black market.

FIxed some construction wirecutter steps needing a screwdriver for some
reason.

Changed up Req's mapping to add a hidden storage room.

slightly changed human remains' description

Added the maintenance jack, can be found in the black market for now.

Improved supply shuttle code somewhat.

# Explain why it's good for the game

> VASTLY enhances the Black Market. Black market items are obtainable by
deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.

Black Market is comically underused, by comically enhancing it like this
it will freshen shipside roleplay and create new and interesting
scenarios for MPs, req, and bystanders to interact with.

> Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...

The contraband needs to be actually meaningful to the players for it to
have any impact. The list of loot has been curated so that players will
be intrigued, but will not be able to abuse it for
too-stronger-than-usual gear without blatant drawbacks.

> Various valuable, rare, or otherwise interesting items now have a
'black market value' that allows them to be sent down the ASRS elevator
in exchange for black market points to order various things with. Added
a scanner to the black market to let them detect said points.

This means CTs could go on scavenger hunts through the ship, evading
curious MPs to sift through maintenance and various hidey holes scanning
everything.

> Added DIALOGUE to the black market.

Finally, we have dialogue in CM! The very first human NPC. We're
ignoring WO because nobody likes WO.

> FIxed some construction wirecutter steps needing a screwdriver for
some reason.

Necessary in this PR to avoid stupid confusion when deconstructing the
computers.

> Changed up Req's mapping to add a hidden storage room.

To let CTs hide their goodies so they won't be in open sight. NOT DONE
YET!

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: VASTLY enhances the Black Market. Black market items are obtainable
by deconstructing a supply computer and pulsing the circuit board. If
you're knowledgeable in engineering enough.
add: Added a whole new category for black market items and thoroughly
enhanced the possible contraband items to order. Guns, drugs, and worse
are plentiful in stock...
add: Various valuable, rare, or otherwise interesting items now have a
'black market value' that allows them to be sent down the ASRS elevator
in exchange for black market points to order various things with.
Anything that's 'rare' is probably worth something. Added a scanner to
the black market to let them detect said points.
add: Added DIALOGUE to the black market.
fix: FIxed some construction wirecutter steps needing a screwdriver for
some reason.
spellcheck: slightly changed human remains' description
add: Added the maintenance jack, can be found in the black market for
now.
code: Improved supply shuttle code somewhat.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: XSlayer300 <35091844+XSlayer300@users.noreply.github.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[5a34d92cb5...](https://github.com/microsoft/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Thursday 2023-03-23 20:44:06 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[b533ada0e6...](https://github.com/TaleStation/TaleStation/commit/b533ada0e64f0cf25a3874a065291a9e889c8c52)
#### Thursday 2023-03-23 21:06:30 by TaleStationBot

[MIRROR] [MDB IGNORE] The Lance Crew Evacuation System (New Emergency Shuttle) (#5019)

Original PR: https://github.com/tgstation/tgstation/pull/74024
-----
## About The Pull Request
Yeah this shuttle deliberately hits the station.
While more hazardous to people in departures, the Lance is a great
crew-friendly tool for a station that has a severely damaged departures!
No longer will you need to struggle with firelocks and collapse just
outside the shuttle in a depressurized departures, when The Lance comes
RIGHT TO YOU.

<details>
<summary> The Lance being used </summary>


![image](https://cdn.discordapp.com/attachments/585862469508005888/1087777600535003266/image.png)

</details>

<details>

<summary> Map screenshot! </summary>


![image](https://user-images.githubusercontent.com/73589390/226687950-3844ade3-ee90-4056-b923-c1a9b460eb61.png)

</details>

### Mapping March
Ckey to receive rewards: Cheshify 
I don't need a token or anything, but the GBP or whatever would be nice
so I can make more map stuff

## Why It's Good For The Game

New shuttles are good! This one has both immense pros (very safe when
you're inside it, lots of supplies) and immense cons (smashes into the
fucking station). It'll be an interesting purchase for the antagonist
using it to kill a bunch of people in departures, and a useful tool for
the crew making it easier for them to evacuate.

This shuttle is not restricted to emags or any other prerequisite, as
that would defeat the purpose. It's supposed to be a mixture of pros and
cons, and keeping it locked behind an emag removes it's use as a
prohibitively expensive but ultimately useful tool for the crew.
## Changelog
:cl:
add: Nanotrasen has given the crew access to a brand new emergency
shuttle! Watch out for it's destructive entrance!
/:cl:

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>

---
## [Zaidannaim91/Shituzhi](https://github.com/Zaidannaim91/Shituzhi)@[23b84430dc...](https://github.com/Zaidannaim91/Shituzhi/commit/23b84430dca37b4a9f21725e521f11597d5ffcc2)
#### Thursday 2023-03-23 21:07:02 by Zaidannaim91

Create [Shituzhi] I Spent the Whole Time Fucking My Girlfriend's Friend While She Went on a Trip

---
## [veggiemonk/awesome-docker](https://github.com/veggiemonk/awesome-docker)@[3164d6df94...](https://github.com/veggiemonk/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Thursday 2023-03-23 21:07:37 by Derek Lee

Add Kurtosis to list of testing tools (#1063)

* Add Kurtosis to list of testing tools

Hey team! We'd like to add Kurtosis to the list of testing tools. 

*What is Kurtosis?* Kurtosis is a built system for multi-(docker)container test environments. 
*What is Kurtosis for?* Kurtosis is for engineers who dev against large distributed systems/applications and who experience pain when trying to configure multi (Docker) container environments for their testing workflows. 

Kurtosis can be used locally without the need to sign up and is free-forever under a source-available license (BSL). 

We have:
- Linked out to our Github: https://github.com/kurtosis-tech/kurtosis
- [A README on our GIthub](https://github.com/kurtosis-tech/kurtosis#readme)
- Content about how to setup/install the project (in our [Github README](https://github.com/kurtosis-tech/kurtosis#to-start-using-kurtosis) and on our [docs](https://docs.kurtosis.com/install)),
- Lots of great examples on: [Github](https://github.com/kurtosis-tech/awesome-kurtosis#awesome-kurtosis-) and in our [docs](https://docs.kurtosis.com/). 

I followed the [Quality Standards](https://github.com/veggiemonk/awesome-docker/blob/master/.github/CONTRIBUTING.md#quality-standards) you guys wrote, but please let me know if you've got any questions about Kurtosis or if we missed something!

Thanks

* add "composable" to description

---
## [nz-m/react](https://github.com/nz-m/react)@[b6978bc38f...](https://github.com/nz-m/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Thursday 2023-03-23 21:35:06 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [ROCmSoftwarePlatform/rocMLIR](https://github.com/ROCmSoftwarePlatform/rocMLIR)@[e1d73990a3...](https://github.com/ROCmSoftwarePlatform/rocMLIR/commit/e1d73990a38d40b022ae00c9f85e725baf995dfb)
#### Thursday 2023-03-23 21:45:57 by Krzysztof Drewniak

Use COMgr to compile our GPU binaries

Since we're considering shipping as a ROCm package, I've investigated
if it's possible to use COMgr instead of shipping our own copy of
LLVM.

This branch shows that it's possible, but I'm not convinced we want to
merge it.

The good news is that the setup works.

The bad news is that, because our LLVM copy is *newer* than the one
shipped in ROCm 5.4 (which is what we're using for our CI) we'll
sometimes need to **downgrade** the LLVM IR we produce to be
acceptable input to ROCm's LLVM. If theirs were newer, it'd be fine,
because LLVM has strong backwards compatibility guarantees, but this
is the other direction.

On top of that, I had to do a few ugly hacks to make COMgr do the
compiler invocations we want.

So ... yeah.

---
## [canonical/operator](https://github.com/canonical/operator)@[ecb9ca1163...](https://github.com/canonical/operator/commit/ecb9ca1163a3618448e797af645b2e1bd38255ed)
#### Thursday 2023-03-23 21:51:13 by Ben Hoyt

Import (almost) all public names in ops __init__.py (#910)

This is to address #731: it's hard to remember or discover which `ops`
sub-module (like `ops.charm` or `ops.framework`) a name comes from.
That, and imports become a bit of a mess (`from ops.charm import X;
from ops.framework import Y; from ops.main import main`).

In my view we had previously split them up somewhat arbitrarily
(eg: `FooEvent` types are in `ops.charm`, but they could just as well
be in `ops.framework`). I considered a different, more logical
sub-module arrangement, but I think it'd still be hard to remember
and know where things were.

This solution is simple: import all the public names into the
top-level `ops` module in the `__init__.py` file. They're quite
unique, so there's no conflicts. The only exception is `ops.pebble`,
whose names aren't imported there (most charms don't use `ops.pebble`
directly anyway, they use it via `model.Container`, but if you need
it its still readily importable).

This makes all the names easily discoverable, either by looking in
`ops/__init__.py` manually, or via your editor's code completion when
you've done `import ops`. I expect that many charms will change to
just `import ops` and access names like `ops.CharmBase` (`ops` is a
nice short prefix) ... see [this PR on my database test charm]
(https://github.com/benhoyt/test-charms/pull/1/files) for an example
of what that would look like.

Folks can also use explicit imports like `from ops import CharmBase`
if they prefer. And of course the existing usage `from ops.charm
import CharmBase` still works fine too.

The one quirky thing is that `ops.main` is currently a module, but we
want to allow `import ops ... ops.main()` or `from ops import
main ... main()`. To solve this we've main the main module callable
(and it just calls the `main` function). This allows the new usage,
but also allows the existing usages `from ops.main import main ...
main()` and  `import ops.main ... main.main()` to continue working.

### Testing note

The user-facing changes here are all done in `ops/__init__.py` and
`ops/main.py`, but I've also updated the `test/test_*.py` files to
show using the single `import ops` approach (partly to set that as a
precedent).

However, I ran all the previous, unmodified tests against the new
`ops/__init__.py`, and they all pass. This ensures that I haven't
messed anything up, including the `main` shenanigans mentioned
above.

Fixes #731.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[68e3077b0a...](https://github.com/git-for-windows/git/commit/68e3077b0add660a05eb6eaad4b4462e075a8e78)
#### Thursday 2023-03-23 21:54:10 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [Abraham-The-Blooket-Hacker/Abraham](https://github.com/Abraham-The-Blooket-Hacker/Abraham)@[c839688368...](https://github.com/Abraham-The-Blooket-Hacker/Abraham/commit/c839688368c6db9bfaa49ec353b8f49d2a6f4eb4)
#### Thursday 2023-03-23 21:57:50 by Abraham-The-Blooket-Hacker

BLOOKET HACK

javascript:/* All terms found in the following link apply: https://github.com/Minesraft2/Blooket-Cheats/blob/main/LICENSE */ (async()=>{var t,d,p,u,m,h,g,b=document.createElement("iframe");if(document.body.append(b),window.confirm=b.contentWindow.confirm.bind(window),window.console.log=b.contentWindow.console.log.bind(window),b.style.display="none",await Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a.get("https://"+(location.host.startsWith("dashboard")?location.host+"/api/games":"play.blooket.com/api/gamequestionsets")+"?gameId=6368436a976422d8a3f70cd7").then(e=>parseInt("0"+e.data.questions.find(e=>"../cheats/gui.js"==e.question)?.answers?.[0]))<1679521365129||confirm("This cheat is outdated and might be bugged, would you still like to run it? You can find regularly updated cheats here https://github.com/Minesraft2/Blooket-Cheats")){function f(e,t={},...a){var o=document.createElement(e);if("object"==typeof t.style){let e="";for(const n in t.style)e+=`${n.replace(/[A-Z]/g,e=>"-"+e.toLowerCase())}: ${t.style[n]}; `;t.style=e}for(const i in t)o[i]=t[i];for(const r of a)o.append(r);return o}console.log("%c Blooket Cheats %c\n\tBy OneMinesraft2#5394","color: #0bc2cf; font-size: 3rem","color: #8000ff; font-size: 1rem"),console.log("%c\tgui.js","color: #0bc2cf; font-size: 1rem"),console.log("%c\tStar the github repo!%c  https://github.com/Minesraft2/Blooket-Cheats","color: #ffd000; font-size: 1rem","");const j={data:null,setItem(e,n){return e.split(".").reduce((e,t,a,o)=>(++a==o.length&&(e[t]=n),e[t]),this.data),localStorage.setItem("JODGUISettings",JSON.stringify(this.data)),this.data},deleteItem(e){return e.split(".").reduce((e,t,a,o)=>(++a==o.length&&delete e[t],e[t]),this.data),localStorage.setItem("JODGUISettings",JSON.stringify(this.data)),this.data},setData(e){this.data=e,localStorage.setItem("JODGUISettings",JSON.stringify(this.data))}};try{j.data=JSON.parse(localStorage.getItem("JODGUISettings")||"{}");for(const N of["backgroundColor","cheatList","contentBackground","defaultButton","disabledButton","enabledButton","infoColor","inputColor","textColor"])j.data[N]&&(j.setItem("theme."+N,j.data[N]),j.deleteItem(N))}catch{j.setData({})}let a,o,i,l,n,e,r,v,s;const M=f("div",{id:"JODGUI",style:{top:Math.max(10,window.innerHeight-600)/2+"px",left:Math.max(10,window.innerWidth-1e3)/2+"px",transform:`scale(${j.data.scale})`,position:"fixed",height:"80%",width:"80%",maxHeight:"600px",maxWidth:"1000px",zIndex:"999",display:"block"}},a=f("style",{id:"variables",innerHTML:`:root {--backgroundColor: ${j.data?.theme?.backgroundColor||"rgb(11, 194, 207)"};--infoColor: ${j.data?.theme?.infoColor||"#9a49aa"};--cheatList: ${j.data?.theme?.cheatList||"#9a49aa"};--defaultButton: ${j.data?.theme?.defaultButton||"#9a49aa"};--disabledButton: ${j.data?.theme?.disabledButton||"#A02626"};--enabledButton: ${j.data?.theme?.enabledButton||"#47A547"};--textColor: ${j.data?.theme?.textColor||"white"};--inputColor: ${j.data?.theme?.inputColor||"#7a039d"};--contentBackground: ${j.data?.theme?.contentBackground||"rgb(64, 17, 95)"};}`}),f("style",{innerHTML:'.alertList::-webkit-scrollbar{display:none;}.alertList{-ms-overflow-style: none;scrollbar-width: none;}.contentWrapper::-webkit-scrollbar{display:none;}.contentWrapper{-ms-overflow-style: none;scrollbar-width: none;}.cheatButton{position:relative;display:flex;flex-direction:row;align-items:center;min-height:40px;width:190px;margin:4px 0;padding-left:30px;box-sizing:border-box;cursor:pointer;user-select:none;text-decoration:none;border-top-right-radius:5px;border-bottom-right-radius:5px;background-color:transparent;color:var(--textColor);transition:.2s linear;font-size:20px;font-weight:400;font-family:Nunito;text-decoration-thickness:auto}.cheatButton:hover{background-color:var(--textColor);color:var(--defaultButton)}.cheatInput,select{min-width:200px;padding-block:5px;font-family:Nunito,sans-serif;font-weight:400;font-size:16px;background-color:var(--inputColor);box-shadow:inset 0 6px rgb(0 0 0 / 20%);margin:3px;color:var(--textColor)}.bigButton:hover{filter:brightness(110%);transform:translateY(-2px)}.bigButton:active{transform:translateY(2px)}.cheatList::-webkit-scrollbar{width:10px}.cheatList::-webkit-scrollbar-track{background:var(--cheatList)}.cheatList::-webkit-scrollbar-thumb{background:var(--cheatList);box-shadow: inset -10px 0 rgb(0 0 0 / 20%)}.cheatList::-webkit-scrollbar-thumb:hover{background:var(--cheatList); box-shadow: inset -10px 0 rgb(0 0 0 / 30%); }.scriptButton:hover{filter:brightness(120%)}.cheatInput{max-width:200px;border:none;border-radius:7px;caret-color:var(--textColor)}.cheatInput::placeholder{color:var(--textColor)}.cheatInput:focus,select:focus{outline:0}.cheatInput::-webkit-inner-spin-button,.cheatInput::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}.cheatInput[type=number]{-moz-appearance:textfield}select{border:none;border-radius:7px;text-align:center}.scriptButton{align-items: center; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; margin: 10px; padding: 5px 5px 11px; position: relative; width: 250px; font-family: Nunito, sans-serif; font-weight: 400; color: var(--textColor); box-shadow: inset 0 -6px rgb(0 0 0 / 20%); border-radius: 7px; cursor: pointer; transition: filter .25s;}.tooltip::after {content: "";position: absolute;width: 10px;height: 10px;background-color: inherit;top: -5px;left: 50%;margin-left: -6px;transform: rotate(135deg)}'}),o=f("div",{style:{width:"100%",height:"100%",position:"relative",outline:"3px solid #3a3a3a",borderRadius:"15px",overflow:"hidden"}},f("div",{id:"background",style:{display:"block",top:"0",left:"0",height:"100%",overflowY:"hidden",overflowX:"hidden",position:"absolute",width:"100%",background:"var(--backgroundColor)",visibility:"visible"}},f("div",{id:"backgroundImage",style:{backgroundImage:"url(https://ac.blooket.com/dashboard/65a43218fd1cabe52bdf1cda34613e9e.png)",display:"block",height:"200%",position:"absolute",width:"200%",top:"50%",left:"50%",backgroundPositionX:"-100px",backgroundPositionY:"-100px",backgroundSize:"550px",visibility:"visible",transform:"translate(-50%,-50%) rotate(15deg)",appearance:"none",opacity:"0.175"}})),l=f("div",{id:"controls",style:{display:"flex",alignItems:"center",justifyContent:"center",paddingBottom:"8px",paddingInline:"15px",position:"absolute",left:"220px",top:"0",visibility:"visible",zIndex:"5",height:"52px",width:"max-content",background:"var(--infoColor)",boxShadow:"inset 0 -8px rgb(0 0 0 / 20%), 0 0 4px rgb(0 0 0 / 15%)",borderBottomRightRadius:"10px",color:"var(--textColor)",fontFamily:"Nunito, sans-serif",fontWeight:"700",userSelect:"text"},innerText:([{ctrl:b,shift:t,alt:d,key:p},{ctrl:u,shift:m,alt:h,key:g}]=[j.data.hide||{ctrl:!0,key:"e"},j.data.close||{ctrl:!0,key:"x"}],`${[b&&"Ctrl",t&&"Shift",d&&"Alt",p&&p.toUpperCase()].filter(Boolean).join(" + ")} to hide | ${[u&&"Ctrl",m&&"Shift",h&&"Alt",g&&g.toUpperCase()].filter(Boolean).join(" + ")} for quick disable\nClick and drag here`),update:({ctrl:e,shift:t,alt:a,key:o}={ctrl:!0,key:"e"},{ctrl:n,shift:i,alt:r,key:s}={ctrl:!0,key:"x"})=>l.innerText=`${[e&&"Ctrl",t&&"Shift",a&&"Alt",o&&o.toUpperCase()].filter(Boolean).join(" + ")} to hide | ${[n&&"Ctrl",i&&"Shift",r&&"Alt",s&&s.toUpperCase()].filter(Boolean).join(" + ")} for quick disable\nClick and drag here`}),f("div",{id:"credits",style:{display:"flex",alignItems:"center",justifyContent:"center",paddingBottom:"8px",position:"absolute",right:"0",top:"0",visibility:"visible",zIndex:"5",height:"47px",width:"280px",background:"var(--infoColor)",boxShadow:"inset 0 -8px rgb(0 0 0 / 20%), 0 0 4px rgb(0 0 0 / 15%)",borderBottomLeftRadius:"10px",color:"var(--textColor)",fontFamily:"Nunito, sans-serif",fontWeight:"700",userSelect:"text"},innerHTML:"Created by OneMinesraft2#5372"}),n=f("div",{id:"controlButtons",style:{display:"flex",alignItems:"center",justifyContent:"center",position:"absolute",right:"0",bottom:"0",visibility:"visible",zIndex:"5",height:"55px",width:"165px",background:"#none",borderLeft:"3px solid black",borderTop:"3px solid black",borderTopLeftRadius:"10px",color:"white",fontFamily:"Nunito, sans-serif",fontWeight:"700",userSelect:"text",overflow:"hidden",pointerEvents:"all"}},e=f("button",{style:{height:"55px",width:"55px",fontFamily:"Nunito",color:"white",backgroundColor:"#00a0ff",border:"none",fontSize:"2rem",cursor:"move"},innerHTML:"✥"}),f("button",{style:{height:"55px",width:"55px",fontFamily:"Nunito",color:"white",backgroundColor:"grey",border:"none",fontSize:"2rem",fontWeight:"bolder",cursor:"pointer"},innerHTML:"-",onclick:function(){let t=!1;return()=>{for(var e of[...o.children])e!=n&&(t?e.style.display=e.style._display:(e.style._display=e.style.display,e.style.display="none"));o.style.height=t?"100%":"55px",o.style.width=t?"100%":"165px",M.style.top=parseInt(M.style.top)+(M.offsetHeight-55)*(t?-1:1)+"px",M.style.left=parseInt(M.style.left)+(M.offsetWidth-165)*(t?-1:1)+"px",M.style.pointerEvents=t?"unset":"none",t=!t}}()}),f("button",{style:{height:"55px",width:"55px",fontFamily:"Nunito",color:"white",backgroundColor:"red",border:"none",fontSize:"2rem",fontWeight:"bolder",cursor:"pointer"},innerHTML:"X",onclick:x})),i=f("div",{className:"cheatList",style:{overflowY:"scroll",background:"var(--cheatList)",boxShadow:"inset -10px 0 rgb(0 0 0 / 20%)",zIndex:"5",width:"220px",position:"absolute",top:"0",left:"0",height:"100%",fontFamily:"Titan One",color:"var(--textColor)",fontSize:"40px",textAlign:"center",paddingTop:"20px",userSelect:"none",padding:"20px 10px 20px 0",boxSizing:"border-box",display:"flex",flexDirection:"column"},innerHTML:'<span style="text-shadow: 1px 1px rgb(0 0 0 / 40%)">Cheats</span>'},f("a",{className:"bigButton",style:{cursor:"pointer",display:"block",fontFamily:"Titan One",margin:"20px auto 10px",position:"relative",transition:".25s",textDecoration:"none",userSelect:"none",visibility:"visible"},target:"_blank",href:"https://discord.gg/QznzysxvX4",innerHTML:`<div style="background: rgba(0,0,0,.25); border-radius: 5px; display: block; width: 100%; height: 100%; left: 0; top: 0; position: absolute; transform: translateY(2px); width: 100%; transition: transform .6s cubic-bezier(.3,.7,.4,1)"></div>\n    <div style="background-color: rgb(11, 194, 207); filter: brightness(.7); position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 5px;"></div>\n    <div style="font-weight: 400; background-color: rgb(11, 194, 207); color: white; display: flex; flex-direction: row; align-items: center; justify-content: center; text-align: center; padding: 5px; border-radius: 5px; transform: translateY(-4px); transition: transform .6s cubic-bezier(.3,.7,.4,1)">\n    <div style="font-family: Titan One, sans-serif; color: white; font-size: 26px; text-shadow: 2px 2px rgb(0 0 0 / 20%); height: 40px; padding: 0 15px; display: flex; flex-direction: row; align-items: center; justify-content: center">\n        <svg style="filter: drop-shadow(2px 2px 0 rgb(0 0 0 / 20%))" xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" viewBox="0 -1 21 16">\n            <path d="M13.545 2.907a13.227 13.227 0 0 0-3.257-1.011.05.05 0 0 0-.052.025c-.141.25-.297.577-.406.833a12.19 12.19 0 0 0-3.658 0 8.258 8.258 0 0 0-.412-.833.051.051 0 0 0-.052-.025c-1.125.194-2.22.534-3.257 1.011a.041.041 0 0 0-.021.018C.356 6.024-.213 9.047.066 12.032c.001.014.01.028.021.037a13.276 13.276 0 0 0 3.995 2.02.05.05 0 0 0 .056-.019c.308-.42.582-.863.818-1.329a.05.05 0 0 0-.01-.059.051.051 0 0 0-.018-.011 8.875 8.875 0 0 1-1.248-.595.05.05 0 0 1-.02-.066.051.051 0 0 1 .015-.019c.084-.063.168-.129.248-.195a.05.05 0 0 1 .051-.007c2.619 1.196 5.454 1.196 8.041 0a.052.052 0 0 1 .053.007c.08.066.164.132.248.195a.051.051 0 0 1-.004.085 8.254 8.254 0 0 1-1.249.594.05.05 0 0 0-.03.03.052.052 0 0 0 .003.041c.24.465.515.909.817 1.329a.05.05 0 0 0 .056.019 13.235 13.235 0 0 0 4.001-2.02.049.049 0 0 0 .021-.037c.334-3.451-.559-6.449-2.366-9.106a.034.034 0 0 0-.02-.019Zm-8.198 7.307c-.789 0-1.438-.724-1.438-1.612 0-.889.637-1.613 1.438-1.613.807 0 1.45.73 1.438 1.613 0 .888-.637 1.612-1.438 1.612Zm5.316 0c-.788 0-1.438-.724-1.438-1.612 0-.889.637-1.613 1.438-1.613.807 0 1.451.73 1.438 1.613 0 .888-.631 1.612-1.438 1.612Z"/>\n        </svg>\n        Discord\n    </div>\n    </div>`})),f("div",{className:"contentWrapper",style:{position:"absolute",left:"220px",top:"70px",overflowY:"scroll",width:"calc(100% - 220px)",height:"calc(100% - 70px)",borderRadius:"7px"}},f("div",{id:"content",style:{position:"absolute",inset:"27px 50px 50px 50px"}},r=f("div",{className:"tooltip",style:{position:"absolute",top:"0",left:"0",backgroundColor:"black",height:"fit-content",maxWidth:"300px",zIndex:"5",borderRadius:"7.5px",color:"white",display:"flex",justifyContent:"center",alignItems:"center",padding:"5px",paddingInline:"15px",pointerEvents:"none",opacity:"0",textAlign:"center"},innerText:"description"}),v=f("div",{style:{alignItems:"center",boxSizing:"border-box",display:"flex",flexDirection:"row",flexWrap:"wrap",justifyContent:"space-evenly",padding:"20px 5px 20px",position:"relative",width:"100%",fontFamily:"Nunito, sans-serif",fontWeight:"400",color:"var(--textColor)",background:"var(--contentBackground)",boxShadow:"inset 0 -6px rgb(0 0 0 / 20%)",borderRadius:"7px"}},s=f("div",{className:"headerText",style:{boxSizing:"border-box",display:"block",height:"45px",left:"-10px",padding:"4px 4px 8px",position:"absolute",top:"-28px",backgroundColor:"#ef7426",boxShadow:"0 4px rgb(0 0 0 / 20%), inset 0 -4px rgb(0 0 0 / 20%)",borderRadius:"7px"}},f("div",{style:{alignItems:"center",boxSizing:"border-box",display:"flex",height:"100%",justifyContent:"center",padding:"0 15px",width:"100%",fontFamily:"Titan One, sans-serif",fontSize:"26px",fontWeight:"400",textShadow:"-1px -1px 0 #646464, 1px -1px 0 #646464, -1px 1px 0 #646464, 2px 2px 0 #646464",color:"white",background:"linear-gradient(#fcd843,#fcd843 50%,#feb31a 50.01%,#feb31a)",borderRadius:"5px"}})))))));for(const T of document.querySelectorAll("#JODGUI"))T.remove();function y(e,t,a,o){const n=f("div",{className:"cheatButton",innerHTML:("string"==typeof t?`<img style="height: 30px; margin-right: 5px" src="${t}">`:t||"")+e,onclick:()=>w(n.innerText,a,o)});return i.appendChild(n),n.onclick}async function w(e,l,t){v.innerHTML="",s.firstChild.innerText=e+(t?"":" Cheats"),v.append(s);for(let s=0;s<l.length;s++){let{name:e,description:t,type:a,inputs:o,enabled:n,run:i,element:r}=l[s];if(!r){const g=f("div",{className:"scriptButton",style:{background:"toggle"==a?n?"var(--enabledButton)":"var(--disabledButton)":"var(--defaultButton)"}},f("div",{className:"cheatName",innerHTML:e}));if(g.dataset.description=t,o?.length)for(let t=0;t<o.length;t++){var{name:c,type:d,options:p,min:u,max:m,value:h}=o[t];let e;try{e=await("function"==typeof p?p?.():p)}catch{e=[]}if("options"==d&&e?.length){const b=document.createElement("select");e.forEach(e=>{var t=document.createElement("option");t.value=JSON.stringify(e?.value||e),t.innerHTML=e?.name||e,b.appendChild(t)}),g.appendChild(b)}else if("function"==d){const y=document.createElement("input");y.classList.add("cheatInput"),y.placeholder=c,y.style.textAlign="center";let e=!(y.readOnly=!0);y.onclick=async()=>{e||(y.value="Waiting for input...",e=!0,y.data=await o[t].function(e=>y.value=e+"..."),e=!1,y.value=y.value.slice(0,-3))},g.appendChild(y)}else{p=document.createElement("input");p.classList.add("cheatInput"),"number"==d&&(p.type="number",p.min=u,p.max=m,p.value=h||(null!=u?u:0)),p.placeholder=c,p.style.textAlign="center",g.appendChild(p)}}g.onclick=function({target:e}){e!=g&&!e.classList.contains("cheatName")||(e=[...g.children].slice(1),i.apply(this,e.map(e=>"number"==e.type?parseInt("0"+e.value):"SELECT"==e.nodeName?JSON.parse(e.value):e.data||e.value)),"toggle"==a&&(g.style.background=this.enabled?"var(--enabledButton)":"var(--disabledButton)"),O.alerts?.[0].addLog(`${"toggle"==a?this.enabled?"Enabled":"Disabled":"Ran"} <strong>${this.name}</strong>`+(o?.length?` with inputs: (${e.map(e=>"SELECT"==e.nodeName?e.selectedOptions[0].innerText:e.value).join(", ")})`:""),"toggle"==a?this.enabled?"var(--enabledButton)":"var(--disabledButton)":null))}.bind(l[s]),l[s].element=g}v.appendChild(l[s].element)}}document.body.appendChild(M);const O={global:[{name:"Auto Answer (Toggle)",description:"Toggles auto answer on",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{var{state:{question:e,stage:t,feedback:a},props:{client:{question:o}}}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];const n=e||o;try{"typing"!=n.qType?("feedback"===t||a?document.querySelector('[class*="feedback"]')?.firstChild:[...document.querySelectorAll('[class*="answerContainer"]')][n.answers.map((e,t)=>n.correctAnswers.includes(e)?t:null).filter(e=>null!=e)[0]])?.click?.():Object.values(document.querySelector("[class*='typingAnswerWrapper']"))[1].children._owner.stateNode.sendAnswer(n.answers[0])}catch{}},50))}},{name:"Highlight Answers (Toggle)",description:"Toggles highlight answers on",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{const{state:a,props:o}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];[...document.querySelectorAll('[class*="answerContainer"]')].forEach((e,t)=>{(a.question||o.client.question).correctAnswers.includes((a.question||o.client.question).answers[t])?e.style.backgroundColor="rgb(0, 207, 119)":e.style.backgroundColor="rgb(189, 15, 38)"})},50))}},{name:"Auto Sell Dupes On Open",description:"Sells the blook you unlock when you open a pack if you already have one (Doesn't sell Legendaries or rarer)",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,XMLHttpRequest.prototype.open=this.data):(this.enabled=!0,this.data=XMLHttpRequest.prototype.open,XMLHttpRequest.prototype._original_open||=XMLHttpRequest.prototype.open,XMLHttpRequest.prototype.open=function(){this.addEventListener("load",async function(){try{var e,t,a,o,n;"https://dashboard.blooket.com/api/users/unlockblook"===this.responseURL&&(e=Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a,t=webpackJsonp.push([[],{rarity:(e,t,a)=>{t.rarity=e=>a("MDrD").a[e].rarity}},[["rarity"]]])["rarity"],a=JSON.parse(this.response)["unlockedBlook"],{name:o,unlocks:n}=(await e.get("https://dashboard.blooket.com/api/users"))["data"],n[a]&&!["Legendary","Chroma","Mystical"].includes(t(a)))&&(await e.put("https://dashboard.blooket.com/api/users/sellblook",{name:o,blook:a,numSold:1}),console.log("Sold duplicate "+a))}catch{}}),XMLHttpRequest.prototype._original_open.apply(this,arguments)})}},{name:"Auto Answer",description:"Click the correct answer for you",run:function(){const{state:{question:a,stage:e,feedback:t},props:{client:{question:o}}}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];try{"typing"!=a.qType?("feedback"===e||t?document.querySelector('[class*="feedback"]')?.firstChild:[...document.querySelectorAll('[class*="answerContainer"]')][(a||o).answers.map((e,t)=>(a||o).correctAnswers.includes(e)?t:null).filter(e=>null!=e)[0]])?.click?.():Object.values(document.querySelector("[class*='typingAnswerWrapper']"))[1].children._owner.stateNode.sendAnswer(a.answers[0])}catch{}}},{name:"Spam Buy Blooks",description:"Opens a box an amount of times",inputs:[{name:"Box",type:"options",options:()=>new Promise(e=>{e(Object.keys(Object.values(webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]]).webpack.c).find(e=>e?.exports?.a?.Safari)?.exports.a||{}))})},{name:"Amount",type:"number"}],run:function(o,n){var e=document.createElement("iframe"),i=(document.body.append(e),window.alert=e.contentWindow.alert.bind(window),window.prompt=e.contentWindow.prompt.bind(window),window.confirm=e.contentWindow.confirm.bind(window),e.remove(),Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache)),c=i.find(e=>e.exports?.a?.get).exports.a;o=o.split(" ").map(e=>e.charAt(0).toUpperCase()+e.slice(1).toLowerCase()).join(" "),c.get("https://dashboard.blooket.com/api/users").then(async({data:{name:e,tokens:t}})=>{var a=i.find(e=>e?.exports?.a?.Safari)?.exports?.a||{Medieval:15,Breakfast:15,Wonderland:15,Space:20,Bot:20,Aquatic:20,Safari:20,Dino:25,"Ice Monster":25};let l=Math.min(Math.floor(t/a[o]),n);if(0==l)0<n&&alert("You do not have enough tokens!");else{let i=confirm("Would you like to alert blooks upon unlocking?"),r={},s=Date.now(),t=!1;for(let n=0;n<l&&(await c.put("https://dashboard.blooket.com/api/users/unlockblook",{name:e,box:o}).then(({data:{unlockedBlook:e,tokens:t,isNewBlook:a}})=>{r[e]||=0,r[e]++;var o=Date.now();i&&alert(`${e} (${n+1}/${l}) ${a?"NEW! ":""}${t} tokens left`),s+=Date.now()-o}).catch(e=>t=!0),!t);n++);alert(`(${Date.now()-s}ms) Results:\n`+Object.entries(r).map(([e,t])=>`    ${e} `+t).join(`\n`))}}).catch(()=>alert("There was an error user data!"))}},{name:"Flood Game",description:"Floods a game with a number of fake accounts",inputs:[{name:"Game ID",type:"string"},{name:"Name",type:"string"},{name:"Amount",type:"number"},{name:"Blook",type:"options",options:async()=>{var e=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"];return Object.keys(Object.values(e.c).find(e=>e.exports.a?.Chick&&e.exports.a?.Elephant).exports.a)}},{name:"Banner",type:"options",options:Object.entries({Starter:"starter",Chalkboard:"chalkboard",Slime:"slime",Bookshelf:"bookshelf","Toaster Pastry":"toasterPastry",Theater:"theater",Sushi:"sushi",Workbench:"workbench",Spooky:"spooky",Spiders:"spiders",Coffin:"coffin",Pumpkins:"pumpkins","Falling Blocks":"fallingBlocks",Racetrack:"racetrack",Harvest:"harvest",Leaves:"leaves","Fall Picnic":"fallPicnic","Winter Drive":"winterDrive","Winter Train":"winterTrain",Ice:"ice",Gifts:"gifts","Christmas Tree":"christmasTree","Soccer Field":"soccerField","Winter Landscape":"winterLandscape","Football Field":"footballField","Outer Space":"outerSpace","Hockey Rink":"hockeyRink","Music Class":"musicClass","Ice Cream Sandwich":"iceCreamSandwich","Science Class":"scienceClass","Fish Tank":"fishTank","Art Class":"artClass",Clockwork:"clockwork","Love Letter":"loveLetter",Farm:"farm",Chocolate:"chocolate","Tech Chip":"techChip",Fire:"fire","Orange Ice Pop":"orangeIcePop"}).map(([e,t])=>({name:e,value:t}))}],run:async function(n,i,e,r,s){var t=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"];const l=Object.values(t.c).find(e=>e.exports?.a?.get).exports.a,c=Object.values(t.c).find(e=>e.exports?.a?.initializeApp).exports.a;for(let o=1;o<=e;o++)(async()=>{var{success:e,fbToken:t,fbShardURL:a}=(await l.put("https://fb.blooket.com/c/firebase/join",{id:n,name:""+i+o}))["data"];e&&(e=c.initializeApp({apiKey:"AIzaSyCA-cTOnX19f6LFnDVVsHXya3k6ByP_MnU",authDomain:"blooket-2020.firebaseapp.com",projectId:"blooket-2020",storageBucket:"blooket-2020.appspot.com",messagingSenderId:"741533559105",appId:"1:741533559105:web:b8cbb10e6123f2913519c0",measurementId:"G-S3H5NGN10Z",databaseURL:a},""+i+o),await(a=c.auth(e)).setPersistence(c.auth.Auth.Persistence.NONE).catch(console.error),await a.signInWithCustomToken(t).catch(console.error),await e.database().ref(n+"/c/"+i+o).set({b:r,bg:s}),e.delete())})(),await new Promise(e=>setTimeout(e,100))}},{name:"Get Daily Rewards",description:"Gets max daily tokens and xp",run:function(){var a,e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),location.href.includes("play.blooket.com")?(a=Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a).post("https://play.blooket.com/api/playersessions/solo",{gameMode:"Factory"}).then(({data:{t}})=>{a.get("https://play.blooket.com/api/users/me").then(({data:{name:e}})=>{a.put("https://play.blooket.com/api/users/add-rewards",{t:t,name:e,addedTokens:500,addedXp:300}).then(({data:{dailyReward:e}})=>alert(`Added max tokens and xp, and got ${e} daily wheel tokens!`)).catch(()=>alert("There was an error when adding rewards."))}).catch(()=>alert("There was an error user data."))}):(alert("This cheat only works on play.blooket.com, opening a new tab."),window.open("https://play.blooket.com/"))}},{name:"Use Any Blook",description:"Allows you to play as any blook",run:function(){const a=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];var e=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]]).webpack("MDrD").a;"/blooks"==location.pathname?a.setState({blookData:Object.keys(e).reduce((e,t)=>(e[t]=a.state.blookData[t]||1,e),{}),allSets:Object.values(e).reduce((e,t)=>e.includes(t.set)?e:e.concat(t.set),[])}):Array.isArray(a.state.unlocks)?a.setState({unlocks:Object.keys(e)}):a.setState({unlocks:e})}},{name:"Every Answer Correct",description:"Sets every answer to be correct",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.freeQuestions=e.questions=e.props.client.questions.map(e=>({...e,correctAnswers:e.answers}))}},{name:"Highlight Answers",description:"Colors answers to be red or green highlighting the correct ones",run:function(){const{state:a,props:o}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];[...document.querySelectorAll('[class*="answerContainer"]')].forEach((e,t)=>{(a.question||o.client.question).correctAnswers.includes((a.question||o.client.question).answers[t])?e.style.backgroundColor="rgb(0, 207, 119)":e.style.backgroundColor="rgb(189, 15, 38)"})}},{name:"Remove Name Limit",description:"Sets the name limit to 120, which is the actual max name length limit",run:function(){var e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),document.querySelector('input[class*="nameInput"]').maxLength=120,alert("Removed name length limit")}},{name:"Remove Random Name",description:"Allows you to put a custom name",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({isRandom:!1,client:{name:""}}),document.querySelector('[class*="nameInput"]')?.focus?.()}},{name:"Sell Cheap Duplicates",description:"Sells all of your uncommon to epic dupes (not legendaries+)",run:function(){var e=document.createElement("iframe"),i=(document.body.append(e),window.alert=e.contentWindow.alert.bind(window),window.confirm=e.contentWindow.confirm.bind(window),e.remove(),Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a);i.get("https://dashboard.blooket.com/api/users").then(async({data:{name:e,unlocks:t}})=>{t=Object.entries(t).filter(([e,t])=>1<t&&!["Legendary","Chroma","Mystical"].includes(webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]]).webpack("MDrD").a[e].rarity));if(confirm("Are you sure you want to sell your uncommon to epic dupes?")){var a,o,n=Date.now();for([a,o]of t)await i.put("https://dashboard.blooket.com/api/users/sellblook",{name:e,blook:a,numSold:o-1});alert(`(${Date.now()-n}ms) Results:\n`+t.map(([e,t])=>`    ${e} `+(t-1)).join(`\n`))}}).catch(()=>alert("There was an error user data!"))}},{name:"Sell Duplicate Blooks",description:"Sell all duplicate blooks leaving you with 1 each",run:function(){var e=document.createElement("iframe"),i=(document.body.append(e),window.alert=e.contentWindow.alert.bind(window),window.confirm=e.contentWindow.confirm.bind(window),e.remove(),Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a);i.get("https://dashboard.blooket.com/api/users").then(async({data:{name:e,unlocks:t}})=>{t=Object.entries(t).filter(e=>1<e[1]);if(confirm("Are you sure you want to sell your dupes?")){var a,o,n=Date.now();for([a,o]of t)await i.put("https://dashboard.blooket.com/api/users/sellblook",{name:e,blook:a,numSold:o-1});alert(`(${Date.now()-n}ms) Results:\n`+t.map(([e,t])=>`    ${e} `+(t-1)).join(`\n`))}}).catch(()=>alert("There was an error user data!"))}},{name:"Simulate Pack",description:"Simulate opening a pack",inputs:[{name:"Pack",type:"options",options:async()=>Array.from(document.querySelectorAll('[class*="packShadow"]')).map(e=>e.alt)}],run:function(){let m=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"],o=Object.values(m.c).find(e=>e.exports?.Class).exports,h={};class n extends o.Scene{constructor(e){super(),this.rarity=e.toLowerCase()}preload(){switch(this.rarity){case"uncommon":this.load.svg("uncommon-1","https://media.blooket.com/image/upload/v1658567787/Media/market/particles/square_green.svg",{width:25,height:25}),this.load.svg("uncommon-2","https://media.blooket.com/image/upload/v1658567787/Media/market/particles/square_light_green.svg",{width:25,height:25}),this.load.svg("uncommon-3","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/circle_dark_green.svg",{width:25,height:25}),this.load.svg("uncommon-4","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/serpentine_dark_green.svg",{width:30,height:30}),this.load.svg("uncommon-5","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/triangle_light_green.svg",{width:30,height:30}),this.load.svg("uncommon-6","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/serpentine_light_green.svg",{width:30,height:30}),this.load.svg("uncommon-7","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/triangle_green.svg",{width:30,height:30});break;case"rare":this.load.svg("rare-1","https://media.blooket.com/image/upload/v1658567765/Media/market/particles/square_light_blue.svg",{width:25,height:25}),this.load.svg("rare-2","https://media.blooket.com/image/upload/v1658567765/Media/market/particles/square_dark_blue.svg",{width:25,height:25}),this.load.svg("rare-3","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/triangle_blue.svg",{width:30,height:30}),this.load.svg("rare-4","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/serpentine_blue.svg",{width:30,height:30}),this.load.svg("rare-5","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/triangle_light_blue.svg",{width:30,height:30}),this.load.svg("rare-6","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/serpentine_light_blue.svg",{width:30,height:30}),this.load.svg("rare-7","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/circle_dark_blue.svg",{width:25,height:25});break;case"epic":this.load.svg("epic-1","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/red.svg",{width:25,height:25}),this.load.svg("epic-2","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/light_red.svg",{width:25,height:25}),this.load.svg("epic-3","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/serpentine_red.svg",{width:30,height:30}),this.load.svg("epic-4","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/serpentine_dark_red.svg",{width:30,height:30}),this.load.svg("epic-5","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/triangle_red.svg",{width:30,height:30}),this.load.svg("epic-6","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/triangle_light_red.svg",{width:30,height:30}),this.load.svg("epic-7","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/circle_dark_red.svg",{width:25,height:25});break;case"legendary":this.load.svg("legendary-1","https://media.blooket.com/image/upload/v1658567740/Media/market/particles/square_orange.svg",{width:25,height:25}),this.load.svg("legendary-2","https://media.blooket.com/image/upload/v1658567740/Media/market/particles/square_light_orange.svg",{width:25,height:25}),this.load.svg("legendary-3","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/circle_orange.svg",{width:25,height:25}),this.load.svg("legendary-4","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/serpentine_orange.svg",{width:30,height:30}),this.load.svg("legendary-5","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/serpentine_light_orange.svg",{width:30,height:30}),this.load.svg("legendary-6","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/circle_dark_orange.svg",{width:25,height:25}),this.load.svg("legendary-7","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/triangle_dark_orange.svg",{width:30,height:30});break;case"chroma":this.load.svg("chroma-1","https://media.blooket.com/image/upload/v1658790246/Media/market/particles/square_turquoise.svg",{width:25,height:25}),this.load.svg("chroma-2","https://media.blooket.com/image/upload/v1658790246/Media/market/particles/square_light_turquoise.svg",{width:25,height:25}),this.load.svg("chroma-3","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/serpentine_dark_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-4","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/serpentine_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-5","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/triangle_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-6","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/triangle_light_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-7","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/circle_dark_turquoise.svg",{width:25,height:25})}}create(){h.scene=this,h.rarity="",h.particles=this.physics.add.group({classType:new o.Class({Extends:o.GameObjects.Image,initialize:function(){o.GameObjects.Image.call(this,h.scene,0,0,"uncommon-1"),this.setDepth(3),this.lifespan=0},spawn:function(e,t,a,o,n,i,r,s,l){this.setTexture(l),this.setActive(!0),this.setVisible(!0),this.setPosition(e,t),this.setScale(a),this.targets=[],h.scene.physics.velocityFromAngle(o,n,this.body.velocity),this.body.setGravityY(i),this.body.setAngularVelocity(r),this.lifespan=s},update:function(e,t){this.lifespan-=t,0<this.lifespan||(this.setActive(!1),this.setVisible(!1))}}),runChildUpdate:!0}),this.nextParticle=0,this.numExplosions=0,this.game.events.on("start-particles",e=>{h.rarity=e,this.numExplosions="Uncommon"===e?75:"Rare"===e?100:-1})}update(e,t){const a=m("74sb");function o(e){switch(e){case"center":var t=Object(a.l)(-115,-65);return{x:h.scene.cameras.main.worldView.width/2,y:h.scene.cameras.main.worldView.height/2,scale:Object(a.l)(.7,1),angle:t,velocity:Object(a.l)(600,750),gravity:700,angVelocity:(-90<t?1:-1)*Object(a.l)(125,175),lifespan:2500};case"right-bottom":return{x:h.scene.cameras.main.worldView.width,y:h.scene.cameras.main.worldView.height,scale:Object(a.l)(.7,1),angle:Object(a.l)(-160,-110),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-bottom":return{x:0,y:h.scene.cameras.main.worldView.height,scale:Object(a.l)(.7,1),angle:Object(a.l)(-70,-20),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(125,175),lifespan:2500};case"top":return{x:Object(a.l)(0,h.scene.cameras.main.worldView.width),y:-50,scale:Object(a.l)(.7,1),angle:90,velocity:Object(a.l)(0,50),gravity:700,angVelocity:Object(a.l)(-150,150),lifespan:2500};case"right-shower":return{x:h.scene.cameras.main.worldView.width,y:Object(a.l)(0,h.scene.cameras.main.worldView.height),scale:Object(a.l)(.7,1),angle:Object(a.l)(-180,-130),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-shower":return{x:0,y:Object(a.l)(0,h.scene.cameras.main.worldView.height),scale:Object(a.l)(.7,1),angle:Object(a.l)(-50,0),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(125,175),lifespan:2500};case"right-diamond":t=Object(a.l)(0,h.scene.cameras.main.worldView.height);return{x:h.scene.cameras.main.worldView.width,y:t,scale:Object(a.l)(.7,1),angle:t>h.scene.cameras.main.worldView.height/2?-150:-210,velocity:Object(a.l)(600,750),gravity:0,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-diamond":t=Object(a.l)(0,h.scene.cameras.main.worldView.height);return{x:0,y:t,scale:Object(a.l)(.7,1),angle:t>h.scene.cameras.main.worldView.height/2?-30:30,velocity:Object(a.l)(600,750),gravity:0,angVelocity:Object(a.l)(125,175),lifespan:2500};default:return{}}}if(h.rarity&&0!==this.numExplosions&&(this.nextParticle-=t,this.nextParticle<=0)){switch(h.rarity){case"Uncommon":for(let e=0;e<2;e++){var n=h.particles.get();n&&n.spawn.apply(n,Object.values(o("center")).concat("uncommon-"+Object(a.m)(1,8)))}break;case"Rare":for(var i=0;i<2;i++){var r=h.particles.get();r&&r.spawn.apply(r,Object.values(o(i%2==0?"left-bottom":"right-bottom")).concat("rare-"+Object(a.m)(1,8)))}break;case"Epic":for(var s=0;s<2;s++){var l=h.particles.get();l&&l.spawn.apply(l,Object.values(o(s%2==0?"left-shower":"right-shower")).concat("epic-"+Object(a.m)(1,8)))}break;case"Legendary":for(var c=0;c<3;c++){var d=h.particles.get();d&&d.spawn.apply(d,Object.values(o("top")).concat("legendary-"+Object(a.m)(1,8)))}break;case"Chroma":for(var p=0;p<3;p++){var u=h.particles.get();u&&u.spawn.apply(u,Object.values(o(p%2==0?"left-diamond":"right-diamond")).concat("chroma-"+Object(a.m)(1,8)))}}this.nextParticle=20,0<this.numExplosions&&(this.numExplosions=Math.max(this.numExplosions-1,0))}}}return function(e){if("/market"!==window.location.pathname)return alert("This must be ran on the market page");var t,a=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];let i=m("fGzD");(i=Object.keys(i.a).reduce((e,t)=>(e.packs.includes(t)&&(e.data[t]=Object.fromEntries(i.b(t))),e),{packs:Array.from(document.querySelectorAll('[class*="packShadow"]')).map(e=>e.alt),data:{}}).data)[e]?(e=function(e){var t=[],a=Object.keys(i[e]);for(const n of a)t.push(i[e][n]+(t[a.indexOf(n)-1]||0));const o=t[t.length-1]*Math.random();return a[t.findIndex(e=>e>=o)]}(e),t=Object.values(m.c).find(e=>e.exports?.a?.Elephant).exports.a,a.setState({loadingPack:!1,openPack:!0,unlockedBlook:e,tokens:a.state.tokens,newUnlock:!0,game:{type:o.WEBGL,parent:"phaser-market",width:"100%",height:"100%",scale:{mode:o.Scale.NONE,autoCenter:o.Scale.CENTER_BOTH},transparent:!0,physics:{default:"arcade"},scene:new n(t[e].rarity)},canOpen:!0})):alert("I couldn't find that box!")}}()},{name:"Simulate Unlock",description:"Simulate unlocking most of the blooks",inputs:[{name:"Blook",type:"options",options:async()=>{let a=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"];return Object.keys(Object.entries(Object.values(a.c).find(e=>Object.values(e.exports?.a||{})[0]?.set).exports.a).reduce((e,t)=>(Object.values(a.c).find(e=>15==e.exports.a?.Breakfast).exports.a[t[1].realSet||t[1].set]&&(e[t[0]]=t[1]),e),{}))}}],run:function(){let m=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"],a=Object.values(m.c).find(e=>e.exports?.Class).exports,h={};class o extends a.Scene{constructor(e){super(),this.rarity=e.toLowerCase()}preload(){switch(this.rarity){case"uncommon":this.load.svg("uncommon-1","https://media.blooket.com/image/upload/v1658567787/Media/market/particles/square_green.svg",{width:25,height:25}),this.load.svg("uncommon-2","https://media.blooket.com/image/upload/v1658567787/Media/market/particles/square_light_green.svg",{width:25,height:25}),this.load.svg("uncommon-3","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/circle_dark_green.svg",{width:25,height:25}),this.load.svg("uncommon-4","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/serpentine_dark_green.svg",{width:30,height:30}),this.load.svg("uncommon-5","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/triangle_light_green.svg",{width:30,height:30}),this.load.svg("uncommon-6","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/serpentine_light_green.svg",{width:30,height:30}),this.load.svg("uncommon-7","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/triangle_green.svg",{width:30,height:30});break;case"rare":this.load.svg("rare-1","https://media.blooket.com/image/upload/v1658567765/Media/market/particles/square_light_blue.svg",{width:25,height:25}),this.load.svg("rare-2","https://media.blooket.com/image/upload/v1658567765/Media/market/particles/square_dark_blue.svg",{width:25,height:25}),this.load.svg("rare-3","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/triangle_blue.svg",{width:30,height:30}),this.load.svg("rare-4","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/serpentine_blue.svg",{width:30,height:30}),this.load.svg("rare-5","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/triangle_light_blue.svg",{width:30,height:30}),this.load.svg("rare-6","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/serpentine_light_blue.svg",{width:30,height:30}),this.load.svg("rare-7","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/circle_dark_blue.svg",{width:25,height:25});break;case"epic":this.load.svg("epic-1","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/red.svg",{width:25,height:25}),this.load.svg("epic-2","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/light_red.svg",{width:25,height:25}),this.load.svg("epic-3","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/serpentine_red.svg",{width:30,height:30}),this.load.svg("epic-4","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/serpentine_dark_red.svg",{width:30,height:30}),this.load.svg("epic-5","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/triangle_red.svg",{width:30,height:30}),this.load.svg("epic-6","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/triangle_light_red.svg",{width:30,height:30}),this.load.svg("epic-7","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/circle_dark_red.svg",{width:25,height:25});break;case"legendary":this.load.svg("legendary-1","https://media.blooket.com/image/upload/v1658567740/Media/market/particles/square_orange.svg",{width:25,height:25}),this.load.svg("legendary-2","https://media.blooket.com/image/upload/v1658567740/Media/market/particles/square_light_orange.svg",{width:25,height:25}),this.load.svg("legendary-3","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/circle_orange.svg",{width:25,height:25}),this.load.svg("legendary-4","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/serpentine_orange.svg",{width:30,height:30}),this.load.svg("legendary-5","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/serpentine_light_orange.svg",{width:30,height:30}),this.load.svg("legendary-6","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/circle_dark_orange.svg",{width:25,height:25}),this.load.svg("legendary-7","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/triangle_dark_orange.svg",{width:30,height:30});break;case"chroma":this.load.svg("chroma-1","https://media.blooket.com/image/upload/v1658790246/Media/market/particles/square_turquoise.svg",{width:25,height:25}),this.load.svg("chroma-2","https://media.blooket.com/image/upload/v1658790246/Media/market/particles/square_light_turquoise.svg",{width:25,height:25}),this.load.svg("chroma-3","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/serpentine_dark_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-4","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/serpentine_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-5","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/triangle_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-6","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/triangle_light_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-7","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/circle_dark_turquoise.svg",{width:25,height:25})}}create(){h.scene=this,h.rarity="",h.particles=this.physics.add.group({classType:new a.Class({Extends:a.GameObjects.Image,initialize:function(){a.GameObjects.Image.call(this,h.scene,0,0,"uncommon-1"),this.setDepth(3),this.lifespan=0},spawn:function(e,t,a,o,n,i,r,s,l){this.setTexture(l),this.setActive(!0),this.setVisible(!0),this.setPosition(e,t),this.setScale(a),this.targets=[],h.scene.physics.velocityFromAngle(o,n,this.body.velocity),this.body.setGravityY(i),this.body.setAngularVelocity(r),this.lifespan=s},update:function(e,t){this.lifespan-=t,0<this.lifespan||(this.setActive(!1),this.setVisible(!1))}}),runChildUpdate:!0}),this.nextParticle=0,this.numExplosions=0,this.game.events.on("start-particles",e=>{h.rarity=e,this.numExplosions="Uncommon"===e?75:"Rare"===e?100:-1})}update(e,t){const a=m("74sb");function o(e){switch(e){case"center":var t=Object(a.l)(-115,-65);return{x:h.scene.cameras.main.worldView.width/2,y:h.scene.cameras.main.worldView.height/2,scale:Object(a.l)(.7,1),angle:t,velocity:Object(a.l)(600,750),gravity:700,angVelocity:(-90<t?1:-1)*Object(a.l)(125,175),lifespan:2500};case"right-bottom":return{x:h.scene.cameras.main.worldView.width,y:h.scene.cameras.main.worldView.height,scale:Object(a.l)(.7,1),angle:Object(a.l)(-160,-110),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-bottom":return{x:0,y:h.scene.cameras.main.worldView.height,scale:Object(a.l)(.7,1),angle:Object(a.l)(-70,-20),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(125,175),lifespan:2500};case"top":return{x:Object(a.l)(0,h.scene.cameras.main.worldView.width),y:-50,scale:Object(a.l)(.7,1),angle:90,velocity:Object(a.l)(0,50),gravity:700,angVelocity:Object(a.l)(-150,150),lifespan:2500};case"right-shower":return{x:h.scene.cameras.main.worldView.width,y:Object(a.l)(0,h.scene.cameras.main.worldView.height),scale:Object(a.l)(.7,1),angle:Object(a.l)(-180,-130),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-shower":return{x:0,y:Object(a.l)(0,h.scene.cameras.main.worldView.height),scale:Object(a.l)(.7,1),angle:Object(a.l)(-50,0),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(125,175),lifespan:2500};case"right-diamond":t=Object(a.l)(0,h.scene.cameras.main.worldView.height);return{x:h.scene.cameras.main.worldView.width,y:t,scale:Object(a.l)(.7,1),angle:t>h.scene.cameras.main.worldView.height/2?-150:-210,velocity:Object(a.l)(600,750),gravity:0,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-diamond":t=Object(a.l)(0,h.scene.cameras.main.worldView.height);return{x:0,y:t,scale:Object(a.l)(.7,1),angle:t>h.scene.cameras.main.worldView.height/2?-30:30,velocity:Object(a.l)(600,750),gravity:0,angVelocity:Object(a.l)(125,175),lifespan:2500};default:return{}}}if(h.rarity&&0!==this.numExplosions&&(this.nextParticle-=t,this.nextParticle<=0)){switch(h.rarity){case"Uncommon":for(let e=0;e<2;e++){var n=h.particles.get();n&&n.spawn.apply(n,Object.values(o("center")).concat("uncommon-"+Object(a.m)(1,8)))}break;case"Rare":for(var i=0;i<2;i++){var r=h.particles.get();r&&r.spawn.apply(r,Object.values(o(i%2==0?"left-bottom":"right-bottom")).concat("rare-"+Object(a.m)(1,8)))}break;case"Epic":for(var s=0;s<2;s++){var l=h.particles.get();l&&l.spawn.apply(l,Object.values(o(s%2==0?"left-shower":"right-shower")).concat("epic-"+Object(a.m)(1,8)))}break;case"Legendary":for(var c=0;c<3;c++){var d=h.particles.get();d&&d.spawn.apply(d,Object.values(o("top")).concat("legendary-"+Object(a.m)(1,8)))}break;case"Chroma":for(var p=0;p<3;p++){var u=h.particles.get();u&&u.spawn.apply(u,Object.values(o(p%2==0?"left-diamond":"right-diamond")).concat("chroma-"+Object(a.m)(1,8)))}}this.nextParticle=20,0<this.numExplosions&&(this.numExplosions=Math.max(this.numExplosions-1,0))}}}return function(e){var t=document.createElement("iframe");document.body.append(t),window.alert=t.contentWindow.alert.bind(window),window.prompt=t.contentWindow.prompt.bind(window),t.remove(),"/market"==window.location.pathname?(t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],t.setState({loadingPack:!1,openPack:!0,unlockedBlook:e,tokens:t.state.tokens,newUnlock:!0,game:{type:a.WEBGL,parent:"phaser-market",width:"100%",height:"100%",scale:{mode:a.Scale.NONE,autoCenter:a.Scale.CENTER_BOTH},transparent:!0,physics:{default:"arcade"},scene:new o(Object.entries(Object.values(m.c).find(e=>Object.values(e.exports?.a||{})[0]?.set).exports.a).reduce((e,t)=>(Object.values(m.c).find(e=>15==e.exports.a?.Breakfast).exports.a[t[1].set]&&(e[t[0]]=t[1]),e),{})[e].rarity)},canOpen:!0})):alert("This can only be ran on the market page!")}}()},{name:"Unlock Plus Gamemodes",description:"Allows you to play any gamemode that is plus only",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState(e=>(e.gameModes.forEach(e=>e.plusOnly=!1),e))}}],brawl:[{name:"Double Enemy XP",description:"Doubles enemy XP drop value",run:function(){for(const a of Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.filter(e=>e.callbackContext?.toString().includes("invulnerableTime"))){var t=a.object2;let e=t.classType.prototype.start;t.classType.prototype.start=function(){e.apply(this,arguments),this.val*=2},t.children.entries.forEach(e=>e.val*=2)}}},{name:"Half Enemy Speed",description:"Makes enemies move 2x slower",run:function(){for(const a of Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.filter(e=>e.callbackContext?.toString().includes("invulnerableTime"))){var t=a.object2;let e=t.classType.prototype.start;t.classType.prototype.start=function(){e.apply(this,arguments),this.speed*=.5},t.children.entries.forEach(e=>e.speed*=.5)}}},{name:"Instant Kill",description:"Sets all enemies health to 1",run:function(){for(const a of Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.filter(e=>e.callbackContext?.toString().includes("invulnerableTime"))){var t=a.object2;let e=t.classType.prototype.start;t.classType.prototype.start=function(){e.apply(this,arguments),this.hp=1},t.children.entries.forEach(e=>e.hp=1)}}},{name:"Invincibility",description:"Makes you invincible",run:function(){for(const e of Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.filter(e=>e.callbackContext?.toString().includes("invulnerableTime")))e.collideCallback=()=>{}}},{name:"Magnet",description:"Pulls all xp towards you",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.find(e=>e.collideCallback?.toString().includes("magnetTime")).collideCallback({active:!0},{active:!0,setActive(){},setVisible(){}})}},{name:"Max Current Abilities",description:"Maxes out all your current abilities",run:function(){const a=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];for(var[t,o]of Object.entries(a.state.abilities))for(let e=0;e<10-o;e++)a.state.game.scene.game.events.emit("level up",t,a.state.abilities[t]++);a.setState({level:a.state.game.scene.level=[1,3,5,10,15,25,35].sort((e,t)=>Math.abs(e-a.state.level)-Math.abs(t-a.state.level))[0]-1})}},{name:"Next Level",description:"Skips to the next level",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],{object1:t,object2:a}=e.state.game.scene.physics.world.colliders._active.find(e=>e.collideCallback?.toString().includes('emit("xp"'));a.get().spawn(t.x,t.y,(1===(a=e.state.level)?1:a<5?5:a<10?10:a<20?20:a<30?30:a<40?40:a<50?50:100)-e.xp)}},{name:"Remove Obstacles",description:"Removes all rocks and obstacles",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.bodies.entries.forEach(e=>{try{e.gameObject.frame.texture.key.includes("obstacle")&&e.gameObject.destroy()}catch{}})}},{name:"Kill Enemies",description:"Kills all current enemies",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.bodies.entries.forEach(e=>e?.gameObject?.receiveDamage?.(e.gameObject.hp,1))}},{name:"Reset Health",description:"Resets health and gives invincibility for 3 seconds",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.game.events._events.respawn.fn()}}],cafe:[{name:"Max Items",description:"Maxes out items in the shop (Only usable in the shop)",run:function(){var e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),"/cafe/shop"!==window.location.pathname?alert("This can only be run in the shop"):(e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],e.setState({items:Object.fromEntries(Object.entries(e.state.items).map(e=>[e[0],5]))}))}},{name:"Remove Customers",description:"Skips the current customers (Not usable in the shop)",run:function(){const a=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];a.state.customers.forEach((e,t)=>Object.keys(e).length&&a.removeCustomer(t,!0))}},{name:"Reset Abilities",description:"Resets used abilities in shop (Only usable in the shop)",run:function(){var e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),"/cafe/shop"!==window.location.pathname?alert("This can only be run in the shop"):(e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],e.setState({abilities:Object.fromEntries(Object.entries(e.state.abilities).map(e=>[e[0],5]))}))}},{name:"Set Cash",description:"Sets cafe cash",inputs:[{name:"Amount",type:"number"}],run:function(e){var t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];t.setState({cafeCash:e}),t.props.liveGameController.setVal({path:"c/"+t.props.client.name,val:{b:t.props.client.blook,ca:e}})}},{name:"Stock Food",description:"Stocks all food to 99 (Not usable in the shop)",run:function(){var e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),"/cafe"!==window.location.pathname?alert("This can't be run in the shop"):(e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],e.setState({foods:e.state.foods.map(e=>({...e,stock:99,level:5}))}))}}],crypto:[{name:"Choice ESP",description:"Shows what each choice will give you",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{var e,t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],t=t.state.choices[0]["text"],a=document.querySelector("[class^=styles__feedbackContainer___]");a.children.length<=4&&((e=document.createElement("div")).style.color="white",e.style.fontFamily="Inconsolata,Helvetica,monospace,sans-serif",e.style.fontSize="2em",e.style.display="flex",e.style.justifyContent="center",e.style.marginTop="675px",e.innerText=t,a.append(e))},50))}},{name:"Password ESP",description:"Highlights the correct password",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{let t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode["state"];"hack"==t.stage&&[...document.querySelector("div[class^=styles__buttonContainer]").children].forEach(e=>{e.innerText!=t.correctPassword&&(e.style.outlineColor="rgba(255, 64, 64, 0.8)",e.style.backgroundColor="rgba(255, 64, 64, 0.8)",e.style.textShadow="0 0 1px #f33")})},50))}},{name:"Always Triple",description:"Always get triple crypto",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({choices:[{type:"mult",val:3,rate:.075,blook:"Brainy Bot",text:"Triple Crypto"}]}),50))}},{name:"Auto Guess",description:"Automatically guess the correct password",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode["state"];if("hack"==e.stage)for(const t of document.querySelector("div[class^=styles__buttonContainer]").children)t.innerText==e.correctPassword&&t.click()},50))}},{name:"Remove Hack",description:"",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({hack:""})}},{name:"Set Crypto",description:"Sets crypto",inputs:[{name:"Amount",type:"number"}],run:function(e){var t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];t.setState({crypto:e,crypto2:e}),t.props.liveGameController.setVal({path:"c/".concat(t.props.client.name),val:{b:t.props.client.blook,p:t.state.password,cr:e}})}},{name:"Set Password",description:"Sets hacking password",inputs:[{name:"Custom Password",type:"string"}],run:function(e){var t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];t.setState({password:e}),t.props.liveGameController.setVal({path:"c/".concat(t.props.client.name),val:{b:t.props.client.blook,p:e,cr:t.state.crypto}})}},{name:"Steal Player's Crypto",description:"Steals all of someone's crypto",inputs:[{name:"Player",type:"options",options:()=>{let e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];return new Promise(t=>e.props.liveGameController._liveApp?e.props.liveGameController.getDatabaseVal("c",e=>e&&t(Object.keys(e))):t([]))}}],run:function(a){let o=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];o.props.liveGameController.getDatabaseVal("c",e=>{var t;e&&Object.keys(e).map(e=>e.toLowerCase()).includes(a.toLowerCase())&&([e,{cr:t}]=Object.entries(e).find(([e])=>e.toLowerCase()==a.toLowerCase()),o.setState({crypto:o.state.crypto+t,crypto2:o.state.crypto+t}),o.props.liveGameController.setVal({path:"c/".concat(o.props.client.name),val:{b:o.props.client.blook,p:o.state.password,cr:o.state.crypto+t,tat:e+":"+t}}))})}}],defense:[{name:"Earthquake",description:"Shuffles around towers",run:function(){let o=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],n=(o.setState({eventName:"Earthquake",event:{short:"e",color:"#805500",icon:"fas fa-mountain",desc:"All of your towers get mixed up",rate:.02},buyTowerName:"",buyTower:{}},()=>o.eventTimeout=setTimeout(()=>o.setState({event:{},eventName:""}),6e3)),o.tiles.forEach(a=>a.forEach((e,t)=>3===e&&(a[t]=0))),o.tiles.flatMap((e,a)=>e.map((e,t)=>0===e&&{x:t,y:a})).filter(Boolean).sort(()=>.5-Math.random()));o.towers.forEach(e=>{var{x:t,y:a}=n.shift();e.move(t,a,o.tileSize),o.tiles[a][t]=3})}},{name:"Max Tower Stats",description:"Makes all placed towers overpowered",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.towers.forEach(e=>{e.range=100,e.fullCd=e.cd=0,e.damage=1e6})}},{name:"Remove Ducks",description:"Removes ducks",run:function(){let{ducks:e,tiles:t}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.forEach(e=>{t[e.y][e.x]=0}),e.length=0}},{name:"Remove Enemies",description:"Removes all the enemies",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.enemies=e.futureEnemies=[]}},{name:"Remove Obstacles",description:"Lets you place towers anywhere",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.tiles=e.tiles.map(e=>e.fill(0))}},{name:"Set Damage",description:"Sets damage",inputs:[{name:"Damage",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.dmg=e}},{name:"Set Round",description:"Sets the current round",inputs:[{name:"Round",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({round:e})}},{name:"Set Tokens",description:"Sets the amount of tokens you have",inputs:[{name:"Tokens",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({tokens:e})}}],defense2:[{name:"Max Tower Stats",description:"Makes all placed towers overpowered",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.towers.forEach(e=>{if(e.stats.dmg=1e6,e.stats.fireRate=50,e.stats.ghostDetect=!0,e.stats.maxTargets=1e6,e.stats.numProjectiles&&=100,e.stats.range=100,e.stats.auraBuffs)for(const t in e.stats.auraBuffs)e.stats.auraBuffs[t]*=100})}},{name:"Kill Enemies",description:"Kills all the enemies",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.state.game.scene.enemyQueue.length=0,e.state.game.scene.physics.world.bodies.entries.forEach(e=>e?.gameObject?.receiveDamage?.(e.gameObject.hp,1))}},{name:"Set Coins",description:"Sets coins",inputs:[{name:"Coins",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({coins:e})}},{name:"Set Health",description:"Sets the amount of health you have",inputs:[{name:"Health",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({health:e})}},{name:"Set Round",description:"Sets the current round",inputs:[{name:"Round",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({round:e})}}],dinos:[{name:"Auto Choose",description:"Automatically choose the best fossil when excavating",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{const t=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"];var e=(()=>{const e=Object.values(t("74sb")).find(e=>e.toString().includes("rate"));return()=>e([{type:"fossil",val:10,rate:.1,blook:"Amber"},{type:"fossil",val:25,rate:.1,blook:"Dino Egg"},{type:"fossil",val:50,rate:.175,blook:"Dino Fossil"},{type:"fossil",val:75,rate:.175,blook:"Stegosaurus"},{type:"fossil",val:100,rate:.15,blook:"Velociraptor"},{type:"fossil",val:125,rate:.125,blook:"Brontosaurus"},{type:"fossil",val:250,rate:.075,blook:"Triceratops"},{type:"fossil",val:500,rate:.025,blook:"Tyrannosaurus Rex"},{type:"mult",val:1.5,rate:.05},{type:"mult",val:2,rate:.025}],3)})();try{var o=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];if("excavate"===o.state.stage){o.state.choices.length||(o.state.choices=e());let t=0,a=-1;for(let e=0;e<o.state.choices.length;e++){var{type:n,val:i}=o.state.choices[e],r=("fossil"==n?o.state.fossils+i*o.state.fossilMult:o.state.fossils*i)||0;r<=t&&"mult"!=n||(t=r,a=e+1)}document.querySelector('div[class^="styles__rockRow"] > div[role="button"]:nth-child('+a+")").click()}}catch{}},50))}},{name:"Rock ESP",description:"Shows what is under the rocks",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{let o=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];const e=[...document.querySelector('[class*="rockButton"]').parentElement.children];e.every(e=>e.querySelector("div"))||o.setState({choices:[{type:"fossil",val:10,rate:.1,blook:"Amber"},{type:"fossil",val:25,rate:.1,blook:"Dino Egg"},{type:"fossil",val:50,rate:.175,blook:"Dino Fossil"},{type:"fossil",val:75,rate:.175,blook:"S…

---
## [CivMC/CivDocker](https://github.com/CivMC/CivDocker)@[7fdbe7c6d9...](https://github.com/CivMC/CivDocker/commit/7fdbe7c6d9d1e9ca8b73aec517daf0300588acdd)
#### Thursday 2023-03-23 22:07:01 by CaptainKlutz

Lengthen all reinforcement maturation times

Reinforcement times across the board are far too short.

It is completely nonsensical that structures built can rival the strength of buildings that have stood for months after just 5 minutes or an hour. It sucks the fun out of civ knowing you have mere seconds to log in and remove stone-reinforced grief before having to use acid blocks instead. It is completely counterproductive for those with lives outside of civ to always be an hour away from being totally invalidated. The stale vault meta is only bolstered by the fact that vault spikes are risk-free and diamond reinforced expansions can be erected overnight.

A lot of people are scared of big maturation numbers but forget they don't represent 'time until viable'. Just a few seconds after SRO is placed, it doubles in strength. The time it takes to mine it then allows it to mature further. Pardon my French, but it is absolutely FUCKED that you can be mining a block and the amount of breaks it will take to destroy it is INCREASING while you're ACTIVELY BREAKING IT.

"but my skybridging": what do you want to be more important, the skybridge or the people fighting in it?

"but my build might be broken overnight": just 15 minutes after you place a stone reinforced block, it will already take 16 hits to break. unless you're building in a warzone, you're going to be fine.

"but my acids will take longer": maybe now it will be actually viable to break blocks still maturing instead of giving up and going straight for acid.

"but my bunker pvp": I've seen bunker pvp on this iteration and it's fair to say I think the vast majority of people hate the stone reinforced obby/trapdoors/doors/buttons spam meta.

"but it will encourage camping to abuse when reinforcements are maturing": but this ALREADY HAPPENS, just the other way around. Players literally wait for people to be offline to spam reinforcements before they log on again. Turning this around to favour the breaker's side is more healthy.

"but now obbybombing is less viable": good.

---
## [IndaPlus22/alww-palinda-2](https://github.com/IndaPlus22/alww-palinda-2)@[945f43e748...](https://github.com/IndaPlus22/alww-palinda-2/commit/945f43e74823aec240a213bf8b92ea3cbb57c32a)
#### Thursday 2023-03-23 22:15:26 by TrollKaaar

My dear friend, you are right that even the gods themselves require rest and repose from time to time. And so it is with us mortals, who are not machines but rather creatures of flesh and blood.

But let us not mistake leisure for idleness, or rest for sloth. For true rest and leisure are essential for the cultivation of the mind and the spirit, and for the pursuit of wisdom and virtue.

So let us take the time we need to refresh ourselves, to gather our strength and our thoughts, and to renew our commitment to the pursuit of truth and goodness. For it is only through such rest and renewal that we can hope to achieve the highest ideals of human existence.

---
## [Offroaders123/Num-Text-Component](https://github.com/Offroaders123/Num-Text-Component)@[d5aefc54f3...](https://github.com/Offroaders123/Num-Text-Component/commit/d5aefc54f3a6023c0ea36d91780d046b1e9cd16e)
#### Thursday 2023-03-23 22:58:07 by Offroaders123

Futher Docs

I think everything is documented now! I'm really glad I ended up going back and documenting everything, it's actually suprisingly not too crazy of a codebase as I thought, it just needed some love with some formatting, documenting, and type safety :)

Now I think I can reliably use this codebase as a reference for the new one :)

Listening to a ton of albums yet again! This has been really fun. I went on a music detour while coding last night, learned a ton. Just heard about Shawn Lane, wow! Interesting to find that he's an influence to both Guthrie Govan *and* Michael Romeo, both of whom are my top favorites. I can't wait to look into his catalog next. I'm sadden to hear about his unfortunate passing and struggles throughout life, it's unfortunate he couldn't have as many years to show the world all of his genius. Now that I've heard his sound, I can hear where the crossover between Govan and Romeo is, I love that style!

This performance is outstanding, this is the first I've listened to from Shawn Lane so far, and I can't wait to listen to more.
https://www.youtube.com/watch?v=XJ_6J-Tb5nM

Of the albums today, so far I've listened to 'Grace for Drowning' (SW), 'V: The New Mythology Suite' (SX), and now I'm listening to 'Comfortably Homeless' (MM). While starting this commit, the song 'The plane' was on, and I ended up looking into the 'Time to go to the bank, MY LITTLE CASH CRABS.' audio section, and I finally found it! Looks like it's from 'Cow and Chicken' on Cartoon Network, and the episode is 'Free Inside' the best I could find.

There was a really old WordPress page someone made years ago that looks like they made the transcriptions for the episodes themselves, and this is where it had those audio clip words from. Now I want to see if I can find the episode for that after this. Thanks for this crazy song, Marco! XD
https://cowandchickenscripts.wordpress.com/

---
## [assortedbeads/CEV-Eris](https://github.com/assortedbeads/CEV-Eris)@[6f75cb9845...](https://github.com/assortedbeads/CEV-Eris/commit/6f75cb984594e66d49dff852532ac69a387899d7)
#### Thursday 2023-03-23 23:04:03 by !Moltov!

Hotkey tweaks (#7956)

* yeah

* changes the hotkey list

* I forgot to push this

* Revert "I forgot to push this"

This reverts commit 845878d1bda9f8be1cee214acd7329b0355a507b.

* Revert "changes the hotkey list"

This reverts commit a1174c47bdc49245e4b31ddb06f85e7fec21e51c.

* re-adds reversions

* Revert "yeah"

This reverts commit e61f425a1231c6049c123724bfe88a7e51b9c199.

* manually adds hotkeys instead of using .dmf

I love the quirky dream maker language

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[700606378e...](https://github.com/Buildstarted/linksfordevs/commit/700606378e2d7e5a6a6ce4d4a1a8eb58dc595ceb)
#### Thursday 2023-03-23 23:08:36 by Ben Dornis

Updating: 3/23/2023 11:00:00 PM

 1. Added: On Slowness
    (https://warrenellis.ltd/jot/on-slowness/)
 2. Added: The Great Deprival
    (https://bastian.rieck.me/blog/posts/2023/deprival/)
 3. Added: Why aren’t logical properties taking over everything? - Chris Coyier
    (https://chriscoyier.net/2023/03/13/why-arent-logical-properties-taking-over-everything/)
 4. Added: Fascination of AWK
    (https://maximullaris.com/awk.html)
 5. Added: Synchronous Reading with Friends
    (https://www.rhotter.com/posts/synchronous-reading)
 6. Added: My favourite Obsidian plugins — Niklas's blog
    (https://pivic.blog/blog/my-favourite-obsidian-plugins/)
 7. Added: Najaf Ali's Homepage
    (https://najafali.blog/notes/moulding-software)
 8. Added: Strategy | Ashu Desai
    (https://ashu.xyz/strategy/)
 9. Added: Large Language Models Are Like The Planet Solaris
    (https://blev.dev/articles/solaris-and-llms/)
10. Added: Mark Volkmann's blog
    (https://mvolkmann.github.io/blog/topics/#/blog/terminal-tips/?utm_source=hnblogs.substack.com)
11. Added: Laptop vs Desktop for RonDB development
    (http://mikaelronstrom.blogspot.com/2023/03/laptop-vs-desktop-for-rondb-development.html)
12. Added: Mads Kristensen's Sneak Peek at Visual Studio's AI Future, To 'Rekindle Our Love of Coding' -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2023/03/23/vs-ai.aspx)
13. Added: 50 years of silence
    (https://www.elidourado.com/p/50-years-supersonic-ban)
14. Added: The AsyncIterator interface - Without boats, dreams dry up
    (https://without.boats/blog/async-iterator/)
15. Added: (How not to) Generate a Large Prime
    (https://richardcocks.github.io/prime.html)
16. Added: Quadratic Sieve - Factoring REALLY fast
    (https://youtube.com/watch?v=x5LTBsmGfFc)
17. Added: Sami Yousef - Secure your network with Cloudflare Tunnels
    (https://blog.samiyousef.ca/secure-your-network-with-cloudflare-tunnels/)
18. Added: None of Your Business - Why, I Wonder?
    (https://yiwonder.com/none-of-your-business.html)

Generation took: 00:08:24.8964391
 Maintenance update - cleaning up homepage and feed

---

