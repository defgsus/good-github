## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-25](docs/good-messages/2023/2023-06-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,735,261 were push events containing 2,629,035 commit messages that amount to 163,638,353 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [Duzos/superhero](https://github.com/Duzos/superhero)@[94012adc83...](https://github.com/Duzos/superhero/commit/94012adc83b99a4e35e578d70463a3db562a6f11)
#### Sunday 2023-06-25 00:02:12 by Duzo

Holy Fuck.
Added particle and rope for spider swing
Added sounds for spider swing
And I hate it all.
Cant wait for Loqor to see it, point out the obvious flaws I havent fixed yet because ive been working on this for hours now and then shit all over me by saying how "easy" it is to do.
Fuck you, tough luck, this is what you're getting.

---
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[c67d6a22a4...](https://github.com/Capsandi/tgstation/commit/c67d6a22a405f006a9d7a537dc35cecbdb65cfde)
#### Sunday 2023-06-25 00:17:11 by Kyle Spier-Swenson

fix stupid error message in delay pre-game (#75824)

tabbing out during init after hitting the verb, while you wait for the
server to un-lockup and present you with the prompt, and coming back in,
noticing you were too late, and cancelling out of the time prompt, only
to get told the round had already started, was kinda fucking lame. I
know, thats why i fucking hit cancel you fucking robit.

also makes the proc more early return

---
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[d01b433ab1...](https://github.com/Capsandi/tgstation/commit/d01b433ab12e7aa45416d42f9045f1135e545dae)
#### Sunday 2023-06-25 00:17:11 by Sealed101

Fixes colossus possessor crystal cockroaches/animals not dumping the user's body upon death/gibbing (#75843)

## About The Pull Request
Hooks the stasis closet thingamajing into `COMSIG_LIVING_DEATH` instead
of checking the animal's stat on `process()`, which makes possessed
animals properly dump the stasis closet's contents upon death or gibbing
(which is death but cooler).
yeah uh this method is hilarious but it does protect the user's body
quite reliably at least lol

## Why It's Good For The Game
Fixes #75829
also probably makes cockroach death saner in some unreported way, this
`. = ..()` vs `..()` is above my non-existent paygrade but it keeps
popping up from time to time

## Changelog
:cl:
fix: gibbing colossus possessor crystal possessed animals will no longer
stick the user's body and their stuff into the shadow realm. the animals
will properly drop your corpse when killed or gibbed
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[18819cc7fb...](https://github.com/Latentish/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Sunday 2023-06-25 00:41:07 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[daa33d89fe...](https://github.com/tgstation/tgstation/commit/daa33d89fef10650f89f7db160f110141ab99e5d)
#### Sunday 2023-06-25 00:59:10 by IndieanaJones

Xenomorph/Alien Rework 2023: Part 1 (#75286)

## About The Pull Request

Alternative to #75277

Kept you waiting, huh?

This PR is the first part of a Xenomorph rework which seeks to make the
big lugs more balanced and up to date with /tg/'s current design. This
mainly involves curtailing xenomorph's infamous hardstuns into more
interactive forms of combat, while also giving some buffs to the
xenomorph's more unique abilities in order to keep them threatening.

Part 1 will focus on simple number changes and some simple mechanic
changes. In the future, changes will be made to endgame involving
xenomorphs, along with changes to other facets of Xenomorphs.

Highly based off of #55937.

Changes:

- Xenomorph disarm has been completely reworked. While a disarm will
attempt to, well, disarm, a human opponent should they be holding
something, it will no longer immediately hardstun targets when they
aren't. Instead, the xenomorph will shove the target several tiles back
and inflict 35 stamina damage. If the target slams into a wall, this
will also come with the added effect of knocking them down. If a human
is incapacitated, however, right click will slam them into the ground,
which paralyzes them for a lengthy 5 seconds (which is ultimately half
the time xenos could stun you for before), allowing for safe transport
back to the nest as long as you keep them close.

- Humans can now shove xenomorphs. Due to being the superior predator,
however, you can't knock down xenomorphs from shoving. You can slow them
for a little bit akin to humans though.

- Neurotoxin no longer is a hardstun. Instead, it deals 50 stamina
damage on contact. It is still resisted by BIO armor.

**HUNTER:**
- Speed reduced from -1 to -0.3.
- Pounce speed is twice as fast as before (1 to 2)
- Hardstun time on pounce reduced from 10 seconds to 5 seconds.

Hunters being insanely fast has been a major balance-ruining factor of
xenomorphs for many years now. These buggers could practically ambush
anyone, hardstun them immediately, and then leave before anyone could do
anything. Now, with their speed nerfed and in combination with the xeno
shove changes, hunters will need to spend more time to down a target.
Their pounce was practically useless, so its been sped up in order to
make it more practical to use.

**SENTINEL**
- Speed reduced from 0 to 0.2
- Cloak alpha reduced from 0.75 to 0.25 (you're more hidden now)

Sentinels receive a large nerf in regards to their spit, but their
before useless cloaking ability has been greatly improved upon as
compensation. They now serve better as defenders and ranged ambushers.

**XENOMORPH DRONE**
- No changes

As in the original PR, drones are perfeclty balanced in my eyes, so no
changes were required.

**XENOMORPH PRAETORIAN**
- Speed increased from 1 to 0.5
- No changes

Praetorians get affected by the nerfs of the other xeno abilities, but
now they're a bit faster in order to close the gap to use their
abilities.

**XENOMORPH QUEEN**
- Speed increased from 3 to 2
- Health increased from 400 to 500
- Damage increased from 20 to 50

Xenomorph queens have been sped up and made more tanky and lethal in
close-range combat. Fighting this beast up-close should be a death
sentence to almost anything else in the game. Speed increases will help
her re-position and close the gap on potential prey.

**OTHER CHANGES**
- Fixed a bug where simplemobs didn't actually use xenomorph's damage
values when they were attacked by them.

## Why It's Good For The Game

Xenomorphs are old, and haven't been updated for quite a long time. This
has left them as sources of a bunch of hardstuns which made counterplay
from a modern spaceman extremely difficult. With these changes, fighting
xenomorphs is more interactive and should end up being more enjoyable
for both crew and xenos. Buffs were also given out to incentivize usage
of xenomorph's unique abilities as opposed to the standard disarm spam
which was most effective for them until now.

## Changelog
:cl:
balance: Xenos have been rebalanced, removing their hardstuns on their
disarm and neurotoxin, along with a slew of other changes. Xenos have
received buffs to their more unique abilities in return.
fix: Fixed simplemobs ignoring xenomorph's melee damage values when
being attacked by them.
/:cl:

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[99149fba2d...](https://github.com/mc776/freedoom/commit/99149fba2d2dd99ff83cf304e80e1f49ae0affc3)
#### Sunday 2023-06-25 01:03:03 by mc776

levels: various minor fixes. (#990)

* levels: various fixes.

E1M2
Fixed some missing and misaligned textures around the secret lowering computer block.

E2M5
The red key bars could both be squeezed through and jumped around on a jump-enabling sourceport. The red key now raises the stairs instead, and the final door before the exit also requires a red key.

E2M7
Added one more bar in front of the exit to prevent squeeze glides.

E3M2
Expanded yellow key pillar so it would match the flat.

E3M6
Untagged the skylight inside the secret as being itself a secret.

E4M1
That line of health and armour bonuses just inside the big building would have a few floaters. They've all been moved forward and should be fully clear of that ledge.

Map05
The pit with the central column of water and the spectres was being blocked off by said spectres before the player could jump into it. There is now a monster blocking line right in front of the ledge, barely far enough to guarantee space for you to drop but close enough to let the pinkies bite.
You can now freely move through the gaps between any of the objects in the blue key room.
The exit from the blue key building now has a lift instead of stairs, and the wall prevents the nearest pinkies from seeing you until you've actually dropped inside. Hopefully this at least mitigates the problem of being stuck on the stairs with a pinkie right below your ability to target.
Miscellaneous aesthetic tweaks.

Map07
The lift overlooking the big arena was still suffering from monsters blocking from below. It has been moved to the side with an intervening ceiling.
The central grey aquatex nukage trim hub was a cross shape and the exits all had very strong lines turning right, making it look like a swastika. The southern section has been tweaked to throw off the symmetry and avoid that impression.
Made it possible to move all the way around the stack of crates in the eastern area with the switch.
Miscellaneous texture improvements.

Map08
The exit bars are now impossible to squeeze glide through. They are also styled in the same manner as the moving pistons by the big switches, giving the suggestion that they would be moved in a similar manner.

Map09
Fixed some floating pickups at the collapsed roof, the red key room, and the stairs to the warehouse admin area.
Shotgun guys in the admin area switch room are now situated between the deep cracks that were preventing their movement.

Map12
Turned the two wall-facing enemies around near (2016,96).
Added a second trigger line for the minigunner ambush store room so it happens even when you approach it from the other side.
Added a second switch for the bars normally opened before reaching the storage room ambush.
Replaced the BFG secret with a megasphere since you already get a BFG in Map11.

Map18
There were some lamps on the lower floor of the southwest room that were invisible from the higher floor but would block your movement. All major blockers have been deleted or moved to the edge of the room.
The tree near the red armour to the right of the start has been moved for similar reasons.

Map20
Moved some pickups (and the dead body) away from the bottom sides of the steps to reduce the chances of someone bypassing them while moving downwards.
Made the armour/health bonus placement more unambiguous around the cross and star.
Simplified the bridge around the red key so that the rising portion is only one sector.

Map22
Because this map has been disproportionately harder to pistol start than anything near it...
Moved all 4 player starts into the starting elevator to avoid a hot start.
Flagged some ammo pickups as appearing on all skill levels, as well as the southern super shotgun and the starting area armour. The easy-only SSG in the starting area is now a chaingun and appears on all skill levels.
The starting shotgun is now only available on easy, with two shotgunners (one of them guarding the armour) in its place on medium and hard.
Differentiated the walls of the starting elevator so you know which way to face, and made the switch resemble the normal (but broken) SW1TEK.
The switch system itself is simplified and given a simpler implied story: the big switch is broken, so you locate and use the backup system. The switch shooting is gone.
Made the fringe around the lava elevator go all the way around and populated it with health bonuses to make it clear you're actually expected to go down there, because frankly the original is so thoroughly obscured it looks like you're breaking sequence by exploiting an oversight in the map.
Extended the staircase down from the brown platform to mitigate the "pinkie right in front of you below your aim" effect.
Added a medikit near that brown platform.
The armour in the crate hall is now a medikit.

Map24
The hanging bodies in the red key room are now the non-blocking versions.
The trilobite stuck on the teleport pad in the square maze is now an octaminator so it doesn't get stuck.
The lines around the door leading to the serpentipedes with their backs to you no longer block sounds.
Removed the sound block flags on the octaminator ambush doors, so the pinkies can join in if you start shooting at them instead of powering through into the new room.

Map26
Health bonuses under crusher were floating.

Map27
Lizardbaby platform now has a full 72 unit clearance.
Spectres in the red rock area to the northeast are now in the tunnels and only come out when you land in the red water.

* levels: fix one screwy texture.

Monitor in the room west of the westmost shiny lowering shelf thing.

* levels: more minor fixes.

E2M1
Life surge secret was marked on the thin doorway, making it possible to fail to register even after you've taken the surge. The secret is now the room itself, at the cost of that random light effect.

E2M6
Life surge secret was marked on the thin central bit of the sigil, leaving *lots* of room to step around it while grabbing the powerup. (The fact that the red makes it kinda look like a hurtfloor really doesn't help.) The secret is now the larger room itself.

Map12
New eastern storage room trigger wasn't covering the entire hallway. It should also be diagonal to minimize the chance of it being skipped entirely.

Map28
The serps on the ledge by the bloodfalls and fleshy sigil were facing the wall and marked as ambush. They now face the actual play area.

Map29
Moved all the secret pit pickups a little bit further inside the square so they look like they're resting on the surface of the solid floor.

Map30
The multiplayer-only spawn pickups are now flagged as multi-only.

* levels: tiny map04 aesthetic tweak.

The fake contrast exaggerates the shadow on some "AGM" silver columns while eliminating the shadow on others. These are often right next to each other on the screen, producing absurd results. This moves 1 vertex from each affected line 2 pixels so they are no longer orthogonal.

---
## [NoTerrainTires/liteSS13](https://github.com/NoTerrainTires/liteSS13)@[e4ece2fbd6...](https://github.com/NoTerrainTires/liteSS13/commit/e4ece2fbd62dfa6a1270ce37e31fe93bd1823c07)
#### Sunday 2023-06-25 01:36:22 by Hatterhat

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
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[64eae49042...](https://github.com/Rustybuckets6601/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Sunday 2023-06-25 02:19:34 by necromanceranne

Replaces the Reaper Scythe with the Vorpal Scythe (also the Morbid trait) (#75948)

adds the Vorpal Scythe, a special chaplain null rod variant, replacing
the Reaper Scythe, a not so special null rod variant.

When you choose the vorpal scythe, it comes as a shard that you implant
into your arm, similar to a cursed katana.

Once implanted, you can draw it at any time like an arm implant.
However, sheathing it again presents some problems. (Also, implanting
the organ gives you ``TRAIT_MORBID``, which I'll explain in a bit)

The Vorpal Scythe has 10 force, one of the weakest null rod variants for
force that isn't a joke null rod. However, it has exceptional armor pen
and also has 2 tiles of reach. So quite unique.

It also has a special beheading ability when you right-click someone.
This borrows some code from amputation shears, functioning pretty
similarly, except with a few additional ways to speed up the action and
restrictions. (It takes 15 seconds baseline to behead someone standing
and conscious, and speeds up or slows down based on factors such as
incapacitation and whether or not our scythe is already empowered)

When you successfully behead someone with a mind, the vorpal scythe
gains 20 force and can be safely stowed and drawn for 2 minutes.
Performing more death knells like this will reset the timer.

If it has not performed its 'death knell', or you haven't hit a living
mob, then it will cause severe damage to you if you ever try and stow it
(or its forced back into your arm). Just hitting a mob with the scythe
will sate it for 4 minutes. Unless it is a non-player monkey. Horrible
things. Just hitting mobs does not reset the timer on empowerment.

What this means is that the chaplain may be more hesitant to simply draw
their weapon on people. It also means that potentially, the chaplain
will not always have magic immunity, since they may end up stowing the
weapon away and be reluctant to draw it on a whim without either taking
damage for sheathing it without hitting something, or dealing with
having one less hand up until they can.

While empowerment only happens when you behead mobs with a mind,
beheading monkeyhumans and other mindless humans subtypes causes their
heads to become haunted! It's mostly harmless and largely just SpOoKy.
We don't want heads with actual players in them to go floating off to
space. (Does not work on monkey heads for sanity reasons)

When you have the Morbid trait, you think creepy stuff is cool and hate
saving peoples lives. You get a mood boost from graverobbing, autopsies,
dissections, amputations (including beheadings with the scythe and
amputations with the shears) and revival surgery. However, you get a
mood penalty when you tend wounds on the living, as well as a hefty
penalty when you perform CPR or defibrillate someone. I was thinking
Victor Frankenstein when I was choosing which actions had an associated
moodlet, so anything that I might have missed would be appreciated.

You also count as potentially cool with regards to haunted objects.
Ghosts think you're neat. (Revenants probably will still kill you if
they had the chance)

---
## [ksylvan/evals](https://github.com/ksylvan/evals)@[aeeb452867...](https://github.com/ksylvan/evals/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Sunday 2023-06-25 02:57:31 by Alexander Raul

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
## [ksylvan/evals](https://github.com/ksylvan/evals)@[bf2ebb9dd6...](https://github.com/ksylvan/evals/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Sunday 2023-06-25 02:57:31 by Amir DIB

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
## [ksylvan/evals](https://github.com/ksylvan/evals)@[38f40050e9...](https://github.com/ksylvan/evals/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Sunday 2023-06-25 02:57:31 by dz-pika

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
## [ksylvan/evals](https://github.com/ksylvan/evals)@[b2250e4117...](https://github.com/ksylvan/evals/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Sunday 2023-06-25 02:57:31 by shivamd1810

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
## [ksylvan/evals](https://github.com/ksylvan/evals)@[9fdbd94c93...](https://github.com/ksylvan/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Sunday 2023-06-25 02:57:31 by Tong

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1f4ceff110...](https://github.com/treckstar/yolo-octo-hipster/commit/1f4ceff110cbda9875c05164d649435e09e6f004)
#### Sunday 2023-06-25 03:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [axietheaxolotl/Skyrat-tg](https://github.com/axietheaxolotl/Skyrat-tg)@[79febdf95d...](https://github.com/axietheaxolotl/Skyrat-tg/commit/79febdf95dbcdb81d6a8027dc21deba19f8e659e)
#### Sunday 2023-06-25 04:37:23 by SkyratBot

[MIRROR] New planetary exclusive random event/unfavorable situation, Chasmic Earthquake [MDB IGNORE] (#21778)

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

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

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [markhepburn/dotemacs](https://github.com/markhepburn/dotemacs)@[d8edf0c727...](https://github.com/markhepburn/dotemacs/commit/d8edf0c727acd62a2885657da8f6b8e52a60962c)
#### Sunday 2023-06-25 04:49:13 by Mark Hepburn

Add in olivetti mode

Super handy, I just have to remember to use it! When I don't want
auto-fill enabled, but still want margins for a better writing
experience, this fiddles with margins instead of me having to hack
around with windows (not that much practical difference in the end I
suppose, but it could be a full-screen no-distraction experience if I
wanted)

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[c4b550c1a9...](https://github.com/OrionTheFox/Skyrat-tg/commit/c4b550c1a94670ae333df12b8200ff33f7f7f175)
#### Sunday 2023-06-25 05:29:47 by SkyratBot

[MIRROR] New Wizard spell "branch": Vendormancy [MDB IGNORE] (#22008)

* New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

* New Wizard spell "branch": Vendormancy

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

---
## [Sharkalien/Godot-YOU-THERE.-BOY.-Walkaround](https://github.com/Sharkalien/Godot-YOU-THERE.-BOY.-Walkaround)@[033f3a1f61...](https://github.com/Sharkalien/Godot-YOU-THERE.-BOY.-Walkaround/commit/033f3a1f61eb0138c8adccbbd4cb275837e9df1d)
#### Sunday 2023-06-25 06:00:27 by Leo Esc

Delete stupid fucking bullshit from stupid fucking GitHub bullcrap

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[a8e16030f8...](https://github.com/Sealed101/tgstation/commit/a8e16030f83911aef695ba9f28d565c41c99c3e6)
#### Sunday 2023-06-25 06:21:00 by LemonInTheDark

Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Reduces timer insertion cost by
80%](https://github.com/tgstation/tgstation/commit/c9e5b285ed74e60108fddd3f6b45d6d3995c92a8)

Timer name generation involved a LOT of string shit, some in ways where
the string only existed for a moment.
This costs a good bit of time, and can be reduced with only minimal
impacts on the end product, so let's do that. Includes a compile flag to
flip it back if we ever have trouble in future.

This is about 0.1s off init, since we do a lot of timer stuff then too

[Removes STOPPABLE flag from QDEL_IN, moves it to a bespoke
macro](https://github.com/tgstation/tgstation/commit/e7a5d7f2a78fcf0dce4742ced258c9505411b202)

Its a waste most of the time, tho I would LOVE to analyze at compile
time to work out if we care
## Why It's Good For The Game

I like it when we don't spend all of our cpu time just setting the name
var on timers. that's good and not bad.
This saves time fucking everywhere. 15% off explosions, 0.1 seconds off
init, bunch of time off foam. it's just good.

Cherry picked out of #76104 since that was too cluttered (sannnnnn)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[5c032cc098...](https://github.com/Sealed101/tgstation/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Sunday 2023-06-25 06:21:00 by LemonInTheDark

Adds border smoothing! (Look ma I'm upstreaming) (#76134)

## About The Pull Request

Ok so we currently have 1 (count em) border object that wants to smooth
with other border objects. That's the tram window.

It currently does this manually, via map edits, but that's kinda crappy
so lets be better.

This pr adds a new smoothing mode to handle border objects. 
Unlike other smoothing modes, it returns a bitfield of directions the
border object connects in.

I do this by memorizing a calculation of which dirs "connect" at init,
and reading out of a global list with border object direction, direction
between objects, and if it's a border object, the other object's dir.

I'm doing this primarily because it's become useful for wallening (a
spriter saw the tram thing and is doing the same thing to pod windows,
and I want to support that)

I do think it's potentially useful in other applications too tho, and I
like dehardcoding tram windows.

Also fun bonus (or maybe downside), it's nearly 0 cost because I pulled
the bitmask smoothing define into 2 subdefines, and am swapping the
handler one out to do what I want.
Oh also I got rid of a for loop in smoothing code, redundant and costs
time in list iteration

[Moves tram windows over to the new border object
smoothing](https://github.com/tgstation/tgstation/commit/114873679c94d680788edee9665fa18dba8108c0)

Also replaces some typepath chicanery with a setDir override, for
redundancy in future
Oh and there's a update paths script too, to be nice

## Why It's Good For The Game

More visual possibility in future, fixes a hack we have currently, and
makes some spriters happy.

## Changelog
:cl:
fix: Dehardcodes some stuff with tram windows, they'll be easier to map
with now
refactor: Border objects can now smooth with each other. I'm sure
something cool will come of this
/:cl:

---
## [Midrewza/odin-recipes](https://github.com/Midrewza/odin-recipes)@[44692575b1...](https://github.com/Midrewza/odin-recipes/commit/44692575b1f3677843819b35e1807f72bc79d7a1)
#### Sunday 2023-06-25 06:59:51 by Michael Garza

Finish Iteration 4: Add More Recipes

Instead of adding 2 more recipes, I have added a total of 3 recipes to
this project. All pages have an identical structures with little
differences if any.

I will explain what updates have been created as this is a pretty big
update.

Created a new directory: images
- I chose to house the images in this project into a directory instead of
having links of every image. The reason for this change is there may be a
possibility that the original links to the images could be deleted
resulting in dead links.

Added 3 new recipes to the recipe directory:
- grilled-caribbean-spiced-pork-tenderloin-with-peach-salsa.html
- homemade-peach-crumb-bars.html
- marinated-greek-chicken-bars.html

Each of these files have an identical structure similar to sangria.html
and will feature a link to go back to the main page: index.html

Modifications to file: Index.html
- Change of title: “Tonight’s Date Night!”
- Change of heading h1: “Let’s Solve Date Night at Home!”
- Added a new image below h1 heading to give the page some life
- Created an ordered list instead of an unordered list since the recipes
I have picked are meant to be eaten in an order

Modifications to file: sangria.html
- Change of title: “Sangria! Sangria!”
- Added a new image below h1 heading from images directory
- Rephrased first step within the ordered list for steps
- Added a link to go back to the main page: index.html

This should wrap up my first project with The Odin Project, I honestly
had fun making this more than other first projects I have made with
other courses. Mainly because I felt that I have learned a tremendous
amount more, I used the command line to commit changes to this project
without using the interface you get using VS Code. Utilizing and
understanding what I'm doing in the command line just made me feel more
engaged with what I'm creating. Although the project doesn't look
pretty, I'm sure we will be going back to it to give it some more color.
Thank you TOP, for giving me a more engaging experience creating, this
has been a fun project and I can't wait to continue creating within this
curriculum.

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[8788e48378...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/8788e483788db2432b9649313efc9426d324379f)
#### Sunday 2023-06-25 07:59:30 by Time-Green

Shuttle events (#76008)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/7501474/a2d83ce8-eba1-42d9-a1f8-9d73f7c40b21

Adds shuttle events! Stuff can now start to happen outside the shuttle,
either benign or spicy (but usually just fun to watch)!
## Why It's Good For The Game

The shuttle escape sequence is an important part of the game, uniting
about every player surviving player. Recently, #71906 has made the
escape sequence more forgiving as well as more interesting by
conditionally doubling the playing field. The area outside the shuttle
is still mostly empty though, except for the few people being spaced,
daredevils and the occasional epic space fight.

This PR adds adds some space events to spice up the outside of the
shuttle! This both gives people something too look at, making the escape
sequence feel less static and more lively, as well as give people a
reason to go outside and get the full experience of ~being decapitated
by a meteor~ swimming with the fishes!

<details>
  <summary>Shuttle Events</summary>

**Friendly carp swarm**
Spawns a group of carp that flies past the shuttle, completely friendly
unless provoked.

**Friendly meteors**
Spawns a lot of strong meteors, but they all miss the shuttle.
Completely safe as long as you don't go EVA

**Maintenance debris**
Picks random stuff from the maintenance spawn pool and throws it at the
shuttle. Completely benign, unless you get hit in the head by a toolbox.
Could get you some cool stuff though!

**Dust storm**
Spawns a bunch of dust meteors. Has a rare chance to hit the shuttle,
doing minimal damage but can damage windows and might need inflight
maintenance

**Alien queen**
One in every 250 escapes. Spawns a player controlled alien queen and a
ripley mech. RIP AND TEAR!! Really not that dangerous when you realize
the entire crew is on the shuttle and the queen is fat as fuck, but can
still be fun to throw people around a bit before being torn to shreds.

**ANGRY CARP**
Once in every 500 escapes. Spawns 12 normal carp and 3 big carps, who
may just decide to go through the shuttle or try and bust through the
window if you look at them wrong. Somewhat dangerous, you could stay
away from the windows and try to hide, or more likely shoot at them and
weld the windows

**Fake TTV**
Lol

**Italian Storm**
Once in every 2000 rounds. Throws pasta, pizza and meatballs at the
shuttle. Definitely not me going off the rails with a testing event

**Player controlled carp trio**
Once in every 100 escapes. Spawns three player controlled carp to harass
the shuttle. May rarely be a magicarp, megacarp or chaos carp. I can't
honestly see them do anything other than be annoying for 3 seconds and
die

There are some other admin only ones: a group of passive carps going
directly through the shuttle and just being little shits, and a magic
carp swarm
</details>

Events are selected seperately, there isn't a crazy weighting system,
each just has a chance to run, and multiple could run at once. They also
don't immediately trigger, so people can get settled a bit, and to make
sure just waiting out the more dangerous ones is still a valid strategy.

## Changelog
:cl:
add: Adds shuttle events! If shuttle escapes weren't exciting before
(doubtful), they definitely are now! I'm joking it's mostly an
atmosphere thing.
admin: Adds an admin panel to interact with shuttle events, under the
Events tab: Change Shuttle Events
fix: Objects spawned in hyperspace will properly catch hyperspace drift
/:cl:

There's a few things I'd like to do later (another PR) (honestly anyone
can do them because I suck at follow-ups), because this is too big as
is:
- Hijack triggered shuttle events
- More events (got a lot of cool suggestions, but I'm putting most of
them on hold)
- Maybe stration announcements if some more dangerous ones get added
- Structures appearing next to the escape shuttle???

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023](https://github.com/petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023)@[f8dc169945...](https://github.com/petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023/commit/f8dc169945902af243d01052bece803d3bb78125)
#### Sunday 2023-06-25 10:10:30 by Petre Ro

16.4 Darn! But, yea, that makes sense. We're joining in our new method... and also in addFortuneCookieJoinAndSelect(). Fortunately, we don't need this second call at all anymore: we were joining and selecting to solve the N+1 problem... but now we have an even more advanced query to do that. Copy our new method, delete, then paste it over the old one.

 And now... got it! Only 1 query!

 Yo friends, we did it! Woo! Thanks for joining me on this magical ride through all things Doctrine Query. This stuff is just weird, cool and fun. I hope you enjoyed it as much as I did. If you encounter any crazy situation that we haven't thought about, have any questions, or pictures of your cat, we're always here for you down in the comments. Alright, see you next time!

---
## [petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023](https://github.com/petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023)@[a215f6b0e8...](https://github.com/petre-symfony/Go-Pro-With-Doctrine-Queries-Symfonycasts-2023/commit/a215f6b0e815411a6b56012af904f13db7c70453)
#### Sunday 2023-06-25 10:10:30 by Petre Ro

14.1 WHERE IN()

 We have categories for "Pets" and "Love", but if we search up here for "pets love"... no results! That makes sense. We're searching to see if this string is matching the name or the iconKey. Let's make our search smarter to see if we can match both of those categories by searching word by word.

 The query for this lives in CategoryRepository... on the search() method. The $term argument is the string we type in. Down here, let's say $termList = then explode that string into an array by splitting on empty spaces. If you want a really rich search, you should use a real search system. But we can do some pretty cool stuff just with the database.

 Here's the goal: I want to also match results where category.name is in one of the words in the array.

 Using the IN
 - Right after category.name LIKE :searchTerm, add OR category.name IN. The only tricky thing about this is the syntax. Add (). If we were writing a raw SQL query, we would write a list here, like 'foo', 'bar'. But with the query builder, instead, put a placeholder - like :termList. Below pass that in: ->setParameter('termList', $termList).

 The key thing is that, when you use IN, you will need the parentheses like normal... but inside of that, instead of a comma-separated list, you'll set an array. Doctrine will transform that for us.

 And now... nice! Once you know how it works, it's just that easy.

 Next: You're probably familiar with the RAND() function for MySQL, or maybe the YEAR() function... or one of the many MySQL or PostgreSQL functions that exist. Well, you might be surprised to learn that some of those don't work out of the box.

---
## [sthagen/python-mypy](https://github.com/sthagen/python-mypy)@[0873230ee6...](https://github.com/sthagen/python-mypy/commit/0873230ee60461110bd7bfde7ca3886878aae389)
#### Sunday 2023-06-25 10:37:25 by Ivan Levkivskyi

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
## [andresgutgon/dotfiles](https://github.com/andresgutgon/dotfiles)@[015e7f4116...](https://github.com/andresgutgon/dotfiles/commit/015e7f4116187872a98f38df6a14e32ae0d24582)
#### Sunday 2023-06-25 11:58:31 by andresgutgon

Introduce nvim-dap (Debugger Adapter Protocol) to my NVim
I want to be able to debug Node apps (Specially NextJS) app on backend
side. nvim-dap use DAP protocol from Microsoft which is the one used by
VSCode on their debugging experience. This is the same in Nvim.

To be honest this has been fucking painful for several reasons.
1. First Next.js latest version has fucked their debugging experience.
   So I had to simplify the problem and first understand how node
   `--inspect` flag works on a simple Node server. Then I look into
   existing issues on Next.js and I discoverd that their debugging
   experience is broken in latest version. A [fix is comming in this PR](https://github.com/vercel/next.js/pull/51467)
2. Second. After setting the `nvim-dap` plugin with the VSCode / JS
   debugging experience I spent a shameful amount of time hitting
   `node-terminal` debug mode when in reality was `pwa-node`. Yes, `pwa`
   is ultra weird and that took me time to figure out. [Issue here about
   it](https://github.com/microsoft/vscode/issues/151910)

FUCK! This was hard :joy:

---
## [naikari/naikari](https://github.com/naikari/naikari)@[3a21931f3c...](https://github.com/naikari/naikari/commit/3a21931f3c6ba2b02b11d7d067f6fa8d03207420)
#### Sunday 2023-06-25 12:17:59 by diligentcircle

Alright, we'll keep "oï". (Fucking indecisive on this shit, aren't I?)

---
## [anglo-korean/landing-pages](https://github.com/anglo-korean/landing-pages)@[a5218b8bff...](https://github.com/anglo-korean/landing-pages/commit/a5218b8bffb934b3666c79ba61309465d4beae8a)
#### Sunday 2023-06-25 13:47:51 by jspc

Ensure initialiser deploys

Seriously, why enforce this fucking idiotic directory structure if it means fuck all?

---
## [DvDeval/lobotomy-corp13](https://github.com/DvDeval/lobotomy-corp13)@[b420c1d519...](https://github.com/DvDeval/lobotomy-corp13/commit/b420c1d519b30cd75759de68f6b2abbe0b12a055)
#### Sunday 2023-06-25 13:48:27 by vampirebat74

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
## [Michaelmanicotti/poetry](https://github.com/Michaelmanicotti/poetry)@[8621097e23...](https://github.com/Michaelmanicotti/poetry/commit/8621097e235a716bf7eb23122d8bd8fbfd4547fb)
#### Sunday 2023-06-25 14:11:11 by Michaelmanicotti

Rename Movement III | To the pretty boy I can't stop writing poems about, Fuck You for stealing my heart. to  Movement III | To the pretty boy I can't stop writing poems about, Fuck You for stealing my heart.

---
## [Road-to-56-RP/roadto56rp](https://github.com/Road-to-56-RP/roadto56rp)@[883e35db96...](https://github.com/Road-to-56-RP/roadto56rp/commit/883e35db9668f5cc0e096edc786bd1d81eb07784)
#### Sunday 2023-06-25 14:17:07 by Simpy

Biccy fra decisios (#21)

* heheheha

FUCK YOUWARLIDER

* fuck off

* Added localization to two decision descriptions.

☺ Omg Lider you are so pretty

---------

Co-authored-by: BiccyThiccy <107998094+BiccyThiccy@users.noreply.github.com>

---
## [Road-to-56-RP/roadto56rp](https://github.com/Road-to-56-RP/roadto56rp)@[aad3d0d7b6...](https://github.com/Road-to-56-RP/roadto56rp/commit/aad3d0d7b6e48424407244518baac39789ff9357)
#### Sunday 2023-06-25 14:17:07 by Simpy

Biccy cat decisions (#23)

* Iberia decision files added

Added files for part 1 of the Iberia rework. So far, just changes to Andorra forming Catalonia.

I need 2 things from whoever is looking over them:

1: Removal of the other, less good decision to form it (located in the RT56 base mod)

2: Someone to look over the code  to make sure it isn't fucked. BTW fuck you Warlider

* Completely replaced file. Two decisions for Portugal added

SIMPPYYYYYYYYYYY I LOVE YOU :D

Please fix

---------

Co-authored-by: BiccyThiccy <107998094+BiccyThiccy@users.noreply.github.com>

---
## [shanmukha7k/personal_site](https://github.com/shanmukha7k/personal_site)@[10aa61a512...](https://github.com/shanmukha7k/personal_site/commit/10aa61a512cce6353b2287281a2c012ea1cc11f3)
#### Sunday 2023-06-25 15:21:04 by Shanmukha K

HTML personal site

Welcome to my personal website! Here you will find a curated collection of my work, passions, and insights. From stunning visuals to thought-provoking content, I invite you to explore my portfolio and delve into the creative projects that have shaped my journey. Discover the intersection of design, technology, and storytelling as I showcase my expertise in web development, graphic design, and digital marketing. Join me on this immersive digital experience as we connect, inspire, and make an impact in the ever-evolving online world. Let's embark on a journey of exploration, innovation, and endless possibilities together.

---
## [Reco201/tgstation](https://github.com/Reco201/tgstation)@[835952ccf4...](https://github.com/Reco201/tgstation/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Sunday 2023-06-25 15:59:09 by MrMelbert

Drunk slurring scales based on how drunk you are (#75459)

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

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[a0064712f7...](https://github.com/yarnpkg/berry/commit/a0064712f7b0ae38c21fb204bea9831c2b269bd7)
#### Sunday 2023-06-25 16:36:07 by Maël Nison

Bumps Node requirements from 14 to 18 (#5445)

**What's the problem this PR addresses?**

We're still supporting Node 14, but it has reached end of life. Node 16
is still maintained, but will reach an early end of life in October, so
I think it's reasonable to drop it now rather than publish a major
release just for that.

**How did you fix it?**

Bumps the requirements from `14.16` to `18.12` (first LTS from the 18.x
release line).

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

---------

Co-authored-by: Kristoffer K <merceyz@users.noreply.github.com>

---
## [nymda/retroGameEngine](https://github.com/nymda/retroGameEngine)@[ebea23230a...](https://github.com/nymda/retroGameEngine/commit/ebea23230a6e9cc668f8be2834ae9df276802888)
#### Sunday 2023-06-25 16:56:03 by J

i fucking hate maths so god damn much
(testing with sprites)

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[1468797059...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/146879705978b0416739823fa54467e865c3ffb2)
#### Sunday 2023-06-25 17:54:51 by TheObserver-sys

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
## [BrodyMoorman/2-3-4Tree](https://github.com/BrodyMoorman/2-3-4Tree)@[30c6928b83...](https://github.com/BrodyMoorman/2-3-4Tree/commit/30c6928b8355d978b9ed714606bacca11e98d069)
#### Sunday 2023-06-25 19:20:10 by BrodyMoorman

Added to delete functionality

Wrote method to fuse root in case of two node and two node children. Began writing method to fuse other two nodes, however the boilerplate holds ints not Integers, so I cant hold references to keep code concise. So I have to come up with a solution which will surely be very ugly. Java kinda sucks right now :(

---
## [noyalreji/The-Gaming-Room](https://github.com/noyalreji/The-Gaming-Room)@[2070531fe5...](https://github.com/noyalreji/The-Gaming-Room/commit/2070531fe5cff07b4c046842815516da06822331)
#### Sunday 2023-06-25 20:11:16 by Noyal Reji Jacob

Add files via upload

The Gaming Room Software Design Documentation

Summary:
The client for this project was The Gaming Room, a gaming center looking to develop custom software for their operations. The software requirements included features for player management, game management, team management, concurrent request handling, player login, security measures, and integration with the existing Android app.

Strengths in Developing the Documentation:
One of the strengths in developing this documentation was effectively capturing and organizing the client's requirements. The document provided a clear overview of the software design, outlining the various functionalities and how they would be implemented. The use of diagrams and visual aids helped convey complex concepts in a concise and understandable manner.

Benefits of Working through the Design Document:
Working through the design document allowed for a systematic approach to software development. It helped identify potential challenges, dependencies, and architectural considerations before starting the coding process. By thoroughly documenting the design, it became easier to communicate and align with both the client and the development team.

Area for Revision and Improvement:
If I could revise one part of my work on these documents, I would focus on providing more detailed explanations of the security measures implemented. While the document mentioned security considerations, it could be improved by specifying the specific technologies, protocols, or algorithms used to ensure a robust and secure system. This would enhance the clarity and instill more confidence in the security aspect of the software design.

Interpreting User Needs and Considering User-Centric Design:
Understanding and implementing the user's needs was crucial in designing the software. By engaging in thorough discussions with the client and conducting user research, we gained insights into their pain points, preferences, and desired functionalities. This information was then translated into the software design to ensure a user-friendly and intuitive experience. Considering the user's needs is essential as it directly impacts user satisfaction, adoption, and overall success of the software application.

Approach to Designing Software and Future Strategies:
In designing the software, a combination of techniques and strategies were employed. This included conducting requirements gathering sessions, creating use case scenarios, developing flowcharts and sequence diagrams, and evaluating different architectural patterns. In the future, I would continue to employ these strategies and also consider additional methods such as prototyping and user testing to further validate and refine the software design. Regular communication and collaboration with the client and development team would remain paramount to ensuring alignment and successful implementation.

---
## [tlindner/mame](https://github.com/tlindner/mame)@[2222a0f098...](https://github.com/tlindner/mame/commit/2222a0f098c2f32ec6090627598a90e596006596)
#### Sunday 2023-06-25 20:52:01 by David 'Foxhack' Silva

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
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[ce0ea0bd98...](https://github.com/wrye-bash/wrye-bash/commit/ce0ea0bd98b59a3b55e2766b53be5355b09cfd8d)
#### Sunday 2023-06-25 21:17:10 by MrD

Squash of ut-336-219-353 with fixups and drop pending_size II:

Nit and small fixes/opts: TTT

In `ext in bush.game.espm_extensions` ext used to be cs - it's not
anymore so this is a fixup. I ended up using EAFP here, hence dropping
the top_level_espm check - should be as fast as before and it's simpler.
Took the opportunity to prune an especially nasty use of getGhosted - a
few str operations should be faster than listing. Note that when
calling process_data_dir from update_data_SizeCrcDate getGhosted()
would be called twice.

__init__.py 4271 RefreshData boot:
d1ad84: 14636191 function calls (14609410 primitive calls) in 13.283 seconds
this  : 13706608 function calls (13679827 primitive calls) in 12.229 seconds

__init__.py 4271 RefreshData tab in:
d1ad84: 284138 function calls (275354 primitive calls) in 0.737 seconds
this  : 283127 function calls (274343 primitive calls) in 0.689 seconds

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

Rename Installer.modified attribute to align with AFile: RRR

Align with AFile

Would be nice to use the rest of the AFile API here (do_update and co -
hard! - edit: done in this merge :). Note I dropped the rpFile =
os.path.join(rsDir, sFile) - chopping asFile[relPos:] should be enough
(and faster).

__init__.py 4271 RefreshData boot:
Nit and small fixes/opts: 13706608 function calls (13679827 primitive calls) in 12.229 seconds
this  :                   13379068 function calls (13352287 primitive calls) in 11.719 seconds

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

Installer.do_update: TTT RRR

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

Progress does not work correctly (never gives focus back to Bash) XXX???

@@ -3460,5 +3460,5 @@ def ShowPanel(self, canCancel=True, fullRefresh=False, scan_data_dir=False,
                 if not do_refresh:
-                    with balt.Progress(_('Scanning Packages...')) as progress:
-                        refresh_info = self.listData.scan_installers_dir(
-                            folders, files, fullRefresh, progress)
+                    #with balt.Progress(_('Scanning Packages...')) as progress:
+                    refresh_info = self.listData.scan_installers_dir(
+                        folders, files, fullRefresh, progress=bolt.Progress())
                     do_refresh = refresh_info.refresh_needed()

__init__.py 4271 RefreshData boot:
d1ad84: 14636191 function calls (14609410 primitive calls) in 13.283 seconds
Nit and small fixes/opts: 13706608 function calls (13679827 primitive calls) in 12.229 seconds
Rename Installer.modified attribute: 13379068 function calls (13352287 primitive calls) in 11.719 seconds
Installer.do_update               :  13179201 function calls (13152382 primitive calls) in 12.129 seconds

__init__.py 4271 RefreshData tab in:
d1ad84: 284138 function calls (275354 primitive calls) in 0.737 seconds
Nit and small fixes/opts: 283127 function calls (274343 primitive calls) in 0.689 seconds
Rename Installer.modified attribute  : 283719 function calls (274935 primitive calls) in 0.697 seconds
Installer.do_update               :    496795 function calls (487975 primitive calls) in 0.580 seconds

FFF inline _refreshInstallers: EEE better comments

Seems now refresh_info and pending/deleted are orthogonal - needs
further simplification. We need to pass pending/deleted to
scan_installers_dir actually and use that instead of listing - edit:
done.

__init__.py 4271 RefreshData boot:
d1ad84: 14636191 function calls (14609410 primitive calls) in 13.283 seconds
Nit and small fixes/opts: 13706608 function calls (13679827 primitive calls) in 12.229 seconds
Rename Installer.modified attribute: 13379068 function calls (13352287 primitive calls) in 11.719 seconds
FFF inline _refreshInstallers:       13179209 function calls (13152391 primitive calls) in 11.780 seconds

__init__.py 4271 RefreshData tab in:
d1ad84: 284138 function calls (275354 primitive calls) in 0.737 seconds
Nit and small fixes/opts: 283127 function calls (274343 primitive calls) in 0.689 seconds
Rename Installer.modified attribute  : 283719 function calls (274935 primitive calls) in 0.697 seconds
FFF inline _refreshInstallers        : 496785 function calls (487966 primitive calls) in 0.618 seconds

refreshBasic -> _reset_cache EEE do_refresh=True flip default

Installer.refresh_installer -> InstellersData.new_info: TTT

setattr(clone, att, copy.copy(getattr(src_inst, att))) should work on LDs TTT

EEE Mopy/bash/basher/dialogs.py InstallerProject import remove.

Another hacky refactoring helper gone but there is more. When we were
unpickling on InstallersData.__load > __setstate we were calling at least
refreshDataSizeCrc but then we would perform a system call on abs_path -
now this is replaced with a necessary stat_tuple() call and
scan_installers_dir learned to skip freshly unpickled installers. We also
hook in AFile.__init__ - this drops abs_path from Installer (if we were
accessing this on markers that'a bug) by adding a new 'volatile' attribute
to _InstallerPackage (AFile's _file_key - now we can't slot we should
revisit all this along with pickling - we should stop pickling non std
classes). __init__ calls _reset_cache, so no need to call needs update
from new_info. One other (and hopefully the last) installer creation
site was __copy__ - that's too much magic, absorbed by new_info and the
bits of (arcane) logic were copied to copy_installer which should be
the only place we copy an installer. Finally I had to exclude fn_key
from persistent - this is set alright by __init__, the latter one being
called on unpickling as specified in __reduce__. So on unpickling
initDefault was called twice - maybe make Installer a dataclass and bin
initDefault?

SSS add_marker -> new_info

Use scandir instead of walk for InstallerProject._stat_tuple: RRR

I was aware there was maybe a way using scandir of not repeating some
stat calls while scanning a directory - all I could find was this:

https://discuss.python.org/t/get-direntry-objects-collected-during-os-walk/8143/5

I wondered if it performed better than walk:

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
        root_len = len(apath) + 1
    folders_times = [os.path.getmtime(apath)] if folders_times is None \
	    else folders_times
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

sc = _scandir_walk(d)
wal = _walk(d)
assert sc[0] == wal[0]
assert set(sc[1]) == set(wal[1])
assert max(sc[1]) == max(wal[1])

C:\Users\MrD\AppData\Local\Programs\Python\Python311\python.exe C:\Dropbox\eclipse_workspaces\python\py_scratch\timings.py
scandir 1.3165479998569936
walk 28.77752220002003

21 times faster! Projects refresh is the bottleneck in BAIN refresh,
hence all the skipRefresh/autoRefreshProjects/projectRefreshed. This
is happily solving this for most installs (don't know if this can
be made faster or switching to event based refreshes RRR is the only real
solution, in which case we still want all the speed we can get scanning
anyway, for the initial scan on booting BAIN, but also for manual
refreshes that might be needed in edge cases).

Absorb _process_data_dir and use scandir:

Time immemorial ago (b17601ef5bc25101c1fc12141f252ea250d49424) was
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

Empties handling: SSS TTT

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
guaranties anyway :Plus we won't really miss anything - if the operation
fails we just leave behind less empty dirs.

Kept error handling the same as before - although all the dirs should
exist in the `raise_error=False` case in _walk_data_dir.

SSS TTT Drop pending_size handling

Let's go nuclear on this. I *think* the problem might actually be some
kind of overflow in native Windows/wxWidgets code with a large enough
Data folder and enough large files in it that need to be updated.

This may actually speed up a Full Refresh. For a large file (e.g.
Fallout4 - Textures1.ba2 at 2.5G) we would issue thousands of progress
calls (1290 for that BA2, to be exact), which definitely isn't ideal in
the middle of a CRC calculation.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[a112679a7d...](https://github.com/wrye-bash/wrye-bash/commit/a112679a7d72bc393ccf830a76b2916e576b8888)
#### Sunday 2023-06-25 21:17:10 by Infernio

Rework temporary file handling RRR TTT

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

Co-authored-by: lojack5 <1458329+lojack5@users.noreply.github.com>

---
## [mocaffy/vim-tpipeline](https://github.com/mocaffy/vim-tpipeline)@[95a6ccbe9f...](https://github.com/mocaffy/vim-tpipeline/commit/95a6ccbe9f33bc42dd4cee45731d8bc3fbcd92d1)
#### Sunday 2023-06-25 22:14:54 by Magnus Groß

Another workaround for the utterly broken gui detection in nvim

Of course GUI detection wasn't fucked up enough in neovim already (see
c2603e4ad5c2a3011cffc9ea58d2b5036717067e for the last rant about this
topic). Instead of requiring special handling just for neovim, we now
also need special treatment just for neovim 0.9, because of course they
don't adhere to their own documentation anymore and v:event['chan'] may
now also return 1, as a sideeffect of running the internal TUI in a
separate process [0].

So to this day there is still no sane way to detect TUI in neovim,
instead we have to add a hacky workaround to check nvim_list_uis() for
ext_termcolors, which I am 100% confident will break in the future too.

Vim had sane API for this since forever and it is as simple as checking
for has('gui_running') at any point of time, but of course neovim can't
have this set at startup because we have to make everything convoluted
as fuck by sourcing plugins before the UI has a chance to attach.

Why the UI is not allowed to set a flag as the very first thing in the
startup sequence (and then attach later), is beyond stupid.

This is also not the first time that neovim's weird startup sequence
causes problems [1].

Fixes #46

[0] https://github.com/neovim/neovim/pull/18375
[1] https://github.com/neovim/neovim/issues/19362

---

