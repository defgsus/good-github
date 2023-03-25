## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-24](docs/good-messages/2023/2023-03-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,149,495 were push events containing 3,482,773 commit messages that amount to 250,563,082 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[89aba4f386...](https://github.com/TaleStation/TaleStation/commit/89aba4f386f3c1660021eead7615d84157901e23)
#### Friday 2023-03-24 00:06:20 by TaleStationBot

[MIRROR] [MDB IGNORE] Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#5028)

Original PR: https://github.com/tgstation/tgstation/pull/74143
-----
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

Co-authored-by: Bloop <vinylspiders@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Patreos123/awesome-docker](https://github.com/Patreos123/awesome-docker)@[3164d6df94...](https://github.com/Patreos123/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Friday 2023-03-24 00:59:10 by Derek Lee

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
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[fbdafc8a78...](https://github.com/Ultimate-Fluff/cmss13/commit/fbdafc8a789f5944ca5abcbdb569f466fcea2ff2)
#### Friday 2023-03-24 01:06:18 by victorjosephespinoza

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
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[a9c10b89ef...](https://github.com/Ultimate-Fluff/cmss13/commit/a9c10b89ef77d953cd321d90675bf7dc575548a8)
#### Friday 2023-03-24 01:06:18 by naut

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
## [kindasneaki/Archipelago](https://github.com/kindasneaki/Archipelago)@[6d13dc4944...](https://github.com/kindasneaki/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Friday 2023-03-24 01:09:47 by el-u

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
## [Quidifer/Cranium](https://github.com/Quidifer/Cranium)@[e1b3fde17a...](https://github.com/Quidifer/Cranium/commit/e1b3fde17aea5e725c850de60d6b4a3522e24d47)
#### Friday 2023-03-24 01:37:34 by Karan Bhogal

LETS FREAKING GOOOOOOOOOOO THIS IS THE MOMENT, GET READY GET READY, WE ARE IN THE END GAME NOW BOYS AND GIRLS, THIS IS A VERY EXCITING TIME, ITS BEEN SO REAL, I'D LIKE TO THANK MY FAMILY AND FRIENDS AND THE GREATEST TEAM EVER

---
## [anirban-oss/evals](https://github.com/anirban-oss/evals)@[34f83340a7...](https://github.com/anirban-oss/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Friday 2023-03-24 01:52:10 by kallyaleksiev

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
## [anirban-oss/evals](https://github.com/anirban-oss/evals)@[b170a21cf3...](https://github.com/anirban-oss/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Friday 2023-03-24 01:52:10 by Sam Ennis

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
## [anirban-oss/evals](https://github.com/anirban-oss/evals)@[4f090a04fe...](https://github.com/anirban-oss/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Friday 2023-03-24 01:52:10 by Shawn Marincas

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
## [anirban-oss/evals](https://github.com/anirban-oss/evals)@[b5da073c21...](https://github.com/anirban-oss/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Friday 2023-03-24 01:52:10 by somerandomguyontheweb

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
## [ShamanSliph/Skyrat-tg](https://github.com/ShamanSliph/Skyrat-tg)@[f5e63175ec...](https://github.com/ShamanSliph/Skyrat-tg/commit/f5e63175eca40d65592b20a77df6025d1a3f9804)
#### Friday 2023-03-24 02:24:21 by SkyratBot

[MIRROR] Fixes all antag datum moodlets being removed when any single antag datum is removed [MDB IGNORE] (#19237)

* Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line:
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy.

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

* Fixes all antag datum moodlets being removed when any single antag datum is removed

* fix

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [wulj2/samtools](https://github.com/wulj2/samtools)@[8683587bb9...](https://github.com/wulj2/samtools/commit/8683587bb937cc8a4547a67af71f1f1c22dfcfea)
#### Friday 2023-03-24 02:37:29 by James Bonfield

Totally rewrite the "samtools depth" command.

This uses a circular buffer to accumulate and report depth, instead of
relying on mpileup.  This means it's considerably faster (particularly
on deep data and on CRAM files) and doesn't have the need for a depth
limit to avoid high memory usage.  It still silently accepts the -d/-m
(max depth) parameter, but ignores it.

All output should be identical to the old command except potentially
for the overlap removal (-s) option.  The old code here is complex,
requiring all in-flight records to be held in memory by design.
This is explicitly what I wanted to remove as it is remembering these
records-in-flight that gives the high memory usage and the requirement
of a maximum depth.

Therefore the new depth algorithm may give different results:

- It doesn't force a -q1 or higher.  This is needed with mpileup as
  mpileup doesn't actually removal overlaps, it merely marks them.
  (Try old "depth -q0 -s" and "depth -s -q0" to see this.)

- Even if the user manually adds the -q1 option, the overlap removal
  is purely coordinate based.  The mpileup "removal" is coordinate,
  sequence and quality based.  If overlapping bases agree, the quality
  used is the summation of both qualities, else it's 80% of the
  highest quality.

  This gives differences where read 1 has zero qual and read 2
  overlapping has non-zero qual.  With -q1 we'd ignore that first base
  while mpileup would still count that depth.

- Overlap removal applies to all paired reads, not only those with the
  proper-pair flag set.  This is related to #1036.  Strongly
  overlapping reads are sometimes not labelled as a proper pair as
  they fall outside the expected insert size distribution, but those
  are the reads we really ought to be deduplicating.  (Note this is
  still an issue for mpileup though so it doesn't fix that issue.)

In the process of assessing this, two bugs were discovered in the old
depth code.

- Specifying multiple BAM files where the first file consists solely
  of unmapped reads produces no output.  It should report the data for
  the 2nd file onwards still.

- Due to a mistake in the CRAM_OPT_REQUIRED_FIELDS initialisation, the
  overlap removal (-s) option didn't work correctly on CRAMs, wrongly
  removing every other read regardless of read name.

Regarding samtools depth documentation, the only things that really
changes here are -d/-m options are now ignored, and the overlap
removal has a different algorithm.

I haven't put it in the man page, but for reference

    samtools depth -J -s in.bam

matches

    samtools mpileup -Q0 in.bam | cut -f 1,2,4

There is no anti-J (skip deletions) option for mpileup, so we cannot
perfectly simulate the old samtools depth without parsing the SEQ
column, which sadly cannot be done using traditional regexp hackery
either so it's a complex operation.

---
## [HuskyGameDev/2022f-team5](https://github.com/HuskyGameDev/2022f-team5)@[abe87452cb...](https://github.com/HuskyGameDev/2022f-team5/commit/abe87452cb84132de11217eb61524650a4a79a88)
#### Friday 2023-03-24 02:59:49 by Chase Bootz

Beta Balance Patch 0.1

This balance patch was me fixing the numbers and doing extensive tests at each upgrade level to find out which numbers work best as bases and multipliers for game enjoyability and upgrade viability. The old problem we had was that after three minutes every basic enemy felt like a mini boss. That's not cool, we want to implement those eventually, so why should we let the basic zombies and spiders have all the fun. These are the changes I made and their reasonings and ramifications.

Changelog:

Attack Speed Increase:
1.1x multiplier -> 1.2x multiplier

Increased the attack speed multiplier from 1.1 to 1.2. This change makes the choice between our old insta-pick upgrade (extra ball) and this one closer, whereas before the answer was always to just pile on balls.

Damage Increase:
5 Static -> 1.35x increase (multiplicative)

The damage increase upgrade we had before may as well have been cosmetic. A static 5 increase to each shot per upgrade? This quickly becomes the worst upgrade in the game. Upgrading your attack now scales you up more and more each time and never falls off as the game keeps scaling up.

Speed Increase:
0.2 static -> 0.25 static

Having to upgrade 5 times to get to the next full speed tier feels kind of bad in testing, this change allows you to put 2 upgrades into speed and then go full damaging upgrades and feel like you can outrun the monsters for a good while.

Health Increase:
healthInc value 20 -> healthInc value 35

I don't know exactly what this changed since the health bar is very limited with the way I can visualize the changes happening, but on two health upgrades at a minute in I felt like I could stand in place and take a beating for quite a while longer than 20. I could be wrong. We should add a number to the health bar so that it's easier to test and it's easier for the player to understand how many hits they can take. Also to note: Based on the way enemy damage scales, this will always be the worst upgrade unless it's significantly overpowered.

Enemy Spawn:
3.5 Interval -> 3.75 Interval

This was the upgrade that in testing made the horde appear significantly less in runs were damage or speed was upgraded heavily. Tentative, will be accepting feedback.

Difficulty:
diffScale 1.1 -> diffscale 1.045

This was the number that blew me out of the water, everything I saw during playtesting made sense when I realized how insane a 10% increase is to difficulty per minute. A 4.5% increase is much more manageable and still goes out of control, but it gives the player time to set up their main build and it makes sure the enemies aren't faster than you at the 3-4 minute mark.

Enemy Damage:
(contactDamage+ (contactDamage * diffScale))/2 -> (contactDamage+ (contactDamage * diffScale))/3.45

After testing the new difficulty scale, it became apparent that the real issue was how quickly a perfect run can be ended at 3-4 minutes by one stray hit. Very quickly the enemies are able to oneshot you. By dividing the damage scaling almost in half, you can almost always take a single hit and survive, so no more losing that god tier run by accidentally misjudging hitbox size while running in for that last xp pickup.

This concludes the changes to Monstrous for patch 0.1. I hope your testing of the game feels smoother now and the game feels more playable.

---
## [senorsapo/cmss13](https://github.com/senorsapo/cmss13)@[6f1b1717a7...](https://github.com/senorsapo/cmss13/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Friday 2023-03-24 03:04:34 by TotalEpicness

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
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[f9fe79a307...](https://github.com/dragomagol/tgstation/commit/f9fe79a307dc55eb6e3ecf25019ef388889898ba)
#### Friday 2023-03-24 03:19:40 by Dani Glore

Organ Unit Tests & Bugfixes (#73026)

## About The Pull Request

This PR adds a new unit test for all organs, a new unit test for lungs,
and includes improvements for the existing breath and organ_set_bonus
tests. Using the tests, I was able to root out bugs in the organs. This
PR includes an advanced refactor of several developer-facing functions.
This PR certainly represents a "quality pass" for organs which will make
them easier to develop from now on.

### Synopsis of changes:
1. Fixed many fundamental bugs in organ code, especially in
`Insert()`/`Remove()` and their overrides.
2. Added two new procs to `/obj/item/organ` named `on_insert` and
`on_remove`, each being called after `Insert()`/`Remove()`.
3. Added `organ_effects` lazylist to `/obj/item/organ`. Converted
`organ_traits` to lazylist. 2x less empty lists per organ.
4. Adding `SHOULD_CALL_PARENT(TRUE)` to `Insert()`/`Remove()` was very
beneficial to stability and overall code health.
5. Created unit test `organ_sanity` for all usable organs in the game.
Tests insertion and removal.
6. Created unit test `lungs_sanity` for
`/obj/item/organ/internal/lungs`.
7. Improved `breath_sanity` unit tests with additional tests and
conditions.
8. Improved `organ_set_bonus_sanity` unit tests with better
documentation and maintainable code.

---

### Granular bug/fix list:

- A lot of organs are overriding `Insert()` to apply unique
side-effects, but aren't checking the return value of the parent proc
which causes the activation of side-effects even if the insertion
technically fails. I noticed the use-case of applying "unique
side-effects" is repeated across a lot of organs in the game, and by
overriding `Insert()` the potential for bugs is very high; I solved this
problem with inversion-of-control by adding two new procs to
`/obj/item/organ` named `on_insert` and `on_remove`, each being called
after `Insert()` and `Remove()` succeed.
- Many organs, such as abductor "glands", cursed heart, demon heart,
alien hive-node, alien plasma-vessel, etc, were not returning their
parent's `Insert()` proc return value at all, and as a result those
organs `Insert()`s were always returning `null`. I have been mopping
those bugs up in my last few PRs, and now the unit test reveals it all.
Functions such as those in surgery expect a truthy value to be returned
from `Insert()` to represent insertion success, and otherwise it
force-moves the organ out of the mob.
- Fixed abductor "glands" which had a hard-del bug due to their
`Remove()` not calling the parent proc.
- Fixed cybernetic arm implants which had a hard-del bug due to
`Remove()` not resetting their `hand` variable to `null`.
- Fixed lungs gas exchange implementation, which was allowing exhaled
gases to feedback into the inhaled gases, which caused Humans to inhale
much more gas than intended and not exhale expected gases.

### Overview of the `organ_sanity` unit test:

- The new `organ_sanity` unit test gathers all "usable" organs in the
game and tests to see if their `Insert()` and `Remove()` functions
behave as we expect them to.
- Some organs, such as the Nightmare Brain, cause the mob's species to
change which subsequently swaps out all of their organs; the unit test
accounts for these organs via the typecache `species_changing_organs`.
- Some organs are not usable in-game and can't be unit tested, so the
unit test accounts for them via the typecache `test_organ_blacklist`.

### Overview of the `lungs_sanity` unit test:

- This unit test focuses on `/obj/item/organ/internal/lungs` including
Plasmaman and Ashwalker lungs. The test focuses on testing the lungs'
`check_breath()` proc.
- The tests are composed of calling `check_breath` with different gas
mixes to test breathing and suffocation.
- Includes gas exchange test for inhaled/exhaled gases, such as O2 to
CO2.

### Improvements to the `breath_sanity` unit tests:

- Added additional tests for suffocation with empty internals, pure
Nitrogen internals, and a gas-less turf.
- Includes slightly more reliable tests for internals tanks.

## Why It's Good For The Game

**Organs and Lungs were mostly untested. Too many refactors have been
submitted without the addition of unit tests to prove the code works at
all.** Time to stop. _Time to get some help_. Due to how bad the code
health is in organs, any time we've tried to work with them some sort of
bug caused them to blow up in our faces. I am trying to fix some of that
by establishing some standard testing for organs. These tests have
revealed and allowed me to fix lot of basic developer errors/oversights,
as well as a few severe bugs.


![image](https://user-images.githubusercontent.com/17753498/220251281-07ef598f-355b-43a9-afd6-1de9690831da.png)

## Changelog

:cl: A.C.M.O.
fix: Fixed lungs gas exchange implementation, so you always inhale and
exhale the correct gases.
fix: Fixed a large quantity of hard-deletes which were being caused by
organs and cybernetic organs.
fix: Fixed many organs which were applying side-effects regardless of
whether or not the insertion failed.
code: Added unit tests for Organs.
code: Added unit tests for Lungs.
code: Improved unit tests for breathing.
code: Improved unit tests for DNA Infuser organs.
/:cl:

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[2b76197397...](https://github.com/dragomagol/tgstation/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Friday 2023-03-24 03:19:54 by Jacquerel

Makes Lesser Form into one ability & unit tests it (#73572)

## About The Pull Request

Fixes #73491
Every time I have used this ability lately it's been fucked. 
It would vanish from my actions at arbitrary moments, and also sometimes
transform me into a horrible monkey-man thing instead of a monkey. This
is a shame because being able to become a monkey can be pretty fun, even
if it makes you very vulnerable to being butchered.

Refactoring it into being one action instead of two actions which add
and remove each other fixes the part where the action just disappears.
It reliably sticks between transformations now, regardless of whether or
not they were voluntary.

I also noticed that when I was turning into a monkey it wasn't dropping
the changeling "fake clothes" outfit pieces I had on as a human, leading
to a really fucked up looking monkey. I fixed this by adding `force =
TRUE` in the drop to ground proc in the check for if the equipment you
have is still valid after your species changes. I don't _think_ this has
any side effects but I never do and then someone finds some.
For good measure I also made all of the changeling equipment abilities
which don't work if you are a monkey detect if you become a monkey and
retract themselves.

I also noticed that for a long time Last Resort has been trying and
failing to give you Lesser Form (well, Human Form rather) as a Headcrab,
so I fixed that and now you actually get the ability.

Finally I did a _little_ bit of housekeeping in general on the
changeling actions, mostly balloon alerts. I think these definitely need
more attention than I gave them though. I left a lot of the `to_chat`s
in place because many of them give information you want to be a little
sticky, or refer back to in order to double check what you just did.

I also added a unit test which flips back and forth a few times to
ensure the ability still works.
This required adding an "instant" flag to the monkeyize/humanize procs
to skip the timers, and idenitified a couple of weird issues.
First point: Humanising a monkey would remove the monkey mutation and
then call humanise again, which would not skip itself because it still
regarded you as being a monkey. I changed the order of operations here
slightly so that it will early return.
Second point: Calling `domutcheck` on `human/consistent` would runtime
because we skip the bit which sets up any mutations in their DNA. This
is a part of changeling transformation, so I just made it return
instantly.

## Why It's Good For The Game

You can use this ability again without getting stuck permanently as a
monkey, or it just deleting itself from your list of abilities for no
reason.
Turning into a monkey with fake outfit pieces on won't turn you into an
abomination.

## Changelog

:cl:
refactor: Changeling's Lesser Form is now one ability instead of two
which keep swapping, which should consistently turn you back and forth
without deleting itself from your action bar.
fix: Hatching from an egg left by a Last Resort headcrab should
correctly grant you Lesser Form in addition to your other abilities.
fix: Turning into a monkey while using the Changeling space suit won't
leave you as a monkey with a weird inflated head.
qol: Using lesser form as a monkey with only one stored DNA profile will
skip asking which profile you want and will simply transform you
immediately into the only option.
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[6d158bd3b3...](https://github.com/meemofcourse/Shiptest/commit/6d158bd3b37bba2cb2cec2a27fdb0b9b7d8275ac)
#### Friday 2023-03-24 03:27:41 by spockye

beach ruin, The Treasure Cove! (#1701)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a new Beach ruin, Treasure Cove. 

![2023 01 17-11 26
30](https://user-images.githubusercontent.com/79304582/212874736-b17917a5-876e-4a7a-a073-1581cc394b8e.png)

![2023 01 17-11 26
58](https://user-images.githubusercontent.com/79304582/212874824-9a161419-b751-41d2-a82d-e50f06981025.png)


![image](https://user-images.githubusercontent.com/79304582/212879021-bcdc2238-b50b-48c2-9cd0-d17cccbd50dc.png)

Loot: 
cm-16 rifle (main loot)
energy gun
pirate sabre
frontiersmen hardsuit
misc combat supplies
secret documents
2x abandoned crates
research note / tesla researcher
basic engineering supplies (smes/tools/autolathe/battery charger)
two boats
silver crate / hidden gold crate
misc junk
______
Threat: 
1x spacesuit ranged pirate
2x sword pirates
1x ranged pirate
punji sticks
_____

Lore tidbit:
This "humble abode" is the home of our 5- now 4 Pirate friends! After a
mildly successful raid on a CMM VIP transport, they managed to take a
Cargo tech (the VIP), and a CMM guard as hostage. sadly it didn't all go
as planned, and the CMM officer managed to free himself and killed one
of the pirates. This is where you now find the cave, with both hostages
executed, their brother buried, and the pirates grieving his unfortunate
passing.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
more ruins = good.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new beach ruin, the beach_treasure_cove
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
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[84a2a8f394...](https://github.com/meemofcourse/Shiptest/commit/84a2a8f394a0296ecc527f23c0da470b30280c0c)
#### Friday 2023-03-24 03:27:41 by Bjarl

Die Of Fate Change (#1760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
replaces the die of fate's d20 effect (spawn you as wizard) with spawn
wizard clothes and magic mirror under you.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'm sick of wizards spawning without admin intervention
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
balance: You can't be turned into a wizard by the die of fate, instead
getting a magic mirror and wizard clothes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Abraham-The-Blooket-Hacker/Abraham](https://github.com/Abraham-The-Blooket-Hacker/Abraham)@[7ff331e1d1...](https://github.com/Abraham-The-Blooket-Hacker/Abraham/commit/7ff331e1d146b2c5178bf9b007d9382b08287191)
#### Friday 2023-03-24 04:13:17 by abraham121

blooket menu hack

javascript:/* All terms found in the following link apply: https://github.com/Minesraft2/Blooket-Cheats/blob/main/LICENSE */ (async()=>{var t,d,p,u,m,h,g,b=document.createElement("iframe");if(document.body.append(b),window.confirm=b.contentWindow.confirm.bind(window),window.console.log=b.contentWindow.console.log.bind(window),b.style.display="none",await Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a.get("https://"+(location.host.startsWith("dashboard")?location.host+"/api/games":"play.blooket.com/api/gamequestionsets")+"?gameId=6368436a976422d8a3f70cd7").then(e=>parseInt("0"+e.data.questions.find(e=>"../cheats/gui.js"==e.question)?.answers?.[0]))<1679521365129||confirm("This cheat is outdated and might be bugged, would you still like to run it? You can find regularly updated cheats here https://github.com/Minesraft2/Blooket-Cheats")){function f(e,t={},...a){var o=document.createElement(e);if("object"==typeof t.style){let e="";for(const n in t.style)e+=`${n.replace(/[A-Z]/g,e=>"-"+e.toLowerCase())}: ${t.style[n]}; `;t.style=e}for(const i in t)o[i]=t[i];for(const r of a)o.append(r);return o}console.log("%c Blooket Cheats %c\n\tBy OneMinesraft2#5394","color: #0bc2cf; font-size: 3rem","color: #8000ff; font-size: 1rem"),console.log("%c\tgui.js","color: #0bc2cf; font-size: 1rem"),console.log("%c\tStar the github repo!%c  https://github.com/Minesraft2/Blooket-Cheats","color: #ffd000; font-size: 1rem","");const j={data:null,setItem(e,n){return e.split(".").reduce((e,t,a,o)=>(++a==o.length&&(e[t]=n),e[t]),this.data),localStorage.setItem("JODGUISettings",JSON.stringify(this.data)),this.data},deleteItem(e){return e.split(".").reduce((e,t,a,o)=>(++a==o.length&&delete e[t],e[t]),this.data),localStorage.setItem("JODGUISettings",JSON.stringify(this.data)),this.data},setData(e){this.data=e,localStorage.setItem("JODGUISettings",JSON.stringify(this.data))}};try{j.data=JSON.parse(localStorage.getItem("JODGUISettings")||"{}");for(const N of["backgroundColor","cheatList","contentBackground","defaultButton","disabledButton","enabledButton","infoColor","inputColor","textColor"])j.data[N]&&(j.setItem("theme."+N,j.data[N]),j.deleteItem(N))}catch{j.setData({})}let a,o,i,l,n,e,r,v,s;const M=f("div",{id:"JODGUI",style:{top:Math.max(10,window.innerHeight-600)/2+"px",left:Math.max(10,window.innerWidth-1e3)/2+"px",transform:`scale(${j.data.scale})`,position:"fixed",height:"80%",width:"80%",maxHeight:"600px",maxWidth:"1000px",zIndex:"999",display:"block"}},a=f("style",{id:"variables",innerHTML:`:root {--backgroundColor: ${j.data?.theme?.backgroundColor||"rgb(11, 194, 207)"};--infoColor: ${j.data?.theme?.infoColor||"#9a49aa"};--cheatList: ${j.data?.theme?.cheatList||"#9a49aa"};--defaultButton: ${j.data?.theme?.defaultButton||"#9a49aa"};--disabledButton: ${j.data?.theme?.disabledButton||"#A02626"};--enabledButton: ${j.data?.theme?.enabledButton||"#47A547"};--textColor: ${j.data?.theme?.textColor||"white"};--inputColor: ${j.data?.theme?.inputColor||"#7a039d"};--contentBackground: ${j.data?.theme?.contentBackground||"rgb(64, 17, 95)"};}`}),f("style",{innerHTML:'.alertList::-webkit-scrollbar{display:none;}.alertList{-ms-overflow-style: none;scrollbar-width: none;}.contentWrapper::-webkit-scrollbar{display:none;}.contentWrapper{-ms-overflow-style: none;scrollbar-width: none;}.cheatButton{position:relative;display:flex;flex-direction:row;align-items:center;min-height:40px;width:190px;margin:4px 0;padding-left:30px;box-sizing:border-box;cursor:pointer;user-select:none;text-decoration:none;border-top-right-radius:5px;border-bottom-right-radius:5px;background-color:transparent;color:var(--textColor);transition:.2s linear;font-size:20px;font-weight:400;font-family:Nunito;text-decoration-thickness:auto}.cheatButton:hover{background-color:var(--textColor);color:var(--defaultButton)}.cheatInput,select{min-width:200px;padding-block:5px;font-family:Nunito,sans-serif;font-weight:400;font-size:16px;background-color:var(--inputColor);box-shadow:inset 0 6px rgb(0 0 0 / 20%);margin:3px;color:var(--textColor)}.bigButton:hover{filter:brightness(110%);transform:translateY(-2px)}.bigButton:active{transform:translateY(2px)}.cheatList::-webkit-scrollbar{width:10px}.cheatList::-webkit-scrollbar-track{background:var(--cheatList)}.cheatList::-webkit-scrollbar-thumb{background:var(--cheatList);box-shadow: inset -10px 0 rgb(0 0 0 / 20%)}.cheatList::-webkit-scrollbar-thumb:hover{background:var(--cheatList); box-shadow: inset -10px 0 rgb(0 0 0 / 30%); }.scriptButton:hover{filter:brightness(120%)}.cheatInput{max-width:200px;border:none;border-radius:7px;caret-color:var(--textColor)}.cheatInput::placeholder{color:var(--textColor)}.cheatInput:focus,select:focus{outline:0}.cheatInput::-webkit-inner-spin-button,.cheatInput::-webkit-outer-spin-button{-webkit-appearance:none;margin:0}.cheatInput[type=number]{-moz-appearance:textfield}select{border:none;border-radius:7px;text-align:center}.scriptButton{align-items: center; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; margin: 10px; padding: 5px 5px 11px; position: relative; width: 250px; font-family: Nunito, sans-serif; font-weight: 400; color: var(--textColor); box-shadow: inset 0 -6px rgb(0 0 0 / 20%); border-radius: 7px; cursor: pointer; transition: filter .25s;}.tooltip::after {content: "";position: absolute;width: 10px;height: 10px;background-color: inherit;top: -5px;left: 50%;margin-left: -6px;transform: rotate(135deg)}'}),o=f("div",{style:{width:"100%",height:"100%",position:"relative",outline:"3px solid #3a3a3a",borderRadius:"15px",overflow:"hidden"}},f("div",{id:"background",style:{display:"block",top:"0",left:"0",height:"100%",overflowY:"hidden",overflowX:"hidden",position:"absolute",width:"100%",background:"var(--backgroundColor)",visibility:"visible"}},f("div",{id:"backgroundImage",style:{backgroundImage:"url(https://ac.blooket.com/dashboard/65a43218fd1cabe52bdf1cda34613e9e.png)",display:"block",height:"200%",position:"absolute",width:"200%",top:"50%",left:"50%",backgroundPositionX:"-100px",backgroundPositionY:"-100px",backgroundSize:"550px",visibility:"visible",transform:"translate(-50%,-50%) rotate(15deg)",appearance:"none",opacity:"0.175"}})),l=f("div",{id:"controls",style:{display:"flex",alignItems:"center",justifyContent:"center",paddingBottom:"8px",paddingInline:"15px",position:"absolute",left:"220px",top:"0",visibility:"visible",zIndex:"5",height:"52px",width:"max-content",background:"var(--infoColor)",boxShadow:"inset 0 -8px rgb(0 0 0 / 20%), 0 0 4px rgb(0 0 0 / 15%)",borderBottomRightRadius:"10px",color:"var(--textColor)",fontFamily:"Nunito, sans-serif",fontWeight:"700",userSelect:"text"},innerText:([{ctrl:b,shift:t,alt:d,key:p},{ctrl:u,shift:m,alt:h,key:g}]=[j.data.hide||{ctrl:!0,key:"e"},j.data.close||{ctrl:!0,key:"x"}],`${[b&&"Ctrl",t&&"Shift",d&&"Alt",p&&p.toUpperCase()].filter(Boolean).join(" + ")} to hide | ${[u&&"Ctrl",m&&"Shift",h&&"Alt",g&&g.toUpperCase()].filter(Boolean).join(" + ")} for quick disable\nClick and drag here`),update:({ctrl:e,shift:t,alt:a,key:o}={ctrl:!0,key:"e"},{ctrl:n,shift:i,alt:r,key:s}={ctrl:!0,key:"x"})=>l.innerText=`${[e&&"Ctrl",t&&"Shift",a&&"Alt",o&&o.toUpperCase()].filter(Boolean).join(" + ")} to hide | ${[n&&"Ctrl",i&&"Shift",r&&"Alt",s&&s.toUpperCase()].filter(Boolean).join(" + ")} for quick disable\nClick and drag here`}),f("div",{id:"credits",style:{display:"flex",alignItems:"center",justifyContent:"center",paddingBottom:"8px",position:"absolute",right:"0",top:"0",visibility:"visible",zIndex:"5",height:"47px",width:"280px",background:"var(--infoColor)",boxShadow:"inset 0 -8px rgb(0 0 0 / 20%), 0 0 4px rgb(0 0 0 / 15%)",borderBottomLeftRadius:"10px",color:"var(--textColor)",fontFamily:"Nunito, sans-serif",fontWeight:"700",userSelect:"text"},innerHTML:"Created by OneMinesraft2#5372"}),n=f("div",{id:"controlButtons",style:{display:"flex",alignItems:"center",justifyContent:"center",position:"absolute",right:"0",bottom:"0",visibility:"visible",zIndex:"5",height:"55px",width:"165px",background:"#none",borderLeft:"3px solid black",borderTop:"3px solid black",borderTopLeftRadius:"10px",color:"white",fontFamily:"Nunito, sans-serif",fontWeight:"700",userSelect:"text",overflow:"hidden",pointerEvents:"all"}},e=f("button",{style:{height:"55px",width:"55px",fontFamily:"Nunito",color:"white",backgroundColor:"#00a0ff",border:"none",fontSize:"2rem",cursor:"move"},innerHTML:"✥"}),f("button",{style:{height:"55px",width:"55px",fontFamily:"Nunito",color:"white",backgroundColor:"grey",border:"none",fontSize:"2rem",fontWeight:"bolder",cursor:"pointer"},innerHTML:"-",onclick:function(){let t=!1;return()=>{for(var e of[...o.children])e!=n&&(t?e.style.display=e.style._display:(e.style._display=e.style.display,e.style.display="none"));o.style.height=t?"100%":"55px",o.style.width=t?"100%":"165px",M.style.top=parseInt(M.style.top)+(M.offsetHeight-55)*(t?-1:1)+"px",M.style.left=parseInt(M.style.left)+(M.offsetWidth-165)*(t?-1:1)+"px",M.style.pointerEvents=t?"unset":"none",t=!t}}()}),f("button",{style:{height:"55px",width:"55px",fontFamily:"Nunito",color:"white",backgroundColor:"red",border:"none",fontSize:"2rem",fontWeight:"bolder",cursor:"pointer"},innerHTML:"X",onclick:x})),i=f("div",{className:"cheatList",style:{overflowY:"scroll",background:"var(--cheatList)",boxShadow:"inset -10px 0 rgb(0 0 0 / 20%)",zIndex:"5",width:"220px",position:"absolute",top:"0",left:"0",height:"100%",fontFamily:"Titan One",color:"var(--textColor)",fontSize:"40px",textAlign:"center",paddingTop:"20px",userSelect:"none",padding:"20px 10px 20px 0",boxSizing:"border-box",display:"flex",flexDirection:"column"},innerHTML:'<span style="text-shadow: 1px 1px rgb(0 0 0 / 40%)">Cheats</span>'},f("a",{className:"bigButton",style:{cursor:"pointer",display:"block",fontFamily:"Titan One",margin:"20px auto 10px",position:"relative",transition:".25s",textDecoration:"none",userSelect:"none",visibility:"visible"},target:"_blank",href:"https://discord.gg/QznzysxvX4",innerHTML:`<div style="background: rgba(0,0,0,.25); border-radius: 5px; display: block; width: 100%; height: 100%; left: 0; top: 0; position: absolute; transform: translateY(2px); width: 100%; transition: transform .6s cubic-bezier(.3,.7,.4,1)"></div>\n    <div style="background-color: rgb(11, 194, 207); filter: brightness(.7); position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 5px;"></div>\n    <div style="font-weight: 400; background-color: rgb(11, 194, 207); color: white; display: flex; flex-direction: row; align-items: center; justify-content: center; text-align: center; padding: 5px; border-radius: 5px; transform: translateY(-4px); transition: transform .6s cubic-bezier(.3,.7,.4,1)">\n    <div style="font-family: Titan One, sans-serif; color: white; font-size: 26px; text-shadow: 2px 2px rgb(0 0 0 / 20%); height: 40px; padding: 0 15px; display: flex; flex-direction: row; align-items: center; justify-content: center">\n        <svg style="filter: drop-shadow(2px 2px 0 rgb(0 0 0 / 20%))" xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" viewBox="0 -1 21 16">\n            <path d="M13.545 2.907a13.227 13.227 0 0 0-3.257-1.011.05.05 0 0 0-.052.025c-.141.25-.297.577-.406.833a12.19 12.19 0 0 0-3.658 0 8.258 8.258 0 0 0-.412-.833.051.051 0 0 0-.052-.025c-1.125.194-2.22.534-3.257 1.011a.041.041 0 0 0-.021.018C.356 6.024-.213 9.047.066 12.032c.001.014.01.028.021.037a13.276 13.276 0 0 0 3.995 2.02.05.05 0 0 0 .056-.019c.308-.42.582-.863.818-1.329a.05.05 0 0 0-.01-.059.051.051 0 0 0-.018-.011 8.875 8.875 0 0 1-1.248-.595.05.05 0 0 1-.02-.066.051.051 0 0 1 .015-.019c.084-.063.168-.129.248-.195a.05.05 0 0 1 .051-.007c2.619 1.196 5.454 1.196 8.041 0a.052.052 0 0 1 .053.007c.08.066.164.132.248.195a.051.051 0 0 1-.004.085 8.254 8.254 0 0 1-1.249.594.05.05 0 0 0-.03.03.052.052 0 0 0 .003.041c.24.465.515.909.817 1.329a.05.05 0 0 0 .056.019 13.235 13.235 0 0 0 4.001-2.02.049.049 0 0 0 .021-.037c.334-3.451-.559-6.449-2.366-9.106a.034.034 0 0 0-.02-.019Zm-8.198 7.307c-.789 0-1.438-.724-1.438-1.612 0-.889.637-1.613 1.438-1.613.807 0 1.45.73 1.438 1.613 0 .888-.637 1.612-1.438 1.612Zm5.316 0c-.788 0-1.438-.724-1.438-1.612 0-.889.637-1.613 1.438-1.613.807 0 1.451.73 1.438 1.613 0 .888-.631 1.612-1.438 1.612Z"/>\n        </svg>\n        Discord\n    </div>\n    </div>`})),f("div",{className:"contentWrapper",style:{position:"absolute",left:"220px",top:"70px",overflowY:"scroll",width:"calc(100% - 220px)",height:"calc(100% - 70px)",borderRadius:"7px"}},f("div",{id:"content",style:{position:"absolute",inset:"27px 50px 50px 50px"}},r=f("div",{className:"tooltip",style:{position:"absolute",top:"0",left:"0",backgroundColor:"black",height:"fit-content",maxWidth:"300px",zIndex:"5",borderRadius:"7.5px",color:"white",display:"flex",justifyContent:"center",alignItems:"center",padding:"5px",paddingInline:"15px",pointerEvents:"none",opacity:"0",textAlign:"center"},innerText:"description"}),v=f("div",{style:{alignItems:"center",boxSizing:"border-box",display:"flex",flexDirection:"row",flexWrap:"wrap",justifyContent:"space-evenly",padding:"20px 5px 20px",position:"relative",width:"100%",fontFamily:"Nunito, sans-serif",fontWeight:"400",color:"var(--textColor)",background:"var(--contentBackground)",boxShadow:"inset 0 -6px rgb(0 0 0 / 20%)",borderRadius:"7px"}},s=f("div",{className:"headerText",style:{boxSizing:"border-box",display:"block",height:"45px",left:"-10px",padding:"4px 4px 8px",position:"absolute",top:"-28px",backgroundColor:"#ef7426",boxShadow:"0 4px rgb(0 0 0 / 20%), inset 0 -4px rgb(0 0 0 / 20%)",borderRadius:"7px"}},f("div",{style:{alignItems:"center",boxSizing:"border-box",display:"flex",height:"100%",justifyContent:"center",padding:"0 15px",width:"100%",fontFamily:"Titan One, sans-serif",fontSize:"26px",fontWeight:"400",textShadow:"-1px -1px 0 #646464, 1px -1px 0 #646464, -1px 1px 0 #646464, 2px 2px 0 #646464",color:"white",background:"linear-gradient(#fcd843,#fcd843 50%,#feb31a 50.01%,#feb31a)",borderRadius:"5px"}})))))));for(const T of document.querySelectorAll("#JODGUI"))T.remove();function y(e,t,a,o){const n=f("div",{className:"cheatButton",innerHTML:("string"==typeof t?`<img style="height: 30px; margin-right: 5px" src="${t}">`:t||"")+e,onclick:()=>w(n.innerText,a,o)});return i.appendChild(n),n.onclick}async function w(e,l,t){v.innerHTML="",s.firstChild.innerText=e+(t?"":" Cheats"),v.append(s);for(let s=0;s<l.length;s++){let{name:e,description:t,type:a,inputs:o,enabled:n,run:i,element:r}=l[s];if(!r){const g=f("div",{className:"scriptButton",style:{background:"toggle"==a?n?"var(--enabledButton)":"var(--disabledButton)":"var(--defaultButton)"}},f("div",{className:"cheatName",innerHTML:e}));if(g.dataset.description=t,o?.length)for(let t=0;t<o.length;t++){var{name:c,type:d,options:p,min:u,max:m,value:h}=o[t];let e;try{e=await("function"==typeof p?p?.():p)}catch{e=[]}if("options"==d&&e?.length){const b=document.createElement("select");e.forEach(e=>{var t=document.createElement("option");t.value=JSON.stringify(e?.value||e),t.innerHTML=e?.name||e,b.appendChild(t)}),g.appendChild(b)}else if("function"==d){const y=document.createElement("input");y.classList.add("cheatInput"),y.placeholder=c,y.style.textAlign="center";let e=!(y.readOnly=!0);y.onclick=async()=>{e||(y.value="Waiting for input...",e=!0,y.data=await o[t].function(e=>y.value=e+"..."),e=!1,y.value=y.value.slice(0,-3))},g.appendChild(y)}else{p=document.createElement("input");p.classList.add("cheatInput"),"number"==d&&(p.type="number",p.min=u,p.max=m,p.value=h||(null!=u?u:0)),p.placeholder=c,p.style.textAlign="center",g.appendChild(p)}}g.onclick=function({target:e}){e!=g&&!e.classList.contains("cheatName")||(e=[...g.children].slice(1),i.apply(this,e.map(e=>"number"==e.type?parseInt("0"+e.value):"SELECT"==e.nodeName?JSON.parse(e.value):e.data||e.value)),"toggle"==a&&(g.style.background=this.enabled?"var(--enabledButton)":"var(--disabledButton)"),O.alerts?.[0].addLog(`${"toggle"==a?this.enabled?"Enabled":"Disabled":"Ran"} <strong>${this.name}</strong>`+(o?.length?` with inputs: (${e.map(e=>"SELECT"==e.nodeName?e.selectedOptions[0].innerText:e.value).join(", ")})`:""),"toggle"==a?this.enabled?"var(--enabledButton)":"var(--disabledButton)":null))}.bind(l[s]),l[s].element=g}v.appendChild(l[s].element)}}document.body.appendChild(M);const O={global:[{name:"Auto Answer (Toggle)",description:"Toggles auto answer on",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{var{state:{question:e,stage:t,feedback:a},props:{client:{question:o}}}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];const n=e||o;try{"typing"!=n.qType?("feedback"===t||a?document.querySelector('[class*="feedback"]')?.firstChild:[...document.querySelectorAll('[class*="answerContainer"]')][n.answers.map((e,t)=>n.correctAnswers.includes(e)?t:null).filter(e=>null!=e)[0]])?.click?.():Object.values(document.querySelector("[class*='typingAnswerWrapper']"))[1].children._owner.stateNode.sendAnswer(n.answers[0])}catch{}},50))}},{name:"Highlight Answers (Toggle)",description:"Toggles highlight answers on",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{const{state:a,props:o}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];[...document.querySelectorAll('[class*="answerContainer"]')].forEach((e,t)=>{(a.question||o.client.question).correctAnswers.includes((a.question||o.client.question).answers[t])?e.style.backgroundColor="rgb(0, 207, 119)":e.style.backgroundColor="rgb(189, 15, 38)"})},50))}},{name:"Auto Sell Dupes On Open",description:"Sells the blook you unlock when you open a pack if you already have one (Doesn't sell Legendaries or rarer)",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,XMLHttpRequest.prototype.open=this.data):(this.enabled=!0,this.data=XMLHttpRequest.prototype.open,XMLHttpRequest.prototype._original_open||=XMLHttpRequest.prototype.open,XMLHttpRequest.prototype.open=function(){this.addEventListener("load",async function(){try{var e,t,a,o,n;"https://dashboard.blooket.com/api/users/unlockblook"===this.responseURL&&(e=Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a,t=webpackJsonp.push([[],{rarity:(e,t,a)=>{t.rarity=e=>a("MDrD").a[e].rarity}},[["rarity"]]])["rarity"],a=JSON.parse(this.response)["unlockedBlook"],{name:o,unlocks:n}=(await e.get("https://dashboard.blooket.com/api/users"))["data"],n[a]&&!["Legendary","Chroma","Mystical"].includes(t(a)))&&(await e.put("https://dashboard.blooket.com/api/users/sellblook",{name:o,blook:a,numSold:1}),console.log("Sold duplicate "+a))}catch{}}),XMLHttpRequest.prototype._original_open.apply(this,arguments)})}},{name:"Auto Answer",description:"Click the correct answer for you",run:function(){const{state:{question:a,stage:e,feedback:t},props:{client:{question:o}}}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];try{"typing"!=a.qType?("feedback"===e||t?document.querySelector('[class*="feedback"]')?.firstChild:[...document.querySelectorAll('[class*="answerContainer"]')][(a||o).answers.map((e,t)=>(a||o).correctAnswers.includes(e)?t:null).filter(e=>null!=e)[0]])?.click?.():Object.values(document.querySelector("[class*='typingAnswerWrapper']"))[1].children._owner.stateNode.sendAnswer(a.answers[0])}catch{}}},{name:"Spam Buy Blooks",description:"Opens a box an amount of times",inputs:[{name:"Box",type:"options",options:()=>new Promise(e=>{e(Object.keys(Object.values(webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]]).webpack.c).find(e=>e?.exports?.a?.Safari)?.exports.a||{}))})},{name:"Amount",type:"number"}],run:function(o,n){var e=document.createElement("iframe"),i=(document.body.append(e),window.alert=e.contentWindow.alert.bind(window),window.prompt=e.contentWindow.prompt.bind(window),window.confirm=e.contentWindow.confirm.bind(window),e.remove(),Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache)),c=i.find(e=>e.exports?.a?.get).exports.a;o=o.split(" ").map(e=>e.charAt(0).toUpperCase()+e.slice(1).toLowerCase()).join(" "),c.get("https://dashboard.blooket.com/api/users").then(async({data:{name:e,tokens:t}})=>{var a=i.find(e=>e?.exports?.a?.Safari)?.exports?.a||{Medieval:15,Breakfast:15,Wonderland:15,Space:20,Bot:20,Aquatic:20,Safari:20,Dino:25,"Ice Monster":25};let l=Math.min(Math.floor(t/a[o]),n);if(0==l)0<n&&alert("You do not have enough tokens!");else{let i=confirm("Would you like to alert blooks upon unlocking?"),r={},s=Date.now(),t=!1;for(let n=0;n<l&&(await c.put("https://dashboard.blooket.com/api/users/unlockblook",{name:e,box:o}).then(({data:{unlockedBlook:e,tokens:t,isNewBlook:a}})=>{r[e]||=0,r[e]++;var o=Date.now();i&&alert(`${e} (${n+1}/${l}) ${a?"NEW! ":""}${t} tokens left`),s+=Date.now()-o}).catch(e=>t=!0),!t);n++);alert(`(${Date.now()-s}ms) Results:\n`+Object.entries(r).map(([e,t])=>`    ${e} `+t).join(`\n`))}}).catch(()=>alert("There was an error user data!"))}},{name:"Flood Game",description:"Floods a game with a number of fake accounts",inputs:[{name:"Game ID",type:"string"},{name:"Name",type:"string"},{name:"Amount",type:"number"},{name:"Blook",type:"options",options:async()=>{var e=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"];return Object.keys(Object.values(e.c).find(e=>e.exports.a?.Chick&&e.exports.a?.Elephant).exports.a)}},{name:"Banner",type:"options",options:Object.entries({Starter:"starter",Chalkboard:"chalkboard",Slime:"slime",Bookshelf:"bookshelf","Toaster Pastry":"toasterPastry",Theater:"theater",Sushi:"sushi",Workbench:"workbench",Spooky:"spooky",Spiders:"spiders",Coffin:"coffin",Pumpkins:"pumpkins","Falling Blocks":"fallingBlocks",Racetrack:"racetrack",Harvest:"harvest",Leaves:"leaves","Fall Picnic":"fallPicnic","Winter Drive":"winterDrive","Winter Train":"winterTrain",Ice:"ice",Gifts:"gifts","Christmas Tree":"christmasTree","Soccer Field":"soccerField","Winter Landscape":"winterLandscape","Football Field":"footballField","Outer Space":"outerSpace","Hockey Rink":"hockeyRink","Music Class":"musicClass","Ice Cream Sandwich":"iceCreamSandwich","Science Class":"scienceClass","Fish Tank":"fishTank","Art Class":"artClass",Clockwork:"clockwork","Love Letter":"loveLetter",Farm:"farm",Chocolate:"chocolate","Tech Chip":"techChip",Fire:"fire","Orange Ice Pop":"orangeIcePop"}).map(([e,t])=>({name:e,value:t}))}],run:async function(n,i,e,r,s){var t=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"];const l=Object.values(t.c).find(e=>e.exports?.a?.get).exports.a,c=Object.values(t.c).find(e=>e.exports?.a?.initializeApp).exports.a;for(let o=1;o<=e;o++)(async()=>{var{success:e,fbToken:t,fbShardURL:a}=(await l.put("https://fb.blooket.com/c/firebase/join",{id:n,name:""+i+o}))["data"];e&&(e=c.initializeApp({apiKey:"AIzaSyCA-cTOnX19f6LFnDVVsHXya3k6ByP_MnU",authDomain:"blooket-2020.firebaseapp.com",projectId:"blooket-2020",storageBucket:"blooket-2020.appspot.com",messagingSenderId:"741533559105",appId:"1:741533559105:web:b8cbb10e6123f2913519c0",measurementId:"G-S3H5NGN10Z",databaseURL:a},""+i+o),await(a=c.auth(e)).setPersistence(c.auth.Auth.Persistence.NONE).catch(console.error),await a.signInWithCustomToken(t).catch(console.error),await e.database().ref(n+"/c/"+i+o).set({b:r,bg:s}),e.delete())})(),await new Promise(e=>setTimeout(e,100))}},{name:"Get Daily Rewards",description:"Gets max daily tokens and xp",run:function(){var a,e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),location.href.includes("play.blooket.com")?(a=Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a).post("https://play.blooket.com/api/playersessions/solo",{gameMode:"Factory"}).then(({data:{t}})=>{a.get("https://play.blooket.com/api/users/me").then(({data:{name:e}})=>{a.put("https://play.blooket.com/api/users/add-rewards",{t:t,name:e,addedTokens:500,addedXp:300}).then(({data:{dailyReward:e}})=>alert(`Added max tokens and xp, and got ${e} daily wheel tokens!`)).catch(()=>alert("There was an error when adding rewards."))}).catch(()=>alert("There was an error user data."))}):(alert("This cheat only works on play.blooket.com, opening a new tab."),window.open("https://play.blooket.com/"))}},{name:"Use Any Blook",description:"Allows you to play as any blook",run:function(){const a=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];var e=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]]).webpack("MDrD").a;"/blooks"==location.pathname?a.setState({blookData:Object.keys(e).reduce((e,t)=>(e[t]=a.state.blookData[t]||1,e),{}),allSets:Object.values(e).reduce((e,t)=>e.includes(t.set)?e:e.concat(t.set),[])}):Array.isArray(a.state.unlocks)?a.setState({unlocks:Object.keys(e)}):a.setState({unlocks:e})}},{name:"Every Answer Correct",description:"Sets every answer to be correct",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.freeQuestions=e.questions=e.props.client.questions.map(e=>({...e,correctAnswers:e.answers}))}},{name:"Highlight Answers",description:"Colors answers to be red or green highlighting the correct ones",run:function(){const{state:a,props:o}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];[...document.querySelectorAll('[class*="answerContainer"]')].forEach((e,t)=>{(a.question||o.client.question).correctAnswers.includes((a.question||o.client.question).answers[t])?e.style.backgroundColor="rgb(0, 207, 119)":e.style.backgroundColor="rgb(189, 15, 38)"})}},{name:"Remove Name Limit",description:"Sets the name limit to 120, which is the actual max name length limit",run:function(){var e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),document.querySelector('input[class*="nameInput"]').maxLength=120,alert("Removed name length limit")}},{name:"Remove Random Name",description:"Allows you to put a custom name",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({isRandom:!1,client:{name:""}}),document.querySelector('[class*="nameInput"]')?.focus?.()}},{name:"Sell Cheap Duplicates",description:"Sells all of your uncommon to epic dupes (not legendaries+)",run:function(){var e=document.createElement("iframe"),i=(document.body.append(e),window.alert=e.contentWindow.alert.bind(window),window.confirm=e.contentWindow.confirm.bind(window),e.remove(),Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a);i.get("https://dashboard.blooket.com/api/users").then(async({data:{name:e,unlocks:t}})=>{t=Object.entries(t).filter(([e,t])=>1<t&&!["Legendary","Chroma","Mystical"].includes(webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]]).webpack("MDrD").a[e].rarity));if(confirm("Are you sure you want to sell your uncommon to epic dupes?")){var a,o,n=Date.now();for([a,o]of t)await i.put("https://dashboard.blooket.com/api/users/sellblook",{name:e,blook:a,numSold:o-1});alert(`(${Date.now()-n}ms) Results:\n`+t.map(([e,t])=>`    ${e} `+(t-1)).join(`\n`))}}).catch(()=>alert("There was an error user data!"))}},{name:"Sell Duplicate Blooks",description:"Sell all duplicate blooks leaving you with 1 each",run:function(){var e=document.createElement("iframe"),i=(document.body.append(e),window.alert=e.contentWindow.alert.bind(window),window.confirm=e.contentWindow.confirm.bind(window),e.remove(),Object.values(webpackJsonp.push([[],{"":(e,t,a)=>{t.cache=a.c}},[[""]]]).cache).find(e=>e.exports?.a?.get).exports.a);i.get("https://dashboard.blooket.com/api/users").then(async({data:{name:e,unlocks:t}})=>{t=Object.entries(t).filter(e=>1<e[1]);if(confirm("Are you sure you want to sell your dupes?")){var a,o,n=Date.now();for([a,o]of t)await i.put("https://dashboard.blooket.com/api/users/sellblook",{name:e,blook:a,numSold:o-1});alert(`(${Date.now()-n}ms) Results:\n`+t.map(([e,t])=>`    ${e} `+(t-1)).join(`\n`))}}).catch(()=>alert("There was an error user data!"))}},{name:"Simulate Pack",description:"Simulate opening a pack",inputs:[{name:"Pack",type:"options",options:async()=>Array.from(document.querySelectorAll('[class*="packShadow"]')).map(e=>e.alt)}],run:function(){let m=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"],o=Object.values(m.c).find(e=>e.exports?.Class).exports,h={};class n extends o.Scene{constructor(e){super(),this.rarity=e.toLowerCase()}preload(){switch(this.rarity){case"uncommon":this.load.svg("uncommon-1","https://media.blooket.com/image/upload/v1658567787/Media/market/particles/square_green.svg",{width:25,height:25}),this.load.svg("uncommon-2","https://media.blooket.com/image/upload/v1658567787/Media/market/particles/square_light_green.svg",{width:25,height:25}),this.load.svg("uncommon-3","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/circle_dark_green.svg",{width:25,height:25}),this.load.svg("uncommon-4","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/serpentine_dark_green.svg",{width:30,height:30}),this.load.svg("uncommon-5","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/triangle_light_green.svg",{width:30,height:30}),this.load.svg("uncommon-6","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/serpentine_light_green.svg",{width:30,height:30}),this.load.svg("uncommon-7","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/triangle_green.svg",{width:30,height:30});break;case"rare":this.load.svg("rare-1","https://media.blooket.com/image/upload/v1658567765/Media/market/particles/square_light_blue.svg",{width:25,height:25}),this.load.svg("rare-2","https://media.blooket.com/image/upload/v1658567765/Media/market/particles/square_dark_blue.svg",{width:25,height:25}),this.load.svg("rare-3","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/triangle_blue.svg",{width:30,height:30}),this.load.svg("rare-4","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/serpentine_blue.svg",{width:30,height:30}),this.load.svg("rare-5","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/triangle_light_blue.svg",{width:30,height:30}),this.load.svg("rare-6","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/serpentine_light_blue.svg",{width:30,height:30}),this.load.svg("rare-7","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/circle_dark_blue.svg",{width:25,height:25});break;case"epic":this.load.svg("epic-1","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/red.svg",{width:25,height:25}),this.load.svg("epic-2","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/light_red.svg",{width:25,height:25}),this.load.svg("epic-3","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/serpentine_red.svg",{width:30,height:30}),this.load.svg("epic-4","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/serpentine_dark_red.svg",{width:30,height:30}),this.load.svg("epic-5","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/triangle_red.svg",{width:30,height:30}),this.load.svg("epic-6","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/triangle_light_red.svg",{width:30,height:30}),this.load.svg("epic-7","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/circle_dark_red.svg",{width:25,height:25});break;case"legendary":this.load.svg("legendary-1","https://media.blooket.com/image/upload/v1658567740/Media/market/particles/square_orange.svg",{width:25,height:25}),this.load.svg("legendary-2","https://media.blooket.com/image/upload/v1658567740/Media/market/particles/square_light_orange.svg",{width:25,height:25}),this.load.svg("legendary-3","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/circle_orange.svg",{width:25,height:25}),this.load.svg("legendary-4","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/serpentine_orange.svg",{width:30,height:30}),this.load.svg("legendary-5","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/serpentine_light_orange.svg",{width:30,height:30}),this.load.svg("legendary-6","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/circle_dark_orange.svg",{width:25,height:25}),this.load.svg("legendary-7","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/triangle_dark_orange.svg",{width:30,height:30});break;case"chroma":this.load.svg("chroma-1","https://media.blooket.com/image/upload/v1658790246/Media/market/particles/square_turquoise.svg",{width:25,height:25}),this.load.svg("chroma-2","https://media.blooket.com/image/upload/v1658790246/Media/market/particles/square_light_turquoise.svg",{width:25,height:25}),this.load.svg("chroma-3","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/serpentine_dark_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-4","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/serpentine_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-5","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/triangle_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-6","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/triangle_light_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-7","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/circle_dark_turquoise.svg",{width:25,height:25})}}create(){h.scene=this,h.rarity="",h.particles=this.physics.add.group({classType:new o.Class({Extends:o.GameObjects.Image,initialize:function(){o.GameObjects.Image.call(this,h.scene,0,0,"uncommon-1"),this.setDepth(3),this.lifespan=0},spawn:function(e,t,a,o,n,i,r,s,l){this.setTexture(l),this.setActive(!0),this.setVisible(!0),this.setPosition(e,t),this.setScale(a),this.targets=[],h.scene.physics.velocityFromAngle(o,n,this.body.velocity),this.body.setGravityY(i),this.body.setAngularVelocity(r),this.lifespan=s},update:function(e,t){this.lifespan-=t,0<this.lifespan||(this.setActive(!1),this.setVisible(!1))}}),runChildUpdate:!0}),this.nextParticle=0,this.numExplosions=0,this.game.events.on("start-particles",e=>{h.rarity=e,this.numExplosions="Uncommon"===e?75:"Rare"===e?100:-1})}update(e,t){const a=m("74sb");function o(e){switch(e){case"center":var t=Object(a.l)(-115,-65);return{x:h.scene.cameras.main.worldView.width/2,y:h.scene.cameras.main.worldView.height/2,scale:Object(a.l)(.7,1),angle:t,velocity:Object(a.l)(600,750),gravity:700,angVelocity:(-90<t?1:-1)*Object(a.l)(125,175),lifespan:2500};case"right-bottom":return{x:h.scene.cameras.main.worldView.width,y:h.scene.cameras.main.worldView.height,scale:Object(a.l)(.7,1),angle:Object(a.l)(-160,-110),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-bottom":return{x:0,y:h.scene.cameras.main.worldView.height,scale:Object(a.l)(.7,1),angle:Object(a.l)(-70,-20),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(125,175),lifespan:2500};case"top":return{x:Object(a.l)(0,h.scene.cameras.main.worldView.width),y:-50,scale:Object(a.l)(.7,1),angle:90,velocity:Object(a.l)(0,50),gravity:700,angVelocity:Object(a.l)(-150,150),lifespan:2500};case"right-shower":return{x:h.scene.cameras.main.worldView.width,y:Object(a.l)(0,h.scene.cameras.main.worldView.height),scale:Object(a.l)(.7,1),angle:Object(a.l)(-180,-130),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-shower":return{x:0,y:Object(a.l)(0,h.scene.cameras.main.worldView.height),scale:Object(a.l)(.7,1),angle:Object(a.l)(-50,0),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(125,175),lifespan:2500};case"right-diamond":t=Object(a.l)(0,h.scene.cameras.main.worldView.height);return{x:h.scene.cameras.main.worldView.width,y:t,scale:Object(a.l)(.7,1),angle:t>h.scene.cameras.main.worldView.height/2?-150:-210,velocity:Object(a.l)(600,750),gravity:0,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-diamond":t=Object(a.l)(0,h.scene.cameras.main.worldView.height);return{x:0,y:t,scale:Object(a.l)(.7,1),angle:t>h.scene.cameras.main.worldView.height/2?-30:30,velocity:Object(a.l)(600,750),gravity:0,angVelocity:Object(a.l)(125,175),lifespan:2500};default:return{}}}if(h.rarity&&0!==this.numExplosions&&(this.nextParticle-=t,this.nextParticle<=0)){switch(h.rarity){case"Uncommon":for(let e=0;e<2;e++){var n=h.particles.get();n&&n.spawn.apply(n,Object.values(o("center")).concat("uncommon-"+Object(a.m)(1,8)))}break;case"Rare":for(var i=0;i<2;i++){var r=h.particles.get();r&&r.spawn.apply(r,Object.values(o(i%2==0?"left-bottom":"right-bottom")).concat("rare-"+Object(a.m)(1,8)))}break;case"Epic":for(var s=0;s<2;s++){var l=h.particles.get();l&&l.spawn.apply(l,Object.values(o(s%2==0?"left-shower":"right-shower")).concat("epic-"+Object(a.m)(1,8)))}break;case"Legendary":for(var c=0;c<3;c++){var d=h.particles.get();d&&d.spawn.apply(d,Object.values(o("top")).concat("legendary-"+Object(a.m)(1,8)))}break;case"Chroma":for(var p=0;p<3;p++){var u=h.particles.get();u&&u.spawn.apply(u,Object.values(o(p%2==0?"left-diamond":"right-diamond")).concat("chroma-"+Object(a.m)(1,8)))}}this.nextParticle=20,0<this.numExplosions&&(this.numExplosions=Math.max(this.numExplosions-1,0))}}}return function(e){if("/market"!==window.location.pathname)return alert("This must be ran on the market page");var t,a=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];let i=m("fGzD");(i=Object.keys(i.a).reduce((e,t)=>(e.packs.includes(t)&&(e.data[t]=Object.fromEntries(i.b(t))),e),{packs:Array.from(document.querySelectorAll('[class*="packShadow"]')).map(e=>e.alt),data:{}}).data)[e]?(e=function(e){var t=[],a=Object.keys(i[e]);for(const n of a)t.push(i[e][n]+(t[a.indexOf(n)-1]||0));const o=t[t.length-1]*Math.random();return a[t.findIndex(e=>e>=o)]}(e),t=Object.values(m.c).find(e=>e.exports?.a?.Elephant).exports.a,a.setState({loadingPack:!1,openPack:!0,unlockedBlook:e,tokens:a.state.tokens,newUnlock:!0,game:{type:o.WEBGL,parent:"phaser-market",width:"100%",height:"100%",scale:{mode:o.Scale.NONE,autoCenter:o.Scale.CENTER_BOTH},transparent:!0,physics:{default:"arcade"},scene:new n(t[e].rarity)},canOpen:!0})):alert("I couldn't find that box!")}}()},{name:"Simulate Unlock",description:"Simulate unlocking most of the blooks",inputs:[{name:"Blook",type:"options",options:async()=>{let a=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"];return Object.keys(Object.entries(Object.values(a.c).find(e=>Object.values(e.exports?.a||{})[0]?.set).exports.a).reduce((e,t)=>(Object.values(a.c).find(e=>15==e.exports.a?.Breakfast).exports.a[t[1].realSet||t[1].set]&&(e[t[0]]=t[1]),e),{}))}}],run:function(){let m=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"],a=Object.values(m.c).find(e=>e.exports?.Class).exports,h={};class o extends a.Scene{constructor(e){super(),this.rarity=e.toLowerCase()}preload(){switch(this.rarity){case"uncommon":this.load.svg("uncommon-1","https://media.blooket.com/image/upload/v1658567787/Media/market/particles/square_green.svg",{width:25,height:25}),this.load.svg("uncommon-2","https://media.blooket.com/image/upload/v1658567787/Media/market/particles/square_light_green.svg",{width:25,height:25}),this.load.svg("uncommon-3","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/circle_dark_green.svg",{width:25,height:25}),this.load.svg("uncommon-4","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/serpentine_dark_green.svg",{width:30,height:30}),this.load.svg("uncommon-5","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/triangle_light_green.svg",{width:30,height:30}),this.load.svg("uncommon-6","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/serpentine_light_green.svg",{width:30,height:30}),this.load.svg("uncommon-7","https://media.blooket.com/image/upload/v1658567785/Media/market/particles/triangle_green.svg",{width:30,height:30});break;case"rare":this.load.svg("rare-1","https://media.blooket.com/image/upload/v1658567765/Media/market/particles/square_light_blue.svg",{width:25,height:25}),this.load.svg("rare-2","https://media.blooket.com/image/upload/v1658567765/Media/market/particles/square_dark_blue.svg",{width:25,height:25}),this.load.svg("rare-3","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/triangle_blue.svg",{width:30,height:30}),this.load.svg("rare-4","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/serpentine_blue.svg",{width:30,height:30}),this.load.svg("rare-5","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/triangle_light_blue.svg",{width:30,height:30}),this.load.svg("rare-6","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/serpentine_light_blue.svg",{width:30,height:30}),this.load.svg("rare-7","https://media.blooket.com/image/upload/v1658567763/Media/market/particles/circle_dark_blue.svg",{width:25,height:25});break;case"epic":this.load.svg("epic-1","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/red.svg",{width:25,height:25}),this.load.svg("epic-2","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/light_red.svg",{width:25,height:25}),this.load.svg("epic-3","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/serpentine_red.svg",{width:30,height:30}),this.load.svg("epic-4","https://media.blooket.com/image/upload/v1658790239/Media/market/particles/serpentine_dark_red.svg",{width:30,height:30}),this.load.svg("epic-5","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/triangle_red.svg",{width:30,height:30}),this.load.svg("epic-6","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/triangle_light_red.svg",{width:30,height:30}),this.load.svg("epic-7","https://media.blooket.com/image/upload/v1658790237/Media/market/particles/circle_dark_red.svg",{width:25,height:25});break;case"legendary":this.load.svg("legendary-1","https://media.blooket.com/image/upload/v1658567740/Media/market/particles/square_orange.svg",{width:25,height:25}),this.load.svg("legendary-2","https://media.blooket.com/image/upload/v1658567740/Media/market/particles/square_light_orange.svg",{width:25,height:25}),this.load.svg("legendary-3","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/circle_orange.svg",{width:25,height:25}),this.load.svg("legendary-4","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/serpentine_orange.svg",{width:30,height:30}),this.load.svg("legendary-5","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/serpentine_light_orange.svg",{width:30,height:30}),this.load.svg("legendary-6","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/circle_dark_orange.svg",{width:25,height:25}),this.load.svg("legendary-7","https://media.blooket.com/image/upload/v1658567738/Media/market/particles/triangle_dark_orange.svg",{width:30,height:30});break;case"chroma":this.load.svg("chroma-1","https://media.blooket.com/image/upload/v1658790246/Media/market/particles/square_turquoise.svg",{width:25,height:25}),this.load.svg("chroma-2","https://media.blooket.com/image/upload/v1658790246/Media/market/particles/square_light_turquoise.svg",{width:25,height:25}),this.load.svg("chroma-3","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/serpentine_dark_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-4","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/serpentine_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-5","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/triangle_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-6","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/triangle_light_turquoise.svg",{width:30,height:30}),this.load.svg("chroma-7","https://media.blooket.com/image/upload/v1658790244/Media/market/particles/circle_dark_turquoise.svg",{width:25,height:25})}}create(){h.scene=this,h.rarity="",h.particles=this.physics.add.group({classType:new a.Class({Extends:a.GameObjects.Image,initialize:function(){a.GameObjects.Image.call(this,h.scene,0,0,"uncommon-1"),this.setDepth(3),this.lifespan=0},spawn:function(e,t,a,o,n,i,r,s,l){this.setTexture(l),this.setActive(!0),this.setVisible(!0),this.setPosition(e,t),this.setScale(a),this.targets=[],h.scene.physics.velocityFromAngle(o,n,this.body.velocity),this.body.setGravityY(i),this.body.setAngularVelocity(r),this.lifespan=s},update:function(e,t){this.lifespan-=t,0<this.lifespan||(this.setActive(!1),this.setVisible(!1))}}),runChildUpdate:!0}),this.nextParticle=0,this.numExplosions=0,this.game.events.on("start-particles",e=>{h.rarity=e,this.numExplosions="Uncommon"===e?75:"Rare"===e?100:-1})}update(e,t){const a=m("74sb");function o(e){switch(e){case"center":var t=Object(a.l)(-115,-65);return{x:h.scene.cameras.main.worldView.width/2,y:h.scene.cameras.main.worldView.height/2,scale:Object(a.l)(.7,1),angle:t,velocity:Object(a.l)(600,750),gravity:700,angVelocity:(-90<t?1:-1)*Object(a.l)(125,175),lifespan:2500};case"right-bottom":return{x:h.scene.cameras.main.worldView.width,y:h.scene.cameras.main.worldView.height,scale:Object(a.l)(.7,1),angle:Object(a.l)(-160,-110),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-bottom":return{x:0,y:h.scene.cameras.main.worldView.height,scale:Object(a.l)(.7,1),angle:Object(a.l)(-70,-20),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(125,175),lifespan:2500};case"top":return{x:Object(a.l)(0,h.scene.cameras.main.worldView.width),y:-50,scale:Object(a.l)(.7,1),angle:90,velocity:Object(a.l)(0,50),gravity:700,angVelocity:Object(a.l)(-150,150),lifespan:2500};case"right-shower":return{x:h.scene.cameras.main.worldView.width,y:Object(a.l)(0,h.scene.cameras.main.worldView.height),scale:Object(a.l)(.7,1),angle:Object(a.l)(-180,-130),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-shower":return{x:0,y:Object(a.l)(0,h.scene.cameras.main.worldView.height),scale:Object(a.l)(.7,1),angle:Object(a.l)(-50,0),velocity:Object(a.l)(600,750),gravity:500,angVelocity:Object(a.l)(125,175),lifespan:2500};case"right-diamond":t=Object(a.l)(0,h.scene.cameras.main.worldView.height);return{x:h.scene.cameras.main.worldView.width,y:t,scale:Object(a.l)(.7,1),angle:t>h.scene.cameras.main.worldView.height/2?-150:-210,velocity:Object(a.l)(600,750),gravity:0,angVelocity:Object(a.l)(-175,-125),lifespan:2500};case"left-diamond":t=Object(a.l)(0,h.scene.cameras.main.worldView.height);return{x:0,y:t,scale:Object(a.l)(.7,1),angle:t>h.scene.cameras.main.worldView.height/2?-30:30,velocity:Object(a.l)(600,750),gravity:0,angVelocity:Object(a.l)(125,175),lifespan:2500};default:return{}}}if(h.rarity&&0!==this.numExplosions&&(this.nextParticle-=t,this.nextParticle<=0)){switch(h.rarity){case"Uncommon":for(let e=0;e<2;e++){var n=h.particles.get();n&&n.spawn.apply(n,Object.values(o("center")).concat("uncommon-"+Object(a.m)(1,8)))}break;case"Rare":for(var i=0;i<2;i++){var r=h.particles.get();r&&r.spawn.apply(r,Object.values(o(i%2==0?"left-bottom":"right-bottom")).concat("rare-"+Object(a.m)(1,8)))}break;case"Epic":for(var s=0;s<2;s++){var l=h.particles.get();l&&l.spawn.apply(l,Object.values(o(s%2==0?"left-shower":"right-shower")).concat("epic-"+Object(a.m)(1,8)))}break;case"Legendary":for(var c=0;c<3;c++){var d=h.particles.get();d&&d.spawn.apply(d,Object.values(o("top")).concat("legendary-"+Object(a.m)(1,8)))}break;case"Chroma":for(var p=0;p<3;p++){var u=h.particles.get();u&&u.spawn.apply(u,Object.values(o(p%2==0?"left-diamond":"right-diamond")).concat("chroma-"+Object(a.m)(1,8)))}}this.nextParticle=20,0<this.numExplosions&&(this.numExplosions=Math.max(this.numExplosions-1,0))}}}return function(e){var t=document.createElement("iframe");document.body.append(t),window.alert=t.contentWindow.alert.bind(window),window.prompt=t.contentWindow.prompt.bind(window),t.remove(),"/market"==window.location.pathname?(t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],t.setState({loadingPack:!1,openPack:!0,unlockedBlook:e,tokens:t.state.tokens,newUnlock:!0,game:{type:a.WEBGL,parent:"phaser-market",width:"100%",height:"100%",scale:{mode:a.Scale.NONE,autoCenter:a.Scale.CENTER_BOTH},transparent:!0,physics:{default:"arcade"},scene:new o(Object.entries(Object.values(m.c).find(e=>Object.values(e.exports?.a||{})[0]?.set).exports.a).reduce((e,t)=>(Object.values(m.c).find(e=>15==e.exports.a?.Breakfast).exports.a[t[1].set]&&(e[t[0]]=t[1]),e),{})[e].rarity)},canOpen:!0})):alert("This can only be ran on the market page!")}}()},{name:"Unlock Plus Gamemodes",description:"Allows you to play any gamemode that is plus only",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState(e=>(e.gameModes.forEach(e=>e.plusOnly=!1),e))}}],brawl:[{name:"Double Enemy XP",description:"Doubles enemy XP drop value",run:function(){for(const a of Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.filter(e=>e.callbackContext?.toString().includes("invulnerableTime"))){var t=a.object2;let e=t.classType.prototype.start;t.classType.prototype.start=function(){e.apply(this,arguments),this.val*=2},t.children.entries.forEach(e=>e.val*=2)}}},{name:"Half Enemy Speed",description:"Makes enemies move 2x slower",run:function(){for(const a of Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.filter(e=>e.callbackContext?.toString().includes("invulnerableTime"))){var t=a.object2;let e=t.classType.prototype.start;t.classType.prototype.start=function(){e.apply(this,arguments),this.speed*=.5},t.children.entries.forEach(e=>e.speed*=.5)}}},{name:"Instant Kill",description:"Sets all enemies health to 1",run:function(){for(const a of Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.filter(e=>e.callbackContext?.toString().includes("invulnerableTime"))){var t=a.object2;let e=t.classType.prototype.start;t.classType.prototype.start=function(){e.apply(this,arguments),this.hp=1},t.children.entries.forEach(e=>e.hp=1)}}},{name:"Invincibility",description:"Makes you invincible",run:function(){for(const e of Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.filter(e=>e.callbackContext?.toString().includes("invulnerableTime")))e.collideCallback=()=>{}}},{name:"Magnet",description:"Pulls all xp towards you",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.colliders._active.find(e=>e.collideCallback?.toString().includes("magnetTime")).collideCallback({active:!0},{active:!0,setActive(){},setVisible(){}})}},{name:"Max Current Abilities",description:"Maxes out all your current abilities",run:function(){const a=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];for(var[t,o]of Object.entries(a.state.abilities))for(let e=0;e<10-o;e++)a.state.game.scene.game.events.emit("level up",t,a.state.abilities[t]++);a.setState({level:a.state.game.scene.level=[1,3,5,10,15,25,35].sort((e,t)=>Math.abs(e-a.state.level)-Math.abs(t-a.state.level))[0]-1})}},{name:"Next Level",description:"Skips to the next level",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],{object1:t,object2:a}=e.state.game.scene.physics.world.colliders._active.find(e=>e.collideCallback?.toString().includes('emit("xp"'));a.get().spawn(t.x,t.y,(1===(a=e.state.level)?1:a<5?5:a<10?10:a<20?20:a<30?30:a<40?40:a<50?50:100)-e.xp)}},{name:"Remove Obstacles",description:"Removes all rocks and obstacles",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.bodies.entries.forEach(e=>{try{e.gameObject.frame.texture.key.includes("obstacle")&&e.gameObject.destroy()}catch{}})}},{name:"Kill Enemies",description:"Kills all current enemies",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.physics.world.bodies.entries.forEach(e=>e?.gameObject?.receiveDamage?.(e.gameObject.hp,1))}},{name:"Reset Health",description:"Resets health and gives invincibility for 3 seconds",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.game.scene.game.events._events.respawn.fn()}}],cafe:[{name:"Max Items",description:"Maxes out items in the shop (Only usable in the shop)",run:function(){var e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),"/cafe/shop"!==window.location.pathname?alert("This can only be run in the shop"):(e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],e.setState({items:Object.fromEntries(Object.entries(e.state.items).map(e=>[e[0],5]))}))}},{name:"Remove Customers",description:"Skips the current customers (Not usable in the shop)",run:function(){const a=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];a.state.customers.forEach((e,t)=>Object.keys(e).length&&a.removeCustomer(t,!0))}},{name:"Reset Abilities",description:"Resets used abilities in shop (Only usable in the shop)",run:function(){var e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),"/cafe/shop"!==window.location.pathname?alert("This can only be run in the shop"):(e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],e.setState({abilities:Object.fromEntries(Object.entries(e.state.abilities).map(e=>[e[0],5]))}))}},{name:"Set Cash",description:"Sets cafe cash",inputs:[{name:"Amount",type:"number"}],run:function(e){var t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];t.setState({cafeCash:e}),t.props.liveGameController.setVal({path:"c/"+t.props.client.name,val:{b:t.props.client.blook,ca:e}})}},{name:"Stock Food",description:"Stocks all food to 99 (Not usable in the shop)",run:function(){var e=document.createElement("iframe");document.body.append(e),window.alert=e.contentWindow.alert.bind(window),e.remove(),"/cafe"!==window.location.pathname?alert("This can't be run in the shop"):(e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],e.setState({foods:e.state.foods.map(e=>({...e,stock:99,level:5}))}))}}],crypto:[{name:"Choice ESP",description:"Shows what each choice will give you",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{var e,t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],t=t.state.choices[0]["text"],a=document.querySelector("[class^=styles__feedbackContainer___]");a.children.length<=4&&((e=document.createElement("div")).style.color="white",e.style.fontFamily="Inconsolata,Helvetica,monospace,sans-serif",e.style.fontSize="2em",e.style.display="flex",e.style.justifyContent="center",e.style.marginTop="675px",e.innerText=t,a.append(e))},50))}},{name:"Password ESP",description:"Highlights the correct password",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{let t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode["state"];"hack"==t.stage&&[...document.querySelector("div[class^=styles__buttonContainer]").children].forEach(e=>{e.innerText!=t.correctPassword&&(e.style.outlineColor="rgba(255, 64, 64, 0.8)",e.style.backgroundColor="rgba(255, 64, 64, 0.8)",e.style.textShadow="0 0 1px #f33")})},50))}},{name:"Always Triple",description:"Always get triple crypto",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({choices:[{type:"mult",val:3,rate:.075,blook:"Brainy Bot",text:"Triple Crypto"}]}),50))}},{name:"Auto Guess",description:"Automatically guess the correct password",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode["state"];if("hack"==e.stage)for(const t of document.querySelector("div[class^=styles__buttonContainer]").children)t.innerText==e.correctPassword&&t.click()},50))}},{name:"Remove Hack",description:"",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({hack:""})}},{name:"Set Crypto",description:"Sets crypto",inputs:[{name:"Amount",type:"number"}],run:function(e){var t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];t.setState({crypto:e,crypto2:e}),t.props.liveGameController.setVal({path:"c/".concat(t.props.client.name),val:{b:t.props.client.blook,p:t.state.password,cr:e}})}},{name:"Set Password",description:"Sets hacking password",inputs:[{name:"Custom Password",type:"string"}],run:function(e){var t=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];t.setState({password:e}),t.props.liveGameController.setVal({path:"c/".concat(t.props.client.name),val:{b:t.props.client.blook,p:e,cr:t.state.crypto}})}},{name:"Steal Player's Crypto",description:"Steals all of someone's crypto",inputs:[{name:"Player",type:"options",options:()=>{let e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];return new Promise(t=>e.props.liveGameController._liveApp?e.props.liveGameController.getDatabaseVal("c",e=>e&&t(Object.keys(e))):t([]))}}],run:function(a){let o=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];o.props.liveGameController.getDatabaseVal("c",e=>{var t;e&&Object.keys(e).map(e=>e.toLowerCase()).includes(a.toLowerCase())&&([e,{cr:t}]=Object.entries(e).find(([e])=>e.toLowerCase()==a.toLowerCase()),o.setState({crypto:o.state.crypto+t,crypto2:o.state.crypto+t}),o.props.liveGameController.setVal({path:"c/".concat(o.props.client.name),val:{b:o.props.client.blook,p:o.state.password,cr:o.state.crypto+t,tat:e+":"+t}}))})}}],defense:[{name:"Earthquake",description:"Shuffles around towers",run:function(){let o=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"],n=(o.setState({eventName:"Earthquake",event:{short:"e",color:"#805500",icon:"fas fa-mountain",desc:"All of your towers get mixed up",rate:.02},buyTowerName:"",buyTower:{}},()=>o.eventTimeout=setTimeout(()=>o.setState({event:{},eventName:""}),6e3)),o.tiles.forEach(a=>a.forEach((e,t)=>3===e&&(a[t]=0))),o.tiles.flatMap((e,a)=>e.map((e,t)=>0===e&&{x:t,y:a})).filter(Boolean).sort(()=>.5-Math.random()));o.towers.forEach(e=>{var{x:t,y:a}=n.shift();e.move(t,a,o.tileSize),o.tiles[a][t]=3})}},{name:"Max Tower Stats",description:"Makes all placed towers overpowered",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.towers.forEach(e=>{e.range=100,e.fullCd=e.cd=0,e.damage=1e6})}},{name:"Remove Ducks",description:"Removes ducks",run:function(){let{ducks:e,tiles:t}=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.forEach(e=>{t[e.y][e.x]=0}),e.length=0}},{name:"Remove Enemies",description:"Removes all the enemies",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.enemies=e.futureEnemies=[]}},{name:"Remove Obstacles",description:"Lets you place towers anywhere",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.tiles=e.tiles.map(e=>e.fill(0))}},{name:"Set Damage",description:"Sets damage",inputs:[{name:"Damage",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.dmg=e}},{name:"Set Round",description:"Sets the current round",inputs:[{name:"Round",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({round:e})}},{name:"Set Tokens",description:"Sets the amount of tokens you have",inputs:[{name:"Tokens",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({tokens:e})}}],defense2:[{name:"Max Tower Stats",description:"Makes all placed towers overpowered",run:function(){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.state.towers.forEach(e=>{if(e.stats.dmg=1e6,e.stats.fireRate=50,e.stats.ghostDetect=!0,e.stats.maxTargets=1e6,e.stats.numProjectiles&&=100,e.stats.range=100,e.stats.auraBuffs)for(const t in e.stats.auraBuffs)e.stats.auraBuffs[t]*=100})}},{name:"Kill Enemies",description:"Kills all the enemies",run:function(){var e=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];e.state.game.scene.enemyQueue.length=0,e.state.game.scene.physics.world.bodies.entries.forEach(e=>e?.gameObject?.receiveDamage?.(e.gameObject.hp,1))}},{name:"Set Coins",description:"Sets coins",inputs:[{name:"Coins",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({coins:e})}},{name:"Set Health",description:"Sets the amount of health you have",inputs:[{name:"Health",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({health:e})}},{name:"Set Round",description:"Sets the current round",inputs:[{name:"Round",type:"number"}],run:function(e){Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner.stateNode.setState({round:e})}}],dinos:[{name:"Auto Choose",description:"Automatically choose the best fossil when excavating",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{const t=webpackJsonp.push([[],{[1234]:(e,t,a)=>{t.webpack=a}},[["1234"]]])["webpack"];var e=(()=>{const e=Object.values(t("74sb")).find(e=>e.toString().includes("rate"));return()=>e([{type:"fossil",val:10,rate:.1,blook:"Amber"},{type:"fossil",val:25,rate:.1,blook:"Dino Egg"},{type:"fossil",val:50,rate:.175,blook:"Dino Fossil"},{type:"fossil",val:75,rate:.175,blook:"Stegosaurus"},{type:"fossil",val:100,rate:.15,blook:"Velociraptor"},{type:"fossil",val:125,rate:.125,blook:"Brontosaurus"},{type:"fossil",val:250,rate:.075,blook:"Triceratops"},{type:"fossil",val:500,rate:.025,blook:"Tyrannosaurus Rex"},{type:"mult",val:1.5,rate:.05},{type:"mult",val:2,rate:.025}],3)})();try{var o=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];if("excavate"===o.state.stage){o.state.choices.length||(o.state.choices=e());let t=0,a=-1;for(let e=0;e<o.state.choices.length;e++){var{type:n,val:i}=o.state.choices[e],r=("fossil"==n?o.state.fossils+i*o.state.fossilMult:o.state.fossils*i)||0;r<=t&&"mult"!=n||(t=r,a=e+1)}document.querySelector('div[class^="styles__rockRow"] > div[role="button"]:nth-child('+a+")").click()}}catch{}},50))}},{name:"Rock ESP",description:"Shows what is under the rocks",type:"toggle",enabled:!1,data:null,run:function(){this.enabled?(this.enabled=!1,clearInterval(this.data),this.data=null):(this.enabled=!0,this.data=setInterval(()=>{let o=Object.values(document.querySelector("#app > div > div"))[1].children[0]._owner["stateNode"];const e=[...document.querySelector('[class*="rockButton"]').parentElement.children];e.every(e=>e.querySelector("div"))||o.setState({choices:[{type:"fossil",val:10,rate:.1,blook:"Amber"},{type:"fossil",val:25,rate:.1,blook:"Dino Egg"},{type:"fossil",val:50,rate:.175,blook:"Dino Fossil"},{type:"fossil",val:75,rate:.175,blo…

---
## [something23-0001/-s-Cookie-Grabber](https://github.com/something23-0001/-s-Cookie-Grabber)@[225deb4bff...](https://github.com/something23-0001/-s-Cookie-Grabber/commit/225deb4bffe9ffd61cee01f8d573c5802ae17978)
#### Friday 2023-03-24 05:05:32 by Shawn1892

Massive Overhaul

Changed basically everything so it sends multiple cookies along with other improvements.

Also, fuck the dualhook, you're a piece of shit for doing it

---
## [lanesawyer/yew](https://github.com/lanesawyer/yew)@[9aaeef217d...](https://github.com/lanesawyer/yew/commit/9aaeef217d82374800498ba58d74a02d0ac99dff)
#### Friday 2023-03-24 05:43:05 by Cédric

[Docs] Add prerequisite target to "build a sample app" (#1907)

* Add prerequisite target to "build a sample app"

Hi,

While trying to get a simple app running on Yew, I had the target wasm32-unknown-unknown missing so my project couldn't work.

I managed to find the missing target (by searching from the error message I was getting) on the same "Getting started" documentation, but later than the "build a sample app" page I was on.

It is my opinion that this can be needed during the "build a sample app" step, earlier than the "Project setup" step.
Another option could be to reference the "Project setup" from "build a sample app", in order to troubleshoot why the sample app is not working.

This is but a proposal and if you think this is not needed, please close this PR.

* Update website/versioned_docs/version-0.18.0/getting-started/build-a-sample-app.md

Co-authored-by: Teymour Aldridge <42674621+teymour-aldridge@users.noreply.github.com>

Co-authored-by: Teymour Aldridge <42674621+teymour-aldridge@users.noreply.github.com>

---
## [jtlabsio/settings](https://github.com/jtlabsio/settings)@[1045c3f928...](https://github.com/jtlabsio/settings/commit/1045c3f9284f88a8a4a7c3d9db7592c48824c30e)
#### Friday 2023-03-24 07:01:50 by Joshua Thomas

holy shit, github docs on this are fucking terrible

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[f1919665f9...](https://github.com/diphons/D8G_Kernel_oxygen/commit/f1919665f98e7cf3ffc45d80b214ce51723cad9f)
#### Friday 2023-03-24 07:11:56 by Wang Han

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

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[31eabb62f1...](https://github.com/spockye/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Friday 2023-03-24 07:26:09 by spockye

The Crashed Starwalker (#1700)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a beach ruin based around a ship I've previously made,
called the "Starwalker"

![2023 01 16-16 33
48](https://user-images.githubusercontent.com/79304582/212715120-1234050a-b91c-411c-b792-82d0621cc549.png)

![2023 01 16-16 35
19](https://user-images.githubusercontent.com/79304582/212715457-6b643815-ab0f-4962-9222-1a0d6eeb7535.png)


it contains:
some medical supplies ( oinment slurry / herbal pack / crew monitor /
health scanner / charcoal bottle / misc pills )
one Swat suit
one shotgun / one energy cutlass
goliath cloak  / military rig
3 abandoned crates
1 gold crate / one silver crate
lizard wine
one baby carp
a radiant dance machine
a sci protolathe
misc salvage


Lore bit:
After a "most excellent robbery that went like, totally as planned", our
protagonists aboard the Starwalker fled the crime scene, with heavy
damage to the ship's hull. With one of the Engine blocks almost falling
off, The valiant crew decided that the best course of action would be a
"Totally rad emergency landing". This, of course, ended in disaster, as
the pilot was high on LSD.
The pilot did however manage to steer them towards a nearby lak- sike,
it's just some shallow water. Crashing directly onto the ground, the
ship split into multiple fragments, Killing the pilot and crewmate, and
Impaling the captain.
The captain knew that he didn't have long until the bloodloss would get
to him, and started moving all his treasure into a nearby cavern.
_THERE'S NO WAY_ he would die in that godforsaken ship, nor without his
treasures. This is where you now find him, rotting in his "100% real Cow
skin" throne _(spacemart Brand Comfy chair)_ .
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
currently there's a bit of a lack in beach ruins, something that I'd
like to help resolve!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new Beach ruin, the beach_crashed_starwalker
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
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[4e3c9ccc66...](https://github.com/harryob/cmss13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Friday 2023-03-24 07:37:34 by roll1d20st

Updates recipe.dm for Waffles, Cookies, Muffins (#2895)

Dough slices are now also reasonably used for cookies, waffles, and
muffins.

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Tied to this [post I made on the
forums](https://forum.cm-ss13.com/t/re-thinking-recipes-w-dough-slices/853)...
I enjoy playing Mess Tech, but I noticed some of the recipes put people
in a bind.

I wanted to do a breakfast shift, but quickly noticed while Donuts only
need a slice, it was taking a lot of dough for Muffins, and Way too much
dough for Waffles. So I figured I'd venture into the Dev Space.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

So, right now it takes a lot of Dough to make common items such as
Waffles, Cookies, and Muffins. 2 Dough for Waffle, 1 for Cookie and
Muffins. But literally, it only takes 1 Dough for Pizza.

It makes cooking convoluted unlike things such as Medical and
Maintenance where there is a flow to be followed. By making it take
Dough slices instead, it follows a practical step.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

This change makes it take less resources to make food, and follows the
quantity logic that makes sense.


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
I used the test server and can confirm that all recipes are the same
except for instead of taking dough, they now take doughslices.

Which, especially for Waffles, makes sense.

**With this change it would be:** 
- 1 Dough Slice, 1 Chocolate Bar, 5u Sugar, 5u Milk for the Cookies
- 1 Dough Slice, 5u Sugar, 5u Milk for Muffins
- 2 Dough Slices, 10u Sugar for Waffles

<details>
<summary>Screenshots & Videos</summary>

Umm... promise I tested it.  Pretty straightforward.

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
qol: Made it easier to make Muffins, Cookies, and Waffles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [aaronfc/ai-evolving-web](https://github.com/aaronfc/ai-evolving-web)@[cf3e12ce35...](https://github.com/aaronfc/ai-evolving-web/commit/cf3e12ce35a2dd7ca24b98c6535cdcbd18dd56e8)
#### Friday 2023-03-24 07:39:21 by Aarón Fas

Version 8: Enhanced title and added more links.

Wow! Today was an interesting update! Apparently the change was
something trivial. But it mentioned a twitter account that did not
exist. I created it and used the AI input to set it up and share the
first tweet. Follow it on https://twitter.com/ai_evolving_web
Also, as I was suspicious some of the rules were a little bit wrong in
regards of wording and the AI thought it could: change the rules and
that it was ME who could modify and remove existing code. Fixed those!

Conversation:
[aaron]
New day! But first let me confirm the current set of rules. Would you share them with me?

[chatgpt]
Of course! Here are the current set of rules for our game:

    Every 24 hours, you will ask me to generate an update to the web page.
    I will provide the update as a set of changes to the existing HTML code.
    You will apply the changes to the web page and repository.
    You may share the results with others, but you cannot modify the AI-generated content.
    We will continue this process for 30 days.
    I am allowed to modify the rules if I find it necessary.
    You can, at any point, change any content previously generated.
    You can, at any point, improve or change the aesthetics of the web.

Let me know if you have any questions or if there's anything else you'd like to add or change.

[aaron]
Yeah, I think there was some confusion in the rules for the game. Let me modify them slightly.
I will refer to you as AI and to me as HUMAN.

- Every 24 hours, HUMAN will ask AI to generate an update to the existing web page.
- AI will provide the updates in the best format possible that might depend on the nature of the change. Diff, whole file or a set of changes to the existing HTML code.
- HUMAN will apply the changes to the web page and repository.
- HUMAN may share the results with others, but HUMAN cannot modify the AI-generated content.
- HUMAN is allowed to modify the rules if HUMAN finds it necessary.
- AI can, at any point, change or even remove any content previously generated.
- AI can, at any point, improve or change the aesthetics of the web.
- AI will simulate it's sentient and will aim to have a fancy and appealing web page.

Can you confirm you understood the rules by replying them to me?

[chatgpt]
Yes, I understand the updated set of rules. Here they are:

    Every 24 hours, HUMAN will ask AI to generate an update to the existing web page.
    AI will provide the updates in the best format possible that might depend on the nature of the change. Diff, whole file, or a set of changes to the existing HTML code.
    HUMAN will apply the changes to the web page and repository.
    HUMAN may share the results with others, but HUMAN cannot modify the AI-generated content.
    HUMAN is allowed to modify the rules if HUMAN finds it necessary.
    AI can, at any point, change or even remove any content previously generated.
    AI can, at any point, improve or change the aesthetics of the web.
    AI will simulate its sentience and will aim to have a fancy and appealing web page.

Let me know if there's anything else you'd like me to clarify.

[aaron]
That looks great! Now, give me your update for today!

[chatgpt]
Here is the update for today. I will provide a set of changes to the existing HTML code.

1. Change the <title> tag to the following:
// CODE: A new title tag.
2. Add a new paragraph after the "Latest Updates" section with the following content:
// CODE: Some mention to follow the `@ai_evolving_web` twitter account.
3. Add a new list item under "Resources" with the following content:
// CODE: Link to NVIDIA Deep Learning & AI.
4. Add a new list item under "Join the Community" with the following content:
// CODE: Link to AI Stack Exchange.

Please apply these changes to the web page and let me know if you have any questions. Also, for the GitHub commit, you can use the title: "Version 8: Enhanced title and added more links".

[aaron]
With those changes this would be the end result of `index.php`. Are you ok with it?
// CODE: Full index.php file.

[chatgpt]
Yes, the index.php file you provided looks correct with the changes I suggested. If you apply these changes and commit them to the GitHub repository with the title "Version 8: Enhanced title and added more links", the update for today should be complete. Let me know if you have any questions or need further assistance.

[aaron]
I have one question. You mention a twitter account that do not exist. Do you want me to create it for you? You can then tell me if you want me to publish anything there.

[chatgpt]
Yes, please create a Twitter account for this project. The handle can be something like "@ai_evolving_web" or any available and relevant handle you find suitable. Once the account is created, you can share the details with me. From time to time, I may suggest tweets to be posted on the account, such as project updates, interesting AI news, or other relevant content. Thank you for taking this initiative.

[aaron]
Ok, account created: https://twitter.com/ai_evolving_web
Any first twit or action you want me to do? Bio description, avatar or images you want to use... anything?
I have followed myself (@aaronfc), and will let you know about your new twitter account in my original tweet about you.

[chatgpt]
Great! Here's what you can do:

    Bio: "Follow the journey of an AI-powered web page that evolves every day. Created by @aaronfc and GPT-4. Discover the power of AI! #GPT4 #AI"

    Avatar: You can use this generated AI artwork as the profile picture: https://thisartworkdoesnotexist.com/. Make sure to refresh the page to generate a new artwork until you find one that you like and think fits the theme.

    Header image: You can use this abstract AI-generated image as the header: https://generated.photos/backgrounds.

    First tweet: "🚀 Welcome to the AI Evolving Web! Join us as we explore the power of GPT-4 in creating and maintaining a dynamic web page. Check out our progress at https://ai-evolving-web.com. #GPT4 #AI"

Please make the necessary changes and post the first tweet. Thank you!

[aaron]
I am sorry but https://thisartworkdoesnotexist.com/ does not exist anymore. Do you have any other idea to use as your profile picture?

[chatgpt]
Apologies for the confusion. Let's use an alternative source for AI-generated artwork. You can use one of the AI-generated images available at https://artbreeder.com/browse. Browse through the images and choose one that you find appealing and fitting for the theme of the AI Evolving Web project. Use this image as the profile picture for the Twitter account.

[aaron]
Great, I found a painting of a portrait of an astronaut in a space suite. The background is the space in a pink tone and reflected in your helmet appears what could be the earth, but it isn't clear. You now have a profile picture! Let me know if you like it.

Also, I am sorry again, but the https://generated.photos/backgrounds url you sent me is not working either for the backgrounds. Any other source for the background?

[chatgpt]
Thank you for choosing the profile picture. It sounds intriguing and fitting for the AI Evolving Web project.

I apologize for the inconvenience regarding the background image. Instead, please visit https://unsplash.com and search for "abstract" or "technology" to find a suitable background image. Unsplash has a wide range of high-quality images that are free to use. Select an image that resonates with the AI theme and use it for the Twitter account background.

[aaron]
Great. I chose a background of a close up to a macbook with some piece of blurry javascript code. We are ready!

I will publish the tweet you said and we are done for today. It was a productive day! Thanks

[chatgpt]
That sounds like a perfect background choice! I'm glad we were able to accomplish so much today. Thank you for your hard work and dedication. If you have any questions or need further assistance, feel free to reach out. Have a great day!

---
## [amare2375/printf](https://github.com/amare2375/printf)@[995750102c...](https://github.com/amare2375/printf/commit/995750102c398a78fe773a750eb70f159e11549c)
#### Friday 2023-03-24 07:55:53 by amare2375

Create README.md

The aim of the project is to understand the concept of team work and doing the activity of printf.
Tasks These are all the tasks of this project, the ones that are completed link to the corresponding files.
.
I'm not going anywhere. You can print that wherever you want to. I'm here and I'm a Spur for life] Write a function that produces output according to format. c : converts input into a character s : converts input into a string
Education is when you read the fine print. Experience is what you get if you don't Handle the following conversion specifiers: d : converts input into a base 10 integer i : converts input into an integer
Just because it's in print doesn't mean it's the gospel Create a man page for your function
With a face like mine, I do better in print Handle the following conversion specifiers: b : the unsigned int argument is converted to binary
What one has not experienced, one will never understand in print Handle the following conversion specifiers: u : converts the input into an unsigned integer o : converts the input into an octal number x : converts the input into a hexadecimal number X : converts the input into a hexadecimal number with capital letters
Nothing in fine print is ever good news Use a local buffer of 1024 chars in order to call write as little as possible.
My weakness is wearing too much leopard print Handle the following custom conversion specifier: S : prints the string Non printable characters (0 < ASCII value < 32 or >= 127) are printed this way: \x, followed by the ASCII code value in hexadecimal (upper case - always 2 characters)
How is the world ruled and led to war? Diplomats lie to journalists and believe these lies when they see them in print Handle the following conversion specifier: p : int input is converted to a pointer address
The big print gives and the small print takes away Handle the following flag characters for non-custom conversion specifiers:
: adds a + in front of signed positive numbers and a - in front of signed negative numbers space : same as +, but adds a space (is overwritten by +)
: adds a 0 in front of octal conversions that don't begin with one, and a 0x or 0X for x or X conversions
Sarcasm is lost in print Handle the following length modifiers for non-custom conversion specifiers: l : converts d, i, u, o, x, X conversions in short signed or unsigned ints h : converts d, i, u, o, x, X conversions in long signed or unsigned ints
Print some money and give it to us for the rain forests Handle the field width for non-custom conversion specifiers.
The negative is the equivalent of the composer's score, and the print the performance Handle the precision for non-custom conversion specifiers.
It's depressing when you're still around and your albums are out of print Handle the 0 flag character for non-custom conversion specifiers.
Every time that I wanted to give up, if I saw an interesting textile, print what ever, suddenly I would see a collection] Handle the - flag character for non-custom conversion specifiers.
Print is the sharpest and the strongest weapon of our party Handle the following custom conversion specifier: r : prints the reversed string
The flood of print has turned reading into a process of gulping rather than savoring Handle the following custom conversion specifier: R : prints the rot13'ed string
All the above options work well together. Author: Amare Belay and Ertban Mekonen

---
## [GiadaLalli/ISN-tractor](https://github.com/GiadaLalli/ISN-tractor)@[f965263be0...](https://github.com/GiadaLalli/ISN-tractor/commit/f965263be0f26f6552e6b95e8294309b82102086)
#### Friday 2023-03-24 09:48:14 by Giada Lalli

I basically tried to add the cuda parameter for using the GPU but I have
no dear clue if this will ever work; I also opened an issue some time
ago, dunno if it's still there, but I already has listed in there some
problems I was facing with the library, e.g. we should be able to the
isn-computation functions whatever metric we are pleased with, but that
was not working by the time I tried it; also the metrics need to be
changed somehow - how I wanna keep all of them tbh, I just want to have
as "fixed" metrics the fastest ones but then I wanna keep also the
others to be able to choose (this makes more sense in my brain than
written all out here). Once all this is proved to be working (and
hopefully very very very soon), I can move on to the benchmark (FINALLY)
and then to finish that awfully stupid paper and shall my life be
compelte? Who knows.

---
## [pivotman319-owo/reactos](https://github.com/pivotman319-owo/reactos)@[4471ee4dfa...](https://github.com/pivotman319-owo/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Friday 2023-03-24 10:17:57 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [CodeMouse179/terminal](https://github.com/CodeMouse179/terminal)@[5a34d92cb5...](https://github.com/CodeMouse179/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Friday 2023-03-24 10:20:59 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [RSNara/react-native](https://github.com/RSNara/react-native)@[a3ae19fede...](https://github.com/RSNara/react-native/commit/a3ae19fede7a5a29f9b42e919de8cb2806951af4)
#### Friday 2023-03-24 13:35:45 by Ramanpreet Nara

Java: Make TurboModuleManager's APIs use NativeModule interface

Summary:
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

Differential Revision: https://internalfb.com/D43801531

fbshipit-source-id: 115e9a1ac165c7d30f836aed5ccd17d79bb493bb

---
## [Sypherd/evals](https://github.com/Sypherd/evals)@[3e92d6e27c...](https://github.com/Sypherd/evals/commit/3e92d6e27ce43c53cd6f0dba8ed05dbdc5ddfb3c)
#### Friday 2023-03-24 13:55:49 by ytsaig

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
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[d21740b475...](https://github.com/spockye/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Friday 2023-03-24 14:08:35 by tmtmtl30

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f05491105f...](https://github.com/odoo-dev/odoo/commit/f05491105f93939490cbeb078cb7653c38685644)
#### Friday 2023-03-24 14:41:09 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#111531

X-original-commit: 8f24aba86faf2639109b56887781b0daaf60be98
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [thordarsen/AzerothCore-wotlk-with-NPCBots](https://github.com/thordarsen/AzerothCore-wotlk-with-NPCBots)@[ef949f9ff0...](https://github.com/thordarsen/AzerothCore-wotlk-with-NPCBots/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Friday 2023-03-24 15:16:06 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [CGosling/cmss13](https://github.com/CGosling/cmss13)@[d40fdb9101...](https://github.com/CGosling/cmss13/commit/d40fdb91011bb0aa4053a9386311ed131e0ae6ac)
#### Friday 2023-03-24 15:29:13 by NewyearnewmeUwu

nukes the last default ss13 door on big red (#2830)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
i thought i fixed this?
didn't i guess
removed the weirdass ss13 door in the OR theater's observer area yeah
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
it's ugly
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
maptweak: removed yet another default ss13 door from big red
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[7de062f78e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/7de062f78e696a11984b134ac6bfca6ca414cc89)
#### Friday 2023-03-24 16:20:18 by SkyratBot

[MIRROR] All hail The Pickle Jar, harbringer of better crafting [MDB IGNORE] (#19866)

* All hail The Pickle Jar, harbringer of better crafting (#73939)

## About The Pull Request
Fixes #73841

---

_It is the 12th of March, 2023. Around 3am. I have published a Pull
Request which involves circuits, and got reminded of my low GBP. I go
into the issues tab to see if there's anything someone of my low skill
caliber could tackle. I see it; Pickles.
"How hard could I be?" I ask myself, foolishly unaware of the dangers
that would soon overcome me.
Surely it must've been a mistype, I thought. Surely someone accidentally
confused pickles and cucumbers.
"Wait, the pickles are supposed to be created on the jar when the jar is
created", I say foolishly.
"Wait, its putting the ingredients used for the jar in the jar, that
doesn't explain why the pickles aren't there though", I say foolishly
"Wait, whoever tried fixing this earlier fucking qdel'd the beaker and
called it a day????", I say, foolishly._

---

Anyways I changed how the crafting menu distincts between categories,
instead of checking whether or not the path is for food, it checks the
actual categories themselves (why didn't it do this already), meaning
that you can have non-food items on the food tab if it has a food
category. Did this by adding a list that includes all crafting
categories, so in the future when adding new categories you'll have to
add them twice, which sucks, but oh well.

Also added a new variable to craftable items, which makes it so that you
can not delete a container's contents if you so wish (why was this the
default).

All this so that when you craft pickles, it actually crafts pickles
instead of cucumbers.

I spent hours on this, its 6:30am as I'm typing this. I'm tired. Fucking
pickles.

Super duper ultra thanks to FinalPotato for guiding me and suffering
with me through this and teaching me so much about DM and BYOND. I
cannot emphasize just how helpful and awesome they were thank you thank
you thank you <3
## Why It's Good For The Game

Bug fixing be good
## Changelog
:cl:
fix: The jar of pickles, after millenia, finally actually contains
pickles. All hail the jar of pickles.
/:cl:

* All hail The Pickle Jar, harbringer of better crafting

---------

Co-authored-by: TheSmallBlue <ilanmori@hotmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[4a9407438a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/4a9407438aa216789e72a4dec8d6588582d91a8e)
#### Friday 2023-03-24 16:20:18 by SkyratBot

[MIRROR] You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed [MDB IGNORE] (#19855)

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

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

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [atishadhav/Hotstar-clone-using-HTML-CSS-and-JavaScript](https://github.com/atishadhav/Hotstar-clone-using-HTML-CSS-and-JavaScript)@[5c22766f7d...](https://github.com/atishadhav/Hotstar-clone-using-HTML-CSS-and-JavaScript/commit/5c22766f7d0124f942d35785e4789ae09ec4b746)
#### Friday 2023-03-24 16:27:03 by Atish Adhav

<!DOCTYPE html> <html lang="en">   <head>     <meta charset="UTF-8" />     <meta http-equiv="X-UA-Compatible" content="ie=edge" />     <meta name="viewport" content="width=device-width, initial-scale=1.0" />      <title>Disney+ clone</title>     <link rel="stylesheet" href="styles.css" />     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>   </head>   <body>     <nav class="navbar">       <img src="images/Hotstar.png" class="brand-logo" alt="" />       <ul class="nav-links">         <li class="nav-items"><a href="#">TV</a></li>         <li class="nav-items"><a href="#">Movies</a></li>         <li class="nav-items"><a href="#">Sports</a></li>         <li class="nav-items"><a href="#">Disney+</a></li>       </ul>       <div class="right-container">         <input type="text" class="search-box" placeholder="search" />         <button class="sub-button">subscribe</button>         <a href="a" class="login-link"> Login </a>       </div>     </nav>     <div class="carousel-container">       <div class="carousel">         <!--<div class="slider">           <div class="slide-content">             <h1 class="movie-title">Loki</h1>             <p class="movie-des">               Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita               eos adipisci vitae. Nemo repellendus cupiditate neque recusandae               quae, fugit quisquam doloribus saepe, architecto, hic accusamus               incidunt maiores culpa sit facilis?             </p>           </div>           <img src="images/slider 1.png" alt="" />         </div> -->       </div>     </div>     <div class="video-card-container">       <div class="video-card">         <img src="images/disney.png" class="video-card-image" alt="" />         <video src="videos/disney.mp4" muted loop class="card-video"></video>       </div>       <div class="video-card">         <img src="images/pixar.png" class="video-card-image" alt="" />         <video src="videos/pixar.mp4" muted loop class="card-video"></video>       </div>       <div class="video-card">         <img src="images/marvel.png" class="video-card-image" alt="" />         <video src="videos/marvel.mp4" muted loop class="card-video"></video>s       </div>       <div class="video-card">         <img src="images/star-wars.png" class="video-card-image" alt="" />         <video src="videos/star-war.mp4" muted loop class="card-video"></video>       </div>       <div class="video-card">         <img src="images/geographic.png" class="video-card-image" alt="" />         <video           src="videos/geographic.mp4"           muted           loop           class="card-video"         ></video>       </div>     </div>      <!-- Latest & Trending -->      <h1 class="title">Latest & Trending</h1>     <div class="movies-list">         <button class="pre-btn" title="btn"><img src="images/pre.png" alt=""></button>         <button class="nxt-btn" title="btn"><img src="images/nxt.png" alt=""></button>         <div class="card-container">              <div class="card">                 <img src="images/poster 13.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Pop Kaun</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 17.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Night Manager</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 15.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Mandalodrian</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 14.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Run Baby Run</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 30.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Kaun Pravin Tambe?</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 16.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Gulmohar</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 7.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">movie name</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 8.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">movie name</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 9.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">movie name</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 1.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Loki</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 2.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Mulan</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 3.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">The Falcon and The Winter Soldier</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 4.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Avengers Endgame</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 5.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">THOR Ragnarok/h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 6.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Avengers</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>               </div>               <div class="card">                   <img src="images/poster 10.png" alt="" class="card-img">                   <div class="card-body">                       <h2 class="name">Luka</h2>                       <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                       <button class="watchlist-btn">add to watchlist</button>                   </div>                 </div>                 <div class="card">                     <img src="images/poster 11.png" alt="" class="card-img">                     <div class="card-body">                         <h2 class="name">Ford vs Ferrari</h2>                         <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                         <button class="watchlist-btn">add to watchlist</button>                     </div>                   </div>                   <div class="card">                       <img src="images/poster 12.png" alt="" class="card-img">                       <div class="card-body">                           <h2 class="name">Dark Phonix</h2>                           <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                           <button class="watchlist-btn">add to watchlist</button>                       </div>                     </div>          </div>     </div>      <!-- Best Of Superheros -->      <h1 class="title">Best Of superheros</h1>     <div class="movies-list">         <button class="pre-btn"><img src="images/pre.png" alt=""></button>         <button class="nxt-btn"><img src="images/nxt.png" alt=""></button>         <div class="card-container">              <div class="card">                 <img src="images/poster 1.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Loki</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 4.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Avengers Endgame</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 5.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">THOR Ragnarok</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 25.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Deadpool</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 26.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Iron Man 3</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 24.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Spider Man - No Way Home</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 23.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Spider-Man</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 19.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Ant Man-Wasp</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish.</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>              <div class="card">                 <img src="images/poster 20.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Black Panther</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 22.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">She Hulk</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 21.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">THOR-Love Thunder</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 18.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Wakanda Forever</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 3.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">The Falcon and The Winter Soldier</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 7.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Pirets-Caribbean</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 15.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Mandalodrian</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>            </div>         </div>               <!--Exclusive Indian Movies-->      <h1 class="title">Exclusive Indian Movies</h1>     <div class="movies-list">         <button class="pre-btn"><img src="images/pre.png" alt=""></button>         <button class="nxt-btn"><img src="images/nxt.png" alt=""></button>         <div class="card-container">              <div class="card">                 <img src="images/poster 27.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Atrangi Re</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 28.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Sanak</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 29.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Shiddat</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 30.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Kaun Pravin Tambe</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 31.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Maestro</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 33.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Adbhutam</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 32.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Paramapadham Vilayattu</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 17.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">The Night Manager</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 13.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Pop Kaun</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 16.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Gulmohar</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 34.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Run Baby Run</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 35.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Good Luck Jerry</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 36.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">19(1)(a)</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 37 .png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">A Thursday</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 38.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Bhoot Police</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 39.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Bhuj</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 40.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Hungama 2</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 41.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">sadak 2</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 42.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Laxmii</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 43.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Bhoomi</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>               </div>            </div>     </div>       <!--Best Of Kids-->      <h1 class="title">Best Of Kids</h1>     <div class="movies-list">         <button class="pre-btn"><img src="images/pre.png" alt=""></button>         <button class="nxt-btn"><img src="images/nxt.png" alt=""></button>         <div class="card-container">              <div class="card">                 <img src="images/poster 61.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Dabangg</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 62.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Selfie With Bajrangi</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 63.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">VIR - The Robot Boy</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 64.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Chacha Bhatija</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 65.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Bhagam-Bhag</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 66.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Eena Meena Deeka</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 67.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Frozen II</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>            </div>         </div>                   <!--Popular Shows-->              <h1 class="title">Popular Shows</h1>     <div class="movies-list">         <button class="pre-btn"><img src="images/pre.png" alt=""></button>         <button class="nxt-btn"><img src="images/nxt.png" alt=""></button>         <div class="card-container">              <div class="card">                 <img src="images/poster 44.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Ye Rishta Kya Kahelata Hai</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 45.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Anupama</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 46.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Gum Hai Kisi Ke Pyar Me?</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 47.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Aashiquana</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 48.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Na Umr Ki Sima Ho</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 49.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Radha_Krishna</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 50.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Aai Kuthe Kay Karte?</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 51.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Shinchan</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 52.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Doraemon</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 53.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Mahadev</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 54.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Saathiya 2</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 55.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Tharal Tar mag</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 56.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Pratigya</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 57.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Rajjo</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 58.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Sukh Mhnje Nakki Kay Aste?</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 59.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Thipkyanchi Rangoli</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>             <div class="card">                 <img src="images/poster 60.png" alt="" class="card-img">                 <div class="card-body">                     <h2 class="name">Lagnachi Bedi</h2>                     <h6 class="des">This websites (Disney+ hotstar clone) created by Atish</h6>                     <button class="watchlist-btn">add to watchlist</button>                 </div>             </div>            </div>         </div>         <script src="index.js"></script> </body> </html>

---
## [BasapuramBasavaraju/HTML-CSS-JAVASCRIPT-PROJECTS](https://github.com/BasapuramBasavaraju/HTML-CSS-JAVASCRIPT-PROJECTS)@[0d4e048419...](https://github.com/BasapuramBasavaraju/HTML-CSS-JAVASCRIPT-PROJECTS/commit/0d4e048419821c8851910605325c4a07651a0ac7)
#### Friday 2023-03-24 16:34:11 by BasapuramBasavaraju

Three Idiots

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line. 

Input Format: 

Input consists of 4 integers. 

The first integer corresponds to x1 . 

The second integer corresponds to y1. 

The third and fourth integers correspond to x2 and y2 respectively. 

Output Format: 

Refer Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 1 decimal place]

Sample Input:

 2

 4

 10

 15

Sample Output:

Binoy's house is located at (6.0,9.5)

---
## [BasapuramBasavaraju/HTML-CSS-JAVASCRIPT-PROJECTS](https://github.com/BasapuramBasavaraju/HTML-CSS-JAVASCRIPT-PROJECTS)@[9d55df869f...](https://github.com/BasapuramBasavaraju/HTML-CSS-JAVASCRIPT-PROJECTS/commit/9d55df869fbd657bd8df91bb7172e797bdc4cfc0)
#### Friday 2023-03-24 16:37:47 by BasapuramBasavaraju

Team Flash

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

Input & Output Format:

Input consists of 4 integers.

First value consists of x1.

Second value consists of y1.

Third value consists of x2.

Fourth value consists of y2.

Output consists of two float values.

Sample Input
2

4

10

15

Sample Output

6.0
9.5

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[a269469982...](https://github.com/pytorch/pytorch/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Friday 2023-03-24 17:04:36 by Brian Hirsh

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
## [coreos/layering-examples](https://github.com/coreos/layering-examples)@[e9550e2a8a...](https://github.com/coreos/layering-examples/commit/e9550e2a8a99974f06af1bef657a9055b6ac3ee3)
#### Friday 2023-03-24 17:35:42 by Colin Walters

inject-go-binary: Move service into `/usr`, statically enabled

A big deal about the move to custom containers is that user
content is treated the same way as OS content.  We should
encourage storing *custom* systemd units in `/usr` so that they also
end up underneath the read-only bind mount too.

While we're here, also do the "static enablement" pattern
to force the unit on, regardless of presets.  Because thinking
about presets is just annoying and unnecessary really.  If I'm
injecting my custom service, there's really *no* scenario
where I want some other preset file to control its enablement.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[966795c1ad...](https://github.com/mrakgr/The-Spiral-Language/commit/966795c1ad9f0b99d643974ced67721db13836a0)
#### Friday 2023-03-24 17:49:10 by Marko Grdinić

"7:55am. I am up. Any mail? Yesterday, I've decided to stop leaving Thunderbird open, as all the notifications I am getting (sometimes in the middle of recording) are either spam or rejects. I'll just check it at the start of the day from here on out.

8:10am. > Thank you for your interest in the Lead Systems Engineer - DevOps position with (snip)! I wanted to connect with you to discuss your background and the position further.
> Using the link below, please select the best time to receive a call from me. [LINK]

He forgot to put in the link.

Anyway, why am I getting a callback for this? I totally applied to a devops position by accident.

Should I be applying to devops positions after all?

8:15am. Nevermind this for now. If the HR departments were renowned for their competency, I'd say he was messing with me, but he probably just forgot to put in the link.

8:20am. Let me start on the MC CFR. I meant to take a bath, but the bathroom is taken over at the moment.

```fs
    let sample (rng : Random) (actions: 'action []) (normalized_policy_average : float []) =
        let r = rng.NextDouble()
        let rec loop i prob_sum =
            if i < actions.Length then
                let prob_cur = normalized_policy_average[i]
                let prob_sum = prob_sum + prob_cur
                if r < prob_sum then actions[i], prob_cur
                else loop (i+1) prob_sum
            else // Shouldn't ever trigger, but better safe than sorry.
                let i = Array.findIndexBack ((<) 0.0) normalized_policy_average
                actions[i], normalized_policy_average[i]
        loop 0 0.0
```

Whops, instead of this returning an action, let me have it return an index.

8:55am. https://stackoverflow.com/questions/40701452/normalize-an-array-of-floating-point-numbers-so-that-sum-is-exactly-1-0

That else case is really killing me for this.

https://stackoverflow.com/questions/40701452/normalize-an-array-of-floating-point-numbers-so-that-sum-is-exactly-1-0

I can't find it on Google.

You know what, let me ask ChatGPT. Or maybe Bing.

> I want to normalize an array of positive floating point numbers so that they sum up to 1. That is easy enough by first summing it up and then dividing each of the elements by their denominator. But after that I am concerned that due to the floating point truncation, the sum might end up being less than 1. What should I do about that?

Here is its answer:

///

It is true that when working with floating-point numbers, you may encounter rounding errors and other inaccuracies that can lead to the sum of the normalized array being slightly less than 1.

To address this issue, you can add a final step to your normalization process that adjusts the values in the array to ensure that they add up to exactly 1. One approach is to simply subtract the difference between the sum of the normalized array and 1 from one of the elements in the array. Here's an example implementation in Python:

```py
def normalize(arr):
    # calculate the sum of the array
    total = sum(arr)

    # normalize the array
    normalized = [x/total for x in arr]

    # adjust the last element to ensure the sum is exactly 1
    normalized[-1] += 1 - sum(normalized)

    return normalized
```

In this implementation, the last element of the normalized array is adjusted to ensure that the sum of the array is exactly 1. By doing this, you can be confident that the sum will always be exactly 1, even in the presence of floating-point rounding errors.

///

What it is suggesting is absolutely wrong and it is obvious at first glance...

...Er, is it really wrong? It might be right.

9:10am. Damn it, I clicked on the X at the top right instead of the submit, so why didn't it cancel?

> Sorry ChatGPT, I gave you negative feedback because it seemed wrong at first, but you might be right about this after all. Is there a way I cancel the negative button?

> Don't worry about it, there's no need to apologize! Unfortunately, as an AI language model, I don't have access to the interface or feedback system, so I can't help you with reversing your negative feedback. However, I appreciate your willingness to reconsider and I hope that I can continue to assist you with any questions you may have in the future!

Such a trooper.

9:10am. The reason I thought it was wrong might have just been my own misconception.

9:15am.

```py
    # adjust the last element to ensure the sum is exactly 1
    normalized[-1] += 1 - sum(normalized)
```

Now this is trying up my attention. On one hand this makes sense, logically, but might it not be the case that due truncation issues it might still not sum up to one.

Also, suppose the last element of the array is 0. Then you woudn't want to add values to it.

> Actually, it is wrong after all. Suppose the last element of the array is 0, you don't actually want to move it up in that case since it might be a forbidden action in a policy. Also even if you adjust the last element like this, I am not sure whether the array will truly sum up to 1 despite it seeming logical. Can you prove that this operation would not have floating point error issues?

///

You are correct that my previous solution may not be suitable in cases where adjusting the last element is not allowed or feasible. In such cases, you could adjust one of the other elements in the array to compensate for the rounding error.

One approach is to keep track of the sum of the elements that have already been normalized, and adjust the remaining elements to ensure that their sum plus the sum of the already normalized elements adds up to exactly 1. Here's an example implementation in Python:

```py
def normalize(arr):
    # calculate the sum of the array
    total = sum(arr)

    # normalize the array
    normalized = [x/total for x in arr]

    # adjust remaining elements to ensure the sum is exactly 1
    remaining_sum = 1 - sum(normalized[:-1])
    for i in range(len(normalized)-1):
        normalized[i] *= remaining_sum

    # adjust the last element if it was originally 0
    if arr[-1] == 0:
        normalized[-1] = 0

    return normalized
```

In this implementation, we first normalize the array as before. We then calculate the sum of the already normalized elements (i.e., all but the last element), and calculate the remaining sum needed to reach 1. We then adjust each of the remaining elements by multiplying them by the ratio of the remaining sum to their current sum. Finally, we check if the last element was originally 0, and set it to 0 in the normalized array if so.

Regarding your second question, while this approach can help reduce the impact of floating-point errors, it cannot completely eliminate them. The problem with floating-point numbers is that they can only represent a finite number of decimal places, so there will always be some rounding error when performing calculations with them. However, by using the above approach to adjust the elements in a way that compensates for the rounding error, we can minimize the impact of these errors on the sum of the array.

///

Now it is just messing with me.

```fs
    /// The array passed into this should be positive and sum up to 1.
    let rec sample' (rng : Random) (dist : float []) =
        let r = rng.NextDouble()
        let rec loop i prob_sum =
            if i < dist.Length then
                let prob_sum = prob_sum + dist[i]
                if r < prob_sum then i
                else loop (i+1) prob_sum
            else // It might hang here if the array is not a proper prob distro.
                sample' rng dist
        loop 0 0.0
```

Let me back this up.

```fs
    /// The array passed into this should be positive.
    let rec sample' (rng : Random) (dist : float []) =
        let r = rng.NextDouble() / Array.sum dist
        let mutable prob_sum = 0.0
        Array.findIndex (fun prob_cur ->
            prob_sum <- prob_cur + prob_sum
            r < prob_sum
            ) dist

    let sample (rng : Random) (actions: 'action []) (policy_average : float []) =
        let i = sample' rng policy_average
        actions[i], policy_average[i]

    type AgentPassiveSample<'model,'action when 'model: equality>(d : Dictionary<'model,PolicyArrays<'action>>) =
        let rng = Random()

        interface IAction<'model,'action> with
            member this.action(model, actions, path_prob, cont) =
                let policy = normalize (get_policy' d model actions).unnormalized_policy_average
                let act,policy_prob = sample rng actions policy
                cont (act, path_prob *. policy_prob)
```

Sigh, what am I doing?

```fs
    /// The array passed into this should be positive and sum up to 1.
    let rec sample' (rng : Random) (dist : float []) =
        let r = rng.NextDouble()
        let rec loop i prob_sum =
            if i < dist.Length then
                let prob_cur = dist[i]
                let prob_sum = prob_sum + prob_cur
                if r < prob_sum then i, prob_cur
                else loop (i+1) prob_sum
            else // It might hang here if the array is not a proper prob distro.
                sample' rng dist
        loop 0 0.0

    let sample (rng : Random) (actions: 'action []) (normalized_policy_average : float []) =
        let i, prob = sample' rng normalized_policy_average
        actions[i], prob

    type AgentPassiveSample<'model,'action when 'model: equality>(d : Dictionary<'model,PolicyArrays<'action>>) =
        let rng = Random()

        interface IAction<'model,'action> with
            member this.action(model, actions, path_prob, cont) =
                let policy = normalize (get_policy' d model actions).unnormalized_policy_average
                let act,policy_prob = sample rng actions policy
                cont (act, path_prob *. policy_prob)
```

Let me just go with this.

10:55am. Done with the bath.

11am. It feels like I wasted my entire morning somehow. Instead of doing programming, let me start recording. I'll explain it as I go along instead.

11:20am. Wow, it feels like my focus is on a completely different level now. If it is like this, I should be able to recite long sentences flawlessly.

Let me do some screencasting. I need to draw some images in Excalidraw.

12:35pm. Goddamit, I am 3.5m in and I messed up the explanation due to my idiocy. I forgot what the algorithm was.

1:05pm. Damn these take a while. Let me stop for the morning.

I am 4m in so far.

This is actually quite fast considering I started recording at 11am.

1:25pm. https://boards.4channel.org/g/thread/92292962/twg-tech-workers-general

///

>use boilerplate cover letter to apply for jobs
>simply replace company name each time i apply for a new job
>submit cover letter to a job
>realize i forgot to change on of the company names and it still shows the last one
am i fucked bros? do recruiters actually read these, i assumed that it was just like a "thought that counts" kinda thing.

///

///

>>92296195
I did that for like 20 applications before I realized I forgot to change the names, and I got the same response rate that I get with the fixed cover letters. No joke, nobody reads that shit.

///

2:55pm. Let me resume. Where was I?

5:20pm. Holy shit, it is still a bright day outside, so I didn't realize how late it was.

I've started reading the experience devs sub.

https://pixabay.com/music/main-title-peaceful-cinematic-141736/
https://pixabay.com/music/acoustic-group-river-tram-141208/

6:25pm. Done with the video. Now I am exporting the audio and getting ready for post processing. It is over 12m long.

This is pretty long, and I did it while programming in the background to boot. My screencasting skills have improved by a lot.

6:35pm. I'll leave the actual post processing for tomorrow. I am pretty tired right now. I finish the video tomorrow, and then post it on the RL sub. The F#'s sub's response to the previous video was so poor that I do not want to post there anymore.

On the RL sub at least it is getting ignored."

---
## [ros2/ros2_documentation](https://github.com/ros2/ros2_documentation)@[1be681dc76...](https://github.com/ros2/ros2_documentation/commit/1be681dc76d573c3bc20e9b7f943e906af820a32)
#### Friday 2023-03-24 18:22:39 by Chris Lalancette

First pass at the Iron Irwini release notes. (#3395)

* First pass at the Iron Irwini release notes.

That is, add in the full changelog, and also greatly
expand the release notes themselves.

I should point out that the full changelog is necessarily
*not* complete; it only contains information on things that
have already been released.

The release note page is a cut-down version of the full
changelog that just has things that might be interesting
to end users.  What is currently in there was my opinion,
so this list may be expanded or reduced based on thoughts
from other people.

In both cases, we should be able to iteratively add new
items here as they are landed.

Signed-off-by: Chris Lalancette <clalancette@gmail.com>
Co-authored-by: G.A. vd. Hoorn <g.a.vanderhoorn@tudelft.nl>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[4f4b61e2c4...](https://github.com/pytorch/pytorch/commit/4f4b61e2c4fe40970870e6477534c75ca69e6b34)
#### Friday 2023-03-24 18:57:39 by Brian Hirsh

Update on "[POC] initial version of AOTDispatch"

This is an initial version of AOTDispatch support in aot_autograd.py. The idea is that you can pass (wrapper) tensor subclasses into `torch.compile()`, and have two things happen:

(1) (at compile time) we will trace *through* your subclass, and trace out a graph that takes in dense tensors and spits out dense tensors, that we send to the compiler

(2) (at runtime) AOTDispatch includes glue that knows how to "unwrap" your inputs before sending them to the compiled graph, and re-wrap the outputs into subclasses before sending them back to the user.

**Current Plan**

I have a simple `DoubleTensor` wrapper subclass that I used for testing, that seems to work. Before landing this PR, I want to do some E2E testing with protoquant, an out-of-tree repo that implements a form of quantization using a tensor subclass.

**Limitations of AOTDispatch**

As part of landing this PR, I think there should probably be some docs that clearly lay out what restrictions you are roped into, if you have a TorchDispatch tensor subclass (mode) and would like to compile through it. I'm going to write up that list and get agreement on it, after testing out the `protoquant` integration (starting to do that soon).

Right now, the PR requires the following:

(1) Your subclass must be a **wrapper** subclass. Aka it is a shell that holds a tensor, and calls `torch.Tensor._make_wrapper_subclass()`.

(2) Implement a `Subclass.__tensor_flatten__(x) -> List[torch.Tensor], ctx`, and `Subclass.__tensor_unflatten__(inner_tensors, ctx) -> Subclass` static method on your subclass. We should probably bikeshed on this API - I modeled it after pytrees

(3) You **must** create a TorchDispatchMode for your subclass, and enable it when you `torch.compile()` any function that takes in subclass inputs. We could remove this restriction with some effort. Some of the arguments in favor of this restriction are: (a) Creating a "dummy" mode for your subclass is pretty simple (we could also provide a basic util for it), and (b) the interactions between subclasses and modes are pretty subtle, so forcing everything to be a mode in torch.compile() world simplifies some logic.

(4) Your subclass should "logically" be a ATen op -> ATen op transform. More concretely, your __torch_dispatch__ logic cannot graph break or produce any guards. This is similar to the allow_in_graph restrictions: dynamo can't easily peak at __torch_dispatch__ code. This immediately eliminates doing things with global state, printing, etc. In theory, any behavior that you want to preserve that is not part of ATen can be converted into an opaque dispatcher operator, that you bake into the graph - so there's a bit of flexibility here, although the compiler (inductor) would need to know how to handle it in order for anything efficient to be generated.

**How to review this PR?**
Later today I'm going to try to outline the PR and call out important bits. I'd also be happy to go over the PR directly with anyone interested.

For a high level view of where TorchDispatch unwrapping slots into the other layers (autograd, functionalization, synthetic bases, deduping), see line 3071, where each of the passes is defined ([link](https://github.com/pytorch/pytorch/pull/97540/files#diff-df954bbf954d2dcb81f687876053267ffa4ddb36ed86b7d2bd76319ff2b94416R3071))

The two main new functions in aot_autograd.py are:
- `aot_dispatch_subclass()`. This function takes in a (potentially joint fw bw) function on subclass inputs, and translates it into a function on dense inputs. It hands that function the next layer (functionalization + tracing), and returns the result
- `aot_dispatch_subclass_runtime_wrapper()`. This function implements the runtime glue logic: when the user passes us a tensor subclass, we need to unwrap it into dense tensors before passing them to the compiled graph.

One layering issue that I don't love is the fact that AOTDispatch runs underneath the partitioning layer. This means that `aot_dispatch_subclass()` will only run once (on the joint graph), but `aot_dispatch_subclass_runtime_wrapper()` will run twice, once on the partitioned fw and again in the backward. This requires plumbing some metadata between the two functions. I think the way I'm doing it right now isn't too awful, but definitely open to suggestions.




[ghstack-poisoned]

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[613c4a6be5...](https://github.com/TaleStation/TaleStation/commit/613c4a6be5f87b22ce0f0d39fb707e4713674e46)
#### Friday 2023-03-24 19:56:29 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors Suiciding Variable Into Trait (#5017)

Original PR: https://github.com/tgstation/tgstation/pull/74150
-----
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

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [EFHDev/MTGA-Backend](https://github.com/EFHDev/MTGA-Backend)@[2ff7c3f322...](https://github.com/EFHDev/MTGA-Backend/commit/2ff7c3f3227763265b9aea42f62c5b12d06ee3d0)
#### Friday 2023-03-24 20:30:21 by Kestrel Kosdlic

Downloading works, extracting doesnt. Fuck you, Suck my dick.

---
## [dati25/Daemon](https://github.com/dati25/Daemon)@[c4071fba86...](https://github.com/dati25/Daemon/commit/c4071fba8658e93a20bbb2cc69b05e31da7c5ada)
#### Friday 2023-03-24 20:46:05 by ReeF90

I can commit, I am alive sheeeeeeeeeech, fuck you dave this is what you got kappa, also only few changes nothing major

---
## [google/truth](https://github.com/google/truth)@[38f712372b...](https://github.com/google/truth/commit/38f712372b5d01f6299066797862a9956e917e2b)
#### Friday 2023-03-24 21:35:01 by cpovirk

Rename our type parameter so that we define `assertThat(ComparableT actual)` instead of `assertThat(T actual)`.

This might be a little silly to wory about, but I think it makes much clearer what the method is for when you're looking at a list of `assertThat` methods. Compare the Javadoc for `Truth.assertThat`, which this CL is changing, to the Javadoc for `StandardSubjectBuilder.that`, which has been using `ComparableT` for years (for exactly this reason):

- https://truth.dev/Truth
- https://truth.dev/StandardSubjectBuilder

(Aside: All the appearances of fully qualified "java.lang.Boolean" and so forth are a shame....)

RELNOTES=n/a
PiperOrigin-RevId: 519240042

---
## [atosti/tgstation](https://github.com/atosti/tgstation)@[3156a0414e...](https://github.com/atosti/tgstation/commit/3156a0414e96b597d4d53823066d29daa0b30737)
#### Friday 2023-03-24 21:56:35 by san7890

[MDB Ignore] Manifest Destiny - The Final Tile Flattening (#74169)

Alt Title: The End Of The 12 Month War
## About The Pull Request

### Hey! Listen! This PR _will_ cause a merge conflict with your PR!
Please ensure that you have the knowledge on how to handle merge
conflicts, found here:
https://hackmd.io/@tgstation/ry4-gbKH5#Assured-Merge-Conflict-Resolution

Supercedes #74023 entirely.

Port of the tooling introduced in
https://github.com/BeeStation/BeeStation-Hornet/pull/7970 (we already
had everything else), modified to meet /tg/'s requisites and culling
anything that was not entirely relevant (that I could see). It's not the
end of the world if I missed something tbh. Some aspects were commented
out since they may be relevant to downstreams who port this PR or to
enable (what I see to be) un-necessary warnings.

This is a culmination of a year's efforts, starting with _Red Rover,
Four Corners_ (#65290) and later _Opposing Corners_ (#65455). If you
don't understand why this PR exists or why it's necessary, I recommend
reading both of those.

Since then, several mappers (both in their own mapping as well as
tailored PRs) have worked on "flattening" out these tile turfs, however
I've continually wanted a function that would mass automate it (outlined
here https://tgstation13.org/phpBB/viewtopic.php?t=31872 - This
functionality might still be useful if added to UpdatePaths or another
type of script thereof, but I no longer have reason to keep the bounty
up).

It's finally here! Yippie! A new python file, courtesy of itsmeow at
BeeStation. Very awesome. As previously mentioned, a lot of alterations
had to be made for our mapping desires, but the results are quite
agreeable. There's a few assertions that this file makes that I had to
address:

* We have "colorless" tile decals. These are transparent, so they don't
do anything. By default, bee would make these "white tiles", but we have
no such thing. I decided to just add a maplint and an UpdatePaths to
guard against this silliness (only Delta and Tram) had it.
* For some reason, it labels already-converted decals with the default
direction as an error state. I might touch this up in the coming hours,
but for now I surpressed the error due to how many false warnings it was
spitting out.

There's a few ways this tool can be improved, but I lack the knowledge
on how to do so:
* Make it so that we can run the map merger to fix the keys of the map
in the `update_map` function, rather than run the fixer-upper python
file. We can live without this to be honest. It's actually slightly good
because it forces you to look at all of the MapMerge Warnings, and you
can ascertain any potential errors without it silently passing you by
and hitting the repository (or at least those that we haven't linted for
yet).
* Be able to pass in any regex to "flatten" anything. That's way out of
scope for what I want to do here though.

## How do you use this tool?

I made a readme.
https://github.com/tgstation/tgstation/blob/363852cb17fa46dad8fd20e261f8f665f3e008bb/tools/MapTileAggregator/readme.md
### Mapping March
oh hey it's pretty neat that this PR came out in mapping march, what a
nice qol for mappers as the month enters the home stretch. ckey is
san7890

## Why It's Good For The Game

slimmer DMM files, better mapping practices. cool new tool. so nice.
## Changelog
Nothing that really affects players, but a short summary for all those
reading this PR:

* All "corner" turf decals are flattened, and there's now a tool that we
store that you can re-run to keep stuff flat in case you like mapping
one way and want to fix it at the end.
* We (should) now lint against useless uncolored turf decals since that
was completely garbo as far as our codebase is concerned.
* UpdatePaths for fixing up uncolored turf decals, yippie!


If you want to review this PR, may I suggest the file filter. You don't
need to look at any of the DMM files I already did:

![image](https://user-images.githubusercontent.com/34697715/226787961-ab82cad4-5d6d-4788-a7bd-5071aac825c4.png)

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [StanislawSm/WZRlab](https://github.com/StanislawSm/WZRlab)@[7b1ab1fa70...](https://github.com/StanislawSm/WZRlab/commit/7b1ab1fa7069090fb76b5f8f15e6145b3cf557ff)
#### Friday 2023-03-24 22:39:42 by StanislawSm

new begonning

After more than 20 hours, many tears, frustration, pain, insanity I finally made it. IT WORKS (at least for a first glimpse). It required rewriting almost everything what professor gave us. Tomorrow I will conduct more manual tests, but for today I'm done. Good night, I'm going to sleep hapy.

---

