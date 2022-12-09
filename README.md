## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-08](docs/good-messages/2022/2022-12-08.md)


2,107,039 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,107,039 were push events containing 3,176,559 commit messages that amount to 261,591,317 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [BurnoutDV/YoutubeVideoTexts](https://github.com/BurnoutDV/YoutubeVideoTexts)@[c1e263c0f5...](https://github.com/BurnoutDV/YoutubeVideoTexts/commit/c1e263c0f5987c4f62d7b75757f51999b8ec281f)
#### Thursday 2022-12-08 00:04:44 by BurnoutDV

08.12.2022 *Midnight Writing*
i wonder if, when i actually would invest the time, could i become a somewhat prolific author? Right now i a feel like the meat version of ChatGPT, i write short blurbs for my youtube videos, if i could train a neural network to summarize the content i would be totally of the job. But for now, this is written by hand and with some love, srsly.

ah, i am still missing the 12 ankh episodes but i will get to them, soon, after i have 'drawn' that thumbnail and remembered what it all was about.

* Yakuza 5 - finally up to date, Episodes 61 to 70 written
* Elden Ring - todays episode, 170
* Elex 2, Episode 8

---
## [DataDog/dd-trace-rb](https://github.com/DataDog/dd-trace-rb)@[e65a90939e...](https://github.com/DataDog/dd-trace-rb/commit/e65a90939e5d255dfea8e64a7ab38d81f75c0ab4)
#### Thursday 2022-12-08 00:18:31 by Ivo Anjo

[PROF-6556] Leave SIGPROF signal handler after disabling profiling

**What does this PR do?**:

This PR changes the teardown behavior of the `CpuAndWallTimeWorker`
collector to NOT remove its SIGPROF signal handler, and instead
leave behind an empty one.

**Motivation**:

While doing other experiments with signal handling, I discovered that
if the Ruby VM receives a SIGPROF signal without having a signal handler
setup, it defaults to the awful UNIX/POSIX behavior of instantly dieing
with a confusing "Profiling timer expired" message (that has nothing to
do with our profiler).

I reasoned that because signal handling is asynchronous, the following
theoretical situation may happen:
1. `CpuAndWallTimeWorker` sends SIGPROF signal
2. `CpuAndWallTimeWorker` notices request to shut down
3. `CpuAndWallTimeWorker` removes SIGPROF signal handler during teardown
4. Process receives SIGPROF, causing it to die.

I strongly suspect this may never happen in practice, but as
documented in the comment I added, the cost of my suspicion being
wrong is really high, so just-in-case I decided to instead leave
behind an empty signal handler.

**How to test the change?**:

Change includes test coverage. Additionally, you can doublecheck
the change in behavior by doing something like:

```
$ DD_TRACE_DEBUG=true DD_PROFILING_ENABLED=true DD_PROFILING_FORCE_ENABLE_NEW=true bundle exec ddtracerb exec pry
D, [2022-11-23T09:31:54.278186 #22975] DEBUG -- ddtrace: [ddtrace] (components.rb:384:in `startup!') Profiling started
[1] pry(main)> Datadog.configure { |c| c.profiling.enabled = false };;
D, [2022-11-23T09:32:08.580276 #22975] DEBUG -- ddtrace: [ddtrace] (profiler.rb:29:in `shutdown!') Shutting down profiler
[3] pry(main)> Process.kill("SIGPROF", Process.pid)
```

and you'll see that the Ruby process stays alive. If you do the
same thing to a process with no profiler, you'll see the process die
when you send it the SIGPROF signal.

---
## [boost-entropy-typescript/apollo-server](https://github.com/boost-entropy-typescript/apollo-server)@[3fd7b5f261...](https://github.com/boost-entropy-typescript/apollo-server/commit/3fd7b5f26144a02e711037b7058a8471e9648bc8)
#### Thursday 2022-12-08 01:51:30 by Trevor Scheer

Update `@apollo/utils.keyvaluecache` dependency (#7187)

Previous releases of the `@apollo/utils.keyvaluecache` package
improperly specified the version range for its `lru-cache` dependency.

Fresh installs of our packages should receive the patch update since
it's careted, so this issue can be worked around by forcing the update
if you're using a lockfile. We should update it anyway since `2.0.0` is
invalid.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [Shadow-Quill/Occulus-Eris](https://github.com/Shadow-Quill/Occulus-Eris)@[866a77c18d...](https://github.com/Shadow-Quill/Occulus-Eris/commit/866a77c18de6544a98b47778850864e6428be175)
#### Thursday 2022-12-08 02:10:41 by MLGTASTICa

Redoes lense code , Thermal lenses no longer provide night vision. (#6607)

* initial fuckeryh

* horrible deeds

* removes explosive lenses and fix grammar

* Update stealthy and inconspicuous weapons.dm

Co-authored-by: MLGTASTICa <ak9bc01d@yahoo.com>

---
## [AntonLTG/bolibompacs](https://github.com/AntonLTG/bolibompacs)@[a5b382f067...](https://github.com/AntonLTG/bolibompacs/commit/a5b382f067eadcf21a735cabab0e07a8e92316d7)
#### Thursday 2022-12-08 02:20:32 by JesusHolyBalls

!important; Yeeeah jump function and advanced movement, gravity is screwed for character

.grounded is bs, need so much information and the troubleshooting is insanly annoying.

1. need to have the character dimmensions, to use raycasts.(raycats gives a true or false value after detecting if an object is a certain distance from a certain point.) Done

2.right now falling at constant speed which needs to be fixed, it is possible to kinda bhop tho. NOT DONE

3.To fix speed we need to calculate theoretical max speed and replace current speed with "max speed" Done

4. Apperantly fbx files is packed so needed to unpack to make the eyes and ears move with the head and then repack it. Done

5.At this time we cant walk upwards on smal height differences, just end up launching the character upwards (the more speed the higher). NEED HOTFIX

6. To import scripts and characters is a hell, you need to rebind all scripts to (in our case) the different body parts to make them move, I should've named the bone structure parts better for easier navigation and easier distrubution, will be hard for others collaborators to understand.

took about 5 hours to rewrite the movement script and add a working jump function with a "check if grounded"

total programming time is about 8hours now and another 20 hours 3D moddeling (includes getting familiar with the programs).

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[00d3780c38...](https://github.com/carlarctg/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Thursday 2022-12-08 02:30:58 by carlarctg

PDT/L Buff (#1757)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

PDT/L kits now fold into cardboard.

Added many spare PDT/L kits and batteries to req. (Marines dropped them
off at req once they realized they were shitty milsurp knockoffs)

Made minibatteries tiny.

Added boldwarning span macro.

Improved locator tube sprites: Now has a pop-out battery slot at the top
that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.

Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Fixed a bug in which a string referenced a null var.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

When I saw the PDT/L kit, I was very interested. It seemed like a great
way to encourage teamwork and buddying up with some fun lore flavor on
the side. However, trying it out, it really feels bare-bones. I get it's
supposed to be 'crappy' because Boots magazine subscriber items suck and
so do the lives of every private on the corps, but the way that's
implemented really ruins the extremely cool concept that is being able
to locate your fellow buddies across the battlefield, so you don't need
to continually say HEY WHERE ARE YOU over comms in the many times you'll
get split up.

Thus I've heavily buffed them around the board, which you may think is
going way too far, and to an extent, you're _right._ It's intentional.
This is a really cool item that actively encourages teamwork and that's
why I would rather swing the buff hammer too hard than give it a paltry
buff and some qol that ultimately nobody cares about. It's the same as
the spotter kit. It's nuts, but needs teamwork to actually be useful.
And this should be encouraged.

If it is still deemed too strong, there are things we can do to
laterally nerf it without closing the PR outright. Making the tube not
work if the bracelet holder's dead, having it needs comms to work come
to mind, but there are surely others.

> Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

The intention here is to let marines actually resupply their kits once
they run dry, and if they're proactive, maybe grab some and bring them
to FOB with them. Despite the description, the cells cannot easily be
recharged as power cell chargers are different from rechargers, they are
effectively Bay12 legacy that is VERY hard to come across.

'What if someone carries like 5 of them in their bag? That'd completely
nullify the power drain part.'

The stinger here is 'in the bag'. There are not enough reasons to carry
bags and satchels in this game right now as the sheer amount of storage
for goods marines have make them a one-man-army with two primaries. If a
marine forgoes a shotgun that might save them from a 1-pounce capping
runner for 5 spare LT batteries, a default medkit, and two flare boxes,
they are well within their rights to do so.

> Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)

This lets req drop them off at FOB if they eventually figure out they
can drop unvended surplus there. If this somehow happens, marines who
never even glanced at the kit in loadout or prep will notice it exists
and maybe, just maybe, use them!

> Made minibatteries tiny.

You may think this contradicts my earlier point about sacrificing
storage value, but _actually_ think about it. All webbing types, armor
slots, pouches, belts, even the helmet, all share the common attribute
of not caring about item size. If it's small or medum it still takes 1
out of the 3 slots in medium armor. Any storage item that isn't a
satchel, effectively. Every spare battery taken directly in the average
marine's inventory is one slot less for 5 shotgun shells, one magazine,
one unga juice flask, binoculars. What this means in the end is simply
that marines may carry one to two spare batteries in their helmet (I
think) at the cost of Drip which few marines will trade for, and satchel
marines don't have to sacrifice a lot of space for the spare battery.
Plus, it makes sense, why wouldn't a small AA rechargeable battery be
tiny.

> Improved locator tube sprites: Now has a pop-out battery slot at the
top that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

This looks so sick!

> Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Adding sounds to items should be standarized, I think. There are so many
cool sounds in the sound/machines folder that go unused. Personally i
felt like these small stupid sounds added a LOT to the atmosphere of
this tiny locator tube and bracelet. Alien Isolation is known for its
sounds, we should strive to emulate that.

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

:cl:
add: Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.
qol: PDT/L kits now fold into cardboard.
add: Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)
balance: Made minibatteries tiny.
refactor: Added boldwarning span macro.
imageadd: Improved locator tube sprites: Now has a pop-out battery slot
at the top that shows up if emptied. The main green stripe is now a
battery indicator with appropiately-faded-out yellow warning and
blinking red danger sprites. The small notch at the bottom is now a
bracelet indicator that turns off without a battery and blinks red if
the bracelet was somehow destroyed.
qol: The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.
soundadd: Added a ton of sounds to interactions with the PDT/L kit.
Beeps on scanning, buzzes on errors, clicks on handling.
fix: Fixed a bug in which a string referenced a null var.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[ce39f048bf...](https://github.com/carlarctg/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Thursday 2022-12-08 02:30:58 by carlarctg

Buffed, resprited, enhanced Oppressor. (#1732)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

**Resprited Oppressor! Pics here:**


![image](https://user-images.githubusercontent.com/53100513/204121775-9f4acd11-d818-46e8-81d3-c38bdfdabf5c.png)

Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Oppressor can hook over the M2C and M56D again.

Oppressor can hook over ledges. (UNIMPLEMENTED)

Tail stab's main ability usage is moved to a different proc for future
custom tail stabs.

Redesigned Tail Stab for Oppressor. Tail seize now utilizes a projectile
and beams to fire a 3-tile reaching tail hook, that pulls in AND DOES
NOT STUN marines. (It slows them for 0.5 seconds)

![Screenshot_20221127-032533~2](https://user-images.githubusercontent.com/53100513/204122365-e1ee57f7-1b9d-443e-a45c-dceec07a88d3.png)

Oppressor's abduct has had its effect strings changed to imply coiling
and uncoiling of the tail. Captured targets will now have a beam of the
Oppressor's tail attached to them (Purely visual) until they reach the
Praetorian, alongside an overlay of the vice grip on their legs.

Added a proc, .ammo/on_bullet_generation(), for the ammo datum to apply
effects to the generated bullet/projectile.

Added the bound_beam variable to projectiles. Could be used in the
future for things like harpoon guns, lasers, etc.

Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

Videos tomorrow.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Animated telegraphs looked really cool, but (I presume) were removed
because BYOND sometimes freezes or starts animations midway through when
short lived animated objects show up, for some reason. I effectively
made it so these are irrelevant by slapping on the border - The animated
effects are just a bonus and will not impact visibility, and in fact
enhance it.

> Oppressor can hook over the M2C and M56D again.

Everyone I've talked to agrees that there really is no reason for these
weapons to protect from abduction. The player can just.. move out of the
way, or even rest if they're in a crowded spot. It's also very
frustrating to see it get in the way of *other* abducts that bonk into
it. The player is going immobile in range of a xenomorph that punishes
immobility.

> Oppressor can hook over ledges. (UNIMPLEMENTED)

Couldn't replicate this issue for some reason... So uh. I dunno.

> Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)

Geeves approved.

This looks so fucking awesome. The slow is barely a thing, so I wouldn't
fret about slow creep. The reaching hook does no damage, only pulls
targets closer. This isn't necessarily super strong, but it's mega cool
and fits with Oppressor's theme of dislocation. I also changed the
windup from 1s to 0.5s so it can be utilized during combat, but this
could be reverted if it's too strong somehow.

> Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

This looked stinky on the tail seize.

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

:cl: Carlarc, Mikola Wei

imageadd: Resprited Oppressor, sprites made by Mikola Wei.
imageadd: Re-added animated telegraphs for Abduction. They've been
tweaked to always have the default border - that way, the weird way
byond handles short-lived animated objects doesn't make the telegraph
absurdly small. It can always be easily seen.
balance: Oppressor can hook over the M2C and M56D again.
refactor: Tail stab's main ability usage is moved to a different proc
for future custom tail stabs.
add: Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)
imageadd: Oppressor's abduct has had its effect strings changed to imply
coiling and uncoiling of the tail. Captured targets will now have a beam
of the Oppressor's tail attached to them (Purely visual) until they
reach the Praetorian, alongside an overlay of the vice grip on their
legs.
refactor: Added a proc, .ammo/on_bullet_generation(), for the ammo datum
to apply effects to the generated bullet/projectile.
refactor: Added the bound_beam variable to projectiles. Could be used in
the future for things like harpoon guns, lasers, etc.
fix: Fixed non-damaging projectiles causing a blood spurt. (It was
checking flags && FLAG instead of flag & flag, remember to use
CHECK_BITFIELD folks!)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

Co-authored-by: harryob <me@harryob.live>

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[c8f4d4ae04...](https://github.com/carlarctg/cmss13/commit/c8f4d4ae042be6fb59f29031eb0a56926e32ab3a)
#### Thursday 2022-12-08 02:30:58 by carlarctg

Money Rework (#1831)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Added a variable to paygrades called pay_multiplier. This multiplies the
starting amount of money from bank accounts.

Refactored how bank accounts are created so the above could work.

Drastically nuked the amount of money people start with. People can no
longer start with thousands of dollars.... they now get 30-50. This
value is multiplied by the pay_multiplier below.

Added pay_multiplier to all paygrades. The higher your rank, the more
money you'll start with, based on this multiplier. (For example, a Major
will have a pay multiplier of 4.) Includes strange roles like VAIPO,
UPP, PMCs, RESS...

Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.

Altered the prices of cigarette vending machines around to overall make
them more expensive. PFCs will not be able to buy Executive Select with
their starting cash.

Made cassetes and Souto from vendors more expensive. Buying food from
Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.

Fixed default parent type dollar items being worth 0 money...

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Drastically nuked the amount of money people start with. People can no
longer start with thousands of dollars.... they now get 30-50. This
value is multiplied by the pay_multiplier below.

Lore. The live of a private sucks. Monkeysfist suggested this value.
Still enough to buy all essentials, scavenge some money if you want to
buy the good cigarette packs down in the colony.

> Added pay_multiplier to all paygrades. The higher your rank, the more
money you'll start with, based on this multiplier. (For example, a Major
will have a pay multiplier of 4.) Includes strange roles like VAIPO,
UPP, PMCs, RESS...

Why were paygrades added without affecting pay. Why could PFCs start
with 3 thousand dollars and COs with 50 dollars total.

> Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.

Inclusivity win! Doesn't actually do anything as we do not have
nonbinary characters.

> Altered the prices of cigarette vending machines around to overall
make them more expensive. PFCs will not be able to buy Executive Select
with their starting cash.

> Made cassetes and Souto from vendors more expensive. Buying food from
Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.

It's funny to make the lives of marines miserable.

> Fixed default parent type dollar items being worth 0 money...

This will let marines money scrounge.

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

Irrelevant.

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
add: Added pay_multiplier to all paygrades. The higher your rank, the
more money you'll start with, based on this multiplier. (For example, a
Major will have a pay multiplier of 4.) Includes strange roles like
VAIPO, UPP, PMCs, RESS...
del: Drastically nuked the amount of money people start with. People can
no longer start with thousands of dollars.... they now get 30-50 dollars
total. This value is multiplied by the pay_multiplier above.
spellcheck: Non-binary WY executives may now spawn with 'Mx.' as their
communications prefix.
balance: Altered the prices of cigarette vending machines around to
overall make them more expensive. PFCs will not be able to buy Executive
Select with their starting cash.
del: Made cassetes and Souto from vendors more expensive. Buying food
from Hot Foods now costs money. Marine coffee now has an appropiate
description. Souto vendors no longer vend water bottles.
fix: Fixed default parent type dollar items being worth 0 money...
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [openeuler-mirror/raspberrypi-kernel](https://github.com/openeuler-mirror/raspberrypi-kernel)@[6a52b0f969...](https://github.com/openeuler-mirror/raspberrypi-kernel/commit/6a52b0f969d56f8071bd12734a91a64c8a617bb5)
#### Thursday 2022-12-08 02:47:57 by Dave Chinner

xfs: reduce kvmalloc overhead for CIL shadow buffers

mainline inclusion
from mainline-v5.16-rc5
commit 8dc9384b7d75012856b02ff44c37566a55fc2abf
category: bugfix
bugzilla: 187526,https://gitee.com/openeuler/kernel/issues/I4KIAO

Reference: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8dc9384b7d75012856b02ff44c37566a55fc2abf

--------------------------------

Oh, let me count the ways that the kvmalloc API sucks dog eggs.

The problem is when we are logging lots of large objects, we hit
kvmalloc really damn hard with costly order allocations, and
behaviour utterly sucks:

     - 49.73% xlog_cil_commit
	 - 31.62% kvmalloc_node
	    - 29.96% __kmalloc_node
	       - 29.38% kmalloc_large_node
		  - 29.33% __alloc_pages
		     - 24.33% __alloc_pages_slowpath.constprop.0
			- 18.35% __alloc_pages_direct_compact
			   - 17.39% try_to_compact_pages
			      - compact_zone_order
				 - 15.26% compact_zone
				      5.29% __pageblock_pfn_to_page
				      3.71% PageHuge
				    - 1.44% isolate_migratepages_block
					 0.71% set_pfnblock_flags_mask
				   1.11% get_pfnblock_flags_mask
			   - 0.81% get_page_from_freelist
			      - 0.59% _raw_spin_lock_irqsave
				 - do_raw_spin_lock
				      __pv_queued_spin_lock_slowpath
			- 3.24% try_to_free_pages
			   - 3.14% shrink_node
			      - 2.94% shrink_slab.constprop.0
				 - 0.89% super_cache_count
				    - 0.66% xfs_fs_nr_cached_objects
				       - 0.65% xfs_reclaim_inodes_count
					    0.55% xfs_perag_get_tag
				   0.58% kfree_rcu_shrink_count
			- 2.09% get_page_from_freelist
			   - 1.03% _raw_spin_lock_irqsave
			      - do_raw_spin_lock
				   __pv_queued_spin_lock_slowpath
		     - 4.88% get_page_from_freelist
			- 3.66% _raw_spin_lock_irqsave
			   - do_raw_spin_lock
				__pv_queued_spin_lock_slowpath
	    - 1.63% __vmalloc_node
	       - __vmalloc_node_range
		  - 1.10% __alloc_pages_bulk
		     - 0.93% __alloc_pages
			- 0.92% get_page_from_freelist
			   - 0.89% rmqueue_bulk
			      - 0.69% _raw_spin_lock
				 - do_raw_spin_lock
				      __pv_queued_spin_lock_slowpath
	   13.73% memcpy_erms
	 - 2.22% kvfree

On this workload, that's almost a dozen CPUs all trying to compact
and reclaim memory inside kvmalloc_node at the same time. Yet it is
regularly falling back to vmalloc despite all that compaction, page
and shrinker reclaim that direct reclaim is doing. Copying all the
metadata is taking far less CPU time than allocating the storage!

Direct reclaim should be considered extremely harmful.

This is a high frequency, high throughput, CPU usage and latency
sensitive allocation. We've got memory there, and we're using
kvmalloc to allow memory allocation to avoid doing lots of work to
try to do contiguous allocations.

Except it still does *lots of costly work* that is unnecessary.

Worse: the only way to avoid the slowpath page allocation trying to
do compaction on costly allocations is to turn off direct reclaim
(i.e. remove __GFP_RECLAIM_DIRECT from the gfp flags).

Unfortunately, the stupid kvmalloc API then says "oh, this isn't a
GFP_KERNEL allocation context, so you only get kmalloc!". This
cuts off the vmalloc fallback, and this leads to almost instant OOM
problems which ends up in filesystems deadlocks, shutdowns and/or
kernel crashes.

I want some basic kvmalloc behaviour:

- kmalloc for a contiguous range with fail fast semantics - no
  compaction direct reclaim if the allocation enters the slow path.
- run normal vmalloc (i.e. GFP_KERNEL) if kmalloc fails

The really, really stupid part about this is these kvmalloc() calls
are run under memalloc_nofs task context, so all the allocations are
always reduced to GFP_NOFS regardless of the fact that kvmalloc
requires GFP_KERNEL to be passed in. IOWs, we're already telling
kvmalloc to behave differently to the gfp flags we pass in, but it
still won't allow vmalloc to be run with anything other than
GFP_KERNEL.

So, this patch open codes the kvmalloc() in the commit path to have
the above described behaviour. The result is we more than halve the
CPU time spend doing kvmalloc() in this path and transaction commits
with 64kB objects in them more than doubles. i.e. we get ~5x
reduction in CPU usage per costly-sized kvmalloc() invocation and
the profile looks like this:

  - 37.60% xlog_cil_commit
	16.01% memcpy_erms
      - 8.45% __kmalloc
	 - 8.04% kmalloc_order_trace
	    - 8.03% kmalloc_order
	       - 7.93% alloc_pages
		  - 7.90% __alloc_pages
		     - 4.05% __alloc_pages_slowpath.constprop.0
			- 2.18% get_page_from_freelist
			- 1.77% wake_all_kswapds
....
				    - __wake_up_common_lock
				       - 0.94% _raw_spin_lock_irqsave
		     - 3.72% get_page_from_freelist
			- 2.43% _raw_spin_lock_irqsave
      - 5.72% vmalloc
	 - 5.72% __vmalloc_node_range
	    - 4.81% __get_vm_area_node.constprop.0
	       - 3.26% alloc_vmap_area
		  - 2.52% _raw_spin_lock
	       - 1.46% _raw_spin_lock
	      0.56% __alloc_pages_bulk
      - 4.66% kvfree
	 - 3.25% vfree
	    - __vfree
	       - 3.23% __vunmap
		  - 1.95% remove_vm_area
		     - 1.06% free_vmap_area_noflush
			- 0.82% _raw_spin_lock
		     - 0.68% _raw_spin_lock
		  - 0.92% _raw_spin_lock
	 - 1.40% kfree
	    - 1.36% __free_pages
	       - 1.35% __free_pages_ok
		  - 1.02% _raw_spin_lock_irqsave

It's worth noting that over 50% of the CPU time spent allocating
these shadow buffers is now spent on spinlocks. So the shadow buffer
allocation overhead is greatly reduced by getting rid of direct
reclaim from kmalloc, and could probably be made even less costly if
vmalloc() didn't use global spinlocks to protect it's structures.

Signed-off-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Allison Henderson <allison.henderson@oracle.com>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Guo Xuenan <guoxuenan@huawei.com>
Reviewed-by: Zhang Yi <yi.zhang@huawei.com>
Signed-off-by: Zheng Zengkai <zhengzengkai@huawei.com>

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[38daf19f12...](https://github.com/Offroaders123/NBTify/commit/38daf19f122efa144212e572cf26f7973e13e8ab)
#### Thursday 2022-12-08 02:55:17 by Offroaders123

4matting + Export Ideas

Re-renamed the IO class options object interface type. I think I like it more that it be the same name as the class, and I want the class to be called `NBTReader` and `NBTWriter`, since having no prefix on those doesn't really make sense if imported outside of a namespace (`import * as NBT` vs `import { NBTReader, NBTWriter }`). But I also like having `NBT.read()` and `NBT.write()`, so I may not be quite decided on whether the module should be imported as a namespace, vs optional imports. I don't really like `readNBT()` and `writeNBT()`, I think..? Also not sure. They sound kind of odd. I guess my thinking is that you'd use the top-level functions like you would `JSON.parse()` and `JSON.stringify()`, and maybe that you'd specifically want to import the IO classes if you're going to be doing something custom. And I think it makes sense for those to have a prefixed name, because of that. Just being `Reader` or `Writer` sounds a bit to unspecific. I'll probably go with something like this eventually:
```ts
// index.ts
export * from "all-the-files-from-nbtify";

import { read, write } from "./index.js"; // This file

export default { read, write };

// example.js
import NBT, { Byte, Short, Int, Float, NBTData, NBTReader, NBTWriter } from "nbtify";

await NBT.read(/* Data */);
await NBT.write(/* CompoundTag */);
```

You'd get a simple API surface, and it would work like the JSON namespace, with only necessary things in there. Then if you needed more things, you can import them by name. I don't know yet, hehe. Gonna have to try a few different things!

Looked into my source code for Menu Drop, and remembered my new organization style, of adding implementation features down the file as they get more primitive/elemental? So your top-level code is shown first, then your code that follows is code that explains how that code works, with more detailed implementation info. And, then onwards. This includes properties like getters and setters, which are after functions. Not sure if this method has any gravity, but I'm gonna try it and see how it is.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[e9cff525dc...](https://github.com/timothymtorres/tgstation/commit/e9cff525dc5b57153af3b4bb9039de08d6823805)
#### Thursday 2022-12-08 03:24:32 by tralezab

Refactors Pirates into Pirate Gangs, Adds the Psyker-gang as new pirates (#71650)

## About The Pull Request

### Refactor
Pirate gangs are now datumized for extendability, custom dialogue, etc.

### Psyker Gang 🧠 
Psyker-gang Members are pirates who are... yes, Psykers. They're on a
gore-binge and need some money for more hits of gore!

- Gore autoinjectors, filled with dirty kronkaine. Don't overdose,
you'll go splat.
- Psykerboost armor, reactive armor that refreshes psychic abilities.
Given to the leader.

- [x] @Fikou is making the map :D

## Why It's Good For The Game

God I fucking love variety also now we can add as many different pirates
as we so desire

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/205342701-9cba63ef-a22c-4f07-9b48-8793c4a2b5af.png)
  
</details>

## Changelog
:cl: Tralezab code, Fikou's map, PigeonVerde and Halcyon for sprites!
add: Psyker-gangers are new pirates
refactor: refactored pirate code so we can add more in the future
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[a753229ee2...](https://github.com/timothymtorres/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Thursday 2022-12-08 03:26:56 by GoldenAlpharex

Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.


<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.


![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @MrMelbert about it and he gave me the go-ahead, as can be seen
here:


![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[35b5ac0c4e...](https://github.com/timothymtorres/tgstation/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Thursday 2022-12-08 03:26:56 by Fikou

Psykers (#71566)

## About The Pull Request
Finishes #66471
At burden level nine (or through a deadly genetic breakdown), you now
turn into a psyker.
This splits your skull in half and transforms it into a weird fleshy
mass. You become blind, but your skull is perfectly suited for sending
out psychic waves. You get potent psy abilities.
First one is brainwave echolocation, inspired by Gehennites (but not as
laggy).
Secondly, you get the ability of Psychic Walls, which act similarly to
wizard ones, but last shorter, and cause projectiles to ricochet off
them.
Thirdly, you get a projectile boost ability, this temporarily lets you
fire guns twice as fast and gives them homing to the target you clicked.
Lastly, you get the ability of psychic projection. This terrifies the
victim, fucking their screen up and causing them to rapidfire any gun
they have in their general direction (they'll probably miss you)
With most of the abilities being based around guns, a burden level nine
chaplain now gets a new rite, Transmogrify. This lets them turn their
null rod into a 5-shot 18 damage .77 revolver. The revolver possesses a
weaker version of antimagic (protects against mind and unholy spells,
but not wizard/cult ones). It is reloaded by a prayer action (can also
only be performed by a max burdened person).
General Video: https://streamable.com/w3kkrk
Psychic Projection Video: https://streamable.com/4ibu7o

![image](https://user-images.githubusercontent.com/23585223/204150279-a6cf8e2f-c678-476e-b72c-6088cd8b684b.png)

## Why It's Good For The Game
Rewards the burdened chaplain with some pretty cool stuff for going
through hell like losing half his limbs, cause the current psychics dont
cut it as much as probably necessary, adds echolocation which can be
used for neat stuff in the future (bat organs for DNA infuser for
example).

## Changelog
:cl: Fikou, sprites from Halcyon, some old code from Basilman and
Armhulen.
refactor: Honorbound and Burdened mutations are brain traumas now.
add: Psykers. Become a psyker through the path of the burdened, or a
genetic breakdown.
add: Echolocation Component.
/:cl:

Co-authored-by: tralezab <spamqetuo2@gmail.com>
Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[4d88f6e437...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/4d88f6e437ee794624e5d3b268a4bf37359832c7)
#### Thursday 2022-12-08 04:46:38 by SkyratBot

[MIRROR] Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. [MDB IGNORE] (#17893)

* Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

* Corrects error in stamina HUD element display calculation. Increases stamina HUD readability.

Co-authored-by: itseasytosee <55666666+itseasytosee@users.noreply.github.com>

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[4fd404aa8f...](https://github.com/itseasytosee/tgstation/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Thursday 2022-12-08 05:17:41 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[5da871e271...](https://github.com/itseasytosee/tgstation/commit/5da871e2719fb7aac04fb1ec4c85ea7a09a83b36)
#### Thursday 2022-12-08 05:17:41 by RikuTheKiller

Made geysers easier to find (#71608)

## About The Pull Request

This PR raises the geyser spawn rate from 0.1 to 0.15 and increases the
weight of wittel geysers to 10 which is the same as every other special
geyser. (previously 6)

Wittel shouldn't be any less difficult to find than other geysers as all
of the special geysers are equally powerful. Hyper-plasmium oxide can be
used to make extremely powerful explosives that can go beyond maxcaps
and hollow water + protozine can create an infinite amount of strange
reagent.

I've subjected myself to going out of my way to visit lavaland/icemoon
several times to get wittel and each time finding a single geyser takes
about 5 minutes of my time. This, coupled with the fact you really don't
have a lot of time to be wasting on looking for the geysers results in
an unfun experience.

I understand geysers are sort of a necessary evil, however, they
shouldn't be THIS difficult to find. Out of the 10 or so geysers I've
found, only 1 has had wittel in it and it was next to a whelp portal
which ended both me and my miner escort.

I've also hunted the entirety of lavaland with no luck. (Horrendous
experience.)

I've dedicated entire rounds to this, by the way.
## Why It's Good For The Game

If you go out of your way to waste ages hunting for geysers, there
should at least be a reward. That is, in the same round, not after 3 or
more rounds as even megafauna gear isn't gatekept THAT hard.

You shouldn't have to waste this much of a miner's time (who is also
going for megafauna gear) to get something that is arguably less
powerful than what they get for less effort. Megafauna gear is also
available every round and is attained via predictable methods.

This PR will also likely make geyser scanning a more comparable method
of point gain to just mining.

Oh and not to mention that penthrite is available almost roundstart via
luxpens. (It's a wittel chem.)
## Changelog
:cl:
balance: Geysers now spawn more often, especially wittel geysers.
/:cl:

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[2425531eb2...](https://github.com/itseasytosee/tgstation/commit/2425531eb2dab84fb27ed864e4c52470bfff6918)
#### Thursday 2022-12-08 05:17:41 by John Willard

Removes tablets (not PDAs) entirely. (#71507)

## About The Pull Request

**Comes with an UpdatePaths!**

Removes the tablet subtype, PDAs now replaces them entirely.

Nukie and Silicon tablets are now subtypes of the PDA instead, while
contractor ones were removed entirely as they didn't do anything and
were unused (though it wouldn't be hard to re-add).

Nukie PDAs are now the only type of PDA that uses modular_tablets.dmi,
which is just larger icons of modular_pda. Each application requires an
icon state in both of these, for 2 different sizes, which makes it
annoying to make new applications, especially if it can also run on
computers/laptops.

### Icons

Because Silicon tablets are now a subtype of PDA, they use PDA icons
instead of tablet ones. Luckily for us, they already exist in code.

![image](https://user-images.githubusercontent.com/53777086/203876575-56eb1593-774c-47c6-8e7d-491a7805f28c.png)

AI's don't use a tablet icon though, so they aren't affected.

## Why It's Good For The Game

There's very little difference between tablets and PDAs, PDAs overshadow
them in every single way, so at this point I don't see why we should
have both of these, and if you compare the two in usefulness and actual
in-game use by players, it's a no-brainer than the item all players get
roundstart and comes with a messenger should be the one we go with.

Also as said in the about section, when making an app you would need to
make icon states for the program running for all hardware it can run on,
which is Computer, Laptop, PDA, and Tablet.

Laptop is just a smaller computer icon
PDA is just a smaller tablet icon

However, you can't simply shrink the size of the icon, instead you have
to completely resprite the same app icon FOUR TIMES for it to not
bluescreen on all these different devices.

<details>
<summary>
Here's examples of it
</summary>
Computer (NOTE: *They share the same icon file as regular computers*)
<img
src="https://user-images.githubusercontent.com/53777086/203876801-486a8054-489a-4983-bdad-a2599b4dc379.png"/>
Laptop
<img
src="https://user-images.githubusercontent.com/53777086/203876333-58e5d135-f4c6-4a02-8948-1df771e294a4.png"/>
Tablet
<img
src="https://user-images.githubusercontent.com/53777086/203876352-816c7fb1-c681-40b9-99e0-052f49632c7f.png"/>
PDA
<img
src="https://user-images.githubusercontent.com/53777086/203876358-1cf7253d-3c6a-456a-8133-ebf7f0351637.png"/>
</details>

If we wish to help in simplifying this, we should remove tablet icons
entirely, which means 1 less icon to worry about. To do this, we'd need
to resprite nukie PDAs, however I am very much not a spriter and never
tried GAGS, so I'll leave it to someone else to do.

## Changelog

:cl:
del: Tablets are now removed, PDAs are now the base 'tablet'. Silicon
and nukie tablets are now PDAs.
/:cl:

---
## [AsurA0001/app-dev](https://github.com/AsurA0001/app-dev)@[2bf31ef7de...](https://github.com/AsurA0001/app-dev/commit/2bf31ef7dec45e3c63f874f45ca05eadb9d24afb)
#### Thursday 2022-12-08 05:28:15 by Liam

Update README.md

This list that I made is like a recommendation; it's a roller coaster ride of emotions. You'll feel Happy, Sad, and more. Just this movies and series will make  you understand what they always say "5 stages of Grief" in our life.

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[661eaa985e...](https://github.com/necromanceranne/tgstation/commit/661eaa985e32056cc25f32bd81d9106861a4f9f8)
#### Thursday 2022-12-08 06:16:18 by MrMelbert

Important heretic spell rebalancing (#71620)

## About The Pull Request

Nerfs
- Furious steel cooldown: 30s -> 60 seconds (when ascended: 10s -> 30s)
- Furious steel: Now affected by antimagic
- Cleave cooldown: 40s -> 45s
- Cleave range: 9 tiles -> 4 tiles
- Cleave wound: Now has natural clotting, changing the amount of blood
loss from inf -> ~40%
- Blood siphon range: 9 tiles -> 6 tiles
- Void Pull: Now affected by antimagic
- Void Phase: Now affected by antimagic

Buffs
- Void Blast cooldown: 60s -> 30s

Other
- Rust Formation now has a "distinct" icon
- Void Blast now has a "distinct" icon

## Why It's Good For The Game

A lot of these spells were extremely oppressive, and made it pretty much
a joke to get away with anything.
They were no-brainer choices, and as a result no one really pathed into
anything else but these.

- Furious Steel: 
- Now that blade heretics have "realignment" in their repertoire, which
offers them another counter for being hit by disablers or batons, this
spell doesn't need to have such an insanely high uptime. The spell
should be used for initiating and obtaining the lead in a combat,
instead of having nigh-invulnerability for most periods.
- Additionally, antimagic protection was kind of missing, which was
partially an oversight of it not being a `/magic` projectile.
 
- Cleave:
- Cleave was by far the most absurd ability available bar none. This
spell was guaranteed death in 30 seconds if the target had no way to
stop the bloodflow immediately. AND it could be casted from across the
screen. This brings cleave's range into midrange between you and the
target, giving a lot more opportunity to be aware for the victim.
- Critical bleed wounds had a negative clotting rate, meaning that prior
you would bleed to 0% from cleave if you didn't stop it. Not very fun,
so with the default clotting rate it now stops at 60% blood flow -
enough to be lethal if untreated, but doesn't completely tap you out
   - **Alternatives**: 
      - Keep the no clotting, make it a pure melee / touch spell. 
      - Reduce the cooldown, make it a projectile
- Change it to be like a cool scythe attack that comes out of the caster
and does a sweep

- Blood Siphon: 
- This was primarily done to slot in better with Cleave's range
decrease, encouraging more close range combat between the two. Getting
point clicked from across the screen isn't fun.

- Void Pull and Phase:
- Largely done for consistency. These are spells which cause damage, so
anti-magic should stop the damage from the spells.

- Void Blast
- I have no idea why I made the cooldown so high on this, 1 minute made
it almost worthless.

TLDR: Instakill click spells from across the screen bad, invulnerability
bad

## Changelog

:cl: Melbert
balance: Heretic: Furious Steel's cooldown has been doubled (30s ->
60s), and abides by antimagic
balance: Heretic: Cleave's cooldown has increased by 5s, range has been
decreased to 4 tiles, and wound applied now has natural clotting
balance: Heretic: Blood Siphon's range has been decreased to 6 tiles
balance: Heretic: Void Pull and Phase abide by antimagic
balance: Heretic: Halved Void Blast's cooldown to 30s
qol: Heretic: Void Blast and Rust Formation now have distinct icons 
/:cl:

---
## [lxc/lxd](https://github.com/lxc/lxd)@[de0d151a2c...](https://github.com/lxc/lxd/commit/de0d151a2cc9bd8cef31431e126649e2b6a18be7)
#### Thursday 2022-12-08 06:37:57 by Thomas Parrott

lxd/instance/drivers/driver/qemu: Fix macvlan NICs losing connectivity on LXD restart

Switch to using monitor.SendFile() rather than monitor.SendFileWithFDSet(), as there
appears to be some rather strange behaviour going on with QEMU when used with macvtap
NICs.

If you pass the macvtap file handles using monitor.SendFileWithFDSet() it will use a
separate FD set for each file handle. This works fine, and I can see the correct file
handles opened by the QEMU process. But when LXD is restarted (the monitor connection
is closed), the file handles are closed by QEMU, causing the connectivity to break.

I have experimented with using the same FD set for all file handles associated to a
particular macvtap NIC. This didn't fix the issue.

I also tried hard coding the FD set ID to 0. This meant that the macvtap NIC would
share an FD set with the root disk device. Interestingly this solved the issue.
However it made me uncomfortable as the root disk is only configured by referencing
the FD set ID itself, rather than a particular FD inside the set. So I don't think
that sharing an FD set with multiple devices is a good idea.

However it got me thinking that perhaps the fact that the root disk is referencing
the FD set by ID (i.e using file=/dev/fdset/0 in its config) meant that QEMU somehow
realised that the FD set should be persisted even after the monitor has disconnected.

I confirmed that using the same FD set (even if a different ID than 0) for macvtap NICS
as the root disk device fixed the issue.

But because of my discomfort at that scenario (explained above) I instead looked for
a different solution. Before introducing multi-queue macvlan support for VMs we were
using monitor.SendFile() which worked fine. However I had switched to using the
monitor.SendFileWithFDSet() function as the former didn't support accessing the specific
FD number that was created inside QEMU. I thought we needed this because all the
documentation around using multi-queue macvtap devices showed the use of numeric FDs.

However on further exploration it turns out that we can infact use monitor.SendFile,
and by sending each file handle with a unique name we can then refer to those file
handles using the same names in `fds` setting for the macvtap devices.

Note: Because the `fds` list is colon separated one cannot use colons in the file
handle names. And I also experienced issues with connectivity when using dashes in
the file handle names. So I opted for using full-stops instead.

Fixes #11201

Signed-off-by: Thomas Parrott <thomas.parrott@canonical.com>

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[e273ed1b5f...](https://github.com/francinum/Therac-Gameserver/commit/e273ed1b5f2cc445810bf4b6f3a0ea659d40a43a)
#### Thursday 2022-12-08 07:49:40 by Kapu1178

update screenshot tests (#55)

* update screenshot tests

* try fix issues

* fix

* try fix lizard

* fuck you im tired

* fucking come on

* fuck it im disabling this and fixing it later

* Fix chain pull through space issue (fixes unit test failure) (#69832)

* Disables ashwalker unit test

* FUCK YOU

Co-authored-by: Marina <50789504+KirbyDaMaster@users.noreply.github.com>

---
## [TheOmnibus/NiggerBlocker](https://github.com/TheOmnibus/NiggerBlocker)@[167349ebb5...](https://github.com/TheOmnibus/NiggerBlocker/commit/167349ebb5ff457e317bfb906c1d7270614e68b8)
#### Thursday 2022-12-08 08:18:30 by Ominous

Update NigBlock

since mickey mouse (er. made-of shitler, i think that was it) says we can't improve the world and society by exterminating all the jews and niggers from the planet, at least there's this goggle so you can use the internet.  enjoy.

---
## [ZerlordJohn/app-dev](https://github.com/ZerlordJohn/app-dev)@[62e02bc35a...](https://github.com/ZerlordJohn/app-dev/commit/62e02bc35aec3f9d426d805362341994fe1e7ef6)
#### Thursday 2022-12-08 09:11:46 by ZerlordJohn

Update README.md

1. The story follows former hitman John Wick and his attempt to hunt down the men who broke into his home, stole his vintage car, and killed his puppy, which was a last gift to him from his recently deceased wife.
2. Facing an uncertain future and confronting the ghosts of his past, Maverick is drawn into a confrontation with his own deepest fears, culminating in a mission that demands the ultimate sacrifice from those who will be chosen to fly it.
3. Is a fantasy romance about a modern day goblin  who seeks to end his cursed immortal life and needs a human bride  to do so. His life then becomes intertwined with a grim reaper  who is unable to remember his 
4. In the film, S.H.I.E.L.D. director Nick Fury assembles Iron Man, Captain America, Hulk, Thor, Black Widow and Hawkeye to battle Thor's adoptive brother, Loki, who attempts to subjugate humanity by leading an invasion by the extraterrestrial race known as the Chitauri.
5. Dr. Stephen Strange, a brilliant but arrogant New York City neurosurgeon on top of his game, is more interested in fame and his perfect success rate than saving lives. And then, a nearly fatal car accident robs Stephen of his impeccable career.

---
## [LeDrascol/S.P.L.U.R.T-Station-13](https://github.com/LeDrascol/S.P.L.U.R.T-Station-13)@[8eec99b320...](https://github.com/LeDrascol/S.P.L.U.R.T-Station-13/commit/8eec99b3206e917bd711987a80422168de53f83d)
#### Thursday 2022-12-08 11:40:52 by LemonInTheDark

Caches GetJobName. Fuck you (#274)

* Caches GetJobName. Fuck you

This code made me deeply upset, WHY IS IT RECURSIVE WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY

* Centcom handling, properly this time

* Empties out real_job_name

* Sets real_job_name up in the right place

* Moves real_job_name to SSjob, uses modularTM

* Yeet

* Removes old code, swaps over to the SSjob list

* dme changes

* indents... comments

Co-authored-by: SandPoot <enric_gabirel@hotmail.com>

---
## [AvanaPY/DV2606_Lab2](https://github.com/AvanaPY/DV2606_Lab2)@[56dd02fcf8...](https://github.com/AvanaPY/DV2606_Lab2/commit/56dd02fcf86de68a5ba810f045757d9851674dca)
#### Thursday 2022-12-08 14:02:31 by Emil Karlström

gitignore updates, holy shit we are soo good at coding like oh my god we should get A*+++

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[fccd833526...](https://github.com/TrashDoxx/TG/commit/fccd833526364b131ce440b4ab0e65022103927c)
#### Thursday 2022-12-08 14:57:30 by GoldenAlpharex

Fishing Odds Code Improvements and Rescue Hooks (#71415)

## About The Pull Request
I wanted to try and implement an easier way for people to fish out
corpses from chasms, as I heard many tales of people trying to fish
others out of chasms and it taking over one IRL hour, with some cases
where it would take over two hours. Obviously, that's not really
interesting gameplay, and it doesn't really give people an incentive to
fish, it just turns it into an annoyance that people won't want to do
for fun. Now, we don't want that, do we?

As such, I've created the rescue hook, a special fishing hook that can
only be used in chasms (as that's currently the only place you can find
people into), which will only be able to fish out duds, skeleton
corpses, any mob that's fallen into a chasm and hasn't been rescued yet,
or rarely, a hostile monster lurking below. It has, at the time of
writing this, a weight of 5 (50 without bait, lower with bait) for duds
and a weight of 30 for chasm detritus, which themselves have a 50%
chance to be a random skeleton corpse, or a lobstrosity, and the
remaining 50% chance of fishing out a mob that's fallen into a chasm.
I'm open to tweaking these values if we think it's too easy or too hard,
but it's still a rather expensive item, so I'd consider it quite fine
the way it is myself, as it's still not risk-free.

It's currently only obtainable through buying it from cargo in the
goodies section, at a default price of 600 credits (making it
SIGNIFICANTLY more expensive than the rest of the fishing content, and
making it something that assistants will have to put some elbow grease
into if they want to be able to afford it).

As it stands currently, it can't be used to recover the fallen's
belongings that weren't on their person (i.e., their crusher if they
were holding it in hands), ~*but* I'm down to make that easier to fish
out using, for instance, the magnet hook, while also making it
incompatible with fishing out bodies, which would make it a nice way to
recover those lost items without spending over an hour fishing for them,
if that's something that maintainers would want.~ Maintainers did want
it, and as such...

The Magnetic hook is now the go-to hook to retrieve objects from chasms!
Not only does it inherently do a much better job at fishing out
non-fishes, it also has a lesser chance of retrieving random junk from
chasms, and an even lower chance of fishing out lobstrosities!

I also improved the code for the fishing weights calculation so that the
hooks and the rods can have an effect on the odds of certain types of
rewards more easily, with the option of offloading a more of what's
currently being calculated on `fishing_challenge` over on the rods or
even the hooks themselves.

I finished by fixing a handful of capitalization and punctuation issues
in various fishing items, as that bugged me when I was testing my
changes.

## Why It's Good For The Game
Corpses being recoverable from chasms was a great idea, however making
it so people would have to sink a major portion of their shift for a
chance at recovering a corpse doesn't create a particularly interesting
gameplay loop. However, being able to spend your hard-earned funds in
order to streamline that process without really being able to use that
to cheese other mechanics sounds like a great deal to me.

## Changelog

:cl: GoldenAlpharex
add: Added a Rescue Hook, that will allow the fishing rod it's attached
onto to become a lot more proficient at recovering corpses from chasms,
at the expense of making it unusable for more traditional fishing. It
isn't entirely lobstrosity-proof, however...
balance: The magnetic hook can no longer fish out corpses from chasms,
but will fish out items much more efficiently than any other hooks,
while also being much less attractive to lobstrosities. Some still fall
for it regardless, however.
spellcheck: Fixed the capitalization and punctuation in the description
of multiple fishing accessories.
code: Improved the code for fishing weights, to allow for different
hooks to have some more noticeable results on the weights without having
to add to an already massive proc.
/:cl:

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[7d04edb6e2...](https://github.com/TrashDoxx/TG/commit/7d04edb6e2927330906a7af89664b7a5ab3aa48c)
#### Thursday 2022-12-08 14:57:30 by Profakos

Mail sorting helper, and disposals fixes (#70861)

## About The Pull Request


![image](https://user-images.githubusercontent.com/2676196/198695007-53db1b70-845f-46a9-b98a-e146bb53951b.png)

This PR adds a mail sorting map helper, which during Late Initialization
will apply a sorting location index to the mail sorting disposals pipe
under them. I have replaced the varedits with all mail sorters with the
appropriate map helpers. I have thoroughly tested this, making sure
packages arrived to every location, where possible.

I have also fixed a few issues with the disposals network:

**Tramstation**

- One of the random maintenance segments had a place with no disposal
pipes. This has been fixed
- A sorter was looking for chapel and library packages, but it actually
meant to look for engineering packages
- There was no dormitory mail sorter, I have added one

**Metastation**

- There was no dormitory mail sorter, I have added one

**Icebox**

- There is no experimentor lab in icebox, but there is an
"experimentation" lab, which is good enough, so I have added it as a
location

**Deltastation**

- There was no dormitory mail sorter, I have added one
- Virology was not connected to the disposals network. However, on every
other map, it has a one way connection. I have hooked it up just like
that, so virology mail will arrive safely, and virology trash will go
into space as usual.

**Kilostation**

- Genetics packages were rerouted to the psychologist office

Unsolved issue on kilostation: there is no experimentor on this station,
and there is no space for a disposals in the circuits lab, so sadly, if
you send a package to this destination, it will come back to the mail
sorting office.

**Future improvements**

The TAGGERLOCATIONS list, which is used to retrieve the labels of the
various tags, is frankly unorganizable, and hard to expand. I have
delayed fixing this for a future PR.

I kinda wish to remove the sortType variable, as it is no longer
necessary to have it around with these helpers, but sadly, this would
ruin downstream maps, so I have no plans for this at the moment.

## Why It's Good For The Game

While mapping, having to constantly compare a comment in flavor_misc.dm
to figure out what to varedit a disposal mail sorter to is rather
annoying. These map helpers, similar to the access helpers, will help
with this issue.

Its also good if mail actually arrives.

## Changelog


:cl:
qol: added a mail sorting map helper, to allow mappers to create
disposal networks faster
fix: fixes several non working disposal mail targets that never received
their packages
/:cl:

---
## [guardian/gateway](https://github.com/guardian/gateway)@[b962f668b3...](https://github.com/guardian/gateway/commit/b962f668b35ac72f8f0a0aaace8ee180da8b816e)
#### Thursday 2022-12-08 15:12:04 by Mahesh Makani

feat(okta): show onboarding flow for new social users

In Okta it is currently not possible to differentiate between new social users, and existing social users. This means that is was not possible to show social users the
onboarding flow.

However there is a case where a new social user differentiates form existing social users. This is to do with the email validated status. A new social user will be in
the `GuardianUser-EmailValidated` but their `emailValidated` field in their user profile will be `false` or `undefined`. So we have a remediation step in our callback to
handle this discrepency, and set the `emailValidated` flag should the user be in the `GuardianUser-EmailValidated` group. This was introduced in this commit:
https://github.com/guardian/gateway/commit/9af078165aa5add60b9e11bfe6731ff25badca6e

This means that the only time this discrepency will occur is for new social users, meaning at this point we can differentiate them from existing social users. This
allows us to use this functionality and set a flag to show the onboarding flow `authState.confirmationPage = consentPages[0].path;`. At any other point in time the user
will have both the `GuardianUser-EmailValidated` group and the `emailValidated` flag set, so they would not see the onboarding flow again.

A number of other options were considered for this functionality, but would involve other changes to the Okta configuration.

1. Using Okta groups
The first option we tried was to use Okta groups to do this. The theory was for new social users we assign them to a specific Okta group that we create, we can then
check this group, and if a user is in this group show then the onboarding flow. We can then remove them from this group so they're not shown the onboarding flow again.

However although this does work and new social users do see the Onboarding flow. I noticed that all social users started seeing the onboarding flow, whether they were
new users, existing users, or had even seen the onboarding flow before. Turns out Okta will always add all social users to the new group if they are not currently in it.
So even when removing the group from the user,  the next time they sign in with social, they get added to the group again, and they get shown the onboarding flow again.
Which wasn't ideal.

2. Using the account `created` timestamp on the user object.
This option was to use the `created` field in the user profile to determine if we should show the onboarding flow or not. This would involve checking this field
everytime a user went to the oauth callback endpoint, and if it's within a certain time period, say 1 minute, then to show the onboarding flow in that scenario.

However the account `created` field isn't returned by default in either the access or id token. So we'd either have to make an additional API call for every time a user
goes to the oauth callback endpoint, or to add a custom claim to add this field to the id token.

Using the API option would require making additional API calls, which we're trying to avoid, due to a limited number of API calls we're able to make to Okta. While
adding this field to the id token would require changes to the Okta terraform configuration to add this in, and would add an additional payload to what's only
effectively used once.

Also we'd have to chose the time period to check to avoid users seeing the onboarding flow multiple times if we set it too long, e.g. if they sign in immeditely after
registering on another browser/device, or not seeing the onboarding flow at all if we set it too short.

Hence the reason I went with the approach that we did.

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[0747099063...](https://github.com/Zergspower/tgstation/commit/074709906301e3e396179c861ca0af068c3f36ec)
#### Thursday 2022-12-08 15:57:19 by RikuTheKiller

Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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

:cl:
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[bf582cb833...](https://github.com/Zergspower/tgstation/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Thursday 2022-12-08 15:57:19 by Profakos

Trophy case update (#71015)

## About The Pull Request

I have been chipping away/procrastinating at this since May, but after
several years, I have finally updated how Trophy Cases work.

So, what this PR does is the following:

- Standardized everything in persistence.dm to use snake case, and added
basic autodocs
- Automatically moves trophies from data/npc_saves/TrophyItems.json to
data/trophy_items.json. Removed legacy .sav conversion by request, it
has been a long time.
- Trophy cases are opened and loaded the same way you would open a
regular ID locked display case (used curator access, relevant access
autodoc has been updated)
- Instead of cheap plastic replicas that turn to dust anyways, trophy
cases use holograms, which can be dispelled by hand
- Trophy data gets saved if an item stays in the trophy case when the
shuttle arrives to centcom, and the item has a description set. This is
in line with paintings, which has to still hang on the wall at round
end.
- You can edit the description of new trophies by using the librarian's
key to unlock History Mode
- When you click on a closed trophy case, it will open a tgui, and will
not display the case description. It will still do for open cases.
Vendatrays have been updated to do the same.
- The UI's icon uses icon2base64(getFlatIcon(showpiece, no_anim=TRUE)).
Vendatrays have been updated similarly, so items with directions and
animations are displayed properly. The base64 strings are updated in
update_static_data.
- Fixes vendatrays from displaying some characters in strange ways, such
as displaying /improper.
- Renames some one letter, or nonindicate argument and var names in
trophy case code
- Adds a trophy management admin panel, where admins can finally delete
all the curator ID cards swallowed over the years. Or, they can replace
the paths with funny new paths.
- If an entry has an incorrect, no longer existing path, it will be
marked red in the management panel
- Adds MAX_PLAQUE_LEN define, which 144 characters
- Removes start_showpieces from trophy cases, as it was completely
unused. The start_showpiece_type var is still around.
- Moves trophy_message var to trophy cases. Only a dice collector
display case used them in the Snowdin map.

What this PR does not do

- Sadly, it still only saves the base image of an item, and no layers or
altered image states. This has to come in the future.

<details>
<summary>Click here to see various states of the trophy tgUI</summary>
 

![kép](https://user-images.githubusercontent.com/2676196/199545412-e5b7e7a8-59fb-41e6-aca5-6b07ba33501c.png)
Locked history mode, existing item.


![kép](https://user-images.githubusercontent.com/2676196/199545574-9e705603-9b7a-457d-9575-2d4145ad940d.png)
Unlocked history mode, but holographic trophy is present.


![kép](https://user-images.githubusercontent.com/2676196/199545883-45c3916b-011f-462a-8296-6eb13db32158.png)
Locked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199545967-a33e2501-aa5f-473b-b79f-ebd950df2afc.png)
Unlocked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199546100-718bd639-3199-4df7-ad77-ed3dbf27b290.png)
Unlocked history mode, item placed, default text. (Note: this picture is
out of date. The typo has been fixed, and "record a message" is now
"record a description" for consistency)
 

![kép](https://user-images.githubusercontent.com/2676196/199546202-5ebbbd28-907c-4f2d-b7cd-29d2ef21c7f3.png)
Unlocked history mode, item placed, new text.

</details>

<details>
<summary>Click here to see the admin panel</summary>


![kép](https://user-images.githubusercontent.com/2676196/199553349-8684f23f-4699-42f2-a27e-15cccad29d0b.png)


</details>

## Why It's Good For The Game

Less curator ID's stuck in the Trophy Cases, and the existing ones can
be cleaned up. A more immersive Trophy Case user experience, in general.

## Changelog


:cl:
refactor: refactored trophy cases, to be more user friendly
admin: created a trophy managment admin panel
/:cl:

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[bbb956d2a6...](https://github.com/Zergspower/tgstation/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Thursday 2022-12-08 15:57:19 by OrionTheFox

Removes Bowls from garbage spawners because they don't fit in trash bags and I'm SICK of not being able to clean! (#71152)

## About The Pull Request
Let me give you a scenario.

---

THIS, is you. Say hi!

![image](https://user-images.githubusercontent.com/76465278/200268480-9dcf1f45-3bc5-402d-b743-b0649deefb08.png)

You're a loyal janitor aboard NT-SS13. You love your job; despite the
dangers, it's generally not too busy or tedious. Just a spray, a sweep,
and put it all in a bag.

---

This. This is your enemy.

![image](https://user-images.githubusercontent.com/76465278/200269058-957ca433-4666-44b5-9c10-ae0da75219cb.png)

Some crewmembers continuously leave them in maintenance, tossing them
into garbage bins as they pass.
This bowl, you cannot spray it. You can sweep it as far as you want, but
in the end, cannot put it into the bag.

![image](https://user-images.githubusercontent.com/76465278/200269156-bbc7758b-9cbe-4a3b-8d17-9aa53254b4b2.png)

---

It exists to torment you.
Nothing more, nothing less.

You hate the bowl. And it hates you.
Wake up.

![image](https://user-images.githubusercontent.com/76465278/200269456-a7fda598-3556-4069-bd2a-44a8793c198f.png)
## Why It's Good For The Game
Usually when you pass a trash pile you expect it to have trash, and
entire bowls aren't technically trash code-wise, nor can you clean them.
Yes, this PR has a modicum of salt. It was salt left behind in THE DAMN
BOWLS.
## Changelog
:cl:
del: NT has decided to begin a Recycling initiative, asking crew to
please stop throwing their bowls away in maintenance. You should only
find trash and grime from now on!
/:cl:

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[c1f0141967...](https://github.com/Zergspower/tgstation/commit/c1f01419671ad084a6c048ec7900d008de53bfe2)
#### Thursday 2022-12-08 15:57:19 by LemonInTheDark

Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

---
## [Lukas-Hron/ZoomGame](https://github.com/Lukas-Hron/ZoomGame)@[a48edbfe60...](https://github.com/Lukas-Hron/ZoomGame/commit/a48edbfe60dc73902bb141ac8862db32b731d024)
#### Thursday 2022-12-08 16:03:25 by Lukas Hron

God damn bro we fucking got something that looks good now

---
## [Philippe-Cholet/rusty-aoc](https://github.com/Philippe-Cholet/rusty-aoc)@[a9d4034bad...](https://github.com/Philippe-Cholet/rusty-aoc/commit/a9d4034badab76645e67bce49b7cf2c10f637ea6)
#### Thursday 2022-12-08 17:43:20 by Philippe-Cholet

Update 2022 day 8

What I commited before was my 3rd version, which I think is nicely structured but I kinda miss my 2nd version which uses quick macros, which is less verbose than my functions with the `Iterator<Item = (usize, usize)>` trait.
I was a bit annoyed by the different types of the iterators types I has, and I did not wanted to box them into `Box<dyn Iterator...>` and use a closure on them hence the macro choice.
I just want to remember these nice/quick macros.

---
## [Atulkumar112/CODES](https://github.com/Atulkumar112/CODES)@[489fdba50b...](https://github.com/Atulkumar112/CODES/commit/489fdba50b59bf1448e18fc1c25de804647579fa)
#### Thursday 2022-12-08 17:47:17 by Atul kumar

Create A. Watermelon.java

A. Watermelon
time limit per test1 second
memory limit per test64 megabytes
inputstandard input
outputstandard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
inputCopy
8
outputCopy
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

---
## [fnfporterhi/SHAGGY](https://github.com/fnfporterhi/SHAGGY)@[ac759663fb...](https://github.com/fnfporterhi/SHAGGY/commit/ac759663fbb670e79aaff5d9ae83b5e9b422b555)
#### Thursday 2022-12-08 18:00:56 by MemeHoovy

the do whatever the fuck you want to license

you just DO WHATEVER THE FUCK YOU WANT TO

---
## [Shad0vvs/cmss13](https://github.com/Shad0vvs/cmss13)@[6120721323...](https://github.com/Shad0vvs/cmss13/commit/6120721323b6431a1d43d89d7354e1ea1763a734)
#### Thursday 2022-12-08 18:52:51 by carlarctg

Added various flasks to loadouts and canteen vendors. (#1802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Added a canteen (item) from an unused sprite.

Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

All flasks (and canteen (item)) can be selected in the character loadout
items menu at the bottom.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

The old W-Y flask looked more like a skull than the logo. The gold badge
bit was legacy from bay12.

> Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Legacy renaming.

> Added a canteen (item) from an unused sprite.

Cool sprite. Fucked up we didn't have canteens until now when, uh.
That's what people actually use in the military, not flasks. (To my
knowledge)

> Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

Canteens are the standard military container, W-Y flasks in the vendors
are a good Lore way to show how much of a WY suckup the USCM is.

> All flasks, vacuum and leather included, (and canteen (item)) can be
selected in the character loadout items menu at the bottom.

I think these flasks are cool ways to add flavor to your character, and
it's a shame most of them either weren't in the game or were in very
annoying to find places.

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

:cl:

imageadd: Resprited the W-Y Flask. Removed the gold badge from the
former detective's flask.
add: Renamed the former detective's flask and bar flask into the brown
and black, respectively, leather flasks.
add: Added a canteen (item) from an unused sprite.
add: Canteens (item) and W-Y flasks can now be found in the canteen
(place) vendors.
add: All flasks, vacuum and leather included, (and canteen (item)) can
be selected in the character loadout items menu at the bottom.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[612930f869...](https://github.com/i3roly/CMI8788/commit/612930f869157ece24b30b575a868b5a428ff504)
#### Thursday 2022-12-08 19:38:50 by gagan sidhu

yup, separate compilation of FPU calls was due to powerpc arch. reverting creation of libAudioFloatClip.

from the c flags it becomes painfully obvious the separate compilation of the floating point calls is due to the powerpc architecture.

this is a recurring theme with inferior (no offence intended, PPC is way cooler than ARM) processors, which require special handling unlike x86.

i was wondering why the fuck you'd have a separate static library for floating point and then link that in after, since it would be the same thing in the end.

but i don't know powerpc and i would imagine, just as some people have to compile ARM trash on softfloat to avoid FPU issues, this is something similar where fp-code is generated "only when you _absolutely_ need it"

curious decision to handle audio via FP when non x86 architectures (aside from MIPS) have grappled with FPU compilation quirks, but unquestionably a "forward-thinking" move.

probably still too far ahead of its time, sadly. shouldn't be, but it is.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[68ba844196...](https://github.com/cmss13-devs/cmss13/commit/68ba84419624366956ae5f9bde67f1e33287301a)
#### Thursday 2022-12-08 20:27:08 by RenaRenaRe

Cross-ciphering fix (#1879)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes the cross-ciphering property so it actually works instead of
producing a never ending stream of runtime errors and a broken larva
that never develops. I'm deliberately being vague about what it does
because I think it's supposed to be a secret, the wiki tells you to
"find out in game!", but you can just read the code since it isn't
complicated.
This is my first time using github so sorry if I've fucked something up.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Things should function the way they're supposed to.
Cross-ciphering is an extremely hard to get property that I'm not sure
if anyone has ever actually made in game, now on the incredibly rare
occasion that somebody actually makes it it should work correctly.
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
fix: Cross-ciphering now works correctly
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [ChungusGamer666/tgstation](https://github.com/ChungusGamer666/tgstation)@[ebc0227176...](https://github.com/ChungusGamer666/tgstation/commit/ebc0227176b5213f379eefc3f5c6aa7be2d09c0a)
#### Thursday 2022-12-08 20:31:26 by Tastyfish

Makes dog a basic mob [MDB IGNORE] (#70799)


About The Pull Request

    Made a basic version of the pet base called /mob/living/basic/pet. It's significantly more stripped down from the old simple_animal one, because its half collar stuff and...

    Made the collar slot a component that you could theoretically remove from a pet to disable the behavior, or add to any other living mob as long as you set up the icon states for the collar (or not, the visuals are optional).
        The corgi's collar strippable slot is now generally the pet collar slot, and in theory could be used for other pet stripping screens.

    I also gutted the extra access card code from /mob/living/basic/pet as it's only being used by corgis. Having a physical ID is now just inherent to corgis, as they're the only ones that could equip it anyway.

    Ported the make_babies() function from simple_animals to a new subtree and associated behavior, called /datum/ai_planning_subtree/make_babies that uses blackboards to know the animal-specific info.
        Note that it's marginally improved, as the female walks to the male first instead of bluespace reproduction.

    Tweaked and improved the dog AI to work as a basic mob, including making /datum/idle_behavior/idle_dog fully functional.

    Made a /datum/ai_planning_subtree/random_speech/dog that pulls the dynamic speech and emotes to support dog fashion.

I've tested base collars across multiple pet types.

For dogs, I've tested general behavior, fetching, reproduction, dog fashion, and deadchat_plays, covering all the oddities I'm aware of.

image
Why It's Good For The Game

Very big mob converted to a basic mob.
Changelog

cl
fix: Lisa no longer uses bluespace when interacting with Ian.
refactor: A large portion of dog code was re-written; please report any strange bugs.
/cl

---
## [PanicAtTheCisco/Discord-Bot-User-Permission-Escalation-Test](https://github.com/PanicAtTheCisco/Discord-Bot-User-Permission-Escalation-Test)@[a8096e84d3...](https://github.com/PanicAtTheCisco/Discord-Bot-User-Permission-Escalation-Test/commit/a8096e84d3033085150666e21cbaebede74cac10)
#### Thursday 2022-12-08 20:48:14 by PanicAtTheCisco

Update joke.js

Replaced old hard-coded joke generator with updated one that gets jokes from the 'icanhazdadjoke' API. Old code has been left because the jokes are still kinda funny, they are just commented out. now.

---
## [faizaanmadhani/cockroach](https://github.com/faizaanmadhani/cockroach)@[97054a0e76...](https://github.com/faizaanmadhani/cockroach/commit/97054a0e76049cd8f78d8b534ab1e2107be9f2ed)
#### Thursday 2022-12-08 20:59:45 by Tobias Grieger

kvnemesis: uniquely identify all versions

This is essentially a v2 of kvnemesis. While a lot of code has changed, it's not a rewrite, rather we are actually bringing kvnemesis closer to the idea which ultimately led to it being built. That idea is that if values can uniquely identify the operation which wrote them, serializability checking becomes easier as any observation of a value totally orders the reader and the writer with respect to each other. "Easier" meant both simpler code, as well as actually being able to computationally do the verification on complex histories.

Prior to this PR, kvnemesis was writing unique values where it could, but it couldn't do it for deletions - after all, a deletion is like writing a "nothing" to MVCC, and there wasn't any way to make two "nothings" distinguishable. Having broken with the basic premise of unique values, there was a lot of bending over backwards going on to avoid, for the most part, devolving into a "normal" serializability checker. However, for contrived edge cases this would not be avoidable, and so there would be histories that kvnemesis just couldn't handle.

"v2" (this PR) gets this right. The main contribution is that we now thread kvnemesis' sequence numbers all the way down into MVCC and back up with the RangeFeed. Values are now truly unique: a deletion tombstone is identifiable via its `MVCCValueHeader`, which carries the `kvnemesisutil.Seq` of the `Operation` that originally wrote it. On top of this, everything "just works" as you expect.

Plumbing testing-only fields through the KV API protobufs isn't something that was taken lightly and that required a good amount of deliberation. However, we figured out a clever (maybe too clever?) way to have these fields be zero-sized in production, meaning they cannot possibly affect production logic and they also do not influence struct sizes or the wire encoding. As a drawback, kvnemesis requires the `crdb_test` build tag (it will `t.Skip()` otherwise).

The remainder of this PR is mostly improvements in code quality. `echodriven` testing was introduced for many of the tests that could benefit from it. The core components of kvnemesis were reworked for clarity (the author spent the first week very confused and wishes for that experience to remain unrepeated by anyone). kvnemesis also tracks the execution timestamps as reported by the KV layer, which a future change could [use](https://github.com/cockroachdb/cockroach/issues/92898) for additional validation.

Of note is the updated doc comment, which is reproduced below in entirety.

Fixes #90955.
Fixes #88988.
Fixes #76435.
Fixes #69642.

----

Package kvnemesis exercises the KV API with random concurrent traffic (as
well as splits, merges, etc) and then validates that the observed behaviors
are serializable.

It does so in polynomial time based on the techniques used by [Elle] (see in
particular section 4.2.3), using the after-the-fact MVCC history as a record
of truth. It ensures that all write operations embed a unique identifier that
is stored in MVCC history, and can thus identify which of its operations'
mutations are reflected in the database ("recoverability" in Elle parlance).

A run of kvnemesis proceeds as follows.

First, a Generator is instantiated. It can create, upon request, a sequence
in which each element is a random Operation. Operations that are mutations
(i.e. not pure reads) are assigned a unique kvnemesisutil.Seq which will be
stored alongside the MVCC data written by the Operation.

A pool of worker threads concurrently generates Operations and executes them
against a CockroachDB cluster. Some of these Operations may
succeed, some may fail, and for some of them an ambiguous result may be
encountered.
Alongside this random traffic, kvnemesis maintains a RangeFeed that ingests
the MVCC history. This creates a "carbon copy" of the MVCC history.

All of these workers wind down once they have in aggregate completed a
configured number of steps.

Next, kvnemesis validates that the Operations that were executed and the
results they saw match the MVCC history, i.e. checks for Serializability. In
general, this is an NP-hard problem[^1], but the use of unique sequence
numbers (kvnemesisutil.Seq) makes it tractable, as each mutation in the MVCC
keyspace uniquely identifies the Operation that must have written the value.

We make use of this property as follows. First, the Validate method iterates
through all Operations performed and, for each, inspects

- the type of the Operation (i.e. Put, Delete, Get, ...),
- the (point or range) key of the operation, and
- its results (i.e. whether there was an error or which key-value pairs were returned).

Each atomic unit (i.e. individual non-transactional operation, or batch of
non-transactional operations, or transaction) results in a slice (in order
in which the Operations within executed[^2]) of observations, where each
element is either an observed read or an observed write.

For example, a Batch that first writes `v1` to `k1`, then scans `[k1-k3)`
(reading its own write as well as some other key k2 with value v2) and then
deletes `k3` would generate the following slice:

       [
         observedWrite(k1->v1),
         observedScan(k1->v1, k2->v2),
         observedWrite(k3->v3),
       ]

Each such slice (i.e. atomic unit) will then be compared to the MVCC history.
For all units that succeeded, their writes must match up with versions in
the MVCC history, and this matching is trivial thanks to unique values
(including for deletions, since we embed the kvnemesisutil.Seq in the value),
and in particular a single write will entirely fix the MVCC timestamp at
which the atomic unit must have executed.

For each read (i.e. get or scan), we compute at which time intervals each
read would have been valid. For example, if the MVCC history for a key `k1`
is as follows:

                  k1

       	 -----------------
       	 t5      v2
       	 t4
       	 t3
       	 t2     <del>
       	 t1      v1

then

  - observedGet(k1->v1)  is valid for [t1,t2),
  - observedGet(k1->nil) is valid for [0,t1) and [t2,t5), and
  - observedGet(k1->v2)  is valid for [t5,inf).

By intersecting the time intervals for each Operation in an atomic unit, we
then get the MVCC timestamps at which this Operation would have observed what
it ended up observing. If this intersection is empty, serializability must have
been violated.

In the error case, kvnemesis verifies that no part of the Operation became visible.
For ambiguous results, kvnemesis requires that either no Operation become visible,
or otherwise treats the atomic unit as committed.

The KV API also has the capability to return the actual execution timestamp directly
with responses. At the time of writing, kvnemesis does verify that it does do this
reliably, but it does not verify that the execution timestamp is contained in the
intersection of time intervals obtained from inspecting MVCC history[^3].

[Elle]: https://arxiv.org/pdf/2003.10554.pdf
[^1]: https://dl.acm.org/doi/10.1145/322154.322158
[^2]: there is currently concurrency within the atomic unit in kvnemesis. It
could in theory carry out multiple reads concurrently while not also writing,
such as DistSQL does, but this is not implemented today. See:
https://github.com/cockroachdb/cockroach/issues/64825
[^3]: tracked in https://github.com/cockroachdb/cockroach/issues/92898.

Epic: none
Release note: None

---
## [iann0036/cfn-stack-rename](https://github.com/iann0036/cfn-stack-rename)@[05cfc7ebd0...](https://github.com/iann0036/cfn-stack-rename/commit/05cfc7ebd063ec7e46a8911e67e4e33607fba719)
#### Thursday 2022-12-08 21:09:46 by vam

I believe stack_rename should have all current functionality of index.py

The tool has been pretty much refactored.

aws_handler added the following:

create_changeset
exec_changeset
list_imports
list_exports
delete_stack
waiter

Added all original functions - with a twist

it does not bomb out if it encounters resources that dont support
importing instead it lists them - but currently it is not printing out
this information.

the list_imports should list all of the stacks using the exports created
by the original stack (the code still needs to be written still) will
need to go through each stack that imports the resource and change that
specific import to be the actual value of the resource rather than an
"import" statement - theoretically this could be something random - it
may break the service but it will be temporary.

There is a function: resolvePropertyValue which I believe was originally
intended to go through the template and replace all subs and refs into
other values - however this is not used any where. I have not included
it.

No where in the documentation does it state that using a ref for a
resource that doesnt exist cant be done - I think the deployment may
fail for a new resource being built from scratch, but not for an import.
For the time being however I am not tackling this - this should be
addedjust for keeping thing sane.

I believe as we are retaining resources - if they reference
resources that cannot be retained / imported - the resources will exist
but become broken on the next update however those resources will once
again exist so should work again - this is the theory however
cloudformation is insanely dumb. Why would anyone use this ? Terraform
exists and absolutely destroys this mess of a deployment system. All
this code to rename a stack ?? Why is this not available as a function
without all of this mess - also stack drift what a farsical way of
handling this - aws has apis it can query itself to know the state of
the system - why do we have ito manually run this process ? Why is it not
capable of maintaining its own "drift" status ? Just awful, supremely
awful.

	modified:   libs/aws_handler.py
	modified:   stack_rename

---
## [Joalor64GH/Chocolate-Engine](https://github.com/Joalor64GH/Chocolate-Engine)@[68f6e6fe67...](https://github.com/Joalor64GH/Chocolate-Engine/commit/68f6e6fe67c91ad3927c5a546133f63d276ff221)
#### Thursday 2022-12-08 21:25:36 by MemeHoovy

okay fuck this stupid shit, fuck you and your methods

---
## [usernameComputer01/android_kernel_samsung_universal7580](https://github.com/usernameComputer01/android_kernel_samsung_universal7580)@[44565e2adc...](https://github.com/usernameComputer01/android_kernel_samsung_universal7580/commit/44565e2adcf5789816b581577257a1b00fd404cb)
#### Thursday 2022-12-08 21:56:52 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

[ Upstream commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d ]

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Change-Id: If4290e58a2c34a7f69e2aa8e9ec0b07f15792d21

---
## [brad0/mpv](https://github.com/brad0/mpv)@[6f7506b660...](https://github.com/brad0/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Thursday 2022-12-08 22:53:00 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [argonui/SCED](https://github.com/argonui/SCED)@[b5fbe4d0db...](https://github.com/argonui/SCED/commit/b5fbe4d0db1ba5b7ecb2547c5f46497b246e7293)
#### Thursday 2022-12-08 22:54:56 by bootleggerFinn

Initial 2.4.0

Rearranged table for new campaign
Previously featured community content converted to downloader versions
Updated/Added Following content: The Scarlet Keys, Celtic Rising, Jumanji, Machining a Mystery, Dr. Jekyll and Mr. Hyde, CYOA Campaign Guides, Dead Space Investigators, Aespa Investigators, Magical Girl Project, Streets of New Capenna, The Bad Batch, Arkham Fantasy  Pixel Art Mini-Cards
Updated snap points
Updated spawn position of standalone scenarios/challenge scenarios memory bags

---
## [arter97/caf_msm-5.10](https://github.com/arter97/caf_msm-5.10)@[4603a37f6e...](https://github.com/arter97/caf_msm-5.10/commit/4603a37f6eaefb2cedc35552f040d15d93025146)
#### Thursday 2022-12-08 23:16:17 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Killingeyes/Killingeyes-](https://github.com/Killingeyes/Killingeyes-)@[e711a6b5b5...](https://github.com/Killingeyes/Killingeyes-/commit/e711a6b5b59ca6268dcae987f558a29f81ad07b2)
#### Thursday 2022-12-08 23:26:30 by Killingeyes

@7@8@6@

![Killingeyes Hacking](Killingeyes_hacking.jpg)

# [Killingeyes Hacking](https://Killingeyes.com//Killingeyes-Hacking) [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Killingeyes%20Hacking%20-%20a%20collection%20of%20awesome%20lists%20for%20hackers%20and%20pentesters%20by%20@Killingeyes&url=https://Killingeyes.com/Hack-with-/Killingeyes-Hacking&hashtags=security,hacking)

**A collection of awesome lists for hackers, pentesters & security researchers.**

Your [contributions](contributing.md) are always welcome !

## Killingeyes Repositories

Repository | Description
---- | ----
[Android Security](https://Killingeyes.com/ashishb/android-security-awesome) 			| Collection of Android security related resources
[AppSec](https://Killingeyes.com/paragonie/awesome-appsec)								| Resources for learning about application security
[Asset Discovery](https://Killingeyes.com/redhuntlabs/Awesome-Asset-Discovery)    | List of resources which help during asset discovery phase of a security assessment engagement
[Bug Bounty](https://Killingeyes.com/djadmin/awesome-bug-bounty) 						| List of Bug Bounty Programs and write-ups from the Bug Bounty hunters
[Capsulecorp Pentest](https:/Killingeyes/.com/r3dy/capsulecorp-pentest) 						| Vagrant+Ansible virtual network penetration testing lab. Companion to "The Art of Network Penetration Testing" by Royce Davis
[CTF](https://Killingeyes.com/apsdehal/awesome-ctf) 										| List of CTF frameworks, libraries, resources and softwares
[Cyber Skills](https://Killingeyes.com/joe-shenouda/awesome-cyber-skills) | Curated list of hacking environments where you can train your cyber skills legally and safely
[DevSecOps](https://Killingeyes.com/devsecops/awesome-devsecops) 						| List of awesome DevSecOps tools with the help from community experiments and contributions
[Embedded and IoT Security](https://Killingeyes.com/fkie-cad/awesome-embedded-and-iot-security) | A curated list of awesome resources about embedded and IoT security
[Exploit Development](https://Killingeyes.com/FabioBaroni/awesome-exploit-development) 	| Resources for learning about Exploit Development
[Fuzzing](https://Killingeyes.com/secfigo/Awesome-Fuzzing) 								| List of fuzzing resources for learning Fuzzing and initial phases of Exploit Development like root cause analysis
[Hacking](https://Killingeyes.com/carpedm20/awesome-hacking) 						| List of awesome Hacking tutorials, tools and resources
[Hacking Resources](https://Killingeyes.com/vitalysim/Awesome-Hacking-Resources)          | Collection of hacking / penetration testing resources to make you better!
[Honeypots](https://Killingeyes.com/paralax/awesome-honeypots) 							| List of honeypot resources
[Incident Response](https://Killingeyes.com/meirwah/awesome-incident-response) 			| List of tools for incident response
[Industrial Control System Security](https://Killingeyes.com/hslatman/awesome-industrial-control-system-security)      | List of resources related to Industrial Control System (ICS) security
[InfoSec](https://Killingeyes.com/onlurking/awesome-infosec) 							| List of awesome infosec courses and training resources
[IoT Hacks](https://Killingeyes.com/nebgnahz/awesome-iot-hacks) 							| Collection of Hacks in IoT Space
[Mainframe Hacking](https://Killingeyes.com/samanL33T/Awesome-Mainframe-Hacking) 				| List of Awesome Mainframe Hacking/Pentesting Resources
[Malware Analysis](https://Killingeyes.com/rshipp/awesome-malware-analysis) 				| List of awesome malware analysis tools and resources
[OSINT](https://Killingeyes.com/jivoi/awesome-osint) 									 | List of amazingly awesome Open Source Intelligence (OSINT) tools and resources
[OSX and iOS Security](https://Killingeyes.com/ashishb/osx-and-ios-security-awesome) 	| OSX and iOS related security tools
[Pcaptools](https://Killingeyes.com/caesar0301/awesome-pcaptools) 						| Collection of tools developed by researchers in the Computer Science area to process network traces
[Pentest](https://Killingeyes.com/enaqx/awesome-pentest) 								| List of awesome penetration testing resources, tools and other shiny things
[PHP Security](https://Killingeyes.com/ziadoz/awesome-php#security) 						| Libraries for generating secure random numbers, encrypting data and scanning for vulnerabilities
[Real-time Communications hacking & pentesting resources](https://Killingeyes.com/EnableSecurity/awesome-rtc-hacking) | Covers VoIP, WebRTC and VoLTE security related topics
[Red Teaming](https://Killingeyes.com/yeyintminthuhtut/Awesome-Red-Teaming) | List of Awesome Red Team / Red Teaming Resources
[Reversing](https://Killingeyes.com/fdivrp/awesome-reversing) 						| List of awesome reverse engineering resources
[Reinforcement Learning for Cyber Security](https://Killingeyes.com/Limmen/awesome-rl-for-cybersecurity) 							| List of awesome reinforcement learning for security resources
[Sec Talks](https://Killingeyes.com/PaulSec/awesome-sec-talks) 							| List of awesome security talks
[SecLists](https://Killingeyes.com/danielmiessler/SecLists) 								| Collection of multiple types of lists used during security assessments
[Security](https://Killingeyes.com/sbilly/awesome-security) 								| Collection of awesome software, libraries, documents, books, resources and cools stuffs about security
[Serverless Security](https://Killingeyes.com/puresec/awesome-serverless-security/) 			| Collection of Serverless security related resources
[Social Engineering](https://Killingeyes.com/v2-dev/awesome-social-engineering) | List of awesome social engineering resources
[Static Analysis](https://Killingeyes.com/mre/awesome-static-analysis) 					| List of static analysis tools, linters and code quality checkers for various programming languages
[The Art of Hacking Series](https://Killingeyes.com/The-Art-of-Hacking/h4cker)    | List of resources  includes thousands of cybersecurity-related references and resources
[Threat Intelligence](https://Killingeyes.com/hslatman/awesome-threat-intelligence) 		| List of Awesome Threat Intelligence resources
[Vehicle Security](https://Killingeyes.com/jaredthecoder/awesome-vehicle-security) 	| List of resources for learning about vehicle security and car hacking
[Vulnerability Research](https://Killingeyes.com/re-pronin/awesome-vulnerability-research) | List of resources about Vulnerability Research
[Web Hacking](https://Killingeyes.com/infoslack/awesome-web-hacking) 					| List of web application security
[Windows Exploitation - Advanced](https://Killingeyes.com/yeyintminthuhtut/Awesome-Advanced-Windows-Exploitation-References) | List of Awesome Advanced Windows Exploitation References
[WiFi Arsenal](https://Killingeyes.com/0x90/wifi-arsenal) 								| Pack of various useful/useless tools for 802.11 hacking
[YARA](https://Killingeyes.com/InQuest/awesome-yara)                                     | List of awesome YARA rules, tools, and people
[Hacker Roadmap](https://Killingeyes.com/sundowndev/hacker-roadmap)                                     | A guide for amateur pen testers and a collection of hacking tools, resources and references to practice ethical hacking.

## Other useful repositories

Repository | Description
---- | ----
[Adversarial Machine Learning](https://Killingeyes.com/yenchenlin/awesome-adversarial-machine-learning) | Curated list of awesome adversarial machine learning resources
[AI Security](https://Killingeyes.com/RandomAdversary/Awesome-AI-Security) | Curated list of AI security resources
[API Security Checklist](https://Killingeyes.com/shieldfy/API-Security-Checklist) | Checklist of the most important security countermeasures when designing, testing, and releasing your API
[APT Notes](https://Killingeyes.com/kbandla/APTnotes) 									| Various public documents, whitepapers and articles about APT campaigns
[Bug Bounty Reference](https://Killingeyes.com/ngalongc/bug-bounty-reference) 			| List of bug bounty write-up that is categorized by the bug nature
[Cryptography](https://Killingeyes.com/sobolevn/awesome-cryptography) | Cryptography resources and tools
[CTF Tool](https://Killingeyes.com/SandySekharan/CTF-tool) 								| List of Capture The Flag (CTF) frameworks, libraries, resources and softwares
[CVE PoC](https://Killingeyes.com/qazbnm456/awesome-cve-poc) | List of CVE Proof of Concepts (PoCs)
[Detection Lab](https://Killingeyes.com/clong/DetectionLab)                              |  Vagrant & Packer scripts to build a lab environment complete with security tooling and logging best practices
[Forensics](https://Killingeyes.com/Cugu/awesome-forensics) 								| List of awesome forensic analysis tools and resources
[Free Programming Books](https://Killingeyes.com/EbookFoundation/free-programming-books) 			| Free programming books for developers
[Gray Hacker Resources](https://Killingeyes.com/bt3gl/Gray-Hacker-Resources) 			| Useful for CTFs, wargames, pentesting
[GTFOBins](https://Killingeyes.io)	| A curated list of Unix binaries that can be exploited by an attacker to bypass local security restrictions
[Hacker101](https://Killingeyes.com/Hacker0x01/hacker101) | A free class for web security by HackerOne
[Infosec Getting Started](https://Killingeyes.com/gradiuscypher/infosec_getting_started)					| A collection of resources, documentation, links, etc to help people learn about Infosec
[Infosec Reference](https://Killingeyes.com/rmusser01/Infosec_Reference) 				| Information Security Reference That Doesn't Suck
[IOC](https://Killingeyes.com/sroberts/awesome-iocs) 									| Collection of sources of indicators of compromise
[Linux Kernel Exploitation](https://Killingeyes.com/xairy/linux-kernel-exploitation) | A bunch of links related to Linux kernel fuzzing and exploitation
[Lockpicking](https://Killingeyes.com/meitar/awesome-lockpicking) | Resources relating to the security and compromise of locks, safes, and keys.
[Machine Learning for Cyber Security](https://Killingeyes.com/jivoi/awesome-ml-for-cybersecurity)   | Curated list of tools and resources related to the use of machine learning for cyber security
[Payloads](https://Killingeyes.com/foospidy/payloads)  | Collection of web attack payloads
[PayloadsAllTheThings](https://Killingeyes.com/swisskyrepo/PayloadsAllTheThings)   | List of useful payloads and bypass for Web Application Security and Pentest/CTF
[Pentest Cheatsheets](https://Killingeyes.com/coreb1t/awesome-pentest-cheat-sheets)		| Collection of the cheat sheets useful for pentesting
[Pentest Wiki](https://Killingeyes.com/nixawk/pentest-wiki) 								| A free online security knowledge library for pentesters / researchers
[Probable Wordlists](https://Killingeyes.com/berzerk0/Probable-Wordlists)  | Wordlists sorted by probability originally created for password generation and testing
[Resource List](https://Killingeyes.com/FuzzySecurity/Resource-List) 					| Collection of useful GitHub projects loosely categorised
[Reverse Engineering](https://Killingeyes.com/onethawt/reverseengineering-reading-list)   | List of Reverse Engineering articles, books, and papers
[RFSec-ToolKit](https://Killingeyes.com/cn0xroot/RFSec-ToolKit)  | Collection of Radio Frequency Communication Protocol Hacktools
[Security Cheatsheets](https://Killingeyes.com/andrewjkerr/security-cheatsheets) 		| Collection of cheatsheets for various infosec tools and topics
[Security List](https://Killingeyes.com/zbetcheckin/Security_list)						 | Great security list for fun and profit
[Shell](https://Killingeyes.com/alebcay/awesome-shell) 									| List of awesome command-line frameworks, toolkits, guides and gizmos to make complete use of shell
[ThreatHunter-Playbook](https://Killingeyes.com/Cyb3rWard0g/ThreatHunter-Playbook) | A Threat hunter's playbook to aid the development of techniques and hypothesis for hunting campaigns
[Web Security](https://Killingeyes.com/qazbnm456/awesome-web-security) | Curated list of Web Security materials and resources
[Vulhub](https://Killingeyes.com/vulhub/vulhub) | Pre-Built Vulnerable Environments Based on Docker-Compose

## Need more ?

Follow **Killingeyes** on your favorite social media to get daily updates on interesting GitHub repositories related to Security.
 - Twitter : [@Killingeyes](https://twitter.com/Killingeyes)
 - Facebook : [Killingeyes](https://www.facebook.com/Killingeyes)

## Contributions

Please have a look at [contributing.md](contributing.md)

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[0e64e06e9e...](https://github.com/yogstation13/Yogstation/commit/0e64e06e9e738cc7c170a008b264b6dbecc98df6)
#### Thursday 2022-12-08 23:35:34 by Sniblet

Update objective.dm (#17000)

My name is not important. What is important is what I'm going to do. I just fucking hate this world, and the human worms feasting on its carcass. My whole life is just cold, bitter HATRED. And I always wanted to die violently. This is the time of vengeance, and no life is worth saving. And I will put into the grave as many as I can. It's time for me to kill. And it's time for me to die.

---
## [Kharzette/GrogLibsC](https://github.com/Kharzette/GrogLibsC)@[c27fdafcbb...](https://github.com/Kharzette/GrogLibsC/commit/c27fdafcbb9474d8ee7978b01f4341e7feaa4187)
#### Thursday 2022-12-08 23:35:51 by Kharzette

Got stalled for a long time on swap chain creation.  The thing that is killing me is that I can't step into SDL from within dxvk.  If I step into SDL from my own code it works.  I'm guessing there's some sort of goblinry going on where the dxvk is loading a different binary.  Why is linux so goofy with shared libs?  I thought dlls couldn't get worse.

Anyway, digging through the assembly I could see some macro failing.  Turns out it was the window handle.  I was grabbing a hwnd through memcpy of some ill defined window struct.  Then I saw a cast of hwnd to SDL_Window... it was one of those freaky C++ casts I never quite trusted, but even magical sky-wizard casting can't do that kind of magic.  I went back and read the docs and yep, you are suppose to just substitute SDL_Window for HWND.

So I have a swapchain!  Yey!

That was a good 6 hours of pain.  I think on windows I'd have had that fixed in 5 minutes, because I'd be able to see what is going on in the debugger.

---

