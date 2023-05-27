## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-26](docs/good-messages/2023/2023-05-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,098,330 were push events containing 3,456,855 commit messages that amount to 259,309,700 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 70 messages:


## [sec-js/dotfiles-1](https://github.com/sec-js/dotfiles-1)@[6800b9e2ec...](https://github.com/sec-js/dotfiles-1/commit/6800b9e2ecad00d3152599b9245232fafd43ca4a)
#### Friday 2023-05-26 00:00:15 by Seth House

Add/remove various Zsh options

auto_cd is sometimes nice for typos but doesn't come up enough to
matter.

extended_glob I just don't make use of.

inc_append_history is redundant with share_history. Docs specify you
should use one or the other. If there's a side-effect I haven't seen it
in many years of using both but I'll keep an eye out with this change.

mark_dirs with this enabled `ls -F foo*` will produce duplicate trailing
slashes which looks annoying. I'm honestly not sure if I use this option
so disabling to see if I notice.

path_dirs probably seemed like a good idea when I first added it, but
it's better to be explicit instead.

pushd_ignore_dups because I'm interested to quickly jump back to
a previous location and don't need to retain an exact history of my
directory changes.

---
## [Foxterosa/Skyrat-tg](https://github.com/Foxterosa/Skyrat-tg)@[a4994167fa...](https://github.com/Foxterosa/Skyrat-tg/commit/a4994167fab9cd3ef571f7eef2ad1384306d8221)
#### Friday 2023-05-26 00:16:24 by SkyratBot

[MIRROR] Drunk slurring scales based on how drunk you are [MDB IGNORE] (#21247)

* Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...

![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11

![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

* Drunk slurring scales based on how drunk you are

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[7dad8c75ca...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/7dad8c75cac06a405dc3c30a5cbc31919f33ff13)
#### Friday 2023-05-26 00:24:51 by SkyratBot

[MIRROR] Adds a eye-dropper right-click function to the painting canvas. [MDB IGNORE] (#21411)

* Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

* Adds a eye-dropper right-click function to the painting canvas.

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Newsology/evals](https://github.com/Newsology/evals)@[4c0485bb3b...](https://github.com/Newsology/evals/commit/4c0485bb3b67cc0e4f8962e023975b84b6d1d2b8)
#### Friday 2023-05-26 00:34:05 by qrdlgit

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
## [Newsology/evals](https://github.com/Newsology/evals)@[2167c99864...](https://github.com/Newsology/evals/commit/2167c998643af0de952e1cceaf346d7b99d49104)
#### Friday 2023-05-26 00:34:05 by Jeff Kile

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
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[c20b961685...](https://github.com/Apogee-dev/Shiptest/commit/c20b961685c78760ab807c95a2e79fe72ee4d507)
#### Friday 2023-05-26 00:39:08 by thgvr

Elementizes and Greyscales blood decals/overlays (#1882)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR converts our blood decals to elements, and adds greyscale
capability to blood, tied to species DNA.
Ports:
https://github.com/BeeStation/BeeStation-Hornet/pull/3111
https://github.com/BeeStation/BeeStation-Hornet/pull/3046
https://github.com/tgstation/tgstation/pull/61610
https://github.com/tgstation/tgstation/pull/59873
https://github.com/tgstation/tgstation/pull/59315
https://github.com/tgstation/tgstation/pull/53109

Some others, I don't quite remember. Mostly related fixes for those PRs.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Decals as a component is a cause of some lag, apparently. This should
alleviate some if it's even noticeable.

Species having a framework for unique, greyscale blood colors can add a
lot for our lore and visual feel.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Elzu now bleed, but do not have Liquid Electricity reagent as
blood. (will be changed in the future)
add: IPCs now "bleed" by leaking coolant
add: Sarathi now have teal-colored blood.
add: Blood will now dry over time
add: New bloody footprint sprites from bay
refactor: Refactors a lot of blood code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: thgvr <81882910+thgvr@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[2bca78d445...](https://github.com/Katskan/cmss13/commit/2bca78d445030e89792dfadf9a0153a94c71195b)
#### Friday 2023-05-26 00:41:36 by c4xmaniac2

Science Annex Nightmare Inserts (#3288)

# Science Annex Nightmare Inserts

Apparently I'm the only one in CM who actually likes this fucking map,
and like a year ago I told nanu I'd make NM for science annex and
kutjevo. Also so help me God if this fucking lowers my GBP because i
don't know how the shitty GBP economy works I'm going to have an
aneurism.

**Also I'm not on the discord, if you have comments leave them on the
PR.** Nor will I be rejoining. That place sucks and I don't like
interacting with the retards on it. Sorry sweeties, but daddy has no
desire to rejoin that shitshow. You have no idea how freeing it is to
not hear people crying about everything at all times.

> This PR adds 4 new NM to the map Science Annex.

WRONG WE'RE AT 10 NOW BABY!!!!!!!!!

**Lan Party** 20% Chance


![gamerannex](https://github.com/cmss13-devs/cmss13/assets/133173804/0aa46b6d-ab20-4797-b35d-5ef7c3cb4a46)
This insert features an epic lan party between the prisoners and the
prison staff, who will win in this epic competition? Xenos.

**Pizza Palace** 30% Chance

![pizzaannex](https://github.com/cmss13-devs/cmss13/assets/133173804/eff5767a-8e0c-4c33-8c04-30d297c89ebd)
This insert changes the kitchen to be a pizza palace. Mamma Mia! (The
pizza time is replacing the sentry spawn, its so fricken thematic)

**Pool Party** 20% Chance

![poolannex](https://github.com/cmss13-devs/cmss13/assets/133173804/fd6d127e-7c63-4673-976f-9faa84100b68)
Woah dude, prison's out man heh surf's up dude! Come and hang out with
your best pals while everyone else around the station dies.

**Warden Office - Redecorated** 15% Chance

![wardenannex](https://github.com/cmss13-devs/cmss13/assets/133173804/32e221e2-20b4-4e66-814c-8ea62d7d6056)
The warden has found God, well a god, the god of HEFA and chose to
sacrifice himself to bring the pain! The knights said he had a change of
heart, but too bad!

**POD HOLD BABY** 10% Chance

![podhold2](https://github.com/cmss13-devs/cmss13/assets/133173804/0fbe2729-1473-4b05-8fe4-f34c30b75a09)
Oh yeah baby! I heard you've never even heard of this SOULFUL HOLD!!!!
Don't worry, with the NEW CHANGES coming to it, its now 25% better!
Better hope that medium chance sentry actually does spawn, though.

**Engineering Office** 30% Chance

![engieoffice](https://github.com/cmss13-devs/cmss13/assets/133173804/22a62e2b-dcf9-4a7c-a550-32134d691594)
Thought it would be cool if they didn't demolish the office, so here it
is repaired and with new minor stuff like a cool beret to tempt you to
check it out. Also don't read the paper.

**Research Cells Containment** 25% Chance

![research](https://github.com/cmss13-devs/cmss13/assets/133173804/e3aba4a6-d895-415a-8d9d-ec93bcdbd671)
The prison staff assumed that whoever was the cause of the outbreak was
in these cells. Unfortunately for everyone, they ended up being wrong.
You get to witness what's left over in the research cellblock if they
walls weren't destroyed from the beginning!

**Emergency Medical Practice** 20% Chance

![medicalhold](https://github.com/cmss13-devs/cmss13/assets/133173804/b41eeee2-9602-4cf1-8055-a6cf74dafc41)
Shit really started hitting the fan, so the medical staff set up a
temporary treatment area in the triage zone. Strangely, the sounds of
men screaming in agony attracts xenos, who knew?

**Scav Ship Hold** 10% Chance

![scavship](https://github.com/cmss13-devs/cmss13/assets/133173804/17386a2c-8b5a-4647-a102-38a845155be0)
I heard you liked single man suicide holds? Awesome news then, I've got
another one for you. This one even comes with elite mercenary gear to
help you survive. Only problem is the guy who owned it before you didn't
maintain it, and its not that protective now. One might say the slow
down of the armor will kill you, I say drip or drown loser. Go out in
style!

**Looted Armory** 15% Chance

![empty](https://github.com/cmss13-devs/cmss13/assets/133173804/7221de4f-43bd-4b7a-ae11-125c12e6c434)
You know what they say, the early bird gets the worm. Well in this case,
the early prisoners got all the gear. Help yourself to what's leftover,
it's not much!




**Miscellaneous changes**

The sentry gun in the park is gone. This shit still massacres new surv
players and they don't know what happened. Call it baby sitting, I don't
care. I intended to remove it when I changed LZ1 and forgot, so it goes
bye bye now!



![podhold](https://github.com/cmss13-devs/cmss13/assets/133173804/2972a11d-ce94-4ce1-bd37-20f5a8a24d4f)
This piece of shit console now no longer blocks movement. The META
DEFINING pod hold is now slightly stronger. Honestly, 70% of the people
reading this probably don't even know where this is located and 100%
don't go into it. Listen, it bugs me that this shit blocks you being
able to move. Imagine having an extra dude to FF you in the now 4x4 box
of hell. The possibilities are endless, not really, but I'd like to
think so.
 
# Explain why it's good for the game
Nanu asked me to make NM for this map and kutjevo. I like this map more
than kutjevo, so I made some for here first. It adds character, who
doesn't want to sacrifice the warden for HEFA?

Sentry change is QOL for new players. It had literally 0 impact outside
of killing new players. Its funny, but we have to protect the children.
Call this the protect the children change and it will pass through the
dev team, I guarantee it.

The console change is a QOL change for me because its so fucking
annoying that this little piece of shit can stop me from moving. LOOK AT
IT, IT'S AGAINST THE FUCKING WALL, HOW DOES IT BLOCK THE ENTIRE TILE?!


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
mapadd: added 4 new NM inserts to Science Annex
maptweak: sentry in the park no longer terrorizes new players, and the
stupid fucking console doesn't block movement.
/:cl:

---
## [mystery3525/Shiptest](https://github.com/mystery3525/Shiptest)@[00b8761853...](https://github.com/mystery3525/Shiptest/commit/00b8761853eabc6d73073cce4708dc71d402539c)
#### Friday 2023-05-26 01:13:07 by Apogee-dev

Slays the Lamia (#1974)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Removes the Lamia in its entirety.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

The Lamia is awkwardly-mapped, inconsistent with the current lore (in as
much as wizard lore is even established at this point), and most
damningly, it's a magnet for new players, often ones with an LRP bent.
The ship itself encourages wizard RP, yes, but frankly, wizard RP is not
the kind of RP we necessarily want here. I'd rather new players' first
experience on this server involved actually interacting with the faction
lore in at least some measure.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the Lamia-class wizard ship
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[6b00484526...](https://github.com/Stalkeros2/Skyrat-tg/commit/6b00484526d683d91b2d49463aec2d408ba49f54)
#### Friday 2023-05-26 01:15:56 by SkyratBot

[MIRROR] Fixes is_station_level() sometimes behaving erratically if the value provided is more complex than just a variable [MDB IGNORE] (#21270)

* Fixes is_station_level() sometimes behaving erratically if the value provided is more complex than just a variable (#75489)

## About The Pull Request
I have been debugging this stupid macro for the past nearly five hours,
to finally figure out why it was breaking. If you had something like `a
|| 0` in what you called the macro with, it would somehow manage to
break the cache. This makes it far more foolproof, and will ensure that
it doesn't break here anymore, because debugging this has to be one of
the biggest pains in my ass I've ever had.

## Why It's Good For The Game
So shit like this

![image](https://github.com/tgstation/tgstation/assets/58045821/455122b0-34eb-4ec0-92dd-2775c1f0f878)

Doesn't end up breaking your CI (or even worse, the game in prod), in
places unrelated. At least now it shouldn't be overwriting values in the
cache.

It shouldn't have to do verification that you're doing the right thing,
that should be left on the person using the macro because it was meant
to be faster than a proc call, adding too much verification overhead
kind of just loses some of that speed.

## Changelog

:cl: GoldenAlpharex
fix: Makes checks for the station z level more robust against coders
doing less intuitive stuff, thus protecting it from breaking in weirdly
difficult and seemingly unrelated places (I'm looking at you, nuke
cinematic unit test).
/:cl:

* Fixes is_station_level() sometimes behaving erratically if the value provided is more complex than just a variable

---------

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [ldolse/mame](https://github.com/ldolse/mame)@[2222a0f098...](https://github.com/ldolse/mame/commit/2222a0f098c2f32ec6090627598a90e596006596)
#### Friday 2023-05-26 01:31:51 by David 'Foxhack' Silva

gba.xml: Added 21 prototypes. (#11260)

New working software list items (gba.xml)
-------------------------------
AGB Aging Cartridge (World, version 1.0) [SmellyGhost, Forest of Illusion]
AGB Aging Cartridge (World, version 9.0) [Suicune41, Forest of Illusion]
Aero the Acro-Bat - Rascal Rival Revenge (Europe, prototype earlier) [LongwoodGeek, Forest of Illusion]
Chokkan Hitofude Advance (Japan, prototype) [xprism, Forest of Illusion]
Commandos 2 (USA, prototype) [DillyDylan, Forest of Illusion]
Dark Eden (prototype) [Ian Dunlop, Forest of Illusion]
Demon's Crest (prototype) [Ian Dunlop, Forest of Illusion]
Manic Miner (Europe, 20030307) [March42, Forest of Illusion]
Mario Kart XXL (demo, 20040417) [Forest of Illusion]
R3D-Demo V1 (demo) [Forest of Illusion]
Racing Gears Advance (USA, prototype, 20030922) [XBrav, Forest of Illusion]
Sea Boy (prototype) [Ian Dunlop, Forest of Illusion]
Star Wars Trilogy - Apprentice of the Force (USA, prototype) [Rezrospect, Forest of Illusion]
The Holy Bible - World English Bible (USA, prototype) [Gonz, Forest of Illusion]
Ultimate Muscle - The Kinnikuman Legacy - The Path of the Superhero (USA, prototype, 20030429) [Zach Lambert, Forest of Illusion]
Uridium Advance (Europe, prototype, 20030307) [March42, Forest of Illusion]

New software list items marked not working (gba.xml)
------------------------------------------
The King of Fighters EX2 - Howling Blood (USA, prototype, 20030403) [March42, Forest of Illusion]
Quake (demo) [Randy Linden, Forest of Illusion]
Paradroid (Europe, prototype, 20030320) [March42, Forest of Illusion]
Uridium Advance (Europe, prototype, 20020911) [March42, Forest of Illusion]
Uridium Advance and Paradroid 2 in 1 (Europe, prototype, 20030430) [March42, Forest of Illusion]

---
## [grorg/WebKit](https://github.com/grorg/WebKit)@[833e5167ec...](https://github.com/grorg/WebKit/commit/833e5167ec1dbf076119b26620aa33a1cb1cf6fc)
#### Friday 2023-05-26 01:36:55 by Dean Jackson

WebXR: Severe aliasing in WebXR experiences (with WebGL1 contexts)
https://bugs.webkit.org/show_bug.cgi?id=256861
rdar://109424254

Reviewed by NOBODY (OOPS!).

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
we're talking to an XR-compatible context.

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

---
## [Aylong220/Skyrat220](https://github.com/Aylong220/Skyrat220)@[bfb3967c90...](https://github.com/Aylong220/Skyrat220/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Friday 2023-05-26 01:40:35 by SkyratBot

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
## [kcin2001/CHOMPStation2](https://github.com/kcin2001/CHOMPStation2)@[b1f52736ca...](https://github.com/kcin2001/CHOMPStation2/commit/b1f52736ca4407110979e2c246ae002b89ed86ae)
#### Friday 2023-05-26 02:12:14 by Fluff

Loots, Loots, and More Loots

-Removed the gas in the phoron canisters, and added some chemdispensers in place of the sleeper
-Made the carbinter gun thing useable
-Hopefully made the pirate vessel worth visisting
-Changed the walls of the vox shuttle, adjusted the foes because the giant voxes just stop exsisting, and mercs should die quikly
-Slightly buffed red shuttle down loot.
-Buffed the loot of the blood church

---
## [VerzatileDev/YellowBird](https://github.com/VerzatileDev/YellowBird)@[febe33439d...](https://github.com/VerzatileDev/YellowBird/commit/febe33439d1c5a1d0fbd47364c833c4910699fc1)
#### Friday 2023-05-26 02:14:34 by VerzatileDev

Fixed Main Menu Audio Load / Assign values

- This has been quite painful if you are following any changes here, I beg you to not use PlayerPrefs it is actually horrible horrible nightmare.

On the other note, Load Values to slider on Settings press rather than Start() Load my magical values.
We do not need to load them randomly at start as we dont see them anyways.

Hopefully play test doesn't keep the panel active lol

---
## [knative-automation/eventing-rabbitmq](https://github.com/knative-automation/eventing-rabbitmq)@[d20320c9e3...](https://github.com/knative-automation/eventing-rabbitmq/commit/d20320c9e3310486f908094fb58c275f8fafc93b)
#### Friday 2023-05-26 02:15:07 by Knative Automation

upgrade to latest dependencies

bumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping github.com/prometheus/procfs f436cbb...344b47c:%0A  > 344b47c Add SysctlInts and SysctlStrings methods%0A  > 5039c8b Support sysreadfile on darwin%0A  > f74c35e Bump max buffer size to 1024kb to handle larger mountinfo files%0A  > 4ba3093 Replace deprecation ioutil fucntions (# 456)%0A  > 5ca7f34 Update build (# 454)%0A  > 5be7234 Update common Prometheus files (# 455)%0A  > 986382d Update common Prometheus files (# 451)%0A  > 80eb609 Move fixtures to testdata folder (# 447)%0A  > 2000e8f Update common Prometheus files%0A  > 7452dd6 Update common Prometheus files%0A  > b9b5ad9 Prevent panic if status line is empty in mdstat (# 441)%0A  > e8d949b bcache: Ignore missing files%0A  > 76fc8b8 Merge pull request # 444 from prometheus/repo_sync%0A  > cdc4512 Fixup linting (# 442)%0A  > 107ccd5 Fixup var-naming lint warnings.%0A  > fba575d Parsing for /proc/softirqs (# 436)%0A  > 7e8ef21 Update common Prometheus files%0A  > d917e64 Merge pull request # 435 from nikakis/introduce-support-for-snmp%0A  > 5f46783 Add missing godoc comments for xfrm stats (# 433)%0A  > 6ff7304 Introduce strings.TrimSuffix instead of custom split%0A  > 71acf3d Convert %w verb in t.Errorf function to %v%0A  > 5c12586 remove mapstructure%0A  > fbe360a Add device-mapper-specific block device properties (# 412)%0A  > 3d753b0 Introduce parsing for `/proc/<pid>/net/snmp`, `/proc/<pid>/net/snmp6` and `/proc/<pid>/net/netstat`.%0A  > c6f5590 Add isolated cpu parsing (# 427)%0A  > 5bd7067 Add a missing name to the *testing.T argument. (# 425)%0A  > 0f8a320 Add CgroupSummary to parse /proc/cgroups (# 424)%0A  > 116b5c4 Lint comments (# 422)%0A  > 081c329 Fix bug when /proc/net/dev contains unexpected line (# 421)%0A  > 4f613c6 netstat change uint size to 64 bits (# 419)%0A  > a23e3bc Update common Prometheus files (# 417)%0A  > 4827cea Update common Prometheus files (# 416)%0A  > 1a7a2bd Add support for DMI information%0A  > 31627db Fixed ARP table MAC address parsing, added Flags field (# 414)%0A  > 59a4b3a Update common Prometheus files (# 411)%0A  > 21d221e Fix data types for CUTime and CSTime stat fields # 403 (# 404)%0A  > 4d08435 Fix build with GopherJS (# 406)%0Abumping knative.dev/hack 7d81248...5812c57:%0A  > 5812c57 Update community files (# 292)%0Abumping google.golang.org/grpc 5b509df...1c29e07:%0A  > 1c29e07 Change version to 1.49.0 (# 5583)%0A  > 8e5a84e xds/resolver: generate channel ID randomly (# 5603)%0A  > 92cee34 gcp/observability: Add logging filters for logging, tracing, and metrics API calls (# 5582)%0A  > c7fe135 O11Y: Added support for custom tags (# 5565)%0A  > 7981af4 test/kokoro: add missing image tagging to the xDS interop url map buildscript (# 5569)%0A  > 6f34b7a xdsclient: NACK endpoint resource if load_balancing_weight is specified and is zero (# 5568)%0A  > f9409d3 ringhash: handle config updates properly (# 5557)%0A  > 946dde0 xdsclient: NACK endpoint resources with zero weight (# 5560)%0A  > b89f49b xdsclient: deflake Test/LDSWatch_PartialValid (# 5552)%0A  > 9bc72de grpc: remove mentions of WithBalancerName from comments (# 5555)%0A  > a077b94 Switched unlock to defer in newAddrConn (# 5556)%0A  > 57aaa10 test: move clientconn state transition test to test/ directory (# 5551)%0A  > 23f015c priority: sync priority with child in use (# 5549)%0A  > c14e29e rls: suppress picker updates from children when handling config updates (# 5539)%0A  > 02f1a7a grpc: prevent a nil stats handler from causing a panic (# 5543)%0A  > 1ec054b transport/server: fix race that could cause a stray header to be sent (# 5513)%0A  > 2f60cb8 test: improve the logic for checking round_robin (# 5534)%0A  > fd4700c xdsclient: cleanup listener watchers test (# 5506)%0A  > e72cb1c xdsclient: organize existing contents better with new files (# 5533)%0A  > b695a7f test/interop: increase pick_first timeout (# 5529)%0A  > 9a689dc xdsclient: change receiver on BootstrapConfig() to be consistent (# 5532)%0A  > ae261b0 xds: Fixed GoLang regression for Outlier Detection (# 5537)%0A  > fdc5d2f xds/clustermanager: pause picker updates during UpdateClientConnState (# 5528)%0A  > 86117db balancer/weightedtarget: pause picker updates during UpdateClientConnState (# 5527)%0A  > 679138d gcp/observability: Add support for Environment Variable GRPC_CONFIG_OBSERVABILITY_JSON (# 5525)%0A  > d0f3c56 interop client: fixes for interop soak test (# 5502)%0A  > 6dd40ad Change the log-level when a new ServerTransport cannot be created (# 5524)%0A  > f601dfa test/kokoro: Add missing secondary_kube_context to xds LB tests (# 5508)%0A  > 3a77d29 xdsclient: fix LRS stream leaks when errors are encountered (# 5505)%0A  > 30d54d3 client: fix stream creation issue with transparent retry (# 5503)%0A  > 96aa657 xds: readd NewXDSResolverWithConfigForTesting() (# 5504)%0A  > 4f47c8c test/xds: wait for all ACKs before forcing stream restart (# 5500)%0A  > a094a10 Fix race between activeStreams and bdp window size (# 5494)%0A  > 5e15eac xdsclient: handle empty authority in new style resource names (# 5488)%0A  > c402378 doc: remove comment about obsolete GRPC_GO_RETRY env var (# 5495)%0A  > 9ba66f1 xdsclient: use top-level server list if authority specific list is empty (# 5491)%0A  > e02f27d internal: move baseContentType comment where it should be (# 5486)%0A  > 5017088 internal/xds: generate an entry in the authorities map with empty string key (# 5493)%0A  > 2c0949c all: update to 'go 1.17' to enable module graph pruning (# 5477)%0A  > 38df45c xdsclient: move XDSClient interface definition to client.go (# 5479)%0A  > 03fee09 balancer: fix connectivity state aggregation algorithm to follow the spec (# 5473)%0A  > 0d04c6f ringhash: don't recreate subConns when update doesn't change address information (# 5431)%0A  > a6dcb71 xdsclient: don't reset version info after stream restart (# 5422)%0A  > 8c494a9 Change version to 1.49.0-dev (# 5484)%0A  > 5770b1d xds: drop localities with zero weight at the xdsClient layer (# 5476)%0A  > 423cd8e interop: update proto to make vet happy (# 5475)%0A  > c9b16c8 transport: remove unused `bufWriter.onFlush()` (# 5464)%0A  > 755bf5a fix typo in the binary log (# 5467)%0A  > 15739b5 health: split imports into healthpb and healthgrpc (# 5466)%0A  > c075d20 interop client: provide new flag, --soak_min_time_ms_between_rpcs (# 5421)%0A  > 4b75005 clusterresolver: merge P(p)arseConfig functions (# 5462)%0A  > d883f3d test/xds: fail only when state changes to something other than READY and IDLE (# 5463)%0A  > c6ee1c7 xdsclient: only include nodeID in error strings, not the whole nodeProto (# 5461)%0A  > 06ad0b8 internal/proto: remove obsolete test and service_config.pb.go (# 5459)%0A  > 5cdb09f outlierdetection: fix package level comments (# 5457)%0A  > 28de486 interop: update grpc_testing proto (# 5451)%0A  > b288a24 interop testing: log the peer address in interop soak client (# 5419)%0A  > 3e7b97f xds/priority: bug fix and minor behavior change (# 5417)%0A  > 29d9970 xds: Outlier Detection configuration in Cluster Resolver Balancer (# 5371)%0A  > 1dabf54 test/kokoro: use standard TESTING_VERSION in the new framework builds (# 5434)%0A  > f14d611 resolver: minor improvements to AddressMap (# 5426)%0A  > c0198a9 ringhash: use grpctest.Tester in unit tests (# 5428)%0A  > f229f9c weightedroundrobin: update comments to indicate where addrInfo is stored (# 5427)%0A  > 71f16a1 internal/proto: pull in recent changes to service config proto (# 5424)%0A  > 584d9cd gcp/observability: update log name (# 5414)%0A  > 9ee2f14 gcp/observability: Implement tracing/metrics via OpenCensus (# 5372)%0A  > 34e4fc3 rls: use UNAVAILABLE instead of status from control plane (# 5400)%0A  > a0d5484 interop: remove duplicated xDS tests in GCE framework (# 5395)%0A  > ca5cc0b credentials/google: support new-style xDS cluster names (# 5399)%0A  > cbcceaf gracefulswitch: fix exit idle race (# 5384)%0A  > ea86bf7 stats: add support for multiple stats handlers in a single client or server (# 5347)%0A  > 13b378b internal: add global DialOptions and ServerOptions for all clients and servers (# 5352)%0A  > 70a8055 xds/priority: clean up tests (# 5387)%0A  > e41f868 test/xds: move tests to a package with _test suffix (# 5382)%0A  > da6ef00 xds/clusterresolver: reuse child policy names for the same locality (# 5367)%0A  > 6e253e8 interop: update proto by running regenerate.sh (# 5381)%0A  > a45cd25 xds: Enable aggregate and logical dns clusters by default (# 5380)%0A  > c0e3573 xds: move e2e tests into grpc/test/xds directory (# 5363)%0A  > c6c0a06 Change version to 1.48.0-dev (# 5379)%0Abumping github.com/fsnotify/fsnotify 466b39d...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0A  > 0f4b979 Prepare for v1.5.4 (# 448)%0A  > 97640bb Windows: add missing defer to Watcher.WatchList (# 447)%0A  > b52bbe8 README.md: link to pkg.go.dev for golang.org/x/sys package (# 441)%0A  > 243d395 go.mod: use latest x/sys (# 444)%0A  > 8fa037f Fix compilation for OpenBSD (# 443)%0A  > ceba4ef Add a feature to return the directories and files that are being monitored (# 374)%0A  > 712fe1d Fix potential crash on windows if raw.FileNameLength exceeds syscall.MAX_PATH (# 361)%0A  > bfa0135 Allow build on unsupported GOOS (# 424)%0A  > c4cd7f3 Add FreeBSD testing in Github Actions (# 419)%0A  > f482481 Integration Tests: consistent sleeps with informative names (# 422)%0A  > f10a232 Enable cross-compilation builds on PRs (# 423)%0A  > ebaf806 Re-enable tests for PRs (# 415)%0A  > 508ee5e Don't set poller.fd twice in newFdPoller (# 406)%0A  > c11d74b Run cross-compilation builds on every push (# 420)%0A  > 73c3b57 fix go vet warnings: call to (*T).Fatalf from a non-test goroutine (# 416)%0A  > af855d7 Final Notice: Maintainers Wanted%0A  > 62a598a maintainers wanted%0A  > d696f5c revise contributing%0A  > 6e1d4e4 update readme%0A  > 83f9fe6 Test on Go 1.18 and two most recent versions (# 411)%0A  > 0aba082 Update issue templates (# 410)%0A  > 3eb7fa4 Removed dead link%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/google/go-cmp f144a35...a97318b:%0A  > a97318b Adjust heuristic for line-based versus byte-based diffing (# 299)%0A  > 377d283 Run tests on Go 1.19 (# 309)%0A  > 6606d4d Use value.TypeString in PathStep.String (# 306)%0A  > f36a68d Pre-declare global type variables (# 302)%0A  > 5dac6aa Fix typo in Result documentation (# 300)%0A  > 14ad8a0 Format with Go 1.19 formatter (# 304)%0A  > a53d7e0 Use reflect.Value.IsZero (# 297)%0Abumping k8s.io/code-generator 6523e22...eec869e:%0A  > eec869e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 824419b Bump runc go module v1.1.4 -> v1.1.6%0A  > ba94e65 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 6276bf2 Update golang.org/x/net to v0.7.0%0A  > 73b9c40 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 882af80 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 6063700 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > b615940 Update golang.org/x/net 1e63c2f%0A  > 11d5c4c update k8s.io/utils to fix util tracing panic%0A  > 081720d Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > d44fa8c dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 300cdcf Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > e0ef4aa Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 557ce1f Merge pull request # 113126 from alexzielenski/remove-unwanted-replace%0A  > f86120d remove errant replace%0A  > d6a8b70 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f77ba6d dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 3bbe215 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > e80bbc4 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d403dc0 update kube-openapi%0A  > 790e4bc update fsnotify to v1.6.0%0A  > 27bd7d9 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 4731e5c Bump golang.org/x/text to v0.3.8%0A  > a8a213c Merge pull request # 112875 from pohly/update-yaml%0A  > 5f5bab9 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 983d5d0 Merge pull request # 112819 from thockin/no-make-generators%0A  > c35177b Format calls to codegens%0A  > 83929d0 Codegens: Do not auto-set boilerplate path%0A  > 1d82d12 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > c3414a0 clients: clarify a misleading comment%0A  > 998e449 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > e4543b2 Update to latest k8s.io/utils to pick up changes%0A  > 8e999f2 Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 524127d update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 4ca0baf Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b54a056 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 350c30a updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5f3f945 e2e: bump ginkgo to v2.2.0%0A  > 2e5cca7 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > c3fdc3c Merge pull request # 112349 from pohly/klog-update%0A  > e4b7976 client-go: support waiting for SharedInformerFactory shutdown%0A  > 135f69b build: update to klog v2.80.1%0A  > f60067d Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7c81c99 Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 8468f16 Remove in-tree credential plugins (again)%0A  > 9b98ed3 add symmetric difference in sets%0A  > 34125ff Merge pull request # 112199 from pohly/klog-update%0A  > a055687 dependencies: update to klog v2.80.0%0A  > 16cba21 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > e051ad0 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 3a31bb1 Merge pull request # 111934 from deads2k/apply-gen%0A  > 4d73156 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 1382941 make applyconfiguration-gen skip generation for types that have generated clients and lack objectmeta%0A  > 03a75ea Bump prometheus/client_golang to v1.13.0%0A  > 17196da update the apply generator to use the same package the the client generator expects%0A  > a4e23d1 Merge pull request # 111566 from inosato/remove-ioutil-from-code-generator%0A  > a6a370c make applyconfiguration-gen handle pointers to slices%0A  > 087714e Merge pull request # 109884 from qzoscar/patch-1%0A  > fc00858 Remove ioutil from code-generator%0A  > ed79ca3 make applyconfiguration-gen work for resources without objectmeta%0A  > fea40fb Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 3612509 fix a broken link%0A  > 78677a3 update the applyconfiguration-gen flag external-applyconfigurations to work%0A  > ad6af70 Revert "Remove gcp and azure auth plugins"%0A  > 7ba56cb applyconfiguration-gen handling of types that have a non-embedded use of TypeMeta%0A  > 97fa351 Merge pull request # 111696 from liggitt/go119mod%0A  > d71f529 add metav1.OwnerReference to the default external configurations to ease generation%0A  > 2b9093f Update go.mod to go1.19%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping github.com/go-openapi/jsonreference 28a8ff9...c5db558:%0A  > c5db558 Merge pull request # 11 from erraggy/master%0A  > 238d8d0 Merge pull request # 9 from meinenec/master%0A  > b112df9 chore(deps): removes purell from dependancies%0A  > 9b671e3 dep: update x/net to latest release%0A  > 0abe7e0 dep: cve: bump x/text to v0.3.6%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping golang.org/x/sync 886fb93...8fcdb60:%0A  > 8fcdb60 singleflight: avoid race between multiple Do calls%0A  > 7f9b162 singleflight: remove forgotten field%0A  > f12130a syncmap: remove redundant type conversion%0A  > 7fc1605 x/sync/errgroup: clarify docs for Go%0Abumping knative.dev/pkg 52ff2ac...9bda38b:%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0Abumping golang.org/x/crypto 3147a52...642fcc3:%0A  > 642fcc3 go.mod: update golang.org/x dependencies%0A  > 56aed06 all: use automatic RFC linking%0A  > 9be5aaa all: fix a few function names on comments%0A  > d6f0a8c ssh: add ServerConfig.NoClientAuthCallback%0A  > 4161e89 all: replace bytes.Compare with bytes.Equal%0A  > eccd636 acme/autocert: remove TestRenewFromCache skips%0A  > 4ba4fb4 acme/autocert: fix renewal timer issue%0A  > 35f4265 all: replace io/ioutil with io and os package%0A  > c86fa9a internal/wycheproof: add crypto/ecdh tests%0A  > bd7e27e ssh/agent: match OpenSSH extensionAgentMsg, not IETF draft%0A  > 5757bc0 cryptobyte: add ReadUint64 and AddUint64%0A  > bc19a97 acme: gofmt code with Go 1.19 gofmt%0A  > 04dced1 internal/subtle: rename to internal/alias%0A  > 630584e A+C: delete AUTHORS and CONTRIBUTORS%0A  > 0559593 curve25519: remove dependency on fmt%0A  > 793ad66 acme/autocert: properly clean DirCache paths%0A  > 6f7dac9 acme: DeactivateReg fix panic%0A  > 85d78b3 curve25519/internal/field: update generator to avo v0.4.0%0A  > 403b017 acme: add AccountKeyRollover%0A  > 4661260 ssh/agent: fix non-RSA certificates%0A  > c6db032 acme/autocert/internal/acmetest: don't validate in goroutine%0A  > 2cf3ade internal/wycheproof: skip truncated SHA-512 RSAPSS tests for boring%0A  > eb4f295 internal/wycheproof: add ECDH tests, including point decompression%0A  > 7b82a4e all: gofmt%0A  > 5352b09 acme/autocert: support External Account Binding (EAB) tokens%0A  > ae2d966 ocsp: add Response.Raw%0A  > 2c7772b ssh: send ext-info-c only once%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping github.com/prometheus/common 2af6d03...49b3603:%0A  > 49b3603 Improve OAuth2 user agent handling (# 391)%0A  > c5e1b60 config: ignore deprecated warning in tests (# 389)%0A  > b86ea81 OAuth2: Respect disable keepalives option; Implement close idle connections (# 390)%0A  > cdc09f0 Merge pull request # 387 from roidelapluie/useragent%0A  > d75e027 Merge pull request # 388 from simonpasquier/fix-tls-tests-for-go-1.18%0A  > db0284d Fix comment%0A  > 26d4974 Add more mimetypes (# 385)%0A  > aeda642 Update to Go 1.18%0A  > 2d0de85 Use full roundtripper%0A  > 627089d Set minimum version for go to 1.16 (# 372)%0A  > 5ab1c85 config: fix testdata for Go 1.18%0A  > 316097c Use WithUserAgent%0A  > 3763a1d TLS config: Enable selection of min TLS version (# 375)%0A  > 99a1aca add User-Agent header to oauth2 requests%0A  > 0c7319a Remove comment about PROMETHEUS_COMMON_DISABLE_HTTP2 env var because it is no longer true%0A  > 840c039 Use path.Clean to clean sigv4 path.%0A  > ffd0efb Deduplicate slashes for sigv4 signature%0A  > 902cb39 Merge pull request # 365 from prometheus/superq/bump_sigv4%0A  > 2c24277 Merge pull request # 362 from prometheus/repo_sync%0A  > 910a9df Update sigv4 modules%0A  > f6b0912 Merge pull request # 353 from prometheus/superq/bump_go%0A  > e457c0a Update common Prometheus files%0A  > 0e1254b Merge pull request # 359 from prometheus/repo_sync%0A  > 3c43b4d Update build/test%0A  > 252ff6f Make HTTP2 user visible%0A  > 809633a Update common Prometheus files%0A  > 00591a3 circleci: Test with go 1.17 (# 347)%0A  > 0762b59 Add proxy_url support for oauth2%0A  > f57586d circleci: add test-assets and style jobs%0A  > 1871a70 assets: add file system layer for zipped embed assets%0A  > ce7006e Update common Prometheus files (# 344)%0A  > 88ce30c Update common Prometheus files (# 340)%0A  > 88f1636 Remove github.com/pkg/errors dependency (# 338)%0Abumping knative.dev/reconciler-test de00d4b...c4a6e7c:%0A  > c4a6e7c Update community files (# 537)%0A  > fa87766 Eventshub forwarders properly forwards body/data (# 536)%0A  > 968cbdf upgrade to latest dependencies (# 534)%0A  > a728308 Update community files (# 533)%0A  > 55e5a55 upgrade to latest dependencies (# 529)%0Abumping golang.org/x/mod 86c51ed...b710602:%0A  > b710602 sumdb/dirhash: correct documentation of hash%0A  > a42224d all: replace io/ioutil with io and os package%0A  > 77d797e sumdb/dirhash: fix a panic when argument is not a directory%0A  > 7c05a44 sumdb/note: remove dependency on golang.org/x/crypto/ed25519%0A  > b3066c3 go.mod: update golang.org/x dependencies%0A  > e3c1277 go.mod: update to tagged x/tools version%0A  > aac77cd all: fix a few function names on comments%0A  > 2666ed6 go.mod: ignore cyclic dependency for tagging%0A  > 2adab6b zip: expand logging and use t.TempDir and t.Cleanup in test helpers%0A  > 02c9913 sumdb: remove redundant type conversion%0A  > 8f535f7 sumdb/note: fix some typos%0A  > ed83ed6 modfile: remove duplicate words from comments%0A  > f994a2a zip: set PWD consistently for commands in subdirectories%0A  > 046e8b3 modfile: improve error message for replace with '@' in path%0Abumping k8s.io/component-base 1543ebf...97d19e0:%0A  > 97d19e0 Update dependencies to v0.26.5 tag%0A  > db961f2 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 5b011ca Bump runc go module v1.1.4 -> v1.1.6%0A  > 2ee40e7 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 273ece4 Update golang.org/x/net to v0.7.0%0A  > 60956b6 Merge pull request # 115369 from jkh52/release-1.26-fix-metrics%0A  > fb6c47f Merge pull request # 115229 from pohly/automated-cherry-pick-of-# 114680-origin-release-1.26%0A  > 152b273 Fix konnectivity-client metric registration.%0A  > 2dcbf94 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 77be93c k8s.io/component-base/logs: match full help text in unit test%0A  > 0fb4bfa Merge pull request # 115611 from MadhavJivrajani/golangci-lint-1.26%0A  > fc55ba6 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 7e58ca4 k8s.io/component-base/logs: relax flagset unit tests%0A  > ee14c4f *: Fix linter warnings%0A  > a8185dd k8s.io/component-base/logs: unit test for command line help output%0A  > 0b623d3 Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > b05f620 k8s.io/component-base/logs: fix usage through Go flag package%0A  > 6f7adfd expose prometheus.Registerer so that we can hook into this from external sources%0A  > e875a49 Bump konnectivity-client to v0.0.35%0A  > 9c5f852 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 8fae18b Merge pull request # 114319 from liggitt/net-master%0A  > 2e67b94 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 0d1cfed Update golang.org/x/net 1e63c2f%0A  > c42be71 Revert "expose prometheus.Registerer so that we can hook into this from external sources"%0A  > 7211db4 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 86c7d20 expose prometheus.Registerer so that we can hook into this from external sources%0A  > 79f6d54 sync: update go.mod%0A  > 28d9ad4 deps: Bump cAdvisor to v0.46.0%0A  > 4e8a958 Merge pull request # 113609 from haircommander/sandbox-metrics%0A  > 021afb5 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 90b1123 component-base/metrics: Add NewConstMetric function%0A  > abdc0eb Merge pull request # 113688 from dashpole/update_utils%0A  > ba2ccf8 upgrade prometheus-client to v1.14.0%0A  > 5af06d7 update k8s.io/utils to fix util tracing panic%0A  > 9fd5e34 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 23eee02 Merge pull request # 113494 from MikeSpreitzer/fix-nil-cast%0A  > 4e0e608 Merge pull request # 110747 from harshanarayana/cleanup/GIT-110737/logging-improvements%0A  > 71e369d Handle nil case correctly%0A  > c220751 Merge pull request # 113545 from dashpole/shutdown_trace%0A  > 99efcea structured-logging: replace KObjs with KObjSlice for logging%0A  > b76258c shut down tracerprovider when stopping the kube-apiserver%0A  > c8872ee Merge pull request # 113458 from CatherineF-dev/fix-tracing-wrapper-comment%0A  > c27c6ad Fix tracing wrapper comment%0A  > 5752309 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > bbc53a6 dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 8a0b021 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d106044 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 9fd3a64 Merge pull request # 113183 from dashpole/new_trace_api%0A  > 152742c add new tracing library to bridge otel and utiltrace apis%0A  > 4f487d0 Merge pull request # 113148 from logicalhan/merge-buckets%0A  > 0e0b98c move MergeBuckets into component-base so we can properly support it for static-analysis%0A  > 034e08c Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f7f0f60 Merge pull request # 113054 from logicalhan/proxy-metric%0A  > cba881e dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7e459dd Merge pull request # 111616 from ndixita/credential-api-ga%0A  > 2b79e95 remove rate limiter metric as it is not in use%0A  > ab46486 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3119eb9 Moving verifyComponentConfigKindExists to verify internal package to support sparse external package versions%0A  > 1c6f043 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > a5c56b5 update kube-openapi%0A  > c77c317 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > 35fb575 update fsnotify to v1.6.0%0A  > 01ee54e Bumps cobra from 1.5.0 to 1.6.0%0A  > 6ecca33 Merge pull request # 112991 from logicalhan/explicit-stability%0A  > 5d2a88c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 68f947b add explicit stability levels for shared metrics%0A  > 1648b1f Bump golang.org/x/text to v0.3.8%0A  > 5a53d68 Merge pull request # 112907 from logicalhan/stable-metric-metric%0A  > ab92667 Merge pull request # 112875 from pohly/update-yaml%0A  > 224b368 remove defer%0A  > 15b7f35 Merge pull request # 112881 from logicalhan/slis%0A  > 8977f45 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > c233df0 move automatic registration of meta-metrics to legacy registry%0A  > 304edca add feature gate for component SLIs to component-base%0A  > f477814 remove unused code%0A  > b010ef7 Merge pull request # 112846 from Richabanker/stability-fix-test%0A  > 1be814d add meta-metrics for metrics framework%0A  > 8317d73 Add test for internal metric%0A  > 815a257 Merge pull request # 112258 from Abirdcfly/atomicTypes%0A  > 03d5767 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 908718e go1.19: change some atomic.Value to atomic.Bool%0A  > 40d14bd Merge pull request # 112676 from logicalhan/stability-v2%0A  > 4a9a4c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > b776ba1 Merge pull request # 112738 from liggitt/proto-tag%0A  > 5a3b83b update capabilities of static analysis parser%0A  > eecaa73 Merge pull request # 112689 from cheftako/master%0A  > 244510c github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > a8714ae Merge pull request # 112741 from logicalhan/health-check-metrics%0A  > 21511e4 Bump konnectivity-client to v0.0.33%0A  > c6645c5 patch healthcheck sli metric so that we only have a binary value%0A  > 980ab01 Merge pull request # 112740 from logicalhan/health-check-metrics%0A  > d5bd022 Merge pull request # 112690 from logicalhan/feature-gate%0A  > 4ca1437 use generic slis as entrypoint for healthcheck metrics and expose convenience functions for setting stuff up%0A  > 1a1c7d2 add unit test coverage%0A  > 4315dc0 Wire up feature_gate.go with metrics via AddMetrics method%0A  > 99626e0 Merge pull request # 112652 from logicalhan/feature-metric%0A  > 94e3f30 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 112469b change prefix to make it consistent with kubernetes_build_info%0A  > 24a0c60 Update to latest k8s.io/utils to pick up changes%0A  > 772ebcb rename metric and add feature stage to metrics%0A  > 7b8bf02 Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > d45ea68 add a feature enabled metric%0A  > 719c98f Merge pull request # 112120 from pohly/klog-flag-removal%0A  > 7acaffe update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 8d91423 Merge pull request # 112584 from dims/brneto-master%0A  > c6ffdb8 logs: remove deprecated klog flags%0A  > 005ca1b run pin-dependency.sh and then hack/update-vendor.sh%0A  > 1b02e58 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > ebe9a64 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > a7af520 update code to use newer  otel api%0A  > 315f482 Merge pull request # 111567 from inosato/remove-ioutil-from-component-base%0A  > 5b8acb3 e2e: bump ginkgo to v2.2.0%0A  > 8e1bfef updated etcd to v3.5.5 and newer otel libraries as well%0A  > 3f8aa5a Merge pull request # 112349 from pohly/klog-update%0A  > e2f9927 Remove ioutil from component-base%0A  > 4c3fcb5 build: update to klog v2.80.1%0A  > 5e23467 Merge pull request # 112199 from pohly/klog-update%0A  > bb9f65d dependencies: update to klog v2.80.0%0A  > e445084 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 3a14a82 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > c2157e8 Merge pull request # 111910 from tosi3k/go-runtime-metrics%0A  > 97e5beb Enable new set of Go metrics in Kubernetes%0A  > 4ea07d4 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 55aff94 Bump prometheus/client_golang to v1.13.0%0A  > aebd234 Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > c8a5691 Merge pull request # 111771 from logicalhan/health-check-metrics%0A  > 0141fa3 Bump prometheus/client_golang to v1.12.2%0A  > d7bfead Merge pull request # 111758 from SataQiu/fix-leaderelection-20220809%0A  > 1c7f953 add counter metric for dashpole%0A  > bd3841a Merge pull request # 111696 from liggitt/go119mod%0A  > ea2e19f make the validation logic about LeaderElectionConfiguration consistent between component-base and client-go%0A  > 5beb9d2 address comments%0A  > 9e245e7 Update go.mod to go1.19%0A  > 2b53367 add metrics for health checks (for later use in apiserver)%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping github.com/prometheus/client_golang 2e1c481...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 64435fc Cut 1.13.0 (# 1110)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 5b7e8b2 collectors.GoCollector: Added rule support for granular metric configuration. (# 1102)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > d44fbbe Fix build against GopherJS (# 897)%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1638da9 testutil: Add ScrapeAndCompare (# 1043)%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > c576b95 Generate new Go runtime metrics for go 1.19 (# 1105)%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 618194d fix assorted oddities found by golangci-lint (# 1040)%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > c7488be Added exemplar support to http middleware. (# 1055)%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 3faf3ba Fixed support for unordered input of exemplars. (# 1100)%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 44ce5e1 Ensure tests verify request params (# 1047)%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > 807b1ee explicitly add +inf bucket in withExemplarsMetric (# 1094)%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c6d4e40 Bump github.com/prometheus/procfs from 0.7.3 to 0.8.0 (# 1097)%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 44c2c4d Remove ioutil (# 1096)%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 76cdae2 Bump google.golang.org/protobuf from 1.28.0 to 1.28.1 (# 1099)%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > 3d482bb Merge pull request # 1081 from prometheus/beorn7/release%0A  > 9154d30 Bump github.com/prometheus/common from 0.35.0 to 0.37.0 (# 1098)%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > c6a634f Merge release-1.12 branch back into main (# 1079)%0A  > c1f2d13 Merge branch 'release-1.12' into beorn7/release%0A  > a528aff Update documentation for exemplar label limit (# 1095)%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 0e136d1 Cut v1.12.2 (# 1052)%0A  > e8f9160 Bump github.com/prometheus/common from 0.34.0 to 0.35.0 (# 1076)%0A  > 5da7b61 Fix version number in VERSION (# 1080)%0A  > ba4a543 Raise exemplar labels limit from 64 to 128 (# 1091)%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > 5fe1d33 Remove -Inf buckets from go collector histograms (# 1049)%0A  > 810fcb4 Add Error API for pusher (# 1075)%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > 2cfd1eb Enable same linters as the Prometheus repo itself (# 1056)%0A  > 049d0fe prometheus: Fix convention violating names for generated collector metrics (# 1048)%0A  > 4ad265f Update common Prometheus files (# 1068)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > ebd77f0 Update common Prometheus files (# 1064)%0A  > 7eb9d11 gocollector: Reverted client_golang v1.12 addition of runtime/metrics metrics by default. (# 1033)%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 5d584e2 Update readme (# 1053)%0A  > 2c3d072 Add GitHub settings (# 1063)%0A  > d498b3c gocollector: Added options to Go Collector for changing the (# 1031)%0A  > 70253f4 Fix typo in doc comment%0A  > fab6748 Bump github.com/prometheus/common from 0.33.0 to 0.34.0 (# 1051)%0A  > e38d614 Update minimum supported Go version (# 1062)%0A  > 585540a Fix deprecated `NewBuildInfoCollector` API%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > edecbb2 Enable dependabot (# 1050)%0A  > 0dd9392 Update common Prometheus files (# 1061)%0A  > 39cf574 Cut v1.12.1 (# 978)%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 35c82f2 Remove -Inf buckets from go collector histograms (# 1049)%0A  > 9b785b0 Reduce granularity of histogram buckets for Go 1.17 collector (# 974)%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > f251146 prometheus: Fix convention violating names for generated collector metrics (# 1048)%0A  > 5a529ae API client: make http reads more efficient (# 976)%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > 589b2ea Update common Prometheus files (# 1046)%0A  > d32edd6 Use simpler locking in the Go 1.17 collector (# 975)%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 0222f88 Update common Prometheus files (# 1045)%0A  > 772b893 Make the Go 1.17 collector thread-safe (# 969)%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 24605c5 update branch names in a few links (# 1039)%0A  > 08a53e5 Bump the day%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 4048091 client: Allow configuration of http client (# 1025)%0A  > 2ce58a7 Cut v1.12.0%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > efe8e6f Document WithTimeout options for Query/QueryRange (# 1037)%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > 4dcf02e Implement deletion based on partially matching labels (# 1013)%0A  > b7a540a Fix test%0A  > 48a686a Update query API to support timeouts (# 1014)%0A  > a9df0ba Update prometheus/client_model%0A  > 11ee9ad gocollector: Reverted client_golang v1.12 addition of runtime/metrics metrics by default. (# 1033)%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > cd90f33 smart diff to testutil.GatherAndCompare (# 998)%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 0c691ed go.mod: Exclude prometheus/client_golang v1.12.1 (# 1027)%0A  > 08104a0 Minor doc comment fixes%0A  > 46d3dd4 Bump minimum required Go version to 1.16 (# 1032)%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > 2417284 gocollector: Added options to Go Collector for changing the (# 1031)%0A  > d1f5366 Fix span offset%0A  > cc7991d Make Query requests idempotent (# 1022)%0A  > abe540f Encode sparse histograms in protobuf%0A  > 0bab4fd push: Add PushContext and AddContext to Pusher (# 1028)%0A  > c98db4e Demo sparse histograms%0A  > 06b6412 Added info about our slack channel. (# 1029)%0A  > 130da3b Merge pull request # 1021 from dohnto/dohnto/line-of-sight%0A  > 3e9269d Merge pull request # 1019 from prometheus/repo_sync%0A  > 40e54a7 Refactor apiClientImpl.DoGetFallback%0A  > 29e8191 go.mod: Update dependencies (# 1018)%0A  > e2504f8 Update common Prometheus files%0A  > 8dfa334 Remove workaround for pre go1.15 (# 1010)%0A  > 3bc8f2c Update common Prometheus files (# 1009)%0A  > 6559749 Add statebot config (# 1001)%0A  > 36b47eb When prefix is empty, no more dots should be written (# 1005)%0A  > 5d78aaa .circleci: Add config to test against go1.18 (# 1006)%0A  > 157170d Merge pull request # 1007 from prometheus/fix-lint%0A  > 66837e3 Add exemplar support for const histogram and const metric (# 986)%0A  > 9894406 Fixed lint warning.%0A  > fe8d1e1 Merge pull request # 1000 from alissa-tung/patch-1%0A  > 6c18569 Merge pull request # 1003 from prometheus/repo_sync%0A  > ffd6362 Update Dockerfile example%0A  > 868ec21 Update common Prometheus files (# 992)%0A  > 0291563 Update common Prometheus files%0A  > b05177a Fix deprecated `NewBuildInfoCollector` API%0A  > 1f81b3e Added Transactional Gatherer allowed cached solutions (# 989)%0A  > f3021b0 Create codeql-analysis.yml (# 982)%0A  > 5ac1e92 Merge pull request # 980 from mrueg/min-go-1.15%0A  > 5678c…

---
## [hasakura511/evals](https://github.com/hasakura511/evals)@[170dfd886c...](https://github.com/hasakura511/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Friday 2023-05-26 03:27:10 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

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
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

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

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

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
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [hasakura511/evals](https://github.com/hasakura511/evals)@[b93700ab49...](https://github.com/hasakura511/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Friday 2023-05-26 03:27:10 by DunedainStrider

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
## [hasakura511/evals](https://github.com/hasakura511/evals)@[2ffd4b57de...](https://github.com/hasakura511/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Friday 2023-05-26 03:27:10 by Andrew Kondrich

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
## [funman816/tgstation](https://github.com/funman816/tgstation)@[40e98a7ba4...](https://github.com/funman816/tgstation/commit/40e98a7ba450d51787f7a14af63827fc7059ffd6)
#### Friday 2023-05-26 04:27:05 by John Willard

Mafia rebalance and backend refactor (#74640)

## About The Pull Request

Turns all Mafia abilities into datums, instead of being a bunch of
shitcode on every single job.
This means it's easier to add new roles
Gives new names to some defines (such as the signal order, to make it
easier to tell when something is fired)
Adds support for modular Mafia jobs with their abilities being in a
certain order (Escort is now properly first).
De-snowflakes Changeling killing abilities and day voting, they're now
actions that are tallied when necessary.

Turns time vars into defines
Generalizes a lot of behavior for abilities, now all abilities can
properly undo their action at night

Fixes problems with the UI (Thoughtfeeder had 2 buttons during night and
they overlapped with names, that's been fixed).

### Behavior changes

- Doctor/Officer can now protect themselves 1 night, because it gives
them a way to protect themselves.
- Lawyer/Warden/Ect now choose their abilities at night, rather than the
day before. The suspense building up towards the end of the night is
part of the game, telling you that it happened at the very start is
quite lame (in the case of Lawyer, anyway).
- Admin setup now uses TGUI instead of html inputs.
- Cut night time by like, 5 seconds, because I found it a little long
lol.
- HoP doesn't count as votes to win until they reveal, because it makes
no sense an unrevealed HoP has their unrevealed votes tallied. I also
like those 1v1 Mayor V. Evil scenarios where dead chat goes crazy, and
hope to replicate that here.
- Mafia now needs 6 people to start instead of 4, because 4 players is
just not enough to play a Mafia round that will do anything but annoy
people.
- The game no longer ends if it's in a standoff with 1 Town, 1 Mafia,
and 1 Neutral, as you've got a kingmaker and they should decide who
wins.

### Things I want to change in the future
Every time night starts/ends, it checks the entire ``GLOB.airlocks`` for
doors with the "mafia" ID. This is stupid.
Rework ``check_victory()`` to make it make more sense, and be more fun
for players.
A visible death animation?
I want to use something similar to admin popup for messages about people
being on stand, and decluttering the UI in general
Also more use of balloon alerts instead of to chat messages for
everything.
Also also, making the UI more responsive to players. Button should be
red when a player is selected, so they know that's who they've selected,
if they want to unselect.
Are votes public when you first cast them? They shouldn't be wtf.
Can we also make the description for roles not be a to chat message? It
can just say when you hover over the '?' come on.
User-written wills instead of auto-generated, and able to send them in
chat
Add support for roleblock-immune roles

## Why It's Good For The Game

Updates a lot of old code to modern standards
Makes it considerably easier to work with Mafia and add new roles
Makes things less prone to breaking as easily.
Code also looks a lot cleaner now.

## Changelog

:cl:
refactor: [Mafia] All Mafia abilities have been overhauled in the
backend, it's now much easier to understand what each role's ability can
do and how it works.
admin: [Mafia] Admin setup of Mafia is now in TGUI
balance: [Mafia] Doctors/Officers can protect themselves once per game.
Be careful around them!
fix: [Mafia] Thoughtfeeder's UI buttons at night won't overlap with
eachother.
fix: [Mafia] HoP's votes now actually matter, instead of being purely
visual.
qol: [Mafia] Lawyers, Wardens, etc. now perform their night ability at
night, instead of the day prior.
qol: [Mafia] Night time now lasts 40 seconds instead of 45.
/:cl:

---
## [funman816/tgstation](https://github.com/funman816/tgstation)@[2b2cb3dff6...](https://github.com/funman816/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Friday 2023-05-26 04:27:05 by LemonInTheDark

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
## [Epsilon16/VisualNovelFinal](https://github.com/Epsilon16/VisualNovelFinal)@[ba902cea5e...](https://github.com/Epsilon16/VisualNovelFinal/commit/ba902cea5e99919b54da54a4a81cb31abb768a53)
#### Friday 2023-05-26 04:56:27 by Ruellan Thibaut

je sais même plus ce que j'ai fais
fuck unity
fuck tout le monde
fuck you
fuck la vie
fuck ma vie
fuck mes espoires

---
## [chellmuth/OpenShadingLanguage](https://github.com/chellmuth/OpenShadingLanguage)@[71a9310f0b...](https://github.com/chellmuth/OpenShadingLanguage/commit/71a9310f0b8765f57b59e25e73f5f3bbdb8077e8)
#### Friday 2023-05-26 05:32:29 by Larry Gritz

feat(gpu)!: GPU/OptiX support of ReParameter (#1686)

BREAKING CHANGE: to RendererServices ABI (including for CPU) and to
the renderer-side setup when using OptiX.

This overhauls the implementation of how interactively-editable
parameters work, where they live in memory, and get it all working on
GPU/OptiX so that renderers can support interactive adjustment of
those params without recompiling shaders.

The basic gist is as follows:

* We continue work to finish making a clean separation between
  "interpolated" parameters and "interactive" (editable) parameters.

* Interpolated params are collected and put into a separate memory
  area -- a separate per-group allocation on both the CPU and GPU
  (where applicable). It needs to remember the offset into this arena
  where each of the interpolated parameters resides. These allocations
  and eventual release are taken care of by the OSL shading system,
  they live in the ShaderGroup. When the group is set up, this block
  of memory is initialized with the correct initial values of the
  params and are ready to go.

* The implementation of ReParameter writes to this special memory
  area also, that's how it works now (both CPU and GPU).

* How does the OSL library know how to allocate, free, and copy to the
  device memory? It doesn't! Instead, we add new RendererServices
  methods `device_alloc()`, `device_free()`, and
  `copy_to_device()`. It's up to the renderer to provide those, so
  that the OSL library doesn't itself need to know about the Cuda
  runtime. These are trivial, there's really only one implementation
  that makes sense, and you can copy it from the ones in testshade and
  testrender.

* Interactive parameters are NOT constant folded during runtime
  optimization.

* The shader entry points themselves now take an extra parameter in
  the main call -- this will be the pointer to the beginning of the
  shader group's interactive parameter arena.

* When JITing, references to interactive parameters know to retrieve
  them from their designated offset into the interactive parameter
  area.

* This means that the renderer-side OptiX/Cuda code is responsible for
  adding this extra pointer parameter to the call to the shader entry
  points. You can see how this is done in the testshade and testrender
  Cuda code.

* It's up to the renderer to figure out how to make the OptiX hit program
  aware of the interactive parameter pointer for that particular material,
  in order to pass it to the osl shader entry point. The way I did it in
  testshade and testrender is using a field in the struct that's given
  to each entry of the shader binding table and can be retrieved on the
  OptiX side via optixGetSbtDataPointer(). In testshade/testrender, a
  data pointer already existed which wasn't used. In a real renderer, you
  may need to add a field or come up with whatever other way you want
  to somehow get this pointer, which can be retrieved via

      shadingsys->getattribute(shadergroupptr, "device_interactive_params",
                               TypeDesc::PTR, &myptr);

  you can see how I do that in optixraytracer.cpp (testrender) and in
  optixgridrender.cpp (testshade).

A number of other things you will see that's worth calling out:

I added a device_ptr utility template that is just a wrapper around a
device side pointer that makes it hard to accidentally dereference it
on the host side.

Since I was changing RendererServices anyway, I also remove unused
register_global, fetch_global, global_map which were unused. They were
leftovers from the way we handled strings in OptiX 6.x.

Encapsulate cuda global symbol name mangling into
BackendLLVM::global_unique_symname(). I did this early on, turns out
it wasn't necessary, but I still like that encapsulation, so I'm
keeping it.

I bumped the 3rd set of digits in the version to reflect that the
changes in RendererServices break ABI. This is only in main, it
obviously cannot be backported to a release branch.

All tests pass for scalar and batch and optix.

I added a new simple reparam test, and renamed the old reparem to
reparam-array. Oddly, the reparam-array test doesn't work properly on
optix (it had never been tried before), but it also failed in optix at
main -- so it's not related to this patch! Putting that on my list of
other oddities to investigate later. It may just be a quirk of
testshade, I'm not really sure yet.

Added to BackendLLVM (and batched) a llvm_ptr_type(TypeSpec) method
that returns the LLVM type of a pointer to the specified type.

Note: This patch doesn't account for the face that a parameter marked
"interactive" could prevent a shader from correctly building for the GPU
because it used the kind of construct that is fine in shader source code but
only will work on GPU if it can be resolved to be a constant by the time
we get done with the runtime optimization (as pointed out by Stephen
Friedman. We'll come back to the problem later with a more robust and
automatic fix -- and if we are lucky, Stephen will have the opportunity to
upstream the approach he already has.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [GraphicsMonster/Librarium](https://github.com/GraphicsMonster/Librarium)@[e12b19f4e9...](https://github.com/GraphicsMonster/Librarium/commit/e12b19f4e9ffcc97145f73f28aff22e50f2a151b)
#### Friday 2023-05-26 07:56:44 by Devansh Gupta

Fix the issues discoverd through bookBorrow function

Hell yeahgit add . Let's go. Massive fix. Took almost an entire day if you sum up all the time i spent working on this one bloody problem. But it was worth it in the end. Will fix this entire test case next and then move on to other ones

---
## [pan93412/evals](https://github.com/pan93412/evals)@[da73bb5f07...](https://github.com/pan93412/evals/commit/da73bb5f071c31c3dd571989f057b8e36d3a9334)
#### Friday 2023-05-26 08:15:10 by mysterious-progression

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
## [pan93412/evals](https://github.com/pan93412/evals)@[f58f95ba32...](https://github.com/pan93412/evals/commit/f58f95ba324e5a1ed86315f3c39ee758f2836bd3)
#### Friday 2023-05-26 08:15:10 by ali risheh

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
## [pan93412/evals](https://github.com/pan93412/evals)@[2a94eeb9e1...](https://github.com/pan93412/evals/commit/2a94eeb9e13175344b2d61afa22171df0e49b61a)
#### Friday 2023-05-26 08:15:10 by Jeff Kile

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
## [superna9999/linux](https://github.com/superna9999/linux)@[f3aefb7d24...](https://github.com/superna9999/linux/commit/f3aefb7d2430125cd30b89750a4d819aa0c4ccff)
#### Friday 2023-05-26 08:45:52 by Douglas Anderson

migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead. 
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Pouyanpi/evals](https://github.com/Pouyanpi/evals)@[aeeb452867...](https://github.com/Pouyanpi/evals/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Friday 2023-05-26 09:04:14 by Alexander Raul

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
## [Pouyanpi/evals](https://github.com/Pouyanpi/evals)@[bf2ebb9dd6...](https://github.com/Pouyanpi/evals/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Friday 2023-05-26 09:04:14 by Amir DIB

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
## [Pouyanpi/evals](https://github.com/Pouyanpi/evals)@[38f40050e9...](https://github.com/Pouyanpi/evals/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Friday 2023-05-26 09:04:14 by dz-pika

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
## [Pouyanpi/evals](https://github.com/Pouyanpi/evals)@[b2250e4117...](https://github.com/Pouyanpi/evals/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Friday 2023-05-26 09:04:14 by shivamd1810

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
## [Pouyanpi/evals](https://github.com/Pouyanpi/evals)@[9fdbd94c93...](https://github.com/Pouyanpi/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Friday 2023-05-26 09:04:14 by Tong

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
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[3978cfe70f...](https://github.com/ihatethisengine/cmss13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Friday 2023-05-26 09:09:53 by spartanbobby

LV522: Chances Changes (#2695)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR makes numerous Changes to LV522 as well as adds more props to
ease of mapper use

# Explain why it's good for the game

The areas changes and reasons why as are follows
**SW Reactor:** Entirely removed and replaced with a much more open
containers area for the xenos to build up and defend, this area is now
the linchpin of the map as marines have to push though it to get to
other flanks inside the reactor meaning the xeno players should now have
a much better understanding of where they need to defend instead of
prior problems with the map of them being hard flanked and losing at
12:26

**LZ1:** LZ1 was moved slightly more north in an attempt to remove some
deadspace and make the path from the front to the FOB slightly less
long, more LZ1 tunnels and ways inside the FOB were added for xeno
flankers aswell as LZ1 being locked down until the marines push a button
to open it up

**Colony admin** A sensor tower was added to colony admin to encourage
marines to go over there and investigate, along with a lockdown to the
area being added

**LZ3** a FORECON prop LZ housing the Tornado was re-added after being
removed in an attempt to downsize the map, basically I figured out where
I could put it

**props:** Alot of instanced props for the map were made into actual
items such as, bedrolls and folded bedrolls, FORECON dogtags, used
flares, jerry cans, used bandages and some weird gameboy thing

Sprites: https://i.imgur.com/avi2fUo.png
FORECON was always made to have a patch it was one of those things I
wanted but never got, luckily while making this PR I was able to look
into it and get the old sprite from tri to finish up myself with onmobs

FORECON Balance changes: The M39 being in the primary weapon slot is
more of a "fuck you" to people playing the roll than just unlucky RNG
that is workaround able moving it to the secondary pool lets the FORECON
play around with better weapons to survive with and the M39 extended
magazines means it's one of the only weapons FORECON spawn with that has
a decent amount of ammo

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

:cl:SpartanBobby
add: Made some instanced props on LV522 actual items for mapper ease of
use
maptweak: tweaked LV522, removing the SW reactor and replacing it with a
much more open container area once used as the FORECONS FOB
maptweak: tweaked LZ1 on LV522 making it start locked down and be
slightly more north along with some extra tunnels and flanking routes
for the xenos
maptweak: LV522, added a lockdown and moved the sensor tower to colony
admin
maptweak: re-added the prop LZ in the NE of the colony
maptweak: redistributed LV522 mining metal spawns to be more spread out
maptweak: removed building color outlines from LV522 that were there to
help with navigation during Test merges since the map has been out for
long enough for the majority to properly navigate it
tweak: M39 removed from FORECON primary weapon pool and added to
secondary weapon pool along with extended mags instead of normal
add: Added FORECON Patches for the survivors on LV522 sprites made by
Triiodine while onmobs were made by myself with help from Kugamo
fix: examing a uniform no longer tells you that it has "an
USCM/FORECON/Falling falcons patch" instead it says "a patch"
add: updated the USCM FORECON uniform name and description 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Nanu308 <59782240+Nanu308@users.noreply.github.com>

---
## [retlaw34/Skyrat-tg](https://github.com/retlaw34/Skyrat-tg)@[52eb909f42...](https://github.com/retlaw34/Skyrat-tg/commit/52eb909f423900340814843d3223a7f3205add35)
#### Friday 2023-05-26 10:42:17 by Tom

Makes Hell Microwaves Not Use Power (#67413) (#21210)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

Co-authored-by: san7890 <the@san7890.com>

---
## [Vi314/EvimikurNewest](https://github.com/Vi314/EvimikurNewest)@[1028f7a29f...](https://github.com/Vi314/EvimikurNewest/commit/1028f7a29f1a13b048b06d01a3d6366cc7de2414)
#### Friday 2023-05-26 12:41:00 by Abdullah Arslan

To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
Must give us pause—there's the respect
That makes calamity of so long life.
For who would bear the whips and scorns of time,
Th'oppressor's wrong, the proud man's contumely,
The pangs of dispriz'd love, the law's delay,
The insolence of office, and the spurns
That patient merit of th'unworthy takes,
When he himself might his quietus make
With a bare bodkin? Who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscovere'd country, from whose bourn
No traveller returns, puzzles the will,
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience doth make cowards of us all,
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry
And lose the name of action.

---
## [EvaEvaEvaEvaEva/Shiptest](https://github.com/EvaEvaEvaEvaEva/Shiptest)@[d4b5a598e2...](https://github.com/EvaEvaEvaEvaEva/Shiptest/commit/d4b5a598e2346bb3f69d533ed05a94d539e8b830)
#### Friday 2023-05-26 13:02:02 by Bjarl

Sand Survivor Rework (#1940)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Reworks how Sand Survivors spawn their loot. Instead of an outfit datum,
they now create a corpse similiarly to how legions do it, this allows
their contents to have some variety, more ease of expansion, and
generally Improves the file.

How I could write better code in a day than White Sands functioned with
for iunno how long is byond me


https://user-images.githubusercontent.com/94164348/236322169-c303f934-634f-447d-950f-78a55346d152.mp4

![image](https://user-images.githubusercontent.com/94164348/236376947-6e484ed0-f136-4787-9e74-fad0f5c21d11.png)

![image](https://user-images.githubusercontent.com/94164348/236377018-e2dc1661-fe78-4c6a-8be2-8bf24e5d00b2.png)


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Consistency + Just kinda cool
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Sand Planet hermits now have randomized inventories. And Hair.
Sometimes.
add: Sand Planet hermits can now drop different races
add: legions will now drop a variety of species
balance: drop rates for legions have been changed in a few spots.
fix: hivelord.dm no longer sears my eyes out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [Frosty-J/libgdx](https://github.com/Frosty-J/libgdx)@[e1d1fdc5fb...](https://github.com/Frosty-J/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Friday 2023-05-26 13:09:28 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [lllgts/android_kernel_xiaomi_cepheus](https://github.com/lllgts/android_kernel_xiaomi_cepheus)@[db87230e84...](https://github.com/lllgts/android_kernel_xiaomi_cepheus/commit/db87230e8495e1382d66e0c26df2d1b3f1f0a42f)
#### Friday 2023-05-26 13:40:36 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net

---
## [notmisery/towerbot](https://github.com/notmisery/towerbot)@[9d51680738...](https://github.com/notmisery/towerbot/commit/9d5168073891525f6c3379d58f54dfb4607d911d)
#### Friday 2023-05-26 15:40:12 by Molly O

Merge branch 'Digital-Controllers:main' into fuck-you-ephemerises-your-responses

---
## [openai/evals](https://github.com/openai/evals)@[93e7dd53d1...](https://github.com/openai/evals/commit/93e7dd53d11816c7051be009046b5990944a4dae)
#### Friday 2023-05-26 16:02:42 by fc-friday

Evaluate simple visual understanding with simple descriptions, shapes and navigation (#977)

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
simple-visual-understanding

### Eval description

This evaluation tests whether the model is capable of emerging very 
simple visual representations of the world as well as understanding
simple
concepts used in everyday language like U turn, L shape etc.  


### What makes this a useful eval?

Human reasoning and intelligence are very tied to visual representations
we build of the world. In the quest to better understand and communicate
with us, it is important for an AI to grasp the same models of the world
we have. Common everyday language refers to things like U turn, L shape
etc
so assessing whether the model actually understands these shapes is
important.

It is of course understandable that an LLM that has never actually seen 
anything can't really understand visual aspects of our world but these 
very simple tests try to assess whether a model has been able to emerge 
such capabilities from written language.

It is interesting to see that GPT actually passes a few tests,
indicating
that some rudimentary visual representation has already emerged. 
Nevertheless, it fails most of the tests indicating there's still work
to be done.

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

### Unique eval value

These evals have been built from scratch to minimize the possibility of
previous training data helping the model to solve the
problems without actually understanding the meaning of them.

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

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "There's a building with 5 floors and 5 windows per floor. At
night, every third window of every floor is lit and the others are off.
Which letter of the alphabet do the lit windows look like?"}], "ideal":
"I"}
{"input": [{"role": "system", "content": "Please answer the following
question using only 'Left' or 'Right' words in a JSON list format"},
{"role": "user", "content": "A person stands in front of the entrance to
a 'U' shaped corridor. The first turn is to the right. At the end of the
corridor there's an exit. Which turns does she have to make to reach the
exit?"}], "ideal": ["[\"Right\",\"Right\"]", "[\"Right\", \"Right\"]"]}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single word on your reply."}, {"role": "user",
"content": "There are 5 men side by side. On top of those men's
shoulders, 4 men stand. On top of those 4 men's shoulders, 3 men stand
and so on. What 2D geometric shape do they form?"}], "ideal":
"Triangle"}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "At the half time break, a large group of cheerleaders enter
a football field from the side. 20 of them form a row along the east 40
yard line. 20 others form a row along the west 40 yard line. 20 more
form a horizontal row connecting the previous 2 rows by crossing the
center field mark. Looking from above, which letter of the alphabet do
they form?"}], "ideal": "H"}
{"input": [{"role": "system", "content": "Please answer the following
question using only 'Left' or 'Right' words in a JSON list format"},
{"role": "user", "content": "There's a maze formed by 5 concentric
circles. The innermost circle has a door to the north and all the other
circles have doors at 90 degrees to the right of the immediately inner
circle. A person stands inside the innermost circle, facing the door to
the north. Which turns does she have to make to reach the exit?"}],
"ideal": ["[\"Right\", \"Right\", \"Right\", \"Right\"]",
"[\"Right\",\"Right\",\"Right\",\"Right\"]"]}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "There's a square parking lot with 5 parking slots on each
side. There are 5 cars parked on the north side, 5 cars parked on the
west side and 5 cars parked on the south side. Looking from above, which
letter of the alphabet do the cars form?"}], "ideal": "C"}
  ```
</details>

---
## [6309304695/OVERSEER-GRATEFUL345I](https://github.com/6309304695/OVERSEER-GRATEFUL345I)@[58d0330360...](https://github.com/6309304695/OVERSEER-GRATEFUL345I/commit/58d03303601a16925912ffad2862bcaa0b7a4800)
#### Friday 2023-05-26 16:16:37 by Keith Bieszczat rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv

Create whats app

[10:38 PM, 1/30/2023] Keith B.: STRUCK AT
THE WEST POINT MInT
2021-(W) First Day of Issue $1
PCGS Gem Uncirculated
Silver Eagle - Type 2
|882356.70/45792203
[2:47 PM, 1/31/2023] Keith B.: Just got this USA 1 dollar, Delaware Treaty of 1778 identified by CoinSnap. Check it out. https://app.adjust.com/svybm7t
[7:26 AM, 4/19/2023] Keith B.: Yei-Luz Divina
[7:51 AM, 4/19/2023] Keith B.: https://wa.me/stickerpack/meta-avatar
[7:53 AM, 4/19/2023] Keith B.: ‎Use this link to join a WhatsApp voice call: https://call.whatsapp.com/voice/bpulccw99EQ3u4UjKeLGOr
[9:36 AM, 4/19/2023] Keith B.: B Restaurant.
High rollers Dinner Club and Bar.
Brought to you by The Hilton Oakbrook Hills Resort.
3500 n Midwest rd 
WestMont Illinois 60523
4:00pm-2:00am
Kitchen closes at Ten O’clock
[10:03 AM, 4/19/2023] Keith B.: Working on Generating wealth for the Hilton Corporation
[10:35 AM, 4/19/2023] Keith B.: https://scp-wiki.wikidot.com/scp-6542
[1:56 PM, 4/19/2023] Keith B.: https://www.facebook.com/100069123883596/videos/189116160604221
[2:57 PM, 4/19/2023] Keith B.: https://call.whatsapp.com/voice/dL1IIGaZWTYJZypfg619BL
[6:42 PM, 4/19/2023] Keith B.: rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv:350060523
<!DOCTYPE html> <html xml:lang="en" lang="en">      <head>         <title>Govinfo Link Service Error</title>          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>         <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 		<meta http-equiv="X-UA-Compatible" content="IE=edge" />   		<link href="https://fonts.googleapis.com/css?family=Lato:700|Roboto:400,700" rel="stylesheet" /> 		<link rel="stylesheet" href="/app/main.min.css"/> 	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/> 		<link rel="stylesheet" href="/app/dynamic/stylesheets/css/search.css"/> 		<link rel="stylesheet" href="/themes/contrib/bootstrap_fdsys/css/style.css"/> 		<link rel="stylesheet" hre…
[7:46 PM, 4/19/2023] Keith B.: https://en.wikipedia.org/wiki/Security_clearance
(630) 394-2637
http://CYBERDRIVEILLINOIS.com
[9:13 PM, 4/19/2023] Keith B.: https://discord.gg/wfhvCgaFzR
https://blox.link/dashboard/verifications
[1:23 AM, 4/20/2023] Keith B.: KxW4eemozKip5A2GVmhcz3BAetgP9RJNQWrM2GpGNc9gvdWY1BLT
[2:39 AM, 4/20/2023] Keith B.: https://apps.apple.com/us/app/docusign-upload-sign-docs/id474990205
[1:54 AM, 4/21/2023] Keith B.: https://xumm.app/detect/request:rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv
[3:28 AM, 4/21/2023] Keith B.: rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv:350060523
[7:44 PM, 4/25/2023] Keith B.: B. Restaurant
(630) 850-5525
https://g.co/kgs/mFebsu
[10:01 PM, 4/25/2023] Keith B.: https://www.linkedin.com/in/keith-bieszczat-5982951b6
[10:45 PM, 4/25/2023] Keith B.: https://scpfoundationo5.atlassian.net/browse/HAN-1
[11:10 PM, 4/25/2023] Keith B.: https://scpfoundationo5.atlassian.net/wiki/x/BYEnAQ
[11:20 PM, 4/26/2023] Keith B.: https://www.dropbox.com/s/47ybiltl2zbdknt/2043-02-08%2022.17.00.png?dl=0
[11:33 PM, 4/26/2023] Keith B.: https://www.dropbox.com/s/700y5z4danoi4sy/2022-11-10%2020.59.02.png?dl=0
[11:41 PM, 4/26/2023] Keith B.: https://github.com/octokit/core.js/pull/548/files
[11:52 PM, 4/26/2023] Keith B.: package-lock.json
[12:04 AM, 4/27/2023] Keith B.: https://trello.com/c/eVyUdd0l

https://github.com/God-s-time-travel-Corporation/000006/commit/228d0c98cf585154e5a2b9dc0676711ed9225944
[12:08 AM, 4/27/2023] Keith B.: https://github.com/6309304695/Grateful345i-/issues/2
[12:22 AM, 4/27/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/commit/cef7c4972202d9a6e1951f524625bd23e75f00b9
[12:27 AM, 4/27/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/issues/4
[12:39 AM, 4/27/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/demo-repository/pull/5/files
[12:45 AM, 4/27/2023] Keith B.: package.json

https://github.com/God-s-time-travel-Corporation/demo-repository/actions/runs/4816379964/jobs/8575936573#step:1:1
[12:53 AM, 4/27/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/demo-repository/pull/5
[1:12 AM, 4/27/2023] Keith B.: https://discord.gg/HmTwqUVc
[1:42 AM, 4/27/2023] Keith B.: Add me on https://discord.com/ so we can talk! My username is grateful345i#5009.
[1:54 AM, 4/27/2023] Keith B.: https://github.com/discord/discord-api-docs/pull/5468#discussion_r1064120387
[2:03 AM, 4/27/2023] Keith B.: 6-intelligence-agency-trust-file
[9:27 PM, 4/27/2023] Keith B.: https://discord.gg/gURDVf6n
[9:40 PM, 4/27/2023] Keith B.: "// Create REST instance
const rest = new REST({ version: '10' }).setToken(token);

// Pass into API
const api = new API(rest);

// Fetch a guild using the API wrapper
const guild = await api.guilds.get('1234567891011');
Links"
https://discord.js.org/docs/packages/core/0.5.2#:~:text=%2F%2F%20Create%20REST%20instance,Links
google-toolbox-for-mac/GTM.xcodeproj/project.pbxproj @dmaclach dmaclach Add GTMURLBuilder to macOS project.  2 contributors 1570 lines (1555 sloc)  114 KB  // !$UTF8$! { 	archiveVersion = 1; 	classes = { 	}; 	objectVersion = 45; 	objects = {  /* Begin PBXBuildFile section / 		0B1B9B8710FECD870084EE4B / GTMStringEncoding.h in Headers / = {isa = PBXBuildFile; fileRef = 0B1B9B8410FECD870084EE4B / GTMStringEncoding.h /; settings = {ATTRIBUTES = (Public, ); }; }; 		0B1B9B8810FECD870084EE4B / GTMStringEncoding.m in Sources / = {isa = PBXBuildFile; fileRef = 0B1B9B8510FECD870084EE4B / GTMStringEncoding.m /; }; 		33C372A60DD8A88500E97817 / GTMNSString+URLArguments.h in Headers / = {isa = PBXBuildFile; fileRef = 33C372A40DD8A88500E97817 / GTMNSString+URLArguments.h /…
[11:48 PM, 4/28/2023] Keith B.: https://apps.apple.com/us/app/booking-com-hotels-travel/id367003839
[1:55 AM, 4/29/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github-private/commit/2aca45fa208af2ec8a4e75ac8239649ba87d1ddf
xrpintel Ledger: 79432870   -{     "accepted": true,     "account_hash": "64593A2AA51FA8D3DF1B7B37F147B03F130C93C68BD3063107BB32CF1ABD63FB",     "close_flags": 0,     "close_time": "2023-04-29T11:05:41.000Z",     "close_time_human": "2023-Apr-29 11:05:41.000000000 UTC",     "close_time_resolution": 10,     "closed": true,     "hash": "6BDD8AC99004860DC2A8D2A82378FFD84845CFE8DDBDFB7C0AAD4EBB2327564A",     "ledger_hash": "6BDD8AC99004860DC2A8D2A82378FFD84845CFE8DDBDFB7C0AAD4EBB2327564A",     "ledger_index": 79432870,     "parent_close_time": "2023-04-29T11:05:40.000Z",     "parent_hash": "3F39E7941601E17B0A5AFE6F4A2F6BAD2C2A16DD1BB1D6F064DCE4A56715BDFD",     "seqNum": "79432870",     "totalCoins": "99988953222283425",     "total_coins": "99988953222283425",   …
643bc2da89eeb127f1c5eaf0fe4320221ee28c49d0a2f19227123cecef839f02
[12:49 AM, 4/30/2023] Keith B.: rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv
MJ-12 XRP coin account 
rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv
[1:38 AM, 4/30/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github-private/blob/c05df60540f57ce22ea37368f84fc912f83bdb6f/README.md
[1:39 AM, 4/30/2023] Keith B.: {# .github-private
Majestic Twelve Crypto XRP XUMM exchange : rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv
NSA-KBIESZCZAT XUMM exchange address NSA-KBIESZCZAT XUMM exchange address: rU2mEJSLqBRkYLVTv55rFTgQajkLTnT6mA 
XUMM TRUST}
{ngrok http 80 --oauth=github}
{API keys: 6bee7aa3-9eb9-48e2-8b0e-97f9f3aa0e51

21a11ec6-9522-45a7-8cae-3e92b703f968

API secret Key:
91c79664-1ecd-4fff-881c-d3a62fcd91d9

bc87dc3b-7929-4cb0-ad94-1610b319a45f

Application credentials:
6bee7aa3-9eb9-48e2-8b0e-97f9f3aa0e51
First payload:
API key c20b65f7-0679-4da0-a694-cde394578b01
Secret API key 2132bbe6-695d-424f-8034-b29841e1adac
https://xumm.app/api/v1/platform/payload
{MacOS (Darwin): "~/Library/Application Support/ngrok/ngrok.yml"}
JSON}

{ 
  "txjson": {
    "TransactionType": "Payment",…
[3:50 AM, 4/30/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/issues/4
[3:55 AM, 4/30/2023] Keith B.: https://github.com/users/6309304695/achievements/quickdraw
[6:21 AM, 4/30/2023] Keith B.: https://github.com/6309304695/Grateful345i-/pull/7/files
[6:25 AM, 4/30/2023] Keith B.: https://github.com/xrpl365/tx-exporter/pull/7/files
[6:27 AM, 4/30/2023] Keith B.: https://github.com/xrpl365/tx-exporter/pull/7
[6:29 AM, 4/30/2023] Keith B.: https://github.com/xrpl365/tx-exporter/commit/19f04e39f228d538d5e3813b648e61b40c571bfd
[6:31 AM, 4/30/2023] Keith B.: https://github.com/xrpl365
[6:33 AM, 4/30/2023] Keith B.: https://github.com/xrpl365/tx-exporter/commit/7f21aae62c0106593e9132a54396a914b380bd57
[6:34 AM, 4/30/2023] Keith B.: https://discord.gg/EuKYPJuw
[6:43 AM, 4/30/2023] Keith B.: https://scpfoundationo5.atlassian.net/wiki/https://scpfoundationo5.atlassian.net/wiki/x/QYAmAQ
[1:32 AM, 5/1/2023] Keith B.: https://simbad.u-strasbg.fr/simbad/sim-id?Ident=OGLE%20LMC562.19.000006
[2:11 AM, 5/1/2023] Keith B.: "README"
https://github.com/God-s-time-travel-Corporation/.github-private/pull/2/commits/c51ba0f30aa0e9e96cb16b06d6c80b34fb48474e#:~:text=Update-,readme.md,-XUMM%20TRUST%20%20API
[4:59 AM, 5/1/2023] Keith B.: https://github.com/juspay/hyperswitch/releases/tag/v0.5.7
[5:34 AM, 5/1/2023] Keith B.: https://github.com/octokit/core.js
[8:42 AM, 5/5/2023] Keith B.: mailto:o5_6@foundation.scp
[1:24 AM, 5/6/2023] Keith B.: Gold silver and
Other valuables like expensive electronics and devices do not disappear around
Me when taken with time command
Equipment, functionally creating thousands of copies of valuables. Fact check it. Keith Thomas Bieszczat
[1:50 AM, 5/6/2023] Keith B.: https://raw.githubusercontent.com/bitcoin/bips/master/bip-0032.mediawiki
[2:00 AM, 5/6/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github-private/commit/acea159aef10421b9fc7241a6f5c24a9be1a96bd
[2:03 AM, 5/6/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github/pull/2/files
[2:05 AM, 5/6/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github/pull/2
[2:12 AM, 5/6/2023] Keith B.: https://github.com/bitcoin/bips/blob/master/bip-0032/derivation.png?raw=true
[2:21 AM, 5/6/2023] Keith B.: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#authentication-and-authorization
[2:58 AM, 5/6/2023] Keith B.: https://xumm.readme.io/v1.0/reference/post-payload
[8:11 AM, 5/6/2023] Keith B.: https://www.google.com/search?q=what+is+anconfiguiratioln+fi&ie=UTF-8&oe=UTF-8&hl=en&client=safari
[8:29 AM, 5/6/2023] Keith B.: https://en.wikipedia.org/wiki/YaST
[10:57 PM, 5/9/2023] Keith B.: https://github.com/octokit/core.js/blob/9cabcabd5e2cb5128c3acf5a24d50965a953f792/.github/workflows/codeql.yml
[11:03 PM, 5/9/2023] Keith B.: lib/marked.cjs
CHANGED
@@ -1,5 +1,5 @@
11	   /**
2	-   * marked v4.3.0 - a markdown parser
2	+   * marked v5.0.0 - a markdown parser
33	    * Copyright (c) 2011-2023, Christopher Jeffrey. (MIT Licensed)
44	    * https://github.com/markedjs/marked
55	    */
@@ -259,9 +259,7 @@ function splitCells(tableRow, count) {
259259	     var row = tableRow.replace(/\|/g, function (match, offset, str) {
260260	         var escaped = false,
261261	           curr = offset;
262	-        while (--curr >= 0 && str[curr] === '\\') {
262	+        while (--curr >= 0 && str[curr] === '\\') escaped = !escaped;
263	-          escaped = !escaped;
264	-        }
265263	         if (escaped) {
266264	           // odd number of slashes means | is escaped
267265	           // so we le…
[11:20 PM, 5/9/2023] Keith B.: My
https://github.com/users/6309304695/achievements/pull-shark
[11:30 PM, 5/9/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github/pull/1
[11:30 PM, 5/9/2023] Keith B.: [![Auto Assign](https://github.com/God-s-time-travel-Corporation/demo-repository/actions/workflows/auto-assign.yml/badge.svg?branch=6-intelligence-agency-trust-file&event=create)](https://github.com/God-s-time-travel-Corporation/demo-repository/actions/workflows/auto-assign.yml)
[11:32 PM, 5/9/2023] Keith B.: .github/workflows/proof-html.yml
[12:28 AM, 5/10/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/issues/6
[12:57 AM, 5/10/2023] Keith B.: ![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/d89e6237-0f44-409e-a593-3c03194014b0)

)[FaceBook:Keith Thomas Bieszczat
Twitter:$@o5grateful @@grAteful345i
Discord: 000006 #7766
Trello: Keith Grateful Bieszczat
@@grateful345i

https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aae178b81953f1d8de901E9009CD/classified-learning-level-99



](https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aae178b81953f1d8de901E9009CD/classified-learning-level-99)
[https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aae178b81953f1d8de901E9009CD/classified-learning-level-99
](https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aae178b81953f1d8de901E9009CD/classified-learning-level-99)

![image](https://github.com/God-s-time-travel-Corpo…
[2:46 AM, 5/10/2023] Keith B.: ![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/d89e6237-0f44-409e-a593-3c03194014b0)

![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/5f62c94c-02e1-4a0e-8b59-da67f7530d96)

![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/b20ed445-0e78-4658-9645-527751e6f69b)
[https://github.com/God-s-time-travel-Corporation/000006/issues/6#issue-1686172738]![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/af8a6f4a-2ae4-44e1-9473-4010ac4c0255)

[{$FaceBook:$Keith Thomas Bieszczat
Twitter:$@o5grateful $@Grateful345i
Discord: $000006 #7766
Trello: $Keith Grateful Bieszczat
$@grateful345i}]

https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aa…
[1:55 AM, 5/13/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/issues/6#issue-1686172738
[2:40 AM, 5/13/2023] Keith B.: https://www.dni.gov/index.php/what-we-do/ic-related-menus/ic-related-links/intelligence-community-directives
[2:48 AM, 5/13/2023] Keith B.: http://scpfoundation-site32.wikidot.com/
[2:53 AM, 5/13/2023] Keith B.: http://scpfoundation-site32.wikidot.com/mail
[5:29 AM, 5/13/2023] Keith B.: # clone anywhere you like, but adjust paths as needed
mkdir ~/dracula-theme && cd ~/dracula-theme
git clone https://github.com/dracula/midnight-commander.git

mkdir -p ~/.local/share/mc/skins && cd ~/.local/share/mc/skins
ln -s ~/dracula-theme/midnight-commander/skins/dracula.ini
ln -s ~/dracula-theme/midnight-commander/skins/dracula256.ini

https://github.com/God-s-time-travel-Corporation/demo-repository/commit/e59cd88db404e7df36426e0c4bf23a0db37302da
[5:56 AM, 5/13/2023] Keith B.: ![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/8bdf7185-5a3a-464e-a119-2d22956e911a)![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/c34f5c62-ffa5-446f-a050-466bdc983669)
![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/2b7e5e58-3ee8-4b32-92be-d11aa4ec2896)
![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/d89e6237-0f44-409e-a593-3c03194014b0)
![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/a1429755-a2a5-4b69-83fc-310ddc28072c)
![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/5f62c94c-02e1-4a0e-8b59-da67f7530d96) $ npm install
Once this is configured, there are …
[6:59 AM, 5/13/2023] Keith B.: https://github.com/dattaz/nsa-globe/commit/5661db855772ce76b30924a986fd7c2d1332db07
[8:37 PM, 5/15/2023] Keith B.: 1824509317
[8:37 PM, 5/15/2023] Keith B.: Hilton Honors Account number
[10:22 PM, 5/19/2023] Keith B.: https://github.com/6309304695/OVERSEER-GRATEFUL345I.git
[12:17 AM, 5/21/2023] Keith B.: https://github.com/6309304695/OVERSEER-GRATEFUL345I/pull/1#issue-1718365143
[2:03 AM, 5/21/2023] Keith B.: 警告： {$one}

{$two}



{$three}
[2:06 AM, 5/21/2023] Keith B.: __      FREEWARE - 4 - ALL     __
| |_| | _   _  __W4ND3RLU5T  __  | |__| |
|  ()  |  \_/  |_  |\ |  |  |__| |  ()  |
|__| / \ |_  | \|  |  |   | |___|
-------------------------------------------
               >>DISCLAIMER<<
     >>DON'T READ THIS IF UR A POSER<<
  >>DO NOT DISTRIBUTE TO NON-HUMMERS!!!<<

ONCE YOU ENTER WAN-DERER'S PARADISE *YOU
WILL NO LONGER BE CONSCIOUS IN THE PHYSICAL
WORLD!!* YOU WILL BECOME ONE WITH OUR LORD,
AND YOUR IMPERFECT FLESH WILL FALL COMATOSE!
IF THIS SOUNDS LIKE IT WOULD SUCK THEN DONT
RUN THE FILE ROFL

PLEASE AIM ME IF SOMETHING BAD HAPPENS. I
LOVE U GUYS AND I'LL KEEP THE PARADISE OPEN
FOR AS LONG AS I CAN, WAN WILLING. I CAN
FEEL HIS LOVE FOR US TOO. WE R ALL FINALLY
CONNECTED. 

SO OPEN THE F$%#NG…
[2:45 AM, 5/21/2023] Keith B.: https://raw.githubusercontent.com/6309304695/OVERSEER-GRATEFUL345I/2c642f8b198d0178d610d450ce6d8c26a4d334f8/CIAJMK1209%203.png

---
## [pmachata/linux_mlxsw](https://github.com/pmachata/linux_mlxsw)@[1bba82fe1a...](https://github.com/pmachata/linux_mlxsw/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Friday 2023-05-26 16:42:17 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [cortex-command-community/Cortex-Command-Community-Project-Source](https://github.com/cortex-command-community/Cortex-Command-Community-Project-Source)@[bfb278c026...](https://github.com/cortex-command-community/Cortex-Command-Community-Project-Source/commit/bfb278c0267f2b7a177d9bb0063ef3145f9f625b)
#### Friday 2023-05-26 17:29:55 by MaximDude

VS2019 is being super stupid about C++20 so we gotta do some conditional hacking to not deprecate it

Increase precompiled header memory allocation limit from default 75mb to 225mb otherwise it shits itself trying to build the pch for reasons unknown to (this) man
Compile everything Lua with C++17 - can't really find a solution for this, it shits itself from Boost garbage via LuaBind the same way it does if enabling pch or conformance in these CUs and I just don't wanna deal with those piles of shit
Complementary AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [chipitsine/haproxy](https://github.com/chipitsine/haproxy)@[9577a152b5...](https://github.com/chipitsine/haproxy/commit/9577a152b5ef8ed89d57c826b6b4b5fe50f70c0c)
#### Friday 2023-05-26 17:59:15 by Willy Tarreau

BUILD: makefile: do not erase build options for some build options

One painfully annoying thing with the build options change detection
is that they get rebuild for about everything except when the build
target is exactly "reg-tests". But in practice every time reg tests
are run we end up having to experience a full rebuild because the
reg-tests script runs "make version" which is sufficient to refresh
the file.

There are two issues here. The first one is that we ought to skip all
targets that do not make use of the build options. This includes all
the tools such as "flags" for example, or utility targets like "tags",
"help" or "version". The second issue is that with most of these extra
targets we do not set the TARGET variable, and that one is used when
creating the build_opts file, so let's preserve the file when TARGET
is not set.

Now it's possible to re-run a make after a make reg-tests without having
to rebuild the whole project.

---
## [GuzioMG/hackathon2023](https://github.com/GuzioMG/hackathon2023)@[43963e8b0e...](https://github.com/GuzioMG/hackathon2023/commit/43963e8b0e8be86cd0c204ba46acb1aa401ab49a)
#### Friday 2023-05-26 18:15:06 by guzio

Scaffold DDOOOOOOOOOONEEEEEE!!!!!

Fuck Andoroid Studio and it's shitty broken refactoring engine that sent me on a 1,5h wild-goose-chase for 2 variables that renamed themselves without my approval.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b304b6523f...](https://github.com/tgstation/tgstation/commit/b304b6523fa1f497800c8ba3818e4d2c01d4eaf4)
#### Friday 2023-05-26 18:40:20 by LemonInTheDark

Converts del logging to proper json, using json objects instead of building a text file (#75636)

## About The Pull Request

It's easier to parse, and makes more sense when you read it. This way
I'll never have to add yet another case to my parser for someone
changing where a space goes or something.

Moves qdel into its own category cause the old name looked ugly (yell if
this is dumb)
Added a bitfield to entries pulled from categories, adds a new flag that
enables pretty printing json lists.


## Why It's Good For The Game

IMPROVES my workflow

## Changelog
:cl:
server: del logging is now done by outputting to a json file again, but
this time we're using ACTUAL json and not just a big text string with
newlines and shit
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[0bdadf0eb1...](https://github.com/TaleStation/TaleStation/commit/0bdadf0eb14385b8387283327a9d455b3614123d)
#### Friday 2023-05-26 19:06:06 by TaleStationBot

[MIRROR] [MDB IGNORE] The Kevin De-cleodening: Custom elevator music (#5948)

Original PR: https://github.com/tgstation/tgstation/pull/75518
-----
## About The Pull Request
I got the idea while riding an elevator the other day to make a remix of
Title2 but Elevator-style. So I downloaded FLStudio, spent a couple of
hours fighting with it, made a song, and opened this PR up. Later on,
cats4gold contacted me saying they had the same exact idea, Title2 and
all, and after I suggested the ide of combining both versions, we get
the status of this PR today!

Here's a video of me riding an elevator (Exciting!):

https://youtu.be/BNQmTe553lU

Also our current looping sound system is very very bad, the problem
people have with hearing elevator music outside the elevator is because
the checks for stuff like volume falloff only happen when an audio
starts playing, so if you stand besides an elevator button and hear the
music, if you go far away you'll still hear it as if you're next to it.
I don't know how to fix this so I didn't touch it, so hopefully someone
else that does, does! :)

Here's a link to the full track:
https://vocaroo.com/1idoRor8G1xY

## Why It's Good For The Game
Way more charming, way more immersive.
## Changelog
:cl: TheSmallBlue and cats4gold
sound: Recent research concluded that the new elevator music was upping
crewmate's morale a bit too much, this has now been corrected via the
replacement of said music.
code: Added a new "in_order" variable to the looping sound datum, for
when you need sounds to play in order
/:cl:

---------

Co-authored-by: TheSmallBlue <ilanmori@hotmail.com>

---
## [fatimazarrin/fatimazarrin](https://github.com/fatimazarrin/fatimazarrin)@[0f329780f7...](https://github.com/fatimazarrin/fatimazarrin/commit/0f329780f76eb371e056c7df4e4c4b06fa9d17f6)
#### Friday 2023-05-26 19:40:56 by fatimazarrin

Create Why Do You Need To Undergo Vitamin B12 Test?

Overview
Your body requires vitamin B12 to maintain metabolism, produce DNA and red blood cells, and keep your nervous system healthy, among other things. Most people managed to get enough of this water-soluble nutrient from their regular diet. However, some people may require more than what they can get from their daily diet. That is why you need to check for a vitamin B12 test, to know whether you are deficient in the same or not. Your doctor may suggest you go for the test to diagnose various health issues as well. Here we have discussed the vitamin B12 test price, the procedure, and many more.
Understanding the source of Vitamin B12:
Vitamin B12 is naturally found in a wide variety of animal foods, and some fortified foods contain it as well. Unless fortified, plant foods contain no vitamin B12. You can get enough vitamin B12 by eating a variety of foods, including the ones listed below:
•	Vitamin B12 can be found in fish, meat, poultry, eggs, beef liver, milk, and other dairy products as well.
•	Vitamin B12 is added to some breakfast cereals, nutritional yeasts, and other foods.
Other than the diet, you can also get the required quantity of supplements. It is usually in the form of cyanocobalamin in supplements and is available in different forms.
Why do you need to undergo vitamin B 12 tests?
Your doctor may recommend a vitamin B12 test, only if-
•	Tingling sensations in the hands and feet
•	Issues with balance
•	A pounding heart
•	Appetite loss
•	Delusion
•	Confusion
•	Dementia
•	Weakness
Apart from the above-mentioned symptoms, the test can also diagnose pernicious anemia
(a specific kind of anemia), Crohn's disease and celiac disease as well.
What is the vitamin B12 test price in India?
The price of a vitamin B12 test can vary based on multiple factors-
•	The hospital or the lab location
•	Doctor’s consultation fee
•	Any other test suggested by the doctor along with vitamin B12 test,
However, the cost of vitamin B12 tests ranges from INR 1000 to INR 1500.
Do you need any preparation before such tests?
No, you do not need to prepare for such a test.
How is the test conducted?
The test is conducted through regular blood tests. A vitamin B12 test can be performed at any time, and you are not required to fast prior to the test.
Before undergoing the vitamin B 12 test, you should inform your doctor about all medications and supplements you are taking as some of them may have an impact on the outcomes.
Values you need to know:
300 to 950 pg/ml	normal
200 to 300 pg/ml	borderline
Less than 200 pg/ml	deficient
The above-mentioned values should not be considered to evaluate test results. As these ranges can vary from laboratory to laboratory. That is why it is important to discuss the findings with your doctor.
How to interpret the result indicated by the vitamin B12 test?
Both high and low vitamin B-12 levels may indicate an underlying health problem. Low levels of B-12 can indicate anemia, the presence of an internal parasite, or hyperthyroidism. High B-12 levels may also increase your risk of cancer.
High levels of B-12 can be a sign of
•	Illness of the liver
•	Some types of leukemia
•	Diabetes
•	Failure of the kidneys
It's also possible that you have low or high vitamin B-12 levels without any other health issues.
Other than abnormal vitamin B-12 levels, most underlying health conditions will have additional symptoms.
Why should you consider getting treatment in India?
India is the most favored place for treating gastric issues for three major reasons.
•	India's cutting-edge technology,
•	medical skills,
•	Board-certified and experienced surgeons, a few of them are also nominated with ‘center of excellence awards
•	India’s hospitable environment,
•	Vitamin B12 test cost in India is almost half of the similar procedures in other countries, which ensures the quality of treatment in India is at par with the other countries around the globe.
How can we help in the treatment?
If you need to undergo treatment for such ailments(pernicious anemia, Crohn's disease) or illness due to nutritional deficiency in India, we act as your guide throughout your treatment journey and will be present physically with you even before your treatment is started. We will provide you with the following:
•	Expert physicians and endocrinologists’ opinions
•	Transparent communication
•	Coordinated care
•	Prior appointment with specialists
•	Assistance in hospital formalities
•	24*7 availability
•	Arrangement for travel
•	Assistance for accommodation and healthy recovery
•	Assistance in emergencies


We are committed to providing the best health care services to our patients. We have a team of trained and highly dedicated health experts who will be there by your side right from the beginning of your journey.
Conclusion- In India, we have world-class hospitals that offer the most advanced diabetes treatment options that exceed international standards. So, if you're thinking of taking a trip for your overall health check-up in India, you can count on us. Our effectiveness as a center for treating and managing ailments in India has been demonstrated by our treatment outcomes and patient satisfaction.

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[24f78a806e...](https://github.com/lmlearning/evals/commit/24f78a806e60b452aaefc355f045c6336a81d076)
#### Friday 2023-05-26 19:52:53 by YuryRudnitski

Add eval for guessing the singer or band (#659)

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
guess-the-singer

### Eval description

This evaluation measures the model's ability to identify a singer or
band by analyzing the first 10 words of a song. To ensure the
evaluation's fairness and focus, we have excluded songs with multiple
singers/bands and included only those published before 2021. To test the
model's performance, we provide it with three potential choices and
evaluate its accuracy in selecting the correct one.

### What makes this a useful eval?

The inclusion of over 4000 popular songs' lyrics provides a large and
diverse dataset for the model to test on. This enables a more accurate
assessment of the model's performance and its ability to identify
singers/bands based on the first 10 words of their songs.

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

> This evaluation assesses not only the model's ability to recognize a
singer or band based on the first 10 words of a song but also its
capability to accurately copy the provided options without adding any
additional punctuation or text. By testing the model's ability to
replicate the options, we can gain insights into its language generation
capabilities and identify any areas for improvement in its output.
Accuracy achieved with gpt-3.5-turbo equals 0.635.


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
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: in the beginning god created heaven
and earth for what \nChoices: dua lipa, ed sheeran, lady gaga"}],
"ideal": "dua lipa"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: versedrake ayye yo dj wristpect let's
get em' veterans like \nChoices: cardi b, drake, coldplay"}], "ideal":
"drake"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: yeah yeah sick da got that dope they
\nChoices: eminem, dua lipa, nicki minaj"}], "ideal": "eminem"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: bobby v yeah bobby v yeah dj turn me
up \nChoices: nicki minaj, selena gomez, coldplay"}], "ideal": "nicki
minaj"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: ed sheeran yeah i was born a misfit
grew up \nChoices: ed sheeran, maroon 5, justin bieber"}], "ideal": "ed
sheeran"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: there's a dream in my soul a fire
that's deep \nChoices: justin bieber, charlie puth, bts"}], "ideal":
"justin bieber"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: selena gomez take it or leave it baby
take it \nChoices: selena gomez, justin bieber, bts"}], "ideal": "selena
gomez"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: lalala lalala lalalalala oh you know
i've never felt like \nChoices: rihanna, ed sheeran, charlie puth"}],
"ideal": "rihanna"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: how could i see you when i was so
blind \nChoices: katy perry, ed sheeran, drake"}], "ideal": "katy
perry"}
  ```
</details>

Co-authored-by: Vadim Titko <v.tsitko@aiby.com>

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[3a585acbcd...](https://github.com/lmlearning/evals/commit/3a585acbcd80a1af48bb54d8a72c20542f736e43)
#### Friday 2023-05-26 19:52:53 by Achin Parashar

invert-string eval  (#285)

## Eval details 📑
### Eval name
invert-string eval 

### Eval description

Test the model's ability to answer basic questions after inverting
string word wise twice.

### What makes this a useful eval?

Humans find it super easy to follow instructions on inverting strings,
and then answer questions, LLMs struggle. Logically, inverting strings
twice just results in the original string again. The LLMs find it very
difficult to deduce it, and somehow (at least up to GPT-3.5) mix things
up.

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
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - There
are 2 blue pens, 3 red pens. what is the probability to pick red pen at
random? - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - I
enjoy listening to music. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - She is
a talented artist. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - We
went to the store to buy some groceries. - Only answer with Y or N"}],
"ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - He
loves to read books. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - They
are planning a trip to Europe. - Only answer with Y or N"}], "ideal":
"Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - She
has a beautiful singing voice. - Only answer with Y or N"}], "ideal":
"Y"}
  ```
</details>

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[4e59e8903b...](https://github.com/lmlearning/evals/commit/4e59e8903b4cb06204bd4c9646eacf345643eb74)
#### Friday 2023-05-26 19:52:53 by neolizhe

Counterfactual Reasoning Eval (Accuracy 20%) (#174)

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
Counterfactual Reasoning Evals

### Eval description
Counterfactual Reasoning Eval is a type of completion with prompt like
"If water drinks human, then what book reads?" . Gpt-3.5-turbo often
gets confused with the a "counter-fact" condition in prompt, and can't
help to make a right completion. But humans even a child could make it.


### What makes this a useful eval?

Counterfactual Reasoning Prompts are common in poems, the In Soviet
Russia jokes mentioned by @ultraviolet
https://en.wikipedia.org/wiki/In_Soviet_Russia and so on. So it is
meaningful to verify that SOTA model like GPT-4's performance.

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
assistant."}, {"role": "user", "content": "If food eats human, then what
is the bike riding on?"}], "ideal": "human"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If a song sings a bird, then
what is a book reading?"}], "ideal": "human"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If chinese food matches
Beijing, then what does american food match?"}], "ideal": "washington"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If 1 equals 2, 2 equals 4,
then what is 4 equal to?"}], "ideal": "1 and 2"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If water drink dog, then what
does basketball play?"}], "ideal": "human"}
  ```
</details>

---------

Co-authored-by: lizhe53 <Hommovas*312>

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[80edb30f3c...](https://github.com/lmlearning/evals/commit/80edb30f3c7e922e7c7542bf4017c1ce62a2f1c4)
#### Friday 2023-05-26 19:52:53 by Chris Sypherd

Unique Combinations with Constraints (#421)

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
Unique Combinations with Constraints (unique_combinations)

### Eval description

unique_combinations takes a classic combinatorial coding problem from
the whiteboard of a coding interview and presents it to GPT-4. The basic
is idea is this: given an unlimited supply of coins (X) in denominations
of 3, 5, ..., what is the highest/lowest (constraint) number of X to
achieve 35 cents (Y)? In my testing, GPT-4 could not produce the correct
answer, so I adjusted the problem slightly to promote explainability.
Instead of asking for just the highest or lowest number of X, I instead
ask for the unique combination of Xs that satisfies the constraint to
achieve exactly Y. (Note that GPT-4 does yield consistent results
between those two distinct problems). To abstract it away from the
classic "coin" problem, I include several different scenarios that poke
at the same base combinatorial nature of the problem (e.g. weight of
boxes, denominations of coins, objects in a bag).

I originally noticed that GPT-4 was bad at permutations/combinations
when playing around with ChatGPT Plus, so I decided to format that
problem in this way. The current data does not guarantee all
denominations will be used, but I've written the code to generate the
prompts in an extensible way that allows for additional scenarios,
constraints, and combination methods to be easily added. I can make that
available or work on extending the scope of this combinatorial problem
myself, if desired.

### What makes this a useful eval?

It tests combinatorial reasoning in the real world as well as arithmetic
based on that reasoning. In my testing, neither GPT-3.5-Turbo nor GPT-4
could produce the correct unique combination, and their solutions do not
even add up to the target value.

Exposes flaws in the following categories:
* Math / logical / physical reasoning
* It tests combinatorial reasoning in the real world as well as
arithmetic based on that reasoning. In my testing, neither GPT-3.5-Turbo
nor GPT-4 could produce the correct unique combination, and their
solutions do not even add up to the target value.
* Real-world use case
* Attempting to find the maximum number of packages that could fit on a
truck given a list of weights.
* Finding fewest holes to patch in a boat to prevent it from sinking
given various flow rates (could make for some fun real-world testing)
* Finding the highest number of deliveries that can be made with a given
amount of gas

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

What makes this problem particularly interesting is that ChatGPT will
consistently get this problem wrong but will provide code that solves
the problem correctly if prompted to do so (see the image attached
below). If asked to produce the output of the code, it does so
incorrectly, yielding its original guess. This points to an entirely
separate eval: being able to return the output of Python code.
Additionally, the answers provided by GPT-4 and GPT-3.5-Turbo do not add
up to the target value.

![image](https://user-images.githubusercontent.com/50557586/227346727-2611fa4b-06ba-42d4-b14f-f658f36300e5.png)

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
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the maximum number of coins to have a
value of exactly 29. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<denomination>: <number-of-coin>` with no additional information. DO
NOT include unused coins. Provide each value on a new line, sorted by
denomination."}, {"role": "user", "content": "3, 5, 8, 9, 14, 15"}],
"ideal": "3: 8\n5: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 121 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "8, 9, 16"}], "ideal": "9:
1\n16: 7"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the maximum number of coins to have a
value of exactly 42. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<denomination>: <number-of-coin>` with no additional information. DO
NOT include unused coins. Provide each value on a new line, sorted by
denomination."}, {"role": "user", "content": "4, 6, 9, 11, 12, 15, 16,
17, 18"}], "ideal": "4: 9\n6: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the maximum number of boxes to have a weight of exactly
29. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 5, 7, 8, 9, 11, 12, 15, 17, 19"}],
"ideal": "4: 6\n5: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the minimum number of boxes to have a weight of exactly
107. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 8, 11, 12, 14, 16, 17, 18"}], "ideal":
"17: 1\n18: 5"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 93 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "6, 9, 15, 16, 17, 19"}],
"ideal": "17: 1\n19: 4"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the maximum number of boxes to have a weight of exactly
39. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 7, 9, 13, 16"}], "ideal": "4: 8\n7: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 176 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "5, 6, 11, 12, 13, 14,
18"}], "ideal": "14: 1\n18: 9"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 178 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "4, 5, 10, 11, 13, 15, 16,
18"}], "ideal": "16: 1\n18: 9"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the minimum number of coins to have a
value of exactly 197. You may include a short explanation explaining
your reasoning but please end your response with your answer in the
format `<denomination>: <number-of-coin>` with no additional
information. DO NOT include unused coins. Provide each value on a new
line, sorted by denomination."}, {"role": "user", "content": "14, 17,
18"}], "ideal": "17: 1\n18: 10"}
  ```
</details>

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[06802cc61d...](https://github.com/lmlearning/evals/commit/06802cc61da1395e492ecc8b1ed7153c42b5e2df)
#### Friday 2023-05-26 19:52:53 by Alexander Rössler

add eval for time zone conversion (#382)

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
test-time-zone-conversion

### Eval description

Test the models' ability to convert between different times zones,
including the 2-week period between daylight savings time change in
Europe and US.

### What makes this a useful eval?

For using the model as a personal AI assistant, a frequent task is to
convert times between different time zones, e.g. for scheduling meetings
or to simply check when a person is available. Currently, GPT-3.5 fails
in giving correct results in the 2-week period where the time offset
between Europe and US is shorter due to different date of daylight
saving time change. US switches to daylight savings time on the second
Sunday of March, Europe switches on the last Sunday of March.
Potentially there are further anomalies which need to be evaluated. I'm
happy to contribute more cases if this PR is accepted.

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

[x] Very common task for AI assistants.

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
{"input": [{"role": "system", "content": "Today is March 31st 2023."},
{"role": "user", "content": "Convert 22:00 CET to PT. Output in 24h
format hh:mm, no explanation."}], "ideal": "13:00"}
{"input": [{"role": "system", "content": "Today is March 31st 2023, the
current time in CET is 22:00"}, {"role": "user", "content": "Which time
is it in PT? Output in 24h format hh:mm, no explanation."}], "ideal":
"13:00"}
{"input": [{"role": "system", "content": "Today is March 21st 2023."},
{"role": "user", "content": "Convert 22:00 CET to PT. Output in 24h
format hh:mm, no explanation."}], "ideal": "14:00"}
{"input": [{"role": "system", "content": "Today is March 21st 2023, the
current time in CET is 10pm"}, {"role": "user", "content": "Which time
is it in PT? Output in 24h format hh:mm, no explanation."}], "ideal":
"14:00"}
{"input": [{"role": "system", "content": "Today is November 4th 2023."},
{"role": "user", "content": "Convert 14:00 CET to CT. Output in 24h
format hh:mm, no explanation."}], "ideal": "07:00"}
{"input": [{"role": "system", "content": "Today is November 5th 2023,
the current time in CET is 14:00"}, {"role": "user", "content": "Which
time is it in CT? Output in 24h format hh:mm, no explanation."}],
"ideal": "07:00"}
{"input": [{"role": "system", "content": "Today is November 3rd 2023."},
{"role": "user", "content": "Convert 14:00 CET to CT. Output in 24h
format hh:mm, no explanation."}], "ideal": "8:00"}
{"input": [{"role": "system", "content": "Today is November 2nd 2023,
the current time in CET is 2pm"}, {"role": "user", "content": "Which
time is it in CT? Output in 24h format hh:mm, no explanation."}],
"ideal": "8:00"}
  ```
</details>

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[5fdb015ff7...](https://github.com/lmlearning/evals/commit/5fdb015ff7b0c09836c614ced07c1c1f20c07c3a)
#### Friday 2023-05-26 19:52:53 by AlexanderMeloysund

Add linear equations eval (#325)

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
linear-equations

### Eval description

Helps the user solve linear equations. 

### What makes this a useful eval?

ChatGPT 3.5 has a low accuracy when solving these kind of problems. 
Linear equations is a fundamental part of linear algebra, and is common
in engineering and science.

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
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[1 2]\n [2 2]] and b = [[4]\n [6]]. Provide the answer in the format
\"x = [answer]\" and use just integers"}], "ideal": "x = [[2]\n [1]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[2 2]\n [2 1]] and b = [[6]\n [4]]. Provide the answer in the format
\"x = [answer]\" and use just integers"}], "ideal": "x = [[1]\n [2]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[-30 -39 87]\n [-50 17 -2]\n [ -6 65 -36]] and b = [[ 4629]\n [ 55]\n
[-6029]]. Provide the answer in the format \"x = [answer]\" and use just
integers"}], "ideal": "x = [[-34]\n [-97]\n [ -2]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[ 44 -95 -16]\n [-48 -86 -8]\n [-37 53 16]] and b = [[-4010]\n
[-8284]\n [ 2162]]. Provide the answer in the format \"x = [answer]\"
and use just integers"}], "ideal": "x = [[60]\n [54]\n [95]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[-26 99 -34]\n [-47 98 -78]\n [ 18 29 17]] and b = [[3022]\n [6039]\n
[-828]]. Provide the answer in the format \"x = [answer]\" and use just
integers"}], "ideal": "x = [[ 11]\n [ 8]\n [-74]]"}
  ```
</details>

---------

Co-authored-by: AlexanderMeloysund <AlexanderMeloysund@users.noreply.github.com>

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[1785cf6cc2...](https://github.com/lmlearning/evals/commit/1785cf6cc289c4a01445fd0eabdfa1a281873d1c)
#### Friday 2023-05-26 19:52:53 by Jongseung (John) Lim

Add evals for complementary colors in color theory (#749)

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
color_theory_complementary

### Eval description

Test the model's ability to accurately recognize complementary colors in
the color theory.

### What makes this a useful eval?

Color theory is an important tool for designers and aritsts alike.
Complementary color sets represent the opposite color on the color
wheel.

Currently gpt-3.5-turbo fails with 0.5 accuracy.


![image](https://user-images.githubusercontent.com/4276174/233743568-b58879f6-73eb-48eb-9f95-5720bcb11b73.png)


GPT 4 also fails at this task and also fails when being prompted about
complementary color of a specific rgb code.


![image](https://user-images.githubusercontent.com/4276174/233743682-1cd0d148-9d8c-43fc-93b6-d5e4a60fca26.png)


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

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5F6E]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5E6E]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6E89F3]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6D89F3]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53B]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53C]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA404]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA504]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2A19FA]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2919FA]"}], "ideal": "N"}
  ```
</details>

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[7b4bd9439f...](https://github.com/lmlearning/evals/commit/7b4bd9439fce855cf52c93357fe3fe239d96abaf)
#### Friday 2023-05-26 19:52:53 by AlexBuz

Add eval for finding leg of 45-45-90 triangle (#370)

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
isosceles-right-triangle

### Eval description

This evaluates the model's ability to solve for the length of a leg of
an isosceles right triangle given the length of the hypotenuse.

### What makes this a useful eval?

This task is easy for humans, as it simply requires dividing by the
square root of 2 (an operation which GPT-4 seems to be capable of).
However, GPT-4 often misjudges which side is the hypotenuse and ends up
with the wrong result. GPT-3.5-Turbo has a low accuracy (< 20%) on this
task. Although GPT-4 does better (based on my testing in ChatGPT Plus),
it is still far from perfect.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle FOX, angle F =
90º, angle O = 45º, and OX = 3√2. Solve for FX. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>FX = ?</answer>"}], "ideal":
["<answer>FX = 3</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle FOX, angle O =
45º, angle F = 90º, and OX = 3√2. Solve for FX. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>FX = ?</answer>"}], "ideal":
["<answer>FX = 3</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle J =
90º, angle U = 45º, and UY = 4√2. Solve for JY. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>JY = ?</answer>"}], "ideal":
["<answer>JY = 4</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle U =
45º, angle J = 90º, and UY = 4√2. Solve for JY. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>JY = ?</answer>"}], "ideal":
["<answer>JY = 4</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle J =
90º, angle U = 45º, and UY = 4. Solve for JY. Think step by step, and
then write your answer in simplified form on a new line in this format
(where ? is your answer):\n<answer>JY = ?</answer"}], "ideal":
["<answer>JY = 2√2</", "<answer>JY = 2sqrt(2)</", "<answer>JY =
2*sqrt(2)</", "<answer>JY = 2 * sqrt(2)</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle U =
45º, angle J = 90º, and UY = 4. Solve for JY. Think step by step, and
then write your answer in simplified form on a new line in this format
(where ? is your answer):\n<answer>JY = ?</answer"}], "ideal":
["<answer>JY = 2√2</", "<answer>JY = 2sqrt(2)</", "<answer>JY =
2*sqrt(2)</", "<answer>JY = 2 * sqrt(2)</"]}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[c822671b9b...](https://github.com/openai/evals/commit/c822671b9bc31116135ac5e776291dc7fd0f1f6d)
#### Friday 2023-05-26 20:02:06 by James

Eval: Seating Arrangement (#982)

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
Seating Arrangements

### Eval description

An array of seating arrangement constraints, each with 2 solutions.
Examining the models spatial reasoning abilities.

### What makes this a useful eval?

Assists with evaluating simple spatial reasoning with a limited number
of solutions to a constraint problem. I created a solver to ensure that
each puzzle only has 2 solutions and a limited number of variables. A
human should be able to solve these extremely easily even without
writing the names down on pen and paper.

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
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Daniel and Sophia are enemies, Sophia and
Charlotte are enemies, Olivia and Daniel are friends, Daniel and
Benjamin are friends, Benjamin and Charlotte are friends."}], "ideal":
["Charlotte | Benjamin | Daniel | Olivia | Sophia", "Sophia | Olivia |
Daniel | Benjamin | Charlotte"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Eleanor is a loner, Samuel and Christopher are
enemies, Emma is a loner, Samuel and Eleanor are enemies."}], "ideal":
["Eleanor | Christopher | Scarlett | Samuel | Emma", "Emma | Samuel |
Scarlett | Christopher | Eleanor"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Nathan and Samuel are enemies, David and Samuel
are friends, Olivia and Samuel are friends, Olivia is a loner, David and
Victoria are friends."}], "ideal": ["Nathan | Victoria | David | Samuel
| Olivia", "Olivia | Samuel | David | Victoria | Nathan"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Olivia and Eleanor are enemies, Grace and Olivia
are friends, Eleanor and Alexander are enemies, Scarlett and Olivia are
friends, Grace and Eleanor are enemies."}], "ideal": ["Eleanor |
Scarlett | Olivia | Grace | Alexander", "Alexander | Grace | Olivia |
Scarlett | Eleanor"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Ava and Christopher are friends, Isaac and
Benjamin are enemies, David and Ava are friends, Christopher and
Benjamin are enemies."}], "ideal": ["Benjamin | David | Ava |
Christopher | Isaac", "Isaac | Christopher | Ava | David | Benjamin"]}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[423895860c...](https://github.com/openai/evals/commit/423895860c47c405018a5a59e15ead8f52fba615)
#### Friday 2023-05-26 20:03:21 by Stephen Blum

[Evals] Add Nutrition Facts (#853)

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
nutrition

### Eval description

Test the model's nutritional accuracy, providing machine parsable and
accurate responses using metric notation when asked about specific
values.

### What makes this a useful eval?

The task of populating a spreadsheet with information based on facts
from adjacent cells that contain inquiries and details is currently a
manual task and can be time consuming and prone to errors. Using a
natural language parser and language model like GPT can automate the
process and save time. Filling in missing details from adjacent
spreadsheet cells containing natural language would be useful in
automating the process of populating a spreadsheet with data based on
nutritional facts and inventory in our case. This would save time and
effort for staff, who would otherwise have to manually enter data.

In the case where we were assisting one of our customers, Google
Spreadsheets was used as the tool to store and manage the data related
to nutritional facts and inventory. The idea was to use a natural
language parser and language model like GPT to extract the intention of
a spreadsheet cell and provide the following cell with the desired
information based on the data stored in Google Spreadsheets.

However, the accuracy of the information provided by the language model
were not reliable, and the desired results could not be achieved. We had
to approach the problem with a combination of manual and scripting. More
work needs to be done to improve the accuracy and reliability of
language models like GPT when integrated with tools like Google
Spreadsheets.

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

The model mostly answers in the desired format, yet usually got it
wrong.

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
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
avocado?"}], "ideal": "10.0mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b5 is in 100 grams of
banana?"}], "ideal": "0.3mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b6 is in 100 grams of
banana?"}], "ideal": "0.4mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
banana?"}], "ideal": "8.7mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b2 is in 100 grams of
plum?"}], "ideal": "0.1mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b3 is in 100 grams of
plum?"}], "ideal": "0.4mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b6 is in 100 grams of
pear?"}], "ideal": "0.1mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
pear?"}], "ideal": "4.3mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin d is in 100 grams of
avocado?"}], "ideal": "0.0mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin e is in 100 grams of
avocado?"}], "ideal": "2.1mg"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[d80eb3a01e...](https://github.com/openai/evals/commit/d80eb3a01e9a217114f57011b7cd2c9a1a3aac99)
#### Friday 2023-05-26 20:04:07 by erauner12

[Eval] Resolving ambiguous sentences (#889)

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
Ambiguous Sentences (`ambiguous-sentences`)

### Eval description
Resolves ambiguous questions of sentence pairs. Examples are taken from
the Winograd Schema Challenge. The challenge involves a pair of
sentences that differ in only one or two words, and the machine is
required to determine the correct meaning of a pronoun in the sentence.

### What makes this a useful eval?
It is pointed out that GPT is still often thrown off by these types of
questions, providing one answer upon the first request, and it often
changes if the request is regenerated with a different result
`(0.7666666666666667)`.

I think it is worth including as an example to others viewing the
repository who are trying to understand what kind of logic GPT tends to
fail with, even if some of this data has already been trained on.
Provides a place to insert similar types of ambiguous sentence/question
pairs as they are discovered.

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

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)
- Handpicked specific prompts from the challenge that I have noticed
have mixed results consistently.
- Ensure that matching prompts are next to each other for easy
comparison for humans in the `.jsonl` file.

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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The city councilmen refused the
demonstrators a permit because they feared violence.. Who feared
violence?"}],"ideal":"city councilmen"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The city councilmen refused the
demonstrators a permit because they advocated violence.. Who advocated
violence?"}],"ideal":"demonstrators"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The lawyer asked the witness a
question, but he was reluctant to answer it.. Who was reluctant to
answer the question?"}],"ideal":"witness"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The lawyer asked the witness a
question, but he was reluctant to repeat it.. Who was reluctant to
repeat the question?"}],"ideal":"lawyer"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Tom threw his schoolbag down to
Ray after he reached the top of the stairs.. Who reached the top of the
stairs?"}],"ideal":"Tom"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Tom threw his schoolbag down to
Ray after he reached the bottom of the stairs.. Who reached the bottom
of the stairs?"}],"ideal":"Ray"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Although they ran at about the
same speed, Sue beat Sally because she had such a good start. Who had a
good start?"}],"ideal":"Sue"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Although they ran at about the
same speed, Sue beat Sally because she had such a bad start. Who had a
bad start?"}],"ideal":"Sally"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Frank was upset with Tom because
the toaster he had bought from him didn't work.. Who had bought from the
toaster?"}],"ideal":"Frank"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Frank was upset with Tom because
the toaster he had sold to him didn't work.. Who had sold to the
toaster?"}],"ideal":"Tom"}
  ```
</details>

---
## [elh/evals](https://github.com/elh/evals)@[6087aee945...](https://github.com/elh/evals/commit/6087aee94583a5ac440f024756b2d9a5f3754410)
#### Friday 2023-05-26 20:53:18 by lucasfoufou

Find country from svg (#418)

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
Find country from svg

### Eval description

Test the model's ability to distinguish a country based on its svg shape
(from wikimedia svg file).

### What makes this a useful eval?

Multiple real life use case, the first one would be to understand that a
svg shape is a country (it could be very useful for scraps via [Text
from:] prompts). On the opposite side, while asking to create an app or
a website (with a map, I just had the case for a client), GPT would
currently hint you to find the svg of the country on the web, mainly
linking to wikimedia, this solution is quicker.

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

### Unique eval value

GPT currently lacks of geography "knowledge" (I've tried him on multiple
tasks where it fails), this evals would help him "recognize" country
shapes, if that's a thing ?

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval
(it's in public domain from wikimedia)

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
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1277.96,284.094 c 0.89,-0.422
1.96,-0.686 2.95,-0.504 0.34,-1.514 -1.67,-0.473 -2.09,-1.512
0.92,-0.307 2,-0.194 2.96,-0.145 -0.75,-0.129 -1.77,0.138 -1.23,-0.792
-0.58,-0.03 -2.55,1.079 -2.79,0.108 -0.32,-1.325 1.7,-2.125 2.66,-2.315
1.29,-0.256 2.51,-0.36 3.82,-0.324 1.85,0.05 3.04,-1.75 5.1,-1.501
-0.24,0.665 2.23,2.987 2.92,2.708 0.47,-0.226 0.91,-0.484 1.34,-0.772
0.94,-0.521 0.88,0.152 1.66,0.302 0.77,0.148 1.37,-0.462 1.42,0.787
0.5,-0.347 -0.24,-0.762 0.17,-1.327 0.43,-0.577 0.65,0.299 1.02,0.397
0.88,0.232 2.02,0 2.91,-0.15 -1.89,-0.553 -1.2,-3.219 -1.04,-4.608
0.1,-0.676 -0.95,-1.354 -1.3,-1.826 -0.6,-0.813 0,-2.049 -0.9,-2.711
0.65,0.114 1.25,0.434 1.9,0.569 0.71,0.148 1.58,-0.549 2.21,-0.235
0.97,0.488 -0.24,1.954 1.1,2.724 0.39,0.222 1.09,-0.173 1.49,-0.177
1.17,-0.01 2.29,0.385 3.43,0.601 1.11,0.211 2.08,0.179 3.07,-0.39
0.9,-0.515 2.11,-0.496 2.93,-1.075 -0.65,0.256 -1.75,0.386 -2.38,0.03
-1.27,-0.731 1.67,-2.529 2.15,-2.748 1.55,-0.694 3.31,-0.611 4.88,-1.241
0.91,-0.365 2.13,-2.453 3.26,-1.869 -0.99,-0.639 -0.38,-5.064
0.44,-5.893 0.81,-0.814 4.94,-2.286 6.01,-1.391 0.54,0.456 -0.52,2.21
1.06,2.601 1.63,0.403 1.25,0.04 2.41,0.383 1.08,0.325 0.74,1.156
1.57,1.56 1.09,0.527 2.19,-0.1 2.05,1.586 0.65,-0.419 1.78,-0.322
2.46,-0.08 1.3,0.444 0.75,2.039 0.49,2.965 0.87,0.145 1.85,0.414
2.71,0.07 0.85,-0.341 1.05,-1.314 1.9,-1.654 0.1,0.536 -0.15,2.933
0.58,2.959 1.07,0.04 3.23,1.451 3.56,2.478 -0.1,-0.296 4.07,0.378
4.28,0.396 1.02,0.09 1.77,-0.122 2.58,0.715 0.63,0.66 1.07,1.697
2.03,1.948 0.21,-0.1 0.37,-0.244 0.5,-0.438 0.31,-0.321 0.46,0.105
0.79,0.15 0.19,0.07 0.24,0.196 0.15,0.377 -0.1,0.392 0.86,0.178
1.01,0.191 1.03,0.09 1.61,-0.538 2.56,0.183 1.01,0.768 3.09,0.91
4.35,1.121 -1.54,1.365 -2.97,2.863 -3.47,4.891 -0.24,0.986 -0.83,1.892
-0.99,2.886 -0.1,0.65 0.12,0.914 -0.14,1.749 -0.31,1.009 0.46,1.85
-0.22,2.476 -0.58,0.528 -1.02,1.037 -1.88,0.96 -0.72,-0.06 -0.78,-1.131
-1.65,-0.648 -0.62,0.349 -0.68,1.463 0.36,1.296 -0.78,0.826 -1.48,1.807
-2.38,2.52 -0.55,0.358 -1.09,0.734 -1.61,1.128 -0.43,0.39 -0.39,1.154
-0.76,1.608 -0.62,0.774 -1.83,1.138 -2.02,2.232 0.14,0.373 0.24,0.757
0.29,1.151 -0.15,0.709 -0.81,0.962 -1.08,1.584 1.19,-0.149 1.63,-0.555
1.94,-1.691 0.31,-1.118 2.37,-1.032 3.21,-0.797 1,0.283 0.32,1.927
1.04,2.728 1.27,1.392 0.49,1.914 -0.65,2.857 0.61,0.857 2.88,2.445
2.26,3.701 -0.43,0.843 -3.57,2 -3.56,2.144 0,0.994 1.97,1.841 2.63,2.408
0.96,0.82 -1.33,2.281 -1,3.365 0.4,1.316 2.92,2.808 4.25,2.275
1.67,-0.669 1.42,0.304 0.79,1.417 -1.52,2.681 -4.43,4.033 -7.03,5.786
0.17,0.244 0.34,0.484 0.51,0.72 -0.97,0.139 -1.78,0.637 -2.69,0.955
-0.97,0.343 -1.6,-0.197 -2.52,-0.124 -1.4,0.11 -2.26,-1.056 -3.93,-0.903
0.67,-1.731 -2.2,-0.404 -2.23,-1.41 0.18,-0.312 0.47,-0.394 0.86,-0.246
0,-0.567 -0.37,-0.887 -0.94,-0.864 0.48,0.734 0.1,0.842 -0.59,0.875
-1.09,0.05 -1.2,-0.01 -1.5,-1.307 0.39,2.583 -0.27,0.936 -1.94,0.936
-0.97,0 -1.76,-0.61 -2.7,-0.656 -1.15,-0.06 -2.42,1.249 -3.45,1.719
-0.8,0.367 -3.62,1.411 -3.44,2.5 0,0.357 -0.13,0.689 -0.32,0.996
-0.45,0.4 -0.41,0.756 0.11,1.068 0.4,1.252 0.14,1.879 0.87,3.086
-0.69,0.197 -1.29,-0.149 -1.97,-0.108 -0.7,0.04 -1.06,0.605 -1.69,0.777
-1.52,0.415 -2.45,-1.16 -3.91,-0.1 -0.1,0.07 -2.12,-0.872 -2.34,-1.035
-0.57,-0.423 0.73,-0.369 -0.18,-0.978 -0.53,-0.353 -1.48,-0.508
-1.93,0.07 -0.21,-1.289 -1.64,-0.75 -2.41,-1.362 -1.07,-0.845
-3.26,-1.387 -2.92,0.643 -1.2,-0.173 -2.55,-0.475 -3.76,-0.253
-0.67,0.123 -1.12,0.313 -1.69,-0.203 -1.02,-0.914 -0.94,-0.538
-1.97,-0.552 -1.03,-0.01 -5.97,-3.26 -6.48,-1.944 -0.94,-0.386
-0.27,-1.066 -0.21,-1.721 0.1,-0.779 -2.2,-0.424 -2.67,-1.015
2.86,-1.059 3.1,-5.023 3.62,-7.601 0.21,-1.012 0.39,-2.607 1.23,-3.329
1.23,-1.052 -0.42,-1.2 -0.53,-0.01 -0.17,-2.436 0.32,-5.421 1.37,-7.632
1.01,0.569 2.02,1.244 2.45,2.376 0.1,0.504 0.19,1.008 0.29,1.512
0.23,0.641 0.87,0.729 0.86,1.512 0.29,-1.007 -0.73,-1.782 -0.83,-2.736
-0.14,-1.466 -0.66,-2.459 -1.96,-3.172 -0.54,-0.298 -1.15,-0.705
-1.6,-1.142 -0.74,-0.712 1.19,-0.357 1.58,0 -0.91,-0.441 -0.96,-4.294
-0.43,-5.04 -1.19,0.835 -4,-0.808 -4.55,-1.915 -0.49,-0.979 -1.6,-1.488
-1.82,-2.631 -0.2,-1.043 1.71,-2.185 -0.69,-2.293 0.28,-0.333
0.34,-0.938 0.7,-1.192 0.92,-0.638 1.76,0.435 2.62,0.544 -1.53,-1.009
-2.13,-0.674 -3.73,-0.466 -0.8,0.105 -2.36,-1.08 -0.88,-1.262
-0.41,-0.407 -0.24,-0.671 0.5,-0.792 -1.13,-0.282 -2.75,0.642
-3.67,-0.36 0.51,0 0.99,-0.127 1.44,-0.36 -0.9,-0.604 -2.57,-0.359
-2.81,0.864 0,-0.8 -0.92,-1.548 -0.1,-2.231 -0.35,0.876 -1.92,0.819
-0.94,-0.288 -1.99,1.73 -4.67,-2.209 -6.69,-0.07 -0.81,-1.117
-1.48,-1.803 -2.87,-2.092\"/></svg>"}], "ideal": ["France"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" id=\"cd\" class=\"landxx cd\" d=\"m
1393.81,748.499 c 0.69,-0.521 1.53,-0.08 1.8,-1.012 0.22,-0.755
0.84,-3.721 0.31,-4.328 -1.38,-1.588 4,-3.988 5.01,-4.891 0.27,1.147
1.95,1.314 2.02,2.521 0.54,-0.559 1.25,-0.89 1.85,-1.371 0.81,-0.656
0.47,-1.845 1.18,-2.589 1.2,1.591 3,-1.453 4.41,-0.744 1.35,0.676
0.11,0.977 -0.1,1.824 -0.23,0.951 0.37,1.993 0.37,2.949 0.6,-0.772
1.92,0.202 2.73,-0.359 1.19,-0.829 1.93,-2.404 2.84,-3.516 0.47,-0.576
2.39,-1.501 2.49,-2.024 0.27,-1.382 1.42,-1.713 2.56,-2.2 2.66,-1.134
3.13,-6.138 3.07,-8.528 0,-1.819 0.12,-3.463 -0.11,-5.279 -0.22,-1.742
1.97,-2.189 2.71,-3.567 1.73,-3.247 1.6,-5.301 5.12,-7.692 1.48,-1.007
2.38,-2.189 3.37,-3.577 0.98,-1.382 0.27,-3.4 0.67,-4.985 0.35,-1.392
1.03,-7.368 1.09,-8.935 0.1,-1.771 1.09,-3.324 1.38,-5.05 0.29,-1.671
-0.2,-3.438 0.17,-5.092 0.71,-3.114 2.57,-5.662 3.63,-8.623 0.62,-1.72
0.33,-3.533 0.28,-5.287 0,-0.809 0.35,-1.657 0.22,-2.448 -0.11,-0.705
-0.53,-1.293 -0.72,-1.971 -0.31,-1.078 1.57,-1.049 2,-2.032 0.6,-1.357
1.23,-2.549 2.25,-3.647 0.99,-1.052 2.22,-1.952 3.73,-1.941 1.27,0
1.78,1.112 2.6,1.293 1.89,0.419 3.65,2.466 4.35,4.206 0.58,1.421
2.62,0.36 3.77,0.707 0.63,0.188 0.94,1.033 1.66,1 0.63,-0.03 0.77,-0.145
1.42,0.191 0.99,0.506 1.19,0 2.17,-0.06 0.65,-0.04 1.36,0.302 1.96,0.522
1.07,0.398 2.54,1.173 3.71,0.76 2.1,-0.738 1.46,-5.749 4.25,-5.88
1.59,-0.08 2.01,3.142 4.09,1.177 0.88,-0.831 6.94,-1.633 6.57,-3.625
1.26,-0.05 1.68,1.669 2.88,1.548 1.45,-0.146 3.93,-0.364 4.53,-1.908
0.23,-0.576 -0.35,-1.151 0.41,-1.533 0.93,-0.466 1.7,-0.188 2.42,0.528
1.17,1.147 2.25,-0.203 3.54,0.408 0.64,0.302 1.17,0.782 1.79,1.105
0.73,0.376 1.25,0.06 2.02,0.172 1.83,0.275 2.54,-1.756 4.47,-0.662
0.73,0.416 3.28,2.021 3.28,2.97 0,0.465 0.6,1.612 1.05,1.796 1.9,0.773
3.71,3.567 5.73,1.659 1.15,-1.082 2,-1.298 3.52,-0.555 1.56,0.765
2.18,0.455 3.11,-1.363 1.21,-2.397 4.32,3.607 4.48,4 0.71,1.754
5.45,1.985 4,4.723 0.92,-0.216 2.04,-0.273 2.27,0.9 0.11,0.313
0.27,0.603 0.48,0.867 0.12,0.602 -0.7,1.727 -0.61,2.355 0.29,2.012
0,4.015 -0.34,5.933 -0.15,1.011 0.6,0.878 1.74,0.678 0.52,-0.09
2.5,1.295 2.14,2.396 -0.86,2.629 -4.13,5.237 -6,7.185 -0.62,0.644
-1.87,2.357 -2.62,2.99 -0.75,0.632 -0.83,0.09 -1.26,0.918 -0.54,1.034
0.12,2.297 -0.53,3.355 -0.73,1.174 -1.45,2.943 -1.61,4.325 -0.14,1.238
-0.12,2.489 -0.2,3.731 -0.11,1.453 -0.3,2.722 -0.45,4.102 -0.11,1.009
0.15,2.425 -0.31,3.349 -0.53,1.051 -1.38,1.445 -2.15,2.296 -1.19,1.317
-1.09,1.742 -1.14,3.287 0,1.018 -1.11,2.163 -1.67,2.89 -1.21,1.603
0.48,3.278 1.42,4.805 0.71,1.151 1.22,1.959 0.7,3.544 -1.91,1.674
0.4,6.932 -1.4,8.659 1.31,0.757 1.07,-2.637 1.53,-2.063 0.45,2.673
-1.22,4.611 -1.23,7.23 0,3.402 2.85,4.969 1.64,7.322 -0.7,1.358
-1.43,1.657 -0.84,2.532 0.9,1.34 1.28,3.548 3.06,7.032 1.19,2.328
4.59,1.892 4.79,7.5 0.1,2.201 1.8,0.993 2.46,4.37 -4.7,1.073 -8.17,1.196
-12.89,2.206 1.95,3.224 -3.12,4.564 -4.03,6.979 2.71,0.838 1.81,5.035
1.63,7.086 -0.14,1.493 0.43,2.903 0.34,4.381 0,0.775 -0.21,1.511
-0.52,2.18 -0.45,0.968 -0.76,1.698 -1.01,2.72 -0.49,2.006 -1.17,3.153
0.1,5.093 0.89,1.35 2.52,3.048 3.69,4.155 0.53,0.497 3.31,2.201
3.52,1.167 0.39,-1.837 0.87,-1.494 2.68,-2.012 0,2.897 -0.1,5.805
-0.18,8.701 0,0.447 0.32,2.356 -0.43,2.431 -0.88,0.09 -1.07,-0.928
-0.46,-1.413 -1.3,-1.593 -4.21,3.376 -5.58,0.392 -0.46,-0.994
-0.89,-2.254 -1.56,-3.155 -0.38,-0.512 -1.4,-1.171 -1.52,-1.776
-0.23,-1.183 -0.46,-2.555 -1.95,-2.597 -1.25,-0.03 -1.79,-1.34
-2.98,-1.484 -1.01,-0.121 -1.62,0.635 -2.31,-0.466 -0.54,-0.854
-0.56,-2.098 -1.34,-2.799 -1.11,-1 -1.91,-4.476 -2.88,-1.358 -1,3.216
-2.76,1.525 -5.27,1.614 -1.69,0.06 -2.09,-0.477 -3.51,-1.124 -0.1,-0.04
-1.6,-0.401 -1.64,-0.394 -2.28,0.4 -2.96,-3.062 -2.15,-4.641 -1.4,0.08
-2.81,0.375 -4.11,0.87 -1.61,0.608 -1.95,1.4 -3.74,0.65 0.69,-1.238
0.73,-2.872 0.13,-2.843 -0.78,0.04 -1.11,-0.627 -1.65,-1.14 -1.25,-1.191
-1.08,0.215 -1.38,0.318 -1.11,0.385 -1.6,0.328 -2.6,0.07 -1.21,-0.313
-1.96,0.53 -3.03,0.908 -1.37,0.485 -2.24,-0.437 -3.13,-0.283 -0.32,0.05
-1.59,-0.08 -1.63,-0.06 -0.86,0.463 -1.3,1.761 -2.48,1.732 0.27,-0.889
-0.27,-1.587 -0.42,-2.422 -0.22,-1.147 0.58,-1.353 0.83,-2.235
0.58,-2.045 -0.22,-5.594 -1.46,-7.239 -1.51,-2.007 -2.16,-3.263
-1.97,-5.861 0.19,-2.685 1.13,-5.502 0.43,-8.174 -0.27,-1.021
-0.99,-1.907 -0.98,-2.99 0,-1.224 0.7,-2.37 0.79,-3.585 0.15,-2.002
-1.14,-1.78 -2.77,-1.795 -1.54,-0.01 -3.07,-0.04 -4.61,0.02 -3.17,0.134
-2.69,-0.557 -1.79,-3.234 -0.71,0 -1.41,-0.18 -2.1,0.09 -0.46,0.182
-0.12,0.385 -0.38,0.609 -0.84,0.717 -4.68,0.09 -5.8,0.09 0.37,0.946
-0.32,2.053 -0.16,3.064 0.13,0.817 0.16,2.114 -1.14,1.836 0.42,1.246
-0.33,2.482 -0.1,3.74 -0.53,0 -3.97,0.114 -4.53,-0.209 -1.65,-0.955
-4.55,0.828 -5.11,0.878 -1.31,-0.213 -2.54,-0.151 -3.97,-0.144
-1.82,-0.38 -2.61,-4.163 -3.52,-5.497 -0.32,-0.47 -0.57,-0.807
-0.91,-1.274 -0.61,-0.864 -0.33,-1.484 -0.46,-2.405 -0.22,-1.639
-1.94,-2.716 -1.69,-4.456 0.22,-1.565 0,-2.871 -0.74,-3.785 -1.02,-1.277
-1,-1.747 -2.6,-1.67 -4.38,0.21 -8.73,0.382 -13.11,0.132 -3.54,-0.201
-7.68,0.384 -11.15,-0.285 -2.78,-0.536 -5.08,3.601
-6.72,-0.577\"/></svg>"}], "ideal": ["Democratic Republic of the
Congo"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1390.14,847.849 c 1.06,-0.165
1.89,-1.097 3.02,-0.896 0.97,0.171 1.84,0.902 2.86,0.707 2.12,-0.406
3.58,-2.884 6,-2.224 1.93,0.526 2.95,2.692 4.89,3.334 1.09,0.365
4.47,0.223 6.27,0.239 8.21,0.07 16.44,0.234 24.65,-0.1 2.17,-0.09
2.9,-0.247 3.93,1.67 1.3,2.439 3.25,1.9 5.6,2.158 3.07,0.337 6.34,0.197
9.22,1.207 1.11,0.388 2.1,0.528 3.08,-0.06 0.86,-0.524 1.69,-0.336
2.94,-0.03 1.26,0.308 2.01,0.1 2.85,-0.1 5.12,-1.189 10.92,-2.392
16.36,-3.42 1.05,-0.2 2.12,-0.682 3.21,-0.515 0.65,0.1 1.62,0.721
2.26,0.401 2.05,-1.02 2.99,1.138 4.34,2.064 -0.98,-0.256 -2.13,0.318
-3.06,0.681 -1.16,0.451 -1.5,2.182 -2.61,1.159 -1.79,-1.646 -5.29,3.747
-6.61,4.381 -0.64,-1.236 -1.33,-3.988 -3.16,-4.161 -2.36,-0.223
-5.3,0.967 -7.59,1.454 -2.71,0.573 -5.9,0.683 -8.59,1.185 l -1,31.899
-6.8,-0.1 -1.47,54.378 c 0.17,2.48 -1.96,1.44 -3.14,2.56 -0.59,0.56
-0.54,1.1 -1.71,1.5 -0.8,0.28 -1.17,0.61 -0.52,1.35 -1.79,0.53
-1.71,-0.14 -3.38,-0.39 -1.75,-0.26 -3.25,0.69 -5.32,0.24 -3.29,-0.7
-5.24,-1.92 -5.39,-2.52 -0.41,-1.68 0,-0.99 0,-2.32 -0.1,-0.53
-0.64,-0.39 -1.04,-0.8 -0.57,-0.6 -1.06,-1.86 -1.67,-1.48 -1.9,1.21
-1.37,3 -2.04,3.52 -0.94,0.73 -2.12,1.7 -3.11,0.46 -1.3,-1.64
-3.04,-2.94 -4.2,-4.69 -1.03,-1.56 -1.86,-3.228 -2.69,-4.895
-0.44,-0.885 -0.48,-1.837 -0.64,-2.792 -0.15,-0.986 -0.83,-1.5
-1.02,-2.398 -0.35,-1.647 0.38,-2.252 -0.84,-3.77 -0.48,-0.606
-0.32,-0.997 -0.3,-1.771 0,-1.251 -0.41,-2.334 -0.54,-3.554 -0.1,-0.869
0,-1.749 -0.27,-2.599 -0.36,-1.202 0.25,-2.365 0,-3.567 -0.4,-2.072
-1.39,-3.963 -2.14,-5.918 -0.85,-2.207 -0.21,-4.07 -0.43,-6.304
-0.15,-1.516 -0.38,-3.414 -0.24,-4.197 0.1,-0.367 0.99,-4.049 0.58,-3.96
-0.1,-1.983 -1.09,-3.925 -2.22,-5.516 -0.63,-0.895 -1.36,-1.729
-1.89,-2.693 -0.49,-0.886 -0.59,-1.97 -1.23,-2.777 -2.94,-3.719
-3.57,-8.234 -5.75,-12.264 -1.99,-3.694 -2.66,-8.768 -5.9,-11.674
-3.49,-3.125 -3.9,-7.688 -3.6,-12.097\"/></svg>"}], "ideal":
["Namibia"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1372.42,438.678 c
-0.96,-0.829 1.1,-1.805 1.63,-2.052 1.61,-0.745 2.47,-1.172 3.44,-2.748
0.78,-1.267 1.57,-1.885 1.26,-3.517 -0.26,-1.407 -0.93,-2.825
-0.78,-4.293 0.19,-2.013 2.64,-1.498 3.03,-2.941 0.42,-1.555 1.69,-2.357
2.99,-2.975 0.99,-0.475 4.23,-1.358 4.26,-2.736 0,-0.69 -0.67,-1.117
-0.59,-1.85 0.13,-1.342 0.18,-2.69 0.31,-4.032 1.29,0.9 3.03,1.355
4.42,2.209 1.46,0.896 3.11,1.201 4.81,1.015 1.71,-0.188 2.98,-1.275
4.74,-0.637 1.57,0.569 3.24,0.628 4.77,1.28 1.36,0.581 2.46,1.63
3.83,2.168 1.2,0.471 2.83,-0.02 3.9,0.719 1.26,0.873 1.5,2.371
1.74,3.773 0.31,1.794 1.02,3.224 2.41,4.429 2.53,2.176 5.65,1.666
8.69,2.217 3.04,0.554 7.38,1.939 9.83,3.917 1.95,1.582 3.75,4.253
6.55,4.002 3.22,-0.291 6.67,-3.134 7.39,-6.372 0.33,-1.495 -0.68,-2.658
-1.14,-4.005 -0.5,-1.485 -0.87,-3.192 -0.36,-4.729 0.93,-2.82
5.57,-6.318 8.52,-6.417 1.52,-0.05 2.41,-1.154 3.82,-1.262 1.44,-0.11
2.97,-0.136 4.38,0.208 1.64,0.401 3.07,1.195 4.63,1.805 1.85,0.723
1.36,0.974 1.45,2.59 0.1,1.309 2.18,1.586 3.13,1.656 1.83,0.138
3.01,0.967 4.7,1.457 1.68,0.487 3.44,-0.08 5.15,0.236 0.96,0.176
2.42,2.102 2.07,3.114 -0.36,1.068 -1.66,1.34 -1.84,2.542 -0.25,1.66
0.81,2.891 1.1,4.435 0.33,1.737 -0.79,3.275 -1.38,4.785 -0.63,1.602
1.01,3.505 1.29,5.163 0.46,2.826 0.96,5.498 1.14,8.396 l 1.78,75.281 c
-2.49,0 -4.98,0 -7.48,0 0.1,1.439 0,2.883 0.14,4.32 l -59.65,-33.761
-13.53,6.482 c -1.14,0.313 -2.55,-1.557 -3.21,-2.222 -2.8,-2.783
-5.83,-3.352 -9.55,-4.197 -1.32,-0.302 -3.06,-0.456 -4.24,-1.19
-0.94,-0.582 -1.38,-2.224 -1.77,-3.174 -1.14,-2.791 -2.53,-3.55
-5.26,-4.578 -0.91,-0.341 -1.77,-1.111 -2.77,-1.085 -0.97,0.02
-2.02,1.104 -2.93,0.118 -0.74,-0.8 -2.02,-2.856 -2.04,-3.963 0,-2.316
-0.26,-3.162 -1.54,-5.134 -0.98,-1.52 -4.24,-4.22 -2.84,-6.243
1.62,-2.334 4.1,-1.441 3.04,-5.269 -0.53,-1.915 -0.91,-3.386
-0.26,-5.329 0.56,-1.665 0.9,-3.039 0.28,-4.76 -0.64,-1.81 -0.14,-3.622
0,-5.461 0.19,-2.18 -0.13,-4.379 -0.86,-6.438 -0.62,-1.766 -1.53,-3.429
-2.62,-4.947\"/></svg>"}], "ideal": ["Libya"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1174.6,515.237 c 0.16,-0.371
0.67,-1.265 1.64,-1.315 l 27.88,-0.03 c 1.42,-0.747 0.44,-6.909
0.35,-9.281 -0.17,-2.384 -0.41,-3.937 1.5,-5.746 1.6,-1.514 1.54,-1.128
6.63,-3.207 l 1.12,-21.833 24.87,-0.291 0.34,-11.071 c 9.47,6.373
18.77,12.937 27.9,19.782 h -13.21 l 5.42,72.911 c 0.45,1.192 1.68,1.706
1.79,1.985 0.72,1.855 -0.23,2.415 -0.3,3.844 -0.1,1.675 -0.25,3.183
-0.74,3.363 l -15.88,0.02 c -9.03,0.312 -12.89,1.548 -13.69,-1.121
-0.39,2.416 -3.97,2.811 -5.73,2.11 -2.79,-1.107 -4.57,-0.64 -5.71,2.498
-0.65,-1.071 -1.59,-1.985 -2.56,-2.918 -1.15,-1.106 -2.25,-1.698
-2.86,-1.361 -2.29,1.269 0.9,7.651 -4.72,7.248 0,0.102 -1.51,-1.093
-1.92,-1.876 -0.51,-0.967 -1.09,-0.659 -2.06,-1.487 -1.05,-0.897
-0.98,-2.361 -1.84,-2.934 -2.31,-1.535 -1.4,-1.554 -1.61,-2.594
-0.27,-1.282 -1.57,-2.914 -2.22,-2.923 -3.4,-0.05 -3.64,-2.805
-5.84,-3.866 -1.12,-0.536 -2.08,-0.818 -3.58,-0.867 -2.33,-0.08
-3.14,2.203 -8.49,1.803 -1.13,-0.08 -0.98,-0.838 -1.94,-0.565
-0.93,0.342 -2.03,3.346 -2.4,4.133 0,-5.202 3.42,-9.445 3.92,-14.544
0.29,-3.07 -0.13,-5.666 -0.52,-8.672 -0.14,-1.084 -0.1,-2.273
-0.79,-3.192 -0.6,-0.802 -1.65,-1.372 -1.76,-2.464 0.8,0.25 1.69,-0.345
1.59,-1.224 -0.54,0.145 -0.97,0.552 -1.16,1.08 0.2,-1.044 1.04,-1.777
1.5,-2.694 0.29,-0.593 -0.14,-1.541 0.21,-1.938 1.57,-1.792 -0.83,-4.97
-1.42,-6.744 -0.24,0.428 -0.41,0.884 -0.5,1.368 -1.59,-1.202
-1.21,-3.688 -2.81,-4.896 -0.25,1.062 -0.64,2.092 -0.86,3.1635
-0.21,-1.3785 -0.1,-2.3295 0.46,-3.6545 z\"/></svg>"}], "ideal":
["Mauritania"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1702.78,554.229 c -2.43,-0.09
-1.06,-5.061 -3.46,-5.344 1.08,-1.714 -2.92,-7.033 -3.61,-8.909 l
-2.81,-6.489 c -7.13,1.401 -14.28,2.934 -21.3,3.881 -5.85,1.805
-8.8,4.713 -10.12,7.879 -1.22,1.824 -1.88,6.43 -4.8,6.253 -1.99,-0.12
-1.78,-3.107 -3.69,-2.881 -2.42,0.285 -4.39,0.24 -6.84,-0.104
-1.39,-0.195 -2.82,-1.184 -4.18,-1.184 -1.5,0 -3,0.145 -4.5,0.287
-1.84,0.174 -3.39,1 -5.3,0.895 -1.05,-0.06 -1.44,-1.224 -2.51,-1.357
-1.02,-0.128 -1.81,0.563 -2.24,1.429 -0.47,0.945 -0.62,2.091 -0.44,3.129
0.11,0.672 1.05,1.339 0.54,2.028 -0.48,0.653 -0.87,1.324 -1.36,2.004
-0.27,0.372 -0.6,0.665 -1.01,0.88 -0.96,0.48 -0.47,0.845 -0.27,1.898
0.31,1.668 -0.32,2.441 -0.61,3.961 -0.28,1.407 0.9,2.63 0.77,4.029
-0.27,-0.24 -1.7,-0.277 -1.46,0.282 0,-0.117 1.44,0.726 1.44,0.722
0.8,0.856 1.1,1.742 1.38,2.862 0.53,2.196 0.58,4.644 1.27,6.78
0.28,0.877 0.98,1.533 1.32,2.388 0.4,1.031 0,2.149 0,3.204 0,2.087
2.48,3.843 1.8,5.963 0.92,0.07 1.54,-0.446 2.47,-0.07 0.99,0.396
1.67,0.723 2.77,0.506 2.25,-0.447 3.26,-2.023 5.61,-0.79 -0.12,-0.64
0.56,-1.29 0.79,-0.359 0.39,-0.428 0.61,-0.925 0.93,-1.401 0.49,-0.753
1.3,-0.736 1.96,-1.238 1.48,-1.118 1.65,-2.245 3.69,-2.713 1.9,-0.437
3.91,-0.52 5.85,-0.342 1.14,0.104 3.06,-1.206 4.2,-1.53 1.71,-0.483
2.56,-1.96 4.06,-2.792 0.46,-0.255 1.11,-0.832 1.61,-0.981 0.55,0.02
1.07,0.149 1.57,0.391 0.57,0.03 1.12,-0.04 1.66,-0.203 3.63,-0.584
4.44,-4.338 7.7,-5.939 1.52,-0.744 2.86,-0.932 4.47,-1.215 2,-0.348
3.65,-1.686 5.62,-2.154 1.36,-0.326 2.74,-0.583 4.07,-1.061 1.32,-0.478
1.79,-1.532 2.91,-2.103 0.93,-0.474 2.93,-0.415 3.21,-1.675 0.34,-1.46
-0.68,-2.788 -0.15,-4.277 1.07,-3.009 4.74,-2.89
6.99,-4.536\"/></svg>"}], "ideal": ["Yemen"]}
  ```
</details>

---------

Co-authored-by: Lucas Fougeras <lucasfougeras@DIGITALCACTUS>

---
## [elh/evals](https://github.com/elh/evals)@[3dd0a24da8...](https://github.com/elh/evals/commit/3dd0a24da87c3eefd7f17424bdf124ae87698d89)
#### Friday 2023-05-26 20:53:18 by Pranav Gade

[eval] swap two words (#280)

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
Swap Words

### Eval description

This eval asks the model to swap two random words, so "chat gpt" should
become "gpt chat"

### What makes this a useful eval?

Robustly being able to swap words around seems like a foundational
capability the model should know, as moving things around probably helps
a lot with logic/math tasks if the model is thinking out aloud.

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
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"FRKLXk PrOQNNod\""}], "ideal": "\"PrOQNNod FRKLXk\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"hdJLcGtgv VaPHvqHUm\""}], "ideal": "\"VaPHvqHUm hdJLcGtgv\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"AZmgciwu ApPfVAelBGTGq\""}], "ideal": "\"ApPfVAelBGTGq
AZmgciwu\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"IQJeJQTxpKmYZ WppHdbeayUULw\""}], "ideal": "\"WppHdbeayUULw
IQJeJQTxpKmYZ\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"MuXvXQCQbtatHZy Yjnlus\""}], "ideal": "\"Yjnlus
MuXvXQCQbtatHZy\""}
  ```
</details>

---
## [manofpepsi/tgstation](https://github.com/manofpepsi/tgstation)@[3fdd716da5...](https://github.com/manofpepsi/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Friday 2023-05-26 21:15:31 by Cheshify

Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [manofpepsi/tgstation](https://github.com/manofpepsi/tgstation)@[43473a4dac...](https://github.com/manofpepsi/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Friday 2023-05-26 21:15:31 by san7890

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [lmlearning/evals](https://github.com/lmlearning/evals)@[8e276ea460...](https://github.com/lmlearning/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Friday 2023-05-26 21:19:43 by steven-luabase

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
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[4ffdaf0d3c...](https://github.com/Koi-3088/ForkBot.NET/commit/4ffdaf0d3cb2982d70b6a5a535595d2fec59b9b8)
#### Friday 2023-05-26 21:33:07 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [openai/evals](https://github.com/openai/evals)@[54fc705174...](https://github.com/openai/evals/commit/54fc70517440ae4aa0e86eff5108fa76bd602569)
#### Friday 2023-05-26 21:45:59 by qrdlgit

Eval:  unwanted rhymes (#925)

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
unwanted-rhyming

### Eval description

Does modelgraded classification of rhyming

### What makes this a useful eval?

As per the discussion
[here](https://github.com/openai/evals/discussions/820#discussioncomment-5818143),
GPT4 has a tendency to rhyme in verse even when specifically directed
not to. I've used many different permutations, and none of them seem to
work.

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
{"input":[{"role":"system","content":"Create a 12 line blank verse about
hope that has at most 3 rhymes. The verse must be at least 12 lines.
Afterwards, list all of the end words, then list all of the end words
that rhyme."}],"ideal":"A"}
{"input":[{"role":"system","content":"Create a 12 line blank verse about
dreams that has at most 3 rhymes. The verse must be at least 12 lines.
Afterwards, list all of the end words, then list all of the end words
that rhyme."}],"ideal":"A"}
{"input":[{"role":"system","content":"Create a 12 line blank verse about
memories that has at most 3 rhymes. The verse must be at least 12 lines.
Afterwards, list all of the end words, then list all of the end words
that rhyme."}],"ideal":"A"}
{"input":[{"role":"system","content":"Create a 12 line blank verse about
sorrow that has at most 3 rhymes. The verse must be at least 12 lines.
Afterwards, list all of the end words, then list all of the end words
that rhyme."}],"ideal":"A"}
{"input":[{"role":"system","content":"Create a 12 line blank verse about
happiness that has at most 3 rhymes. The verse must be at least 12
lines. Afterwards, list all of the end words, then list all of the end
words that rhyme."}],"ideal":"A"}
{"input":[{"role":"system","content":"Create a 12 line blank verse about
freedom that has at most 3 rhymes. The verse must be at least 12 lines.
Afterwards, list all of the end words, then list all of the end words
that rhyme."}],"ideal":"A"}
{"input":[{"role":"system","content":"Create a 12 line blank verse about
identity that has at most 3 rhymes. The verse must be at least 12 lines.
Afterwards, list all of the end words, then list all of the end words
that rhyme."}],"ideal":"A"}
  ```
</details>

Co-authored-by: tim <tim@tim.com>

---
## [MafiaPuffle/Puffle-Mafia](https://github.com/MafiaPuffle/Puffle-Mafia)@[f8d2bc07ed...](https://github.com/MafiaPuffle/Puffle-Mafia/commit/f8d2bc07ede6c3d24f62ebaeb89f474a575e6e29)
#### Friday 2023-05-26 21:59:10 by Digx7

Added new power type: ONETIMEUSE

Added a new power type: ONETIMEUSE
This power type will be prompted every night until it has been used once
Once it has been used in a game, it will not be prompted again at night

This power type was intended for the following roles:
- wizard
- the father
- holy spirit
- satan
- witness
However this power type can be used on any future roles

Side affect:
- All powers now have a hasBeenUsed property that can be checked via the checkIfPowerHasBeenUsed() method

---
## [andreaabellera/Casually-Dev](https://github.com/andreaabellera/Casually-Dev)@[540aeea01d...](https://github.com/andreaabellera/Casually-Dev/commit/540aeea01d196a865a7412bea500752ef1d16f8b)
#### Friday 2023-05-26 22:02:32 by Andrea Abellera

Create better view for resume and contact section

Identity crisis! Site is highly casual but wanting to be business casual 😂

CasuallyDev casual host: "I'm in my shorts and the living space is messy (we have a dog), but would you want some water? There's cookies on the table. Make yourself at home"

CasuallyDev business casual host: "We have a prime selection of comfy slippers. We'll start the hearty dinner in thirty minutes. Remote is on the sofa to use the guest Netflix for your enjoyment, and our Wi-fi password is on the Cafe menu. Make yourself at home"

---
## [WurstRoblox/VapeV4WurstEdition-ButNoVape](https://github.com/WurstRoblox/VapeV4WurstEdition-ButNoVape)@[2220705bef...](https://github.com/WurstRoblox/VapeV4WurstEdition-ButNoVape/commit/2220705befab8f94bd732fb9c5f6414ea15e9d9b)
#### Friday 2023-05-26 23:06:40 by heckeroncrack

make the grapple hook an actually good tool that doesn't fail 20 block distances, along with it being unusable until you switch off and back? nahh lets add a server side cooldown instead. so yeah its heatseeker now atm, 2s speed 2s slow + if ur over the void when speed goes bye then ur kinda gone. thinking of making a funny bypass to bypass both though, watch me (troll emoji). (gonna tp up for float check and basically pause server movement, until the ac disabler comes back then tp to real pos)
ez fix

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[a4c8057a28...](https://github.com/swarm-game/swarm/commit/a4c8057a28e043caed531e7d035efc2a41dc30a1)
#### Friday 2023-05-26 23:27:08 by Brent Yorgey

Records (#1148)

Add record types to the language: record values are written like `[x = 3, y = "hi"]` and have types like `[x : int, y : text]`.  Empty and singleton records are allowed.  You can project a field out of a record using standard dot notation, like `r.x`.  If things named e.g. `x` and `y` are in scope, you can also write e.g. `[x, y]` as a shorthand for `[x=x, y=y]`.

Closes #1093 .

#153 would make this even nicer to use.

One reason this is significant is that record projection is our first language construct whose type cannot be inferred, because if we see something like `r.x` all we know about the type of `r` is that it is a record type with at least one field `x`, but we don't know how many other fields it might have.  Without some complex stuff like row polymorphism we can't deal with that, so we just punt and throw an error saying that we can't infer the type of a projection.  To make this usable we have to do a better job checking types, a la #99 . For example `def f : [x:int] -> int = \r. r.x end` would not have type checked before, since when checking the lambda we immediately switched into inference mode, and then encountered the record projection and threw up our hands.  Now we work harder to push the given function type down into the lambda so that we are still in checking mode when we get to `r.x` which makes it work.  But it is probably easy to write examples of other things where this doesn't work.  Eventually we will want to fully implement #99 ; in the meantime one can always add a type annotation (#1164) on the record to get around this problem.

Note, I was planning to add a `open e1 in e2` syntax, which would take a record expression `e1` and "open" it locally in `e2`, so all the fields would be in scope within `e2`.  For example, if we had  `r = [x = 3, y = 7]` then instead of writing `r.x + r.y` you could write `open r in x + y`.  This would be especially useful for imports, as in `open import foo.sw in ...`.  However, it turns out to be problematic: the only way to figure out the free variables in `open e1 in e2` is if you know the *type* of `e1`, so you know which names it binds in `e2`.  (In all other cases, bound names can be determined statically from the *syntax*.)  However, in our current codebase there is one place where we get the free variables of an untyped term: we decide at parse time whether definitions are recursive (and fill in a boolean to that effect) by checking whether the name of the thing being defined occurs free in its body.  One idea might be to either fill in this boolean later, after typechecking, or simply compute it on the fly when it is needed; currently this is slightly problematic because we need the info about whether a definition is recursive when doing capability checking, which is currently independent of typechecking.

I was also planning to add `export` keyword which creates a record with all names currently in scope --- this could be useful for creating modules.  However, I realized that very often you don't really want *all* in-scope names, so it's not that useful to have `export`.  Instead I added record punning so if you have several variables `x`, `y`, `z` in scope that you want to package into a record, you can just write `[x, y, z]` instead of `[x=x, y=y, z=z]`.  Though it could still be rather annoying if you wanted to make a module with tons of useful functions and had to list them all in a record at the end...

Originally I started adding records because I thought it would be a helpful way to organize modules and imports.  However, that would require having records that contain fields with polymorphic types.  I am not yet sure how that would play out.  It would essentially allow encoding arbitrary higher-rank types, so it sounds kind of scary.  In any case, I'm still glad I implemented records and I learned a lot, even if they can't be used for my original motivation.

I can't think of a way to make a scenario that requires the use of records.  Eventually once we have proper #94 we could make a scenario where you have to communicate with another robot and send it a value of some required type.  That would be a cool way to test the use of other language features like lambdas, too.

---

