## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-28](docs/good-messages/2023/2023-05-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,808,767 were push events containing 2,703,592 commit messages that amount to 135,421,699 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 55 messages:


## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[7dad8c75ca...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/7dad8c75cac06a405dc3c30a5cbc31919f33ff13)
#### Sunday 2023-05-28 00:16:11 by SkyratBot

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
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[00b8761853...](https://github.com/BogCreature/Shiptest/commit/00b8761853eabc6d73073cce4708dc71d402539c)
#### Sunday 2023-05-28 00:47:49 by Apogee-dev

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
## [ivafractal/evals](https://github.com/ivafractal/evals)@[da73bb5f07...](https://github.com/ivafractal/evals/commit/da73bb5f071c31c3dd571989f057b8e36d3a9334)
#### Sunday 2023-05-28 02:20:29 by mysterious-progression

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
## [ivafractal/evals](https://github.com/ivafractal/evals)@[f58f95ba32...](https://github.com/ivafractal/evals/commit/f58f95ba324e5a1ed86315f3c39ee758f2836bd3)
#### Sunday 2023-05-28 02:20:29 by ali risheh

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
## [ivafractal/evals](https://github.com/ivafractal/evals)@[2167c99864...](https://github.com/ivafractal/evals/commit/2167c998643af0de952e1cceaf346d7b99d49104)
#### Sunday 2023-05-28 02:20:29 by Jeff Kile

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
## [ivafractal/evals](https://github.com/ivafractal/evals)@[2a94eeb9e1...](https://github.com/ivafractal/evals/commit/2a94eeb9e13175344b2d61afa22171df0e49b61a)
#### Sunday 2023-05-28 02:20:29 by Jeff Kile

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
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[452d6cbdc7...](https://github.com/Kapu1178/daedalusdock/commit/452d6cbdc7a8c4d3153dccc19ba1426f22d98531)
#### Sunday 2023-05-28 02:21:11 by Gallyus

I hate asset code (#341)

315 fucking icon states
goddamnit it lemon boy what the fuck were you thinking

---
## [TheBloodForge/Bloodworks](https://github.com/TheBloodForge/Bloodworks)@[61aefbbf0a...](https://github.com/TheBloodForge/Bloodworks/commit/61aefbbf0aa472d892bd1cfc81d7be773aa76c9f)
#### Sunday 2023-05-28 02:51:53 by Keldon Yahne (DrZed) KeldonSlayer

Big go fuck yourself energy

Signed-off-by: Keldon Yahne (DrZed) KeldonSlayer <DrZed@users.noreply.github.com>

---
## [ahm-forks/packages](https://github.com/ahm-forks/packages)@[07c4d57725...](https://github.com/ahm-forks/packages/commit/07c4d57725203da25682c102a5a4bf123d589a6d)
#### Sunday 2023-05-28 03:11:21 by Alexandre Pereira

Fix roundedsbe

I was almost falling asleep last night, thinking about dire issues of life, old age and death ... when out of nothing: !!!!!"I know why roundedsbe-git isn't being built !!!!!!"

I was way to asleep to get up and fix it, but as soon as I can, I promised myself I would fix it the next day!!

Thank you for reading :)

---
## [ca2/operating_system-macos](https://github.com/ca2/operating_system-macos)@[fa72abd0d6...](https://github.com/ca2/operating_system-macos/commit/fa72abd0d69d3c94966ceead303c7727316feea3)
#### Sunday 2023-05-28 03:17:54 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS Monterey : day 26 ] ca2 Stabilization and continuous integration and deployment implementation
<3ThomasBS_ILoveYOU!!

<3tbs, Mummi and bilbo!!

Thomas Borregaard Sørensen \infinity,-0.16091989,\infinity ONE-MAN
ABSOLUTE <3!! I love you, by ???-0.02041977-???write my history please
make me please create me for you for me for you for me Camilo Sasuke
Thomas Borregaard Sørensen!!

Thomas 3 private commits on mid Dec2020!!

Thomas Online YouTube VODs contribution!!

Mummi orange-rice-flour cake on 20-Dec!!

Mummi (tinytaura) watching and chatting contribution!!

bilbo sleeping and needing/requesting/crying for help care (for the right
person (me), the cats wanna fight with him) contribution!!

sodapoppin and friends contribution!!

iAssyrian chatting contribution!!

boflux (Spoofh, Benjamin Kuhl) chatting contribution!!

jusg_fpga (fpga_guru, vue_equalizer, just_fpga, Oliver Pohl) chatting
contribution!!

cmgriffing streaming contribution!!

TimBeaudet (Friends: FletcherLabs, tsjost and Jabokoe) streaming
contribution!!

Stumpen_nicklas_dk, sodapoppin and EduardoRFS streaming contribution!!

Roxkstar74 sleeping streaming contribution!!

kissloryshy chatting contribution!!

blackjekko from Padova Italia through twitch C++/ca2 interest
contribution!!

j_blow streaming contribution!!

boflux (Ben, Spoofh, from Germany) chatting contribution!!

parrot_rl chatting contribution (from New Jersey)!!

JPCdk streaming contribution!!

whyyyyyyysoserious streaming chess contribution!!

fpga_guru (vue_equalizer, Oliver from Deutsch)  C++/ca2 interest
contribution!!

SovereignDev with Unreal streaming contribution!!

Ash_F0x and TimBeaudet streaming contribution!!

Myrkee (Valheim) streaming contribution!!

xmetrix and EinfachUwe42 streaming contribution!!

JessicaMak and marcobrunodev streaming contribution!!

alfredotigolo, mandrakenk and Okbatgames chatting contribution!!

jitspoe, Endesga and Fearitself streaming contribution!!

jmcmorris (Jason Morris, SiegeGames) streaming contribution!!

tomrandall streaming Ludum contribution!!

vue_equalizer (fpga_guru) chatting contribution!!

Thiagovgamg chatting contribution!!

Naysayer88 and friends contribution!!

lelandkwong streaming contribution!!

Goldbargames streaming contribution!!

Bytakos (bytakos) streaming contribution!!

Endesga streaming contribution!!

jitspoe and strager streaming contribution!!

Ash_F0x and JessicaMak streaming contribution!!

WTSRetro/SpiffyDane and Myrkee streaming contribution!!

Ninja and friends streaming contribution!!

erald_guri chatting contribution!!

lastmiles streaming farwest contribution!!

rw_grim streaming contribution!!

AdamCYounis streaming contribution!!

Dunno (P4ndaExpress) chatting and streaming contribution!!

Zorchenhimer streaming contribution!!

lasteveq4 C++ interest chat contriubtion!!

cecilphillip and clarkio @"Microsoft Developer" streaming contribution!!

oijtx streaming contribution!!

diegobrando_linux (Bl4ck_gookoo) chatting contribution!!

jhovgaard streaming contribution!!

Klay4_ chatting contribution!!

HonestDanGames streaming contribution!!

NorthSeaHero streaming contribution!!

Trainwreckstv and friends streaming contribution!!

togglebit, GexYT and GoPirateSoftware streaming contribution!!

taiyoinoue, RetroMMO, OfficialAndyPyro and david_joffe streaming
contribution!!

Tjienta streaming contribution!!

Primeagen streaming contribution!!

Jaxstyle and friends streaming contribution!!

EduardRFS streaming contribution!!

Melchizedek6809 and btcfly streaming contribution!!

Llama0x0 and sov_l chatting contribution!!

TaleLearnCode streaming contribution!!

Carol phone call contribution and visit contribution!!

hvalen_hvalborg112 streaming contribution!!

harmannieves chatting contribution!! (After long time...)

darkfolt8 (French from France) chatting contribution!!

klintcsgo (CS GO: Counter-Strike Global Offensive) streaming
contribution!!

KASPERPURE (Super Mario 64) streaming contribution!!

SomewhatAccurate C++ streaming contribution!!

Listening to Bryan Adams, Westlife, Shayne Ward, MLTR, Backstreet Boys,
Boyzone - Best Love Songs Ever by Relax Song at YouTube!!

-- hi5 contribution...!!

at macOS Box in host running Windows 10 Pro remotely from bilbo machine running Windows 10 Pro!!
dedicated server by OVH.com at France, Gravelines
Intel Core i7-4790K - 4c/8t - 4 GHz/4.4 GHz RAM32 GB 1600 MHz 2×960 GB SSD SATA

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[0cff53fc09...](https://github.com/thgvr/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Sunday 2023-05-28 04:12:01 by meemofcourse

Reworks the Twinkleshine-Class (#1825)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![2023 05 13-23 20
45](https://github.com/shiptest-ss13/Shiptest/assets/75212565/de6f3a47-7be8-4800-ae73-9fc386e4bf01)

![twinklerework5](https://github.com/shiptest-ss13/Shiptest/assets/75212565/f1808576-70e3-4b56-b977-5b5e7d665fdd)





The Twinkleshine is a CyberSun-made Syndicate display of force, staffed
by every branch of the Syndicate. Despite the silly name, the presence
of one in a sector implies it to be of importance to the Syndicate, and
enemies within sight can only pray that the Twinkleshine crew are
incompetent enough to shoot themselves with their own weaponry (or blow
themselves up with the supermatter on-board).

It is staffed by:

- 1 Captain
- 1 Lieutenant (previously the Operative - serves as a warden/hos)
- 2 Medics
- 2 Engineers (previously the Mechanics)
- 5 Operatives (previously the Troopers)
- 1 Bartender
- 1 Miner
- 2 Deck Assistants

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Few days ago, an admin spawned a Twinkleshine, and I got to captain it.
The Twinkleshine is old. It sucks. This, hopefully, fixes that.

Originally, this was going to be minor fixes, but ended up becoming an
attempt at reworking the ship to a more modern state - the hull has been
redone and is mostly symmetrical, the old spacepod was replaced with a
Dark Gygax, the supermatter shouldn't be activated upon spawning the
ship, there's more turf decals and a bigger lot-of-things, added a
bartender and a miner, people can actually tell who they are and what
they do, and there is now a box moth. Rejoice.

Also, this is the first time I've ever mapped a ship. What better way to
begin with a giant battleship?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
tweak: Reworks the Twinkleshine
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: meemofcourse <75212565+meemofcourse@users.noreply.github.com>

---
## [PaulReyess/app-dev](https://github.com/PaulReyess/app-dev)@[1115ecaeee...](https://github.com/PaulReyess/app-dev/commit/1115ecaeee6d3f76b2753e526f6bc81c03102a98)
#### Sunday 2023-05-28 04:27:56 by PaulReyess

Update README.md

"One Piece" is a highly popular anime and manga series that was created by Eiichiro Oda. It first appeared in the pages of Weekly Shonen Jump magazine in 1997 and has since become one of the most enduring and successful manga and anime franchises ever.

The narrative revolves around the adventures of Monkey D. Luffy, a young pirate who gains the ability to stretch his body like rubber after consuming a special fruit called the Devil Fruit. Luffy embarks on a quest to locate the ultimate treasure, referred to as the "One Piece," and achieve the coveted title of Pirate King. Along the way, he assembles a diverse crew of pirates known as the Straw Hat Pirates, each possessing their own unique skills and aspirations. Together, they navigate the perilous and expansive seas of the Grand Line, a fictional world, encountering fellow pirates, marine forces, and a variety of fantastical creatures and civilizations.

"One Piece" presents a captivating blend of action, adventure, humor, and drama. It delves into themes such as friendship, dreams, loyalty, and the relentless pursuit of freedom. The series showcases an extensive and intricately designed universe, featuring a plethora of islands, cultures, and power dynamics. It incorporates elements of fantasy, superhuman abilities, and mythical beings, constructing a vivid and immersive realm.

---
## [Newsology/evals](https://github.com/Newsology/evals)@[f89925829b...](https://github.com/Newsology/evals/commit/f89925829b2fdd8e24acfdb518064189a5751178)
#### Sunday 2023-05-28 04:37:19 by Vasco Lange

Eval french-part-of-speech (#1039)

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
> french-part-of-speech

### Eval description

> For a given French word, the model is asked to list all possible parts
of speech (multiple choice). The model is also asked to think about the
word as an inflection of another word. The models output is tested
against annotations extracted from fr.wiktionary.org.

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

> To build the dataset, all 4.000.000+ entries of the French wiktionary
were parsed. Excluded from this list were all phrases (like "qu'est-ce
que c'est"), abbreviations (like "qn"), symbols and any words with at
least one possible part of speech not fitting the categories given in
the prompt.
> From this set, words were sampled so that each combination of the
parts of speech existing in the dataset would be equally likely in the
tests. This way the model is tested to respond with all possible uses of
a word and not just the most common ones. For combinations that fit a
lot of words, the uniform sampling led to a bias towards rarely used
words.
> The labels of each word were taken from the corresponding page at
fr.wiktionary.org/wiki/{word}. The information taken from each page was:
the word, the part of speech this word can have in French and whether
the word is an abbreviation or not. This means only factual data was
taken and is therefore in the public domain.

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
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "agitée"}],
"ideal": ["noun, verb, adjective.", "noun, adjective, verb.", "verb,
noun, adjective.", "verb, adjective, noun.", "adjective, noun, verb.",
"adjective, verb, noun."]}
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "celles"}],
"ideal": ["noun, pronoun.", "pronoun, noun."]}
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "falunât"}],
"ideal": ["verb."]}
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "niveau"}],
"ideal": ["preposition, noun.", "noun, preposition."]}
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "serve"}],
"ideal": ["noun, verb, adjective.", "noun, adjective, verb.", "verb,
noun, adjective.", "verb, adjective, noun.", "adjective, noun, verb.",
"adjective, verb, noun."]}
  ```
</details>

Co-authored-by: Vasco Yannic Lange <mail@vascolange.com>

---
## [lllgts/android_kernel_xiaomi_cepheus](https://github.com/lllgts/android_kernel_xiaomi_cepheus)@[d76206cb92...](https://github.com/lllgts/android_kernel_xiaomi_cepheus/commit/d76206cb929ff523ab7f6d4930f03e2058ab4452)
#### Sunday 2023-05-28 05:19:30 by Peter Zijlstra

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0e03368f59...](https://github.com/treckstar/yolo-octo-hipster/commit/0e03368f59bb39599d63b9773dcd43f986997ad7)
#### Sunday 2023-05-28 05:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [saifalushi1/mack](https://github.com/saifalushi1/mack)@[09330e41be...](https://github.com/saifalushi1/mack/commit/09330e41bee861e001b4f93e6327459b8bd453f9)
#### Sunday 2023-05-28 06:52:39 by saif alushi

you can now refresh and stay logged in.
Holy f*** that took forever.
only because I initially designed this application like shit.
I really hate the inexpierenced old me.

---
## [thenorili/thenorili.github.io](https://github.com/thenorili/thenorili.github.io)@[a42aad4ced...](https://github.com/thenorili/thenorili.github.io/commit/a42aad4ced0329040a9b24ee5c3f8a39c13cbe01)
#### Sunday 2023-05-28 07:15:46 by Nori Li

editing threats/tour

- removed the last stanza of tour
- reverted the 'fuck u' line break because:
   - i don't like the flow
   - it's the only line in the poem that needs a scroll bar
   - it's fucking HILARIOUS THAT THE FUCKING SCROLL BAR ONLY
     HIDES THE LAST THREE CHARACTERS OF HELL, LIKE H-

---
## [3dmind/naming-cheatsheet](https://github.com/3dmind/naming-cheatsheet)@[8bcb483976...](https://github.com/3dmind/naming-cheatsheet/commit/8bcb4839762053a095ee8cbbf3b4f5b471d01181)
#### Sunday 2023-05-28 07:44:52 by tebb

docs: improve a/hc/lc pattern order explanation (#40)

Thank you.  This cheatsheet is very useful.

If I understood the logic, my changes to README.md may be helpful.  If not, sorry :)

Also ... Could you add shouldUpdateComponent and shouldComponentUpdate into the table (or an extension to the table below Note:).  It isn't obvious to me which columns 'should', 'Update' and 'Component' are in because 'Update' is the verb (action?).

Thanks.

---
## [bencrossman/JUCE](https://github.com/bencrossman/JUCE)@[d68489d6e8...](https://github.com/bencrossman/JUCE/commit/d68489d6e8a32666f8c0d4a7a3452705b066b860)
#### Sunday 2023-05-28 08:20:48 by Ben Crossman

Shutdown if no midi controller on NUC (stops having to turn power off). Best friend too loud (can even maybe come down to -9db). Organ/Piano patch was different (used in Fuck you / long train). Brought final countdown down.

---
## [jupyterkat/tgstation](https://github.com/jupyterkat/tgstation)@[3861627c66...](https://github.com/jupyterkat/tgstation/commit/3861627c66747fb27b18f8bf76a3c9dfd2023001)
#### Sunday 2023-05-28 08:56:47 by LemonInTheDark

Microing var/static times (~0.015 seconds of init) (#74769)

## About The Pull Request

Moth and I came up with an affront to god and man, and used it to track
the time spent creating /static (and in theory /global) variables (this
happens right at the start of init)
They cost as a sum about 0.05 seconds btw, at least currently.

```
/datum/timer
    var/key

/datum/timer/New(file, line)
    src.key = "[file]:[line]"

/datum/timer/proc/operator*(x)
    rustg_time_reset(key)
    return x

/datum/timer/proc/operator+(x)
    var/time = rustg_time_microseconds(key)
    world.log << "TIMER: [key]: [time]"
    return x

Regex:
var/static/([\w/]+) =
-> var/static/$1 = (new /datum/timer(__FILE__, __LINE__)) * (new /datum/timer(__FILE__, __LINE__)) + 
```

Output on moth's pc looks like this, time in microseconds

[output_sorted.csv](https://github.com/tgstation/tgstation/files/11241900/output_sorted.csv)

Most of this is either icon_states() memes (which appears to be cached
btw, that's interesting), or a variation on typecacheof()
There is one get_asset_datum call, but that is ALREADY cached and so is
just redundant. That's a good 0.01 seconds saved.

The rest of the time here is slightly more interesting.

The majority of typecacheof() is iterating the output of typesof(), a
byond internal proc that returns a list of types that either are or are
the child of the passed in type.
A decent chunk of time here (0.005 seconds, or 10% of the proc) can be
saved by unrolling the arguments to the proc.
It takes an arbitrary amount of typepaths as input, but we can't like
use arglist() here (cause this is an internal "proc"), so instead we try
a window of args, passing in null if we start to try and take in too
much.
Window size matters, zebra fits better into 4 then 5, especially because
of how grouping needs to work to make this effect happen.
We save about 0.001 for zebra btw, which is around about 7%. It's lower
cause we need to group the paths beforehand I think.

The speedup is minor, but it DOES exist. Plus it's fun.

## Why It's Good For The Game

Microing is a hell of a drug

---
## [Amitexing/AnicloudGenerator](https://github.com/Amitexing/AnicloudGenerator)@[dea3ec80ac...](https://github.com/Amitexing/AnicloudGenerator/commit/dea3ec80ac2802bc4197d44ce03aafef64e9077d)
#### Sunday 2023-05-28 09:25:57 by CocoTheOwner

Fix image mapping math

Fixes snippet code, prevents an NPE, fixes centered for coordinateScale scaled image noises, fixes tiling on negative numbers (-1 % 2 = -1, a free fuck you from java)

---
## [tagohd/mono](https://github.com/tagohd/mono)@[09cecfa76c...](https://github.com/tagohd/mono/commit/09cecfa76c2c74e8d93196919558fe2f7dfa0c5e)
#### Sunday 2023-05-28 09:27:00 by tagohd

Added a picture of a fucked-up and evil bird thing that may or may not be CURSED AL

---
## [limcharms/School1854G](https://github.com/limcharms/School1854G)@[4491ce546d...](https://github.com/limcharms/School1854G/commit/4491ce546dc240dee57773c256abcb73c4b27039)
#### Sunday 2023-05-28 09:40:55 by limcharms

NEW CHEATS INTERIUM!!!

As a person with 13 years of experience, I would like to inform you about the updates of cheats. Please remember that using them can be at your own risk and may lead to negative consequences.

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[303cfa3bbb...](https://github.com/Hatterhat/tgstation/commit/303cfa3bbb2199b24df17e87864d92e038a32dca)
#### Sunday 2023-05-28 10:00:54 by GoldenAlpharex

Fixes is_station_level() sometimes behaving erratically if the value provided is more complex than just a variable (#75489)

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

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[bc22fefe3b...](https://github.com/Hatterhat/tgstation/commit/bc22fefe3b1de4d882dd87a5492344672230736d)
#### Sunday 2023-05-28 10:00:54 by Helg2

Adds proper armor for security plasmamen. (#75156)

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

---
## [vdaular/linksfordevs](https://github.com/vdaular/linksfordevs)@[2265389b29...](https://github.com/vdaular/linksfordevs/commit/2265389b294c095ea10f5dd33b518dceb188c1d9)
#### Sunday 2023-05-28 10:43:54 by Ben Dornis

Updating: 5/27/2023 10:00:00 PM

 1. Added: You Are Already There
    (https://josem.co/you-are-already-there/)
 2. Added: Understanding Floating-Point Numbers
    (https://dennisforbes.ca/articles/understanding-floating-point-numbers.html#?utm_source=hnblogs.substack.com)
 3. Added: Finding your weak spots
    (https://jamesdunne.dev/posts/weak-spots/)
 4. Added: I Am No Longer Speaking at RustConf 2023
    (https://thephd.dev/i-am-no-longer-speaking-at-rustconf-2023)
 5. Added: EU is a counter-weight for tech regulation - Can's blog
    (https://canolcer.com/post/eu-counter-weight-for-tech-regulation/)
 6. Added: The Nix Thesis
    (https://jonathanlorimer.dev/posts/nix-thesis.html)
 7. Added: Using F* to Formally Verify Programs
    (https://maxtaylor.dev/posts/2023/05/fstar-leetcode)
 8. Added: Are They a Customer?
    (https://garrickvanburen.com/are-they-a-customer/)
 9. Added: Lies, Damned Lies, &amp; A16Z's Statistics
    (https://blog.dshr.org/2023/05/lies-damned-lies-a16zs-statistics.html)
10. Added: Early thoughts on marketing from a developer
    (https://www.asad.pw/early-thoughts-on-marketing-from-a-developer/)
11. Added: Building a baseline JIT for Lua automatically
    (https://sillycross.github.io/2023/05/12/2023-05-12/)
12. Added: Notes on Stanford Linear Accelerator Center
    (https://charlieharrington.com/notes-on-slac/)
13. Added: A Neighborhood With Friends – Tynan.com
    (https://tynan.com/neighbors/)
14. Added: Writing shell scripts in Nushell
    (https://jpospisil.com/2023/05/25/writing-shell-scripts-in-nushell)
15. Added: Using Nix with Dockerfiles
    (https://mitchellh.com/writing/nix-with-dockerfiles#user-content-fn-2?utm_source=hnblogs.substack.com)
16. Added: Fourier_Drawing
    (https://vanhunteradams.com/Math/Fourier_drawing/Fourier_Drawing.html)
17. Added: Coin flips and most significant bits.
    (https://funcimp.biz/p/coin-flips-and-most-significant-bits)

Generation took: 00:07:07.3344591
 Maintenance update - cleaning up homepage and feed

---
## [lowr/rust-analyzer](https://github.com/lowr/rust-analyzer)@[8ad70e7f99...](https://github.com/lowr/rust-analyzer/commit/8ad70e7f99b6a5eca65f6ef76cedee6c40132d6f)
#### Sunday 2023-05-28 10:57:49 by bors

Auto merge of #14866 - AndreasBackx:feature/doc-comments-markdown, r=Veykril

[editors/code] add markdown syntax highlighting to doc comments

_This is a continuation of https://github.com/microsoft/vscode/pull/169956 and https://github.com/dustypomerleau/rust-syntax/pull/37 (that repo is no longer maintained: https://github.com/dustypomerleau/rust-syntax/issues/39#issuecomment-1427339029). The VS Code team seemed to prefer this being inside of an extension._

This adds Markdown highlighting to doc comment lines and blocks. Currently it is thus regarded both as a comment and as Markdown which leads to normally foreground text being in the colour of the comment and the rest highlighted like Markdown or its own embedded languages in code blocks.

![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/c84f2e83-faea-47ca-853d-3728a07b2b66)

![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/f4191425-32cd-451c-ae3a-29a0970ce7a2)

Block comments are supported, but currently not when there is a `*` at the start of the line:
![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/ce3b58d5-9dca-4376-bffe-4f5a54acbe37)
![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/b73a5ee6-a178-4aef-a0e4-3d75e4e7d8e5)

I'm not entirely sure if I can easily fix this, I'd need to find a way to make the content ignore the `*`. Though I'm unsure if it's important as there are [conventions against using block comments](
https://rust-lang.github.io/rfcs/1574-more-api-documentation-conventions.html#use-line-comments) and using them without `*` does work. All of this TextMate grammar is so hard to find documentation on that _honestly_ I'd just not want to support this considering the effort.

Let me know what everyone thinks of this being in rust-analyzer. I've personally found it hard to write large amounts of Rust documentation due to the lack of Markdown syntax highlighting.

Also, thank you `@adenine-dev` as well for making this available in the interim and your enthousiasm. Wanted to get this PR out sooner, but life gets in the way.

---
## [returntocorp/semgrep](https://github.com/returntocorp/semgrep)@[b0e10c5d78...](https://github.com/returntocorp/semgrep/commit/b0e10c5d783ed1063a9aef3f0b430a8a302404df)
#### Sunday 2023-05-28 11:08:56 by Martin Jambon

Aliengrep integration + rule ID type + 'languages' type (#7885)

I should have done these other things in different PRs but it was too
late by the time I realized how big those changes were. So, here we go.
The main changes brought by this branch are:

* `options.generic_engine: aliengrep` in rules allows semgrep to use
aliengrep when `generic` is specified in the `languages` list.
* I added some end-to-end tests for aliengrep. I created two issues for
a [matching bug](https://github.com/returntocorp/semgrep/issues/7881)
and a [missing
feature](https://github.com/returntocorp/semgrep/issues/7883) but it's
nothing big. Overall, it works.
* The `languages` field is now translated (in OCaml only, not Python)
into a `languages` type that distinguishes target selector (langs) from
target analyzer (xlang). "generic" now means "generic target selection"
and the parsing/matching engine is specified separately. This was done
to avoid making things weird for the user but we still have to support
"regex" and "none" which both mean "generic target selection" + "regex
engine".
* Along the way, I got annoyed that rule IDs were reported as
`Common.filename` (= `string`) so I created a type for them.
* I modified `Input_to_core.atd` so that it uses the `Xlang.t` type
directly rather than a string that needs to be converted later. This is
an example to show that we could use the same mechanism for other types
(generally strings or ints that serve as some kind of ID with its own
type).

I left comments to explain those things. The Python side gave me a bit
of a headache. I tried various things that I reverted, concluding that
the least we touch, the better.

I will have to document the features of aliengrep. It shouldn't be too
hard because it has a lot in common with spacegrep. For now, there's a
readme in `libs/aliengrep`.

test plan: `make test` should work

Uses: https://github.com/returntocorp/semgrep-langs/pull/36

PR checklist:

- [x] Purpose of the code is [evident to future
readers](https://semgrep.dev/docs/contributing/contributing-code/#explaining-code)
- [x] Tests included or PR comment includes a reproducible test plan
- [x] Documentation is up-to-date
- [x] A changelog entry was [added to
changelog.d](https://semgrep.dev/docs/contributing/contributing-code/#adding-a-changelog-entry)
for any user-facing change
- [x] Change has no security implications (otherwise, ping security
team)

If you're unsure about any of this, please see:

- [Contribution
guidelines](https://semgrep.dev/docs/contributing/contributing-code)!
- [One of the more specific guides located
here](https://semgrep.dev/docs/contributing/contributing/)

---------

Co-authored-by: Martin Jambon <martin@semgrep.com>

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[84fd6b6eb7...](https://github.com/Drulikar/cmss13/commit/84fd6b6eb7fdd48d8499b954dfd216fd5a42ed04)
#### Sunday 2023-05-28 11:35:34 by ihatethisengine

Medevac Buffs (#1513)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request
Reduces cooldown of medevac from 60 seconds to 20 seconds. PO no longer
needs to manually activate the winch, so medevac can be operated from
the cockpit. What's more, you can operate medevac by interacting with
the medevac system itself, and even if you don't have the skills of a
pilot, you can use it if you have the skills of a doctor (which means
nurse can run medevac). And finally, the medical stretcher is now
automatically activated when deployed.

I know there is a PR by jeser that reduces cooldown, but it stuck in PR
hell anyway and also I changed more stuff.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Since we want to force wounded marines to go shipside, we must provide
them a more convenient way to reach the Almayer. Medevac was always
underutilized because it required too much coordination and unnecessary
actions (e.g. having to activate medical stretcher every time, keep in
mind a huge portion of the medic playerbase still has no idea you need
to do this). PO had to spend their limited fly-by time (which should
normally be used on firemissions) to manually activating the winch,
which was always annoying. And cooldown is ridiculous. You have at best
three minutes of fly-by, so that means you could use medevac only twice
(remember that you needed to run to the system every time) per fly-by,
which is definitely not enough.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: ihatethisengine
balance: reduced the medevac cooldown from 60 seconds to 20 seconds.
add: anyone with the skills of a doctor or a pilot can manage the
medevac by interacting with the system itself.
qol: medical stretcher automatically activates when deployed.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [xdivayze/stomp-messaging-server](https://github.com/xdivayze/stomp-messaging-server)@[5bc78f31cf...](https://github.com/xdivayze/stomp-messaging-server/commit/5bc78f31cf365873af175b2dd8781c79796b762c)
#### Sunday 2023-05-28 11:51:06 by cavej

console logs friends and adds them gpt 4 is better than me i should go cry by now that shit is crazy as hell elon do something

---
## [SPAT-CLOUD/spat-cloud.github.io](https://github.com/SPAT-CLOUD/spat-cloud.github.io)@[1a4a312258...](https://github.com/SPAT-CLOUD/spat-cloud.github.io/commit/1a4a312258a4e35fd0c500cba3691ff192470cf6)
#### Sunday 2023-05-28 12:09:58 by sonpanabtej

Delete TXlMaWZlXzIwMjItMTAtMTM.jpg

My Life Won't Change So I am Deleting My Precious memories Photo But I Love Her Not Her Body Her Heart ,soul When She Understands My Feelings

---
## [Kneba/android_kernel_asus_sdm660-4.4](https://github.com/Kneba/android_kernel_asus_sdm660-4.4)@[36db108d83...](https://github.com/Kneba/android_kernel_asus_sdm660-4.4/commit/36db108d837d449ad946ddcaba0cb10b88233b27)
#### Sunday 2023-05-28 13:21:37 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: RyuujiX <saputradenny712@gmail.com>
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [bkevans98/ubiquitous-umbrella](https://github.com/bkevans98/ubiquitous-umbrella)@[a9aaa79cc8...](https://github.com/bkevans98/ubiquitous-umbrella/commit/a9aaa79cc8e1e81c4cecaf75a2468d85e0f7705a)
#### Sunday 2023-05-28 14:36:04 by Bkevans98

Update README.md

I am trying to understand why my shit went haywire last summer while we were apart for nearly 8 weeks, 2500 miles away. Ive always thought she was in my emails, then I found this repository that she says isnt hers even though its her log in info with her email address. This maybe lame, but I just want to know if she is being truthful to the man she has been married to for 10 years.

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[c48fadd953...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/c48fadd95304227ad0876d6d5055abe7b86294a9)
#### Sunday 2023-05-28 14:41:58 by AmyBSOD

Lightsaber colors

"omg amy that is stupid" shut up, I'm planning a system where the color will become relevant and therefore I don't want all of them to be cyan just because the shaft would have a metallic color IRL. And who knows, maybe the Jedi actually colored the shafts so that it's easier to recognize what color of lightsaber you have :P

---
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[39ebf7c2af...](https://github.com/LovliestPlant/Skyrat-tg/commit/39ebf7c2af41309fa4d5206f77cc4d261f47dfb7)
#### Sunday 2023-05-28 14:55:40 by SkyratBot

[MIRROR] Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] [MDB IGNORE] (#20832)

* Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

## About The Pull Request
---

The Space Tram is currently spaced. This is a known issue with not the
map, but Trams in general. The Space Tram is a Space Tram to encourage a
fix. Until then, the Space Tram is a maint tram that's an actual hazard
but cannot directly kill anyone, including lizards. Enjoy the commodity
as you zip from secmaint to medmaint.
-------------------------------------------------------

I... really don't know if I should be proud of myself here. This whole
process has been akin to a fever dream and it has only been little over
a month since I first created the .dmm for this. What started as a
simple yet humble reimagining of Birdboat has turned into an entirely
new station, and blown past Metastation sized proportions. This has been
my most expansive project yet, and somehow it's also been my quickest.
So without further ado, I unveil Birdshot - Successor to Birdoat.

-------------------------------------------------------

**Due to recent cost expenditures on Icemoon projects, and a growing
need for orbital research stations, Nanotrasen has decided to pull
Birdboat Station out of mothball after nearly 5 years of abandonment.**

Since then, the station has seen a variety of changes at the hands of
the various vagabond lawless scum and villains that have decided to make
the abandoned station their home. Do not fret though, a Nanotrasen
Operation has secured the companies rightful property for corporate use
once again, though you'll need to be the stewards of the remaining
cleanup operation.

------------------------------------------------------

Now, as you might have guessed by now, Birdshot is heavily based on
Birdboat station. Many of the decisions here follow the original layout,
and what had to be modified or moved still tries its best to replicate
and imitate what bird being said. At least, that was the idea initially.
This has very much grown into its own beast and as such, while the main
inspiration has been Birdboat, there are a lot of new ideas thrown into
the mix that really give this station its own unique and deserving
identity. Maybe it's not perfect, but I've been inspired by @ MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**

![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)

See the image in more detail here: https://imgur.com/iT5Vi8k

## Why It's Good For The Game

We've been with the same 5 maps for a while now. @ san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @ EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @ Fikou's new mannequin dolls.
Command is outfitted with a Corporate Guest Suite, and Officials sent
from Nanotrasen can embark from their ferry into the safety of their own
Corporate Dock. Elements of Cerestation are present, yet not in a way
that makes traversal annoying. Furthermore we have **2 Trams** (that I
have yet to get functional but we'll get there) on Birdshot, that's
right 2. One Security Prison Tram, and then other, a Space Tram. Both
Novel in their own ways. Departments on Birdshot twist and turn, and
there's an abundance of Maintenance Tunnels to cut through everything,
for the brave and the bold that is. And there's plenty left to discover,
but I'd rather let Birdshot speak for itself. I'm proud of this one.

If you want something new, this is something that is almost the complete
opposite of Chilled Station - Explicitly Designed to send you back to
the metal death trap that is: **Space Station 13.**

## Changelog
:cl:
add: Birdshot station has been pulled out of Mothball.
add: New station areas and places to visit. A Mix of Kilo and Delta
maints with winding shortcutting paths.
add: A host of new shuttles to support this bold endeavor to reclaim
something that really shouldn't be reclaimed.
add: Two Trams, Two Trams.
add: For the last time Bob, the gaping hole is a **feature.** Use the
breach shutters or have the virologist make starlight.
add: A smiling salute to stations past...
add: Secrets.

/:cl:

---------

Co-authored-by: Zytolg <theoriginaldash@ gmail,com>

* Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION]

* basemap

* automapper templates

* Update maps.txt

* Update _basemap.dm

---------

Co-authored-by: Zytolg <33048583+Zytolg@users.noreply.github.com>
Co-authored-by: Zytolg <theoriginaldash@ gmail,com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[1b3310bb3a...](https://github.com/wrye-bash/wrye-bash/commit/1b3310bb3a50af03df6b33c06279534152971234)
#### Sunday 2023-05-28 14:57:49 by sibir

Nightly:

RRR Add support for Fallout NV on EGS

No curveballs, it just has the same localized directories as the WS
version, unique My Games & AppData folders, & a `FalloutNV_lang.esp`.

Under # 648 <--- RRR

Add support for GOG versions of TES3, FO3 and FNV RRR

Can't use game_detect_includes here because that one is a logical
conjunction. For the .ico files used by GOG games we need a logical
disjunction instead, so we have to override test_game_path. Also made
the mixins inherit from GameInfo to fix some PyCharm warnings.

Unsure if we can add a separate installer option for these. Someone
would have to test if they overwrite Steam's registry key (we'll
eventually want to refactor the way we detect Steam games to stop
relying on that potentially shared key, which will fix this problem for
good).

Under # 646 <--- RRR

SSS Bump ifileoperation

Bug fix for a case that shouldn't concern us.

Don't ghost the main game ESM

We rely on that one being present on boot. Could refactor WB to allow
the main game ESM to be ghosted, but I don't think allowing this one to
be ghosted is a good idea anyway - how is the game going to boot without
it? Even the original Nehrim needed an empty, dummy Oblivion.esm file to
be there.

TES3: Fix regression causing crash on boot

Broke in c5c493fd179d18b7e2c26fa030b1f1f7f731c9ec. This is very ugly
though.

Fix regression when wizard image is missing SSS

Forgot to add a fallback branch when an image is missing and is supposed
to be in the Wizard Images folder.
Broke in 1fe6d2dc38808d079836a2f575699f4ea7a4b2aa.

FFF add note

ci: Bump PR workflow dependencies

Create hidden dir before unhiding

Otherwise it'll open some random directory instead (e.g. My Documents).

Add support for listing default tweak 'errors'

More accurate terminology would be "reasons why the INI can't be
applied", but that's a different can of worms. The only reason why this
had to be disabled for default INIs is the usage of self.abs_path, but
we only use that to the get the tail - which we already have as
self.fn_key. So just use that, and it magically works for default tweaks
as well.

Create directory before duplicating files

Ran into this once with the INI Edits tab while testing, but couldn't
replicate it again afterwards unless I deleted the INI Tweaks directory
after WB was started (since WB *should* always create that directory
during boot).

Downgrade save activate/reorder errors to warnings

This is commonly encountered when activating or reordering the load
order to match a save's masters. Don't show a big red error about it, a
warning is fine.

Fix another MreRecord.size regression

Broke in c5c493fd179d18b7e2c26fa030b1f1f7f731c9ec as well.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[208f372490...](https://github.com/mrakgr/The-Spiral-Language/commit/208f3724901d14f992d19a27eec10090e301413a)
#### Sunday 2023-05-28 15:22:35 by Marko Grdinić

"https://youtu.be/j9Vn6PC2u8k?t=1065
> I always forget how bad React is.

I never knew it myself.

https://youtu.be/j9Vn6PC2u8k?t=1251
> I am in full support of single stack languages.

Interesting to hear him say that. I've been seriously considering this myself now that I am in Blazor.

https://youtu.be/j9Vn6PC2u8k?t=1413

I wouldn't have expected Node of all things to have problems with cold starts.

https://youtu.be/j9Vn6PC2u8k?t=1670
> I've been wanting to find a technology that I am excited about writing full stack applications in.

5/28/2023

6:25am. I keep getting earlier and earlier.

I program, get tired, don't feel like reading novels & manga due to being tired, go to bed early, and wake up early because I don't need 12h of sleep.

6:30am. Got a reply from the author. He says FeatureState allows me to specify a static method.

6:35am. https://re-library.com/translations/hero-king/volume-8/chapter-338-15-year-old-inglis-and-the-prisma-battle-16/

Let me catch up with Inglis.

https://ac.qq.com/ComicView/index/id/653742/cid/3175?fromPrev=1

Then the raws for this. And then I'll resume programming.

6:45am. https://www.reddit.com/r/ProgrammingLanguages/comments/13sz0vh/how_to_implement_a_lexicographic_graph_sort_for_a/

I guess I won't be posting this here.

7:20am. Let me just finish the chapter and then I will start.

The PL sub doesn't want my vids. The mod wants something higher quality apparently.

But making high quality videos is difficult.

It is not that easy to be a high grade actor.

For now, I'll finish this video and then get to work seriously mining the job market. I need to figure out why I am not getting interviews. I'll have ChatGPT help me bust my way through this initial hump.

There shouldn't be so much pressure on jobs in Europe.

In order to get a high salary, I really need to have a lot of demand for myself. Competing offers.

Just having experience on my resume won't matter.

To put it another way, my salary is solely determined by how well I act at interviews, and what is written on my resume, not by anything I did in reality.

7:25am. But at the same time, I need to have some pride, and actually have the relevant skills in full stack development.

Fable wasn't it. Neither could Bolero fit.

Realistically, I could have gone with React, but I would have hated myself.

So Blazor is the only option.

7:30am. I need to make figuring out the job market my hobby.

I am suspecting that my nationality might deter people from hiring me, but unfortunately, that I am located in Croatia is the one thing I won't be able to lie about. So I'll have to operate with that restriction in place.

Let's get started.

Music - on.

11:10am. https://learn.microsoft.com/en-us/aspnet/core/blazor/advanced-scenarios?view=aspnetcore-7.0

So this is how you can generate them manually.

11:40am. https://learn.microsoft.com/en-us/aspnet/core/blazor/components/data-binding?view=aspnetcore-7.0

I should have used bind.

12:40pm. Let me take a break here.

1:50pm. I'd rather take off, but let me resume.

Let me resume.

Failed to create MSBuildWorkspace: [Failure] Cannot open project because the file extension '.fsproj' is not associated with a language

3:05pm. I found an issue associated with this error. It is open.

Also right now I am grappling with the weirdest Blazor bug ever. It won't accept a compnent that inherits from another component.

3:35pm. Damn it, I removed the Build project and it wiped out everything in the solution. Stupid thing!

3:55pm. Let me resume. I wasted like an hour on this error.

4:05pm. Oh my god, did I fucking lose the work I did on the UI?

Edit: Nope.

4:50pm. I am too tired to program anymore for the day.

I was doing it since way earlier than usual.

I think I am about 70% done with the rewrite.

5:15pm. Done with lunch.

I'll close here."

---
## [thenameissushant/Car_Game](https://github.com/thenameissushant/Car_Game)@[fd303d19c1...](https://github.com/thenameissushant/Car_Game/commit/fd303d19c15ffdb2ff2f3d541225f032595369d8)
#### Sunday 2023-05-28 15:57:05 by Sush@nt

Add files via upload

This GitHub repository contains a fun and interactive Car Game built using HTML, CSS, and JavaScript. The game is designed to provide an enjoyable gaming experience while showcasing the potential of web technologies.

Features:

User-friendly interface: The game offers an intuitive interface that allows players to easily navigate and interact with the game elements.
Responsive design: The game adapts to different screen sizes, ensuring compatibility with various devices, including desktops, laptops, tablets, and smartphones.
Smooth gameplay: The game provides a seamless and smooth gaming experience, thanks to optimized JavaScript code and animations.
Car customization: Players have the option to customize their cars, choosing from a range of colors, styles, and designs.
Challenging levels: The game offers multiple levels with increasing difficulty, providing players with an exciting and engaging gameplay experience.
Score tracking: The game keeps track of the player's score, allowing them to compete with themselves or others for high scores.
Sound effects: Engaging sound effects enhance the gaming experience, adding an immersive element to the gameplay.
This repository serves as a resource for developers and enthusiasts interested in learning about game development using web technologies. It provides a codebase that demonstrates the implementation of core game mechanics using HTML, CSS, and JavaScript. Developers can study the code, modify it, and build upon it to create their own unique game experiences.

Whether you're a beginner learning web development or an experienced developer looking to explore game development on the web, this Car Game repository can serve as an excellent starting point. Feel free to clone, contribute, and customize the game to suit your needs and preferences. Let's race and have some fun!

---
## [Michaelmanicotti/poetry](https://github.com/Michaelmanicotti/poetry)@[8188c7cb85...](https://github.com/Michaelmanicotti/poetry/commit/8188c7cb8591e7bd29777ad541a4779fa34eea37)
#### Sunday 2023-05-28 16:13:00 by Michaelmanicotti

Create  Movement III | Fuck you, for stealing my heart.

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[16e4f3c492...](https://github.com/RaShCat/FF-STG/commit/16e4f3c492cd18e74c975051c4fcd9da5e59fb80)
#### Sunday 2023-05-28 16:35:57 by SkyratBot

Tcomms Soundloop Comes From One Source And Is Less Awful [MDB IGNORE] (#20713)

* Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Tcomms Soundloop Comes From One Source And Is Less Awful

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[500cdb9257...](https://github.com/RaShCat/FF-STG/commit/500cdb925720c408de4332df6b2d8b8e0b20b63c)
#### Sunday 2023-05-28 16:35:57 by SkyratBot

north star's asylum no longer spawns with prisoners [MDB IGNORE] (#20732)

* north star's asylum no longer spawns with prisoners (#74879)

## About The Pull Request
the asylum on the north star no longer spawns prisoners, only the
permabrig does
the computer in the asylum is rotated correctly

## Why It's Good For The Game
on the paper, it seems like a cool concept, but theres a few issues here
the psychologist isnt designed to handle prisoners in the first place.
this is fine on mrp but it gets kinda muddy when prisoners on lrp like
beating people up
prisoners are recommended as a new player role by the wiki (very
stupid), this role starting in an asylum without anything to do while
being asked some stuff by a psychologist seems like itd add onto
confusion
players dont know what jobs are spawning with them, there very well may
not be a cmo or psychologist. if theres no one in sec you can deal with
that because you have a small botany and kitchen, and can possibly
escape. this aint a thing here, only thing you have is reading books and
maybe pen and paper rpgs if another prisoner spawns, while being stuck
in an extremely tiny space

this can work in the future i think, but it requires code support we
currently dont have, so it better to cut its

## Changelog
:cl:
del: prisoner spawns from the north star asylum
/:cl:

* north star's asylum no longer spawns with prisoners

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[178b6fc96c...](https://github.com/RaShCat/FF-STG/commit/178b6fc96cef11619565d802750cad9e6c34b12a)
#### Sunday 2023-05-28 16:35:57 by SkyratBot

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles [MDB IGNORE] (#20711)

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [psingley/evals](https://github.com/psingley/evals)@[170dfd886c...](https://github.com/psingley/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Sunday 2023-05-28 16:37:43 by Robert Bateman

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
## [psingley/evals](https://github.com/psingley/evals)@[ef1f0ebe0e...](https://github.com/psingley/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Sunday 2023-05-28 16:37:43 by Josh Gruenstein

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
## [psingley/evals](https://github.com/psingley/evals)@[2ffd4b57de...](https://github.com/psingley/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Sunday 2023-05-28 16:37:43 by Andrew Kondrich

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
## [Stalkeros2/tgstation](https://github.com/Stalkeros2/tgstation)@[b304b6523f...](https://github.com/Stalkeros2/tgstation/commit/b304b6523fa1f497800c8ba3818e4d2c01d4eaf4)
#### Sunday 2023-05-28 16:53:52 by LemonInTheDark

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
## [KingStank/nodemon](https://github.com/KingStank/nodemon)@[e099e91cb6...](https://github.com/KingStank/nodemon/commit/e099e91cb6ff9cbb7912af86d22b91cd855a1ad0)
#### Sunday 2023-05-28 18:48:35 by Remy Sharp

fix: remove postinstall script

This was needed a few years ago to let people know that without active
support I'd (remy) wouldn't feel like there's any actual support to help
me maintain this project.

Since then (it's been a good few years), there's been a few things come
up. Firstly, the `||` breaks (some) powershell users. Not all, I could
never replicate the problem myself, but others definitely experience it.

Then there was the `npm fund` attempt to support projects. In honesty,
this does zero to actually support nodemon. The reality is that people
want their tools (and software) for free, so asking users to run an
extra step after installing (the `npm fund` bit) and _then_ pick a
project they want to support *and then* do the payment thing was
just way way too much. I know I don't use it, and I'm positive others
don't too.

The majority of early supporters of nodemon have been individuals, and
I know it was because of the postinstall script I added back in 2018:
https://remysharp.com/2018/01/10/open-source-with-a-cap-in-hand

Lastly, the vast, vast majority of financial supporters to nodemon in
the last 12 months haven't been individuals. Nor have they been
companies (with the exceptions being opencollective themselves and
Frontend Masters - both, thank you, it means a lot). The recent
supporters have come from an…"odd" spot of the internet. Perhaps to
help their SEO ranking, I'm not sure, but I am going to take their
money as a way of them saying "let's support the many developers who
use nodemon by giving it's maintainer financial support".

So, long story short: I've removed the postinstall, and hopefully
this reduces the noise to you, the amazing day-job developer, and
hopefully that odd corner of the web continues their donations, as
I'm positive they're not using the `npm fund`!

---
## [TheRealScarHomie/mojave-sun-13](https://github.com/TheRealScarHomie/mojave-sun-13)@[b2f0f35f3a...](https://github.com/TheRealScarHomie/mojave-sun-13/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Sunday 2023-05-28 18:58:00 by EdwardNashton

Speed, Money and Faith: Updating an areas of Town. (#2286)

* Update TGS DMAPI

* Speed, Money and Faith: Updating an areas of Town.

Added a Church with a graveyard area (that currently empty because we have no tombs).

Remade one quarter into 4 different shops: Liquor, Pharmacy, Gun Shop, General Store.

Remade old shitty Library into Biker's Club.

Remade a Dime's Radio Station (by his permission)

Fixed a small area issue on a top z-level of Car Jankyard.

* Fixes up a bunch of stuff :)

* additional minority fixes

---------

Co-authored-by: tgstation-server <tgstation-server@users.noreply.github.com>
Co-authored-by: Edward Nashton <eddienigma48@gmail.com>
Co-authored-by: Professor Popoff <omniderpectional@gmail.com>

---
## [Szikaka-97/Receiver2ModdingKit](https://github.com/Szikaka-97/Receiver2ModdingKit)@[e0ca8d51e7...](https://github.com/Szikaka-97/Receiver2ModdingKit/commit/e0ca8d51e702b4a503645bf0fece0c5612c93000)
#### Sunday 2023-05-28 19:35:47 by Szikaka-97

Merge pull request #2 from CiarenceW/master

few things to make me hate my life less

---
## [danielschafi/dblpProject](https://github.com/danielschafi/dblpProject)@[ce632fb2b9...](https://github.com/danielschafi/dblpProject/commit/ce632fb2b9387bd75a07fdf71362cbc7628b8508)
#### Sunday 2023-05-28 19:36:22 by Daniel Schafhäutle

python project structure shit sucks ass bitch, why you bully me

---
## [LongSleeves/Liberty-Station-13](https://github.com/LongSleeves/Liberty-Station-13)@[0f74820c9d...](https://github.com/LongSleeves/Liberty-Station-13/commit/0f74820c9d04762ac5b06907e6eb5207be80f136)
#### Sunday 2023-05-28 22:22:42 by ThePainkiller

Fixes upon fixes and more

- Fixes exploit on medical fabricator that allowed it to take any disk
- Consequently, fixes general autolathe's capacity to receive medical disks as was... intended?
- Comments out cartographer's seal and pyramid anomalies
- Bruise packs and the like should now cost their exact amount of materials (and chemicals) to print, no longer accruing massive costs
- New: Gate floodlights, they're static, fixed, brighter, and can't have their cells taken out (they come with a large posi). To illuminate the fence at night. TODO: Make them create a directional light spot like flashlights
- Wallets can now take syrettes
- Bone gel now made out of biomatter
- Fixes extant references to Lonestar on the vault's gold shovel
- Adds and renames missing stamps to heads of staff offices
- New functionality: CTRL SHIFT clicking a PDA ejects its pen
- New functionality: Alt clicking a dropper selects transfer amount
- Ammo kits (and the crafting table) can now make caseless ammo
- Fixes Ugil's mag overlay issue
- Changes up many, many weapon's firing sounds to be more fitting
- Fixes self heating coffee doing eating sounds
- Adds quality of life sounds to MRE-like foods, when opened, heated up, and finished heating
- Beautification of the Custodians of the Bonfire's Stronghold, removing references to church, new areas as well
- Changed the lift's walls' names from the mines from "The Rocinante" to "Elevator" proper
- Many musical instruments and loot added to the map
- Bar now has a piano!

---
## [ioccc-src/temp-test-ioccc](https://github.com/ioccc-src/temp-test-ioccc)@[22bbe488e9...](https://github.com/ioccc-src/temp-test-ioccc/commit/22bbe488e94644fd699f00154043190ff3aa56da)
#### Sunday 2023-05-28 23:25:22 by Cody Boone Ferguson

Format fix 2019/poikola/README.md

Yesterday I noticed that Timo wrote directly to me in his remarks and I
wanted to address this by adding a link to myself (which is what is
being done with all winners being referred to) but this naturally meant
I should format fix the file too. I am very touched by this especially
as 2019 was a very hard year for me and I didn't even think I was going
to participate in that year (did in the end and didn't win but funnily
enough some of my entry ideas actually won though with some differences
of course) so I wanted to address it now. I might end up changing my
name to my full name but I want to keep it as close to as possible
(format fixed and links added notwithstanding) first to see how it
looks. Thank you Timo! It means a great deal to me.

In the paragraph to me Timo wrote about his 2018 entry and I linked to
that too.

I changed another winner Timo mentioned to be a link (the winner in
winners.html as well as the winning entry referred to are now both
links).

Add some links and other format fixes.

Added INABIAF section to both the README.md file and bugs.md.

Typo fixes or at least adding a word here and there to make certain
things a bit clearer.

---
## [BrokerBrain/evals](https://github.com/BrokerBrain/evals)@[b93700ab49...](https://github.com/BrokerBrain/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Sunday 2023-05-28 23:25:31 by DunedainStrider

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
## [BrokerBrain/evals](https://github.com/BrokerBrain/evals)@[8e276ea460...](https://github.com/BrokerBrain/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Sunday 2023-05-28 23:25:31 by steven-luabase

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
## [chadvandy/nagash](https://github.com/chadvandy/nagash)@[e6672d8b02...](https://github.com/chadvandy/nagash/commit/e6672d8b025f8a5863265edd04ff777146e07586)
#### Sunday 2023-05-28 23:41:42 by Scott (JvJ)

The lots of shit update

Tech

Dieter Tech, Ageless Necromancer now grants +10 Phys/Spell/Missile/Fire and Ward save to Dieter
Dieter Tech, Seat of Good Manner now grants Empower stance + X
Dieter Tech, Doom's Day now grants spell mastery for spellcaster lords/liche priests/vampires and +3 additional uses of Staff of Flaming Death
Dieter Tech, Arcane Ascendance now grants 600 barrier for morghast units and +15% fire res for all characters
Dieter Tech, Mortal Mask now grants +20% healing cap and 10% HP for all characters,  10% healing cap for Zombies, 5% HP for Zombies
Dieter Tech, Dooms Own now grants plus 10% phys to all MI units, +20% fire res and frenzy to crypt ghouls and horrors
Dieter Tech, Destined Acolyte now grants +5 recruit rank for Master Necros, +1 uses for Raise Dead and all of it's variants
Master Arcane Conduit, removed disable effects for arcane/greater conduit, icon now appears in the skill and the removal process is handled elsewhere
Arkhan Tech, Right-Hand Arkhan, no longer reduces attrition damage
Arkhan Tech, Right-Hand Arkhan, now grants increased reinforcement range and decreased reinforcement time
Vlad Tech, Emperor of Man, now unlocks Thrall Crossbowmen and Thrall Handgunners
Husk and Boss Nagash both start with spell mastery, not greatly useful on it's own but helps later
Added all applicable modded mixer cultures to our battle context vs culture flags
Servant to Lust now correctly applies -10% cost reduction for lore of vamps
Tales from the Crypt fixed incorrect loc pathing
Grim's Reaping now correctly states it summons Skeleton Reapers
Removed dummy vanguard flag from Vlads Mortarch innate
Updated a few mission and ui locs
New mixed item set containing Items from VC,CST,TMB and some item from a number of other sources
25 new Followers
New* In the Shadows Lair skill for Dieter provides stalk/vanguard for ghoul and beastly units, replaces beasts of the doomed lord
Secrets of Nagashizzar now grants spell mastery to self, WoM reserves and some bound cast of Hand of Dust and Soul Stealer
Death is Peace, diplomatic penalty reduced from -666 to -60, Vs bonuses now apply to certain game 3 races
New* Immortal Levies skill for Vlad grants +1,+4 caps of Sylvanian Thrall Crossbowmen/Handgunners in that order plus some buffs for those units
Doomed Legion added thanks to Barney (Undead Khornate Chosen (S&B) profile with some tweaks, comes with guardian as standard and dampen contact effect))
Blood Beasts added thanks to Barney (A trio of Varghulfs, no SEM passive, blood frenzy ability, unbreakable (tweaked HP due to being malnourished also 3 of them))
Sylvanian Thrall Crossbowmen added ((needs Tex work) tweaked profile from living variant undead, can rampage, slightly stronger/faster, new hunger ability)
Sylvanian Thrall Handgunners added ((needs Tex work) tweaked profile from living variant undead, can rampage, slightly stronger/faster, new hunger ability)
Spirit Hosts, Spectre Swarms, Shade Haunts now 100% AP In the case of Swarms and Haunts this also includes the vortex damage)
Spirit Hosts, Spectre Swarms weapon split from 26/4 to 0/16
Spectre Swarms, Shade Haunts weapon split from 20/8 to 0/28
Spectre Swarms, Shade Haunts vortex damage from 5/2 to 0/6
Spirit Hosts, Spectre Swarms, Shade Haunts +40% HP
Spirit Hosts, Spectre Swarms, Shade Haunts -20% Phys Resist to meet standard
Spirit Hosts now take 1 turn to recruit REJOICE
Mortis Engine now takes 2 turns to recruit
All units now have new/correct banner offset heights
Vanilla 3.1 changes already apply
Nag Guard both +4 base weapon damage +2/+2 split
Tweaked RoR unlock lvls
Added Bone Colossus to missing sets
Fixed some missing attrition entries

---

