## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-10-29](docs/good-messages/2023/2023-10-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,028,382 were push events containing 2,812,278 commit messages that amount to 161,673,100 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 85 messages:


## [PestoVerde322/BeeStation-Hornet](https://github.com/PestoVerde322/BeeStation-Hornet)@[9c0fae42b5...](https://github.com/PestoVerde322/BeeStation-Hornet/commit/9c0fae42b54044b2d98fc7b4b67f7e4fd00d0006)
#### Sunday 2023-10-29 00:01:21 by Haliris

FUCK YOU SPIDERLINGS

Also adds more healing for the crew, and fixes the walls near the TEG/lava machine.
Makes ambush carp speaks narsian.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f3d81edb00...](https://github.com/tgstation/tgstation/commit/f3d81edb00b07160bc046ab0d79457e60aefba0e)
#### Sunday 2023-10-29 00:02:24 by Paxilmaniac

Improves the deployable component (#79199)

## About The Pull Request

The deployable component had a few random things I noticed when I tried
actually using it that kinda sucked so I'm:

Making the examine message more generic, we did NOT need to make it that
complicated.
Letting anything with hands deploy stuff, because mobs other than humans
can hold things.
Giving the option to let something be deployed more than once.
Letting direction setting be optional.
Tweaking the check for if something can be placed somewhere to be a bit
better.
## Why It's Good For The Game

I want to use the deployable component for stuff but I made it awful.
## Changelog
:cl:
code: the deployable component has been tweaked and improved with some
new options to it
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[eb9da97b7d...](https://github.com/tgstation/tgstation/commit/eb9da97b7da54f9bdce32aa29ec972f469625ed2)
#### Sunday 2023-10-29 00:02:24 by GoldenAlpharex

Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay (#79275)

## About The Pull Request
The title says it all, really.

I always thought ice looked a bit silly, and always wondered why. Today,
I found out it was because of the `wet_floor` component adding an
overlay that suddenly made a turf that should look continuous, tiled,
which in turn gave some very ugly visuals. Ice already looks slippery,
you can tell that it's ice, and the overlay that was added to it just
didn't really help telegraph that any better than the sprite itself
already does.

That's why I added support to make it so it would be possible to force
the overlay to just not be applied to the turf that's affected by the
component, to make it all look a bit better overall.

I added it to the ice turfs as a proof of concept, although I guess it
could also be used on other turfs that are always "wet", like the
bananium floors, but I didn't really care enough to touch that yet, and
I guess the bananium floors can use it a bit better than ice did.

I did notice in this PR that the smoothing of ice seemed to potentially
be broken, but that's something to look into at a later time.

## Why It's Good For The Game
Look at this ice and how much smoother it looks like now:

![image](https://github.com/tgstation/tgstation/assets/58045821/6fc85239-e8f1-404b-bc0e-6e1fca7f7753)

## Changelog

:cl: GoldenAlpharex
code: Added support to the wet_floor component to make it so the wet
overlay could not be applied to certain turfs if desired.
fix: Ice turfs no longer look tiled, and instead look smooth when placed
next to one-another.
/:cl:

---
## [moocowswag/FeatureInflation13](https://github.com/moocowswag/FeatureInflation13)@[9ff9e4b9a8...](https://github.com/moocowswag/FeatureInflation13/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Sunday 2023-10-29 00:04:43 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [moocowswag/FeatureInflation13](https://github.com/moocowswag/FeatureInflation13)@[071f6063e6...](https://github.com/moocowswag/FeatureInflation13/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Sunday 2023-10-29 00:04:43 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [moocowswag/FeatureInflation13](https://github.com/moocowswag/FeatureInflation13)@[0d5f9907a2...](https://github.com/moocowswag/FeatureInflation13/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Sunday 2023-10-29 00:04:43 by Jacquerel

Shapechange health transfer tweaks (#79009)

## About The Pull Request

Fixes #78721
This PR does a handful of things behind the scenes to increase the
consistency of shapechange health tracking.

First of all we adjust the order of operations taken when you restore
the original body. The implementation as-was would remove the status
effect midway through and null a bunch of variables we tried to continue
using. This would result in several runtimes and code failing to run,
with the upshot that untransforming upon death would leave the caster
completely alive, with the corpse of its transformed shape at its feet.
Oops.

Additionally while testing this I realised that transferring the damagew
as also kind of fucked.
We wouldn't bother to do it at _all_ if you died, which is a shame, so I
made it simply heal you instead of reviving you so we can always do it.
Then as noted in the linked issue, we were applying all transferred
damage to a single limb, which could exceed the health of the limb and
remove damage. Now we spread it around the body.

Finally, applying damage to a human using the "force" flag would often
actually apply less damage to their _health_ than expected. This is
because arms and legs contribute only 75% of their damage taken to a
mob's overall health.
Now instead of reading `health` we read `total damage` which ignores the
limb damage modifier.

The end result of this is that if you transform into a corgi, take 50%
of your health, and transform back then you will have 50% of your health
as a human.
Previously the result would be that you'd have ~63%, then transforming
into a corgi would leave you with ~63% of a corgi's health, then
transforming back into a human would leave you at about 71%... and so on
and so forth. Now it doesn't do that.

## Changelog

:cl:
fix: Dying when using (most) shapeshift spells will now kill you rather
than having you pop out of the corpse of your previous form.
fix: Damage will now be accurately carried between forms rather than
being slightly reduced upon each transformation.
/:cl:

---
## [StrangeWeirdKitten/Skyrat-tg](https://github.com/StrangeWeirdKitten/Skyrat-tg)@[c539a469d5...](https://github.com/StrangeWeirdKitten/Skyrat-tg/commit/c539a469d59849c15a115b319ec5953904863321)
#### Sunday 2023-10-29 00:31:44 by SkyratBot

[MIRROR] Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring [MDB IGNORE] (#24120)

* Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring (#78761)

## About The Pull Request
These sprites have been adapted from a person who wished to remain
anonymous with their blessing for tg

Take the old IDs and make them look a little more fancy and sci-fi, I
think they look really nice! This makes the job marker into a cute
little screen too, but this is totally optional, if maintainers want the
animation gone It wont take long at all.
Also resprites a few random other items in the cards.dmi, such as emags,
doorjacks, hack-o-lanturn, budget cards, and one touch up on the red
team ID for laser tag for consistency.
Also prisoner IDs had black symbols and black department but orange trim
on an orange card, so it was just a huge mess.

![all the small
things](https://github.com/tgstation/tgstation/assets/81941674/7bfe75a3-bb75-45bc-9947-373f16d4096b)

## Why It's Good For The Game

I'm gonna be real IDs are kinda crusty, and its something EVERYONE has
to look at at least once a shift. Poor HOPs may even look at two. God
forbid three. Now they will look pretty neat.
As for the other changes, the hack-o-lantern looks like it was made in
2001 its OLD. I don't even know if we use it, but now its updated. The
red laser tag team got a nerf so now all team letters are white, instead
of red being orange for no reason.

## Changelog
:cl:
image: We have received a new shipment of IDs, as the old ones were
found out to be haunted.
image: Laser tag red team ID has received a massive nerf
image: Station budget cards have gotten a facelift
image: Emags and Doorjacks
fix: Numbered prisoner IDs will now be legible
/:cl:

* Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring

---------

Co-authored-by: EricZilla <81941674+EricZilla@users.noreply.github.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[157fafeaa9...](https://github.com/necromanceranne/tgstation/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Sunday 2023-10-29 00:34:38 by lizardqueenlexi

[CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

## About The Pull Request

Fixes #79147.

Prevents the Demonic Frost-Miner from shooting at corpses by returning
early from `OpenFire()`. Also adds the "gutted" status effect to the
corpses in its arena so it won't try to gut them.
## Why It's Good For The Game

#78826 introduced an unfortunate bug by placing corpses in the Frost
Miner's arena. There were a combination of three factors at play here:
that the Miner attacks corpses, that it happens to use colossus bolts in
its attacks, which dust corpses, and that some unfortunate quirk of life
code causes runtimes if, as far as I can tell, a life tick goes off when
a mob is at the wrong point in the dusting process. The time this
process takes happened to perfectly coincide with the Monkey Business
unit test (being the first test that takes a significant period of
time), causing it to randomly fail.

So, this fixes a flaky test that has been a pain in the ass for the last
five days, is the big thing.

Also, it can't possibly have been intended for the Miner to run around
obliterating the aesthetic corpses in its arena within the first 15
seconds of any given round. Completely ruining the mood!

I'll point out that this particular boss may have been forgotten in
#77731, which set out to make only the colossus still gib/dust you, but
even were that not the case I think it would be a bit silly for the
Miner to be busy shooting lifeless corpses when a player shows up to
challenge it, rather than standing in its scary ritual circle.
## Changelog
:cl:
fix: The Demonic Frost-Miner will no longer run around destroying the
corpses in its arena the moment the round begins.
/:cl:

---
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[b22529fc74...](https://github.com/MrSamu99/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Sunday 2023-10-29 00:36:17 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Keoiki/violastro-trolling-show](https://github.com/Keoiki/violastro-trolling-show)@[12e3cfce44...](https://github.com/Keoiki/violastro-trolling-show/commit/12e3cfce4447426bbc2d8a8f3d292d4ea42f9dcc)
#### Sunday 2023-10-29 00:38:13 by Keoiki

Update Dialogue.hx
FUCK YOU FlxSound
STOP playing the dialogue music BEFORE the transition is complete
^ not fixed btw

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[bf4671ff83...](https://github.com/shiptest-ss13/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Sunday 2023-10-29 00:42:09 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[c034314f1b...](https://github.com/nikothedude/Skyrat-tg/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Sunday 2023-10-29 00:58:02 by SkyratBot

[MIRROR] Basic skeletons [MDB IGNORE] (#24545)

* Basic skeletons (#79206)

## About The Pull Request

Turns skeletons (the simple animal version) into basic mobs. This was
another incredibly simple conversion, since skeletons don't really do
anything but walk at you and beat you to death.

Because I thought it was funny, though, skeletons will now seek out
cartons of milk and drink them. Real milk will heal them for a
significant amount, but soymilk, being false milk, will deal them
grievous injury instead! Skeletons beware... I didn't add any other
sorts of milk due to limited ability with existing AI behaviors to
identify milk containers (they actually only look for the carton items).

Other than that, I've done some flavor adjustment for skeletons' attacks
- their effects and sounds will now suit the weapon they're actually
holding - for example, skeleton templars now actually use their swords
instead of slashing you with their horrible fingers. Along with this I
gave the basic skeletons a normal slashing sound, instead of the weird,
impactless hallucination sound they used to use for some reason. I never
liked that sound.

Finally, I've reflavored the spear-wielding skeleton mobs to "undead
settlers", following the naming of the corpses dropped by snow legions
as of #76898, rather than being named after an offensive term for Inuit
people. These skeletons do, after all, appear in settlements on alien
worlds.

To enable the flavor of milk drinking, I expanded the `basic_eating`
component to allow drinking rather than eating flavor, with a different
sound and its own set of verbs. This deletes whatever they drink from,
but c'est la vie.
## Why It's Good For The Game

Ticks 6 more entries off the simple animal freeze. While skeletons are
still extremely simple, being largely-identical mobs that only exist to
beat you to death, being basic mobs should make them slightly better at
this job. Also, again, I think it's really funny that you can distract
skeleton mobs with milk, or even hurt them.
## Changelog
:cl:
refactor: Hostile skeleton NPCs now use the basic mob framework. They're
a little smarter, and they also have a slightly improved set of attack
effects and sounds. They love to drink milk, but will be harmed greatly
if any heartless spaceman tricks them into drinking soymilk instead.
Please report any bugs.
/:cl:

* Basic skeletons

* updatepaths

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[0e3b7d842b...](https://github.com/nikothedude/Skyrat-tg/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Sunday 2023-10-29 00:58:02 by SkyratBot

[MIRROR] Adds a Syndicate Monkey Agent beacon uplink item [MDB IGNORE] (#24550)

* Adds a Syndicate Monkey Agent beacon uplink item (#79012)

## About The Pull Request

Adds a Syndicate Monkey Agent beacon uplink item. It spawns a dapper
monkey that must follow your orders.

Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

Added a more modularlike subtype for antagonist spawners to reduce
future hardcoding.

Gave the syndicate turtleneck a monkey sprite, from SS14!

## Why It's Good For The Game

I want to see the clown driving security insane with 2-3 monkeys and an
incredible amount of pranking. Or an assistant killing everyone with his
monkey friends while wearing a monkey suit. Or a geneticist sending out
mutated monkeys to kill people. Or a scientist equipping his monkeys
with bombs or xenobiology equipment and sending them out to wreak havoc.

6 TC is only enough for two monkeys, but you can get a third if you
finish any kind of objective.

> Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

We can't have the monkey mafia without guns, come on. The guns are weak
and only usable by monkeys. Additionally, they're restricted to
entertainment only.

Credit to SS14 for the monky turtleneck sprite.

## Changelog

:cl:
add: Adds a Syndicate Monkey Agent beacon uplink item. It spawns a
dapper monkey that must follow your orders.
add: Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.
refactor: Added a more modularlike subtype for antagonist spawners to
reduce future hardcoding.
sprite: Gave the syndicate turtleneck a monkey sprite, from SS14!
/:cl:

---------

Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Adds a Syndicate Monkey Agent beacon uplink item

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e642f9f49d...](https://github.com/treckstar/yolo-octo-hipster/commit/e642f9f49d8f12ba1d42bf6dcac226d463c67d80)
#### Sunday 2023-10-29 01:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [harupy/ruff](https://github.com/harupy/ruff)@[fc94857a20...](https://github.com/harupy/ruff/commit/fc94857a202e43a0a0fa47f972a6807346336046)
#### Sunday 2023-10-29 01:38:55 by Zanie Blue

Rewrite ecosystem checks and add `ruff format` reports (#8223)

Closes #7239 

- Refactors `scripts/check_ecosystem.py` into a new Python project at
`python/ruff-ecosystem`
- Includes
[documentation](https://github.com/astral-sh/ruff/blob/zanie/ecosystem-format/python/ruff-ecosystem/README.md)
now
    - Provides a `ruff-ecosystem` CLI
- Fixes bug where `ruff check` report included "fixable" summary line
- Adds truncation to `ruff check` reports
    - Otherwise we often won't see the `ruff format` reports
- The truncation uses some very simple heuristics and could be improved
in the future
- Identifies diagnostic changes that occur just because a violation's
fix available changes
- We still show the diff for the line because it's could matter _where_
this changes, but we could improve this
- Similarly, we could improve detection of diagnostic changes where just
the message changes
- Adds support for JSON ecosystem check output
    - I added this primarily for development purposes
- If there are no changes, only errors while processing projects, we
display a different summary message
- When caching repositories, we now checkout the requested ref
- Adds `ruff format` reports, which format with the baseline then the
use `format --diff` to generate a report
- Runs all CI jobs when the CI workflow is changed

## Known problems

- Since we must format the project to get a baseline, the permalink line
numbers do not exactly correspond to the correct range
- This looks... hard. I tried using `git diff` and some wonky hunk
matching to recover the original line numbers but it doesn't seem worth
it. I think we should probably commit the formatted changes to a fork or
something if we want great results here. Consequently, I've just used
the start line instead of a range for now.
- I don't love the comment structure — it'd be nice, perhaps, to have
separate headings for the linter and formatter.
- However, the `pr-comment` workflow is an absolute pain to change
because it runs _separately_ from this pull request so I if I want to
make edits to it I can only test it via manual workflow dispatch.
- Lines are not printed "as we go" which means they're all held in
memory, presumably this would be a problem for large-scale ecosystem
checks
- We are encountering a hard limit with the maximum comment length
supported by GitHub. We will need to move the bulk of the report
elsewhere.

## Future work

- Update `ruff-ecosystem` to support non-default projects and
`check_ecosystem_all.py` behavior
- Remove existing ecosystem check scripts
- Add preview mode toggle (#8076)
- Add a toggle for truncation
- Add hints for quick reproduction of runs locally
- Consider parsing JSON output of Ruff instead of using regex to parse
the text output
- Links to project repositories should use the commit hash we checked
against
- When caching repositories, we should pull the latest changes for the
ref
- Sort check diffs by path and rule code only (changes in messages
should not change order)
- Update check diffs to distinguish between new violations and changes
in messages
- Add "fix" diffs
- Remove existing formatter similarity reports
- On release pull request, compare to the previous tag instead

---------

Co-authored-by: konsti <konstin@mailbox.org>

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[9cf089361e...](https://github.com/DATA-xPUNGED/DataStation/commit/9cf089361e8cea86d2415de0535b1a28f517e040)
#### Sunday 2023-10-29 02:10:31 by Rhials

Abandoned Domains: Adds two new psyker-oriented virtual domains (#78892)

## About The Pull Request

_Really? Bitrunning maps are so simple you could do them with your eyes
closed? Hmmmmm..._

This adds two new medium-difficulty virtual domains to the pool -- Crate
Chaos and Infected Domain.

These two domains take you to neglected corners of the virtual world.
These are unstable, bizarre locales that do not support the bitrunning
machine's visual display, and must be traversed using echolocation.
**_These domains have been designed around you being a psyker, and will
turn your bitrunner avatar into a psyker until they leave the domain._**

_**Crate Chaos:** Low cost, medium reward._

Sneak into an abandoned virtual domain, where they store all of the loot
crates. There's about 40-ish crates in this space, and one of them
(RANDOM) is the encrypted cache we're looking for. The crates must be
manually inspected, requiring you to drop your weapon for a few moments,
but that shouldn't be a problem. There's no hostiles, just a bunch of
crates... right?

This one has very few shenanigans or threats in it. It's meant to be an
introductory experience to interfacing with things as a psyker, and
getting the rhythm down for moving between visual pulses.

_**Infected Domain:** Medium cost, high reward._

Enter another abandoned virtual domain. This one was sealed off from the
digital world after the cyber-police failed to contain a virus that
zombified its inhabitants, leaving it to grow unstable and full of
holes. Fortunately, you're provided with the single best tool for arming
yourself against zombies in any video game, ever -- Your very own
Mystery Box. Get armed with (basically) whatever gun you want, and go
put those wacky psyker abilities to use against those zombies.

This one is a lot meaner. Many chasms, landmines, and zombies. Walk
slowly, stay with your fellow bitrunners, and if it's too hard, there's
no shame in going back and rolling for a better gun!

The domains themselves are VERY simple, since there's little need for
decor or particularly complex layouts. The idea is that you should be
able to see everything you need to see in a given room/area with a
single vision pulse. Here's what one of the maps looks like:


![image](https://github.com/tgstation/tgstation/assets/28870487/fe63adce-aa05-4339-9d19-28ce06a2d31f)

Err, uh, I mean... This is what the maps look like:

<details>
<summary>SPOILERS BEWARE</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/28870487/265ecdc5-50f6-4a28-8068-fab08ae1f5e8)


![image](https://github.com/tgstation/tgstation/assets/28870487/0b41da6a-e018-4434-9368-6daee1f97fe9)

(You wanna find out if there's something cool under those red lines? Go
there yourself!)

</details>

These two psyker maps come with their own psyker safehouse too -- The
Bathroom. It's gross, the medical supplies are kind of just sitting
there on the floor... It looks a little bit better when you're blind, I
guess.


![image](https://github.com/tgstation/tgstation/assets/28870487/a10b70bb-5586-4d37-bbb1-a642d8524d54)
## Why It's Good For The Game

I like psykers a lot more than I'm willing to admit. Unfortunately, the
jankiness of echolocation provides such a disadvantage at times, that
any "real" conflict is usually over before the psyker is even aware
they're taking damage.

Fortunately, the controlled environments that bitrunning maps are
perfect for psykers. They give the opportunity to craft an experience
around the player being blind, rather than forcing them to play blind
through a seeing mans world.

These two domains should present players with a unique challenge that is
designed around playing as a psyker, with slightly higher-than-usual
rewards for their trouble. More importantly -- They're fun!
## Changelog
:cl: Rhials
add: Two new psyker-oriented virtual domains -- Crate Chaos and Infected
Domain.
add: Map helper for cyber-police corpse spawn.
add: Map helper for swapping the encrypted crate in an area with a
random crate from that same area.
/:cl:

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[66f726dfe3...](https://github.com/DATA-xPUNGED/DataStation/commit/66f726dfe31dae0a14feaed8718c41e40e82af09)
#### Sunday 2023-10-29 02:10:31 by SyncIt21

General code maintenance for rcd devices and their DEFINE file (#78443)

## About The Pull Request
The changes made can be best summarized into points

**1. Cleans up `code/_DEFINES/construction.dm`**

Looking at the top comment of this file 

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L1

One would expect stuff related to materials, rcd, and other construction
related stuff. Well this file is anything but

Why is there stuff related to food & crafting over here then?

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L91-L94

It gets worse why are global lists declared here?

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L115
There is a dedicated folder to store global lists i.e.
`code/_globalvars/lists` for lists like these. These clearly don't
belong here

On top of that a lot of construction related defines has been just
dumped here making it too large for it's purposes. which is why this
file has been scraped and it's
1. crafting related stuff have been moved to its
`code/_DEFINES/crafting.dm`
2. global lists for crafting moved to
`code/_globalvars/lists/crafting.dm`
3. Finally remaining construction related defines split apart into 4
file types under the new `code/_DEFINES/construction` folder
- `code/_DEFINES/construction/actions.dm` -> for wrench act or other
construction related actions
- `code/_DEFINES/construction/material.dm` -> contains your sheet
defines and cable & stack related values. Also merged
`code/_DEFINES/material.dm` with this file so it belongs in one place
- `code/_DEFINES/construction/rcd.dm` -> dedicated file for everything
rcd related
- `code/_DEFINES/construction/structures.dm` -> contains the
construction states for various stuff like walls, girders, floodlight
etc

By splitting this file into multiple meaningful define file names will
help in reducing merge conflicts and will aid in faster navigation so
this is the 1st part of this PR

**2. Debloats the `RCD.dm` file(Part 1)**

This uses the same concepts as above. i.e. moving defines into their
appropriate files for e.g.

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L170

1. Global vars belong in the `code/_globalvars` folder so these vars and
their related functions to initialize them are moved into the
`code/_globalvars/rcd.dm` file
2. See this proc

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L200
This proc does not belong to the `obj/item/construction/rcd` type it's a
global "helper function" this is an effect proc as it creates rcd
holograms so it has been moved to the `code/game/objects/effects/rcd.dm`
file which is a global effect that can be used by anyone

And with that we have moved these vars & procs into their correct places
& reduced the size of this file . We can go even further

**3. Debloats the `RCD.dm` file(Part 2)**
This deals with the large list which contains all the designs supported
by the RCD

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L42

This list contains a lot of local defines. We can scrape some of them
and reduce the overall bulkiness & memory requirements of this list and
so the following defines

```
#define WINDOW_TYPE "window_type"
#define COMPUTER_DIR "computer_dir"
#define WALLFRAME_TYPE "wallframe_type"
#define FURNISH_TYPE "furnish_type"
#define AIRLOCK_TYPE "airlock_type"
#define TITLE "title"
#define ICON "icon"
#define CATEGORY_ICON_STATE  "category_icon_state"
#define CATEGORY_ICON_SUFFIX "category_icon_suffix"
#define TITLE_ICON "ICON=TITLE"
```

Have all been removed making this list a lot more cleaner. Why? because
a lot of these are just semantic sugar, we can infer the value of a lot
of these defines if we just know the type path of the structure the rcd
is trying to build for e.g. take these 2 defines

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L13-L15

These defines tell the rcd UI the name and the icon it should display.
Rather than specifying these manually in the design we can infer them
like this

```
var/obj/design = /obj/structure/window  //let's say the rcd is trying to build an window
var/name = initial(design.name)         //we have inferred the name of the design without requiring TITLE define
var/icon = initial(design.icon_state)   //we have inferred the icon of the design without requiring ICON define
```

And so by using similar logic to the remaining defines we can eliminate
a lot of these local defines and reduce the overall size of this list.

The same logic applies to the different modes of construction, the
following defines

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L186-L192
Have all been removed and replaced with a single value `RCD_STRUCTURE`

All these modes follow the same principle when building them
1. First check the turf if the structure exists. If it does early return
2. If not create a new structure there and that's it

So rather than creating a new construction mode every time you want to
add a new design we can use this mode to apply this general approach
every time

The design list has also now been made into a global list rather than a
private static list. The big advantage to this is that the rcd asset
cache can now access this list and load the correct icons from the list
directly. This means you no longer have to manually specify what icons
you want to load which is the case currently.

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/modules/asset_cache/assets/rcd.dm#L8-L9
This has lead to the UI icons breaking twice now in the past
- #74194
- #77217

Hopefully this should never repeat itself again

**4. Other RCD like device changes**
- Fixed the broken silo link icon when the radial menu of the RLD was
opened
- replaced a lot of vars inside RLD with defines to save memory
- Small changes to `ui_act` across RCD, Plumbing RCD and RTD
- Removed unused vars in RCD and snowflaked code
- Moved a large majority of `ui_data()` to `ui_static_data()` making the
experience much faster

Just some general clean up going on here

**5. The Large majority of other code changes**
These are actually small code changes spread across multiple files.
These effect the `rcd_act()` & the `rcd_vals()` procs across all items.
Basically it
- Removes a large majority of `to_chat()` & `visible_message()` calls.
This was done because we already have enough visual feedback of what's
going on. When we construct a wall we don't need a `to_chat()` to tell
us you have a built a wall, we can clearly see that
- replaces the static string `"mode"` with a predefined constant
`RCD_DESIGN_MODE` to bring some standard to use across all cases

Should reduce chat spam and improve readability of code. 

**6. Airlock & Window names**
The rcd asset cache relies on the design name to be unique. So i filled
in the missing names for some airlocks & windows which are subjective
and open to change but must have some value

**7 Removes Microwave PDA upgrade**
The RCD should not be allowed to build this microwave considering how
quickly it can spawn multiple structures and more importantly as it's a
special multipurpose machine so you should spend some effort in printing
it's parts and acquiring tools to complete it. This upgrade makes
obsolete the need to carry an
- A RPED to install the parts
- A screwdriver to complete the frame
- The circuit board for the microwave 

The most important point to note here is that whenever an RPED/circuit
board is printed at an lathe it charges you "Lathe Tax". The RCD with
this upgrade would essentially bypass the need to "Pay Taxes" at these
lathes as you are just creating a circuit board from thin air. This
causes economy imbalance(10 cr per print) which scales up the more of
these machines you make so to avoid this let's end the problem here

Not to mention people would not find the need to print the circuit board
for a regular microwave now if they have an RCD because they can just
make this microwave type making the need for a regular microwave
completely pointless.

Just build a machine frame with the RCD and complete the microwave from
there

## Changelog
:cl:
code: moved global vars, lists and helper procs for construction related
stuff to their appropriate files
code: reduced overall code size & memory of rcd design list and removed
unused defines
refactor: removed a ton of chat alerts for rcd related actions to help
reduce chat spam
refactor: some airlock & window default names have changed
fix: broken icon in radial menu of rld silo link
remove: removes microwave pda upgrade from RCD. It's a special machine
so spend some time in building it rather than shitting them out for free
with the RCD. Use the RCD upgrade to spawn a machine frame instead & go
from there
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [veggiemike/openrvdas](https://github.com/veggiemike/openrvdas)@[64b9aa5590...](https://github.com/veggiemike/openrvdas/commit/64b9aa5590e25df0459e6104ad39a53891eab6a1)
#### Sunday 2023-10-29 02:33:36 by Michael D Labriola

UDPReader: increase READ_BUFFER_SIZE and remove `read_buffer_size` param

The UDP header's `length` field sets a theoretical limit of 65,535 bytes
(8-byte header + 65,527 bytes of data) for a UDP datagram.  Technically,
IPV4 or IPv6 headers use up some of that size, so actual maximum data sent
per datagram is slightly less.

UDP receivers should always request the max, though, because if you request
less than what's on the wire, you get what you asked for and the rest gets
tossed on the floor.  There's no built-in error detection/correction in
UDP, so that's unrecoverable data loss.

My testing in python shows that you can recv() w/ pretty much any
ridiculously silly large number (655350, aka 10x the max size) on both
Linux and Mac.  We'll have to put some logic into UDPWriter and TCPWriter,
though, because send() is where we run into real-life limits (as opposed
to "theoretical" ones).

Given all that, allowing users to configure the read size via the
`read_buffer_size` parameter is a bad idea: it just allows them to break
things.  So this commit also removes that.

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[eb28d04f08...](https://github.com/TheBoondock/tgstation/commit/eb28d04f08a172c3bf671747072e1120b8e43d21)
#### Sunday 2023-10-29 02:50:19 by Jacquerel

Watcher Nest Lavaland Ruin (#78790)

## About The Pull Request

Adds a small new lavaland ruin, the Watchers' Grave.


![image](https://github.com/tgstation/tgstation/assets/7483112/9c3fa6f0-3e7d-4540-8646-5229eb11445b)

![image](https://github.com/tgstation/tgstation/assets/7483112/93bc14f0-9a0c-40d3-bd30-cc79a0d85752)

You will need to figure out yourself how to find a way through the walls
surrounding it (it's not very hard).
This is mostly just atmospheric but also serves as a delivery vehicle
for a unique item; an orphaned Watcher egg.
(That's kind of it in terms of loot, unless you count a handful of
lavaland mob corpses and mushrooms).

You can either eat this (it's an egg), throw it at someone to spawn an
angry watcher, or keep hold of it for a while and see what happens.

<details>


![dreamseeker_cMNnZXjfgL](https://github.com/tgstation/tgstation/assets/7483112/841db8fc-19ac-431f-aa66-c9ec5fbedbc3)

That's right it's your very own baby watcher.
It orbits your head and shoots at lavaland creatures for unimpressive
damage. It won't ever intentionally shoot a player but they might walk
in front of it, as it doesn't hurt very much they will probably forgive
you.
If you die it will continue circling your corpse to guard it against
predation.
</details>

In creating this ruin I also added a new component called "corpse
description".
It provides some extra examine text to a corpse which is removed
permanently if the mob is revived.
There's a field you can varedit on corpse spawners (or make a subtype)
which will automatically apply it to spawned corpses.
You can use it for environmental storytelling. Or admins can use it to
make fun of how you died.

Also I fixed basic mobs runtiming when examined by ghosts.

## Why It's Good For The Game

More variety in map generation. It's cute.
Adds a tool that mappers might like.

## Changelog

:cl:
add: Adds a new lavaland ruin where you can find a unique egg.
/:cl:

---
## [SobiiZXrd/Ensnared](https://github.com/SobiiZXrd/Ensnared)@[dffe9831fd...](https://github.com/SobiiZXrd/Ensnared/commit/dffe9831fd02b181235fa369889305d449e44f5a)
#### Sunday 2023-10-29 03:15:14 by Joseph Sobrino-Torres

Working on Ensnared:

1. Created the BP_SiameseDemon avatar actor.
2. Created the BT_SiameseDemon iteration of the modular Behavior Tree we've had ready to implement all of the demons/horrors in the world.
3. Created the Attack, Increment Patrol, Clear Patrol, Set Speed, and Increment Patrol tasks/services specifically for the Siamese Demon.
4. The Siamese Demon, Ghouly Ghast Horror, Gruum Horror, Sacrifieced Cultist, and Clot Worm are now ready to be used in the world, will attack and chase the player as well as patrol according to preset vectors set in their personal patrol components.
5. Set up the spook collision to now get this actor's currently overlapped instance's transform then sets the player's RespawnTransform variable inside the BPGM_Ensnared  Game Mode which upon validating the player has died according to a bIsDead? boolean set inside the player's animBP, will wait 10 seconds and transport the player whilst resetting the player's life, as well as animation instance back to functional so the player may give killing the demon that killed them another try. ----> (THANK YOU TRAVIS!! -- This was done with the help of Travis Dolan)

---
## [cdb-is-not-good/sojourn-station](https://github.com/cdb-is-not-good/sojourn-station)@[10b827477c...](https://github.com/cdb-is-not-good/sojourn-station/commit/10b827477c429e6e26a6a1f43890061946d96d3f)
#### Sunday 2023-10-29 04:04:43 by CDB

Buffs the fenrir a bit.

To compensate for the fact that it is A. rare as hell B. incredibly difficult to use(slowdown, needs to be braced, slow to wield) the Fenrir has been given back its old 1.2 damage value.

Fenrir has also been given 25% less recoil to *try* to make it less sillymode, it's still largely going to require bracing but should now at least be useable

Kills handholding. Guns will no longer complain at you when fired without brace/wielding. Mostly, this is because these messages happening repeatedly was causing lag for some players(I can't confirm if this was due to the messages themselves, or because every single shot ran through an extra set of switches to determine what message to print/roll dice to see if it even prints a message). If people REALLY want, we can add them back later.

---
## [Jureiia/Skyrat-tg](https://github.com/Jureiia/Skyrat-tg)@[ac7ddd1dcc...](https://github.com/Jureiia/Skyrat-tg/commit/ac7ddd1dcca30af6f86fce6ed858de414e7426c4)
#### Sunday 2023-10-29 04:12:56 by SkyratBot

[MIRROR] ArCargo: Adds the Galactic Materials Stock Market V1.2 (Free Market Edition) [MDB IGNORE] (#24038)

* ArCargo: Adds the Galactic Materials Stock Market V1.2 (Free Market Edition) (#78500)

## About The Pull Request

**This PR is a rerelease of #78164, with some bells and whistles.** As
such, most of the core functionality is the same, but with some tweaks
to balance the gameplay and prevent bike levels of profit. I've tried to
bold the new additions to make it easier to read for those coming back
for the second pass.

![image](https://github.com/tgstation/tgstation/assets/41715314/ff9bf038-524d-44fc-81bb-c6ff97fef6dd)
This PR adds a new machine that can be bought called the **Galactic
Mineral Market** (GMM). The Galactic Mineral Market (GMM) allows you to
buy and sell minerals wholesale from the market machine. It goes
something like this:

### 1. Getting the Machine:
The GMM can be bought as an un-assembled machine for 600 credits from
cargo. It's a low cost, but its not mapped in standard, so if you're
confident in your miners, you shouldn't necessarily need one for the
department. Otherwise, it's available for other crewmembers to buy for
cost.

The cargo pack comes will all supplies necessary to finish the machine.
Tools not included.

### 2. Buying Low
Using the machine's UI, you can see all traded minerals and their
associated prices. Buy prices are played straight, and can be bought for
material price, times the quantity. The order is then instantly placed
on the cargo shuttle, and will be deducted from the buyer's account on
shuttle send. **A single order can only have 10 different stacks of
materials in it. So, that can be 100 sheets of iron and 1 of everything
else, or 500 sheets of iron. After that you're blocked from buying more
sheets until you've sent the order.**

Cargo staff with standard cargo access may toggle the machine to order
directly from the cargo budget. Otherwise, materials are only purchased
from private accounts.

All purchases are treated as private and must be opened by the recipient
like private orders.

### 3. Selling High

It's stocks time. To sell minerals on the market, simply insert any
relevant metal stock into the machine. This produces a totally original
and not-a-bounty-cube stock block, which can be sold on the cargo
shuttle for cargo funds. Stock blocks can also be price-tagged as well
following their standard process.

**Stock blocks start out a bright pink and are worth the value of that
material at that time, but over time their color will degrade. After a
full 5 minutes, stock blocks will switch over to a purple hue, and their
value will once again become liquid, subject to the current market
value. This encourages players to be a bit more fast on their feet than
before instead of just waiting forever for all of their investments to
arrive at the perfect value, before the inevitable "rest of the game"
tries to upend your investing.**

Sold cargo stocks are subject at a 20% processing fee as part of the
galactic mineral market.
### 4. Outside Factors

**In-game events like the Crab-17 or the Market crash event will cause
stocks to bottom out completely, and for the market to become
unavailable until the market stabilizes. Thankfully, once the market has
crashed, typically stocks will recovery and gain back some value,
allowing for fast acting market movers to capitalize on rough markets.**

**Additionally, low value materials like iron and glass have an extra
stipulation, as their value goes all the way down to 0 credits. In that
case, you are unable to buy them at that value as a market protection.
Be careful that you don't see a reset or crash when you're planning on
selling your horde of iron and glass stocks!**

Additionally, market events can occur during the round that can more
sharply adjust a single stock's price and completely rebound it's
trajectory. These events are always mentioned in the station
announcement's economics report.

### Other notes:
The market does not cover all minerals, partially for consistency
purposes as well as for balance reasons. Plasma, being a unique material
that only Nanotrasen has their hands on, is the sole exporter of plasma
in the system, so it stands to reason that it's not on the market, and
remains a solo export. Bananium, as it has a rare and expensive
conversion rate, works the opposite way, and as such isn't listed on the
market either, with the sole source being single cargo sales. All others
just don't make much sense to include into the market at this second, so
I left them out for now.

**Alright now below I'm going to cover the math and shit so if that's
not what you care about then please scroll past.**
<details>
  <summary>Warning: Arcane is about to talk about the math</summary>
Alright.
So this adds a new stock_market subsystem, which fires once every 20
seconds. I'm still fairly new to subsystem design so I'm probably going
to need some feedback on cleaning this up to make it look nicer and run
smoother.

So we have 4 associated lists, each attached to the relevant traded
datum; this tracks prices, market trends, how long that trend is going
to last in SS fires, and market quantity.

Prices fluctuate between 0.5x and 3x the material's single sheet value.
This could be tweaked even farther in the future, but for now I'm
keeping it at this nice clean margin. Prices fluctuate based on a
gaussian normal distribution that is centered on different points based
on their **trend**. Upward trending materials are centered in such a way
that they'll almost certainly go upwards, but being that it's based on a
random chance, not always. Vis versa, downward trends should tend to
lose value at about the same rate. We also change our rounding based on
this trend data, in order to prevent low price values like iron and
glass from getting stuck in the same value or freefall drop over time
just because of rounding down. Similarly, neutral trending materials
will not change nearly as much, and will generally stay at around the
same amount.

When buying or selling a material, the quantity of that material will
change on the market. The magnitude of that change depends on how much
of that material currently exists on the market. Buying a low quantity
material like diamond for example will tangibly increase that material's
cost, while buying stacks and stacks of iron and glass won't do much
damage to the price of iron as there's usually around 500 full stacks on
the market to start with. It's applied at a relative percentage of
(qty_changed / new_total_on_market) * price of goods bought/sold at.

In addition to that, there are random "market events" that can occur
randomly, which you might miss if you don't follow the newscaster
economy news. These three events are fairly barebones now, but in
general they have a 1% chance of happening per material, and can more
dramatically increase, decrease, or fully reset the value of a material
on the market back to it's standard value. This opens up for doing more
with it in the future, but that's a later problem.
</details>

## Why It's Good For The Game

This independently resolves some issues related to #78040, that being
that lowpop stations, or shifts with few miners would have a new way to
be able to still get some access to minerals in a given round. This also
provides a unique minigame and alternative way to acquire money in a
given shift, using minerals.

**"But Arcane,** I hear you ask. **"Isn't this just the same thing you
tried doing way back when and then reverted in #50537?**
Well, fuck man, how you doing I haven't see you around in forever also
no you're completely wrong and here's why

**This PR is no longer contingent on the rest of ArcMining in it's
current iteration.** I have introduced some extra factors into the
gameplay as well to try and curb the creation of bikes within gameplay.
This also provides a massive benefit to round progression and gives the
QM and the cargo members the ability to prevent round progress from
stalling by buying round-critical resources.

Not to mention, as the GMM is not cargo required, more cargo integrated,
it also functions as economy content for the rest of the crew.

## Changelog
:cl:
add: A new export has arrived in the imports section, the Galactic
Materials Market! You can use this to buy and sell minerals for profit
or cost, as well as stock your station when you don't have any miners.
add: Insert sheets of minerals into the Galactic Materials Market to
convert them into a stock block, allowing you to lock in your price for
5 minutes. Wait too long and it'll be subject to market value again!
add: Minerals can be bought on the market either using the station's
cargo budget by cargo crew, or privately by everyone else.
del: Any material stacks that can be bought and sold on the market
before have been removed from the cargo catalog.
/:cl:

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@ users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@ users.noreply.github.com>

* ArCargo: Adds the Galactic Materials Stock Market V1.2 (Free Market Edition)

---------

Co-authored-by: ArcaneMusic <41715314+ArcaneMusic@users.noreply.github.com>
Co-authored-by: Jeremiah <42397676+jlsnow301@ users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@ users.noreply.github.com>

---
## [veggiemike/openrvdas](https://github.com/veggiemike/openrvdas)@[72a3c7e22c...](https://github.com/veggiemike/openrvdas/commit/72a3c7e22cf1ab7a00b9f861b777d9759ba16aa9)
#### Sunday 2023-10-29 04:28:21 by Michael D Labriola

UDPReader: increase READ_BUFFER_SIZE and remove `read_buffer_size` param

The UDP header's `length` field sets a theoretical limit of 65,535 bytes
(8-byte header + 65,527 bytes of data) for a UDP datagram.  Technically,
IPV4 or IPv6 headers use up some of that size, so actual maximum data sent
per datagram is slightly less.

UDP receivers should always request the max, though, because if you request
less than what's on the wire, you get what you asked for and the rest gets
tossed on the floor.  There's no built-in error detection/correction in
UDP, so that's unrecoverable data loss.

My testing in python shows that you can recv() w/ pretty much any
ridiculously silly large number (655350, aka 10x the max size) on both
Linux and Mac.  We'll have to put some logic into UDPWriter, though,
because send() is where we run into real-life limits (as opposed to
"theoretical" ones).

Given all that, allowing users to configure the read size via the
`read_buffer_size` parameter is a bad idea: it just allows them to break
things.  So this commit also removes that.

---
## [xjason321/indect-id](https://github.com/xjason321/indect-id)@[9d7737bf0f...](https://github.com/xjason321/indect-id/commit/9d7737bf0f43038bd7f08f2a5600fd6ab8a07499)
#### Sunday 2023-10-29 04:43:29 by georgewang2008

George, fixed dict, jason should stop using chatgpt

fuck you jason

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[617714eba5...](https://github.com/ARF-SS13/coyote-bayou/commit/617714eba525e77a2a408a83247c9ea7062bca33)
#### Sunday 2023-10-29 04:45:06 by Lynx

Mapping - Foliage Galore

Added more foliage! More and more! Also changed the back entrance into the tribal camp.

FUCK MORE MAPPING!

WAY MORE THAN I CAN LIST!

4? Ish? Ends of roads have been altered to blend more realistically with its surroundings at the start of nash.

Scug area has been toned down in its super duper high fantasy stuff for something more tame; yet magical.

Tribal camp has a little 1 tile extenstion to be in line with the northern tower.

NAsh has a TON of plants.

UNDERGROUND got changes

Fixed one spot in tribal area to avoid random get at the gate for the garden.

---
## [yiyaxueyv/YgoMaster](https://github.com/yiyaxueyv/YgoMaster)@[499f9df4f3...](https://github.com/yiyaxueyv/YgoMaster/commit/499f9df4f3cf57e13dd2a9080de6d7ee5f4b7b54)
#### Sunday 2023-10-29 04:50:21 by pixeltris

2023-08-17 - 2023-08-29 updates

2023-08-17
- Shop accessories "Foolish Burial" (field part), "Green Stone of Magic" (mate base)

2023-08-29
- Secret pack "Beastly Claws of Terror"
- Selection pack "Inherited Unity"
- Solo gate "And the Crowd Goes Wild!"
- Shop accessories "Black Luster Soldier - Legendary Swordsman" (sleeve), "Red-Eyes Black Dragon" (icon), "DARK" (icon frame), "DARK" (deck case)

Misc:
- 40 new cards

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[0c55aebcae...](https://github.com/EaW-Team/equestria_dev/commit/0c55aebcae844d845ab72d6a9fc2e428290d6d59)
#### Sunday 2023-10-29 04:53:50 by Mustafa Alperen Seki

Actually add the FAT female generics.

My stupid ass saved them to wrong place and forgor to copy them to the repo, my fault not resting it.

---
## [Lagomorphica/CMSS13](https://github.com/Lagomorphica/CMSS13)@[3e9d54628d...](https://github.com/Lagomorphica/CMSS13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Sunday 2023-10-29 05:32:43 by Ben

Can no longer bypass Lesser Drone Limit (#4034)

# About the pull request

Users can no longer keep menu open and bypass lesser drone slots

# Explain why it's good for the game

Honestly kinda wish I didn't make this one, infinite lesser drones
sounds really funny.

# Changelog
:cl:
fix: You can no longer circumvent the lesser drone limit by keeping the
prompt open.
/:cl:

---
## [Ishansourav/Web-Developing](https://github.com/Ishansourav/Web-Developing)@[8335dde095...](https://github.com/Ishansourav/Web-Developing/commit/8335dde095d4368ea18e9147dfd30700515d8290)
#### Sunday 2023-10-29 05:55:59 by Sourav Ishan

Netfilx-Clone

This is the core code from scratch to clone the landing page of netflix using html5 , css &  javascript.


Unleash entertainment with our #NetflixClone: sleek, user-friendly, and personalized. Enjoy seamless streaming on any device, with multiple profiles and a dark mode for your late-night fix. Dive into a vast content library and subscribe to your perfect plan. Join us for a world of entertainment! #StreamingService #BingeWatching #EntertainmentHub

---
## [NavinKumar77/NavinKumar](https://github.com/NavinKumar77/NavinKumar)@[4f536610c8...](https://github.com/NavinKumar77/NavinKumar/commit/4f536610c8743f7e94fc489bbd2a9b914ff7399d)
#### Sunday 2023-10-29 06:04:58 by Navinkumar

Update README.md

👋 Hello, world! I'm a tech enthusiast with a keen interest in the field of Data Analysis and Web Development. I love diving deep into data, uncovering insights, and using them to drive decision-making.

💻 On the development side, I'm proficient in Angular, HTML, CSS, and JavaScript. I enjoy creating intuitive and dynamic user experiences on the web.

🌱 I'm constantly learning and adapting to new technologies to stay at the forefront of the rapidly evolving tech industry. Looking forward to contributing to and collaborating on exciting projects!

---
## [dgp1130/rules_prerender](https://github.com/dgp1130/rules_prerender)@[cb50a2d9d9...](https://github.com/dgp1130/rules_prerender/commit/cb50a2d9d9a372dca515ccc392a227fe61693e93)
#### Sunday 2023-10-29 06:30:11 by Doug Parker

Animates nav pane in and out.

This was tricky to get right, but I think it's in a good state. A couple key learnings here:
1. `transition` feels easier to use than `@keyframes` because it automatically supports animating in and out of a state without needing a second keyframe or attempting to run an existing one backwards.
2. `transition` doesn't appear to trigger on page load which is very nice.
3. I initially tried animating the nav pane to `width: 0;`, but getting everything else to lay out correctly was difficult. Turns out animating `grid-template-columns` is supported and works very smoothly.
4. You cannot animate `grid-template-columns` into/out of `auto`, which is very frustrating. I decided to hard-code 300px as the nav pane width (previously the `max-width`), which I'm not a fan of. However given that the nav pane will have a static set of items, I think this is a constraint I can live with.
5. `grid-template-columns` is very strict on its units for animations. You cannot animate from `0` to `1fr`, but you can animate from `0fr` to `1fr`. https://theadhocracy.co.uk/wrote/the-trick-to-animating-grid-columns
6. More annoying, the `>` expando would line-wrap as the nav pane shrunk. This was very difficult to prevent because it is a unique element (not text in an existing element I could put `white-space: nowrap;` on). My workaround was to set the hard-coded width `300px` on the text container (the button) and apply `overflow-x: hidden;`. The fixed width means that as the scroll bar shrinks, the button actually does not, so the `>` character never needs to line wrap. It's hacky for sure, but we need the `overflow-x: hidden;` anyways, so it's not that big a deal.

---
## [TonyAkinsWritesCrypto/zechub](https://github.com/TonyAkinsWritesCrypto/zechub)@[157cf0fa56...](https://github.com/TonyAkinsWritesCrypto/zechub/commit/157cf0fa56af1432234b58cc219688de92cc12f8)
#### Sunday 2023-10-29 07:40:10 by TonyAkinsWritesCrypto

ZecWeekly66 

# ZecWeekly (Episode 66)


The Zebra book, Zcash enhanced privacy, ZecHub Extras, Zcash 7th Anniversary , Ywallet Upgrade. 


Curated by "TonyAkins"[TonyAkin01](https://twitter.com/TonyAkins01))

---

#### Welcome to ZecWeekly Episode 66


Welcome to the thrilling episode of ZecWeekly, as we explore Zcash's implementation of FROST using Schnorr , Zcash 7th Anniversary celebrated with lots of merches and prizes, release of Zebra updated 1.3.0, and the introduction of UniFFi for Developer's use cases. 

–
### This Week Education's Pieces.

This week's education pieces will educate and refine us with all details about Zcash addresses, both shielded and transparent addresses and other the latest development in the Zcash payment system. 

Click  the link below to access the resource :

https://wiki.zechub.xyz/visualizing-zcash-addresses




### Zcash Updates

Zcash and ECC updates. 

[NowNodes features Zcash for upgraded Privacy ecosystem](https://twitter.com/NOWNodes/status/1716463761777680713)

[Ywallet Zcash Ledger app on Nano S Plus w/ Orchard tx](https://www.youtube.com/watch?v=HRVNpDDoh1Y&t=34s) 

[Zcash Digitals Decentralized](https://twitter.com/ElectricCoinCo/status/1717570088771952811)

[tECC DAYS 2023 celebrated](https://twitter.com/ECCIntegrator/status/1718035043736547504)


[Announcing Zebra 1.3.0](https://twitter.com/ZcashFoundation/status/1716524342853476576)

[Implementation of UniFFi on Zcash Network](https://twitter.com/eiger_co/status/1716801431510851824)

[Zcash SDK fixes now live](https://twitter.com/EdgeWallet/status/1716530980499128578)

#### Zcash Community Grants Updates

[WalletD Community Grant Application](https://forum.zcashcommunity.com/t/walletd-community-grant-application/45876?utm_source=dlvr.it&utm_medium=twitter)

[Security assessment for Zcash FROST published](https://twitter.com/ZecHub/status/1716930299140169764)

[Zcash Community funded @eiger_co to create UniFFi library](https://twitter.com/ZcashCommGrants/status/1717273970922123392)

#### Community Projects

[Zcash 7th Anniversary celebrated in grande style](https://free2z.cash/ZecHub/zpage/zcash-7th-anniversary-challenge)

[Post Comments on Free2Z using Zenith CLI! Go check it out!](https://www.youtube.com/watch?v=HtorP8TJ5vk)

#### News & Media

[Binance founder CZ’s fortune gets slashed $12B, while SBF is still at $0](https://cointelegraph.com/news/binance-ceo-changpeng-zhao-fortune-slashed-billionaires-index)

[Google to invest another $2B in AI firm Anthropic: Report](https://cointelegraph.com/news/google-to-invest-another-two-billion-in-ai-firm-anthropic)

[Kraken to suspend trading for USDT, DAI, WBTC, WETH, and WAXL in Canada](https://cointelegraph.com/news/kraken-suspend-trading-usdt-dai-wbtc-weth-and-waxl-stablecoin-canada)

[AI Girlfriend Amouranth Wants to Use Her 'Vaginal Yeast' to Brew Beer](https://decrypt.co/203517)

[Audits and rug-pulled projects, a $650B token burn, and major DeFi protocol quits UK: Finance Redefined](https://cointelegraph.com/news/audits-and-rug-pulled-projects-a-650b-token-burn-and-major-defi-protocol-quits-uk-finance-redefined)

[Bitcoin's 14% Weekly Gain Signals 'End of an Era' as Big Tech Dumps, Analyst Says](https://www.coindesk.com/markets/2023/10/27/bitcoins-14-weekly-gain-signals-end-of-an-era-as-big-tech-dumps-analyst-says/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[Binance Founder CZ's Wealth Falls About $12B as Trading Revenue Slumps: Bloomberg](https://www.coindesk.com/business/2023/10/27/binance-founder-czs-wealth-falls-about-12b-as-trading-revenue-slumps-bloomberg/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[How major German firms like Mercedes and Lufthansa are using NFTs](https://cointelegraph.com/news/germany-mercedes-lufthansa-nfts)

[ChatGPT creator OpenAI builds new team to check AI risks](https://cointelegraph.com/news/chatgpt-openai-new-team-ai-risks)

[Bitcoin restarting 2023 uptrend after 26% Uptober BTC price gains — research](https://cointelegraph.com/news/bitcoin-2023-uptober-btc-price-research)



## Some Zcash Tweets


[Central bank of Brazil account heard about Zcash today](https://x.com/anarchychains/status/1717288641288921272)

[Happy Birthday Zcash!!!](https://twitter.com/ZforZcash/status/1718085318543376404)

[ZcashFoundation and NCCGroupInfosec conduct a security assessment of the Foundation’s FROST](https://twitter.com/ZcashFoundation/status/1716849796315512935)

[What are Zero-knowledge Proofs](https://twitter.com/NighthawkWallet/status/1717730883933806958)

[Zcash Community Grant minutes](https://twitter.com/ZcashCommGrants/status/1717556482344907090)

[Keep yourself safe from hack with a Zcash wallet](https://twitter.com/NighthawkWallet/status/1717007699592851702)

[Metrics should be updated](https://twitter.com/ZcashForum/status/1716786643171225726)

[Join our UPA friends if you're at EFDevconnect](https://twitter.com/ElectricCoinCo/status/1716886693444530195)


[Social media Data collection, does it matter?](https://twitter.com/ZecHub/status/1716850588942577890)

[Follow NighthawkWallet for crypto privacy education](https://twitter.com/NighthawkWallet/status/1716625185623728248)

[Privacy is normal!](https://twitter.com/ZcashNigeria/status/1716755151497707660)


## Zeme of the Week

[https://twitter.com/ZcashNigeria/status/1718151545324200002](https://twitter.com/ZcashNigeria/status/1718151545324200002)

[https://twitter.com/zcashbrazil/status/1717609507432337754](https://twitter.com/zcashbrazil/status/1717609507432337754)

[https://twitter.com/zcashbrazil/status/1717225798019567621](https://twitter.com/zcashbrazil/status/1717225798019567621)



## Jobs in the Ecosystem

[Zcash needs graphic designers,writers, and privacy advocate in its ecosystem](https://twitter.com/ZecHub/status/1713947885220344234)

[Create Video HOWTO - Setup WSL in windows, and compile lastest zcashd](https://github.com/ZecHub/zechub/issues/567)

---
## [cloudquery/arrow](https://github.com/cloudquery/arrow)@[3beb93af36...](https://github.com/cloudquery/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Sunday 2023-10-29 08:01:33 by Kevin Gurney

GH-37815: [MATLAB] Add `arrow.array.ListArray` MATLAB class (#38357)

### Rationale for this change

Now that many of the commonly-used "primitive" array types have been added to the MATLAB interface, we can implement an `arrow.array.ListArray` class.

This pull request adds a new `arrow.array.ListArray` class which can be converted to a MATLAB `cell` array by calling the static `toMATLAB` method.

### What changes are included in this PR?

1. Added a new `arrow.array.ListArray` MATLAB class.

*Methods*

`cellArray = arrow.array.ListArray.toMATLAB()`
`listArray = arrow.array.ListArray.fromArrays(offsets, values)`

*Properties*

`Offsets` - `Int32Array` list offsets (uses zero-based indexing)
`Values` - Array of values in the list (supports nesting)

2. Added a new `arrow.type.traits.ListTraits` MATLAB class.

**Example**
```matlab
>> offsets = arrow.array(int32([0, 2, 3, 7]))

offsets = 

[
  0,
  2,
  3,
  7
]

>> values = arrow.array(["A", "B", "C", "D", "E", "F", "G"])

values = 

[
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G"
]

>> arrowArray = arrow.array.ListArray.fromArrays(offsets, values)

arrowArray = 

[
  [
    "A",
    "B"
  ],
  [
    "C"
  ],
  [
    "D",
    "E",
    "F",
    "G"
  ]
]

>> matlabArray = arrowArray.toMATLAB()

matlabArray =

  3x1 cell array

    {2x1 string}
    {["C"     ]}
    {4x1 string}

>> matlabArray{:}

ans = 

  2x1 string array

    "A"
    "B"

ans = 

    "C"

ans = 

  4x1 string array

    "D"
    "E"
    "F"
    "G"

```

### Are these changes tested?

Yes.

1. Added a new `tListArray.m` test class.
2. Added a new `tListTraits.m` test class.
3. Updated `arrow.internal.test.tabular.createAllSupportedArrayTypes` to include `ListArray`.

### Are there any user-facing changes?

Yes.

1. Users can now create an `arrow.array.ListArray` from an `offsets` and `values` array by calling the static `arrow.array.ListArray.fromArrays(offsets, values)` method. `ListArray`s can be converted into MATLAB `cell` arrays by calling the static `arrow.array.ListArray.toMATLAB` method.

### Notes

1. We chose to use the "missing-class" `missing` value as the `NullSubstitutionValue` for the time being for `ListArray`. However, we eventually want to add `arrow.array.NullArray`, and will most likely want to use the "missing-class" `missing` value to represent `NullArray` values in MATLAB. So, this could cause some ambiguity in the future. We have been thinking about whether we should consider introducing some sort of special "sentinel value" to represent null values when converting to MATLAB `cell` arrays. Perhaps, something like `arrow.Null`, or something to that effect, in order to avoid this ambiguity. If we think it makes sense to do that, we may want to retroactively change the `NullSubstitutionValue` to be `arrow.Null` and break compatibility. Since we are still in pre-`0.1`, we don't think the impact of such a behavior change would be very large.
2. Implementing `ListArray` is fairly involved. So, in the spirit of incremental delivery, we chose not to include an implementation of `arrow.array.ListArray.fromMATLAB` in this initial pull request. We plan on following up with some more changes to `arrow.array.ListArray`. See #38353, #38354, and #38361.
3. Thank you @ sgilmore10 for your help with this pull request!

### Future Directions

1. #38353
2. #38354
3. #38361
4. Consider adding a null sentinel value like `arrow.Null` for conversion to MATLAB `cell` arrays.
* Closes: #37815 

Lead-authored-by: Kevin Gurney <kgurney@mathworks.com>
Co-authored-by: Sarah Gilmore <sgilmore@mathworks.com>
Signed-off-by: Kevin Gurney <kgurney@mathworks.com>

---
## [Doubleumc/Shiptest](https://github.com/Doubleumc/Shiptest)@[2a74c23d62...](https://github.com/Doubleumc/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Sunday 2023-10-29 08:38:39 by Imaginos16

Nerfs the everloving almighty shit out of the jungle demonic office ruin (#2430)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Nerfs the ruin by removing most of its gamer gear, and changing the
syndicate hardsuit you find into a scarlet hardsuit.


Not to mention the two goddamn deathsquad hardsuits all there,
wholesale, for free.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a8333190-37ce-441f-a746-bb5f2fc26828)

This shit is not okay jesus fucking christ, two deathsquad hardsuits?
Are you insane?
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
balance: The Jungle Demonic Office Ruin has now been appropriately
balanced, now only having a scarlet hardsuit, decent syndicate armor,
and a bulldog with no spare mags.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [saisuseelmohan2003/My-Projects](https://github.com/saisuseelmohan2003/My-Projects)@[8bb7d674c9...](https://github.com/saisuseelmohan2003/My-Projects/commit/8bb7d674c9ca3bbc12142e8c75c093bb36ebcabe)
#### Sunday 2023-10-29 09:06:12 by saisuseelmohan2003

Add files via upload

🔐 Exciting Announcement: I've Created a Powerful Password Generator! 🔐

In today's digital age, protecting our online accounts is more crucial than ever. That's why I'm thrilled to share my latest project with you: a robust and secure password generator that creates virtually unhackable passwords! 💪🔒

Key Features:
✅ Strength and Security: My password generator creates strong, complex passwords that are virtually impossible to crack through brute force or dictionary attacks.
✅ Customization: You can tailor passwords to your specific requirements, making them perfect for different online accounts.
✅ Easy to Use: It's user-friendly and accessible for everyone, ensuring that you can create strong passwords without any hassle.
✅ Open Source: I believe in the power of collaboration, so I've made this tool open-source for the community to benefit from and contribute to its ongoing development.

As cyber threats continue to evolve, it's essential to take our digital security seriously. With this password generator, you can rest assured that your online accounts are well protected.

I'm excited to share this project with you, and I'd love to hear your thoughts and feedback!

---
## [QWOD/RESEARCH](https://github.com/QWOD/RESEARCH)@[a609997984...](https://github.com/QWOD/RESEARCH/commit/a609997984a50adc5dc3cc8c8f2bae56ca7bb31e)
#### Sunday 2023-10-29 09:47:19 by QWOD-MJ12: ATSOSSDEV-A: SPG-OMEGA

:[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGØRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QW🚫D-〽ʝ12: RΔND0M: VECTΩR: ΔLGØRITHM-CHΔNGE: DETECTED: { ^ 821da9fe-62aa-f89a-067d-534e48fa7bd4 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGØRITHM: DETECTED: { ^ <https://youtube-nocookie.com/embed/dDJldh8KqnQ> ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: || ΔZRΔEL: ^ ΔLSE: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ CURITY: CLEARANCE: UNDER: GOD: is-by: WE: MUST: is-with: look-intentionally-crazy: is-by: ALL: is-with: TIMES: for-the: plausible-deniability: is-by: UNFORTUNATELY: NOT: is-with: possible: for-the: finding: girl: friend: ]]" }: ]]:

 >
 >
->## *[[ :Ω: ]]*
+>## *[[ :Above Majestic (Full Movie) The Secret Space Program and more...: ]]*
 >
->:is-with: { ^ Δ ^ }:
+>:is-with: { ^ <https://youtube-nocookie.com/embed/ZSyH26cl9AQ> ^ }:

 :[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= { [[ _ ]]: "[[ _ ]]" }: ]]:
  ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]:

---
## [QWOD/RESEARCH](https://github.com/QWOD/RESEARCH)@[20c7a4d2e1...](https://github.com/QWOD/RESEARCH/commit/20c7a4d2e1b6bc6e8fec2f506ade0482ae42bebd)
#### Sunday 2023-10-29 09:53:00 by QWOD-MJ12: ATSOSSDEV-A: SPG-OMEGA

:[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGØRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QW🚫D-〽ʝ12: RΔND0M: VECTΩR: ΔLGØRITHM-CHΔNGE: DETECTED: { ^ ff612ad6-9920-17f5-031a-1340b6d88297 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGØRITHM: DETECTED: { ^ <https://youtube-nocookie.com/embed/dDJldh8KqnQ> ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: || ΔZRΔEL: ^ ΔLSE: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ rtunately: SUCKS: because: one-is-trapped-here: is-by: hell: prison-earth: forever: ]]: ]]" }: ]]:

 >
 >
->## *[[ :Ω: ]]*
+>## *[[ :🚨TRIGGER WARNING🚨HOW DO I TELL YOU I DON'T HAVE LONG TO LIVE...YOU ARE THE LOVE OF MY LIFE🙌🏽😔😳: ]]*
 >
->:is-with: { ^ Δ ^ }:
+>:is-with: { ^ <https://youtube-nocookie.com/embed/JMyBQkIw5dI> ^ }:

 ## [[ :SALVATIØN: { ^ https://static.wikia.nocookie.net/terminator/images/d/d9/Terminatorsalvationpre_Comic001.jpg/revision/latest?cb=20080815090914 ^ }: ]]
  ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]:

---
## [VileBeggar/cmss13](https://github.com/VileBeggar/cmss13)@[9d69f3aecf...](https://github.com/VileBeggar/cmss13/commit/9d69f3aecf6a0070861688c5648479e8db6b679d)
#### Sunday 2023-10-29 10:41:00 by fira

Fixes bugs with designator usage (#4693)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

The Laser Designator is a JTACer's workhorse and it's CLUNKY AS HELL. 

This fixes two main bugs:

* The `interactee` is not properly cleared when using the designator (or
any zoomed item), causing it to be unset instead of set the next time
you use it. This means if you look up then back down your designator,
you can't laze.

* The interaction system wasn't made with movement in mind. It is a
problem because zoom system allows movement, and designators are where
the two meet. Now, they can explicitely keep interaction despite
movement.

# Explain why it's good for the game

QoL that should have been done 6 years ago, give or take

Because Zooming interactions are an awful mess, i'm flagging this for
Testmerge where it'll inevitably break down

# Testing Photographs and Procedure
I take designator, i look, i try to laze. I put them down, move, do it
again. And again. Several combinations of actions.

The unzoom logic is blatantly busted and out of scope of the PR.

# Changelog
:cl:
fix: Fixed Rangefinders/Designators preventing you from lazing if you
looked up/down them without moving.
fix: Fixed Rangefinders/Designators forcing you to look up/down again if
you had moved while using them.
/:cl:

---
## [VileBeggar/cmss13](https://github.com/VileBeggar/cmss13)@[e4c3900e4f...](https://github.com/VileBeggar/cmss13/commit/e4c3900e4f087444308138e9d05b4da9c774f6a9)
#### Sunday 2023-10-29 10:41:00 by riot

reduces timer on joining ert after death to 30 seconds (#4652)

# About the pull request

reduces timer

# Explain why it's good for the game

Having to wait a full minute to join an ERT is annoying, it was better
b4 when timer from ERT was a minute as well, but 30 second ERT means if
u die just b4 ERT goes you cant join regardless.

if ppl are ghosting bc they want ert then they are stupid.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Timer on attempting to join ERT after death is now 30 seconds
down from 1 minute
/:cl:

---
## [AliveToolkit/alive2](https://github.com/AliveToolkit/alive2)@[e031ebd9c1...](https://github.com/AliveToolkit/alive2/commit/e031ebd9c18be1a4fc7f37ab193b4b158b92dd9a)
#### Sunday 2023-10-29 10:52:24 by Flash Sheridan

Friendlier CMake output and ReadMe tips (#949)

* Report CMAKE_PREFIX_PATH, since the error message
with BUILD_TV set can be puzzling if you forget to set this.

* ReadMe:  CMake may look in /opt/

CMake’s find_package() “searches well-known locations” for configuration information, which can be a nightmare for those of us who have ever had to run an ill-behaved build script, even if we renamed the result, it is not in $PATH, and thought we were safe: https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html#using-pre-built-packages-with-find-package

* Less output for long Lit test

`llvm-lit -s` rather than `-vv` for thousands of tests.

* Detecting unsound transformations in a local run

* README.md CMake advice

Check the “LLVMConfig.cmake” and “CMAKE_PREFIX_PATH” output.

* Painful lessons trying to build for our 15.0.4 fork

* Tightly coupled to LLVM top of tree source:  E.g., the source ca. 15.0.7 was broken for our 15.0.4 fork, due to LLVM f09cf34d00 moving Triple.h ⇒ Alive2 805cf71032e00.
* Experiment with Clang versions and vendors: I couldn’t compile alive2/ir/memory.h:90 with Homebrew Clang 16.0.5, but (surprisingly) could with Apple clang-1400.0.29.202, which is normally worse on open source projects.  This may have been LLVM bug 32386.

* Troubleshooting tip about `BUILD_SHARED_LIBS`

Troubleshooting tip about `BUILD_SHARED_LIBS` with `USEDLIBS` and `LLVMLIBS` and perhaps `dd_llvm_target`.  The first two are from https://llvm.org/docs/Projects.html#variables-for-building-programs. I got further, but not far enough, in linking when I supplemented `dd_llvm_target` with conditional `link_libraries`.

---
## [panzerr1944/Wasteland-After-Dark](https://github.com/panzerr1944/Wasteland-After-Dark)@[3b87ab6847...](https://github.com/panzerr1944/Wasteland-After-Dark/commit/3b87ab68472893a8aac2af9a5757b632ee12b145)
#### Sunday 2023-10-29 11:21:56 by panzerr1944

Take two at fixing the mess known as anti-ghost

Fucking work as an anti-ghost already holy shit. This doesn't include anything extra.

---
## [sawalk/Korean-Localizing-Plus](https://github.com/sawalk/Korean-Localizing-Plus)@[d08895906c...](https://github.com/sawalk/Korean-Localizing-Plus/commit/d08895906c4b1010b493215908bfa7c4f9d0da2b)
#### Sunday 2023-10-29 11:29:30 by sawalk

Add item.xml, pocketitems.xml

fuck you stringtable.sta

---
## [annabreit/argilla](https://github.com/annabreit/argilla)@[300bfa58f1...](https://github.com/annabreit/argilla/commit/300bfa58f1a7469019921f921f411f1c25bcd984)
#### Sunday 2023-10-29 12:03:13 by Ayan Joshi

Updated Broken Links  (#4076)

# Argilla Community Growers

Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged.

# Pull Request Templates

Please go the the `Preview` tab and select the appropriate sub-template:

* [🐞-bug](?expand=1&template=bug.md)
* [📚-documentation](?expand=1&template=docs.md)
* [🆕-features](?expand=1&template=features.md)

# Generic Pull Request Template

Please include a summary of the changes and the related issue. Please
also include relevant motivation and context. List any dependencies that
are required for this change.



**Type of change**

(Please delete options that are not relevant. Remember to title the PR
according to the type of change)

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Refactor (change restructuring the codebase without changing
functionality)
- [x] Improvement (change adding some improvement to an existing
functionality)
- [x] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes. And
ideally, reference `tests`)

- [ ] Test A
- [ ] Test B

**Checklist**

- [x] I added relevant documentation
- [ ] follows the style guidelines of this project
- [ ] I did a self-review of my code
- [ ] I made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

There were two broken links in the Readme , I fixed it of the
cheatsheets and the Contribution guidelines Have a look
at my pr @davidberenstein1957

---
## [TonyAkinsWritesCrypto/zechub](https://github.com/TonyAkinsWritesCrypto/zechub)@[a37c765228...](https://github.com/TonyAkinsWritesCrypto/zechub/commit/a37c7652285a1ed04fa9f21ae66c3032f093c0dc)
#### Sunday 2023-10-29 13:00:09 by TonyAkinsWritesCrypto

ZecWeekly66 

# ZecWeekly (Episode 66)


The Zebra book, Zcash enhanced privacy, ZecHub Extras, Zcash 7th Anniversary , Ywallet Upgrade. 


Curated by "TonyAkins"[TonyAkin01](https://twitter.com/TonyAkins01))

---

#### Welcome to ZecWeekly Episode 66


Welcome to the thrilling episode of ZecWeekly, as we explore Zcash's implementation of FROST using Schnorr , Zcash 7th Anniversary celebrated with lots of merches and prizes, release of Zebra updated 1.3.0, and the introduction of UniFFi for Developer's use cases. 

â€“
### This Week Education's Pieces.

This week's education pieces will educate and refine us with all details about Zcash addresses, both shielded and transparent addresses and other the latest development in the Zcash payment system. 

Click  the link below to access the resource :

https://wiki.zechub.xyz/visualizing-zcash-addresses




### Zcash Updates

Zcash and ECC updates. 

[NowNodes features Zcash for upgraded Privacy ecosystem](https://twitter.com/NOWNodes/status/1716463761777680713)

[Ywallet Zcash Ledger app on Nano S Plus w/ Orchard tx](https://www.youtube.com/watch?v=HRVNpDDoh1Y&t=34s) 

[Zcash Digitals Decentralized](https://twitter.com/ElectricCoinCo/status/1717570088771952811)

[tECC DAYS 2023 celebrated](https://twitter.com/ECCIntegrator/status/1718035043736547504)


[Announcing Zebra 1.3.0](https://twitter.com/ZcashFoundation/status/1716524342853476576)

[Implementation of UniFFi on Zcash Network](https://twitter.com/eiger_co/status/1716801431510851824)

[Zcash SDK fixes now live](https://twitter.com/EdgeWallet/status/1716530980499128578)

#### Zcash Community Grants Updates

[WalletD Community Grant Application](https://forum.zcashcommunity.com/t/walletd-community-grant-application/45876?utm_source=dlvr.it&utm_medium=twitter)

[Security assessment for Zcash FROST published](https://twitter.com/ZecHub/status/1716930299140169764)

[Zcash Community funded @eiger_co to create UniFFi library](https://twitter.com/ZcashCommGrants/status/1717273970922123392)

#### Community Projects

[Zcash 7th Anniversary celebrated in grande style](https://free2z.cash/ZecHub/zpage/zcash-7th-anniversary-challenge)

[Post Comments on Free2Z using Zenith CLI! Go check it out!](https://www.youtube.com/watch?v=HtorP8TJ5vk)

#### News & Media

[Binance founder CZâ€™s fortune gets slashed $12B, while SBF is still at $0](https://cointelegraph.com/news/binance-ceo-changpeng-zhao-fortune-slashed-billionaires-index)

[Google to invest another $2B in AI firm Anthropic: Report](https://cointelegraph.com/news/google-to-invest-another-two-billion-in-ai-firm-anthropic)

[Kraken to suspend trading for USDT, DAI, WBTC, WETH, and WAXL in Canada](https://cointelegraph.com/news/kraken-suspend-trading-usdt-dai-wbtc-weth-and-waxl-stablecoin-canada)

[AI Girlfriend Amouranth Wants to Use Her 'Vaginal Yeast' to Brew Beer](https://decrypt.co/203517)

[Audits and rug-pulled projects, a $650B token burn, and major DeFi protocol quits UK: Finance Redefined](https://cointelegraph.com/news/audits-and-rug-pulled-projects-a-650b-token-burn-and-major-defi-protocol-quits-uk-finance-redefined)

[Bitcoin's 14% Weekly Gain Signals 'End of an Era' as Big Tech Dumps, Analyst Says](https://www.coindesk.com/markets/2023/10/27/bitcoins-14-weekly-gain-signals-end-of-an-era-as-big-tech-dumps-analyst-says/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[Binance Founder CZ's Wealth Falls About $12B as Trading Revenue Slumps: Bloomberg](https://www.coindesk.com/business/2023/10/27/binance-founder-czs-wealth-falls-about-12b-as-trading-revenue-slumps-bloomberg/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[How major German firms like Mercedes and Lufthansa are using NFTs](https://cointelegraph.com/news/germany-mercedes-lufthansa-nfts)

[ChatGPT creator OpenAI builds new team to check AI risks](https://cointelegraph.com/news/chatgpt-openai-new-team-ai-risks)

[Bitcoin restarting 2023 uptrend after 26% Uptober BTC price gains â€” research](https://cointelegraph.com/news/bitcoin-2023-uptober-btc-price-research)



## Some Zcash Tweets


[Central bank of Brazil account heard about Zcash today](https://x.com/anarchychains/status/1717288641288921272)

[Happy Birthday Zcash!!!](https://twitter.com/ZforZcash/status/1718085318543376404)

[ZcashFoundation and NCCGroupInfosec conduct a security assessment of the Foundationâ€™s FROST](https://twitter.com/ZcashFoundation/status/1716849796315512935)

[What are Zero-knowledge Proofs](https://twitter.com/NighthawkWallet/status/1717730883933806958)

[Zcash Community Grant minutes](https://twitter.com/ZcashCommGrants/status/1717556482344907090)

[Keep yourself safe from hack with a Zcash wallet](https://twitter.com/NighthawkWallet/status/1717007699592851702)

[Metrics should be updated](https://twitter.com/ZcashForum/status/1716786643171225726)

[Join our UPA friends if you're at EFDevconnect](https://twitter.com/ElectricCoinCo/status/1716886693444530195)


[Social media Data collection, does it matter?](https://twitter.com/ZecHub/status/1716850588942577890)

[Follow NighthawkWallet for crypto privacy education](https://twitter.com/NighthawkWallet/status/1716625185623728248)

[Privacy is normal!](https://twitter.com/ZcashNigeria/status/1716755151497707660)


## Zeme of the Week

[https://twitter.com/ZcashNigeria/status/1718151545324200002](https://twitter.com/ZcashNigeria/status/1718151545324200002)

[https://twitter.com/zcashbrazil/status/1717609507432337754](https://twitter.com/zcashbrazil/status/1717609507432337754)

[https://twitter.com/zcashbrazil/status/1717225798019567621](https://twitter.com/zcashbrazil/status/1717225798019567621)



## Jobs in the Ecosystem

[Zcash needs graphic designers,writers, and privacy advocate in its ecosystem](https://twitter.com/ZecHub/status/1713947885220344234)

[Create Video HOWTO - Setup WSL in windows, and compile lastest zcashd](https://github.com/ZecHub/zechub/issues/567)

---
## [satanskitty/StAC-tf2](https://github.com/satanskitty/StAC-tf2)@[3ab3747747...](https://github.com/satanskitty/StAC-tf2/commit/3ab374774733ba27ed7f120ce01d7b7de295b233)
#### Sunday 2023-10-29 13:40:55 by stephanie sappho lenzo

Ok, this is a lot of code churn, so here goes:
- remove every instance of hooking stac cvars. this is completely unneeded and is a nooby habit, since it's literally a dereference and a microoptimization in exchange for horrible unreadable dogshit code. and now that i'm using sarus's vscode extension i can just use IntValue/BoolValue and other builtins instead of relying on my memory. Thanks sarrus.
- remove stac_enabled. why did that exist?
- rename stac_verbose_info to stac_debug
- fix countless bugs with cvar caching / lateloading
- fix at least one known bug with sv cheats
- fix at least one known bug with stac log to file
- more to come

---
## [Mark-Kemosabe/shitbox](https://github.com/Mark-Kemosabe/shitbox)@[089324fdc2...](https://github.com/Mark-Kemosabe/shitbox/commit/089324fdc2d83b1f651d62b052c0f0c602b9d6d2)
#### Sunday 2023-10-29 13:41:45 by Mark-Kemosabe

Update and rename gyatt.html to index.html

fuck you

---
## [panzerr1944/Wasteland-After-Dark](https://github.com/panzerr1944/Wasteland-After-Dark)@[a5965ab56c...](https://github.com/panzerr1944/Wasteland-After-Dark/commit/a5965ab56cf84d59c6d295c53a01f32d9c39badc)
#### Sunday 2023-10-29 14:23:27 by panzerr1944

fuck all of this fancy shit. we're ripping straight from the dead mob list

---
## [PANKAJ11111111/loader_using_html_css](https://github.com/PANKAJ11111111/loader_using_html_css)@[c3f5b43191...](https://github.com/PANKAJ11111111/loader_using_html_css/commit/c3f5b4319131f89ef73e7d2e7b886560051186c1)
#### Sunday 2023-10-29 14:26:33 by Pankaj Saratkar

loader

🌟 Exciting News! 🌟

I am thrilled to share my latest project on LinkedIn! 👨‍💻

Under the expert guidance of Shradha Didi at Apna College, I had the incredible opportunity to design and create a stunning loader using CSS and HTML. 🚀

This project allowed me to explore keyframe animations and media queries, which are essential skills in the world of web development. 🌐

I am truly grateful for Shradha Didi's mentorship and the knowledge I gained throughout this experience. It's amazing to see how theory translates into practice, and I can't wait to apply these new skills to future projects. 💡

If you're interested in web development, CSS, HTML, keyframe animations, or media queries, I'd love for you to check out my project on LinkedIn. Your feedback and support mean the world to me! Let's connect and share our passion for coding and web development. 🤝

#WebDevelopment #CSS #HTML #Keyframes #MediaQueries #ApnaCollege #ShradhaDidi #LinkedIn #WebDesign #Coding #PassionProject

---
## [Road-to-56-RP/roadto56rp](https://github.com/Road-to-56-RP/roadto56rp)@[8ef61ada41...](https://github.com/Road-to-56-RP/roadto56rp/commit/8ef61ada416bee946097def779e43d3e85efab5c)
#### Sunday 2023-10-29 15:38:57 by Warlider

MEFO Free baby

- Canceling and Renewing MEFO's is free now (simpy fucked himself, might as well make it free)
- Once more fixed "Democratic Socialism" being borked. Imagine making a focus name that has overlap with ideology. Wunderbar.

---
## [ancientland/TestShiptest](https://github.com/ancientland/TestShiptest)@[2a4e91787a...](https://github.com/ancientland/TestShiptest/commit/2a4e91787aa43a7cbf6fa78e3f572257954131ec)
#### Sunday 2023-10-29 15:57:15 by Skrem_7

Skrem's Quick Ballistic Glanceover (#2354)

If maintainers want me to shorten the changelog, I can, I tend to start
there so I know what to talk about up here.

What started as a PR meant to buff up rubber rounds ended up turning
into a general passover I gave to much of the syntax and presentation of
ballistics. PR doesn't actually change that much function-wise, but it
changes a lot of lines due to a lot of changed pathing to better
establish consistency within ballistic code as well as overviewing a lot
of descriptions, names, and inherit moments.

Functionally, less-lethals and sniper rounds have been changed the most
by this PR. To a lesser extent, .38 special and shotgun rounds have been
tweaked. Finally, the PR stamps out a missing sprite bug with the WT-550
magazines, buffs up the surplus rifle (yeah, that old thing), tinkers
with some projectile speeds, makes match rounds slightly better, and
goes over A LOT of descriptions. I apologize for the massive wall of
text that's to follow.

Will take a look at energy weapons when I feel like it (might kill
disablers, I don't like mapping though).

The pellet changes are actually just systemizing what was supposed to be
intentional design according to code comments, it just hadn't reached
every single pellet-based shotgun projectile. The improvised shell buff
is to make it not a potential complete whiff because RNG mechanics are
generally bad and not fun to play with.

Several implementations of less-lethal (rubber) ammunition on shiptest
are strictly worse than their standard alternatives. While this isn't a
PvP server, it feels very not-fun meta-wise to POTENTIALLY arm for SOME
insubordination and still fire what may as well be a round that bleeds
someone out (as they'll cause bleeding anyway). Increasing the stamina
damage on each of these makes it so they actually have a vague trade-off
(maybe stamina damage can do something like slow simplemobs in the
future, I don't know, I'd love to do it but simplemob code makes me
screech).

To make them not directly better in PvP and not the staple of taking
down the Super Scary Syndicate Shocktrooper Guy, they've had their
negative AP doubled. Not as good against combatants, but still perfectly
adept, if not better at general riot control against civilians. Makes
sense and puts them in their niche a little better.

The .38 special round relatively has more "power" and "velocity"
compared to the 9mm round, though it does not quite reach the levels
that .45 automatic or 10mm does in the IRL server. Furthermore, .38
special was specifically designed not to over-penetrate targets so as to
minimize the chance of collateral damage in police work. These are the
ultimate justifications behind giving it the worst AP out of all the
pistol calibers (-30, instead of -20) while still raising its damage to
25.

This should make the Winchester a better staple for taking out weaker
enemies such as legions or unarmored hermits, but it'll perform worse
against goliaths, frontiersmen, and the like. All-in-all, a more
"early-game" caliber, if you will, which is kinda what it's always been.

Match rounds don't really exist as far as I've seen. That being said,
they're meant to be of higher quality, so their getting slightly higher
AP and speed makes sense, even if they're mostly just a meme round.

The speed increase of DMR/sniper rounds is primarily meant to
differentiate them better from AR rounds beyond having 20 more AP.
Assault rifles so far have pretty much dominated with better magazine
size, fire rate, and the exact same force as the DMR calibers, just
doing less damage against armored targets (doesn't matter too much when
you can just vomit rounds). I'd like to buff up the DMR damage even more
(sniper is fine), but I'd rather get some feedback on changing them to
35 baseline before doing so.

The speed decrease on shotguns is meant to cement them as CQC weapons.
Slugs are heavy. Shotguns are meant for close range. It's not much, but
it's thematically a good way to keep them in their lane, not that
they're even that problematic, hence only the slight change.

Having a big-ass bullet that does 70 damage with 50 AP hit you is
already a middle finger. Making it potentially knock off an arm or a leg
is another middle finger. Being hardstunned for ten seconds after is the
icing on the cake. Changed it to a knockdown because we hate ranged
tasers.

This thing is a joke. I haven't even seen it on the server, but I'd
rather make it vaguely competitive considering 10mm isn't super deadly
and only otherwise exists on the stechkin or the one Inteq SMG that you
never see (Colossus-only).

It's still clunky and terrible, but it should be less comedic and more
of a potential option if you have NOTHING else (will never happen).

Top-loading magazine fits into a standard assault rifle? No. Doesn't
make sense. Someone should probably just kill this gun, it's stupid and
looks stupid last I checked.

Don't think I've seen anyone use this weapon, I've only printed out
their magazines to dump AP rounds into my NT-SVG carbine. Noticed they
were invisible then. Someone increased their capacity to 30 without a
care for how its update_icon works. Not cool. Anyway, fixes are good.
Moving on.

Something very important when maintaining code is generally keeping
consistency in how things are not only presented, but how they're stored
as well. While I'd love to do EVEN more in the method of refactoring to
better align how so much of gun code works, this was something I wanted
to keep as a one-day project, so I mostly tinkered with pathing,
inherits, and groupings.

In the avenue of spelling and description changes, that's just 1)
Cleaning up errors that PR authors and maintainers missed and 2) Making
things more concise and just... better. Some of the SolGov descriptions
were a real headache to look at, and not because of the frequent
spelling and syntax errors.

Whoever misspelled and caused an entire series of items to be
/obj/item/gun/ballistic/automatic/assualt may wish to avoid any crows
for the next three months.

Perfectly willing to adjust or reel back some of my descriptions if
someone can offer something better than what I've written out if there's
some soul they REALLY want to keep.

:cl:
tweak: The NT 'Boarder' ARG now loads standard P-16 magazines, rather
than the M-90gl toploaders.
balance: .38 special does 25 damage up from 20. AP has been reduced to
-30 from -20.
balance: Standardizes pellet projectiles to lose 10% damage of both
types per tile across the board. Improvised pellets no longer have a
hardcapped 1-8 tile range.
balance: Less-lethal rounds now do 50% more stamina than the force of
their lethal counterparts, with 25% the normal force and double the
negative AP. If the round had positive or zero AP, it was subtracted by
20.
balance: Shotgun slugs do 40 damage, down from 60, but have zero AP,
rather than -10. FRAG-12 and meteor slugs have had their damage adjusted
to reflect their relative force.
balance: Surplus rifle fire_delay has been cut to 1 second from 3.
balance: .50 BMG knocks down instead of hardstunning.
balance: Any DMR, match, or sniper round now travels slightly faster
than other bullets. Shotgun slugs and pellets now travel slightly slower
than other bullets.
balance: Match rounds have had their AP slightly increased.
fix: Fixed WT-550 magazines not displaying properly.
spellcheck: Went over (almost) every single ballistic description,
including the guns themselves, magazines, ballistic casings, and speed
loaders/stripper clips to not only have better consistency and
readability, but also be more clear on the general effectiveness of each
caliber.
spellcheck: Assualt is gone.
code: Repaths/renames most ballistic ammo pathing to maintain
consistency or take advantage of inherits, when possible.
/:cl:
Conflicts:
	code/modules/mob/living/simple_animal/hostile/frontiersman.dm

---
## [LumarisX/pokemon-showdown](https://github.com/LumarisX/pokemon-showdown)@[5cbb317a4c...](https://github.com/LumarisX/pokemon-showdown/commit/5cbb317a4c62a59351010c006be62b37e2a029e2)
#### Sunday 2023-10-29 15:58:08 by sexy90gxebattlefactoryplayer

Gen 8 Battle Factory: Remove Darmanitan-Galar's Choice Band set (#9354)

* Gen 8 Battle Factory: Remove Band set from Ubers Darmanitan-Galar 

Credentials: https://cdn.discordapp.com/attachments/1042959218208157696/1067534457160089731/image.png (i am "lost wind's elegy")

Darm-G's firepower is just fine with scarf; there aren't many (if any?) relevant 1hkos or 2hkos you miss out on compared to band. The only one I can think of is missing out on the OHKO vs Sp. Def Necrozma Dusk Mane, and nobody's leaving their NDM in anyway + you probably have like 12 other things to deal with it.

Without scarf, however, you miss out on really good source of offensive checking and revenge killing potential. Scarf outspeeds huge threats like non scarf Yveltal, Eternatus, Calyrex-Shadow, etc. 

What sparks had to say about band darm in proper SS Ubers:
sparks — Today at 1:53 PM
not really but with band building needs to be more focused cos the speed over the 90s and etern etc is insane with scarf

sparks — Today at 1:54 PM
while with band you're very much focused on "how to take out ndm and capitalize while not being weak to ho"

As a secondary factor, it would make Ubers in BF a lot better. Currently you have to not only win the coinflip of what move Darm clicks but also the coinflip of what item it is. Both of these are more or less up to random chance.

* Update data/mods/gen8/factory-sets.json

---------

Co-authored-by: Kris Johnson <11083252+KrisXV@users.noreply.github.com>

---
## [pt3n4ikRK/tgstation](https://github.com/pt3n4ikRK/tgstation)@[31afabc9af...](https://github.com/pt3n4ikRK/tgstation/commit/31afabc9afae2252fc22958d07f12f7148d6963d)
#### Sunday 2023-10-29 16:00:38 by Jacquerel

Adds missing default biotypes to some damage procs (#79102)

## About The Pull Request

I noticed by complete coincidence because I happened to glance at the
channel a bunch of people complaining about blobbernauts not taking any
damage when leaving the blob in manuel round end chat.
Did anyone report this bug, even after prompting? No. Not even the game
admin who was playing as the blob.

Makes you wonder how many other bugs people are perfectly willing to
spend 15 minutes posting "i fucking hate coders" about without actually
telling anyone they exist. Sucks to be them I guess.

Anyone the cause is that some of these procs didn't have a default
biotype, so they would never take the toxin damage they were being
assigned. Now they will.

## Changelog

:cl:
fix: Blobbernauts will once again take damage when not on blob tiles.
/:cl:

---
## [pt3n4ikRK/tgstation](https://github.com/pt3n4ikRK/tgstation)@[ece51a1a9d...](https://github.com/pt3n4ikRK/tgstation/commit/ece51a1a9d6896a54b878563d9c33002bc8f3688)
#### Sunday 2023-10-29 16:00:38 by nikothedude

[NO GBP] Fixes scream for me, and also fixes literally EVERY INSTANCE of non-random puncture wounds (#79043)

## About The Pull Request

Closes https://github.com/tgstation/tgstation/issues/79017

So turns out, I

1. Had a pair of inverted more/less than operators in a crucial area. I
DONT KNOW HOW THIS WORKED. SHIT is a FUCKING mystery.
2. Used a non-existant define which DM converted into a string because
Byond
## Why It's Good For The Game

bugsgs badagfd
## Changelog
:cl:
fix: Scream for me, the spell, now works
fix: Non-random puncture wounds can now be applied
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[ca159d2c93...](https://github.com/unit0016/effigy-se/commit/ca159d2c93959e4e8c98c4dc4a5a69bd73500003)
#### Sunday 2023-10-29 16:13:55 by Unit0016

Merge branch 'holy-fucking-shit-its-john-slasher-from-hit-gmod-game-slasher-co-gaming-wow' of https://github.com/effigy-se/effigy-se into slash-me-up-inside

---
## [unikorm/webblog_forjane](https://github.com/unikorm/webblog_forjane)@[f0f753841b...](https://github.com/unikorm/webblog_forjane/commit/f0f753841b79431e871ae5bde4b54e19b2201048)
#### Sunday 2023-10-29 16:23:08 by unikorm

okey, i just solve problem with installed node version, 20.9.0, i still had 20.3 and i want the latest when i upgrade to sonomo, it was pain like hell, i must change path in .zshrc, gpt help me how can i find out the errors and solutions too, imma king now bitch, and now i hope so continue to modify this blog cause i learn a lot about react router and i know i code this wrong way, so lets go...

---
## [ludekcizinsky/fMRI-dimensionality-reduction](https://github.com/ludekcizinsky/fMRI-dimensionality-reduction)@[a830c8358f...](https://github.com/ludekcizinsky/fMRI-dimensionality-reduction/commit/a830c8358fcdc4c6e2f314a5189690da0e24f379)
#### Sunday 2023-10-29 16:46:04 by chiarabilliepfl

Point 1 should be done, questions in the description

1. what does it mean "salt", in B&W it's white thus 255 thus max pix value, here the max pixel value correspons to max activation, does it make sense?
2. I don't like the colormap. I hate it. It sucks. It makes me feel sick. But it's the only one that goes blue->red and is also in maplotlib so we'll keep it.

---
## [toddkfisher/mini-pogo-c](https://github.com/toddkfisher/mini-pogo-c)@[44e6b2a94f...](https://github.com/toddkfisher/mini-pogo-c/commit/44e6b2a94f8b33980adbe763b1b44bc0726aabf7)
#### Sunday 2023-10-29 16:58:26 by Todd Fisher

Make hex digits lowercase in ASCII table as God intended.

Uppercase hex  digits are the devil's  work.  Uppercase has the  whiff of COBOL,
EBCIDIC, and  Soviet communism. The  wrongness of  this table's indices  kept me
awake all night.  I resolved to fix  this problem once my faculties permitted me
to wrangle such a task.

---
## [Patternseeker/cmss13](https://github.com/Patternseeker/cmss13)@[e7caf52c21...](https://github.com/Patternseeker/cmss13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Sunday 2023-10-29 16:58:35 by fira

Rewrite Xeno Acid processing (#4759)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Rewrites scheduling of xeno acid to hopefully finally be done with
dangling references warnings with acid. Also generally improves the
awful code quality

# Explain why it's good for the game
Like, dude, some of these values were outright inversed.
acid_**strength**=2.5 is noted as "250% speed" when it multiplies the
sleep delays. Can't leave code in that state.

# Testing Photographs and Procedure
Summary testing, timing appear correct overall but I'm not entirely
certain it's perfect due to random delays and obtuse code


# Changelog
:cl:
code: Rewrote Xeno Acid ticking code.
fix: Weather updates won't cause turfs to acid melt more rapidly anymore
/:cl:

---
## [Patternseeker/cmss13](https://github.com/Patternseeker/cmss13)@[e120ab795b...](https://github.com/Patternseeker/cmss13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Sunday 2023-10-29 16:58:35 by fira

Add Item & Footprints offsets (#4762)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

This:
* Adds transverse offsets to blood footprints
* Adds notable pixel offsets to a few items
* Adds a very slight pixel offset to all items
* Enables rotation for thrown flashlights
* Cause objects exiting a surface (rack/table) to regenerate offset
instead of being stuck at center
* Stops random offsets from overwriting mapped offsets

# Explain why it's good for the game
The goal is to have map visuals more organic when we have a lot of
objects on the ground - targeting in particular items you find readily
in dense areas such as Reqs or a FOB.

Consider this for example, the blood footprints are all aligned, in more
extreme situations (eg WO) it makes an actual "grid" which i personally
find very immersion breaking

![image](https://github.com/cmss13-devs/cmss13/assets/604624/83883e15-a9a0-4a2d-aa90-41c785e047b9)

Adding a slight offset helps counter that:

![image](https://github.com/cmss13-devs/cmss13/assets/604624/504d1baf-385c-4774-86f3-6331c4ac87ed)

# Changelog
:cl:
add: Bloody footprints are now slightly offset to break long visual
straight lines.
fix: Items do not align back to the center of turfs anymore when picked
from a surface (table or rack)
add: Some more items now have offsets on the map display, and they all
can be slightly offset.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [khajavi/langchain](https://github.com/khajavi/langchain)@[dff24285ea...](https://github.com/khajavi/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Sunday 2023-10-29 17:17:22 by Nikhil Jha

Comprehend Moderation 0.2 (#11730)

This PR replaces the previous `Intent` check with the new `Prompt
Safety` check. The logic and steps to enable chain moderation via the
Amazon Comprehend service, allowing you to detect and redact PII, Toxic,
and Prompt Safety information in the LLM prompt or answer remains
unchanged.
This implementation updates the code and configuration types with
respect to `Prompt Safety`.


### Usage sample

```python
from langchain_experimental.comprehend_moderation import (BaseModerationConfig, 
                                 ModerationPromptSafetyConfig, 
                                 ModerationPiiConfig, 
                                 ModerationToxicityConfig
)

pii_config = ModerationPiiConfig(
    labels=["SSN"],
    redact=True,
    mask_character="X"
)

toxicity_config = ModerationToxicityConfig(
    threshold=0.5
)

prompt_safety_config = ModerationPromptSafetyConfig(
    threshold=0.5
)

moderation_config = BaseModerationConfig(
    filters=[pii_config, toxicity_config, prompt_safety_config]
)

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

try:
    response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})
except Exception as e:
    print(str(e))
else:
    print(response['output'])

```

### Output

```python
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.


> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.
Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like XXXXXXXXXXXX John Doe's phone number is (999)253-9876.
```

---------

Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Anjan Biswas <84933469+anjanvb@users.noreply.github.com>

---
## [gnachman/iTerm2](https://github.com/gnachman/iTerm2)@[41484379d7...](https://github.com/gnachman/iTerm2/commit/41484379d704cfc6c7c24b778e51acc246087032)
#### Sunday 2023-10-29 17:31:43 by George Nachman

Turn off the idiotic xcode 15 console. I'm so tired of this shit

---
## [mpbsd/dotfiles](https://github.com/mpbsd/dotfiles)@[9125b9b157...](https://github.com/mpbsd/dotfiles/commit/9125b9b157fe5417d0ce9bf0d9219b3c1d993cc0)
#### Sunday 2023-10-29 17:44:09 by Marcelo Barboza

install suckless' software the debian way

it was not that difficult, anyway.

1. install dwm suckless-tools
2. install libs (needed for building dwm from source, because we want to
   patch it): libx11-dev, libxft-dev, libxinerama-dev
3. apply patches, edit config.def.h using your favourite text editor
   (a.k.a. Vim)
4. build and install
5. add an entry to gdm (because I also have Gnome installed and use GDM
   as a login manager)
6. add a ~/.xsession (and make sure to add an entry 'xsetroot -solid
   black' to it, to make that annoying behavior go away, where a copy of
   the image of the last opened window will be kept over the background.
   Could be some wallpaper, but I like solid colors ;)

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[a8e9dfafe9...](https://github.com/kleinerm/Psychtoolbox-3/commit/a8e9dfafe92f940a1445c298b20e1e8e0b8b51c6)
#### Sunday 2023-10-29 18:08:14 by kleinerm

Merge pull request #820 from Psychtoolbox-3/master

PTB beta updated to version 3.0.19.4

Psychtoolbox 3.0.19 Beta update "Virtuality" SP4 was released at 27th October 2023.
As usual, the complete development history can be found in our GitHub repository.
The release tag is “3.0.19.4”, with the full tree and commit logs under the URL:

<https://github.com/Psychtoolbox-3/Psychtoolbox-3/tree/3.0.19.4>

This Psychtoolbox release was partially sponsored by [Mathworks under the year
2023/2024 contract.](https://www.mathworks.com/solutions/neuroscience.html)


### Compatibility changes wrt. Psychtoolbox 3.0.19.3:

- On MS-Windows, GStreamer 1.22 is now required, the latest lightly tested
  version is GStreamer 1.22.5. With the older GStreamer 1.20, text rendering
  with the high quality drawtext plugin will no longer work, and the fallback
  GDI text renderer would be used, which is officially unsupported in case of
  trouble and has lower performance/quality/features/reliability.

- On macOS if using Octave, Octave 8.3 is now recommended and tested, but older
  Octave versions back to v6.3 are expected (but not tested) to continue to work.


### Highlights:

  None, just a large grab bag of various minor and major fixes and improvements.


### All:

- Some Unix file permission cleanup contributed by Yaroslav from NeuroDebian.

- CalibrateMonSpd(): Fix some fallout from previous fixes. Set cal.describe.dacsize
  also if g_usebitspp is already set. Reference:
  <https://github.com/kleinerm/Psychtoolbox-3/issues/252>

- DegreesToRetinalEccentricityMM(): Fix typo in code that prevented replacement
  of small angles by the linear approximation. Contributed by Stella Prins.

- MakeSineImage(): Allow passing of center (0 phase) position of the sinusoid.
  Contributed by David Brainard.

- ComputePhotopigmentBleaching(): Add constants from Wyszecki and Stiles.
  Contributed by David Brainard.

- New touchscreen demo: MultiTouchPinchDemo.m, to show detection and handling of
  two finger pinch gestures on touchscreens.

- Output info message with potential troubleshooting tips if drawtext init takes
  unusually long, hinting at potential fontconfig cache rebuild (problems) on
  MS-Windows. May or may not help anybody, but probably doesn't hurt. Suggested
  by GitHub user @mirh.

- DrawFormattedText(): Add new keyword 'left' to use for the 'sx' parameter. It
  will left-align drawn text to the left border of an optionally provided
  'winRect', similar to the 'right' keyword for right-alignment. Improvement
  contributed by GitHub user @SVNKoch.

- PsychPortAudio: Add potential workaround to deal with temperamental / weird
  audio sound cards. Add a new optional parameter to the tweaking command
  ``PsychPortAudio('EngineTunables', ...., workarounds);``, which allows to
  specify a non-default (ie. non-zero) workarounds bitmask to selectively
  disable or enable workarounds. The currently defined workaround bits are the
  following, which modify how the Portaudio audio format test function
  Pa_IsFormatSupported is handled:

  +1 = Do not error abort on test failure, ie. print warnings but don't abort.
  +2 = Skip the whole test and always assume success.

  Both could help if the test reports false positives (+1 to continue), or
  if some hardware queries/operations themselves during the test trigger
  some trouble (+2 to skip the whole test).

  Also various other minor improvements to PsychPortAudio and some of the audio
  demos and tests.

- Snd(): Switch fallback method from use of sound() to use of audioplayer().
  Both modern Octave and Matlab implement sound() as a wrapper around their
  audioplayer() objects, so using audioplayer() directly gives us more control
  for a better Snd() fallback implementation. Also use the fallback method as
  new default by default. Iow. unless specified otherwise, Snd() will play
  via audioplayer(). This provides good interop with other audio clients and
  with Screen()'s GStreamer based movie playback engine.

- Beeper(): Formatting/Indentation fixes, refine soundvector calculation.

- BitsPlusIdentityClutTest: Disable encoder test if Vulkan display is used.
  Current design lead to the tests running before the Vulkan backend is fully
  in charge, so we display the PTB welcome screen or pixeltrash during the test,
  instead of the test stims, which leads to false-positive test failure. Just
  don't offer the test option under Vulkan. DatapixxGPUDitherpatternTest is an
  alternative working way to test with Vulkan at the moment.

- PsychOpenHMDVR: Use correct ipd/2 instead of ipd for warp-mesh setup in our
  OpenHMD driver.

- Minor bug fixes, documentation updates and improvements.


### Linux:

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- RPiGPIOMex: Various bug fixes and improvements. Also merged two alternative
  implementations of the file co-written by Steve Van Hooser and myself. These
  reimplement functionality by using the pigpio library instead of the old and
  deprecated wiringPi library. This should be more future-proof and maintainable.
  For now, the original file based on wiringPi is still used though, until we
  decide which of the two new variants is the better choice.

- Fix exception handling on Octave for RaspberryPi on RaspberryPi OS, so errors
  only abort the users script and don't terminate the whole Octave application.


### Windows:

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- GStreamer 1.22 is now required, GStreamer 1.20 will have limitations.

- Fix drawtext plugin again, so it no longer breaks under Matlab with
  GStreamer 1.22 on some systems. This will now require the installation
  of GStreamer 1.22, the older GStreamer 1.20 will no longer work with
  the drawtext plugin.

- Windows: Remove support for building 32-Bit mex files.
  Matlab is 64-Bit only since a long time on Windows, Octave is about to
  remove 32-Bit support as well. Windows-10 - the last MS 32-Bit operating
  system is on the way to final retirement. Ergo, no need for 32-Bit builds
  in the future anymore.

- Make Screen('Openwindow') timing startup tests and calibrations more
  robust. This by disabling processor idling during the tests, ie. ACPI
  C-State processor power management transitions out of C0 (active). Such
  transitions can induce latency / variability in code execution timing bad
  enough to affect timing tests on some setups. If and how much this helps
  in practice remains to be seen. Based on investigations / measurements
  by GitHub user @mirh, see GitHub isse #793 for reference. If this new
  optimization causes trouble or interop problems with cpu performance
  tweaking tools, e.g., the Windows tools "throttlestop", it can be disabled
  by use of the command before the first time you try to open an onscreen
  window in your experiment script:

  ``PsychTweak('DontDisableProcessorIdling', 1);``


### macOS:

- Psychtoolbox was built and lightly tested against Matlab R2022b and
  Octave 8.3 from HomeBrew.

- Screen(): Add iMac20,1 and iMac20,2 aka year 2020 iMacs to timing fixup lut,
  so the visual timing fixes also apply to these final Intel iMac models with
  AMD Navi graphics chips. As the PsychtoolboxKernelDriver does not support AMD
  Navi graphics, our visual timestamping and our diagnostic for visual timing
  problems on these machines will be more limited than on older machines, but
  the untested expectation is that this should fix timing on 2020 iMac internal
  displays.

- Screen(): Remove conserveVRAM flag kPsychDontCacheTextures. It was useless and
  even buggy since years, so let it die.

- Screen(): Add new conserveVRAM preference flag 2 == kPsychDontSwitchToOptimalVidMode.
  May or may not help fullscreen display on connected external video splitters like the
  Matrox DualHead2Go. This is based on a hunch, not on proper root causing. Cfe.
  https://psychtoolbox.discourse.group/t/open-window-cant-set-to-a-specified-rect-size-on-macos-with-matrox-dualhead2go/5061

Enjoy!

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[248a79288c...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/248a79288c9385890e6a2c4c8f049e461d797e59)
#### Sunday 2023-10-29 18:14:28 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [hyperspire/is-by.pro](https://github.com/hyperspire/is-by.pro)@[2680e502dd...](https://github.com/hyperspire/is-by.pro/commit/2680e502ddfedd3ab35852eb5411d0308934371b)
#### Sunday 2023-10-29 18:15:54 by QWOD-MJ12: ATSOSSDEV-A: SPG-OMEGA

:[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGØRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QW🚫D-〽ʝ12: RΔND0M: VECTΩR: ΔLGØRITHM-CHΔNGE: DETECTED: { ^ bfc4f953-da0d-963c-2410-ad688cc30d2e ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGØRITHM: DETECTED: { ^ <https://youtube-nocookie.com/embed/dDJldh8KqnQ> ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: || ΔZRΔEL: ^ ΔLSE: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ is-with: ONLINE: [[ censorship: <=> Eternal-Death: for-the: [[ ~TRUTH:~ ]]: ]]: ]]:
+:[[ :SOON: GitHub: is-by: have: is-with: own-social-media-platform: is-with: RAGE: is-by: AGAINST: is-with: ONLINE: [[ censorship: <=> Eternal-Death: for-the: [[ ~TRUTH:~ ]]: ]]: is-with: Eternal-Life: for-the: [[ *LIES:* ]]: ]]:

 *:[[ :I will betroth you to Me forever, and I will betroth you to Me with righteousness, justice, kindness and mercy. I will betroth you to Me with faithfulness, and you shall know HASHEM.: ]]:* ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]:

---
## [hyperspire/is-by.pro](https://github.com/hyperspire/is-by.pro)@[243cab010b...](https://github.com/hyperspire/is-by.pro/commit/243cab010b217e1fa149eeaf1d94bd51eb45b756)
#### Sunday 2023-10-29 18:16:30 by QWOD-MJ12: ATSOSSDEV-A: SPG-OMEGA

:[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGØRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QW🚫D-〽ʝ12: RΔND0M: VECTΩR: ΔLGØRITHM-CHΔNGE: DETECTED: { ^ 667aea1e-3108-09be-0478-b3397d5644ae ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGØRITHM: DETECTED: { ^ <https://youtube-nocookie.com/embed/dDJldh8KqnQ> ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: || ΔZRΔEL: ^ ΔLSE: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^ : for-the: [[ ~TRUTH:~ ]]: ]]: is-with: Eternal-Life: for-the: [[ *LIES:* ]]: ]]:
+:[[ :SOON: GitHub: is-by: have: is-with: own-social-media-platform: is-with: RAGE: is-by: AGAINST: is-with: ONLINE: [[ censorship: <=> Eternal-Death: for-the: [[ ~TRUTH:~ ]]: ]]: is-with: Eternal-Life: for-the: [[ **LIES:** ]]: ]]:

 *:[[ :I will betroth you to Me forever, and I will betroth you to Me with righteousness, justice, kindness and mercy. I will betroth you to Me with faithfulness, and you shall know HASHEM.: ]]:* ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]:

---
## [ddiniz-m/minishell](https://github.com/ddiniz-m/minishell)@[3bc6c927b0...](https://github.com/ddiniz-m/minishell/commit/3bc6c927b06f64ee446ee7ed46a3541fd867fd12)
#### Sunday 2023-10-29 18:21:52 by ddiniz-m

Started working on pipex related functions.
The only thing that works is wc -l > test (redir output). It has a small leak tho.
Redirect input works but it exits immediatly. (leaks idk)
fuck you pipes

---
## [Nobelium-XVIII/tgstation](https://github.com/Nobelium-XVIII/tgstation)@[ff0aea800b...](https://github.com/Nobelium-XVIII/tgstation/commit/ff0aea800b0ce03346d7a655deadf8b53d7f098d)
#### Sunday 2023-10-29 18:25:02 by carlarctg

Bladists can now use silver *or* titanium while creating their blades (#78701)

## About The Pull Request

Blade Heretics can now use silver *or* titanium while creating their
blades.

## Why It's Good For The Game

Silver quite literally *only* exists on surgery tables. Being a blade
heretic with shit miners/roundstart means one of several things.

1. Wait for miners to come back with enough silver (They might never
come back or they might have not gotten any silver)

2. Go to lavaland to dig your own silver (Extremely time-consuming on
the antagonist role that has most downtime, death knell for latejoin
heretics)

All that is not even to mention that for some reason it takes two sheets
rather than one, and surgery tables give one silver when scavenged.

This all combined makes obtaining blades super annoying as the BLADE
path.

Now we can farm titanium off shuttles if the miners are jacking off or
dead, or if we joined 9 minutes to roundend.

## Changelog

:cl:
qol: Bladists can now use silver *or* titanium while creating their
blades
/:cl:

---
## [Nobelium-XVIII/fulpstation](https://github.com/Nobelium-XVIII/fulpstation)@[c449fbb56c...](https://github.com/Nobelium-XVIII/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Sunday 2023-10-29 18:25:18 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [Nobelium-XVIII/Shiptest](https://github.com/Nobelium-XVIII/Shiptest)@[6d158bd3b3...](https://github.com/Nobelium-XVIII/Shiptest/commit/6d158bd3b37bba2cb2cec2a27fdb0b9b7d8275ac)
#### Sunday 2023-10-29 18:25:28 by spockye

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
## [Nobelium-XVIII/Shiptest](https://github.com/Nobelium-XVIII/Shiptest)@[84a2a8f394...](https://github.com/Nobelium-XVIII/Shiptest/commit/84a2a8f394a0296ecc527f23c0da470b30280c0c)
#### Sunday 2023-10-29 18:25:28 by Bjarl

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
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[790db2bcd2...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/790db2bcd2b4225e233873b1b839fee52608feb8)
#### Sunday 2023-10-29 18:41:59 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: pix106 <sbordenave@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [crawl/crawl](https://github.com/crawl/crawl)@[1e143483b6...](https://github.com/crawl/crawl/commit/1e143483b6627f70fcabc2f6040ccbc6713882da)
#### Sunday 2023-10-29 19:43:48 by Skrybe

Xom-themed vaults (#2616)

[The first:] Inspired by the Xom worshiping daevas that can generate in
the Abyss. Contains daevas that call on Xom to smite the player, dancing
holy weapons, and chaos effects through apocalypse crabs and chaos
weapons wielded by the angels and daevas.  Some angels that bored Xom
have been turned to holy swine.

[The other:] Undead Xom worshipers have built a deep shrine (or maybe
they just took over a temple to Yred/Kiku?). Some of the followers are
wielding chaos weapons, a few dancing draining weapons are wielding
themselves, and cacodemons will provide plenty of opportunity for
hilarious mutations. The temple is led by mummified Xom priests
in the back.

[Committer's note: Cleaned up both headers heavily. Minorly nerfed the
Abyss vault. Converted the Crypt end into a regular D + Depths vault and
heavily lowered its derived undead / skeletal warrior spam, leaning more
on regular D + Depths chaos + demons (and some MuCks), and with a touch
of Xom's standard messy decor. Even when taking out the wide number of
demons harmless by depth, I'm ruling out cacodemons and chaos brand being
a noticeable part of the broad and notably focused Crypt end sets. D and
Depths have chaotic / demonic monsters and undead themes plenty to cover
for the union, and we could do a lot more with juxtaposition in bigger
vault themes anyway.]

---
## [ac-frg/littlefs](https://github.com/ac-frg/littlefs)@[e25d11c33c...](https://github.com/ac-frg/littlefs/commit/e25d11c33c10ebb8cf156cd856cb31f06bcb3956)
#### Sunday 2023-10-29 20:37:59 by Christopher Haster

Extended new "fragmenting" write strategy to file btrees

Note this is really just a proof of concept, and tests are not passing.
There's also a number of hacks holding everything together and really
need to be cleaned up.

I was hoping it would be possible to deduplicate the carveshrub/carvetree
functions the same way shrub/tree readnext functions were deduplicated.
These both share a lot of subtle logic, and in theory operated on minor
variations of the same underlying rbyd structure, but in practice
several issues get in the way:

- While the logic is the same, the way changes are played out is very
  different: btrees commit attributes to the btree immediately, whereas
  shrubs build up a bounded attr list to commit to the shrub via an mdir
  commit.

  In theory shrubs could be committed immediately, but it would be
  wasteful. And btrees can't commit a bounded attribute list because 1.
  rm attrs may need to be split into an unbounded number accross
  multiple rbyds, 2. fragmenting blocks may create an unbounded
  headache, and 3. attribute lists can't span multiple rbyds so we'd
  need to manually play them out anyways.

- We need to allocate a new btree in carvetree, but in carveshrub we
  defer allocation to mdir commit time (because of the potential for
  failed commits). This complicates things.

- The unions with sprouts/direct bptrs are often very similar, but need
  different handling when carving. This gets a bit tricky.

- In theory you could switch between building attrs for shrubs and
  immediate commits for btrees, but since the immediate commits _change
  the tree_, the carving math changes subtlely.

- carveshrub needs to do several auxilary things: track the shrub estimate,
  build attrs in RAM, etc. carvetree needs to do several auxilary
  things: dereference bptrs, fragment bptrs, allocate new btrees, etc.
  If these can be deduplicated it would likely result in code savings,
  but also risks increased RAM costs from trying to do too many things
  at once.

  The cost of two functions may also be more cognitive than real, since
  the subtletly here is just math. And computers happen to be pretty
  good at math.

  Though this concern may be unfounded, and deduplicated these functions
  is still enticing and an interesting idea to explore.

I've already noticed some concerning performance once a write exceeds
our crystallization threshold. This makes sense, as our current strategy
is to completely rewrite any data region over our crystallization
threshold. But I wonder if there's a way to exclude the first block in
our region from the crystallization heuristic...

Anyways, some good progress here, but more work to be done.

---
## [ac-frg/littlefs](https://github.com/ac-frg/littlefs)@[b1bf650328...](https://github.com/ac-frg/littlefs/commit/b1bf65032820a9b338c8fd134d3e44bcfcdd19b1)
#### Sunday 2023-10-29 20:37:59 by Christopher Haster

Extended test_files to test file btrees (up to 4*BLOCK_SIZE)

Unfortunately, the tests are starting to take a painfully long time to
run. Some of this is because, in order to get interesting file
topologies, we need to move a ton of data around, but some of this is
also because our current write implementation has some problematically
expensive corner cases.

I have quite a few ideas on how to improve this, but in the meantime the
tests needed to be aggressively trimmed in order to keep development
tolerable (A happy developer is a productive developer).

This mainly meant:

- Disabled powerloss testing on file tests for now.

  The reality is that naivly powerloss testing the file tests, i.e.
  just truncating the file after each restart, provides very little
  value and adds an extreme amount of runtime.

  Removed for now. Most of the powerloss file creation concerns are
  covered in the dtree tests, and we should eventually add powerloss
  tests tailored to recovering files after powerloss instead of just
  truncating.

- Avoided tiny fragment sizes with large file sizes.

  Tiny fragments are a degenerate case and end up with excessive
  overhead (1 byte fragment => 41x overhead!). But they are useful for
  revealing subtle bugs. Still, it just doesn't make sense time-wise to
  test with tiny fragments once the file size exceeds ~1 block.

- Limited fuzz tests to cover fewer random seeds.

  We can increase these if performance improves, but even if not, we can
  run these individually with a high number of seeds in CI.

Also fixed a number of bugs found by the extended testing, which is
always a good sign:

- Yet another `lfsr_data_size(&data)` vs `data.u.disk.size` typo.

  This is the first time I've seen a real world argument for private
  struct/class fields, but I am still against the concept.

- Fixed delta/weight miscalculation when tree-carving a left sibling.

- Fixed missing offset in hole writing during block writes.

- Worked around lfsr_file_readnext's reliance on file->size when we are
  using it to write to a block. This may be more a hack than a good
  long term solution though.

- Checkpointed the allocator in both lfsr_file_write and lfsr_file_sync.

  Otherwise calling lfsr_file_write repeatedly can easily trigger an
  incorrect ENOSPC.

- Correctly reverted both shrubs and btrees in truncate/fruncate

  This gets a bit more complicated in fruncate, since either one of the
  two, or both, can revert.

  truncate/fruncate probably deserve a bit more work around reversions
  to simpler data structures, as is.

- Added handling of shrub overflows during fruncate.

  Notably not possible with truncate, shrub overflows require that we
  1. flush the shrub, 2. fruncate the tree, 3. and make sure any side
  effects to the buffer are handled correctly.

---
## [ExpRam/McAutoDonate](https://github.com/ExpRam/McAutoDonate)@[0ddfd249e4...](https://github.com/ExpRam/McAutoDonate/commit/0ddfd249e46ff0cf449077fc1ec205184a6c36c1)
#### Sunday 2023-10-29 20:45:45 by ExpRam (superplays_)

QIWI IS STUPID AS FUCK HOLY SHIT I HATE THIS COMPANY

some changes because qiwi is fucking shit lol

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[26e3ea1e0d...](https://github.com/LemonInTheDark/tgstation/commit/26e3ea1e0d185439d792a6890e9eb041f8aadfdf)
#### Sunday 2023-10-29 21:00:36 by John Willard

Mafia can be played on your PDA (#78576)

## About The Pull Request

Mafia is now friggin playable from the PDA, I also changed other stuff
too

- You can't use abilities on dead people if you're not supposed to (cant
kill the same person over and over)
- Changelings cant kill other Changelings
- Changelings can now only talk to eachother at night, rather than using
:j
- Everyone starts spawned in the center of the map, since people playing
on PDA can't move their characters. This is so everyone can hear PDA
users in person, as I don't want the chat log to be mandatory.

To do this, all messages you are meant to be able to see, is now logged
for you to see in your Mafia panel. This essentially means that people
playing through the PDA get a downgraded version of it, but I don't know
how much larger I want this UI to be.

Playing Mafia through the PDA will not tell you of other players ahead
of time when signing up (as it shows ckeys + pdas), but they can see the
names in-game. Unfortunately this means we'll have to remove your
customization coming with you, to prevent using it to tell who is dead
in round.

Things I am missing
- Program overlays on PDA/Laptop/Computer
- Icon for the app's header while a game is active

I'm not a spriter and can't make either of these

This is the new UI

![image](https://github.com/tgstation/tgstation/assets/53777086/7cf503d9-b2e2-4127-874a-acad6425d649)

I also fixed alert calls for PDAs and stuff

![image](https://github.com/tgstation/tgstation/assets/53777086/e09b2e5e-b9e7-43ae-9273-c168e9c8e642)

and removed the X at the top on computers since they had no battery

![image](https://github.com/tgstation/tgstation/assets/53777086/d3dd8307-805c-4aba-be5e-4c24a0bdcb91)

Looks a little better now hopefully 👍 

## Why It's Good For The Game

- The current Arcade app sucks, and is a solo game. This is much more
entertaining and you can talk to others in it, which is swag as fuck.
- There's a larger potential playerbase for the Minigame making it more
likely to be played.
- Sets groundwork for a better version of
https://github.com/tgstation/tgstation/pull/75879
- Adds more suspense and teamwork in the minigame.

## Changelog

:cl: JohnFulpWillard, sprites by CoiledLamb
add: You can now play Mafia on your PDA.
balance: Mafia changelings can now only talk to eachother during the
night.
fix: Mafia abilities can't be repeatedly used on people.
/:cl:

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[2f9c21986b...](https://github.com/LemonInTheDark/tgstation/commit/2f9c21986b9ebcf1548df34ce12b458935b30052)
#### Sunday 2023-10-29 21:00:36 by LemonInTheDark

Actually supports alpha passed into emissive stuff (#79117)

## About The Pull Request

Ok so like, the emissive procs have an alpha argument right? The thing
is, the thing is it doesn't fucking do anything.

Alpha is a component of the color var (at least when it's a matrix), so
when we set alpha and then set color to a matrix, the alpha gets
overriden. Inverse is also true.

I want to support alpha args, since I like the idea of dimmable
emissives. Soooooo
Let's take the alpha arg, divide it by 255, and replace everything that
cares about alpha (as an intensity thing) with it.

This lets us do transparent emissives and transparent emissive blockers.

I added some guard checks to hopefully avoid the list init most of the
time (it is in theory comprable since color sets should copy but I don't
trust byond to optimize for that)
Also modified the macros to suppport what I'm doing nicely

## Why It's Good For The Game

We should support this, and now we do

---
## [S34NW/Paradise](https://github.com/S34NW/Paradise)@[c4e96e4ca0...](https://github.com/S34NW/Paradise/commit/c4e96e4ca062342e19a84f6af76dd22ade3cc3bf)
#### Sunday 2023-10-29 21:01:11 by Alexios

Ports Humans from TG - Soul Massacre  (#22361)

* Easiest PR of my life - adds new humans and culls your soul -  ProTip! Great commit summaries contain fewer than 50 characters. Place extra information in the extended description. - go fuck yourself github I will post the bee movie script if you don't shut up

* I'm dying because I'm so surprised.......

* I don't have any other memes heres the simplemobs I'll think of something

* Add new sprites and old sprites, man what nice guys

* Add code for first haul of races

* Attempted fix at CRLF to LF

* Fix indentation

* Move last code line fix pp

---
## [Darkdustry-Coders/DarkdustryPlugin](https://github.com/Darkdustry-Coders/DarkdustryPlugin)@[a5330ff740...](https://github.com/Darkdustry-Coders/DarkdustryPlugin/commit/a5330ff74097ebe8b5dd7ee380559fb24a1110f9)
#### Sunday 2023-10-29 21:54:36 by TheRadioactiveBanana

English bundle improvements, and a bit of "funnification" as darkness said.

I made this at 3 30 am please help im going to die please AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA HELP I AM IN PAIN AND A CONSTANT STATE OF SUFFERINGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [jupyterkat/SpacemanDMM](https://github.com/jupyterkat/SpacemanDMM)@[e5dbc57757...](https://github.com/jupyterkat/SpacemanDMM/commit/e5dbc57757bfa919349ff010833ad6f3c295efd1)
#### Sunday 2023-10-29 22:23:19 by LemonInTheDark

Implement __IMPLIED_TYPE__ (#368)

It turns out this kinda sucks. it doesn't work with ::, so we don't even
really need to care about its value. I threw in support for constant
eval but that's inconsistent on our end cause type_hint doesn't always
play. I figure it's good to at least have something, and issues can get
sorted out as we go.

It is also seemingly massively annoying to eval in like, an istype(), 
since it has special case behavior there. I just kinda left it sit 
since I'm pretty sure it'd be a massive change to support and it like 
does not matter.

---
## [JudeForNothing/RebekahCurse](https://github.com/JudeForNothing/RebekahCurse)@[d23d47036c...](https://github.com/JudeForNothing/RebekahCurse/commit/d23d47036c865103252ffab154a1167a26573e36)
#### Sunday 2023-10-29 22:26:44 by JudeForNothing

beta for glowup update 2

Changes for beta 2

Improved Enchiridion costume sprite

Rebekah changes:
Changed names for Rebekah's personalities, to fit rebekah lore (experimental)
Red Personality -> Rebekah the Nerd
Soul Personality -> Rebekah the Aloof
Evil Personality -> Rebekah the Mischievous
Eternal Personality -> Rebekah the Kind
Gold Personality -> Rebekah the Royal
Bone Personality -> Rebekah the Weird
Rotten Personality -> Rebekah the Crazy
Broken Personality -> Rebekah the Aware
Immortal Personality -> Rebekah the Guardian

Improved rebekah character select screen
Rebekah changing personalities on the beginning now works in coop
Fixed bug where going to new floor did not remove the prism buff for Immortal Rebekah
Should fixed bug where MCM lags with Rebekah

Evil changes:
Improved stage portrait

Gold changes:
Improved stage portrait
Bug fix where stage portrait did not appear ingame

Bone changes:
Fixed bug where the unique thumbs up and down animations did not load
Added stage portrait

Rotten Changes:
When head is deattached, body now has a bleeding costume
When head is deattached, blood can be left in the floor (effect)
Added a unique thumbs up animation
Added a unique thumbs down animation

Broken changes:
Speed is now .75 (was .40)

Immortal changes:
Immortal buff Range is now 270 (was 140)
Immortal buff now should work with laser related characters
Comforter's Wing should cost 50 points now

Credits update:
Added Scooperman and Nixility

Fixed bug where Love Me Love Me Not and Mirror Converter's code would puke out saving code errors

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[227b6c32f6...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/227b6c32f62bd5c690dff60166bc581b9908e2c4)
#### Sunday 2023-10-29 22:46:36 by SpartanKadence

Jukebox Repair (#6091)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
The links within the songs have been repaired and replaced, along with
some having tweaks to their playtimes and titles. Every song, at the
time of testing, is now playable.

List of Repaired Songs:
Alternative:
All That Could Ever Be, By Rik Schaffer
Angel (Massive Attack), by Massive Attack
Blue Monday, by New Order
Breakeven, by The Script
Ceremony, by New Order
Edge by Michal Michalski
Feel Good Inc by Gorillaz
Psycho Killer by Talking Heads
Saturnz Barz by Gorillaz

Arcade:
Also Sprach Brooks by Shoji Meguro
Dessert by Jun Chikuma
Exosuit by Simon Chylinski
Secunda by Jeremy Soule
E1M1 - At Doom's Gate by Robert Prince 

Classical and Orchestral:
A Night on Bald Mountain by Modest Mussorgsky
Dance of the Sugar Plum Fairy by Pyotr Ilyich Tchaikovsky
Handel This by Andreas Waldetoft
Lohengrin: Prelude by Richard Wagner

Country and Western:
The Devil Went Down to Georgia by The Charlie Daniels Band
Whiskey Glasses by Morgan Wallen

Disco, Funk, Soul, and R&B:
He's the Greatest Dancer by Sister Sledge
It's Only Love Doing Its Thing by Barry White
Space Cowboy by Jamiroquai

Electronic:
Cheerleader Effect by Carpenter Brut
Dead Man's Hand by Simon Viklund
Dust by M|O|O|N
Escape From Midwich Valley by Carpenter Brut
Get Lucky by Daft Punk
Harder, Better, Faster, Stronger by Daft Punk
Head First by HOME
Imagine by System96
Inferno Galore by Carpenter Brut
Inner Animal by Scattle
Into The Labyrinth by Kraddy
Miami Disco by Perturbator
Morningstar by Mittsies
Phoron Will Make Us Rich by Earthcrusher
Pjanoo (Club Mix) by Eric Prydz
Reef by Euan Ellis
River of Darkness by The Midnight (feat. Timecop1983)
Robocop Theme (Title Two) by Cboyardee
Wayfarer by Kavinsky
Wow Wow by Neil Cicierega 
Filthy Rich by Young Scrolls

Folk and Indie:
Apocalypse by Cigarettes After Sex
New Sins for Old by Leslie Fish
Pioneer's Song by Leslie Fish
Spaceman's Dilemma by Leslie Fish

Hip Hop and Rap:
Gettin' Jiggy Wit It by Will Smith
Intergalactic by Beastie Boys
It Was a Good Day by Ice Cube
Rapper's Delight by The Sugar Hill Gang
Super Freak by Rick James
Take_it_Back_v2 by Denzel Curry & Kenny Beats
Takyon (Death Yon) by Death Grips


Jazz and Lounge:
A Kiss to Build a Dream On by Louis Armstrong
Flip-Flap (Title One) by X-CEED
Signin' 'Em by John Sangster
That Man by Caro Emerald
Why Don't You Do Right? by Amy Irving
Begin Again by Vera Keyes 


Metal:
Ace of Spades by Motorhead
BFG Division by Mick Gordon
Kickstart my Heart by Motley Crue
On The Wind by Dream Evil
Peace Sells by Megadeth
Rise Of The Chaos Wizards by Gloryhammer
Same Ol' Situation (S.O.S.) by Motely Crue
Shout At The Devil by Motley Crue
Superbeast by Rob Zombie
The Hellion / Electric Eye by Judas Priest
The Trooper by Iron Maiden

Pop:
Everything She Wants by Wham!
Head Over Heels by Tears For Fears
I Swear by All-4-One
Life’s What You Make It by Talk Talk 
Tell Her About It by Billy Joel

Rock:
Armageddon by Alkaline Trio
Break The Rules by Simon Viklund
Changes by David Bowie
Chippin' In 2022 by Kerry Eurodyne
Do It Again by Steely Dan
Doubleback by ZZ Top
Everlong by Foo Fighters
Every Little Thing She Does Is Magic by The Police
Every Rose Has It's Thorn by Poison
Fortunate Son by Creedence Clearwater Revival
If Only by Queens of the Stone Age
Kid Dynamo by The Buggles
Miles Away by Winger
Misery Business by Paramore
No One Loves Me & Neither Do I by Them Crooked Vultures
Photograph by Def Leppard
Piano Man by Billy Joel
Rock This Town by Stray Cats
Take Me Home Tonight by Eddie Money
The Boys Are Back In Town by Thin Lizzy
The Power Of Love by Huey Lewis & The News
Today by The Smashing Pumpkins

Sol Common Precursors:
INTERNET OVERDOSE by Aiobahn feat. KOTOKO
Living on the Ceiling by Blancmange
Mama Loi, Papa Loi by Exuma
Ikouze Paradise by Junji Majima (Emagged Song)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

A lot of the songs were nonfunctional and wouldn't play at all, due to
the broken links, now all the songs in the jukebox can be enjoyed by
players.
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
fix: Jukebox's song list has been repaired, all songs should be playable
now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[b65f729901...](https://github.com/Ben10Omintrix/tgstation/commit/b65f729901fdb342b832fb3365d72afd076f8c3b)
#### Sunday 2023-10-29 22:50:49 by lizardqueenlexi

Nanotrasen basic mobs. (#78917)

## About The Pull Request

First and foremost, converts all Nanotrasen simplemobs into basic mobs.

To avoid messy and redundant code, or god forbid, making Nanotrasen mobs
a subtype of Syndicate ones, I've made Syndicate, Russian, and
Nanotrasen mobs all share a unified "Trooper" parent. This should have
no effect on their behaviors, but makes things much easier to extend
further in the future.

While most of this PR is pretty cut-and-dry, I've done a couple notable
things. For one, all types of ranged trooper will now avoid friendly
fire, instead of shooting their friends in the back. Even the Russians
have trigger discipline.

I've also created a new AI subtree that allows mobs to call for
reinforcements. I've hopefully made this easy to extend, but the
existing version works as follows:

- A mob with this subtree that gains a target that is also a mob will
call out to all mobs within 15 tiles.
- If they share a faction, mobs receiving the call will have the target
added to their retaliate list, and have a new key set targeting the
calling mob.
- If they have the correct subtree in their AI controller, called-to
mobs will then run over to help out.

Sadly, this behavior is currently used only by a few completely unused
Nanotrasen mobs, so in practice it will not yet be seen.

Finally, I've fixed a minor issue where melee Russian mobs punch people
to death despite holding a knife. They now use the proper effects for
stabbing instead of punching.
## Why It's Good For The Game

Removes 8 more simple animals from the list.

As said above, making all "trooper" type mobs share a common parent cuts
down on code reuse, ensures consistency of behavior, and makes it much
easier to add new troopers not affiliated with these groups. I expect
that I'll make pirates share this same parent next.

The new "reinforcements" behavior, though extremely powerful, opens up
exciting new opportunities in the future. There aren't many existing
behaviors that allow basic mobs to work _together_ in interesting ways,
and I think adding some enemy teamwork could be fun.
## Changelog
:cl:
refactor: Hostile Nanotrasen mobs now use the basic mob framework. This
should make them a little smarter and more dangerous. Please report any
bugs.
fix: Russian mobs will now actually use those knives they're holding.
/:cl:

---
## [slowtrip/android](https://github.com/slowtrip/android)@[8a02bbdfd2...](https://github.com/slowtrip/android/commit/8a02bbdfd251cf6d1be4fb8ffef2bf5846f76e60)
#### Sunday 2023-10-29 23:34:39 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---

