## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-09](docs/good-messages/2023/2023-04-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,898,181 were push events containing 2,621,390 commit messages that amount to 141,098,513 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[b2f0f35f3a...](https://github.com/Koshenko/mojave-sun-13/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Sunday 2023-04-09 00:51:32 by EdwardNashton

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[e7a6f94460...](https://github.com/Stalkeros2/Skyrat-tg/commit/e7a6f94460cc391e7afc69682ddbefc87e036261)
#### Sunday 2023-04-09 01:15:50 by SkyratBot

[MIRROR] Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances [MDB IGNORE] (#20358)

* Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction

- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one.

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

* Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[09e95cdfbc...](https://github.com/meemofcourse/Shiptest/commit/09e95cdfbc8337b5b7a84a088c32b458ee1d996d)
#### Sunday 2023-04-09 01:30:57 by Bjarl

Saloon rework (#1594)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Expands whitesands_surface_camp_saloon to cover a 30x30 footprint and
not be nearly as bad. The previous version had some really glaring
design flaws, like holes in the wall for a bar. On a planet with a
deadly atmosphere. Yeah. Also all the chairs faced the same direction.
![2022 10 31-11 32
50](https://user-images.githubusercontent.com/94164348/199083356-5fabd2c8-0298-4a31-a830-b63dbcd2737f.png)
You can see how it looks. It's not great. 
Here's the new version
![2022 10 31-11 36
20](https://user-images.githubusercontent.com/94164348/199083924-9537beb7-0c74-4c57-9422-60fe953ae0bc.png)
![2022 10 31-11 36
25](https://user-images.githubusercontent.com/94164348/199084468-32d94ec8-846f-42e7-ae33-dc0b52e8b9b8.png)

![dreamseeker_ePSrp5zNFp](https://user-images.githubusercontent.com/94164348/199085448-24879745-650f-4bdc-9b0c-f1d9706ab865.png)
Ignore the patches of error, it's purple grass and doesn't display the
icon in sdmm for some reason.

The major changes are:
Expanding the building's footprint out to 30x30
Moving the loot behind the building, but locking it behind a shovel of
some sort (of which you can go through the ruin to get).
Improving the loot a LITTLE

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] The map loads although I still haven't managed to get it to load
on the proper planet with the spawning verb

## Why It's Good For The Game
The old version was kinda bad. Between the clown and mime masks out
front. The small footprint, and the free guns (also out front). This
solves those issues kinda while making it bigger.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Camp_Saloon has been expanded, expect frontier luxuries if you find
it!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[c21670412d...](https://github.com/meemofcourse/Shiptest/commit/c21670412dff10f4a3a1b1ab1e72f53294581d25)
#### Sunday 2023-04-09 01:30:57 by Bjarl

New Ruin: The Beach Town (#1572)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a new beach ruin, the abandoned beachside town
![2022 10 10-18 20
10](https://user-images.githubusercontent.com/94164348/194977185-0f35d08e-64c1-459d-94b2-ec6b66137753.png)
![2022 10 10-18 20
00](https://user-images.githubusercontent.com/94164348/194977192-0b93346e-cea0-4fb2-8b66-5ae7319ec3f1.png)

![dreamseeker_Ht2YcvyQbH](https://user-images.githubusercontent.com/94164348/194977254-d0b25aba-ec6b-4e8b-bad5-949a9961cf07.png)

![dreamseeker_KAB6kPSLrP](https://user-images.githubusercontent.com/94164348/194977259-561f8d97-962e-4545-a4b7-1637ad1a7156.png)

![dreamseeker_8Xe7Cuq6NH](https://user-images.githubusercontent.com/94164348/194977262-fb125315-2508-4022-9eda-5ed5078442c9.png)

![dreamseeker_SKJXeK9SOt](https://user-images.githubusercontent.com/94164348/194977268-b4efcd99-0896-4209-8b83-c61c086bda65.png)

![dreamseeker_6Ak0bNoVe5](https://user-images.githubusercontent.com/94164348/194977270-367aaf92-5d6d-4cd8-9827-eba99ec92080.png)

The town is an mostly empty place formerly devoted to tourism and the
beloved art of "chilling out". Facets of the life of its inhabitants
before their disappearance included drinking, grilling, and swimming off
the coast of their fairly large beach. Many interesting things happened
on the boardwalk, and a landing pad was present to allow for small ships
to dock inside the town.

The loot list is sparse here. I intend for this to mostly be a setpiece
for roleplay instead of a loot pinata. There's a good selection of
hydroponics seeds and gear, 2 full bar kits, basic kitchen equipment, an
autolathe, a few PDAs, a lotta wood, and a jukebox. Also donuts.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] Ruin spawns, nothing is out of whack that shouldn't be.

## Why It's Good For The Game
Continues the trend of making planets more good by adding more content
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An oddly empty town has been spotted on beach planets in the area.
Check it out spacers.
add: Random donut spawners, never eat the same donut two days in a row!

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

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[babf89eb74...](https://github.com/meemofcourse/Shiptest/commit/babf89eb746741ba4f33f686b0c4750fe68e1603)
#### Sunday 2023-04-09 01:30:57 by The-Moon-Itself

SubShips attempt 2 (#1627)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Accidentally destroyed my old PR for this, #1573, by completely botching
a merge from master to the point that it was easier to make a whole new
fork than try to save it, so here we are again. Here's the original
description:

Ports the parts of beestation/beestation-hornet#7152 that adds the
framework for ships to land on top of each other and not break
everything. A ship can only land on another ship if there's an open
docking port on the mothership that's large enough for the subship.
Here's a video of it in action on a modified dwayne-class:


https://user-images.githubusercontent.com/51838176/195471361-f9f0d145-d7c9-480e-ad4a-d18705f2590f.mp4

This system should be able to handle just about any orientation of ships
on top of each other, such as ships landed across areas, multiple ships
landed on a single ship, a single ship landed on multiple ships, a ship
that is only partially landed on another ship, a ship that is partially
landed on a ship that's partially landed on another ship, and so on.
Just make sure that you never try to land a ship on itself.

Something to note for this is that ships remember what's underneath them
via baseturfs, and there's a hardcoded check that will cause errors if a
baseturf list grows over 10 entries long. Because ship turfs have
typically 1-3 baseturfs, after about 3 ships stacked on top of each
other things will start to break.

You can also make maps with subships on them, to do this, follow these
steps:
1. make the subship as if it were a regular ship in its own map file
2. create a new /datum/map_template/shuttle subtype that points to your
subship map, these datums can be found in code/datums/shuttle.dm
3. On your main ship, place "subship dock" landmark in turf where you
want the bottomleft corner of the subship's bounding box to be, you can
also use the offset_x and offset_y vars on the landmark to offset this
corner if you need to place the landmark somewhere else.
4. Set the "subship_template" var on the landmark to the path of your
subship's map_template subtype
5. Optionally change the dir on the landmark to rotate the subship. for
reference, NORTH is no rotation, EAST is a 90 degree clockwise rotation,
etc.

You can put the stationary docking port anywhere on your map, as long as
it's on the ship. You can have its bounding box hang off the side of
your ship, but please try to keep the entirety of its bounding box
within the bounding box of map file, otherwise subships landing on your
main ship might accidentally clip through structures nearby your
mainship, including virtual z level borders.
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
Subships allow for many more creative designs and interesting dynamics
between and within ships, especially when a crew may need or want to
split its attention between multiple locations at the same time, or to
make interactions between ships easier when you just need to land a
smaller vessel inside of the other, cutting out the need to travel
through space turfs to get between two ships.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Subships are now possible
code: Lots of large changes to ship code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[d23ac504a0...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/d23ac504a0963a99c4a598abf102cd51144a0ef5)
#### Sunday 2023-04-09 02:15:35 by Captain277

Ashlanders Phase 3.5: Prelude to War (#5259)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

_War is coming to Surt-nar-Vel'la. It rages in the caverns below, held
back only by the furious roiling blood of the Mother. More and more
Scori are driven up to Surt-nar-Vel'la, and they bring ancient secrets
with them. But, perhaps not all that dwells below should be
unearthed..._

1. **Increases Mother's Blessing from 5 minutes to 15.**
2. **Gives Ashlanders access to Sign Language.**
3. **Creates reagent Phlogiston.**
4. **Creates Condensed Phlogiston item.**
5. **Creates craftable Heaven Shaker hand-held explosive.**
6. **Buffs Shank riding speed.**
7. **Makes tying posts dense.**
8. **Adds craftable Primitive Splints.**
9. **Adds craftable Bone Pipes.**
10. **Adds the craftable Spark Striker.**
11. **Adds cowls.**
12. **Adds Ashlander cryo.**

## Why It's Good For The Game

1. _This buff is too short-lived to be used by the Ashlanders. I'm
raising it to 15 minutes. However, it is still fairly robust, so I might
drop it to 10. Or raise it even further if it's still too short._
2. _It's been months of lessons. Knowledge of primitive sign is now
available to most surface dwellers. It is slowly being disseminated
below the surface to those who are willing to learn, meaning those who
are likely to come to the surface may know it too._
3. _Phlogiston is the alchemical compound found in all explosive and
flammable things. Here I imagine it as a sticky tar similar to napalm or
condensed nitroglycerin._
4. _Condensed Phlogiston is basically semtex. Not much more to add
there._
5. _These craftable grenades require condensed phlogiston. They are
designed to address an impending threat, but will almost certainly need
to be nerfed and fine tuned. They come in two flavors: HE and Frag._
6. _Shanks now move slightly faster, providing a movement bonus to
mounted travel._
7. _Tying posts not being dense has bothered me for a while now._
8. _Gotta have a way to temporarily mend bones until surgery is done!_
9. _Apparently Ashlanders are missing avenues to fine tobacco - and
other substances. Perhaps a new avenue of trade..._
10. _Going to need lighters for your pipes._
11. _These are basically the hood parts of certain cloaks or jackets,
but toggleable as simple headwear._
12. _No longer will there be braindead Ashlanders sleeping in the
Temple!_

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

:cl:
tweak: Increases duration of Mother's Buff.
tweak: Gives Scori Sign Language.
add: Adds Ashlander cryo.
add: Adds Phlogiston and Condensed Phlogiston.
add: Adds Heaven Shaker grenades, using phlogiston.
tweak: Buffs riding speed of Shanks.
tweak: Makes tying posts dense.
add: Adds craftable primitive splints.
add: Adds bone pipes.
add: Adds primitive lighters.
add: Adds cowls.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [lperezmo/evals](https://github.com/lperezmo/evals)@[ab5f7b2a89...](https://github.com/lperezmo/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Sunday 2023-04-09 02:17:07 by oscar-king

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
## [lperezmo/evals](https://github.com/lperezmo/evals)@[b170a21cf3...](https://github.com/lperezmo/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Sunday 2023-04-09 02:17:07 by Sam Ennis

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
## [lperezmo/evals](https://github.com/lperezmo/evals)@[b5da073c21...](https://github.com/lperezmo/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Sunday 2023-04-09 02:17:07 by somerandomguyontheweb

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
## [zmin9/next.js](https://github.com/zmin9/next.js)@[268dd6e80b...](https://github.com/zmin9/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Sunday 2023-04-09 02:59:16 by José Fernando Höwer Barbosa

Simplify with-google-analytics example (#43894)

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->
## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm build && pnpm lint`
- [x] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

First of all thanks for this amazing project and all the help you
provide with these examples.

It seems there is code duplication in this example. After some tests
locally seem to _document.js is not necessary for `gtag` to work
properly.


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_app.js#L30-L34


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_document.js#L13-L17

I am aware of https://github.com/vercel/next.js/pull/40645 and I would
like to ask @dave-hay, @SukkaW and @ijjk to consider this is still
necessary. If so why then not move all content of the scripts from _app
to _document?

In any case, I am open to adding here some comments explaining what is
the reason for this code duplication if necessary.

<hr/>

Changes that come from  https://github.com/vercel/next.js/pull/43897

1. The `event` hashChangeComplete should be removed since `/home` and
`/home/#section` is not new pageview, but just reference to the same
page.

If we go from /home to /home/#section (with a button click or a link for
example) this shouldn't trigger a new page visit on `gtag`.

For this reason, I think we should revert the changes from
https://github.com/vercel/next.js/pull/36079. If there is a better
argument of why this should stay I am also open to creating comments to
clarify this on the example since I don't think should be the default
behavior and not useful in most cases.

2. The `id="gtag-init"` was added with no context to the example from
https://github.com/vercel/next.js/pull/29530

If there is a reason for this id in the script to existing I am open to
adding a comment that clarifies this since in my experience is not
necessary at all.


Edit: Batching with https://github.com/vercel/next.js/pull/43897 as
recommended by
https://github.com/vercel/next.js/pull/43897#issuecomment-1344635000

---------

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[997dac9616...](https://github.com/Hatterhat/tgstation/commit/997dac9616768643cfa9ddce53432d684e196fb1)
#### Sunday 2023-04-09 03:03:52 by necromanceranne

Imports and Contraband: Different! Cargo crates without locks! MEAT! (#74490)

## About The Pull Request

### **Cargo Black Market goods should stay in cargo's hands**

#### New Cargo Console Category: Imports

This category is explicitly the non-departmental category beyond simply
having a Misc category. It is meant for material that nobody is meant to
be buying for their departments, and mostly for the odd-ball crates that
might show up. It also allows us to maintain contraband as exactly that;
contraband that the departments shouldn't have access too whatsoever. If
someone is buying from this category, they probably intend to be a
cheeky fuck.

<details>
  <summary>The New Changes</summary>

#### Baseline Imports

MEAT: MEAT (meat backpack you can eat)

<details>
  <summary>MEAT</summary>
  
![MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593459-f3c98abe-114b-43c1-a3e2-afc16b76c84f.png)
![MEAT MEAT MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593473-07a30781-a05e-4ca5-893b-778900cd2d1c.png)

</details>

Duct Spiders: They're adorable and cause a mess, but that doesn't stop
Nanotrasen from importing them from the Australicus sector to your
station!

Stack of 50 Bamboo Cuttings: Pretty expensive and kind of a premium.
Allows for those people looking to make bamboo decorations without
hoping botany exists, and are at least willing to pay. Also lets them
make horribly dangerous stuff with bamboo, of course.

A Single Sheet of Bananium: The problems this will cause I think speak
for themselves. (mostly due to a clown fruitlessly attempting to make
something actually disruptive while bankrupting cargo)

Natural Fish Bait: It isn't cheating, it's homemade. (Really good bait
but expensive and obviously drugs)

A dumpster...: A corpse in a dumpster, doesn't get more complicated than
that. Useful for corpse reasons.

Made using some code I borrowed from over here!
https://github.com/lizardqueenlexi/orbstation/pull/354

#### Contraband Imports

Foam Force Pistols: Same as it ever was with a price reduction. I
brought it down because riot darts are like 8 bullets a clip, and do
less damage than a disabler using riot darts. It feels like a sidegrade
weapon, and even if it technically is a ballistic weapon, it...isn't
that strong. I think this is pretty safe.

Definitely Not a Duct Spider: It's actually a giant spider in a box. If
you want to waste cargo's money while also sending them a mess to deal
with, this is the crate for you.

Russian Surplus Military Gear Crate: I took this opportunity to futz
with boltaction rifles. There are two kinds of mosin nagant you can get
in this crate. One of them is the good kind (no jamming). The other is
the shit kind (yes jamming), but you get more of them. You can get the
good ammo, or you can get the shit ammo. You'll have to pick through it
a lot more carefully to make sure you know which ones you've received.
Since this dilutes the pool even further, getting a good number of
mosins that aren't trash is even more expensive, and even if you do get
mosins at all, you might still only get the bad ammunition that doesn't
work against actual human threats as well. It also now cannot be
purchased through the security cargo supply console, and as to why they
could in the first place baffles me. Doesn't have a lock anymore
because...it's contraband? Who is locking this stuff?

**Side note: _You can make surplus 7.62 in the autolathe as well. It is
not very good except to fight fauna or naked assistants._**

**Side Side note: _I've killed off the shitty brand_new subtype and
brought peace once more to this land._**

#### Illegal Imports (Emag)

NULL_ENTRY: A journal that suggests how to make a...very interesting
weapon. The Regal Condor. Kind of an evolution on some other ideas I've
had over the years. This one is basically a secret weapon with a few
hurdles to jump through. Very lethal. Very expensive.

**Side note: _For reference, it's effectively 19 TC worth of gear to
make, but there does exist some methods to acquire this more cheaply if
you can get some bits and pieces from world spawns. Given it requires
you to get some pieces of equipment that might require additional
purchases of contraband, and getting into the captain's office to loot a
specific piece of clothing, the stakes more than make up for the
effectiveness._**

Smuggled WT-550 Autorifle Crate: This is basically the same, but you
might have noticed had you recently attempted, like me, to buy these
when you emagged them using a personal account and discovered a tragic
oversight. You couldn't, because they still needed armory access. This
removes that access, because you've already gone to the effort of
getting your hands on an illicit firearm through cargo, and if they
techs somehow miss the fact that you've purchased a WT-550...all the
better for you!

Smuggled WT-550 Ammo Crate: Includes AP and Incendiary!

**Side note: _You can get WT-550 ammo again via the Illegal Technology
node._**

Shocktrooper: Replaces the Special Ops crate. Contains a box of EMPs,
smoke grenades, a couple of gluon grenades and a couple of frag
grenades. Funsies.

Special Ops: The NEW Special Ops crate. Contains a chameleon mask,
jumpsuit and agent card. And a knife.

**Side note: _This is what appears in some cargo loan events._**

Refurbished Mosin Nagant Crate: The actual good mosin nagants. There are
6 of them. But they don't come with spare ammo. Hand them out to your
techs!
</details>

#### New Crates

- MEAT crate - Standard
- Duct Spider crate - Standard
- Giant Hostile Spider crate - Contraband
- 50 sheets of Bamboo crate - Standard
- A single sheet of bananium crate - Standard
- Natural (drugs) fish bait - Standard
- Dumpster with a corpse in it - Standard
- Shocktrooper crate (Grenades) - Emag
- Special Ops crate (Disguise) - Emag - Appears in some cargo loan
events
- Refurbished Mosin Nagant crate - Emag
- Regal Condor construction journal (NULL_ENTRY) - Emag

#### Changed Crates

- Foam Force Pistols (cheaper) - Contraband
- Russian Surplus Crate (less reliable, can't be bought by security
console) - Contraband
- WT-550 crate (more obtainable via personal accounts, thus
incriminating, not armory locked) - Emag
- WT-550 ammo (includes incendiary and AP) - Emag

#### Crates that got moved, unchanged, into Imports

- Foam Force Crate 
- Cosa Nostra Crate 
- Black Market LTSRBT 
- 'Contraband' Crate 
- Biker Gang Crate

#### Not crate changes
- You can print Surplus 7.62 (same as normal 7.62 but it sucks against
armor) from hacked autolathes.
- You can get WT-550 ammo from illegal tech.
- Removes the redundant Brand New Mosin subtype
- Fixes a potential exploit with jamming chance on Mosins.

## Why It's Good For The Game

I just think some of the magic of Cargo getting their hands on obviously
dangerous equipment and either hording it for themselves or attempting
to pawn it off was lost in recent times. A lot of this 'black market'
gear, however, suddenly became openly available to the crew anyway. For
_free_. Contraband crates and mafia crates could be purchased via the
Service budget. Security could just stock up en masse on mosins through
their console. And one fairly unfortunate consequence of a few recent
changes has made it nearly impossible to actually get illicit gear in
the first place, even if you did go to the effort of getting the money
for it.

On top of this, most of cargo's goods are pretty safe purchases. There
isn't much that would be considered 'actually a really bad idea to buy'
other than maybe supermatter shards. I wouldn't mind there existing ways
for someone to waste cargo's money while also causing them to have to
clean up the mess.

## Changelog
:cl:
balance: A significant overhaul of various illicit and dubiously legal
goods and gadgets available via cargo.
balance: Cargo now has an Import category for all non-departmental
goods. (And black market goods)
balance: Most contraband that already exists has been moved into
Imports.
adds: Includes several new imports of dubious quality. You get what you
pay for.
code: Removes the brand new mosin subtype as it is now defunct.
fix: Fixes potentially exploitative code in the jamming proc. Cleans up
that code while I'm at it.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [coalescentdivide/stable-diffusion-discord-bot](https://github.com/coalescentdivide/stable-diffusion-discord-bot)@[5231ee922d...](https://github.com/coalescentdivide/stable-diffusion-discord-bot/commit/5231ee922dc1ddb4ce59a82e877f50e251959c72)
#### Sunday 2023-04-09 05:12:18 by ausbitbank

Merge pull request #37 from coalescentdivide/reply-logic-tweaks

nice updates to reply logic thx to coalescentdivide <3
```


Some tweaks I made to the reply logic. I thought I'd share because I personally get a huge value with these tweaks.

A while back I noticed you could work off of an existing image by replying with .. as opposed to the tweak menu, and I thought that was a super useful feature. However it was tedious for me because I found that nearly every time I used this feature, I would forget to type things that I didn't want to change, such as the model used.

I thought it would be nice to just type .. --scale 11 or .. --steps 60 or some combination of parameters, while retaining the model and other settings from the render being replied to. So I updated the .. reply to do that. I updated the + and - reply also, but I really don't use them that much.

I also found that due to the discord mobile app limitations, copying the seed or other details from a render was a bit annoying from my phone. On mobile I would have to copy the entire text, then extract the seed from the copied text to reuse. So I added two new replies to make it more mobile friendly: seed and info.

replying with seed gets a reply back with the seed as an embed like this: --seed 12345. Since it is an embed, on mobile you can simply press and hold to copy it.

Similarly, replying with info gives a response that contains the full !dream command. But I didn't want to include EVERY command, things like upscale, seamless and threshold for instance. So to keep it tidy, I made it so those are only included in the string if they are used. Another benefit I found for the info reply: When an output is far enough back in the chat history where you have to click 'jump to present', this causes the tweak menu to disappear. replying with info will work for this, however if the queue was wiped and an output was before the wipe, that will give the wrong dream command.

I also changed the template reply so that by default, the ddim sampler is used, as it seems to work best for img2img. Any other sampler can still be specified.

Similar to that, I added one more reply inpaint which is just like template but defaults to the inpainting model.

disclaimer: I am only starting to dabble with coding within the last few months (thanks to language models like gpt) so I wouldn't be surprised if there is a better way to accomplish all of this. I've tested for a while in my discord and it does seem to work as intended. Feel free to edit into something better if my code sucks!

*The main limitation I'm aware of is that it the .., + and - reply methods don't retain the template image for an img2img render.
```

---
## [heady8354/Video-Game-Project](https://github.com/heady8354/Video-Game-Project)@[09ec2bb3f9...](https://github.com/heady8354/Video-Game-Project/commit/09ec2bb3f91734591cb3d3dd3ab8cffd5627ae54)
#### Sunday 2023-04-09 05:37:24 by heady8354

beach completion

tonight i have finished the beach along with introducing a new character, sand kid. you get to bully him and knock over his stupid ugly sand castle hahahah

---
## [Agameofscones/cmss13](https://github.com/Agameofscones/cmss13)@[df247be72a...](https://github.com/Agameofscones/cmss13/commit/df247be72a87e69e8841ad754633329c87a7883d)
#### Sunday 2023-04-09 05:40:19 by brian

reduces platform and handrail projectile coverage significantly (#2995)

# About the pull request

Does exactly what the title implies: reduces platform and handrail
projectile coverage significantly.
Platforms 60% -> 0%
Handrails 35% -> 10%

# Explain why it's good for the game

When a platform and handrail are combined, that totals at a 95% chance
of blocking a bullet passing through that tile. Platform corners also
catch bullets. That's some hogwash if you ask me. It makes areas like
Sorokyne's Mining platform entrance nearly un-defendable for marines
since they can't shoot past what is effectively an invisible bullet
wall. When I made Sorokyne, this was not the intent of the area. New
Varadero has similar problems.

You may ask, why not change those areas instead? My answer: Sod off,
they look awesome, and I don't want to code a check on projectiles to
determine if you're shooting 'up' at a ledge which would be the logical
simulationist fix. Also handrails aren't supposed to block bullets
unless they're reinforced (not that anyone uses that mechanic though).
How do I know this? I willed this mechanic into existence for Strata
with shitcode. I was there when it was written.

Both xenos that spit and marines that shoot will benefit from this
change.

Oh yeah and corners won't catch bullets anymore.

# Changelog

:cl: Triiodine
balance: Reduced projectile coverage of platforms from 60% to 0%.
balance: Reduced projectile coverage on handrail types from 35% to 10%.
Sandstone handrails are unaffected and remain at 35% projectile
coverage.
balance: Sandstone handrails can no longer be reinforced.
/:cl:

---------

Co-authored-by: Chadwick B. Dunlop <fake@fake.mail>

---
## [Agameofscones/cmss13](https://github.com/Agameofscones/cmss13)@[4e86fc8df2...](https://github.com/Agameofscones/cmss13/commit/4e86fc8df2247dcb18b14e473d6ab6cca3c7567d)
#### Sunday 2023-04-09 05:40:19 by victorjosephespinoza

Let (whitelisted) ghosts join in as Working Joes (#2963)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

https://forum.cm-ss13.com/t/make-it-so-ghosted-players-can-spawn-in-as-working-joes/588
Adds a ghost verb so ghosts can now join the game as working joes.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Like it was said in the forum post, Joes are pretty much harmless, their
impact on the round is pretty much minimal, so adding this wouldn't
imply any balance change whatsoever.

The intent of adding something like this to the server is mainly trying
to get more attention to the role. Which is barely played at the moment,
however, if dead players could now respawn as them, I believe it might
get more activity.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
Unsure of what kind of debugging I could provide in here, request any in
the comments and I'll do it.

There's a high chance that something is not treated as it should. This
is probably the first PR where I had to look and understand what I was
writing, despite the fact that a lot of the code is taken from the pred
initialization. So yeah, if you would have placed something somewhere
else, or differently, go ahead and tell me.

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
add: Added a new verb for ghosts to join in as working joes (ONLY
WHITELISTED GHOSTS).
code: Edited max spawns of the working joes to 3.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [PA-GK/android_frameworks_base](https://github.com/PA-GK/android_frameworks_base)@[17253272a6...](https://github.com/PA-GK/android_frameworks_base/commit/17253272a69324df9819b278c4035904933ed5a8)
#### Sunday 2023-04-09 06:42:52 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [gentoo/portage](https://github.com/gentoo/portage)@[28cd240fb2...](https://github.com/gentoo/portage/commit/28cd240fb23d880b8641a058831c6762db71c3e2)
#### Sunday 2023-04-09 06:52:10 by Sam James

emerge-webrsync: support PGP verification via gemato

Introduce PGP verification of the webrsync snapshot tarballs
using app-portage/gemato - which is already a dependency of Portage
for verifying normal rsync.

This is the same method Portage uses (see below).

Technical changes before we dive into the rationale:
- Use gemato for PGP verification just like Portage does for
  sync-type=webrsync, sync-type=rsync (although that uses a metamanifest),
  and sync-type=git (although that uses gemato for gpg-wrap, so works differently).

- Use gentoo-functions automagically if available for better output
  functions.

- Be more verbose about verification and various other operations,
  while also respecting --quiet if passed for misc. existing & new
  messages.

- Make --verbose a no-op. There weren't enough output messages
  to justify three states (--quiet, normal, --verbose).

- Bail out more aggressively in the event of errors or "warnings".

- Use modern terminology for repository, etc (avoid overloading the
  "portage" term.)

- Allow disabling PGP verification with --no-pgp-verify.

Technically, the fix is very straightforward, but getting to
the fix was the slightly painful bit. What I've concluded
happened is:
- Portage starts getting reworked to gain proper sync module support;

- Someone gets the idea of implementing emerge-webrsync fully in Python
  as a Portage sync module (which is a not-unreasonable idea);

  [This ultimately hasn't gone anywhere, and in fact, while working on this
  bug, I ended up finding a bunch of typos that meant you couldn't even test it.
  But it's a stub anyway.]

- The idea of deprecating emerge-webrsync is floated around. The idea
  being Portage should call it via its new sync module with sync-type=webrsync.

  This is presumably with the ultimate goal of it transparently one day
  using the aforementioned (yet-non-existent) Python implementation as its
  backend, and not the shell script.

  [To this day, Portage's webrsync implementation shells out to the emerge-webrsync
  shell script, but it has the abstraction to switch that out, in theory.]

- At the time, PGP verification in general of the Gentoo
  repository is an active topic, especially now we'd migrated to git which makes
  it way easier, unlike CVS.

- A bug is filed for PGP verification in emerge-webrsync.

  People decide it doesn't matter too much, because Portage is going to
  Real Soon Now (TM) have its own backend (replacing the shell script) and/or
  Portage's sync module support obsoletes emerge-webrsync entirely.

  The idea here, I think, being that nobody should call emerge-webrsync and
  everyone should just call emerge (or emaint) to sync as appropriate.

  [This isn't a terrible idea in a sense, but it needs a better basis:
  we should probably make emerge-webrsync a wrapper which creates a temporary
  repo config to forcefully webrsync a repository if the user asks us to. This
  is what people expect from emerge-webrsync with the default sync-type=rsync
  in repos.conf for ::gentoo.

  I actually started implementing this before I realised that emerge was
  shelling out to emerge-webrsync, so have postponed it.]

- Then nothing happens with the "replacement" ideas and the good
  ol' trusty emerge-webrsync ends up with the same problems sitting
  there because nobody saw the point in working on it if it was to
  be replaced soon. But that didn't happen.

The fix overall for this is pretty small, but the commit is larger
than I'd like because I had to rework a few things to sensibly allow
disabling PGP verification as well as follow the flow.

(I did start splitting up this commit but ultimately it needs -w
for best review even without the output tweaks in this commit and
deconstructing this for atomic commits would end up being more brittle
as I couldn't be as confident in the result.)

Bug: https://bugs.gentoo.org/597800
Signed-off-by: Sam James <sam@gentoo.org>

---
## [CalculusEnjoyer/numertic-methods-lab-2](https://github.com/CalculusEnjoyer/numertic-methods-lab-2)@[880b5d7f25...](https://github.com/CalculusEnjoyer/numertic-methods-lab-2/commit/880b5d7f256590a5510a224d11d7b0cfa00608c8)
#### Sunday 2023-04-09 09:28:54 by CalculusEnjoyer

In the year 2525, if man is still alive
If woman can survive, they may find
In the year 3535
Ain't gonna need to tell the truth, tell no lie
Everything you think, do and say
Is in the pill you took today
In the year 4545
You ain't gonna need your teeth, won't need your eyes
You won't find a thing to chew
Nobody's gonna look at you
In the year 5555
Your arms hangin' limp at your sides
Your legs got nothin' to do
Some machine's doin' that for you
In the year 6565
You won't need no husband, won't need no wife
You'll pick your son, pick your daughter too
From the bottom of a long glass tube
In the year 7510
If God's a coming, He oughta make it by then
Maybe He'll look around Himself and say
Guess it's time for the judgment day
In the year 8510
God is gonna shake His mighty head
He'll either say I'm pleased where man has been
Or tear it down, and start again
In the year 9595
I'm kinda wonderin' if man is gonna be alive
He's taken everything this old earth can give
And he ain't put back nothing
Now it's been ten thousand years
Man has cried a billion tears
For what, he never knew, now man's reign is through
But through eternal night, the twinkling of starlight
So very far away, maybe it's only yesterday
In the year 2525, if man is still alive
If woman can survive, they may find

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[78f6cb4ae8...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/78f6cb4ae846d6a2e1f9d1c9b225c3a8cad90d73)
#### Sunday 2023-04-09 09:34:19 by Tashfin Shakeer Rhythm

Revert "thermal_core: Do not unload thermal core driver as a module"

thermal_unregister_governors() is not marked with __init annotation anymore
and my sorry ass didn't remember during rebase. Revert this broken patch.

This reverts commit e3036b0a6a61076444cf6b4e8dd83e52e581c939.

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [khwilliamson/perl5](https://github.com/khwilliamson/perl5)@[15119347e4...](https://github.com/khwilliamson/perl5/commit/15119347e461bd5ff2afb671b1c8138cbe635b42)
#### Sunday 2023-04-09 12:31:43 by Yves Orton

epigraphs.pod - add epigraph from 5.37.10

My dad had beautiful handwriting, and whenever he got a new pen he would
write out this stanza of Lewis Carrolls poem on the blue lined paper he
used to write his notes on. So this is my homage to him.

For some reason I can never remember the wording properly and say it
as "to /speak/ of many things" instead of "to /talk/ of many things".
Memory is a funny thing.

---
## [DimensionalDevelopment/atlantis](https://github.com/DimensionalDevelopment/atlantis)@[71b788e06b...](https://github.com/DimensionalDevelopment/atlantis/commit/71b788e06b45503ecab4ff7d473542be920437cb)
#### Sunday 2023-04-09 12:35:11 by RaveTr

Something Something Refactor Part 1 Something

-Grouped init classes together into the init package.
-Refactored all blocks.
-Temporarily removed some datagen stuff, will return by next commit
fully automated. Some models may appear broken temporarily while
testing.
-Remember that part where I said I refactored all the blocks? Yeah, I
mean I literally did. All variable names and other things have been
changed by me, readability improved.
-Improved some consistency in code.
-Organized imports.
-Properly indented some inconsistently indented code blocks. FOLLOW ONE
INDENTATION PATTERN DAMMIT!!
-Refactored all init classes.
-Improved overall readability of the parts I did end up modifying for
this commit.
-The most manual 2 hours and 34 minutes of my life I've ever spent since
I first learned how to set up development environments :skull:

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[dc2f52e386...](https://github.com/ZephyrTFA/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Sunday 2023-04-09 13:06:49 by tralezab

Blink is no longer a forbidden school spell?? (#74487)

## About The Pull Request

Turns blink's school from forbidden to translocation. This has some
incredibly minor changes nobody is going to notice:
- Changes the blink's invocations when mixed with a CERTAIN spell
- If you were very specifically a chaplain with the holy crusade sect
and you casted blink, before it would excommunicate you, now it will
just smite you, as translocation spells are seen as less bad than
forbidden magic
- probably some more niche interactions but that's all I can remember

## Why It's Good For The Game

Guys, I know blink is a very annoying spell but come on now it's not
forbidden magic, that's for heretics and super duper evil stuffs

## Changelog
:cl:
fix: blink is now a translocation spell
/:cl:

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[48183ec0ff...](https://github.com/ZephyrTFA/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Sunday 2023-04-09 13:06:49 by san7890

Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[b5ebf5c942...](https://github.com/ZephyrTFA/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Sunday 2023-04-09 13:06:49 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [JoeCodeswell/dom-examples](https://github.com/JoeCodeswell/dom-examples)@[e37a50882e...](https://github.com/JoeCodeswell/dom-examples/commit/e37a50882ee79dd42459f87be59cc80799323d5a)
#### Sunday 2023-04-09 15:28:29 by JoeCodeswell

230409_08_25_19_Sun
### RESULT: Thanks, God. simple-service-worker WORKS! Successfully
ran simple-service-worker << >>
 mdn/dom-examples:main.  using `npx lite-server .`
### TODO
1. Trust in the Lord, Jesus Who is the Resurrection and the Life.
2. Set my mind on the Spirit, in Peace & Truth & Life.
3. Let the SAME Mind be in me that was in Christ Jesus.

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[e65dff59bd...](https://github.com/Thunder12345/tgstation/commit/e65dff59bd47f5805e8b33f623f02cd1700d22ec)
#### Sunday 2023-04-09 16:16:52 by zxaber

Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs (#74225)

## About The Pull Request
Reduces the price of the Doomsday equipment by 20 PT for each APC hacked
in a Head of Staff office, as well as the Vault.
## Why It's Good For The Game
See #71404 for the prior PR and my full reasoning.

Long-story short, activating the Doomsday before having a plan in place
is suicide, and it takes 13 APCs to unlock. Since there are few well
hidden APCs in general, you'll usually be gathering APCs after going
loud (such as with a borg machine). 13 APCs is 13 minutes, and by the
time you've gathered your malfbux, you're either already dead or have
already taken full control.

I had intended to give Doomsday a flat 70 PT price, but concerns were
raised that an AI could conceivably hack only APCs on their sat (and
perhaps one on the Lavaland outpost) and Doomsday without ever really
touching the station*. So a compromise was proposed, we instead give the
AI discounts by hacking Head of Staff areas, and the Vault, which are
usually situated in well-traveled areas, and also have some fluff
reasoning.

*I still think it'd be suicide to do this, but it's not a hill I want to
die on.
## Changelog
:cl:
balance: Malf AIs that hack Head of Staff and Vault APCs will now find a
discount issued on Doomsday.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[9dfe00d79d...](https://github.com/Thunder12345/tgstation/commit/9dfe00d79dd7bd540442ce825caa4e964c619b46)
#### Sunday 2023-04-09 16:16:52 by san7890

IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request


![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

---
## [restarone/violet_rails](https://github.com/restarone/violet_rails)@[3d13e4c7fd...](https://github.com/restarone/violet_rails/commit/3d13e4c7fdb101fb91297dea864eb7ee409746eb)
#### Sunday 2023-04-09 16:17:24 by Don Restarone

[fix] optimize analytics V2 further + lockdown profiler (#1522) (#1523)

Addresses: https://github.com/restarone/violet_rails/issues/1399 and https://github.com/restarone/violet_rails/issues/1452

## Profiling Results 📈 🧪 


### Slight improvements to user experience

When analysis going back 1 year is shown, there is a noticeable performance improvement:

<img width="1728" alt="Screen Shot 2023-04-08 at 11 03 31 AM" src="https://user-images.githubusercontent.com/35935196/230728720-31d5d2c0-83e0-4aa2-b3ef-fede1458ff4f.png">

### Less memory & objects used
When a 1 year analysis is shown, less memory and objects are allocated and retained: 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 04 09 AM" src="https://user-images.githubusercontent.com/35935196/230728751-5302c578-4240-4f77-8ac8-166d2046be27.png">

### Garbage collector is running consistently 
on a per request basis, we observe that the garbage collector runs before the request is served. Indicating that used memory has been drained and freed to be used for other requests. 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 06 48 AM" src="https://user-images.githubusercontent.com/35935196/230728822-c1f86bd8-b8fb-45ee-86fa-848c27698a6f.png">


# Real life example, Marked Restaurant

## Resource usage

comparison of memory / CPU usage before and after patch

### Baseline 🆎 

The "resting memory rate" for a high traffic Violet system is around 600MB: 
<img width="1728" alt="Screen Shot 2023-04-09 at 11 44 16 AM" src="https://user-images.githubusercontent.com/35935196/230782692-84553698-fc07-4392-b7e6-45cda169d370.png">

### Before ⏪ 

Viewing the 1 year analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 23 AM" src="https://user-images.githubusercontent.com/35935196/230782749-11df1621-27ce-4b08-bf65-3625e5eddf7f.png">

Viewing the 1 month analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 08 AM" src="https://user-images.githubusercontent.com/35935196/230782771-8801aa10-13c3-4bc5-82bc-70d09924000b.png">

We observe 1.2 GB of memory use (double the resting rate)

Profiler result 📈 
While attempting to run the memory profiler on the 1 year analysis, we observed 3GB+ of memory usage ⚠️ 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 43 51 AM" src="https://user-images.githubusercontent.com/35935196/230782803-0ca221c6-976b-4e28-a669-67f8e196f6d0.png">

⭐  After the test was run, puma was restarted to ensure system stability

### After ⏩ 

Viewing the 1 year analysis: 
<img width="1728" alt="Screen Shot 2023-04-09 at 12 08 06 PM" src="https://user-images.githubusercontent.com/35935196/230783850-ee5963b2-7280-4323-9dbf-73812671b040.png">

We observe 720MB of memory use

Viewing the 1 month analysis:
<img width="1728" alt="Screen Shot 2023-04-09 at 12 11 44 PM" src="https://user-images.githubusercontent.com/35935196/230783889-8fb54846-47d0-487f-9480-3ded87fc7217.png">

We observe 850 MB of memory use 


Profiler result 📈 
We observe 900MB of memory use when profiling the 1 year analysis
<img width="1728" alt="Screen Shot 2023-04-09 at 12 10 11 PM" src="https://user-images.githubusercontent.com/35935196/230783899-5a66ded5-8529-4900-aab2-9003d89e06b1.png">

### Result

The system is now consuming memory in analytics V2 comparable to its resting memory usage rate. 







Co-authored-by: Prashant <25191509+alis-khadka@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[400212f6bd...](https://github.com/mrakgr/The-Spiral-Language/commit/400212f6bdc8f02a234247ee2fca7b05e0154b8e)
#### Sunday 2023-04-09 16:48:44 by Marko Grdinić

"9:30pm. https://gogoanime.llc/rwby-volume-9-dub-episode-3

I am watching S9 of RWBY and these developments in the first two seasons are beyond retarded. What are the writers doing?

https://gogoanime.llc/category/i-was-stuck-on-the-same-day-for-one-hundred-thousand-years-3

Maybe I should really give some Chinese series a try.

8:40pm. I am looking up threads in the archive and apparently Ruby kills herself. Wtf?

I am laughing out loud here at how stupid it is. Let me watch the rest.

10pm. https://old.reddit.com/r/ExperiencedDevs/comments/12ei8mo/is_the_phrase_programming_language_doesnt_matter/

> What are your options for early exit? Can your language perform automatic loop unrolling? Are you running in a functional language where you need to be mindful of tail recursion? Does your language prefer list comprehensions or ranges or map and fold for iteration? Can you create side effects in a loop? Are you forced to create side effects in a loop due to the age of your language? Is a loop a statement or a meaningful expression? Does your language handle nested breaks cleanly? What about post condition checking (do...while)? What about optimizations around intentionally infinite loops? Can you interrupt a loop for asynchronous execution? Does your language have a good debugger for finding unexpectedly hot loops?

10:35pm. A lot of good comments in this thread. Small subs like this can have gems before they are overrun by the masses.

https://old.reddit.com/r/ExperiencedDevs/comments/12ei8mo/is_the_phrase_programming_language_doesnt_matter/jfen1cc/

///

Context is key.

When learning, which programming language you choose to start out with doesn't really matter. The key is to really learn programming, not to memorize how to do something in a particular language or ecosystem.

When solving a problem, programming language isn't as critical as most non-developers think, but it does matter.

* Choosing a language will put a cap on the performance available to you. If you choose C++, the max performance will be limited only by your skill and the speed of the hardware. If you choose Ruby, the max performance will be 1/20 or less of the C++ code. Other languages fall between those extremes.
* Choosing a language with dynamic types means you're missing out on some key software engineering tools that can help keep a code base clean over the long term, as well as helping people onboard to the project. I don't mind writing short scripts in strictly dynamic type languages, but refuse to work on extremely complex projects based on, e.g., PHP or Python.
* Choosing a language typically ties you to an ecosystem, or in some cases, one or more ecosystems. The tools available in one ecosystem (e.g., Node.js+TypeScript) might be so much more powerful for a particular task (e.g., CRUD) than those in another ecosystem (e.g., C++) that one ecosystem requires 1/50th or less the amount of code to accomplish the same tasks. I'm not even exaggerating.
* Some languages trade performance for developer productivity. In the last example, part of that 50x improvement when using TypeScript is simply that the same logic takes less code.
* Some language ecosystems are poorly designed to the point to recommend against using them. PHP falls under that category for me. The language was designed with even less skill than JavaScript, and the libraries practically beg you to create SQL injection flaws. You need to be an expert to work around all of those security holes...and yet most PHP developers are actually among the least skilled, leading to an ecosystem that pretty much dominates the security advisory lists.
* Some languages (e.g., C, though to a lesser degree, C++) require that you understand software at a lower level than languages that are GC based. There are decent, and probably even good, Java or JavaScript or Python developers who, when trying to make the jump to C or C++, simply fail. Yes, you can put together "Hello World" in C or C++ without much effort. But to really use either language requires a quantum shift in how you think about programming, and in my experience trying to teach other developers these concepts, some find they can't bridge the gap. C++ adds another layer of complexity on top of the lower-level understanding required by C, and there are people who are virulently against using C++ for ... reasons ... even though C++ is strictly better than C for some domains (e.g., embedded).

So yes, there are differences. And I refuse to work on some languages even though I know them well enough that I could use them (e.g., PHP).

///

https://old.reddit.com/r/ExperiencedDevs/comments/12c4mxs/junior_dev_using_chatgpt_for_code_reviews/

///

I'd also be pissed because ChatGPT is flat out wrong all the time. I use it daily and it's hardly some magic bullet. A junior may not get that.

ChatGPT pisses me off because everyone trusts it. It's very very good at looking correct. It is often wrong.

///

11:50am. > When someone tells us in an interview they’re excited about working here because they like functional programming (say), we count that as an indication they might not be a good fit.

4/9/2023

8:25am. I am up early, but regardless, I still have been lounging in bed for a while. This is despite me going to bed past 11pm yesterday.

9:50am. Done with the bath. What follows next is screencasting. Let me get on with it.

https://pixabay.com/music/modern-classical-relaxing-145038/
https://pixabay.com/users/music_for_videos-26992513/

This guy is good.

https://pixabay.com/music/modern-classical-slow-piano-145044/

Let me get this one as well.

11:55am. > In the current version of ASP.NET, it seems you need to specify the authorization schema in the claims identity directly. Before that we had to add the relevant authentication services to the dictionary the framework is using under the hood.

Let me cut this out. I do not have anywhere to put this.

12:25pm. Had to take a break so I might as well segue it into breakfast. Currently I am 25m into it.

2pm. Done with breakfast, Birdie Wing and chores.

Let me resume. I need to do more screencasting. Time to bring in the database.

3:25pm. https://pixabay.com/music/modern-classical-slow-piano-2-145042/

Let me add this to the video as well.

https://learn.microsoft.com/en-us/aspnet/core/data/ef-rp/crud?view=aspnetcore-7.0&viewFallbackFrom=aspnetcore-2.2#singleordefaultasync-vs-firstordefaultasync

4:05pm. https://stackoverflow.com/questions/56257157/how-to-check-for-null-from-newtonsoft-when-the-compiler-insists-that-it-isnt

This is so annoying.

https://stackoverflow.com/questions/43328417/translate-entity-framework-core-example-to-f

4:40pm. https://pixabay.com/music/modern-classical-coronavirus-145019/

Let me also get this one.

5:25pm. Did the thumbnail.

...Now it is rendering in the background.

5:50pm. https://youtu.be/wQEIEDbABFU
Authentication & Authorization With ASP.NET Core And Giraffe. How To Build A Login Page. (Pt. 1)

Here it is. Let me post it on the F# sub. Maybe my Twitter. Also I should find a way to get into the F# slack even if it means registering via a different address.

6:10pm. https://twitter.com/foonpm/status/1488760256624828419
> Sometimes I wish F# devs actually existed. As I'd build an entire team!

Check this tweet out. Well, that was a year ago, who knows if he is still interested.

> CEO @ Marvin - Hiring (Craftsman, DDD/CQRS/ES, TDD, Clean Code, Functional programming) - Full Remote - Worldwide

I saw a post from over a year ago that you are hiring F# devs, so I thought I'd ask whether that is still the case. You can see some of my most recent work on the F# subreddit. I've been getting into webdev lately, and and my particular specialty is creating programming languages and ML libraries.

Spiral is my best work: https://github.com/mrakgr/The-Spiral-Language

I have about 7 years of experience, most of it in F#.

6:40pm. I wasted my time trying to send a message, but I can't even DM him.

https://www.remote.io/

I'll keep this site in mind, why did I waste my time trying to contact this guy?

Forget this. Let me play Limbus for a bit.

Then I'll watch anime. It is really great that Birdie Wing got S2. G Witch is out. I'll also give ep 1 of Destroyes a try as well.

Time for some fun. Tomorrow I'll continue building the login page and screencasting as I go along. I've managed to hit my stride and am doing good work."

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[a6f49ed542...](https://github.com/Jackraxxus/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Sunday 2023-04-09 17:04:06 by san7890

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
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[625a3e01e8...](https://github.com/Koi-3088/ForkBot.NET/commit/625a3e01e870d452e2978835b0f343727896e3c8)
#### Sunday 2023-04-09 17:07:18 by Koi

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
## [JoeCodeswell/dom-examples](https://github.com/JoeCodeswell/dom-examples)@[bafb83b6f2...](https://github.com/JoeCodeswell/dom-examples/commit/bafb83b6f258e06efd1636634d0be7e06f0fbb24)
#### Sunday 2023-04-09 17:33:19 by JoeCodeswell

230409_10_28_20_Sun
### RESULT: Thanks, Holy Trinity. Added
`console.log('Service worker registering');` to app.js  - still Works.
### TODO
1. Trust in the Lord, Jesus Who is the Resurrection and the Life.
2. Set my mindon the Spirit in Truth and Life and Peace,
3. Let the SAME Mindbe in me that wasin Christ Jesus.

---
## [kinneb/tgstation](https://github.com/kinneb/tgstation)@[c3b78761d2...](https://github.com/kinneb/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Sunday 2023-04-09 18:13:21 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [kinneb/tgstation](https://github.com/kinneb/tgstation)@[e1221c986f...](https://github.com/kinneb/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Sunday 2023-04-09 18:22:56 by san7890

Chasm Hell On Icebox - 300 Active Turfs on Prod Moment (#74410)

## About The Pull Request

Spontaneous regressions introduced by #74359
(1e58c1875d9e2f48a306fe31a0626dbbb1990ff9).
```txt
 - Z-Level 2 has 150 active turf(s).
 - Z-Level 3 has 150 active turf(s).
 - Z-Level trait Ice Ruins Underground has 300 active turf(s).
 - Z-Level trait Mining has 300 active turf(s).
 - Z-Level trait Station has 300 active turf(s).
 - End of active turf list.
 ```

![image](https://user-images.githubusercontent.com/34697715/229213138-5a6a7a4f-edec-47ab-8def-ee4e4bddfe61.png)

Basically the lavaland ruin sucks dogshit and I had to do a lot of stuff to account for everything failing. There was even a moment where we were adding something to `flags_1` instead of `turf_flags` and that was also really bad to figure out.

![image](https://user-images.githubusercontent.com/34697715/229213428-63bb1f6e-6f88-4604-a3c6-e08e20cbfa7a.png)

i also had to add orange genturfs because it was really getting bad with all of the assertions we had to keep making, especially since stuff like this could also show up:

![image](https://user-images.githubusercontent.com/34697715/229213562-4a145453-5f90-4d05-b8cc-5c1beec2b0dd.png)

That's the prison in the red box, those are active turfs because a chasm scraped it away.

Sorry if this is hard to follow but I promise you everything in this is essential. I wish we didn't have to rely on turf flags as much as we do but this is a fix PR, not a refactor.
## Why It's Good For The Game

Even one active turf on IceBox ate up _three_ seconds of SSair's initialization every single time it was really fucking bad.

We haven't had to deal with chasms for about two years so there's a lot of mapping assertions we made since they just weren't a thing, but now they're back so lets do it properly.
## Changelog
:cl:
fix: The prison on IceBox should no longer leak air as often.
/:cl:

I have compiled this map about 30 times until active turfs stopped fucking happening and now I am content. This likely doesn't fix _everything_ because some stuff can still be hidden to me, and we still have PRs that need to be merged to reduce the amount of noise we're getting on prod.

---
## [kinneb/tgstation](https://github.com/kinneb/tgstation)@[0a1f7e8de2...](https://github.com/kinneb/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Sunday 2023-04-09 18:22:56 by Hatterhat

Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[0410075cc8...](https://github.com/shiptest-ss13/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Sunday 2023-04-09 19:01:09 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [KritRom/MonikaModDev](https://github.com/KritRom/MonikaModDev)@[f4920a3c1c...](https://github.com/KritRom/MonikaModDev/commit/f4920a3c1cb642af1c4dfb270e51266c32a49564)
#### Sunday 2023-04-09 19:26:28 by Kris the artist

"Do you miss the other girls?" Topic.

I always thought it'd be nice to know if she sometimes misses her club members, given that they were meant to be friends prior to MC's arrival. Here's my view on the topic. Apologies for any bugs or mistakes in this, I checked everything as thoroughly as I could. Grammatical corrections are appreciated!

---
## [OpenSourceScienceFramework/aperta-testing](https://github.com/OpenSourceScienceFramework/aperta-testing)@[dffc9ab0c5...](https://github.com/OpenSourceScienceFramework/aperta-testing/commit/dffc9ab0c570dca7956a06f81dd7bd8ea467655d)
#### Sunday 2023-04-09 20:04:03 by michael-voropanov

    DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

Copyright (c) 2023 Author. All rights reserved.

Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

    DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
    0. You just DO WHAT THE FUCK YOU WANT TO.

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[6085e3b5ee...](https://github.com/Helg2/tgstation/commit/6085e3b5eed0f4954d2ba25549c919653207611d)
#### Sunday 2023-04-09 20:09:44 by MrMelbert

Reagent soup / Soup rework / Stoves - A kitchen expansion (#74205)

## About The Pull Request


![image](https://user-images.githubusercontent.com/51863163/227391708-8de28b68-149f-4e02-a2d3-22f6e3067784.png)

**This PR:** 

- Reworks most* existing soup into reagents. 

- Adds Stoves and Ranges. Ranges replace most* existing ovens. 

- Adds soup pots, to cook soup

**How does it work?** 

In the kitchen you will find a stove now.

Stoves act as a "reagent container heater", essentially a chem heater.
You can set a pot onto the stove.

To make soup, visit the cooking recipe book for a guide. Most recipes
are the same as before, just tweaked slightly - Add water to the pot (50
units for 1 batch generally), then add all the corresponding ingredients
to the pot. Set the pot out on the stove and right click it to turn it
on. If the recipe's correct, shortly it will start to mix and give you
soup!

One soup recipe will give you roughly 3 servings of soup. You can pour
our the soup into a bowl using a ladle or just by pouring it manually.

Of note: **All of the reagent contents of the ingredient are transferred
into the soup.** Better, more nutrient rich ingredients produces more
soup, and poisoned produce will pass it on.

If you place the soup into a chem master, you will notice it's roughly
half "soup reagent" and half a variety of reagents, including nutriments
/ proteins. This is your soup! It is recommended you serve your soup
with the reagents included, as they make up more nutrition for the
customer, however you can separate it out if you're picky.

**Todo:** 

- [x] Fill out the PR body a bit more 
- [x] Mapping (wait for big merge conflict pr to go past)
- [x] Soup colors
- [x] Balance pass over for soup recipes
- [x] TODOs
- [ ] Unit tests
- [x] Cullen Skink's recipe is invalid
- [x] Try to see if there's an easy way to prevent soup from fattening
you up too easy.

## Why it's good for the game

Adds some more depth to the kitchen and moves chef away from the
click-button-get-food style that exists.

Allows for inherently custom soups by the way of making it reagents, so
no need to support custom soup food items.

## Changelog

:cl: Melbert, stove and pot sprites by Kryson, ladle sprite by Kinneb
add: Kitchens are now stocked with Ranges. 
add: You can now print (and create) Stoves. 
add: The dinnerware vendor now dispenses ladles. 
add: Spoons can now actually spoon... things.
add: Soup has been reworked entirely. Soups are now reagents, cooked via
a soup pot on a Stove or Range. Simply add water and your required
items, then apply heat. Be careful not to boil over!
add: Stoves, Ranges, and Griddles will now heat up their surroundings -
don't turn them on around plasma!
fix: Fixes being able to cook in an Oven while the room is depowered
qol: Hitting a customer bot with an incorrect recipe no longer counts as
a hostile attack leading to your demise shortly after
refactor: Customer bots that request a reagent now use custom orders
code: Cut down a lot of code in the crafting menu code, and removes some
ugly ispaths
del: Soup is no longer food items, so can't appear in random food pools
(at least not yet).
balance: Virus Food recipe now requires you cool it to 200k.
/:cl:

---
## [openbsd/src](https://github.com/openbsd/src)@[e4c559e853...](https://github.com/openbsd/src/commit/e4c559e853ce1cc130d8342715a65ada3e5f26e9)
#### Sunday 2023-04-09 20:20:19 by tb

Move a few functions out of OPENSSL_NO_DEPRECATED

Geoff Thorpe added OPENSSL_NO_DEPRECATED nearly two decades ago. The hope
was that at some point some functions can be dropped. Most of the functions
marked deprecated are actually unused nowadays but unfortunately some of
them are still used in the ecosystem. Move them out of OPENSSL_NO_DEPRECATED
so we can define it without breaking the consumers in the next bump.

ERR_remove_state() is still used by a dozen or so ports. This isn't a big
deal since it is just a stupid wrapper for the not quite as deprecated
ERR_remove_thread_state(). It's not worth patching these ports.

Annoyingly, {DH,DSA}_generate_parameters() and RSA_generate_key() are still
used. They "make use" of the old-style BN_GENCB callback, which is therefore
more difficult to remove - in case you don't know know: that's the thing
responsible for printing pretty '.', '+' and '*' when you generate keys.

Most annoyingly, DH_generate_parameters() was added to rust-openssl in 2020
for "advanced DH support". This is very unfortunate since cargo bundles a
rust-openssl and updates it only every few years or so. As a consequence
we're going to be stuck with this nonsense for a good while.

ok beck jsing

---
## [EdwardNashton/mojave-sun-13](https://github.com/EdwardNashton/mojave-sun-13)@[237789979a...](https://github.com/EdwardNashton/mojave-sun-13/commit/237789979a56a09589e299cf362a090ae8273805)
#### Sunday 2023-04-09 20:37:54 by ProfessorPopoff

Drought babyyyy!! Spawners/Mobs distribution. Baron town and more (#2326)

Okay! So basically this is an unatomized PR. This adds in a lot of things that we need for Drought to be the best it can. It includes things like a mappersprite edit cape for the Baron.... Crafted terminal fixes... A bunch of structure visual shifts, new pipes added- a metric FRICK ton of new walls SPECIFICALLY FOR DROUGHT.

Legion have gender checks now. If you're not a male, it makes you a male and gives you a random legion name. They're pretty cool. Similar situation with the Baron. Female becomes male. Gets cool name. You get the jist.

NOMADS. Nomads are Wastelanders that look different. Specifically for Drought. yippie.

On top of any coding changes, obviously there's a ton of work put into Drought itself. There's mobs and loot dispersed through the map. Well? I don't know yet. We'll see in testing. I personally added two locations. The Barony, and some little adobe shacks on the long stretch to the raider base. I've fixed up a TON of errors, go count them all! There's likely more left. I was as thorough as I could be.

---
## [katubug/CottageWitch119](https://github.com/katubug/CottageWitch119)@[8daec2500a...](https://github.com/katubug/CottageWitch119/commit/8daec2500adc2c5ab45c04874776ce9943cef467)
#### Sunday 2023-04-09 21:49:55 by Katu

1.13.0a

Misc:
- Ambient Sounds have now had their volume strongly reduced. This can be changed by accessing the Mods menu and searching for the Ambient Sounds entry, then configuring from there.
- Backpacked! packs have had their inventory doubled from 9 to 18.
- The welcome quest now grants a Quark Backpack as a reward.
- Withers, Lightning, and the Ender Dragon will no longer be audible to the entire server.
- The game will now ding once it's done loading.
- Flower collecting quests no longer require Sprout hybrid flowers.
- New flowers have been added to the Flower collecting quests.
- New quests have been added for the following mods:
-- Backpacked! (Armor and Tools)
-- Customizable Elytra (Armor and Tools)
-- Environmental (Armor and Tools, Wildlife)
-- Magic Mirror  (Armor and Tools)
-- End's Delight  (Culinary Arts)
-- Reaping (Farming)
-- Spelunkery (Misc)
-- Gateways to Eternity (Wildlife)
- Altered the text of the Create: Central Kitchen quest to warn against using it in the Akashic Tome.
- Added tutorial quest explaining the Akashic Tome controls.
- Plushies have been added as quest rewards for lots of quests!
- A crafting recipe to duplicate plushies you've earned has also been added.
- The Globetrotting Quest "Bearclaw Inn" has been changed to correctly be "Sunken Ship."
- The Balloon Box quest hopefully now correctly fires only when a Balloon Box chest is obtained.
- Hostile Mobs quests have had their icons changed.
- There is now a repeatable quest to kill spiders, which offers drops from the bugs which have been disabled from Alex's Mobs.
- JEI recipe categories have been sorted to hopefully provide a more helpful recipe-lookup experience.
- Raw pasta now accepts any eggs.
- Duck meat is now correctly tagged and can be used in more recipes.
- Farseers spawns have been adjusted back to normal.
- Skreechers no longer spawn in Ancient Cities, they spawn only in the Otherside.
- Wraiths and Cindershells now spawn in the Otherside.
- Tarot Card The Sun's effect has been changed from +15% health to +10% health.
- Spice of Life has been largely rebalanced. It has had its max value changed from 31 to 100. It grants slightly more hearts, but it takes more food to earn them. If maxed, a bonus of "permanent" Nourishment effect is given.
- Added a recipe to make Larger Dragon Egg Shell.
- Backpacked! packs can now be crafted from Quark Backpacks.
- BYG colored sand now properly crafts into sandstone blocks.
- Added tags to Reaping Tools to show effectiveness.
- Coal is now fully compatible with 3-tier Compacting Drawers.
- Glowsticks now accept more variant ingredients.
- Better Fishing's Mixed Ore now accepts deepslate variants of ores.
- New foods, drinks, ingredients, flowers, and plants have been added to the searchable tooltips.

---
## [gilch/hissp](https://github.com/gilch/hissp)@[6b62c703bd...](https://github.com/gilch/hissp/commit/6b62c703bdcbf5597aab523a55460fa0c9e67063)
#### Sunday 2023-04-09 21:52:34 by gilch

Remove code of conduct

On reflection, it seems like more trouble than it's worth right now.
Despite writing one on GitHub's recommendation,
this kind of thing would tend to scare me off of a project rather than make me feel comfortable,
the same way a "privacy policy" would make most people uncomfortable.
("Oh, you feel the need to legally cover yourself because you're in a position to be doing potentially shady things with my private information?
So you're going to make me comb through pages of legalese to find the gotchas?
Gee, thanks."
Similarly, needing a "code of conduct" suggests there was past community misconduct.
We're not there yet, and I don't want to suggest we are until that happens.)
I'd rather rely on present GitHub norms than try to invent my own.
It can be resurrected from the repo (or rewritten) if it ever becomes necessary.

---
## [LJmartin94/Unity_WorldMap](https://github.com/LJmartin94/Unity_WorldMap)@[cde66c9431...](https://github.com/LJmartin94/Unity_WorldMap/commit/cde66c9431168c31452dc0677d3c3e2e13d4d835)
#### Sunday 2023-04-09 22:47:00 by Lindsay

Start fresh in Unity

Using MLX was going to be more of a pain than a time saver, and Thijs showed me an amazing youtube series doing something very similar to what I wanted in Unity, which is exactly the engine I wanted to switch to once I had my prototype. Sorry Leon!

---
## [TheDarkElites/Foundation-19](https://github.com/TheDarkElites/Foundation-19)@[e4613632cc...](https://github.com/TheDarkElites/Foundation-19/commit/e4613632cc5b9ab4363d8c768752d74623e9112b)
#### Sunday 2023-04-09 23:21:00 by Grey

Remove ERT Code that makes it so you can't call the shuttle for 30 minutes (#639)

* gets rid of old dumb code

* Revert "gets rid of old dumb code"

This reverts commit a816ca0c26964781b8a0bdf2d1af4858bc76964d.

* simpler implementation (i was strongarmed)

* removes the datum

* fuck your predicates they're not used anywhere

* Revert "fuck your predicates they're not used anywhere"

This reverts commit eefa96c718892a74936efff85b96edbef4382c0a.

* Revert "Revert "fuck your predicates they're not used anywhere""

This reverts commit 6ad00652eda432e76c4cf1a6edf0ff0ee4bcafa8.

* THIS TIME WE ACTUALLY REMOVE THE DME RIGHT

---
## [LesmusTrompiz/Krakenvolution](https://github.com/LesmusTrompiz/Krakenvolution)@[9a42197d82...](https://github.com/LesmusTrompiz/Krakenvolution/commit/9a42197d823bb6853ba071c63dd97f9f5084159e)
#### Sunday 2023-04-09 23:28:39 by Diego Morales Román

Changed the arguments so that it works with the fucking stupid ROS2 working conditions. Angel increase my salary by twofold

---
## [cortex-command-community/Cortex-Command-Community-Project-Source](https://github.com/cortex-command-community/Cortex-Command-Community-Project-Source)@[bfb278c026...](https://github.com/cortex-command-community/Cortex-Command-Community-Project-Source/commit/bfb278c0267f2b7a177d9bb0063ef3145f9f625b)
#### Sunday 2023-04-09 23:30:42 by MaximDude

VS2019 is being super stupid about C++20 so we gotta do some conditional hacking to not deprecate it

Increase precompiled header memory allocation limit from default 75mb to 225mb otherwise it shits itself trying to build the pch for reasons unknown to (this) man
Compile everything Lua with C++17 - can't really find a solution for this, it shits itself from Boost garbage via LuaBind the same way it does if enabling pch or conformance in these CUs and I just don't wanna deal with those piles of shit
Complementary AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[bd4392ab74...](https://github.com/tgstation/tgstation/commit/bd4392ab7463c383c7e2824f8a9b7d154ad7940c)
#### Sunday 2023-04-09 23:51:37 by Bloop

New inhand icons for light tubes, makes latex balloons craftable, and various other fixes/improvements (#74576)

## About The Pull Request

This ended up turning into a bit of a junk drawer of a PR I'll admit,
but there's really not a whole lot to it.

There are three parts:

### Part I - Inhand sprites for light tubes.

Adds inhand sprites for light tubes. No more cardboard tube placeholder.
This is self explanatory-they have unique sprites for all 3 states
(normal, broken, and burnt out). The broken version has sharpness now.

Also refactored light_items.dm a bit, it was using a bespoke proc called
`update` to do icon updates. Now it has been _updated_ to use
`update_appearance` instead.


![dreamseeker_6WC8vJMiBW](https://user-images.githubusercontent.com/13398309/230615134-31c51e94-cee5-4eef-ba63-c348a3b2debc.gif)

### Part II - Latex Balloons

Latex balloons, a very old piece of code that was full of typos, has had
some life breathed back into it. It is a fun little item, and I saw no
reason to let it rot. It can now be crafted using a latex glove and some
cable. Also, you can pop them using anything sharp... such as a broken
light tube! Aha!

We've come full circle.


![image](https://user-images.githubusercontent.com/13398309/230617764-3a304fd2-05d0-4b2f-b420-056a93c0dce3.png)

### Part III - update_inhand_icon proc

A new atom helper function, `/atom/proc/update_inhand_icon(mob/target =
loc)`

I was struggling to find an existing proc that could update inhand icons
of a mob that was holding any given atom, without necessarily having a
ref to the mob yet.

So I ended up writing one that did that, and finding the spots in the
code which were using a similar way of doing it (that is in fact how I
stumbled upon the latex balloon item).

...........But then Iearned of the
`/datum/element/update_icon_updates_onmob` component and ended up using
that instead. There are still some very niche cases where you might not
be able to use the component where the proc would come in handy however
e.g. in transforming.dm--and if anything, I think it could serve as a
good spot to leave a comment informing would be users of
`update_icon_updates_on_mob` as an alternative.

For that reason especially I thought it worth keeping. 

## Why It's Good For The Game

New inhand sprites, and a fun little craftable balloon. What's not to
like?

## Changelog

:cl:
add: latex balloons can now be crafted using a latex glove and some
cable. You can fill them with air using a tank. They also have a new
sound effect.
imageadd: light tubes have a new inhand sprite
fix: broken light tubes now actually have sharpness to them as they are
basically spikes of glass.
refactor: refactored latex balloon code
/:cl:

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[c0ef4ba907...](https://github.com/JohnFulpWillard/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Sunday 2023-04-09 23:53:43 by tralezab

Adds the Dark Matt-eor when you emag a stupid amount of meteor shields + lots of meteor file sorting + qol + dark matter singularity + dark matt-eor summoning final traitor objective (#74330)

## About The Pull Request

<details>
  <summary>Dark Matt-eor Image</summary>
  

![image](https://user-images.githubusercontent.com/40974010/228368755-34ae5f89-e1bb-498b-bbf8-a14ff4240dc0.png)

</details>

> A barely visible blur in the cosmic darkness, like a ghostly shadow on
a moonless night. A piercing howl in the vacuum of space, as if it were
tearing the fabric of reality. A twisted halo of light around it,
bending and breaking the rays of distant suns. A shower of quantum
sparks, flickering and fading in its wake. A dark matter meteor (dark
matt-eor) is a wonder to witness, and to dread.

> A sudden impact, like a hammer blow to the heart of the station. A
violent tremor, shaking and shattering the metal walls and windows. A
deafening roar, as the air rushes out of the breached hull. A blinding
flash, as the dark matter meteor unleashes its hidden energy. A tiny
black hole, forming and growing in the center of the station. A
relentless pull, dragging everything towards the abyss. A dark matter
meteor is incredibly deadly.

Emagging too many meteor shields will summon a dark matt-eor. This comes
with several warnings, and after awhile, warns the station that someone
is trying to summon a dark matteor.

The dark matt-eor itself is not that damaging in its impact, but drops a
singularity in its final resting place.

## Why It's Good For The Game

It's a new way to terrorize a round as an antagonist. Before, emagging a
lot of meteor shields would basically make meteor showers the only event
that can run, which is cool, but since constant meteor waves are going
to destroy the station, let's also throw in the mother of all meteors!

This also adds warnings to spamming emagging meteor shields, which imo
needs it. The round ends when someone spams emagged meteor shields, and
since they're meteor shields nobody is going to reasonably check on
them.

## Changelog
:cl:
add: The dark matt-eor
add: Summon a dark matt-eor final traitor objective
add: Dark matter singularity variant, which can't grow as big as a
regular singularity but hungers for blood
code: cleaned up/sorted meteor shield code, satellite control, and more
qol: added a lot of feedback to interacting with meteor shields
balance: emagging a lot of meteor shields warns the station, but
emagging enough of them summons a Dark Matt-eor.
/:cl:

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[ccef887efe...](https://github.com/JohnFulpWillard/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Sunday 2023-04-09 23:53:43 by san7890

Lints Against Unmanaged Local Defines (#74333)

# MAINTAINER - USE THE BUTTON THAT SAYS "MERGE MASTER" THEN SET THE PR
TO AUTO-MERGE! IT'S MUCH EASIER FOR ME TO FIX THINGS BEFORE THEY SKEW
RATHER THAN AFTER THE FACT.

## About The Pull Request

Hey there,

This took a while to do, but here's the gist:

Python file now regexes every file in `/code` except for those that have
some valid reason to be tacking on more global defines. Some of those
reasons are simply just that I don't have the time right now (doing what
you see in this PR took a few hours) to refactor and parse what should
belong and what should be thrown out. For the time being though, this PR
will at least _halt_ people making the mistake of not `#undef`ing any
files they `#define` "locally", or within the scope of a file.

Most people forget to do this and this leads to a lot of mess later on
due to how many variables can be unmanaged on the global level. I've
made this mistake, you've made this mistake, it's a common thing. Let's
automatically check for it so it can be fixed no-stress.

Scenarios this PR corrects:

* Forgetting to undef a define but undeffing others.
* Not undeffing any defines in your file.
* Earmarking a define as a "file local" define, but not defining it.
* Having a define be a "file local" define, but having it be used
elsewhere.
* Having a "local" define not even be in the file that it only shows up
in.
* Having a completely unused define*

(* I kept some of these because they seemed important... Others were
junked.)
## Why It's Good For The Game

If you wanna use it across multiple files, no reason to not make it a
global define (maybe there's a few reasons but let's assume that this is
the 95% case).

Let me know if you don't like how I re-arranged some of the defines and
how you'd rather see it be implemented, and I'd be happy to do that.
This was mostly just "eh does it need it or not" sorta stuff.

I used a pretty cool way to detect if we should use the standardized
GitHub "error" output, you can see the results of that here
https://github.com/san7890/bruhstation/actions/runs/4549766579/jobs/8022186846#step:7:792
## Changelog
Nothing that really concerns players.

(I fixed up all this stuff using vscode, no regexes beyond what you see
in the python script. sorry downstreams)

---

