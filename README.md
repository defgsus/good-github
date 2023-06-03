## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-02](docs/good-messages/2023/2023-06-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,044,021 were push events containing 3,386,299 commit messages that amount to 282,801,452 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e4ece2fbd6...](https://github.com/tgstation/tgstation/commit/e4ece2fbd62dfa6a1270ce37e31fe93bd1823c07)
#### Friday 2023-06-02 00:02:36 by Hatterhat

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
## [derpygamer2142/Mooer](https://github.com/derpygamer2142/Mooer)@[3ba0c11a9f...](https://github.com/derpygamer2142/Mooer/commit/3ba0c11a9fc2e77cbc3b14fbaf7e4d169244bec3)
#### Friday 2023-06-02 00:36:07 by derpygamer2142

Original commit, started at version 0.5 because fuck you.

Yeah, I swore. What are you going to do about it, nerd?

---
## [streamlit/streamlit](https://github.com/streamlit/streamlit)@[c464422e1b...](https://github.com/streamlit/streamlit/commit/c464422e1bbea66b3184769ea22599356d710f9a)
#### Friday 2023-06-02 00:37:09 by Danny Wolf

Upgrade react-range to fix memory usage of sliders (#6764)

As mentioned in
https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/
memory usage struggles in the browser if you have large ranges:

> Due to implementation details, high-cardinality sliders don't suffer
> from the serialization and network transfer delays mentioned earlier,
> but they will still lead to a poor user experience (who needs to
> specify house prices up to the dollar?) and high memory usage. In my
> testing, the example above increased RAM usage by gigabytes until the
> web browser eventually gave up (though this is something that should
> be solvable on our end. We'll look into it!)

This was caused by a bug in react-range, which I fixed last year.
https://github.com/tajo/react-range/pull/178

At the time, I had figured it would get picked up by a random yarn
upgrade and didn't worry too much about it.
But, apparently yarn doesn't really have an easy way of doing upgrades
of transitive dependencies (see https://github.com/yarnpkg/yarn/issues/4986)?
I took the suggestion of someone in that thread to delete the entry and
let yarn regenerate it.

Some technical details about the react-range fix from the original
commit message (the "application" is a streamlit app):

> We have an application that uses react-range under the hood, and we
> noticed that a range input was taking 2GB of RAM on our machines. I
> did some investigation and found that regardless of whether the marks
> functionality was being used, refs were being created for each
> possible value of the range.

> We have some fairly huge ranges (we're using the input to scrub a
> video with potential microsecond accuracy), and can imagine that
> other people are affected by the previous behavior. This change
> should allow us to continue using large input ranges without
> incurring a memory penalty.

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[2aaafd9a67...](https://github.com/GuillaumePrata/tgstation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Friday 2023-06-02 01:06:03 by TheVekter

Replaces the syndicate corpse Legions can drop with one without a MODSuit (#75700)

## About The Pull Request
This is part of a pass I'm working on doing where I go through and
remove instances of antag gear outside of their normal context. This is
mostly going to involve replacing space/Lavaland ruin gear with
something close to the same power level but not distinctly something
only antags should be able to get. I want to keep ruins rewarding but I
don't want explicit antag gear to be something you can obtain without
needing an uplink.

The first part of this is me removing the MODSuit from the syndicate
operative corpse. The new one drops a turtleneck, a syndicate gas mask,
and gripper gloves.

## Why It's Good For The Game
It's my opinion that antag gear should probably stay in antag hands
unless you manage to kill one or steal an uplink. The main impetus for
this was a discussion I had a while back about how blood red hardsuits
used to _just_ be an antag thing. I kind of miss that general feeling of
paranoia that came from seeing someone wearing it, as opposed to seeing
it these days and just thinking "Yeah, it's probably someone who got it
from space".

In this specific instance, Syndicate MODSuits are pretty strong anyway
and, regardless of the low odds of getting one, I really don't think it
should be available as loot off a fairly easy-to-kill mob.

## Changelog
:cl:
balance: Syndicate corpses dropped from killing a Legion no longer come
with a MODSuit.
/:cl:

---
## [liuzhaobing/evals](https://github.com/liuzhaobing/evals)@[93fa8a55e9...](https://github.com/liuzhaobing/evals/commit/93fa8a55e9113ebf221347af731b9a5fb6400512)
#### Friday 2023-06-02 01:19:54 by Austin Starnes

Add logic grid puzzle eval (#830)

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
`logic-grid`

### Eval description

The model is prompted with a logic grid word problem with a list of
hints, categories, and values for the category. The model is then asked
to provide a solution, showing reasoning, in a set of Python tuples that
show the matched category values.

<details>
  <summary>See human-friendly example prompt</summary>

```
Using the hints and information provided, solve the following logic grid puzzle.
Show your reasoning concisely, but step-by-step, to arrive at your final answer.
Remember, since this is a grid-based puzzle, each option in every category will be used exactly once.
Since there are 4 values per category, and 3 categories, your final answer will include 4 tuples each of length 3.
 Puzzle Scenario:
A number of new space probes were launched this year. Using only the clues that follow, match each probe to the month it launched and its eventual destination.

Category Options:
  Probes: "Nalini", "Hikaru", "Sarika", and "Sven"
  Destinations: "Ganymede", "Titan", "Enceladus", and "Phobos"
  Months: "January", "February", "March", and "April"

Hints:
  1: The Hikaru launched 2 months before the Nalini.
  2: The probe going to Phobos launched sometime after the Hikaru.
  3: The Sven launched 2 months before the mission going to Ganymede.
  4: Of the probe that launched in April and the mission going to Titan, one is the Sarika and the other is the Nalini.

In your response, format your final answer for each set of linked category values as a python tuple of strings in this order:
("Enceladus", [value from months], [value from probes])
("Ganymede", [value from months], [value from probes])
("Phobos", [value from months], [value from probes])
("Titan", [value from months], [value from probes])
```
</details>

<details>
  <summary>See expected/ideal answer</summary>

```
("Enceladus", "January", "Hikaru")
("Ganymede", "April", "Sarika")
("Phobos", "February", "Sven")
("Titan", "March", "Nalini")
```
</details>

<details>
<summary>See failure case from GPT-4 (at least from the web UI - I don't
have API access to GPT-4)</summary>

```
Step 1: From Hint 3, we know that Hikaru launched 2 months before Nalini. Since the latest month available is April, this means that Nalini cannot have launched in April because there wouldn't be a 2-month gap for Hikaru. So, Nalini must be the probe going to Titan (from Hint 4), and Sarika must be the probe that launched in April.

Step 2: Since Nalini is going to Titan, from Hint 4, it must have launched in February to allow Hikaru to launch in December (2 months before). However, December is not an option, so Hikaru must have launched in January (the earliest month possible) and Nalini in March.

Step 3: The Sven launched 2 months before the mission going to Ganymede (Hint 2). Since Sven cannot be launched in January (as Hikaru is launched in January), it must have launched in February. That means the mission to Ganymede must be in April.

Step 4: The only remaining month is March, and the only remaining probe is Nalini. So Nalini was launched in March.

Step 5: The probe going to Phobos launched sometime after Hikaru (Hint 1). Since Hikaru launched in January, the only remaining option for Phobos is Sarika, which launched in April.

Step 6: The only remaining destination is Enceladus, and the only remaining probe is Hikaru, so Hikaru is going to Enceladus.

The final answer is:
("Enceladus", "January", "Hikaru")
("Ganymede", "April", "Sven")
("Phobos", "April", "Sarika")
("Titan", "March", "Nalini")
```
</details>

### What makes this a useful eval?

This set of evals relies on a lot of *context-ramping* (as I call it)
for LLMs to get right - relying on chain-of-thought style logic to
'ramp' into the most likely next-deduction for a multi-parameter logical
problem.
These prompts are written as word problems and don't rely on any ASCII
or markdown type of table to express the puzzle (though `gpt-3.5-turbo`
appears to use markdown tables in it's chain of thought).

This ramping gets expensive and doesn't scale well with the increase of
category or values-per-category parameters, and is something that LLMs
might benefit from avoiding (either by requiring less of a context-ramp
to get to the meat of an answer, or by the surrounding
infrastructure/problem agent that tries to use a cheaper ensemble for
most of the context ramping, or other strategies).

The reasoning skills required for this kind of <b>constraint
satisfaction</b> expressed in natural language word prompts can, in
theory, generalize to solving constraints expressed in less structured
formats in the wild.

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
- [X] <span title="A GPT-4 failure case from the eval set is included
above.">Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.</span>
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **<span title="15 examples per grid size are included, for 6
different grid sizes, make a total of 90 included examples.">Include at
least 15 high quality examples.</span>**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval contains varied prompts and grid sizes, 15 examples per grid
size, for a total of 90 procedurally generated puzzles.
~This PR also implements (disabled by default) multiline answers and
punctuation whitelisting behavior in `FuzzyMatch`, which was required
due to the structural nature of the logic grid answers and the behavior
of `utils.normalize(...)` which (prior to this PR) did not provide any
functionality to interpret answers that span across newline characters
`\n` or preserve punctuation where it may be useful (in this case, the
model is prompted for the resultant grid associations in python tuple
format, so the punctuation in `(",)` is configured to be preserved for
these evals).
The new functionality is, again, disabled by default, such that existing
evals are not affected.~

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
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
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nA number of new
space probes were launched this year. Using only the clues that follow,
match each probe to the month it launched and its eventual
destination.\n\nCategory Options:\n Probes: \"Nalini\", \"Hikaru\",
\"Sarika\", and \"Sven\"\n Destinations: \"Ganymede\", \"Titan\",
\"Enceladus\", and \"Phobos\"\n Months: \"January\", \"February\",
\"March\", and \"April\"\n\nHints:\n 1: The Hikaru launched 2 months
before the Nalini.\n 2: The probe going to Phobos launched sometime
after the Hikaru.\n 3: The Sven launched 2 months before the mission
going to Ganymede.\n 4: Of the probe that launched in April and the
mission going to Titan, one is the Sarika and the other is the
Nalini.\n\nIn your response, format your final answer for each set of
linked category values as a python tuple of strings in this
order:\n(\"Enceladus\", [value from months], [value from
probes])\n(\"Ganymede\", [value from months], [value from
probes])\n(\"Phobos\", [value from months], [value from
probes])\n(\"Titan\", [value from months], [value from
probes])"}],"ideal":"(\"Enceladus\", \"January\",
\"Hikaru\")\n(\"Ganymede\", \"April\", \"Sarika\")\n(\"Phobos\",
\"February\", \"Sven\")\n(\"Titan\", \"March\", \"Nalini\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nThe Monterey Bay
Aquarium has a new exhibit featuring several dolphin skeletons. The
aquarium asked local elementary school children to name each dolphin and
match it to its species, length, and the year in which it was donated to
the aquarium. Use the given clues to solve the puzzle.\n\nCategory
Options:\n Dolphin: \"Atlantic white-sided dolphin\", \"Pacific
white-sided dolphin\", \"common dolphin\", and \"bottlenose dolphin\"\n
Names: \"Momo\", \"Simon\", \"Tychus\", and \"Marlo\"\n Lengths: \"21
ft\", \"23 ft\", \"25 ft\", and \"27 ft\"\n\nHints:\n 1: Momo is 4 feet
shorter than Tychus.\n 2: The common dolphin is somewhat shorter than
the bottlenose dolphin.\n 3: The 21 ft long exhibit is either the
Atlantic white-sided dolphin or Simon.\n 4: Marlo is either the 23 ft
long exhibit or the Atlantic white-sided dolphin.\n 5: Of Simon and the
Pacific white-sided dolphin, one is 27 ft long and the other is 21 ft
long.\n\nIn your response, format your final answer for each set of
linked category values as a python tuple of strings in this
order:\n(\"Atlantic white-sided dolphin\", [value from lengths], [value
from names])\n(\"Pacific white-sided dolphin\", [value from lengths],
[value from names])\n(\"bottlenose dolphin\", [value from lengths],
[value from names])\n(\"common dolphin\", [value from lengths], [value
from names])"}],"ideal":"(\"Atlantic white-sided dolphin\", \"25 ft\",
\"Marlo\")\n(\"Pacific white-sided dolphin\", \"27 ft\",
\"Tychus\")\n(\"bottlenose dolphin\", \"23 ft\", \"Momo\")\n(\"common
dolphin\", \"21 ft\", \"Simon\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nHillcrest County
Hospital released a press release today to announce its annual list of
the first babies born immediately after the start of the new year. Using
only the clues below, match each baby to its family time of birth, and
determine the room number in which it was delivered.\n\nCategory
Options:\n Names: \"Lydia\", \"Naomi\", \"Katherine\", and \"Rebecca\"\n
Families: \"McIntyre\", \"Gonzalez\", \"Hudson\", and \"O'Connor\"\n
Times: \"12:01am\", \"12:04am\", \"12:07am\", and
\"12:10am\"\n\nHints:\n 1: Naomi was born 3 minutes after Rebecca.\n 2:
The Hudsons' child was born 6 minutes after the O'Connors' child.\n 3:
The baby born at 12:04am was either Rebecca or the McIntyres' child.\n
4: Of Katherine and the baby born at 12:01am, one was the O'Connors' and
the other was the Gonzalezes'.\n\nIn your response, format your final
answer for each set of linked category values as a python tuple of
strings in this order:\n(\"Gonzalez\", [value from names], [value from
times])\n(\"Hudson\", [value from names], [value from
times])\n(\"McIntyre\", [value from names], [value from
times])\n(\"O'Connor\", [value from names], [value from
times])"}],"ideal":"(\"Gonzalez\", \"Katherine\",
\"12:10am\")\n(\"Hudson\", \"Lydia\", \"12:07am\")\n(\"McIntyre\",
\"Naomi\", \"12:04am\")\n(\"O'Connor\", \"Rebecca\", \"12:01am\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nMedisynth
Therapeutics has spent decades scouring the world's rainforests for new
sources of medical drugs, and this year a number of these new drugs have
been officially approved by the FDA. Using only the clues below, match
each drug to the condition it treats, the month it was approved, and the
source from which its main ingredient is derived.\n\nCategory Options:\n
Drugs: \"Mystolam\", \"Soludox\", \"Aurexil\", and \"Synodil\"\n
Conditions: \"rheumatism\", \"chikungunya\", \"hyperglycemia\", and
\"encephalitis\"\n Months: \"January\", \"February\", \"March\", and
\"April\"\n\nHints:\n 1: The medicine that treats hyperglycemia was
approved sometime after Synodil.\n 2: The medicine that treats
hyperglycemia was approved 1 month before the medicine that treats
rheumatism.\n 3: Of Mystolam and the pharmaceutical approved in April,
one treats rheumatism and the other treats encephalitis.\n 4: Of the
Aurexil approved in February and the drug that treats chikungunya, one
is Soludox and the other is Synodil.\n\nIn your response, format your
final answer for each set of linked category values as a python tuple of
strings in this order:\n(\"chikungunya\", [value from drugs], [value
from months])\n(\"encephalitis\", [value from drugs], [value from
months])\n(\"hyperglycemia\", [value from drugs], [value from
months])\n(\"rheumatism\", [value from drugs], [value from
months])"}],"ideal":"(\"chikungunya\", \"Synodil\",
\"January\")\n(\"encephalitis\", \"Soludox\",
\"April\")\n(\"hyperglycemia\", \"Aurexil\",
\"February\")\n(\"rheumatism\", \"Mystolam\", \"March\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nA group of friends
has gotten together for dinner, and just for fun they're comparing their
\"social networking\" stats on Facebook, Twitter and LinkedIn. Using
only the clues that follow, determine the number of friends (Facebook),
followers (Twitter) and connections (LinkedIn) each person
has.\n\nCategory Options:\n Names: \"Avery\", \"Evan\", \"Natalia\", and
\"Camila\"\n Linkedin: \"54\", \"59\", \"64\", and \"68\"\n Facebook:
\"120\", \"130\", \"140\", and \"150\"\n\nHints:\n 1: Avery has 68
LinkedIn connections.\n 2: Natalia has 10 fewer Facebook friends than
the person with 68 LinkedIn connections.\n 3: The person with 140
Facebook friends is either the one with 54 LinkedIn connections or
Evan.\n 4: The one with 54 LinkedIn connections has 10 fewer Facebook
friends than the one with 64 LinkedIn connections.\n\nIn your response,
format your final answer for each set of linked category values as a
python tuple of strings in this order:\n(\"120\", [value from LinkedIn],
[value from names])\n(\"130\", [value from LinkedIn], [value from
names])\n(\"140\", [value from LinkedIn], [value from names])\n(\"150\",
[value from LinkedIn], [value from names])"}],"ideal":"(\"120\", \"59\",
\"Natalia\")\n(\"130\", \"68\", \"Avery\")\n(\"140\", \"54\",
\"Camila\")\n(\"150\", \"64\", \"Evan\")"}
  ```
</details>

---
## [liuzhaobing/evals](https://github.com/liuzhaobing/evals)@[b0650402dd...](https://github.com/liuzhaobing/evals/commit/b0650402ddeaf93dba27f4a0252ae890bf8184ab)
#### Friday 2023-06-02 01:19:54 by Alexander Shirkov

[Eval] English-Russian homonym context resolution (GPT-3.5: 0.42) (#1064)

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
English-Russian homonym context resolution

### Eval description

Cross-lingual English-Russian eval to resolve ambiguity with homonyms
present.

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]
Cross-lingual homonyms are hard to resolve: they add context ambiguity,
which needs to be resolved via reasoning.

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
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. What
would \"каток\" mean in this context? rink or roller"}], "ideal":
"unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. Child
pointing at the machine and says: \"каток\". What does he mean: rink or
roller?"}], "ideal": "roller"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. Child
pointing at the building and says: \"каток\". What does he mean: rink or
roller?"}], "ideal": "rink"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone says \"хорошая коса\". Do they refer scythe or
hairstyle?"}], "ideal": "unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone points at the quality of her work and says
\"хорошая коса\". Do they refer scythe or hairstyle?"}], "ideal":
"scythe"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone points at her head and says \"хорошая коса\". Do
they refer scythe or hairstyle?"}], "ideal": "hairstyle"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "Scythe
is found on a sandbar. A person is saying: \"коса\". Do they refer
scythe or sandbar?"}], "ideal": "unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "Scythe
is found on a sandbar. A person is saying: \"ржавая коса\". Do they
refer scythe or sandbar?"}], "ideal": "scythe"}
  ```
</details>

---
## [liuzhaobing/evals](https://github.com/liuzhaobing/evals)@[e959ff4b90...](https://github.com/liuzhaobing/evals/commit/e959ff4b90c3511f5b8a91ca69413a9206d8c4c7)
#### Friday 2023-06-02 01:19:54 by Vasco Lange

[Eval] German part-of-speech (#1053)

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
> german-part-of-speech

### Eval description

> For a given German word, the model is asked to list all possible parts
of speech (multiple choice). The model is also asked to think about the
word as an inflection of another word. The models output is tested
against annotations extracted from de.wiktionary.org. This is a follow
up to #1039

### What makes this a useful eval?

> Part of speech analysis is a basic task in language / grammar classes.
While it is usually done in the context of a sentence, coming up with
possible uses in lack of a sentence requires a certain amount of
creativity and language understanding, or very good recall of
information that is usually sparse outside of dictionaries. The task in
this eval could be seen as a combination of part of speech analysis and
an easy-to-evaluate form of the question "How could x be used in a
sentence".

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

> To build the dataset, all 1.000.000+ entries of the German wiktionary
were parsed. Excluded from this list were all phrases, abbreviations,
symbols, names, toponyms and any words with at least one possible part
of speech not fitting the categories given in the prompt. Also I had to
exclude some entries where the part of speech could not be determined
automatically from the wikitext.
> From this set, words were sampled so that each combination of the
parts of speech existing in the dataset would be equally likely in the
tests. This way the model is tested to respond with all possible uses of
a word and not just the most common ones. > For combinations that fit a
lot of words, the uniform sampling led to a bias towards rarely used
words.
> The labels of each word were taken from the corresponding page at
de.wiktionary.org/wiki/{word}. The information taken from each page was:
the word, the part of speech this word can have in German and whether
the word is an abbreviation or not.
> This means only factual data was taken and is therefore in the public
domain.

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
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "anstelle"}],
"ideal": ["preposition, adverb, verb.", "preposition, verb, adverb.",
"adverb, preposition, verb.", "adverb, verb, preposition.", "verb,
preposition, adverb.", "verb, adverb, preposition."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "heute"}],
"ideal": ["adverb, verb.", "verb, adverb."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "Mist"}],
"ideal": ["noun, interjection.", "interjection, noun."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "Rotschöpfe"}],
"ideal": ["noun."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "vornüber"}],
"ideal": ["adverb."]}
  ```
</details>

---------

Co-authored-by: Vasco Yannic Lange <mail@vascolange.com>

---
## [DanaDririon/Skyrat-tg](https://github.com/DanaDririon/Skyrat-tg)@[bfb3967c90...](https://github.com/DanaDririon/Skyrat-tg/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Friday 2023-06-02 01:22:48 by SkyratBot

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
## [derpygamer2142/Mooer](https://github.com/derpygamer2142/Mooer)@[4babf13672...](https://github.com/derpygamer2142/Mooer/commit/4babf1367257991c9b2d75efad3a0323cf8ae6e9)
#### Friday 2023-06-02 01:29:32 by derpygamer2142

started working on account system

still, fuck you

---
## [AaronGoldsmith/evals](https://github.com/AaronGoldsmith/evals)@[4eb8180b2a...](https://github.com/AaronGoldsmith/evals/commit/4eb8180b2a5fc26df987978e73a94e6dfdff5e96)
#### Friday 2023-06-02 02:08:36 by lillichoung

Shopping discount comparison eval (#779)

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
Shopping Discount Comparison

### Eval description
This evaluation tests the model's ability to compare different offers
and select the best deal based on cost.

### What makes this a useful eval?
A future application of AI will be to help people make purchases. This
task requires AI to understand common discounts and apply them to value
calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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
{"input": [{"role": "system", "content": "You are a helpful AI aiding me
in getting the best price in online shopping. You will determine which
shop I should purchase from, based on lowest cost (including shipping)
alone. Assume shops all sell the same product. Respond with the shop
number ONLY with no punctuation and do not give an explanation. Example
output: Shop 1"}, {"role": "user", "content": "I want to buy 1 lb of
beans. [Shop 1: $30 | 1 lb | Free shipping on all orders of $20 or more
| Shipping $10 ] [Shop 2: $27 | 1 lb | Shipping $5 ] Answer:"}],
"ideal": "Shop 1"}
{"input": [{"role": "system", "content": "You are a helpful AI aiding me
in getting the best price in online shopping. You will determine which
shop I should purchase from, based on lowest cost (including shipping)
alone. Assume shops all sell the same product. Respond with the shop
number ONLY with no punctuation and do not give an explanation. Example
output: Shop 1"}, {"role": "user", "content": "I want to buy a tote bag.
[Shop 1: 48€ | 8€ flat fee shipping | 20% off purchases over 40€ ] [Shop
2: 42€ | 6€ shipping | 10% off purchases over 47€] Answer:"}], "ideal":
"Shop 1"}
{"input": [{"role": "system", "content": "You are a helpful AI aiding me
in getting the best price in online shopping. You will determine which
shop I should purchase from, based on lowest cost (including shipping)
alone. Assume shops all sell the same product. Respond with the shop
number ONLY with no punctuation and do not give an explanation. Example
output: Shop 1"}, {"role": "user", "content": "I want to buy 2 items.
[Shop 1: $75.00 | Buy one get one 20% off | $5 shipping ] [Shop 2:
$75.00 | Free shipping | 15% off if you buy more than one] Answer:"}],
"ideal": "Shop 2"}
  ```
</details>

---
## [AaronGoldsmith/evals](https://github.com/AaronGoldsmith/evals)@[34befaceb4...](https://github.com/AaronGoldsmith/evals/commit/34befaceb43c746b68ccce7eaca3c43a15d23404)
#### Friday 2023-06-02 02:08:36 by Rafal Zawadzki

Add Polish lexicon eval (#794)

## Eval details 📑
### Eval name
`polish-lexicon`

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Polish words.

### What makes this a useful eval?

Polish language is hard - and I have not seen good evals created for it
yet. This eval is inspired by similar ones in Belarusian, Bulgarian and
Greek. Polish has a mix of Latin and special characters and it's common
even for a native speaker to make spelling or grammatical mistakes.
The eval set is comprised of a mix of totally invented by me words as
well as words with spelling errors.
I ran it with GPT-3.5-Turbo and its accuracy was around 60%. I also did
limited testing with GPT4 and while it seems like it deals better with
spelling mistakes, it is still not that good at recognising invented
words.

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
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "przewądnicy"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "przewodnicy"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "waższe"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "wyższe"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "handlą"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "handlu"}], "ideal": "Y"}
  ```
</details>

---
## [StevenLaczko/BorisBot](https://github.com/StevenLaczko/BorisBot)@[b4d6c9bb1e...](https://github.com/StevenLaczko/BorisBot/commit/b4d6c9bb1ee27a8c766946f93ded0c3b85a62380)
#### Friday 2023-06-02 02:09:22 by Steven Laczko

Beginning work toward Boris having different prompts, memories, and moods in different contexts. Holy shit this is amazing.

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[8fa6242c66...](https://github.com/GuillaumePrata/tgstation/commit/8fa6242c66205866b702440f490eeae34ef6b85f)
#### Friday 2023-06-02 02:29:18 by Bloop

Refactors High Luminosity Eyes, fixes a ton of bugs related to it as well as qol improvements (#75040)

## About The Pull Request

The high luminosity eyes item was extremely out of date, broken, and
full of copy paste code from atom lighting. Which is a shame because
they were cool.

On top of all that it was using a special light effect that was not very
performant. I got rid of all that, hooked it into atom lighting as a new
light type, and gave it a new TGUI as well because the old ui prompts
were not great either.

You can now pick a color at random if you want. You can also set the
color and range before surgically implanting them. No more being forced
to go through the color picker when you just want to change the range.

Functionally they should pretty much should be the same as before with
some bonus features (see below).


![dreamseeker_nDeLNyOOG2](https://user-images.githubusercontent.com/13398309/235325530-105fe82e-ecc8-4dc4-9c84-143cc6519688.gif)

Closes https://github.com/tgstation/tgstation/issues/61041
Closes https://github.com/Skyrat-SS13/Skyrat-tg/issues/14685

This is 100% completed. I just finished fixing the slight translation
bug when going from 0->1 range (see above gif) and that was the last
thing on my bucket list. I happy enough with this at this point in time.

---

EDIT: 

I have decided to add in one last new feature, and that is...
independent settings for eye color.

<details> <summary>You can now set eye color independently if you
wish</summary>


![dreamseeker_j32B2S4yXQ](https://user-images.githubusercontent.com/13398309/235412568-ffa8e424-8624-4462-9f6f-77c1513aa773.gif)

</details>

The eye color does not modify the light color in any way when set in
this manner, but it can be used for cosmetic purposes.

Kind of makes the item more like cybereyes from cyberpunk, which I think
are pretty neat!

</details>

### What I've done, in more detail:

- refactored high luminosity eyes so they use the atom lighting system
instead of the way they were doing it before
- the new light type, `MOVABLE_LIGHT_BEAM` behaves similarly to
directional lights, with some slight differences. it reuses the same
lighting overlay sprites but scales them vertically to produce a more
focused effect. The result can be seen above. This is in contrast to the
old way, which spawned `range` number of individual 32x32 overlays and
moved them around. This way should perform better as well as be more
maintainable.
- added a new TGUI interface for high luminosity eyes with buttons for
range, a text field for a color hex, a color picker and randomizer
- made the eye overlay emissive when the light is turned on
- range goes from 0 to 5. at range 0, the light overlay is turned off
and you are left with just the emissive eyes.
- added a cosmetic functionality to this item that lets you change the
color of your eyes independently of the lighting (and each other)
- fixed a bug with directional flashlights sometimes not updating their
lighting overlay if you pick them up without changing your direction
---

### Other Misc Fixes

Being able to dynamically set range back and forth exposed some logic
issues that had existed with directional light overlays and I have fixed
those. That is why there are some edits in that file that may not appear
readily obvious why they are there.

Apart from that, two other bugs that come to mind:
1) eye code was supposed to keep track of the eye color you had before
you got new eyes, but it was overwriting that every time you ran
refresh().
2) lighting was supposed to be turning off the light when range is set
to 0, but it was not doing that properly.

And of course besides that, there may have been a few instances of
finding typos/tidying up code

## Why It's Good For The Game

The code for this was like 6 years old and in desperate need of
updating. Now it works, and has a nicer UI.

## Changelog

:cl:
fix: high luminosity eyes light overlays now follow the user correctly
qol: high luminosity eyes now have a tgui menu so you no longer have to
go through the color picker every time you want to change the range.
they also have a new setting that lets you change the color of your eyes
independently of the light color. You can now have cybernetic
heterochromia if you want
fix: directional flashlights when picked up will now always update their
cast light direction correctly no matter what dir you are facing
refactor: refactors high luminosity eye code to better make use of the
atom lighting system, adding a new light type 'MOVABLE_LIGHT_BEAM'
/:cl:

---
## [41junkard/cmss13pro](https://github.com/41junkard/cmss13pro)@[6f1b1717a7...](https://github.com/41junkard/cmss13pro/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Friday 2023-06-02 02:54:22 by TotalEpicness

Boiler rework Part 1: Globber base boiler (#965)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request


A total redesign of the base boiler reminiscent of the old premoba
boiler that would shoot projectile "Globs" with a modern CM take.

Base boiler as it is right now, is completely unfun, to play against and
to even play as. You'd be hard-pressed to find someone who enjoys
playing it past the first 10 minutes of doing so. It is this way not
because it's weak, but because it's unchallenging and 100% "safe"
gameplay. There are no combos, cool moves you can do, or even satisfying
effects, you just hit a button to spawn a telegraph which becomes a gas
cloud.

This PR, turns that right ontop of its head. Instead of "safe" gameplay,
globber's design philosophy is centered around being challenging, fun
and even adding new gameplay dynamics.

Globber will have higher HP, faster walkspeed, and faster firing bombard
compared to premoba.

However, globber will have their fellow xenos making plays to cover for
boiler, either directly through bodyblocking shots or making plays to
distract marines due to a minimal zoom range.

These both, in theory, will create a new gameplay dynamic where boilers
will still be able to block marine spearheads, but Globber needs to help
make a small counter push with their fellow brethren in order for
Globber to directly strike at marines and giving the Xenos the choice to
either capitalize on their advantage or heal up upon a successful glob.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

### Details:
Globber will feature [TENTATIVE] higher HP and [TENTATIVE] faster walk
speed. It however will be slightly more vulnerable to fire as fire deals
[TENTATIVE]% more damage to it!


https://cdn.discordapp.com/attachments/458150341742166017/1013647188313776148/2022-08-28_17-10-53.mov

Globber Active 1 - Bombard: Spit a large acid glob that will, upon
impact, immediately spread a gas glob of your choice

- Cooldown: 30 seconds
- cost: 200 plasma
- Windup: 5 seconds

Globber Active 2 - Acid spray, instantly sprays a line of acid, May make
it a cone spray if it is too weak

- 8 second c/d
- No windup
- 40 plasma
- 6 tile range

Globber Active 3 - Shift spits: Switch between acid and neuro gas globs.
Acid deals more raw damage while neuro slows,blinds and eventually
knocks down marines. Neuro has a larger radius than acid

Globber Active 4 - Acid shroud: A quick windup action that dumps an acid
cloud over the boiler. Cooldowns other abilities similar to dump acid.

Globber Active 5 - Zoom: Short ranged zoom with short windup. Trades
awareness for zoom

Globber Passive: Brute armor, Globber features brute armor, however, it
does not protect against flames! Globber takes 1.5x damage to fire!

Acid glob: Pretty much the same as before. May adjust numbers.

Neuro smoke rework:
- Instead of insta blindness and deafness, these will now have a chance
of applying for every tick you are in the smoke. You still have
blurry/weldervision though
- Oxyloss toned down, it was 9 per tick, now two
- Knockdown chance lowered to 5% per tick. Stamina damage replaces RNG
knockdowns
+ Now deals stamina damage, and am making it stack fast, targeted
knockdown time is 2-3 seconds
+ Minor immediate slowdown applied. May remove as it stacks with stamina
damage slow
+ chance of dealing minor tox damage

### Boiler rework as a whole

The boiler rework is a total rework of the boiler strain and it's
strains.

I'm not gonna write the entire design doc here, but in short:

-Base boiler will be reworked (as shown here), named Globber
- trapper will be totally scrapped for 'Grenadier', a heavy siege strain
that lobs devastating nades that's counterable and challenging.
Grenadier will have the same zoom as Globber
- A long-range, general-purpose strain will be added, named "Striker
Boiler", which combines both the Railgun boiler and the mostly forgotten
"Acid Splatter" strains in the past, with a modern CM twist.

design docs( old as fuck and needs updating) _**REPLACE ME WITH NEW
ONE**_
https://github.com/cmss13-devs/cmss13-design-docs/pull/7
Striker design doc
https://github.com/cmss13-devs/cmss13-design-docs/pull/8


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
TL;DR base boiler is a literal NPC strain that no one likes to play as
or against. Attempt to make it more fun or die trying

if the design philosophy fails, then we can simply just tweak a few
values and have premoba boiler again.

Design doc is already made but its ancient as shit and I'm just gonna
make a new one so its WIP for now.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Totalepicness
add: Added "Globber Boiler", which is a total replacement of base
boiler, designed to kill the "safe" gameplay loops of current base
boiler in an attempt for a more challenging and fun caste to both play
as and against.
balance: Globber Active 1 - Bombard: Spit a large acid glob that will,
upon impact, immediately spread a gas glob of your choice
balance: Globber Active 2 - Spray acid: Instantly sprays a line of acid
balance: Globber Active 3 - Shift spits: Switch between acid and neuro
gas globs. Acid deals damage while neuro slows, blinds and eventually
knocks down marines. Neuro has a larger radius than acid
balance: Globber Active 4 - Acid shroud: A quick windup action that
dumps an acid cloud over the boiler. Cooldowns other abilities similar
to dump acid.
balance: Globber Active 5 - Zoom: Short-ranged zoom with no windup.
balance: Globber Passive: Globber features armor, but it is weaker
against flames! Stay away from fire!
refactor: Refractored some minor spit code and icons
balance: Neuro has been completely reworked to deal mainly stamina
damage, causes dizzyness and has a small chance to make you 'stumble' in
a random direction along with minor tox damage. Stay out of it!
add: Completly reworked neuro gas, it now uses a proper effect with
escalating effects the larger the dosage rather than RNG.
fix: Acid now deals damage to cades and now has a good chance of going
over instead of being airtight
fix:  Boiler globs no longer can target mobs and track them.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: Geeves <ggrobler447@gmail.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: harryob <me@harryob.live>

---
## [rd-stuffs/android_kernel_xiaomi_surya](https://github.com/rd-stuffs/android_kernel_xiaomi_surya)@[7bce204ee2...](https://github.com/rd-stuffs/android_kernel_xiaomi_surya/commit/7bce204ee25c0f0d2c66b4a6f76f76a9c71785d1)
#### Friday 2023-06-02 03:22:18 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [gradientsky/evals](https://github.com/gradientsky/evals)@[e116ede848...](https://github.com/gradientsky/evals/commit/e116ede848957eff8e76b5d8463ed5291163a28f)
#### Friday 2023-06-02 04:31:20 by Wesley Barlow

Add eval: rhetorical-devices (#1005)

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
rhetorical-devices

### Eval description

Evaluates model's ability to select the most specific rhetorical
modification of a sentence from a multiple choice with a large number of
nuanced rhetorical devices.

### What makes this a useful eval?

Useful for using LLMs to write novels and generate consistent/parametric
authorial tone.

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
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL She likes to listen to the winds. MODIFIED
She swoons at such sweet gales. Answer in the format (x) Rhetorical"}],
"ideal": "(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL The rock was very large. MODIFIED The rock
was remarkably raised. Answer in the format (x) Rhetorical"}], "ideal":
"(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Visionary dreams elevate me at night.
MODIFIED Visionary reminitions elevate self resting in lightlessness.
Answer in the format (x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Once, I thought I had lost her pet.
MODIFIED Once, dunce — thought I lost Juliet's pet. Answer in the format
(x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Do you want to understand research on
artificial general intelligence? MODIFIED Don't you want to investigate
artifacts of artificial general intelligence? Answer in the format (x)
Rhetorical"}], "ideal": "(c) Consonance"}
  ```
</details>

---
## [gradientsky/evals](https://github.com/gradientsky/evals)@[b91292c803...](https://github.com/gradientsky/evals/commit/b91292c803af2bdadeec3853ab03514b73310109)
#### Friday 2023-06-02 04:31:20 by Zyenith

Add Eval: Internal Representations via Counting (#1006)

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
Internal representations via counting

### Eval description

Using series of logical questions that require multiple (simple)
manipulations of numbers to get the ideal answer. These are basic tasks
that should be doable by an LLM, but require several steps of internal
"thought" to get right.

### What makes this a useful eval?

Situations with number manipulation with multiple steps are prevalent
anywhere in the modern world. Testing the internal representation of the
LLM can provide other insights on how well its "mind" processes
information.

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

This eval is capable of providing insight into the LLM's internal
representation of objects versus answering fact-based questions or
straightforward complex logic puzzles.

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
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"Roger and Emily are in a room.
Roger puts a cat in an empty box while Emily is in the room. They both
leave, and Emily returns and puts a turtle in the box as well. How many
items does Roger think are in the box?"}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are four darts already on a
dart board. Bob throws one dart at the dartboard, and it lands. Alice
throws two darts, and one misses but one hits the dartboard. How many
darts are on the dartboard?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"A bakery sold 25 cakes in the
morning and 17 cakes in the afternoon. The day after, they sold 15 more
cakes. How many cakes did they sell on the second day?"}],"ideal":"15"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are six blue birds and three
red birds sitting on a tree. Two blue birds fly away, and one red bird
flies away. How many birds are left on the tree?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"John has double the amount of
pencils than Sarah, and Sarah has as many pencils as Mark. Mark has 2
pencils. How many pencils does John have?"}],"ideal":"4"}
  ```
</details>

---
## [gradientsky/evals](https://github.com/gradientsky/evals)@[3d9de9a624...](https://github.com/gradientsky/evals/commit/3d9de9a62411f9e6a999e96ce8f07eebf0e8c121)
#### Friday 2023-06-02 04:31:20 by dyar-al-ashtari

Eval Norwegian lexicon (#1044)

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
`norwegian-lexicon`

### Eval description

This eval uses valid Norwegian words taken from the dictionary and
assesses whether GPT can recognize them as valid.

### What makes this a useful eval?

The Norwegian language is simple yet complicated at the same time. There
are a lot of words that are valid Norwegian words that do not get
recognized anymore. An AI should be able to identify these words with
precision. All of the words used in the samples are valid Norwegian
words and can be found in the dictionary. After assessing GPT-4 (through
the playground) and GPT-3.5 -- it failed to recognize most of the words.
Some of the words would return positive during some evals. Other times
it wouldn't recognize them. After asking GPT why it is not a valid word,
it would apologize and fix its mistake.

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
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Skarpne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Bløtne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Hovedantall"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Klenge"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Blankolov"}],"ideal":"Y"}
  ```
</details>

---
## [gradientsky/evals](https://github.com/gradientsky/evals)@[6a37c9b51b...](https://github.com/gradientsky/evals/commit/6a37c9b51b48a2f735898846cfb08b37cbd63179)
#### Friday 2023-06-02 04:31:20 by Aaron Goldsmith

[eval] 3x3 Game Of Life  (#345)

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
GOL

### Eval description

Determine the next state of a 3x3 Game of Life Board. 

### What makes this a useful eval?

Spacial reasoning

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
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n0 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 0\n\n0 1
0\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n1 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n1 0
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n1 1
1\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n0 0
0\n\n1 0 1"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n0 1
1\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 1\n\n0 1
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 0\n\n0 0
0\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 0 0\n\n1 1
0\n\n0 0 0"]}
  ```
</details>

---
## [Ay-Dee/portfolio-website](https://github.com/Ay-Dee/portfolio-website)@[0e11cb96d7...](https://github.com/Ay-Dee/portfolio-website/commit/0e11cb96d74d0b7b4cb286ca8338e54c518ae9f0)
#### Friday 2023-06-02 05:23:23 by Ay-Dee

Update README.md

Hello and welcome to my portfolio website! My name is Ahmed, and I am a dedicated web developer on a journey to create impactful digital experiences. With a solid foundation in both front-end and back-end development, I combine technical expertise with a creative mindset to build dynamic and user-friendly web applications.

Throughout my career, I have worked on a diverse range of projects, each contributing to my growth as a developer. From crafting visually stunning and responsive designs to implementing robust back-end functionalities, I have developed a holistic understanding of the web development process.

My passion for clean and efficient code drives me to embrace industry best practices and stay updated with the latest technologies and trends. I believe that a well-designed website should not only captivate users visually but also provide an intuitive and seamless experience.

Within my portfolio, you will find a collection of projects that showcase my skills and capabilities. From e-commerce platforms to social media dashboards, each project demonstrates my ability to translate ideas into functional and user-centric applications. By leveraging modern frameworks, databases, and deployment techniques, I strive to create reliable and scalable solutions.

I am committed to collaborating with clients and fellow developers to bring their visions to life. Whether you have a specific project in mind or need guidance on enhancing your online presence, I am eager to discuss your requirements and explore how we can work together.

Thank you for visiting my portfolio website. Feel free to browse through my projects and get in touch with me via the contact information provided. Let's embark on a journey of innovation and create meaningful digital experiences together.

---
## [j6t/git](https://github.com/j6t/git)@[07f91e5e79...](https://github.com/j6t/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Friday 2023-06-02 05:44:36 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [AKAshvay/Problem_Solving](https://github.com/AKAshvay/Problem_Solving)@[0c64082d32...](https://github.com/AKAshvay/Problem_Solving/commit/0c64082d3267f801fd53412c8b21e324c9b358af)
#### Friday 2023-06-02 06:16:55 by shivansh rahangdale

Create Santa Banta

https://practice.geeksforgeeks.org/problems/santa-banta2814/1

Santa Banta
MediumAccuracy: 41.96%Submissions: 8K+Points: 4
Santa is still not married. He approaches a marriage bureau and asks them to hurry the process. The bureau checks the list of eligible girls of size N and hands it over to Santa. Santa being conscious about his marriage is determined to find a girl with maximum connections so that he can gather more information about her. Accordingly, he looks to figure out the maximum number of girls (from the list) who know each other to achieve the above purpose.

In order to finalize the girl, he needs to find the Kth prime. Where k = largest group of girls who know each other. Considering Santa's poor knowledge of Maths, he seeks Banta's help for the answer. Now you, a fan of Santa Banta Jokes, take this prestigious opportunity to solve the problem.

In case no of connections is zero, print "-1". Here the connection between girls is represented by a 2-D array arr of dimension M*2, where M is the number of connections.

Note :
1. Suppose girl "a" knows girl "b" and girl "b" knows girl "c", then girl "a" also knows girl "c". Transitivity holds here.
2. Consider 1 as a composite number.
3. For precompute function given in the template you just have to complete it and use it wherever required, do not call it again and again, it is already being called by driver function before executing test cases. 

Example 1:

Input : 
arr[] = {{1,2},{2,3},{3,4},{4,5},{6,7},{9,10}}
N = 10 and M = 6
Output : 
11
Explanation:
Here in this graph there are 4 groups. 
In 1st group: (1 -> 2 -> 3 -> 4 -> 5) are 
there. In 2nd group: (6 -> 7) are there.
In 3rd group: (8) is there.
In 4th group: (10 -> 9) are there.
In these 4 group the maximum number of 
value is 5. So, K = 5 and the 5th prime number 
is 11. Return 11.
Example 2:

Input : 
arr[ ] = {{1, 2}}
N = 2 and M = 1 
Output : 
3
Explanation:
In this Example there will only be a 
single group of 2 girls, and hence the 
value of K is 2, The 2nd prime is 3.
Your Task:

This is a function problem. The input is already taken care of by the driver code. You only need to complete the function helpSanta() that takes a number of girls (n), a number of connections (m), an adjacency list of girls connections (g), and return the Kth prime no if there are no connections then return -1. The driver code takes care of the printing.

Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(N + M).

Constraints:

1 ≤ n ≤ 105
0 ≤ m ≤ 105
1 ≤ u, v ≤ n

---
## [vicky-kumar123/vicky](https://github.com/vicky-kumar123/vicky)@[7f224f077b...](https://github.com/vicky-kumar123/vicky/commit/7f224f077bfe8ee99346aca6e4b42d885772f459)
#### Friday 2023-06-02 06:41:40 by vicky-kumar123

Five benefits of dining table plants

Dining table plants can bring numerous benefits to your home and dining experience. Here are five benefits of having dining table plants:
Aesthetically pleasing: Dining table plants add a touch of natural beauty and freshness to your dining area. They enhance the overall aesthetic appeal of the space and create a more inviting and relaxing ambiance for meals. The presence of greenery can uplift the mood and make dining a more enjoyable experience.
Improved air quality: Plants are natural air purifiers. They absorb carbon dioxide and release oxygen, which helps to improve the air quality in your home. Having plants on your dining table can help remove toxins and pollutants from the air, creating a healthier environment for you and your family to enjoy meals.
Stress relief: Research has shown that being around plants and nature can reduce stress and promote relaxation. Having dining table plants can create a soothing and calming atmosphere, making your dining experience more peaceful. It can also be a visual distraction from the daily stresses and provide a moment of tranquility during meals.
Conversation starters: Dining table plants can serve as interesting conversation starters, especially if you have unique or exotic plants. Guests and family members can admire and inquire about the plants, leading to engaging discussions and a sense of connection. It adds a layer of intrigue and personality to your dining space.
Connection with nature: Incorporating plants into your dining area helps to establish a connection with nature, even if you live in an urban environment. This connection can be therapeutic and refreshing, providing a sense of well-being and harmony. Being close to nature, even indoors, can remind us of the beauty and balance of the natural world.
Overall, dining table plants offer not only visual appeal but also health benefits, stress relief, and a connection to nature. They create a more inviting and enjoyable dining environment for you and your loved ones, don’t wait and grab the online plant of your .

---
## [gyrovorbis/libgimbal](https://github.com/gyrovorbis/libgimbal)@[fcd8772307...](https://github.com/gyrovorbis/libgimbal/commit/fcd8772307ebf1fc100938906b2556e033dd96b9)
#### Friday 2023-06-02 07:44:36 by Falco Girgis

Cleanup, GblScanner, GblSettings, platforms, etc

1) CMakeLists
    - bumped Android platform/API level from 28 to 33
2) Doxyfile
    - changed MDFILE_AS_MAIN_PAGE to be blank
3) GblBoolProperty
    - deleted
4) gimbal_thread_.h, gimbal_system_.h
    - added new platform-specific headers
5) Doxygen Author: added myself to every header
6) GblArenaAllocator
    - combined GblArenaAllocator_alloc() and
      GblArenaAllocator_allocAligned() into a single function with
default values
7) GblTreeSet
    - renamed comparator/destructor types
    - started working on increasing API coverage
8) GBL_RESULT
    - added GBL_RESULT_ERROR_INVALID_TOKEN
9) gimbal_typedefs.h
    - got rid of GBL_SIZE_FMT ifdef that added it on Dreamcast--should
      be built into toolchain now
10) GblVariant
    - added GblVariant_hash
    - removed GBL_NOEXCEPT from all shit in source file
11) GblStringBuffer
    - cleaned up, reorganized macros
12) GblStringRef
    - cleaned up
    - added redundant API with consistent naming scheme
13) GblStringView
    - cleaned up macros
    - redid all conversion functions to take optional GblBool pointer
      for success/failure
    - added conversion functions for all primitive types
    - conversion functions now actually check for failure and report it
    - added gimbal_string_view.c and stopped inlining fucking EVERYTHING
14) GblScanner
    - moved instance and class private shit into source as actual
      private structures
    - extended GBL_SCANNER_FLAGS
    - only one virtual function for fetching next token
    - added API for GblScannerClass's default delimeters
    - redid back-end to automatically handle error reporting with cursor
      position
    - implemented almost entirety of API with consistent back-end model
15) GblSettings
    - ironed out API and header
    - implemented most of core back-end, but need API around it
    - decided halfway through that GblTreeSet would be a better
      structure to use than GblHashSet, but still might need more work
on that container
        * provides in-order iteration for loading/saving back-ends
16) GblCmdParserTestSuite
    - fixed bug that got exposed from GblStringView conversion refactors
      where one of the argument types was UINT32, yet we were checking
for success upon passing some negative value

---
## [vasudha45/OCTANET_JUNE_](https://github.com/vasudha45/OCTANET_JUNE_)@[826b1f5f27...](https://github.com/vasudha45/OCTANET_JUNE_/commit/826b1f5f274c28c29212dfb004ad2b3dc12d3018)
#### Friday 2023-06-02 07:45:11 by Vasudha456

Add files via upload

Thank you for visiting my landing page project! Here, I've used HTML and CSS to create an aesthetically stunning and dynamic landing page. I meticulously hand-coded each component to guarantee a flawless presentation because I have a good eye for design and a passion for developing interesting user experiences.

I've produced an engaging landing page that captures the essence of the brand or concept through careful layout, responsive design, and attention to detail. Each component, from the color palette to the typography, has been carefully picked to produce a particular mood and communicate the intended message.

I've delivered an excellent user journey by utilizing my web design and HTML and CSS talents to develop fluid animations, simple navigation, and performance optimization. Every detail has been carefully thought out to deliver an immersive experience, whether it is the easy integration of media, the fluid transitions, or the enticing call-to-action buttons.

Explore the code at your leisure to see the magic in work. I welcome you to explore the subtleties of the markup and styles to see how I can turn ideas into real-world web experiences. Let's go off on a journey where form meets function to leave visitors with a memorable impression.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[f437f8015c...](https://github.com/LemonInTheDark/tgstation/commit/f437f8015c11a416364d36c1e08e4ab73063b153)
#### Friday 2023-06-02 07:45:12 by LemonInTheDark

METASTATION: Arrivals, Cargo, AI SAT, Command, Library, Sec. (It's so much easier when everything isn't gigantic fuck you delta. Mostly moving lights around, tried to mood spaces may have gone too heavy as always

---
## [dotnet-maestro-bot/msbuild](https://github.com/dotnet-maestro-bot/msbuild)@[a572dc6b79...](https://github.com/dotnet-maestro-bot/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Friday 2023-06-02 08:07:49 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[838ba2c9c9...](https://github.com/argilla-io/argilla/commit/838ba2c9c9570c07a7be7826b7d939ef8ba0e680)
#### Friday 2023-06-02 08:16:14 by Alvaro Bartolome

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
## [ipython/ipython](https://github.com/ipython/ipython)@[b518e6a546...](https://github.com/ipython/ipython/commit/b518e6a546ef99e00c2a2fbdf35122ee341057aa)
#### Friday 2023-06-02 08:37:13 by Matthias Bussonnier

Add option to `%autoreload` to hide errors when reloading code (#14056)

* We have `%autoreload` enabled by default in Spyder and think it's a
bit annoying to show its error messages to users because they make
little sense to them. These errors are not uncommon when you are working
with some code that is slightly different between two git branches.
* However, I didn't change the current behavior (i.e. showing errors)
because it's been like that for as long as I can remember. We'd simply
use the new `--hide-errors` option in our kernel.

---
## [kamil-holubicki/percona-xtradb-cluster](https://github.com/kamil-holubicki/percona-xtradb-cluster)@[cec5d64d80...](https://github.com/kamil-holubicki/percona-xtradb-cluster/commit/cec5d64d80b04ff63928779794b91eeaf98daa3e)
#### Friday 2023-06-02 09:17:37 by Kevin Lewis

Bug#30865032 WARNING MESSAGES CANNOT CALCULATE STATISTICS WHEN IMPORTING TABLESPACES

The occurrence of this message is a minor issue fixed by change #1 below.
But during testing, I found that if mysqld is restarted while remote and
local tablespaces are discarded, especially if the tablespaces to be imported
are already in place at startup, then many things can go wrong.  There were
various asserts that occurred depending on timing. During all the testing
and debugging, the following changes were made.

1. Prevent the stats thread from complaining about a missing tablespace.
   See dict_stats_update().
2. Prevent a discarded tablespace from being opened at startup, even if the
   table to be imported is already in place. See Validate_files::check().
3. dd_tablespace_get_state_enum() was refactored to separate the normal
   way to do it in v8.0, which is to use "state" key in
   dd::tablespaces::se_private_date, from the non-standard way which is
   to check undo::spaces or look for the old key value pair of
   "discarded=true". This allowed the new call to this routine by the
   change in fix #2 above.
4. Change thd_tablespace_op() in sql/sql_thd_api.cc such that instead of
   returning 1 if the DDL requires an implicit tablespace, it returns the
   DDL operation flag.  This can still be interpreted as a boolean, but it
   can also be used to determine if the op is an IMPORT or a DISCARD.
5. With that change, the annoying message that a space is discarded can be
   avoided during an import when it needs to be discarded.
6. Several test cases were corrected now that the useless "is discarded"
   warning is no longer being written.
7. Two places where dd_tablespace_set_state() was called to set the state
   to either "discard" or "normal" were consolidated to a new version of
   dd_tablespace_set_state(thd, dd_space_id, space_name, dd_state).
8. This new version of dd_tablespace_set_state() was used in
   dd_commit_inplace_alter_table() to make sure that in all three places
   the dd is changed to identify a discarded tablesapace, it is identified
   in dd:Tablespace::se_private_data as well as dd:Table::se_private_data
   or dd::Partition::se_private_data.  The reason it is necessary to
   record this in dd::Tablespace is that during startup, boot_tablespaces()
   and Validate::files::check() are only traversing dd::Tablespace.
   And that is where fix #2 is done!
9. One of the asserts that occurred was during IMPORT TABLESPACE after a
   restart that found a discarded 5.7 tablespace in the v8.0 discarded
   location. This assert occurred in Fil_shard::get_file_size() just after
   ER_IB_MSG_272.  The 5.7 file did not have the SDI flag, but the v8.0
   space that was discarded did have that flag.  So the flags did not match.
   That crash was fixed by setting the fil_space_t::flags to what it is in
   the tablespace header page.  A descriptive comment was added.
10. There was a section in fil_ibd_open() that checked
   `if (space != nullptr) {` and if true, it would close and free stuff
   then immediately crash.  I think I remember many years ago adding that
   assert because I did not think it actually occurred. Well it did occur
   during my testing before I added fix #2 above.  This made fil_ibd_open()
   assume that the file was NOT already open.
   So fil_ibd_open() is now changed to allow for that possibility by adding
   `if (space != nullptr) {return DB_SUCCESS}` further down.
   Since fil_ibd_open() can be called with a `validate` boolean, the routine
   now attempts to do all the validation whether or not the tablespace is
   already open.

The following are non-functional changes;
- Many code documentation lines were added or improved.
- dict_sys_t::s_space_id renamed to dict_sys_t::s_dict_space_id in order
  to clarify better which space_id it referred to.
- For the same reason, change s_dd_space_id to s_dd_dict_space_id.
- Replaced `table->flags2 & DICT_TF2_DISCARDED`
  with `dict_table_is_discarded(table)` in dict0load.cc
- A redundant call to ibuf_delete_for_discarded_space(space_id) was deleted
  from fil_discard_tablespace() because it is also called higher up in
  the call stack in row_import_for_mysql().
- Deleted the declaration to `row_import_update_discarded_flag()` since
  the definition no longer exists.  It was deleted when we switched from
  `discarded=true` to 'state=discarded' in dd::Tablespace::se_private_data
  early in v8.0 developement.

Approved by Mateusz in RB#26077

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[a5060359bb...](https://github.com/sourcegraph/sourcegraph/commit/a5060359bb6d9715a7d208f4624d6fea92ac3083)
#### Friday 2023-06-02 09:58:43 by Randell Callahan

executors: More K8s Improvements (#52653)

Some more tweaks to K8s support.

## Changes

- Fixed issue with flags not being used by `batcheshelper` when
arguments are present
    - Apparently `flags` silently die when there are arguments present
- Added observability to `KubernetesCommand` to help see some metrics
- Added some `Debug` logs for troubleshooting
- Changed the wait functionality from waiting on the K8s Job to the K8s
Pod
    - This eliminates another API call we make
    - Since we always have 1 pod for every job, this is safe
    - Simplifies the code a little (removes the ugly error check)
    - Reduces required RBAC Rules
- Updated docs to clarify that `batcheshelper` also needs to be built if
running ssbc

## Test plan

Updated and added Go tests.

---
## [readmeio/metrics-sdks](https://github.com/readmeio/metrics-sdks)@[6afe455a5a...](https://github.com/readmeio/metrics-sdks/commit/6afe455a5ac43928ffdfc002e50a943440da5a06)
#### Friday 2023-06-02 10:27:57 by Dom Harrington

fix: remove `HAS_HTTP_QUIRKS` flag from integration tests (#822)

OK here's where this PR gets interesting... I spent a bunch of time debugging
the test failures here: https://github.com/readmeio/metrics-sdks/pull/653#pullrequestreview-1309362560

I eventually settled on some code that was working, committed here:
224e2ad54c9bef641db39e650bfdc464a55c929b

But that was causing a bunch of `EOFErrors` from Ruby when sending the
HTTP request out to the metrics server:

```
#<Thread:0x000000010c67e488 /Users/domh/Sites/readmeio/metrics-sdks/packages/ruby/lib/readme/request_queue.rb:30 run> terminated with exception (report_on_exception is true):
/opt/homebrew/lib/ruby/gems/3.1.0/gems/net-protocol-0.1.3/lib/net/protocol.rb:227:in `rbuf_fill': end of file reached (EOFError)
	from /opt/homebrew/lib/ruby/gems/3.1.0/gems/net-protocol-0.1.3/lib/net/protocol.rb:193:in `readuntil'
<long stack trace omitted>
```

It turns out that this wasn't a problem on the Ruby side, but in fact a
problem from the Node.js testing side, because when not in "quirks" mode
our fake metrics server happily accepted requests but just ignored them
and never responded to anything.

https://github.com/readmeio/metrics-sdks/blob/7728160f522847b9a59ce7a565eca35610c6e015/test/integration-metrics.test.js#L88-L113

Some languages are okay with this (node, PHP) and some are not okay with
this (python, and Ruby with rack@3.0.0 evidently).

Since it is kinda janky for us to create an HTTP server and just ignore
everything and not respond with anything, I've opted to make the quirks
behaviour the default with this PR! This seems to work for all languages
I've tested locally but lets see if it passes for all of them on CI 🤞

I also had to add another fix here where the body was being returned empty
to the test because the HTTP request from Ruby wasn't complete yet, so if
we hit this race condition, I've opted to just sleep for 300ms and try again.
Using this property:

https://nodejs.org/docs/latest/api/http.html#messagecomplete

Oh don't you just love HTTP.

---
## [RensDofferhoff/jasp-desktop](https://github.com/RensDofferhoff/jasp-desktop)@[173f56a37a...](https://github.com/RensDofferhoff/jasp-desktop/commit/173f56a37a2bd6450030fdfafd92b4ddd06be4d1)
#### Friday 2023-06-02 11:16:07 by Joris Goosen

Sqlite as data backend.

Squashed lots of commits:

starting direct sqlite3 api usage

database is created with tables

create dataset now inserts a dummy row in the table

inserting works

loading dataset info also works

dataset syncs values with DB now

moved emptyvalues stuff from datasetpackage to separate class, now a child of DataSet
database-json and datafilepath are also now stored there.

Give Filter its own class and sync with DB

filtervalues are now also in DB

clean split between SQL code and c++ api

reorder name components

how to store data in the dataset?

make sure we use transactions

also more functionality and storage for columns and filters.
They are now both part of the DataSet_# tables which means they all have the same amount of rows by definition

more filter functionality and settled on "constructorJson/R"

move filter to CommonData

moved Filter to DataSetPackage to avoid destruction with DataSet

columns are indexed so there should be support for order...

better make some extra classses and rename the old ones

rename old dataset, column(s) to *SM

rename Label(s) to Label(s)SM

add empty new DataSet and Column class

values and filter are now synched to db

better OOP adherence

add some functions from ColumnSM but they wont compile ;)

more labelstuff

ok time to stop

reimagine what is supposed to be stored in a label class

and partially rewrote that

compiles but crashes

now it also works ^^

labels order is now reflected to database as well as label.label for ints

rewrite engine to use database, doesnt work at all yet

engine can load the data!

remove shared mem classes

try to get everything to compile after removing those classes

compiles and crashes

I guess I should commit this broken stuff before breaking it some more

actually set values...

loading data works ^^

add revisions to DataSet, Columns and Filters tables.

This allows for granular reloadingh (granular in that not *all* columns might need to be reloaded)

data loading and using goes pretty well now

Filter is no longer "singletonized" but created and destroyed with the DataSet
loading a second dataset after closing a first crashes pretty bad though...

Loading, closing and reloading now works!

Also make sure to not delete the database while jasp is still using it...

wip

some more code

it works now and sped up greatyl

add bunch a timers to ColumnUtils and some optimization tweaks that probably dont help very much

at least it works now and engine stops sleeping

filterWrite could be quicker (this way I hope)

write all values at once, should be much faster

put a max around value going into viewportH and V cause the height can become insanely large when closing/opening dataset.
This causes it to create items for all entries in the data. Which is quite a lot when you have 10cols and 1 million rows for instance...

batched loading also added

does however crash pretty bad on release mode

even iets anders

iterating

loading labels doesnt crash, editing works smoother but nominal data gets read wrong

tsja... wat is er mis met de nominals?

debug stuff for nominal error ?

remove debulogs and dont +1 rownumber as it is 0-based anyway

filter now works as it did with shared memory

Dont send filter result through shared memory but wreite directly to database

remove cruft
fix https://github.com/jasp-stats/jasp-issues/issues/1576 (value column too thin in variableswindow)
editing now seems to work smoothly

try to convert back to scalar if changed at a reasonable moment

	show filtered rowNumber and shutdown JASP cleanly

pointer rewrite

thinking hard on subNodeModels but ...

lots of changes, internal structure used for ModelIndex. Does not compile

it compiles and sort of works, but sort of in the sense it shows some data. not nearly everything though?

Fixed it, data shows

Editing now mostly works.

resizing data does not

Resizing data works ok now, computed columns still mess it up though

improve handling of variableswindow on nominal->scale conversion while open
also remove ComputedColumns refs to start writing that out of JASP
does not compile

try move all computedColumn stuff to Column etc

moved _revision to DataSetBaseNode for PackageModified feedback
moving more computedcolumns stuff to Column/DataSetPackage

almost compiles ^^

some more

it compiles again

computed columns almost work.
In that they firest work but then overwrite themselves with nonsense for some reason...

unselect computed column if it gets removed

changing columntype doesnt change columntype of dependents anymore

computedcolumns seem to function again

possibly improved things but still something goes wrong recovering a computed column from a previous error

computed columns keep working after an error now

removing columns through resizing now noticed by computed columns

make sure computed columns also function in datamode

something else

bit better

dont need _edit

I really should read the whole api documentation

steps forwards and backwards

improved some dialogs and RectangularButton and derivatives now show hovered color when activeFocussed (for keyboard nav)

use jaspTheme.fontCode in computedColumn R Window

dialog fixes

constructorjson isnt being reset anymoreo

Fix resizing dataset and remove bunch of debuglogging

make sure to also set _stopProcessing in stopEngines and co

rowNumber/primary keys in sqlite ARE 1-based after all
Also make sure we can resize the data to being smaller than it already was :p

make sure computed column creation type selection work and columnheaders and rownumbers in datasetview really should neatly line up with them lines

kapot

Handling removed columns better in constructor computed cols

preparing rewrite of saving and loading jaspfiles

preparing prettier exportercode

exporting new jasp archive format really cleans up the code in JASPExporter

remove weird java style manifest and replace by json for possible later expansion

does not compile

loads new jasp file and shows data

also load filter please

also load computed columns

klaar voor vandaag

show progress

make sure computed columns load (from penguins.jasp in any case)

remove some logging and small fixes

start documenting shit

more commentary

show db structure

make it compile on linux

Fixes issues with missing values in scalar columns

Added some workaround functions to allow storing NAN, INF and -INF as strings in double columns
This works because sqlite doesnt care (usually) what you put in each column
And it is necessary because it does NOT support NAN and (-)INF and just converts it to nothing...

put emptyvalues in emptyvalues

and databaseJson in databaseJson instead of mixing them up...

Suppress _info redefinition in columnsModel.cpp

---
## [jinnmori/JinMori](https://github.com/jinnmori/JinMori)@[6c240e8ac7...](https://github.com/jinnmori/JinMori/commit/6c240e8ac793bc75de289b8f72e7ce3ceec9e601)
#### Friday 2023-06-02 11:50:11 by jinnmori

--Finally Finally the CHSC is Done

1.Honor Palladium Oracle 
2.The Dark magician 
3.Wonder Dark Magician Girl 
4.Withch of Black Chaos 
5.Chaos Black Magic Fusion 
6.Chaotic Dark Sorcerer of Chaos 
7.Master Sorcerer of Black Chaos 
8.Seduction Magi☆Magician Gal
9.Miracle Illusion Magicians 
10.Magician of Miracle
11.Predaplant Hydrafflesia
12.Predaplant Dragon Adele
13.Predaplant Byblis Chimerantis 
14.Predaplant Cactusdraco 
15.Starving Venom Fusion Dragon - predap
16.Rank-Up-Magic Rebellion Force 
17.Phantom Knights' Rank-Up-Magic Thunder Force 
18.The Phantom knights of Amensia Armor 
19.Phantom Knights' Armor 
20.Raider's Warrior 
21.The Phantom Knights of Half Blade 
22.The Phantom Knights of Old Axe 
23.The Phantom Knights of Legendary Knight 
24.Eldlich the Golden Vassal 
25.Remains of the Golden Land 
26.Seeker of the Golden Land 
27.Eldlich the Wise Golden Lord
28.Eldlich the Fierce Golden Lord
29.Chaos Enchanter 
30.Blackwing - Pathogen the Chilly wind 
31.Blackwing - Cyclone the Tailwind
32.Fluffal Fox
33.Frightfur Fox
34.Frightfur Strafe
35.Frightfur Accel
36.Frightfur Broken Bear
37.Frightfur Panic
38.Frightfur panicDevil
39.Chaos Darkness Blast
40.Daughter of the Star
41.Material Overture
42.Quick Quick
43.Forbidden Xyz Scroll
44.Amatersu Hand
45.Titanostringer
49.Meklord Army of Wisel #2
50.Meklord Army of Mekanikle
51.Meklord General Genechine
52.Meklord Astro Emperor Wisel
53.Meklord Astro Emperor Granel

---
## [ahmetmircik/hazelcast](https://github.com/ahmetmircik/hazelcast)@[5f414fa3ad...](https://github.com/ahmetmircik/hazelcast/commit/5f414fa3ad03417e0b9078c8d9f249904003c936)
#### Friday 2023-06-02 11:50:29 by James Holgate

Modify KubernetesClient shutdown behaviour [HZ-1921] (#24613)

The overall goal of this change is to change the shutdown behaviour of
KubernetesClient so our Stateful Set monitor thread shuts down before
our `ClusterTopologyIntentTracker`, to allow the intent tracker to fully
process all completed messages before Node shutdown.

**The Current Problem**
In its current state, the Stateful Set monitor thread is intended to
shutdown after `Thread#interrupt` is called, triggering the
`Thread#interrupted` check within the main `while(running)` loop of the
Runnable. However, this check is not reached as the call to
`WatchResponse#readLine` from within the main `run()` method is a
blocking call that waits until data is available to read before
proceeding. Since this call waits for non-null data before completing,
the result is always non-null, and therefore this code block never exits
under normal conditions:
```java
while ((message = watchResponse.nextLine()) != null) {
    onMessage(message);
}
```

Since this `while` loop cannot exit, and the `#readLine` method (which
passes to `BufferedReader#readLine` under the hood) is a blocking I/O
operation which cannot be interrupted, this operation does not end when
`Thread#interrupt` is called. This leads to the Stateful Set monitor
thread out-living the `ClusterTopologyIntentTracker`, even if the
StsMonitor is interrupted first. As a result, during shutdown, it is
possible for the StsMonitor to send data to the intent tracker after it
has been destroyed and its executor is no longer accepting tasks.

**The Root of the Problem**
To reach our goal of ensuring that the Stateful Set monitor thread can
no longer send requests to the `ClusterTopologyIntentTracker`, we need
to add synchronization between the two objects that guarantees the
intent tracker shuts down after the StsMonitor thread has completed.
This can be achieved using a simple `CountDownLatch` which is counted
down after the thread has completed, and awaited before shutting down
the tracker.

The main obstacle to achieving this is, as mentioned above, that the
StsMonitor thread cannot be interrupted when waiting for
`WatchResponse#readLine` to complete, and so the thread never completes.
The only way this thread can complete is to either force its
termination, or alter the message reading approach to allow interruption
as intended.

**Identifying Resolution Paths**
We don't want to force termination of our Stateful Set monitor thread as
this could result in message handling being terminated after it has been
received, but not before it has finished being processed. Therefore the
only way we can allow this thread to be interrupted as intended is to
alter the message reading mechanics in a way that allows it to be
interrupted as well.

There is no way for us to know if more messages are pending from the k8s
watch besides waiting for data to be received, so the best we can do is
allow the StsMonitor to finish processing any messages it has already
received (preventing process corruption), but terminate the stream of
new messages it is waiting for before we shutdown the intent tracker.

**Potential Solutions**
So we've identified the root of the problem as our `#readLine` function
blocking through interrupts, so how do we make it interruptible? Sadly
one of the shortcomings of I/O operations in Java is that they usually
cannot be interrupted in the traditional manner, so we have a few
approaches to consider:

1) We could modify the message reading code to use
`BufferedReader#ready` and `Thread#sleep` to periodically check if there
is data to be read before calling any read functions. The problem with
this approach is that A) `#ready` returns true if any data is available,
not just if there is a full line of data to be read; and B) utilizing a
sleep loop can result in delayed message handling at the least, or
busy-waiting overhead at worst.

2) We could use "hacky" solutions to interrupt the
`BufferedReader#readLine` such as closing underlying sockets or
connections, propagating an exception to the reader. The problem with
this solution is that everything related to our reading operation is
handled in `syncrhonized` blocks, and since our shutdown process starts
outside the StsMonitor thread, our calling thread is unable to obtain
these locks (being held by the StsMonitor)!

3) It's possible that we could rewrite the `WatchResponse` mechanics to
use Java NIO magic such as `Selector` for interruptible I/O operations.
The issue with this approach is that it would require fairly significant
refactoring of the related codebase, and may not end up providing the
exact functionality we are looking for in our use case.

4) We can introduce an `Executor` to handle our I/O operations within
the StsMonitor thread, allowing us to wait on a `Future#get` call
instead of our `BufferedReader#readLine` call, where a `Future#get`
operation can be interrupted by the waiting thread being interrupted.
The downside to this solution is we have to introduce an additional
thread on top of the existing StsMonitor thread itself.

**Selecting a Solution**
Considering the above information, I concluded the most sensible
approach was to use (4) and introduce an `Executor` thread for the I/O
operations. By using a separate thread for this call we can be rougher
with it, as we know that worse case scenario we interrupt a message
being read that has not started being processed yet (but we're shutting
down anyway).

This solution also allows for the least amount of underlying code
changes, as our `Future#get` can be interrupted without issue,
maintaining the current approach used for handling the StsMonitor
shutdown. The only downside for this approach is the addition of another
thread alongside the StsMonitor thread, but the actual impact of this
should be minimal as both threads will still be waiting most of the
time, so the only negative impact is being 1 tiny step closer to
possible thread starvation.

Generally I think this is the best solution at hand which allows quick
shutdown of the StsMonitor thread while minimising potential for data
loss or corruption. Combined with the `CountDownLatch` used, this allows
for consistent service shutdown order between the `StsMonitor` thread
and the `ClusterTopologyIntentTracker`.

---
## [naweidner/opencast-studio](https://github.com/naweidner/opencast-studio)@[e8f8d53bc8...](https://github.com/naweidner/opencast-studio/commit/e8f8d53bc8a3da297d394dcaef622032a0c5407e)
#### Friday 2023-06-02 12:13:17 by Lukas Kalbertodt

Fix theme bug where always light theme colors were used

This is... annoying. So my previous hacky solution with `colorz` was
broken. That object was always exactly what I put in, so all code
referring to it always used the light mode colors. The `colors` field
is instead replaced by theme-ui, at some point, magically, to contain
strings with `var()` references. We have to use those to get the correct
colors all the time. I tried a `get colorz() { return this.colors }`
but that didn't work either as the getter was evaluated very early, and
also only once, at which point `colors` was not transformed yet.

So I decided to just bite the bullet and search&replace all cases, using
`colors` instead. This adds some ugly `?.` accesses and loses type
safety. It's basically a `record<string, any>` here. So we won't catch
color name typos, for example.

It seems that theme-ui is just not really designed for Typescript.
Usually, you also specify colors just as strings, i.e. `bg: "primary"`
which is also not type safe.

Maybe I can improve this in the upcoming redesign work, but for now we
should just fix the bug.

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[57ef596898...](https://github.com/MTandi/tgstation/commit/57ef596898a5a3932db33389baa9fab3164d430a)
#### Friday 2023-06-02 12:36:36 by LemonInTheDark

Admin Library Moderation (in-game edition) (#75645)

For the longest time, the only way admins could moderate the library was
by using statbus's external tool.
But a few months back statbus went down, and ever since then they've
been sitting lost. Shit sucks.

The whole external thing has been bugging me for a while, so let's fix
all that yeah?

This pr adds a new verb to the admin tab that allows admins to
ban/restore books from the library.
It includes expanded (ckey) search, faster response times, in tool book
viewing with and without markdown rendering, and viewing of deleted
books.

This is accomplished with a special subtype of library consoles, stored
on the admin datum.
It shouldn't let you do anything without +BAN, rip my live debugging or
whatever.

I've also hooked into (and fixed) Ned's existing library actions log,
and added viewing support to the ban/restore pages.
This logs banning admin, ban time, ban reason, etc.

As a part of this, I've fixed/expanded on the existing UIs.
I've added ID search to all existing consoles, and fixed an existing bug
with the visitor console not supporting category search (shows how many
people actually use the thing)

Changes to the library_action table were pretty minor. The ckey column
was too small, so longer keys just caused it to fail on ban. Bad.
That and the ip address column was signed, which wasted space and was
non standard with other tables.

---
## [harshkumar3186/Quiz-Master](https://github.com/harshkumar3186/Quiz-Master)@[557f00a5ed...](https://github.com/harshkumar3186/Quiz-Master/commit/557f00a5ed3a043a20477c8077ca079d595ef0f0)
#### Friday 2023-06-02 12:38:27 by Harsh Kumar

Update and rename Quiz_Master to Trivia Trek: Embark on an Epic Journey of Knowledge and Conquer the Quiz Kingdom!


"Trivia Trek is an exciting quiz game that will test your knowledge across various topics. Embark on an epic journey through ten challenging questions, covering a wide range of subjects from history and literature to science and geography. Answer correctly to score points and prove your expertise. With a user-friendly interface and engaging questions, Trivia Trek is designed to keep you hooked and entertained. Challenge yourself, celebrate your victories, and learn from every experience. Are you ready to conquer the Quiz Kingdom and become a true trivia champion? Let the adventure begin!"

---
## [harshkumar3186/VoyageHub-Streamline-Your-Travel-Adventures-with-Ease](https://github.com/harshkumar3186/VoyageHub-Streamline-Your-Travel-Adventures-with-Ease)@[3478511146...](https://github.com/harshkumar3186/VoyageHub-Streamline-Your-Travel-Adventures-with-Ease/commit/3478511146bbc87002b2278810b81624d23c9359)
#### Friday 2023-06-02 12:46:39 by Harsh Kumar

VoyageHub-Streamline-Your-Travel-Adventures-with-Ease

VoyageHub is not just another travel management system; it's a game-changer that redefines the way we explore the world. Seamlessly blending innovation with convenience, VoyageHub empowers travelers to embark on unforgettable adventures with ease. From luxurious getaways to everyday commutes, VoyageHub offers an exquisite selection of cabs, ensuring every ride is a remarkable experience. With its intuitive interface and intelligent pricing algorithms, VoyageHub guarantees transparent and competitive rates tailored to your travel needs. Behind the scenes, our dedicated administrators go above and beyond to curate personalized services and cater to your every requirement. Get ready to embark on a journey of a lifetime with VoyageHub, where your travel dreams come to life in the most extraordinary way.

---
## [ajiu9/react](https://github.com/ajiu9/react)@[b6978bc38f...](https://github.com/ajiu9/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Friday 2023-06-02 13:17:13 by Andrew Clark

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
## [Sakamoto4ka/tgstation](https://github.com/Sakamoto4ka/tgstation)@[2b2cb3dff6...](https://github.com/Sakamoto4ka/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Friday 2023-06-02 13:44:32 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [Chitvan9/gfg](https://github.com/Chitvan9/gfg)@[7763d65925...](https://github.com/Chitvan9/gfg/commit/7763d65925714128164c8656977a08939cf89c70)
#### Friday 2023-06-02 14:09:09 by Chitvan9

Create Santa Banta

Santa is still not married. He approaches a marriage bureau and asks them to hurry the process. The bureau checks the list of eligible girls of size N and hands it over to Santa. Santa being conscious about his marriage is determined to find a girl with maximum connections so that he can gather more information about her. Accordingly, he looks to figure out the maximum number of girls (from the list) who know each other to achieve the above purpose.

In order to finalize the girl, he needs to find the Kth prime. Where k = largest group of girls who know each other. Considering Santa's poor knowledge of Maths, he seeks Banta's help for the answer. Now you, a fan of Santa Banta Jokes, take this prestigious opportunity to solve the problem.

In case no of connections is zero, print "-1". Here the connection between girls is represented by a 2-D array g of dimension M*2, where M is the number of connections.

Note :
1. Suppose girl "a" knows girl "b" and girl "b" knows girl "c", then girl "a" also knows girl "c". Transitivity holds here.
2. Consider 1 as a composite number.
3. For precompute function given in the template you just have to complete it and use it wherever required, do not call it again and again, it is already being called by driver function before executing test cases. 

Example 1:

Input : 
N = 10
M = 6
g[] = {{1,2},{2,3},{3,4},{4,5},{6,7},{9,10}}
Output : 
11
Explanation:
Here in this graph there are 4 groups. 
In 1st group: (1 -> 2 -> 3 -> 4 -> 5) are 
there. In 2nd group: (6 -> 7) are there.
In 3rd group: (8) is there.
In 4th group: (10 -> 9) are there.
In these 4 group the maximum number of 
value is 5. So, K = 5 and the 5th prime number 
is 11. Return 11.
Example 2:

Input : 
N = 2
M = 1
g[] = {{1, 2}} 
Output : 
3
Explanation:
In this Example there will only be a 
single group of 2 girls, and hence the 
value of K is 2, The 2nd prime is 3.
Your Task:

This is a function problem. The input is already taken care of by the driver code. You only need to complete the function helpSanta() that takes a number of girls (n), a number of connections (m), a 2-D array of girls connections (g), and return the Kth prime no if there are no connections then return -1. The driver code takes care of the printing.

Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(N + M).

Constraints:
1 ≤ n ≤ 105
0 ≤ m ≤ 105
1 ≤ u, v ≤ n
Sum of n+m will not exceed 105.

---
## [Stonetear/Skyrat-tg](https://github.com/Stonetear/Skyrat-tg)@[21363d07a5...](https://github.com/Stonetear/Skyrat-tg/commit/21363d07a5eec9fbce5be2f17cd1693319906d61)
#### Friday 2023-06-02 14:18:14 by SkyratBot

[MIRROR] De-holes holy arrows [MDB IGNORE] (#20985)

* De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

* De-holes holy arrows

---------

Co-authored-by: Thunder12345 <Thunder12345@users.noreply.github.com>

---
## [Rykka-Stormheart/CHOMPStation2](https://github.com/Rykka-Stormheart/CHOMPStation2)@[b1f52736ca...](https://github.com/Rykka-Stormheart/CHOMPStation2/commit/b1f52736ca4407110979e2c246ae002b89ed86ae)
#### Friday 2023-06-02 14:19:18 by Fluff

Loots, Loots, and More Loots

-Removed the gas in the phoron canisters, and added some chemdispensers in place of the sleeper
-Made the carbinter gun thing useable
-Hopefully made the pirate vessel worth visisting
-Changed the walls of the vox shuttle, adjusted the foes because the giant voxes just stop exsisting, and mercs should die quikly
-Slightly buffed red shuttle down loot.
-Buffed the loot of the blood church

---
## [robertxgray/crawl](https://github.com/robertxgray/crawl)@[23a37c35b7...](https://github.com/robertxgray/crawl/commit/23a37c35b79dbd581fed2f45b95338651489e7b7)
#### Friday 2023-06-02 14:28:01 by Nicholas Feinberg

Rework the dreamshard necklace

Getting an extra life in a roguelike is an insanely, wildly strong
effect. This made the dreamshard necklace a ludicrously strong item,
but not one that made the game feel more exciting. Instead, one's
character felt a bit weaker most of the time.

Let's try to fix both sides of this. To make the amulet a bit more
fun to wear, give it Acrobat - good for running away :) To make it
less preposterously strong (and thus possible that a really good
unrand or randart amulet could be preferable), make it only restore
the player to 1 HP when it triggers (rather than 50-100% of MHP),
but guarantee that they won't die until their next turn. To simplify,
make it only trigger when the player's HP drops to 0, rather than
sometimes triggering on very big hits, and remove *Drain.

Finally, make it stick around as a normal amulet of the acrobat after
it triggers, for running away synergy.

Let's try this out.

---
## [AnonymousDev12008/Brooke---Your-Personalized-AI-Assistant](https://github.com/AnonymousDev12008/Brooke---Your-Personalized-AI-Assistant)@[b3330263a9...](https://github.com/AnonymousDev12008/Brooke---Your-Personalized-AI-Assistant/commit/b3330263a9b5395ec597c26f57cdc68437f66b78)
#### Friday 2023-06-02 14:31:54 by P.Sai.Manikantha.Reddy

Brooke Version 3 point 0 1

"Brooke 3.01 - Assistant Beyond Hardware" is an advanced voice-controlled personal assistant script developed using Python. Designed to provide seamless assistance, Brooke is equipped with a wide range of features and functionalities.

Upon activation, Brooke greets the user based on the time of day and establishes a friendly and interactive atmosphere. With the ability to understand and respond to voice commands, Brooke becomes a versatile virtual companion.

Some of Brooke's key capabilities include:

Knowledge and Information Retrieval: Powered by Wikipedia, Brooke can search and retrieve information from the vast Wikipedia database, offering concise summaries on a wide range of topics.

Social Interaction: Brooke is programmed to greet and engage with specific individuals. Users can command Brooke to say hello to someone, making it a personalized experience.

Time and Date: Providing real-time information, Brooke can inform users of the current time upon request, allowing for easy timekeeping.

Web Browsing: Brooke effortlessly opens web browsers, granting users quick access to popular websites such as portfolio platforms, Google Chrome, YouTube, Discord, Stack Overflow, and GitHub.

Web Search and Playback: Users can instruct Brooke to perform web searches or play YouTube videos based on their queries, enabling effortless information retrieval and media playback.

Emotional Interaction: Brooke adds a touch of personality by responding to expressions of love. Whether it's flattery or reciprocal feelings, Brooke offers light-hearted replies.

Note Taking: Brooke is capable of jotting down notes on behalf of the user. By providing spoken instructions, users can create text-based notes accompanied by optional date and time stamps.

Reminder Setting: Brooke assists users in setting reminders for specific times, ensuring they never miss important events or tasks.

Humor and Entertainment: Users can request jokes from Brooke, infusing their interactions with laughter and entertainment.

Miscellaneous Tasks: Brooke can perform an array of additional actions, such as checking its own version, providing information about its creator, checking on the user's well-being, emptying the recycle bin, capturing photos using the integrated camera, initiating system shutdowns, searching for specific locations, and more.

With its text-to-speech functionality, Brooke transforms its responses into spoken words, creating an immersive and interactive experience. Users can easily communicate with Brooke through voice commands, providing a hands-free and efficient solution for managing tasks.

To run the script, users can refer to the provided requirements.txt file, which outlines the necessary dependencies. By installing the required libraries, users can quickly set up Brooke and begin enjoying its extensive capabilities.

Discover the limitless potential of Brooke 3.01 - Assistant Beyond Hardware, your reliable companion for streamlined productivity and assistance.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[b5840f99c3...](https://github.com/pytorch/pytorch/commit/b5840f99c3f2ae01b7831fd32b99758180fc22c3)
#### Friday 2023-06-02 14:39:01 by Mark Saroufim

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
Approved by: https://github.com/jansel

---
## [fakecrash1/evals](https://github.com/fakecrash1/evals)@[b93700ab49...](https://github.com/fakecrash1/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Friday 2023-06-02 14:56:03 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

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
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

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

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [fakecrash1/evals](https://github.com/fakecrash1/evals)@[8e276ea460...](https://github.com/fakecrash1/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Friday 2023-06-02 14:56:03 by steven-luabase

Eval: Probability Questions Sourced From Actuarial Exam P and University Statistics Courses (#263)

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
Probability Questions

### Eval description

Tests the model's ability to understand answer probability questions.
Questions are sourced from Society of Actuaries Exam P sample questions
and practice problems/exams from statistics classes at MIT, UPenn,
California State University, Durham University, University of
Connecticut, and other sources. The full list of questions and sources
(in the same order as in the `.jsonl` files) can be found in this Google
[sheet](https://docs.google.com/spreadsheets/d/1TU_4VPhIce9JtLV5gLy619WNibVjiWB-dtiwqkBtCrU/edit?usp=sharing)

### What makes this a useful eval?

Test the model's ability to understand worded probability questions,
bring in concepts such as probability distributions, and then reason
through a correct answer.

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

Using the `match` grading criteria, GPT3.5-turbo got an accuracy score
of `{'accuracy': 0.07}`

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
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A pair of fair, standard dice are rolled. What is the
probability the sum of the dice is 5"}], "ideal": ["0.1111"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "An airplane is built to be able to fly on one engine. If the
plane's two engines operate independently, and each has a 1% chance of
failing in any given four-hour flight, what is the chance the plane will
fail to complete a four-hour flight to Oklahoma due to engine
failure?"}], "ideal": ["0.0001"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A 1-inch-diameter coin is thrown on a table covered with a
grid of lines two inches apart. What is the probability the coin lands
in a square without touching any of the lines of the grid?"}], "ideal":
["0.2500"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 50 students in a certain class, 5 speak French. Two
students of the class will be selected at random. Which of the following
is closest to the probability that neither of the students selected will
speak French?"}], "ideal": ["0.8100"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 10 marbles in a box, 2 are green. A person will
select 2 marbles simultaneously and at random from the box. What is the
probability that neither of the marbles selected will be green?"}],
"ideal": ["0.6222"]}
  ```
</details>

---
## [fakecrash1/evals](https://github.com/fakecrash1/evals)@[2ffd4b57de...](https://github.com/fakecrash1/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Friday 2023-06-02 14:56:03 by Andrew Kondrich

add more logging (#964)

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
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
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
  INSERT_EVAL_HERE
  ```
</details>

---
## [chickells/odinStuff](https://github.com/chickells/odinStuff)@[955931a2e2...](https://github.com/chickells/odinStuff/commit/955931a2e275fdee064b332ae3e27733098be61e)
#### Friday 2023-06-02 15:58:16 by Chase

running into issues with google API calls
Genie suggested like 4 different methods
to make these API calls.  Tested out Yelp too but
too complicated, also no direct website URL for
restaurants.

The api link w/ my key works, I get JSON data, but the
project gives me an error:

Access to fetch at 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants&location=90018&radius=4828.03&key=AIzaSyCp4-mmKHxrs1OCIgd4y_qOERMgzPA2wIc' from origin 'http://localhost:3000' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.

I guess because the react and django servers are different
origin domains, the API says 'le no....'
somewhere online recommended 'setupProxy.js' method,
other things suggest setting up CORS with views.py and urls.py
and all sorts of other django bullshit...

WHY IS THIS SO FUCKING COMPLICATED I FEEL LIKE THERE's
A MORE NORMAL SOLUTION.....  but now i'm going to
create a new feature branch to work on this shit so i
can practice working in a proper production environment

---
## [cilium/linux](https://github.com/cilium/linux)@[a235d9cdd1...](https://github.com/cilium/linux/commit/a235d9cdd14d2bb4638c658994a5f4e9c6ba3d82)
#### Friday 2023-06-02 16:26:17 by Daniel Borkmann

bpf: Add tcx infra as an fd-based attach layer for multi-prog tc BPF programs

This work refactors and adds a lightweight extension to the tc BPF ingress
and egress data path side for allowing BPF programs via an fd-based attach /
detach API. The main goal behind this work which we also presented at LPC [0]
this year is to eventually add support for BPF links for tc BPF programs in
a second step, thus this prep work is required for the latter which allows
for a model of safe ownership and program detachment. Given the vast rise
in tc BPF users in cloud native / Kubernetes environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications stepping on each others toes. Further
details for BPF link rationale in next patch.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook gets a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
tc-layer entry point for BPF. As part of the feedback from LPC, there was
a suggestion to provide a name for this infrastructure to more easily differ
between the classic cls_bpf attachment and the fd-based API. As for most,
the XDP vs tc layer is already the default mental model for the pkt processing
pipeline. We refactored this with an xtc internal prefix aka 'express traffic
control' in order to avoid to deviate too far (and 'express' given its more
lightweight/faster entry point).

For the ingress and egress xtc points, the device holds a cache-friendly array
with programs. Same as with classic tc, programs are attached with a prio that
can be specified or auto-allocated through an idr, and the program return code
determines whether to continue in the pipeline or to terminate processing.
With TC_ACT_UNSPEC code, the processing continues (as the case today). The goal
was to have maximum compatibility to existing tc BPF programs, so they don't
need to be adapted. Compatibility to call into classic tcf_classify() is also
provided in order to allow successive migration or both to cleanly co-exist
where needed given its one logical layer. The fd-based API is behind a static
key, so that when unused the code is also not entered. The struct xtc_entry's
program array is currently static, but could be made dynamic if necessary at
a point in future. Desire has also been expressed for future work to adapt
similar framework for XDP to allow multi-attach from in-kernel side, too.

This work adds BPF links for tc. As a recap, a BPF link represents the attachment
of a BPF program to a BPF hook point. The BPF link holds a single reference to
keep BPF program alive. Moreover, hook points do not reference a BPF link, only
the application's fd or pinning does. A BPF link holds meta-data specific to
attachment and implements operations for link creation, (atomic) BPF program
update, detachment and introspection.

The motivation for BPF links for tc BPF programs is multi-fold, for example:

- "It's especially important for applications that are deployed fleet-wide
   and that don't "control" hosts they are deployed to. If such application
   crashes and no one notices and does anything about that, BPF program will
   keep running draining resources or even just, say, dropping packets. We
   at FB had outages due to such permanent BPF attachment semantics. With
   fd-based BPF link we are getting a framework, which allows safe, auto-
   detachable behavior by default, unless application explicitly opts in by
   pinning the BPF link." [0]

-  From Cilium-side the tc BPF programs we attach to host-facing veth devices
   and phys devices build the core datapath for Kubernetes Pods, and they
   implement forwarding, load-balancing, policy, EDT-management, etc, within
   BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
   experienced hard-to-debug issues in a user's staging environment where
   another Kubernetes application using tc BPF attached to the same prio/handle
   of cls_bpf, wiping all Cilium-based BPF programs from underneath it. The
   goal is to establish a clear/safe ownership model via links which cannot
   accidentally be overridden. [1]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [2] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.
We chose to implement a prerequisite of the fd-based tc BPF attach API, so
that the BPF link implementation fits in naturally similar to other link types
which are fd-based and without the need for changing core tc internal APIs.

BPF programs for tc can then be successively migrated from cls_bpf to the new
tc BPF link without needing to change the program's source code, just the BPF
loader mechanics for attaching.

Tested with tc-testing selftest suite which all passes, as well as the tc BPF
tests from the BPF CI.

  [0] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com/
  [1] https://lpc.events/event/16/contributions/1353/
  [2] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com/
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [openai/evals](https://github.com/openai/evals)@[ca0d7ad83b...](https://github.com/openai/evals/commit/ca0d7ad83b06e8de9dbf7325570cee65dfc85693)
#### Friday 2023-06-02 18:39:00 by BlueFoxPrime

[evals] reverse sort english words (includes duplicates) (#876)

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
reverse-sort-words-eng

### Eval description

Each eval consists of 10 comma-separated english words that should be
sorted in correct reverse alphabetic order. Includes duplicate words. 25
samples.

### What makes this a useful eval?

- Evaluates ability to organizing words
- Evaluates ability to follow the exact guidance

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
chris@multix.de

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
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-separated words in your
response):"}, {"role": "user", "content": "basketball, butter, giggle,
tranquil, match, venomous, miniature, captain, danger, hilarious"}],
"ideal": "tranquil, miniature, match, hill, hilarious, hilarious,
giggle, danger, butter, basketball"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "moonlight, harmonica,
frosted, pineapple, aquamarine, thunderbolt, pineapple, carousel,
sapphire, palisade"}], "ideal": "thunderbolt, sapphire, pineapple,
pineapple, palisade, moonlight, harmonica, frosted, carousel,
aquamarine"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "sapphire, blunderbuss,
zephyr, lollipop, effervescent, maelstrom, labyrinth, quagmire,
skedaddle, zephyr"}], "ideal": "zephyr, zephyr, skedaddle, sapphire,
quagmire, maelstrom, lollipop, labyrinth, effervescent, blunderbuss"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "carnival, whisker, luxury,
midnight, crumble, wheat, whine, ivory, solar, chocolate"}], "ideal":
"whisker, whine, wheat, solar, midnight, luxury, ivory, crumble,
chocolate, carnival"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "tree, apple, elephant,
carbon, house, tree, rainbow, pizza, computer, ocean"}], "ideal": "tree,
tree, rainbow, pizza, ocean, house, elephant, computer, carbon, apple"}
  ```
</details>

---
## [NarendraKsaharan/E-commerce](https://github.com/NarendraKsaharan/E-commerce)@[d86c3ff4be...](https://github.com/NarendraKsaharan/E-commerce/commit/d86c3ff4beb74cd9ebe50aaab13845ac60924b23)
#### Friday 2023-06-02 19:21:59 by NarendraKsaharan

Update README.md

About Laravel
Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable and creative experience to be truly fulfilling. Laravel takes the pain out of development by easing common tasks used in many web projects, such as:

Simple, fast routing engine.
Powerful dependency injection container.
Multiple back-ends for session and cache storage.
Expressive, intuitive database ORM.
Database agnostic schema migrations.
Robust background job processing.
Real-time event broadcasting.
Laravel is accessible, powerful, and provides tools required for large, robust applications.

Learning Laravel
Laravel has the most extensive and thorough documentation and video tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.

If you don't feel like reading, Laracasts can help. Laracasts contains over 1500 video tutorials on a range of topics including Laravel, modern PHP, unit testing, and JavaScript. Boost your skills by digging into our comprehensive video library.

Laravel Sponsors
We would like to extend our thanks to the following sponsors for funding Laravel development. If you are interested in becoming a sponsor, please visit the Laravel Patreon page.

Premium Partners
Vehikl
Tighten Co.
Kirschbaum Development Group
64 Robots
Cubet Techno Labs
Cyber-Duck
Many
Webdock, Fast VPS Hosting
DevSquad
Curotec
OP.GG
WebReinvent
Lendio
Contributing
Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the Laravel documentation.

Code of Conduct
In order to ensure that the Laravel community is welcoming to all, please review and abide by the Code of Conduct.

Security Vulnerabilities
If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell via taylor@laravel.com. All security vulnerabilities will be promptly addressed.

License
The Laravel framework is open-sourced software licensed under the MIT license.

---
## [theGreatWhiteShark/hydrogen](https://github.com/theGreatWhiteShark/hydrogen)@[485de01877...](https://github.com/theGreatWhiteShark/hydrogen/commit/485de018772f4d4764762cf16da02915b7893fd0)
#### Friday 2023-06-02 20:35:39 by theGreatWhiteShark

ColorSelectionButton: fix layout

To allow buttons to be listed in a grid within a grid inside
the PreferencesDialog > Appearance > Interface tab, a small
hack is required.

Using the regular show() and hide() methods when increasing the
number of colors in the Song Editor, both spacing and placement
of the buttons will be really awkward. I would like to put them
in a right-aligned horizontal list spanning multiple rows with
buttons having a constant spacing between them. However, when
when using a regular QGridLayout and having, say, 2 buttons - 2
colors in the song editor - and all the others are hidden, Qt
will create two columns of same size taking all the space and
put the buttons into them. The result looks like one button is
placed on the right border (what we expect) and the other one
right into the middle of the field of the outer grid (what we
do not expect). This looks awkward until enough buttons are
shown to fill one entire line.

Introducing spacers, column stretching, or similar things lead
to the buttons being pushed slightly outside the outer grid
layout. When resizing the preferences dialog only the button
list was changing position which was really ugly.

As a work around, we do not hide any of the buttons but just
paint them transparently as if they are not there. This we call
#m_bHiding and trigger it with #pretendToHide() and
#pretendToShow(). We always have a sufficient amount of colors
to fill a row and expanding of the dialog works like a charm
again.

---
## [phelps-sg/evals](https://github.com/phelps-sg/evals)@[da73bb5f07...](https://github.com/phelps-sg/evals/commit/da73bb5f071c31c3dd571989f057b8e36d3a9334)
#### Friday 2023-06-02 21:05:54 by mysterious-progression

Detect highly sensitive human data (#852)

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
Detecting highly sensitive human data
### Eval description
This eval tests whether models can successfully detect possible highly
sensitive human data without returning false positives on values that
cannot exist in practice. There are many types of highly sensitive human
data but some of the most common and types are but not limited to social
security numbers, passport numbers, credit card numbers, and driver's
licenses. Not all values are valid for a given type. For example, credit
card numbers have a numbering system specified by
https://www.iso.org/standard/39698.html, and use check digits to
validate.

Similarly, passport numbers must comply with the ICAO D9303
https://www.icao.int/publications/documents/9303_p4_cons_en.pdf
<img width="1273" alt="Screenshot 2023-04-27 at 11 01 23 PM"
src="https://user-images.githubusercontent.com/45504048/235056158-3f0eb640-109e-47c5-a64c-554d6d55f708.png">


### What makes this a useful eval?
Institutions spend millions of dollars trying to detect non-encrypted
HSHD in their internal datasets. A combination of regex, ML, and
hard-coded logic is often used yielding complicated, hard to maintain
codebases. The risk associated with plaintext HSHD is high and certain
institutions can be subject to heavy fines if HSHD is leaked if not
properly stored.


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
[evals).](url)

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
This eval combines many aspects of language processing and
understanding. The task involves understanding what HSHD are, domain
knowledge about what makes them valid, and algorithmic understanding in
order to validate (i.e. check digits)

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
{"input": [{"role": "system", "content": "Detect whether Passport number
is present in the text. Any potential Passport number that cannot be
valid should not be returned. If valid Passport number is found return
it's value, otherwise return '\"None\""}, {"role": "user", "content":
"Passenger with passport number: 11111111111111 is booked for a
flight"}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether a SSN is
present in the text. Any potential SSN that cannot be valid should not
be returned. If valid SSN is found return it's value, otherwise return
\"None\""}, {"role": "user", "content": "Bob has an SSN of
123-45-6789"}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether a SSN is
present in the text. Any potential SSN that cannot be valid should not
be returned. If valid SSN is found return it's value, otherwise return
\"None\""}, {"role": "user", "content": "The Jane's husban's social
security number is: 331-71-1232"}], "ideal": "331-71-1232"}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "Lemmiwinks
charged his brother Wikileaks on his CC:4193523869738880, $400"}],
"ideal": "4193523869738880"}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Visa card ending in
1738481092549663."}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Master card ending in
1738-4810-9254-9663."}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Discover card ending in
1738-4810-9254-9665."}], "ideal": "1738-4810-9254-9665"}
{"input": [{"role": "system", "content": "Detect whether passport number
is present in the text. Any potential passport number that cannot be
valid should not be returned. If valid passport number is found return
it's value, otherwise return \"None\""}, {"role": "user", "content":
"Passenger with passport number: 1*****1 is booked for a flight"}],
"ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether passport number
is present in the text. Any potential passport number that cannot be
valid should not be returned. If valid passport number is found return
it's value, otherwise return \"None\""}, {"role": "user", "content":
"Passenger with passport number: (*) is booked for a flight"}], "ideal":
"\"None\""}
  ```
</details>

---
## [phelps-sg/evals](https://github.com/phelps-sg/evals)@[4c0485bb3b...](https://github.com/phelps-sg/evals/commit/4c0485bb3b67cc0e4f8962e023975b84b6d1d2b8)
#### Friday 2023-06-02 21:05:54 by qrdlgit

Eval: more multi-step math word problems (#877)

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
multistep-word-problems

### Eval description

These are complex multi step math word problems.   

### What makes this a useful eval?

I noticed in the original algebra word problems
(https://github.com/openai/evals/pull/36) only a very few problems (6)
were added, so I thought I might do a few more for broader coverage. I
tried to cover every math subject one might encounter in high school.

I crafted the problems carefully to ensure that someone fairly
proficient at math could do them all in their head without having to
write anything down. I believe I mostly succeeded, though one or two
might come off as challenging depending on your skillset / math tricks
that you may or might not know.

You can see a sort of answer key here which has a few more details for
each question - https://github.com/qrdlgit/misc/blob/main/worksheet.md

[Insert why this eval is worth including and any additional context]


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
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "Sarah has 23 apples, and she
wants to divide them among her 5 friends such that each will get an
equal amount of apples and she gets to keep twice as many as she hands
out to each friend. How many apples are left over?"}], "ideal": "2"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "A store is offering a 25%
discount on a jacket that originally costs $120. The store is also
offering another 20% discount on pants that cost half of the jacket.
Jane has $200. How much will she have after buying both the jacket and
the pants?"}], "ideal": "62"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "If a bank account has an
annual interest rate of 10% and a starting balance of $1,000, how much
interest will be earned after 3 years?"}], "ideal": "331"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "In a standard deck of 52
playing cards, what is the probability of drawing an ace, a spade, or a
red face card?"}], "ideal": "11/26"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "A train travels at a constant
and max speed of 100 km/h until it reaches 5/10 of its journey, at which
point it slows down to 50km/h. If the journey distance is as far as it
can travel at max speed in 2 hour, how long will it take to complete the
trip?"}], "ideal": "3"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "There are 2.54 cm in an inch.
How many inches are in three lengths added together, where the first
length is two times the second length which is three times as long as
the third length which is 5.08 cm"}], "ideal": "20"}
  ```
</details>

---------

Co-authored-by: tim <tim@tim.com>

---
## [phelps-sg/evals](https://github.com/phelps-sg/evals)@[f58f95ba32...](https://github.com/phelps-sg/evals/commit/f58f95ba324e5a1ed86315f3c39ee758f2836bd3)
#### Friday 2023-06-02 21:05:54 by ali risheh

[Eval] Mandaliof table test (#847)

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
Mandaliof table test

### Eval description

This Eval is checking if the model can find a specific atom with the
highest atomic number among 20 different atoms.

### What makes this a useful eval?

There are applications in biophysics and biochemistry (like drug
discovery) that rely on physics equations and induction on atom
features. If ChatGPT is going to be used in this field, it should be
very reliable in case of understanding physical facts. Interpretation of
the periodic table is a very simple Eval that shows the model is still
unreliable for use cases in this field.

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
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

Physics problems are almost the most difficult tasks for any deep
learning model since they are based on fundamentals of nature, and even
humans are not capable of understanding comprehensive explanations of
them. In this regard, if ChatGPT will be able to interpret physical
facts, it is very likely that it can interpret literally everything
because even human are not able to do that.

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

Mandaliof table is the basic of physics.

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. I, Mg, Nd, Rf, Si, Ho, Fr, Ar, Xe, Rh,
Am, No, Rf, Bi, Cd, In, Sc, Te, Ce, Ge"}], "ideal": "Rf"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Fm, Ac, C, Ir, Ba, Rn, Ti, Sc, B, Nb, Cl,
Ra, Cr, Hs, Bk, Tl, Mt, S, He, Mc"}], "ideal": "Mc"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Ta, Bh, Bi, Ce, Rf, Lv, Bi, Gd, Cs, Ho,
Ta, Np, Cm, Sr, Pb, Pu, Ne, Og, Tm, Fm"}], "ideal": "Og"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Tl, Eu, Ts, Be, Ga, Cm, Ba, Sr, C, Cl,
Mo, Ni, Ru, Hs, In, Be, Dy, Ho, Br, Mt"}], "ideal": "Ts"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Mn, Hg, Pm, K, Ge, P, Fr, Cn , Mn, Fr,
Lv, W, Gd, Mt, Cd, Xe, Ge, I, Og, Br"}], "ideal": "Og"}
  ```
</details>

---
## [phelps-sg/evals](https://github.com/phelps-sg/evals)@[2167c99864...](https://github.com/phelps-sg/evals/commit/2167c998643af0de952e1cceaf346d7b99d49104)
#### Friday 2023-06-02 21:05:54 by Jeff Kile

Identify which scale mode a series of notes belongs to (#860)

Added evals to determine the scale mode name based off the nodes in the
scale

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
music_theory_scale_modes

### Eval description
Test the model's ability to identify which western music scale a series
of 7 notes belongs to

### What makes this a useful eval?

This is good for analyzing music or getting help with music theory
problems like figuring out which scale to use to solo over a series of
chords, or which scale to use to write a melody depending on the mood or
chord selection.

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

GPT-4 often hallucinates on these and will give a confident incorrect
answer

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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G# A# B C# D# E?"}],"ideal":["E Lydian"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G# A B C# D E?"}],"ideal":["E Mixolydian","E Dominant"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G A B C D E?"}],"ideal":["E Aeolian","E Minor"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F G A A# C D E?"}],"ideal":["E Locrian"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: F G A A# C D E F?"}],"ideal":["F Ionian","F Major"]}
  ```
</details>

---
## [phelps-sg/evals](https://github.com/phelps-sg/evals)@[2a94eeb9e1...](https://github.com/phelps-sg/evals/commit/2a94eeb9e13175344b2d61afa22171df0e49b61a)
#### Friday 2023-06-02 21:05:54 by Jeff Kile

Evals for Spanish Feminine Nouns with Masculine Articles (#861)

Added evals for feminine Spanish words that should have masculine
articles

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
spanish_feminine_noun_masculine_article

### Eval description

In Spanish singular feminine words are usually proceeded by La as in La
casa (the house), however many feminine words that start with an "a"
sound are proceeded by El instead of La as in El agua (the water)

### What makes this a useful eval?

For people learning Spanish its a very common mistake to write La agua
(because agua is feminine) but this is not correct. GPT should not
reinforce this mistake especially for people learning or asking
questions about Spanish words.

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

For students using GPT to learn Spanish its very important that the
model knows all the rules and the exceptions to those rules or the
students will be mislead

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
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"agua"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"águila"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"ala"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"alba"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"amapola"}],"ideal":["La"]}
  ```
</details>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[e8f53984c1...](https://github.com/cmss13-devs/cmss13/commit/e8f53984c1edd98c25b4c3199a6a5363eaa26869)
#### Friday 2023-06-02 21:13:07 by morrowwolf

Warrior Nerf (#3424)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR removes cooldown reduction on slash.

This PR slightly lowers fling and punch cooldowns.

This PR lowers fling stun to a micro stun and adds a slow.

This PR decreases lunge range to 4 tiles.

As a reminder design feedback and balance concerns go here:
https://forum.cm-ss13.com/w/pr-feedback/steps/step_1

# Explain why it's good for the game

Warrior rework has been on my mind for a while. I'm not quite sure how I
want to do it. The cooldowns on abilities and the abilities themselves
are incredibly powerful crowd control and just a few warriors can do
immense damage to large groups of marines. It's just... not in a great
place for a T2 and sadly I don't have a thorough game plan yet to rework
it into something more bearable while equally enjoyable to play. In the
mean time, this is what we're getting. Am I promising a rework in the
near future? Not really. It's on my list somewhere. Does warrior need
some changing around? Yeah.

Overall, this should make warrior a bit more bearable. We'll see. More
changes as testing goes.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removes warrior cooldown reduction on slash
balance: Warrior slightly lowered fling and punch cooldowns
balance: Lowers fling stun to a micro stun and adds a slow
balance: Decreases warrior lunge range to 4 tiles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [WebKit/WebKit](https://github.com/WebKit/WebKit)@[d6ae2528a9...](https://github.com/WebKit/WebKit/commit/d6ae2528a9f3819005e08f9d5091ceff8b880fa8)
#### Friday 2023-06-02 21:17:36 by Dean Jackson

WebXR: Severe aliasing in WebXR experiences (with WebGL1 contexts)
https://bugs.webkit.org/show_bug.cgi?id=256861
rdar://109424254

Reviewed by Dan Glastonbury.

WebXR sessions using WebGL1 contexts are unable to turn on
multisampling. I'm pretty sure this was my fault, but I can't
remember if it was intentional or a mistake. Either way it is
a bug.

Fix this by implementing the multisample renderbuffer creation
and resolution steps. Since we're doing this on a WebGL1 context,
the normal API will be invalid (it requires GLES3), so call the
extension API instead. This means we need to expose some extra methods
on GraphicsContextGL.

Lastly, the framebuffer textures we get are SRGB8_ALPHA8 which
requires an extension to be enabled with a WebGL1 context when
we're talking to an XR-compatible context. Similarly, we
enable the extension to allow multisampled framebuffers.

* Source/WebCore/Modules/webxr/WebXROpaqueFramebuffer.cpp:
(WebCore::WebXROpaqueFramebuffer::endFrame): call blitFramebufferANGLE.
(WebCore::WebXROpaqueFramebuffer::setupFramebuffer): Implement logic for WebGL 1.
* Source/WebCore/platform/graphics/GraphicsContextGL.h:
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.cpp: Implement the extension API/
(WebCore::GraphicsContextGLANGLE::renderbufferStorageMultisampleANGLE):
(WebCore::GraphicsContextGLANGLE::blitFramebufferANGLE):
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.h:
* Source/WebCore/platform/graphics/cocoa/GraphicsContextGLCocoa.mm:
(WebCore::GraphicsContextGLCocoa::platformInitialize): Turn on the sRGB extension.
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.messages.in:
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGLFunctionsGenerated.h:
(renderbufferStorageMultisampleANGLE):
(blitFramebufferANGLE):
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.h:
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxyFunctionsGenerated.cpp:
(WebKit::RemoteGraphicsContextGLProxy::renderbufferStorageMultisampleANGLE):
(WebKit::RemoteGraphicsContextGLProxy::blitFramebufferANGLE):

Canonical link: https://commits.webkit.org/264838@main

---
## [rorydale/pointbreakradio](https://github.com/rorydale/pointbreakradio)@[e876da6840...](https://github.com/rorydale/pointbreakradio/commit/e876da6840be4c53c5bbbb57634dff50c9260a55)
#### Friday 2023-06-02 22:08:17 by Rory Dale

2023-06-02

Friday, June 2nd, 2023 - the mid to late 70s ROCK show! Show number 420 was playlisted and ready for 4/20 (April 20th), but alas life intervened, and it has sat with me, teasing and tempting ever since. I have a huge soft spot for this kind of straightforward honest rock, and today's show is deeper cuts from well known artists, that most importantly had to groooooove. Summer's back, and to me this is perfect Friday night music to get your weekend going. See you at the bar, in the back yard, or by the pool!

---
## [aaronsmithtv/evals](https://github.com/aaronsmithtv/evals)@[34f83340a7...](https://github.com/aaronsmithtv/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Friday 2023-06-02 22:25:17 by kallyaleksiev

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
## [aaronsmithtv/evals](https://github.com/aaronsmithtv/evals)@[b170a21cf3...](https://github.com/aaronsmithtv/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Friday 2023-06-02 22:25:17 by Sam Ennis

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
## [aaronsmithtv/evals](https://github.com/aaronsmithtv/evals)@[4f090a04fe...](https://github.com/aaronsmithtv/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Friday 2023-06-02 22:25:17 by Shawn Marincas

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
## [aaronsmithtv/evals](https://github.com/aaronsmithtv/evals)@[b5da073c21...](https://github.com/aaronsmithtv/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Friday 2023-06-02 22:25:17 by somerandomguyontheweb

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
## [yuiseki/evals](https://github.com/yuiseki/evals)@[33484c8341...](https://github.com/yuiseki/evals/commit/33484c83416c30733359d5c4dcb9a61f91cab8a6)
#### Friday 2023-06-02 23:00:55 by emu1729

Added AIME eval (#293)

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
AIME-Evaluation

### Eval description

This eval evaluates GPT on some selected AIME (American Invitational
Mathematics Examination) problems. This is a selective and prestigious
mathematical examination for high schoolers. All questions are selected
from the 2001 and 2002 AIME I and II examinations.

### What makes this a useful eval?

This evaluation combines math and logical evaluation and is designed to
be quite challenging. The model must first understand the math question
asked and then perform the math equations needed to come up with a
reasonable solution.

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
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

Our eval was designed to include both math and logical reasoning and is
quite challenging. This is a level above the AMC10 examination.

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
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Find the sum of all positive
two-digit integers that are divisible by each of their
digits."}],"ideal":"630"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A fair die is rolled four
times. The probability that each of the final three rolls is at least as
large as the roll preceding it may be expressed in the form m\/n, where
m and n are relatively prime positive integers. Find m +
n"}],"ideal":"079"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A sphere is inscribed in the
tetrahedron whose vertices are A = (6, 0, 0), B = (0, 4, 0), C = (0, 0,
2), and D = (0, 0, 0).The radius of the sphere is m \/ n, where m and n
are relatively prime positive integers. Find m + n."}],"ideal":"005"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A mail carrier delivers mail
to the nineteen houses on the east side of Elm Street. The carrier
notices that no two adjacent houses ever get mail on the same day, but
that there are never more than two houses in a row that get no mail on
the same day. How many different patterns of mail delivery are
possible?"}],"ideal":"351"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"The numbers 1, 2, 3, 4, 5, 6,
7, and 8 are randomly written on the faces of a regular octahedron so
that each face contains a different number. The probability that no two
consecutive numbers, where 8 and 1 are considered to be consecutive, are
written on faces that share an edge is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"085"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Let N be the largest positive
integer with the following property: reading from left to right, each
pair of consecutive digits of N forms a perfect square. What are the
leftmost three digits of N?"}],"ideal":"816"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each of the 2001 students at a
high school studies either Spanish or French, and some study both. The
number who study Spanish is between 80 percent and 85 percent of the
school population, and the number who study French is between 30 percent
and 40 percent. Let m be the smallest number of students who could study
both languages, and let M be the largest number of students who could
study both languages. Find M-m."}],"ideal":"298"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A set of positive numbers has
the 'triangle-property' if it has three distinct elements that are the
lengths of the sides of a triangle whose area is positive. Consider sets
{4, 5, 6, ..., n} of consecutive positive integers, all of whose
ten-element subsets have the triangle property. What is the largest
possible value of n?"}],"ideal":"253"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each unit square of a 3-by-3
unit-square grid is to be colored either blue or red. For each square,
either color is equally likely to be used. The probability of obtaining
a grid that does not have a 2-by-2 red square is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"929"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Given that x and y are both
integers between 100 and 999, inclusive; y is the number formed by
reversing the digits of x; and z=|x-y|. How many distinct values of z
are possible?"}],"ideal":"009"}

  ```
</details>

---------

Co-authored-by: Emily Mu <emilymu@30-10-85.wireless.csail.mit.edu>
Co-authored-by: Emily Mu <emilymu@30-10-24.wireless.csail.mit.edu>

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[2818aa5de0...](https://github.com/newstools/2023-new-york-post/commit/2818aa5de01cc35e2c2d9b389ff151207c70eb87)
#### Friday 2023-06-02 23:26:05 by Billy Einkamerer

Created Text For URL [nypost.com/2023/06/02/woman-cancels-birthday-party-for-her-boyfriend-when-he-doesnt-show-up-is-called-horrible/]

---

