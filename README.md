## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-10-25](docs/good-messages/2023/2023-10-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,443,676 were push events containing 3,737,794 commit messages that amount to 289,065,180 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 75 messages:


## [Iamgoofball/Skyrat-tg](https://github.com/Iamgoofball/Skyrat-tg)@[4a618d0561...](https://github.com/Iamgoofball/Skyrat-tg/commit/4a618d05616c654924ea86ea63eb4a12684caeb1)
#### Wednesday 2023-10-25 00:06:06 by SkyratBot

[MIRROR] Watcher Nest Lavaland Ruin [MDB IGNORE] (#24286)

* Watcher Nest Lavaland Ruin (#78790)

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

* Watcher Nest Lavaland Ruin

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[c034314f1b...](https://github.com/Paxilmaniac/Skyrat-tg/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Wednesday 2023-10-25 00:08:25 by SkyratBot

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
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[0e3b7d842b...](https://github.com/Paxilmaniac/Skyrat-tg/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Wednesday 2023-10-25 00:08:25 by SkyratBot

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
## [Towelstation13/towelstation13](https://github.com/Towelstation13/towelstation13)@[b2bf63490b...](https://github.com/Towelstation13/towelstation13/commit/b2bf63490bf5d9fdb30022e0f4d5884b990d9ea9)
#### Wednesday 2023-10-25 00:25:59 by Alexis

(Mirror) Icewalker camp update (#75)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Mirror of https://github.com/Skyrat-SS13/Skyrat-tg/pull/24056
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## How This Contributes To The Towelstation Roleplay Experience
Cooler icewalker base
<!-- Please add a short description of why you think these changes would
benefit the game and the roleplay atmosphere of the server. If you can't
justify it in words, it might not be worth adding. -->

## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->
<!-- To our mappers and spriters: Posting screenshots of content INSIDE
EDITORS (aseprite, PDN, SDMM, ect) is NOT valid proof of testing. Please
make sure that you COMPILE the game and provide PROOF you tested your
edits. -->

<details>
<summary>Screenshots/Videos</summary>
  
</details>

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

:cl: Paxilmaniac
add: The icewalker camp has been completely remade to be less of a
single house in the middle of hell, to a location befitting our viking
felines. As a side effect, the spawn of the camp is now static and in
the corner of the map, because the ruin loader really did not enjoy the
size of the templates.
image: Sprites for all of the forging related structures have been
redone because I REALLY hated what I did with them before
image: Several new sprites for things like wooden shelves, barrels, and
so on, all made by yours truly
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[a8edd9004f...](https://github.com/DesmontTiney/tgstation/commit/a8edd9004f1875bd3be409e2f382933a74bf8a40)
#### Wednesday 2023-10-25 00:47:06 by carlarctg

Gun kits don't need cable coil or tools, halved crafting time (#78419)

## About The Pull Request

Crafting R&D guns from gun kits no longer requires tools or cable coil.
The decloner and energy crossbow still need reagents.

Halved R&D gun crafting time. 20->10 seconds.

## Why It's Good For The Game

These changes were made a long, long while ago and honestly while I
understand gun kits I don't understand why it was made So. Annoying. To
make the fucking guns once you got everything ready. It makes it a total
annoyance. You spent 40 minutes getting all the tech for it, you
shouldn't have to also get tools and cables and wait 20 seconds standing
still.

Anyone who has played ingame like any time after that change can attest
how underused any R&D gun is now. X-ray laser guns still DESTROY blobs
but people don't even THINK about them because of the dumb annoying
recipe (alongside RnD being a pain now).

Simply put this just. Makes life easier for security officers. And
reduces tool dependency.

## Changelog

:cl:
qol: Crafting R&D guns from gun kits no longer requires tools or cable
coil. The decloner and energy crossbow still need reagents.
qol: Halved R&D gun crafting time. 20->10 seconds.
/:cl:

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[68b6c1fa75...](https://github.com/DesmontTiney/tgstation/commit/68b6c1fa753a4ae33cbe2d2a603041db4abdc7cf)
#### Wednesday 2023-10-25 00:47:06 by RikuTheKiller

Rounded supermatter delamination times to 5 seconds, restored old mood messages (#78335)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Makes the supermatter delaminate in 15 seconds instead of 13 and 5
seconds instead of 3 if a sliver has been taken from it, mainly to
please perfectionists (me and some others who commented on the PR) as
well as giving people at least a chance to escape delam round removal.

I don't like it when flavorful text is replaced by bland and
not-as-funny alternatives.
Also, how the hell is it gamey for staff to know the engineers are in
charge of the power?
It's honestly more gamey for them to know what a resonance cascade or
supermatter delamination is, so I'd say you've done the opposite of what
the goal was with the message changes on top of making them less fun in
general. I disapprove.

Oh, yeah, and the SM now reports the times correctly due to it reporting
them every 5 seconds, meaning people would only see the 10 second
announcement. Now there is going to be a 15 second announcement as well.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Watering down messages to be bland is just, like, less fun, ya know?
I didn't see a single person in support of the message changes apart
from the PR author, everyone else was just complaining about them,
including myself.

Also, several people mentioned the fact it could just be 15 instead of
13 for a nice round number, including myself. I also made the sliver
delamination time 5 seconds instead of 3 seconds because you pretty much
can't get out in time, especially if the game is laggy. 3 - 5 people
being round removed because of one traitor objective with no chance to
escape it is just bad gameplay.

Oh, and, bugfix good, I suppose.

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
balance: Supermatter now takes 15 seconds to delaminate normally and 5
if a sliver has been taken from it. Gives a little more time to escape
in the case of the sliver and also evens out the times to please
perfectionists.
fix: Supermatter now accurately reports it's detonation time.
spellcheck: Supermatter mood descriptions have been reverted back to
their old, more flavorful selves.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [CS4800-2023FALL-Group4/WarriorDiningTest](https://github.com/CS4800-2023FALL-Group4/WarriorDiningTest)@[f948e2c984...](https://github.com/CS4800-2023FALL-Group4/WarriorDiningTest/commit/f948e2c984c82777fe72704790260fb896352be2)
#### Wednesday 2023-10-25 00:48:19 by Dan C

commit
- Added a scroll view with the breakfast menu inside, need to work on menu items once JSON parsing is finished.
- Since there are three tabs for breakfast, lunch, and dinner, other members could take say lunch and dinner and make menu classes for them (if we're really hurting for classes others can do).

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[9d69f3aecf...](https://github.com/realforest2001/forest-cm13/commit/9d69f3aecf6a0070861688c5648479e8db6b679d)
#### Wednesday 2023-10-25 00:49:04 by fira

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
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[e4c3900e4f...](https://github.com/realforest2001/forest-cm13/commit/e4c3900e4f087444308138e9d05b4da9c774f6a9)
#### Wednesday 2023-10-25 00:49:04 by riot

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
## [TwistedGiraffe/RP-0](https://github.com/TwistedGiraffe/RP-0)@[d1c1ff1f43...](https://github.com/TwistedGiraffe/RP-0/commit/d1c1ff1f437a3d22a95a08f9bc64602304df6279)
#### Wednesday 2023-10-25 00:56:18 by Blothorn

X-Planes overhaul (#2198)

* X-Planes overhaul

As much as I like planes, I have a few frustrations with the X-Planes contracts/program--some going back to legacy, some new with PLC.
- It's somewhat tedious. Despite not having any unlimited repeatables, a full completion of the program involves about 30 flights--even ignoring the levels of SS High that require High-speed Flight or above. This is quite a lot of flight time, and much of it non-AFK game time for the many people who haven't fully automated these flights. (Also, the high number of cooldown contracts combined with crew training requirements can require a lot of bookkeeping.)
- There isn't a lot of variety. All missions are basically either "hold X speed with a jet" or "reach X altitude with a rocket plane"--the only deviation being the rocketplane development contracts that somewhat constrain the flight path to reach an altitude. It's possible, and in PLC quite attractive, to complete the program with two planes, each optimized for a single mission profile, and one of which repeats the exact same kOS script over a dozen times.
- The funding fits awkwardly within PLC. Now that crewed orbit is split, no program comes close to the time and tech range--the first handful of missions can be easily completed in the first year, while the last requires post-orbital tech. This means that from start to finish the opportunity cost of the program slots increase considerably, and thus its funding is only competitive for a fairly narrow range of start dates and speeds--most of which require painful compromises. (And I think it's actually more expensive to run than an SR program--almost all of the tech required is dead-end tech you could otherwise skip without issue, and hiring a pilot in the first year is a significant expense. Meanwhile, since you need to complete an SR program to advance and both overlap heavily in tech and LC requirements, you save very little from only taking one.

I've attempted to address this from a few directions. I think these are largely separable if you think some but not others are good ideas; I've lumped them in this PR so I don't have to also balance them separately.
- Split the program into an early program (roughly covering the X-1 through X-3 missions) and a late program (X-15). This allows people to start planes late while still seeing X-15 funding while it's still vaguely competitive. (Particularly attractive to double SR/heavy sat playthroughs where you need to wait for either two admin upgrades or finishing both SR programs to take early.) I considered further splitting early into 1-point jet and rocket programs to appease people who are bored of jets, but I think that would make taking at least one of the plane programs at the start to fill out the fifth program slot much too attractive.
- Reduce the number of missions--this cuts the Supersonic and 80km Altitude milestones, reduces the repetitions of most optional missions by 30-50% by increasing the gap between contracts, and bumps up some reputation rewards to partially make up for the reduced count.
- Add some new missions. The Stratospheric Research missions are modeled on the cover story for the U-2, and I think provide an interesting design challenge that doesn't consist of optimizing the wave-drag coefficient. The hypersonic research missions are modeled on the high-speed low-altitude X-15 flights, and probably don't change plane design much but at least provide something different to do.

Aside from contract testing, I've done a partial career taking X-planes at the start. I still think that's suboptimal; hiring an astronaut or two and adding at least one point of research that doesn't benefit sounding rockets can't compete with the synergy between the SR programs. However, the reduction in confidence for the smaller program and better first-year funding feels a lot better than the current slow start. I think the situation will be somewhat better for careers taking it alongside sounding rockets after an admin upgrade. I expect the X-15 program is somewhat undertuned--if you take it in late '52 it's respectable money through 53 and 54, but after FO it blocks the targeted/comms satellite programs that are even more lucrative despite being single-slot programs--but I haven't tested that stage enough to dare push it higher.

* Actually fix the hypersonic contracts

* Implement suggestions

* Add missing optional

* Tweak funding curve

* Re-add the hypersonic required flight

* Revert rebase errors

* Bump mach 2 science and update program rep/confidence.

---------

Co-authored-by: Ian Sturdy <sturdyi12@mail.wlu.edu>

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[ae41c46c50...](https://github.com/Zytolg/tgstation/commit/ae41c46c50b59f8e9d83ac5d413784420af02f97)
#### Wednesday 2023-10-25 00:59:40 by Time-Green

Only double HCR for impressive greentexts (#78383)

There were a few exploits with free antags that would double your score.
This happened to me once by accident, but anyone could essentially
guarantee a point doubling.

I've changed the whole thing to only work for:
- Traitor
- Changeling
- Heretic
- Blood brother
- Headrev
- Wizard (you could get this with die of fate)
- Obsessed
- Magic and gun survivalists
- Holding the greentext book (because a cripple fighting for their life
for the greentext just seems funny and is rare enough)

Notably, revolutionairies, cult converts and brainwashed now no longer
pay out. Cult is pointless since you can't greentext without gibbing
(trust me I tried) and revolutionairy takes no effort other than having
strong teammates and doing nothing. There are a lot of other antags this
excludes, but those are mostly midrounds and non-humans (which are by
default excluded)

:cl:
balance: Only traitor, changeling, heretic, blood brother, headrev,
wizard, obsessed, magic/gun survivalists and greentext book holders can
now double their hardcore random score
qol: Redtexting as antag with hardcore random score will pay you default
points, instead of none (normal survival rules)
fix: End report screen will properly report hardcore random survival in
case of station destruction
/:cl:

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[78842d1180...](https://github.com/Sonic121x/Skyrat-tg/commit/78842d1180f29bf79225dce42fa1efa2759801fe)
#### Wednesday 2023-10-25 01:00:09 by SkyratBot

[MIRROR] Adds missing default biotypes to some damage procs [MDB IGNORE] (#24461)

* Adds missing default biotypes to some damage procs (#79102)

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

* Adds missing default biotypes to some damage procs

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [ChewieTea/Bagel-Merch](https://github.com/ChewieTea/Bagel-Merch)@[10e3a7dd9d...](https://github.com/ChewieTea/Bagel-Merch/commit/10e3a7dd9dda7df27428776f3b91d1a78af767f3)
#### Wednesday 2023-10-25 01:03:43 by ChewieTea

Comment

A small issue when hosting the website through GitPages.

Apparently GitPages runs on Linux, which cares about case sensitivity. Since i like JS i've been using the syntax in my file names as a joke but now it's biting me in the ass and not loading the images in my "/imageBank/merchModels" because of that.

So we're going to fix that, like it says.

I can't wait.

I just can't wait for this.

It's going to be so much fun.

Honestly the highlight of my day.

What could be better than going over all the code you've worked on for the past 2 weeks+ and making sure each file is lowercase.

The dream really.

---
## [francope41/UI_PantryParcel_Project](https://github.com/francope41/UI_PantryParcel_Project)@[370a393f7f...](https://github.com/francope41/UI_PantryParcel_Project/commit/370a393f7fd1ddb1de69cd5aa149a5aa288cea87)
#### Wednesday 2023-10-25 01:37:29 by sumivengalot

Add files via upload

Corn Flakes Breakfast Cereal
Brand : Kellogg's Corn Flakes Breakfast Cereal,
Price : $4.98 each
Availability : 150 packs

Description:
Greet your morning with Kellogg’s Corn Flakes cereal, a healthy, delicious breakfast cereal that helps you start the day right. Includes one, 18-ounce box of this classic family favorite cereal, perfect for kids and adults. Made to enjoy by the bowlful, each serving contains a good source of eight vitamins and minerals, is fat free, and contains no artificial colors or flavors; You can also use these flakes to prepare numerous sweet and savory dishes. Kellogg's Corn Flakes can be used whole and incorporated into casseroles, crushed for your favorite Corn Flakes Crusted Chicken recipe, or added to a yogurt parfait for some extra crunch. Just add your favorite dairy or nut milk to Kellogg’s Corn Flakes, the Original and Best.

---
## [JamesMcGowan123/homebrew](https://github.com/JamesMcGowan123/homebrew)@[6ce58fc74c...](https://github.com/JamesMcGowan123/homebrew/commit/6ce58fc74cefafadf43e9481dac8497c584bd255)
#### Wednesday 2023-10-25 01:45:29 by JamesMcGowan123

Add files via upload



After much toil and trouble, the early version of our witch class is finally here and available to you, our beloved patrons!! A lot of care and deliberation went into developing the class for Erika to use, and we’ve been so eager to share it with you all and hear what you think.

We have to stress that this is an early draft of the class mechanics—it hasn’t been thoroughly playtested (you’ve basically heard the extent of it on the podcast), so GMs should be fully aware of that before allowing it to be used in their games.

Because of this, we’ll be seeking feedback from the Patreon in a month or two, once people have had some time to play the class and test it out. We don’t expect feedback, but if you decide to try it out and are willing to share some thoughts, we’d love to hear from you, so keep an eye out!

Big thanks to everyone who helped us put this together, including designers Mazey Veselak, Brandes Stoddard, and Hannah Rose; layout artist Ruby Lavin; illustrators Corey Brickley, Tucker Donovan, and Taylor Moore; and original character illustrator Lorena Lammer.

---
## [PraneshVats/HTML-Projects](https://github.com/PraneshVats/HTML-Projects)@[c69b821294...](https://github.com/PraneshVats/HTML-Projects/commit/c69b821294ec39fe5395e3d5329ae4203c6c0ba6)
#### Wednesday 2023-10-25 01:50:52 by Pranesh Vats

Add files via upload

Spotify Clone # HTML Spotify Clone Website
Overview
The HTML Spotify Clone Website is a project designed to replicate the look and feel of the popular music streaming platform, Spotify. This website aims to provide a simplified version of Spotify's user interface, allowing users to explore and play music tracks, create playlists, and enjoy a seamless music streaming experience.
Key Features
1. User Authentication: Users can create accounts, log in, and manage their profiles, complete with a user profile picture.

2. Music Library: A vast collection of music tracks categorized by genres, artists, and albums.

3. Search and Discover: Users can search for their favorite songs, artists, or albums, and explore music recommendations based on their listening history.

4. Playlists: Users can create and manage custom playlists, add or remove songs, and share their playlists with others.

5. Music Player: A functional audio player that allows users to play, pause, skip, and control the volume of tracks.

6. Responsive Design: Ensures the website adapts to different screen sizes and devices for an optimal user experience.

7. Album Art and Lyrics: Displaying album cover art and lyrics for the currently playing track.

8. User Interaction: Users can like and save their favorite songs, as well as follow their preferred artists.

9. Dark Mode: An option to switch between light and dark themes for visual comfort.

10. Simplified Backend: Although this is an HTML clone, it can be enhanced by integrating a backend for user accounts, playlists, and recommendations.

 Technologies Used
#HTML5: The backbone of the website's structure and content.
#CSS3: Styling the website to match the Spotify aesthetic.
#JavaScript: To add interactive features, control the audio player, and handle user interactions.

 Purpose
The HTML Spotify Clone Website project is primarily for educational purposes and as a demonstration of web development skills. It provides an opportunity to learn and practice HTML, CSS, and JavaScript while creating a user-friendly interface inspired by a well-known online platform.

Please note that this project is a clone and does not include actual music streaming. It is a starting point that can be expanded upon by adding additional features, a backend server, and integrating with APIs to fetch real music data.

---
## [UBCFormulaElectric/Consolidated-Firmware](https://github.com/UBCFormulaElectric/Consolidated-Firmware)@[48ee00ec77...](https://github.com/UBCFormulaElectric/Consolidated-Firmware/commit/48ee00ec772e45a997365bdf7dadaecc117a31e9)
#### Wednesday 2023-10-25 02:03:16 by Gus Tahara-Edmonds

Make CAN signal names unique (#1019)

### Summary
<!-- Quick summary of changes, optional -->

Currently CAN signal names are not unique. This is not a problem when
using PCAN or writing code, since signals are categorized by their CAN
message. However, this is not the case when uploading data to Influx,
since then only signal names are uploaded. This means that there are
weird conflicts between signals of the same name. For example, `State`
for the BMS and the DCM.

This PR changes so signal names are prefixed by their board, and then we
enforce all signals are unique across all boards. To avoid ridiculously
long CAN setters/getters in the firmware, only the signal name is now
used.

For example:
| | Before | After |

|-----------|--------------------------------------------|---------------------------------|
| Message | `BMS_Contactors` | `BMS_Contactors` |
| Signal | `AirPositive` | `BMS_AirPositive` |
| TX Setter | `App_CanTx_BMS_Contactors_AirPositive_Set` |
`App_CanTx_BMS_AirPositive_Set` |

The board name prefixes are also now added automatically to
messages/signals, so they've been removed from the `*_tx.json` files.

### Changelist 
<!-- Give a list of the changes covered in this PR. This will help both
you and the reviewer keep this PR within scope. -->

- Change `jsoncan` Python to support these changes
- Rename all signals
- Removed a few unused signals

Note: This diff is huge because of the autogenerated example code in
`jsoncan`. I should really remove this and add proper unit tests
instead.

### Testing Done
<!-- Outline the testing that was done to demonstrate the changes are
solid. This could be unit tests, integration tests, testing on the car,
etc. Include relevant code snippets, screenshots, etc as needed. -->

- [x] Validated on car

### Resolved Issues
<!-- Link any issues that this PR resolved like so: `Resolves #1, #2,
and #5` (Note: Using this format, Github will automatically close the
issue(s) when this PR is merged in). -->

### Checklist
*Please change `[ ]` to `[x]` when you are ready.*
- [x] I have read and followed the code conventions detailed in
[README.md](../README.md) (*This will save time for both you and the
reviewer!*).
- [x] If this pull request is longer then **500** lines, I have provided
*explicit* justification in the summary above explaining why I *cannot*
break this up into multiple pull requests (*Small PR's are faster and
less painful for everyone involved!*).

---
## [clemyan/berry](https://github.com/clemyan/berry)@[9c3dc22b7e...](https://github.com/clemyan/berry/commit/9c3dc22b7e3c2a2c0782ee1222b4cf9ac6a2846f)
#### Wednesday 2023-10-25 02:09:54 by Maël Nison

Implements enableOfflineMode (#5710)

**What's the problem this PR addresses?**

We didn't have a good story for people performing local development on
their projects while under network-constrained environments. I'm myself
working from trains from time to time, and each time it always come a
point where I want to do a quick repro with one package or another, but
since I don't have network it's a pain.

**How did you fix it?**

A new `enableOfflineMode` setting tells Yarn to reuse the metadata
stored in the cache, even if they may be stale (a good feature reuse of
the logic @paul-soporan's originally made for perf reasons!).

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
## [Kyogon/Skyrat-tg](https://github.com/Kyogon/Skyrat-tg)@[c056f4dac9...](https://github.com/Kyogon/Skyrat-tg/commit/c056f4dac9e4649a960be5d6331b110c89f3080e)
#### Wednesday 2023-10-25 02:21:46 by SkyratBot

[MIRROR] Nanotrasen basic mobs. [MDB IGNORE] (#24573)

* Nanotrasen basic mobs. (#78917)

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

* Nanotrasen basic mobs.

* Modular

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [KSrikari28/MotionCutInternshipProjects](https://github.com/KSrikari28/MotionCutInternshipProjects)@[0c320adaaa...](https://github.com/KSrikari28/MotionCutInternshipProjects/commit/0c320adaaa4d691f820c21765e0f0475ea0e2880)
#### Wednesday 2023-10-25 02:37:19 by KSrikari28

Add files via upload

This is my fourth week project of my internship at MotionCut. This is a quiz platform- Bookish Trivia which is a quiz platform on literary novels under different categories such as Fiction, Non-Fiction, Thriller, Mystery and Fantasy. The platform is very user friendly and has features such as score,leaderboard and also displaying the correct answer if the chosen is wrong immediately. 
Languages used:
HTML: HTML has been used for creating the basic structure of the website.
CSS: CSS has been used to style the website as per the requirements to make it user friendly and seamless.
JavaScript: JavaScript has been used to add all the required functionalities to the website such as score calculation, leaderboard and marking the correct and wrong answer.

---
## [francope41/UI_PantryParcel_Project](https://github.com/francope41/UI_PantryParcel_Project)@[bc351ed2ad...](https://github.com/francope41/UI_PantryParcel_Project/commit/bc351ed2ad368ca0a63082e4e7d36951023a2ea8)
#### Wednesday 2023-10-25 03:21:19 by sumivengalot

Add files via upload

Name: Dark Chocolate Candy
Price : $5.70 each
Available Qty : 100 nos
Brand  : Dove
Description: Experience the pleasure of Dove Promises Silky Dark Chocolate Candy. Every bite of enjoyment is crafted with natural ingredients and the highest quality cacao: a match made in heaven. This 8.46-ounce resealable bag of individually wrapped, Dove Promises dark chocolates are a holiday candy must. Whether you use them for baking holiday favorites, self-treating, or premium gifting, these dark chocolate delights will be adored and appreciated all season long. Spread the love with friends and family by sharing a bag of Dove Promises Dark Chocolate party candy or party favors at the holidays and during celebrations. Each candy comes individually wrapped in elegant foil with a special message inscribed on the inside. Whether eaten as a delightful treat or as a deliciously simple dessert recipe, these iconic dark chocolates will make you feel indulgent and pampered.

---
## [francope41/UI_PantryParcel_Project](https://github.com/francope41/UI_PantryParcel_Project)@[bb1c5f8c03...](https://github.com/francope41/UI_PantryParcel_Project/commit/bb1c5f8c03a675b5fc2419a54c173c6d1477b7c0)
#### Wednesday 2023-10-25 03:24:57 by sumivengalot

Add files via upload

Name: Lindt Lindor Dark Chocolate Truffles
Price :  $4.95 each
Available Qty : 65 
Brand  : Lindt
Description: Do you dream in chocolate? Then discover Lindor and enjoy a moment that is yours: When you break Lindor's delicate chocolate shell, the irresistibly smooth filling starts to melt, gently caressing all your senses and taking you to a place where chocolate dreams come true .Perfectly balanced dark chocolate offers a deeply indulgent premium chocolate experience. A delicate dark chocolate shell enrobes an irresistibly smooth dark chocolate center.

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[af47d2ef41...](https://github.com/unit0016/effigy-se/commit/af47d2ef41fdb933a2a8ed365e719b57318c26ec)
#### Wednesday 2023-10-25 04:14:30 by lizardqueenlexi

Basic Constructs: Artificer (#79015)

## About The Pull Request

Really getting into the meat of the constructs now. Artificers have
become basic mobs.

On the whole, this was a pretty rote conversion, with no significant
gameplay changes other than the switch to using healing hands rather
than a unique heal ability. The player experience as an artificer is
more or less identical.

The _interesting_ part comes with the AI for the seldom-used "hostile"
variant. Hostile artificers, being squishy and laughably weak, are now a
dedicated "medic" role for constructs. They will perform triage, always
seeking the most wounded construct (or shade!) to give healing to. They
will not attack at all, but they _will_ flee with great speed if
attacked and not busy healing. If they are healing another construct,
they will remain even if they are beaten to death.

I've added some more AI functionality that may come in handy in the
future, and done some refactoring to keep things from getting out of
hand:
- A planning subtree for finding targets that will always select the
most heavily wounded living target that the mob can see (or rather, the
one with the least health). Useful again for medical triage, or for
making a particularly cruel mob that always attacks whoever is easiest
to kill. I plan to use this for NPC wraith constructs when I convert
them.
- Targeting datums can now check a blackboard key to see if they should
only target wounded mobs. This is particularly useful for "medic" type
mobs such as this one.
- I've refactored the "minimum stat" behavior of targeting datums to be
stored in a blackboard key. This removes the need to have unique
subtypes for each different minimum stat we might want. Which... for the
most part, weren't even used, leading to proliferation of several
completely identical targeting datums in a bunch of different files.
Hopefully this change will make things cleaner.

In addition, this PR fixes a pair of bugs from #78807 that I didn't
catch:
- Healing constructs can now actually heal shades. Turns out I forgot to
add the correct biotype.
- Healing hands, when set to print the target's remaining health, no
longer does so as a visible message.

The one thing I didn't do that I kind of wanted to is make NPC
artificers heal themselves when wounded and not busy doing something
else, but it ended up being kind of annoying to make a mob willingly
target itself. NPC artificers never had this behavior before, so I
consider it okay, but maybe I'll circle back to it later.
## Why It's Good For The Game

Another basic conversion, another 5 items off the checklist. Very little
should change in-game, though I think the new NPC AI could make for
interesting challenges in ruins or bitrunning or something.
## Changelog
:cl:
refactor: Artificer constructs have been converted to the basic mob
framework. This should change very little about them, but please report
any bugs. NPC artificers are now smarter, and will focus on healing
nearby wounded constructs - if you see them, take them out first!
/:cl:

---
## [BurgerLUA/Bubberstation](https://github.com/BurgerLUA/Bubberstation)@[f1169ed555...](https://github.com/BurgerLUA/Bubberstation/commit/f1169ed5555f58d716b1ec314408c73027a71c17)
#### Wednesday 2023-10-25 04:15:19 by Waterpig

Removes the shitty skyrat "Realism" change that just stops your heart when you get shocked (#620)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
See name

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Realism is cool and all but random chance to just die from any shock
that can damage you is annoying as all hell, and randomness that can
instakill simply isn't fun.
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
del: Shocks no longer have a chance to kill you
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MalleeFoul/Homebrew-zrythm-reqs](https://github.com/MalleeFoul/Homebrew-zrythm-reqs)@[cc89ae5a82...](https://github.com/MalleeFoul/Homebrew-zrythm-reqs/commit/cc89ae5a820775d988dd03a3ed515128eb617a18)
#### Wednesday 2023-10-25 04:44:17 by MalleeFoul

Oh thank god
I think it actually works now holy shit!

---
## [janakniraula/frameworks_base](https://github.com/janakniraula/frameworks_base)@[056b297711...](https://github.com/janakniraula/frameworks_base/commit/056b2977119514add1abe1cf86878a6fccd1c6b8)
#### Wednesday 2023-10-25 04:50:49 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [tempest2k/hsmusic-data](https://github.com/tempest2k/hsmusic-data)@[3ebd44e0a3...](https://github.com/tempest2k/hsmusic-data/commit/3ebd44e0a3b53e28cc860996a4fbe706c2fdd22d)
#### Wednesday 2023-10-25 04:56:45 by tempest2k

fixed Vilcus tag

I'm fucking idiot. hello viewer twelve years from now checking the history of the hsmusic wiki git repository. please always remember that I'm fucking idiot.

---
## [Treachce/tgstation-master](https://github.com/Treachce/tgstation-master)@[ece51a1a9d...](https://github.com/Treachce/tgstation-master/commit/ece51a1a9d6896a54b878563d9c33002bc8f3688)
#### Wednesday 2023-10-25 05:07:41 by nikothedude

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[13e5bc3ff0...](https://github.com/treckstar/yolo-octo-hipster/commit/13e5bc3ff01ab67792d5a1a2a7463e7c25dbd4a1)
#### Wednesday 2023-10-25 05:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Chanda-yeswanth-reddy/stock-price-viz-tool](https://github.com/Chanda-yeswanth-reddy/stock-price-viz-tool)@[2d670f0e09...](https://github.com/Chanda-yeswanth-reddy/stock-price-viz-tool/commit/2d670f0e0965a49de37a3fc3e603dc8bcdd509b8)
#### Wednesday 2023-10-25 07:36:20 by Chanda Yeswanth Reddy

Add files via upload

Here are some key highlights of this project:

1️⃣ Data at Your Fingertips: The Stock Price Visualization Tool allows you to explore stock market data in an interactive and user-friendly way, thanks to Plotly's robust data visualization capabilities.

2️⃣ Customizable Timeframes: With this tool, you have the flexibility to select the specific time or month of stocks you want to analyze, giving you greater control and insights.

3️⃣ Effortless Access: No need for complex installations or downloads. Access the tool online through Mercury's seamless deployment platform, ensuring high availability and performance.

4️⃣ User-Centric Design: The focus here is on simplicity and ease of use, making it accessible to everyone interested in stock market analysis, regardless of their level of expertise.

Whether you're an investor, trader, or simply someone curious about stock market data, this tool is designed to provide you with an insightful and visually pleasing experience. I invite you to explore it and share your thoughts.

---
## [cc-tweaked/CC-Tweaked](https://github.com/cc-tweaked/CC-Tweaked)@[6656da5877...](https://github.com/cc-tweaked/CC-Tweaked/commit/6656da58770887a30fc2617ceb236d3dadfc21c4)
#### Wednesday 2023-10-25 08:07:17 by Jonathan Coates

Remove disable_lua51_features config option

In practice, we're never going to change this to true by default. The
old Tekkit Legends pack enabled this[^1], and that caused a lot of
problems, though admittedly back in 2016 so things might be better now.

If people do want this functionality, it should be fairly easy to
replicate with a datapack, adding a file to rom/autorun.

[^1]: See https://www.computercraft.info/forums2/index.php?/topic/27663-

      Hate that I remember this, why is this still in my brain?

---
## [AJITH538/Portfolio](https://github.com/AJITH538/Portfolio)@[8b519ce156...](https://github.com/AJITH538/Portfolio/commit/8b519ce156d66bb48ee9b11d03b75905c8b440f9)
#### Wednesday 2023-10-25 09:05:32 by AJITH538

Add files via upload

GitHub Portfolio: 

Welcome to my GitHub portfolio! Here, you'll find a collection of my personal and professional projects, showcasing my skills, interests, and contributions to the world of software development. I'm passionate about technology and innovation, and I'm always exploring new ideas and challenges.

What You'll Discover in My Portfolio:

Web Development: Explore my web development projects, including responsive websites, web applications, and interactive web experiences. I work with HTML, CSS, JavaScript, and various web frameworks and libraries.

Data Science and Machine Learning: Dive into my data analysis, machine learning, and AI projects. Discover how I leverage data to solve real-world problems and build predictive models.

Open Source Contributions: I actively contribute to open source projects. See how I collaborate with the community and make a positive impact on various repositories.

Coding Challenges: I enjoy participating in coding challenges and competitions. Check out my solutions to problems from platforms like LeetCode, HackerRank, and Codeforces.

Software Tools: View my utility scripts and tools that I've developed to make life easier for developers and automate repetitive tasks.

Feel free to explore my projects, provide feedback, and get in touch if you have any questions or collaboration opportunities. I'm always open to new ideas and challenges!
Thank you for visiting my GitHub portfolio. I hope you find my work interesting and inspiring. Don't hesitate to reach out if you'd like to connect or collaborate.

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[c3d2abf109...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/c3d2abf109ea24194f29f0006d1f26c021a448f7)
#### Wednesday 2023-10-25 10:07:54 by Ruchit

sm7125-common: Disable blur by default

Holy shit snapdragon 720g is awful

---
## [dcfidalgo/argilla](https://github.com/dcfidalgo/argilla)@[b2073f9262...](https://github.com/dcfidalgo/argilla/commit/b2073f926247cd6b1255c6e4919d77ba4d414c21)
#### Wednesday 2023-10-25 10:48:50 by Sara Han

docs: cheatsheet fixing typos gramamar and urls (#3867)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

Fixing the grammar, typos and URLs of the Cheatsheet. It also fixes the
dead URL of the common file, as it appears here too

Closes #3865 

**Type of change**

(Remember to title the PR according to the type of change)

- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [X] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [ ] I added relevant documentation
- [X] I followed the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [Aachlyss/RunGroupWebApp](https://github.com/Aachlyss/RunGroupWebApp)@[a7bf53c41c...](https://github.com/Aachlyss/RunGroupWebApp/commit/a7bf53c41cf2790f1b72a80e8c63ba3634c13627)
#### Wednesday 2023-10-25 11:08:30 by Aachlyss

Club View Update

Updated Club View so that it shows the exact number of clubs in the DB and display that number of cards for each one. (I hate my life)

---
## [SudharsanSundar/beyond-scale-SS-fork](https://github.com/SudharsanSundar/beyond-scale-SS-fork)@[4953161976...](https://github.com/SudharsanSundar/beyond-scale-SS-fork/commit/495316197635763566ef271db1cdf2f7512934cd)
#### Wednesday 2023-10-25 11:43:58 by Brando Miranda

Create plan_div_performance_ginc.md

# Experiment Plan: The Effect of Diversity on Downstream Performance 

## Goal

Essential Goal: Does pre-training on a highly diverse data set lead to high performance on pre-training evaluation sets?
(note: it's more of a causation than a correlation experiment).

## Experiment Plan 1: Concepts in pre-train set intercepting concepts in test set

1. Fix an eval synthetic GINC data set with 10K concepts (~0.024 diversity coeff. with probe network ... TODO1: what is the probe network? whatever ginc alycia used should be fine),
denote it as `C_{test, 10k, ginc}` and generate a data set `D_eval = D_{test, 10k, ginc}` with `n= ?` examples (TODO2 same as alycia's, or original ginc or something that seems reasonable, if I had to guess at least 30 due to CLT but would choose 500 or a sample complexity guess from learning MHHMs or ask Michael original ginc author)`. 
2. Sample `k <= 10K` concepts from `C_{test, 10k, ginc}` to generate a pre-training data set `D_{tr, k, ginc}` using concpets `C_{tr, k, ginc}`.
3. Compute the diversity of the data set of the previous step and denote it as `div_k = div(D_{tr, k, ginc})`.
4. Pre-train a sufficiently large (e.g., deep) transformer model (TODO3: whatever alycia, michael used for ginc, I think it's a custom GPT/decoder model? I strongly recommend a decoder model)
5. Now start plotting 
   6. A (Ess): `x-axis = div_k vs y-axis = performance_i(D_eval)` (tests main hypothesis/essential goal)
   7. B (Ess): `x-axis = align(D_k, D_eval) vs y-axis = performance_i(D_eval)` (sanity check, tests `if as the alignment in pre-train & test set increases ==> increase in performance`)
   8. C (Ess): `x-axis = div_k  vs align(D_k, D_eval)` (sanity check, `if the diversity increases then ==> increases probability of covering test sets which ultimately ==> increases alignment`)
   9. (D (extra): `x-axis = delta in alginment(D_k', D_eval) vs performance_i(D_eval)` (hypothesis, does the most aligned data added cause the most increase in performance?))
   10. (E (extra): `x-axis = div vs ground truth div` (sanity check div correlates with ground truth div))

Then repeat from step 2 but with a different `k` until `k==10k`. 
Alignment is how aligned is the pre-train & test sets with formulas 
- `alg1(D_k, D_eval) = 1 - div(D_k, D_eval) = 1 - E_{B1 ~ D_k, B2 ~ D_eval}[d_cosine(e_{B1}, e_{B2})]`
- `alg2(D_k, D_eval) = d_cosine(e_{D_k}, e_{D_eval})`

Where `e_{D}` is the Task2Vec embedding (diagonal of the FIM of probe network).

Hypothesis being tests, Rational:
- First let's validate/falsify that if the train set has latent concepts samples exactly from the concepts from the test set, if the eval. performance increases. 
  - Sanity check: This is the simplest scenario, if this doesn't work, it might still be worth sampling different concepts to generate the data set, but I wouldn't expect the latter to work, right?
- test if diversity increase ==> performance eval 
- Sanity Check: as `div increases ==> alignment increases`?

Assumptions/Risk:
- Assumption 1: when plotting `performance_i(D_eval)` we will choose at least 3 metrics `i. ppl, ii. token edit distance (or avg token match), iii. extract string match`
- Assumption 2: the model is **sufficiently large** so that even if the diversity increases by "too much", it won't catastrophically forget or new knowledge would interfere with past knowledge.
- Assumption 3: using performance in the y-axis is enough to detect difference (statistical significant)
  - if we can't detect a difference, perhaps we can use effect size in the y-axis?
- Assumption 4: the code alycia has is easy to run + the architecture they have will be easy to train. 
  - wonder if EasyLM (llama v1 or v2 arch would be better?). Ask easy LM when they will include the better llama v2 arch
  - ask on Twitter why llama v2 trains so stably

Comments:
- note: even though the concepts intersect, the sequences are being generated independently (e.g., with a different seed), so there isn't a contamination from the pre-train set to the test set.
- note: I prefer token edit distance vs avg token match, it's similar to average token error but it's more accepted in the NLP literature (TODO: recall from Rylan why it's a good metric).
- note: **comparisons must be fair** e.g., effectively we must only change the data set (and thus diversity) in the experiments when comparing the performance of different methods. 
  - I suggest we fix: 1. arch 2. compute FLOPS (TODO4: get Rylan's formula) 3. tokens trained on/iterations 4. optimizer 5. anything else?
- not essential but if the experiments work it would be nice to have the diversities normalized in this way: `div'_k = (div_k - min_{D} div(D)) / max_{D} div(D)` i.e., center according to the lowest div divide by the largest diversity.

Decision & justifications for TODOs:
- TODO1 Ans: 
- ...

## Experiment Plan 2: Concepts in pre-train set not necessarily intercepting with concepts in test set
Essentially the same set of experiments as in `Experiment Plan 1` but step 2 changes to adding some `k'` new concepts to the current pre-training data set that not deliberately sampled from the set of concepts in the test sets.
Therefore, we are adding new random concepts to the pre-training mixture.

1. Fix an eval synthetic GINC data set with 10K concepts (~0.024 diversity coeff. with probe network),
denote it as `C_{test, 10k, ginc}` and generate a data set `D_eval = D_{test, 10k, ginc}` with `n = 500?` examples. 
2. Sample `k'` new concepts (not necessarily from `C_{test, 10k, ginc}`) to generate a new pre-training data set `D_{tr, k+k', ginc}` using concepts `C_{tr, k+k', ginc}`.
3. Compute the diversity of the data set of the previous step and denote it as `div_k = div(D_{tr, k, ginc})`.
4. Pre-train a sufficiently large (e.g., deep) transformer model
5. Now start plotting 
   6. A (Ess): `x-axis = div_k vs y-axis = performance_i(D_eval)` (tests main hypothesis/essential goal)
   7. B (Ess): `x-axis = align(D_k, D_eval) vs y-axis = performance_i(D_eval)` (sanity check, tests `if as the alignment in pre-train & test set increases ==> increase in performance`)
   8. C (Ess): `x-axis = div_k  vs align(D_k, D_eval)` (sanity check, `if the diversity increases then ==> increases probability of covering test sets which ultimately ==> increases alignment`)
   9. (D (extra): `x-axis = delta in alginment(D_k', D_eval) vs performance_i(D_eval)` (hypothesis, does the most aligned data added cause the most increase in performance?))
   10. (E (extra): `x-axis = div vs ground truth div` (sanity check div correlates with ground truth div))

Comments:
- note: as we include new data `k'`, we can compute the distance from the test set and see if the more aligned the pre-trained data we train on (add) if that predicts/causes the most increase in performance.
  - note: I wonder if we can compute how far the pre-train and test/eval sets are using (normalized?) MSE/NED of MHMMs ground truth params or hellinger distance
    - we could even provide more data for `div vs ground truth div` ! (we don't even need ground truth to be normalized, we can for visualization purposes)

### Random thoughts
Risk:
- Risk: our eval sets are bad. Tim D. mentiond to me MMLU sucks. Let's ask him why he thinks that, document it and ask him/consider using something else (?). Note, if we only have to evaluate then perhaps it's not too expensive/hard to compute eval on MMLU? 

Comments:
- note: for the real data set, let's articulate which evaluation data sets we are using and why. I propose we use at least 2 from the hugging face eval board: ARC, MMLU.
- note: make sure we know what type of eval we are doing. TODO: ask Brando to share ref. on the subtleties on evaluating LLMs e.g., HELM, etc. let's try to summarize it.

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[2ab4fa3a92...](https://github.com/psychonaut-station/PsychonautStation/commit/2ab4fa3a923a8d1930547d47110823aeed8163f4)
#### Wednesday 2023-10-25 11:53:15 by carlarctg

Heretic Rebalance -  Main Knowledge gives free Side points, reduced rune drawing time, Codex Cicatrix is easier and roundstart knowledge (#77939)

## About The Pull Request

Heretic Rebalance

Researching the Main Knowledge paths that unlock Side Paths will grant
one Side Point that can be used only on those side paths. You can still
spend normal knowledge points on them if you wish.

Rune drawing time has been reduced from 30->20 seconds. Codex drawing
time has been reduced from 15->8.

Codex Cicatrix is now a roundstart knowledge, works as an amber focus
when held in-hand and opened, and has had its recipe changed to: 1 of
any non-standard pen (literally anything that isn't the base pen), any
book, and either animal hide OR a corpse, any kind.

Added support for using a list inside ritual requirements and a special
'snowflake check' rituals can utilize.

The first non-path knowledge, the Mansus Hand Mark, has had its cost
reduced from 2->1 points.
## Why It's Good For The Game

Heretic is an extremely top-heavy antagonist that is EXCEEDINGLY weak in
the early-game, free get out of jail card aside, and gets utterly
overwhelmed with options extremely quickly once hopping past the
mid-game hurdle. You're completely starved for knowledge points to the..
point that you feel like you can't blow any on side paths, even though
these are often essential as well!


Once you hop the hurdle - 40 minutes in, usually - you suddenly find
yourself blazing through path after path obtaining a ridiculous amount
of points that you don't know what to do with and unlocking spell after
spell all at once rather than slowly, meaning it becomes extremely hard
to keep focus and actually use these things - attempting to keep 5 new
spells in mind during combat will just cause you to stretch yourself
thin and die.

This PR is meant to address this by giving Heretics a lot more leeway on
the early game so they don't feel nearly as stifled as they are right
now, which will also, ideally, help them unlock singular abilities
earlier on so they can practice with them. **None of these changes are
straight buffs to combat ability, they simply relax the extremely tight
restrictions early-game heretics have.**

> Researching the Main Knowledge paths that unlock Side Paths will grant
one Side Point that can be used only on those side paths. You can still
spend normal knowledge points on them if you wish.

This idea in specific is supported by @MrMelbert - which I'm using as a
request to not instaclose this PR due to the slightly lower than neutral
GBP I have. He supports this specific bit at least and doesn't outright
disagree with me on the rest, as far as I'm aware from my last
conversation with him on the subject a while back. Besides, I have a
refactor on mirrors open!

Meta aside, this bit is meant to combat how claustrophobic early heretic
feels by allowing the guy to pick one of two side paths for free* after
unlocking that path's equivalent of Ash Jaunt, so they have *something*
to use besides their sword and stink hand at the start.

> Rune drawing time has been reduced from 30->20 seconds. Codex drawing
time has been reduced from 15->8.

The absurdly long drawing time is just extremely arduous and
frustrating. It's way too slow but just not enough to let you zone out,
and it has a ridiculously noticeable animation the whole way through
which guarantees you being found out if you're found out midway through.
It makes heretic even SLOWER early on as they need to set up one or
several bases which takes forever.

> Codex Cicatrix is now a roundstart knowledge, works as an amber focus
when held in-hand and opened, and has had its recipe changed to: 1 of
any non-standard pen (literally anything that isn't the base pen), any
book, and either animal hide OR a corpse, any kind.

Quite the buff, but I think all of these are good changes. Codex
Cicatrix being a roundstart change lets one decide - do they want to
rush the book to get multiplied influence strength, or do they want to
get all the influences ASAP? It also lets them set up bases quicker at,
again, the cost of having a blatantly evil item inside the bag.

The Codex recipe was annoyingly complicated, requiring you to run all
around the station in yet another of Heretic's many fetch quests just
for something that used to be part of the default kit, especially with
how annoying getting animal hide can be. Now it's a lot easier to
handle.

The Amber Focus bit is just as a panic option for heretics if they get
caught without one, at least they can use the book, and wielding a book
in combat is awesome.

> The first non-path knowledge, the Mansus Hand Mark, has had its cost
reduced from 2->1 points.

I don't think there ever really was a need to gate this behind two
points, it's the very first unlockable research and it needs you to get
two influences for some reason. The reasoning is probably 'heretic setup
time so they dont start at full strength', which is solid, but is
already well handled enough by their other systems and restrictions as
mentioned in the rest of the PR.

Heretics have been on a constant trend of just.. not doing anything.
Getting caught early and flopping or never managing to do things of
note. They need changes, not because They're UnderPowered And The
Competitive Balance Is Skewed, but because it's simply not that fun to
*be* a heretic with these issues, and not that fun to FIGHT a heretic
that merelay has a stink hand, a blade, two pieces of lint in their
pocket, and a dead rat.

I also think the Ritual of Knowledge should 1. not cost points, and 2.
be split across the 33% and 66% mark and give 2 points, but that's for
another PR.

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[9073290d8a...](https://github.com/psychonaut-station/PsychonautStation/commit/9073290d8ac18476a5165c6df6dcf062b70c635a)
#### Wednesday 2023-10-25 11:53:15 by ArcaneMusic

ArCargo: Adds the Galactic Materials Stock Market V1.2 (Free Market Edition) (#78500)

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

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[db8eca7bf3...](https://github.com/psychonaut-station/PsychonautStation/commit/db8eca7bf3366a97163c0abd6574bee82bd38fd3)
#### Wednesday 2023-10-25 11:53:15 by Ghom

The fishing portal generator expansion (plus skill-chip) (#78203)

## About The Pull Request
This is a PR I worked on last month, but had to put on hold while
dealing with some pressing issues with fishing feature, minigame and
other stuff, and because I had to atomize out some of the stuff
previously present here.

I've expanded on the fishing portal generator to do something other than
dispense guppies and goldfishes. It now has multiple settings,
unlockable by performing scanning experiments for fish types, available
from the get go, which also reward a meager amount of techweb points
upon completion. The generator can now be built too. No longer it has to
be ordered from cargo.
It can also be emagged for the syndicate setting, tho right now it only
dispenses donkfish and emulsijack, both otherwise impossible to get
outside of... exodrone adventures.

The advanced fishing rod now comes with an experiment handler component,
specific to the fish scanning experiment, that automatically scans
fished content. The node to get it now requires 2000 points and the
first fish scanning exp to be unock.

A new skillchip has been added, which adds a trait that changes the icon
of the fish shown in the minigame UI, giving some clues on what the
reward will be. The same trait is also gained by reaching the master
(penultimate) level of the fishing skill.

A new fish type has been added, with its own quirks. One of these quirks
included temporarily switching movement direction of the bait.
Currently, it can only be fished in the hyperspace and randomizer
setting of the fishing portal.

Screenshots:
![fuck
yea](https://github.com/tgstation/tgstation/assets/42542238/b4c75951-fa07-44ae-99ee-f602adf8a5a4)

![radial](https://github.com/tgstation/tgstation/assets/42542238/68ff21d8-69fd-4ba5-aa58-9976b6e3282f)

## Why It's Good For The Game
The fishing portal generator is but a stale and underdeveloped prototype
of the fishing feature right now, so much I was thinking of removing it
at first. However, we also have a lot of fishes which are pretty much
unfishable, so I came up with the idea of adding new portal settings
that allow people to actually get them.

As for the skillchip and trait, it's but an extra to both the vending
machine in the library and the fishing skill itself, which has an
overall humble impact on the minigame.

## Changelog

:cl:
add: Expanded the fishing portal generator. It now comes with several
portal options that can be unlocked by performing fish scanning
experiments, which also award a modest amount of techweb points.
balance: The fishing portal generator is now buildable and no longer
orderable. The board can be printed from cargo, service and science
lathes.
balance: Advanced fishing tech is no longer a BEPIS design. It now
requires the base fish scanning experiment and 2000 points to be
unlocked.
add: The advanced fishing rod now comes with an incorporated
experiscanner specific for fish scanning.
add: Added a new skillchip that may change the icon of the "fish" shown
in the minigame UI to less generic ones. Reaching master level in
fishing also does that.
qol: The experiment handler UI no longer shows unselectable experiments.
/:cl:

---
## [FlufflesTheDog/tgstation](https://github.com/FlufflesTheDog/tgstation)@[26e3ea1e0d...](https://github.com/FlufflesTheDog/tgstation/commit/26e3ea1e0d185439d792a6890e9eb041f8aadfdf)
#### Wednesday 2023-10-25 12:08:24 by John Willard

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
## [FlufflesTheDog/tgstation](https://github.com/FlufflesTheDog/tgstation)@[10f194781d...](https://github.com/FlufflesTheDog/tgstation/commit/10f194781db0a6b2e71d2769a07fca7d5960c21f)
#### Wednesday 2023-10-25 12:08:24 by Jacquerel

It is now possible to survive the Mansus  (#79131)

## About The Pull Request

Fixes #79113

There were a handful of bugs with the Mansus realm, this PR fixes them.

Firstly an most importantly, a refactor to damage handling touched the
"unholy determination" effect incorrectly (and I'm not even sure why?),
causing it to damage you instead of healing you most of the time. This
damage was not avoidable, so most people would be crit shortly after
entering the area and stay there.

Secondly, some of the heretic realms were unlit. A change to when
lazyloaded template atmosphere initialises means that the bonfires were
trying to light themselves with no air. Now they do this in
late_initialize instead, giving time for air to arrive.

Thirdly, the spooky hands were runtiming when passing through transit
tiles outside of the bounds of the heretic map. They shouldn't be
effected by shuttle drag anyway, so now they aren't.

Fourthly, I removed a row of empty space at the edge of the heretic map,
just because it annoyed me slightly.

Finally, while I was touching the heretic buff I made it heal you 1/4 as
much as it originally did. This is a balance change rather than a fix,
I'll atomise it out if it is controversial but I don't really expect it
to be.
In the future I would like to come back to these and make each realm
more specific to the path, because I think we could make these both more
exciting and more characterful.

## Why It's Good For The Game

Once it is working properly, the hand dodging minigame is actually
extremely forgiving, even if you don't move very much and get frequently
hit. This means some of those hits might actually add some tension.

## Changelog

:cl:
fix: You should be revived properly when entering the mansus realm
following a heretic sacrifice
fix: The buff which is supposed to heal you in the mansus realm will now
do that instead of unavoidably damaging you
balance: The mansus realm's healing buff heals for 25% as much as it did
before it was broken
/:cl:

---
## [Slouserg/wazuh](https://github.com/Slouserg/wazuh)@[9e401d3445...](https://github.com/Slouserg/wazuh/commit/9e401d34451a0e314863839786d3eadf8f801549)
#### Wednesday 2023-10-25 12:25:13 by Slouserg

Create wazuh-install-script.sh

This commit introduces the `wazuh-install-script.sh`, an automation script to streamline the installation of Wazuh, the open-source security monitoring platform. This script is created by Knippin ICT and simplifies the setup of the Wazuh manager (server), Wazuh indexer, and Wazuh dashboard.

**Key Features:**

- Automates the installation process, reducing manual configuration steps.
- Prompts the user for LAN IP addresses, allowing for easy customization.
- Downloads the latest `config.yml` from the Wazuh repository.
- Sets up the Wazuh manager, indexer, and dashboard seamlessly.
- Provides a straightforward and user-friendly installation experience.

**Usage:**

1. Clone or download the script from this repository.
2. Make the script executable with `chmod +x wazuh-install-script.sh`.
3. Run the script with `./wazuh-install-script.sh`, and follow the prompts to configure the installation.
4. Access the Wazuh dashboard via a web browser for security monitoring.

**Additional Notes:**

- For more detailed information and troubleshooting, please refer to the official Wazuh documentation: https://documentation.wazuh.com/.
- This script is intended for educational purposes and may be customized to fit specific requirements and environments.

**License:**

This script is available under the MIT License.

Please feel free to use and adapt this script for your Wazuh installation needs. We welcome feedback and contributions to enhance its functionality and usability.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[071f6063e6...](https://github.com/tgstation/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Wednesday 2023-10-25 12:39:56 by carlarctg

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[af7c0cfe2a...](https://github.com/TaleStation/TaleStation/commit/af7c0cfe2a0af51d11edbb780ce48bd5c87fafe4)
#### Wednesday 2023-10-25 12:47:00 by TaleStationBot

[MIRROR] [MDB IGNORE] Actually supports alpha passed into emissive stuff (#8271)

Original PR: https://github.com/tgstation/tgstation/pull/79117
-----

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

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [ThetaLad/tgstation](https://github.com/ThetaLad/tgstation)@[4b73b37d60...](https://github.com/ThetaLad/tgstation/commit/4b73b37d60dbff8746ffb3e1eb0f6ff51895fffc)
#### Wednesday 2023-10-25 13:09:26 by jimmyl

Heretic Knock Path (#78108)

## About The Pull Request

other changes: GODMODEd mobs cannot receive embeds or bleed, admins can
now use the traitor panel to give heretics a focus

adds a new heretic path, the path of knock
its a path about opening shit and having access
wound opening included, and stealing
this is its award icon

![ascended](https://github.com/tgstation/tgstation/assets/70376633/01473bf2-5c44-4574-850c-83fb5db204fd)
its knowledge is as follows:

### A Locksmith’s Secret
starting knowledge, unlocks the key blade which also works as a crowbar


https://github.com/tgstation/tgstation/assets/70376633/3690232d-5687-4b0c-a9cc-b6374e7f1850

### Grasp of Knock
it literally just opens stuff (also makes a knocking sound)
unbolts bolted airlocks and opens them, opens locked closets, opens
mechas, logs you into consoles
(comms consoles are with barebones head-level access, no buying shuttle,
but hey you can shitpost over comms)
Sidepaths: Ashen Eyes, Codex Cicatrix


https://github.com/tgstation/tgstation/assets/70376633/8b890d69-ee03-4d12-99dd-dde7b4483cd4

### Key Keepers Burden
transmute a rod,wallet, and some id card to create an eldritch id card
(very original naming), the ID card used is not preserved
this ID card functions essentially as a superior agent card, using other
IDs on it makes it be consumed by the eldritch ID and have its accesses
and forms added into it, you can use it inhand to turn it into any of
the cards that were consumed
in addition you can hit two airlocks with it to link them together to
create portals under the doors, which has a green glow
going through the portal as a Heretic gets you to the other destination
going through as a nonheretic lands you in a random onstation airlock,
SM chamber included if youre unlucky
1 id card can only have 1 set of portals, making another destroys the
former set, one of the airlocks being destroyed also destroys them


https://github.com/tgstation/tgstation/assets/70376633/e96a518e-b35d-44aa-9a7c-8f2103feab6f

### Rite Of Passage
transmute a white crayon, a multitool, and a plank to create consecrated
lintel
heretics can use this cool looking book to create a 8 second shield that
knocks back any nonheretic that tries to pass
also its ranged


https://github.com/tgstation/tgstation/assets/70376633/036e0875-c422-433e-87b3-71328cb2bf8a

### Mark Of Knock
the mansus grasp will now mark its victim for like 10 seconds
marked victims are denied access by all objects, public airlocks
included


https://github.com/tgstation/tgstation/assets/70376633/6187ef36-30f4-4a92-af21-e5b288afb869

### Burglars Finesse
steal a random item from the victims backpack (or other storage item if
they dont have a backpack) and puts it into your hand
the victim will probably hear you and also gets a chat message about
this



https://github.com/tgstation/tgstation/assets/70376633/2529fa78-616d-4a46-ae18-3cb22efb1ab1

### Ritual of knowledge
this is nothing new i put this here to keep it in order

### Apetra Vulnera (sidepath with flesh)
the victim receives bleed wounds on every single bodypart that has more
than 15 brute
if they dont have a bodypart that has >= 15 brute they get a random
wound anyway so
side paths are: blood siphon and void cloak



https://github.com/tgstation/tgstation/assets/70376633/3c2cd21e-edbc-4956-8c2d-cd9a42b87f33

### Wave of Desperation (sidepath with flesh)
cannot be casted uncuffed with no bola, can be casted cuffed with no
bola, with a bola and no cuffs
adjacent mobs are knocked down, mobs are repulsed away, your cuffs and
bola are destroyed, and you gain a status effect that:
after 12 seconds makes you unconscious for 20 seconds
5 min cooldown


https://github.com/tgstation/tgstation/assets/70376633/da480921-d5dd-4b46-b2e8-0cf543640bf9

### Opening Blade
your blade has a 35% chance to cause a weeping avulsion on hit


https://github.com/tgstation/tgstation/assets/70376633/b6fd2837-6b0a-4a5a-bc7b-b9c3f7f715d1

### Caretakers Last Refuge
you can only cast this when not near sentient living beings
while in refuge you are invincible and near transparent, cannot use your
hands or spells
also immune to damage slowdown, being hit with a null rod cancels this
also if you lose your focus you get out of refuge


https://github.com/tgstation/tgstation/assets/70376633/f053cfd8-2a16-4195-8004-17df077983ca



https://github.com/tgstation/tgstation/assets/70376633/72330486-5273-4123-a108-b437b56120c4

### Many secrets behind the Spider Door (Ascension)
ritual needs 3 bodies without organs in their chest
when successfully performed you ascend and;
open a tear in reality (not the BoH one) which;
Polls all ghosts with sentient mob enabled to spawn and siege the
station, ghosts can interact with the portal to spawn as a random
eldritch mob
spawned mobs are loyal to whoever ascended and on examine can identify
their master
also fills the entire room with purple light

also the heretics opening blade is upgraded to a 65% chance, and they
gain Ascended Shapeshift which allows them to shapeshift into eldritch
mobs, and its not 1 choice only



https://github.com/tgstation/tgstation/assets/70376633/8d06286e-789d-442f-b33c-878d26deab07


## Why It's Good For The Game

its cool i think and an option for those wanting to steal and be sneaky
and stuff

## Changelog
:cl:
add: heretic knock path and its respective items and award
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [cyphar/runc](https://github.com/cyphar/runc)@[9c9a1f126c...](https://github.com/cyphar/runc/commit/9c9a1f126cef7b61a727df41a3d51db6f96ec8a5)
#### Wednesday 2023-10-25 14:15:15 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) but
operating on the actual inodes associated with the tid requires this
locking.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[1e9d7dbb64...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/1e9d7dbb642a23455b9905229d24fd90df2f8502)
#### Wednesday 2023-10-25 14:29:17 by Ruchit

sm7125-common: Kill blur

Holy shit snapdragon 720g is awful

---
## [kevinsung/documentation](https://github.com/kevinsung/documentation)@[6a7124e86c...](https://github.com/kevinsung/documentation/commit/6a7124e86cc8621826a4d6397110db903c7b2635)
#### Wednesday 2023-10-25 14:37:19 by Eric Arellano

Allow generating API docs for specific projects (#196)

One of the ideas from https://github.com/Qiskit/documentation/issues/63.
This is useful to me right now because I want to only redo
qiskit-ibm-provider.

`yargs` is a popular command line library in JavaScript. I've used it in
a personal project and had a great experience with it.

There will be future config we need to add, like probably having users
tell us what CI URL to look at when generating the docs, whereas right
now we pull from the live websites (see #63). I think it's likely that
config will be best set via a config file, rather than command line
arguments. But, even if we have that config file in the future, I still
think we'd want `--packages` to be a CLI arg since that is a quick thing
that you want to be flexible with setting, vs updating a file. If we
switch 100% to a file, that's fine; we can always remove `yargs`.

---
## [T-J-Teru/binutils-gdb](https://github.com/T-J-Teru/binutils-gdb)@[1b28c0f488...](https://github.com/T-J-Teru/binutils-gdb/commit/1b28c0f488bb84c8cc9f680afa9680dc0b0e2b3d)
#### Wednesday 2023-10-25 14:41:17 by Andrew Burgess

gdb: fix auxv cache clearing from new_objfile observer

It was pointed out on the mailing list that a recently added
test (gdb.python/py-progspace-events.exp) was failing when run with
the native-extended-gdbserver board.  This test was added with this
commit:

  commit 59912fb2d22f8a4bb0862487f12a5cc65b6a013f
  Date:   Tue Sep 19 11:45:36 2023 +0100

      gdb: add Python events for program space addition and removal

It turns out though that the test is failing due to a existing bug
in GDB, the new test just exposes the problem.  Additionally, the
failure really doesn't even rely on the new functionality added in the
above commit.  I reduced the test to a simple set of steps that
reproduced the failure and tested against GDB 13, and the test passes;
so the bug was introduced since then.  In fact, the bug was introduced
with this commit:

  commit a2827364e2bf19910fa5a54364a594a5ba3033b8
  Date:   Fri Sep 8 15:48:16 2023 +0100

      gdb: remove final user of the executable_changed observer

This commit changed how the per-inferior auxv data cache is managed,
specifically, when the cache is cleared, and it is this that leads to
the failure.

This bug is interesting because it exposes a number of issues with
GDB, I'll explain all of the problems I see, though ultimately, I only
propose fixing one problem in this commit, which is enough to resolve
the crash we are currently seeing.

The crash that we are seeing manifests like this:

  ...
  [Inferior 2 (process 3970384) exited normally]
  +inferior 1
  [Switching to inferior 1 [process 3970383] (/tmp/build/gdb/testsuite/outputs/gdb.python/py-progspace-events/py-progspace-events)]
  [Switching to thread 1.1 (Thread 3970383.3970383)]
  #0  breakpt () at /tmp/build/gdb/testsuite/../../../src/gdb/testsuite/gdb.python/py-progspace-events.c:28
  28	{ /* Nothing.  */ }
  (gdb) step
  +step
  terminate called after throwing an instance of 'gdb_exception_error'

  Fatal signal: Aborted
  ... etc ...

What's happening is that GDB attempts to refill the auxv cache as a
result of the gdbarch_has_shared_address_space call in
program_space::~program_space, the backtrace looks like this:

  #0  0x00007fb4f419a9a5 in raise () from /lib64/libpthread.so.0
  #1  0x00000000008b635d in handle_fatal_signal (sig=6) at ../../src/gdb/event-top.c:912
  #2  <signal handler called>
  #3  0x00007fb4f38e3625 in raise () from /lib64/libc.so.6
  #4  0x00007fb4f38cc8d9 in abort () from /lib64/libc.so.6
  #5  0x00007fb4f3c70756 in __gnu_cxx::__verbose_terminate_handler() [clone .cold] () from /lib64/libstdc++.so.6
  #6  0x00007fb4f3c7c6dc in __cxxabiv1::__terminate(void (*)()) () from /lib64/libstdc++.so.6
  #7  0x00007fb4f3c7b6e9 in __cxa_call_terminate () from /lib64/libstdc++.so.6
  #8  0x00007fb4f3c7c094 in __gxx_personality_v0 () from /lib64/libstdc++.so.6
  #9  0x00007fb4f3a80c63 in _Unwind_RaiseException_Phase2 () from /lib64/libgcc_s.so.1
  #10 0x00007fb4f3a8154e in _Unwind_Resume () from /lib64/libgcc_s.so.1
  #11 0x0000000000e8832d in target_read_alloc_1<unsigned char> (ops=0x408a3a0, object=TARGET_OBJECT_AUXV, annex=0x0) at ../../src/gdb/target.c:2266
  #12 0x0000000000e73dea in target_read_alloc (ops=0x408a3a0, object=TARGET_OBJECT_AUXV, annex=0x0) at ../../src/gdb/target.c:2315
  #13 0x000000000058248c in target_read_auxv_raw (ops=0x408a3a0) at ../../src/gdb/auxv.c:379
  #14 0x000000000058243d in target_read_auxv () at ../../src/gdb/auxv.c:368
  #15 0x000000000058255c in target_auxv_search (match=0x0, valp=0x7ffdee17c598) at ../../src/gdb/auxv.c:415
  #16 0x0000000000a464bb in linux_is_uclinux () at ../../src/gdb/linux-tdep.c:433
  #17 0x0000000000a464f6 in linux_has_shared_address_space (gdbarch=0x409a2d0) at ../../src/gdb/linux-tdep.c:440
  #18 0x0000000000510eae in gdbarch_has_shared_address_space (gdbarch=0x409a2d0) at ../../src/gdb/gdbarch.c:4889
  #19 0x0000000000bc7558 in program_space::~program_space (this=0x4544aa0, __in_chrg=<optimized out>) at ../../src/gdb/progspace.c:124
  #20 0x00000000009b245d in delete_inferior (inf=0x47b3de0) at ../../src/gdb/inferior.c:290
  #21 0x00000000009b2c10 in prune_inferiors () at ../../src/gdb/inferior.c:480
  #22 0x00000000009c5e3e in fetch_inferior_event () at ../../src/gdb/infrun.c:4558
  #23 0x000000000099b4dc in inferior_event_handler (event_type=INF_REG_EVENT) at ../../src/gdb/inf-loop.c:42
  #24 0x0000000000cbc64f in remote_async_serial_handler (scb=0x4090a30, context=0x408a6b0) at ../../src/gdb/remote.c:14859
  #25 0x0000000000d83d3a in run_async_handler_and_reschedule (scb=0x4090a30) at ../../src/gdb/ser-base.c:138
  #26 0x0000000000d83e1f in fd_event (error=0, context=0x4090a30) at ../../src/gdb/ser-base.c:189

So this is problem #1, if we throw an exception while deleting a
program_space then this is not caught, and is going to crash GDB.

Problem #2 becomes evident when we ask why GDB is throwing an error in
this case; the error is thrown because the remote target, operating in
non-async mode, can't read the auxv data while an inferior is running
and GDB is waiting for a stop reply.  The problem here then, is why
does GDB get into a position where it tries to interact with the
remote target in this way, at this time?  The problem is caused by the
prune_inferiors call which can be seen in the above backtrace.

In prune_inferiors we check if the inferior is deletable, and if it
is, we delete it.  The problem is, I think, we should also check if
the target is currently in a state that would allow us to delete the
inferior.  We don't currently have such a check available, we'd need
to add one, but for the remote target, this would return false if the
remote is in async mode and the remote is currently waiting for a stop
reply.  With this change in place GDB would defer deleting the
inferior until the remote target has stopped, at which point GDB would
be able to refill the auxv cache successfully.

And then, problem #3 becomes evident when we ask why GDB is needing to
refill the auxv cache now when it didn't need to for GDB 13.  This is
where the second commit mentioned above (a2827364e2bf) comes in.
Prior to this commit, the auxv cache was cleared by the
executable_changed observer, while after that commit the auxv cache
was cleared by the new_objfile observer -- but only when the
new_objfile observer is used in the special mode that actually means
that all objfiles have been unloaded (I know, the overloading of the
new_objfile observer is horrible, and unnecessary, but it's not really
important for this bug).

The difference arises because the new_objfile observer is triggered
from clear_symtab_users, which in turn is called from
program_space::~program_space.  The new_objfile observer for auxv does
this:

  static void
  auxv_new_objfile_observer (struct objfile *objfile)
  {
    if (objfile == nullptr)
      invalidate_auxv_cache_inf (current_inferior ());
  }

That is, when all the objfiles are unloaded, we clear the auxv cache
for the current inferior.

The problem is, then when we look at the prune_inferiors ->
delete_inferior -> ~program_space path, we see that the current
inferior is not going to be an inferior that exists within the
program_space being deleted; delete_inferior removes the deleted
inferior from the global inferior list, and then only deletes the
program_space if program_space::empty() returns true, which is only
the case if the current inferior isn't within the program_space to
delete, and no other inferior exists within that program_space
either.

What this means is that when the new_objfile observer is called we
can't rely on the current inferior having any relationship with the
program space in which the objfiles were removed.  This was an error
in the commit a2827364e2bf, the only thing we can rely on is the
current program space.  As a result of this mistake, after commit
a2827364e2bf, GDB was sometimes clearing the auxv cache for a random
inferior.  In the native target case this was harmless as we can
always refill the cache when needed, but in the remote target case, if
we need to refill the cache when the remote target is executing, then
we get the crash we observed.

And additionally, if we think about this a little more, we see that
commit a2827364e2bf made another mistake.  When all the objfiles are
removed, they are removed from a program_space, a program_space might
contain multiple inferiors, so surely, we should clear the auxv cache
for all of the matching inferiors?

Given these two insights, that the current_inferior is not relevant,
only the current_program_space, and that we should be clearing the
cache for all inferiors in the current_program_space, we can update
auxv_new_objfile_observer to:

  if (objfile == nullptr)
    {
      for (inferior *inf : all_inferiors ())
	{
	  if (inf->pspace == current_program_space)
	    invalidate_auxv_cache_inf (inf);
	}
    }

With this change we now correctly clear the auxv cache for the correct
inferiors, and GDB no longer needs to refill the cache at an
inconvenient time, this avoids the crash we were seeing.

And finally, we reach problem #4.  Inspired by the observation that
using the current_inferior from within the ~program_space function was
not correct, I added some debug to see if current_inferior() was
called anywhere else (below ~program_space), and the answer is yes,
it's called a often.  Mostly the culprit is GDB doing:

  current_inferior ()->top_target ()-> ....

But I think all of these calls are most likely doing the wrong thing,
and only work because the top target in all these cases is shared
between all inferiors, e.g. it's the native target, or the remote
target for all inferiors.  But if we had a truly multi-connection
setup, then we might start to see odd behaviour.

Problem #1 I'm just ignoring for now, I guess at some point we might
run into this again, and then we'd need to solve this.  But in this
case I wasn't sure what a "good" solution would look like.  We need
the auxv data in order to implement the linux_is_uclinux() function.
If we can't get the auxv data then what should we do, assume yes, or
assume no?  The right answer would probably be to propagate the error
back up the stack, but then we reach ~program_space, and throwing
exceptions from a destructor is problematic, so we'd need to catch and
deal at this point.  The linux_is_uclinux() call is made from within
gdbarch_has_shared_address_space(), which is used like:

  if (!gdbarch_has_shared_address_space (target_gdbarch ()))
    delete this->aspace;

So, we would have to choose; delete the address space or not.  If we
delete it on error, then we might delete an address space that is
shared within another program space.  If we don't delete the address
space, then we might leak it.  Neither choice is great.

A better solution might be to have the address spaces be reference
counted, then we could remove the gdbarch_has_shared_address_space
call completely, and just rely on the reference count to auto-delete
the address space when appropriate.

The solution for problem #2 I already hinted at above, we should have
a new target_can_delete_inferiors() call, which should be called from
prune_inferiors, this would prevent GDB from trying to delete
inferiors when a (remote) target is in a state where we know it can't
delete the inferior.  Deleting an inferior often (always?) requires
sending packets to the remote, and if the remote is waiting for a stop
reply then this will never work, so the pruning should be deferred in
this case.

The solution for problem #3 is included in this commit.

And, for problem #4, I'm not sure what the right solution is.  Maybe
delete_inferior should ensure the inferior to be deleted is in place
when ~program_space is called?  But that seems a little weird, as the
current inferior would, in theory, still be using the current
program_space...

Anyway, after this commit, the gdb.python/py-progspace-events.exp test
now passes when run with the native-extended-remote board.

Bug: https://sourceware.org/bugzilla/show_bug.cgi?id=30935
Approved-By: Simon Marchi <simon.marchi@efficios.com>
Change-Id: I41f0e6e2d7ecc1e5e55ec170f37acd4052f46eaf

---
## [0perator-github/mameui](https://github.com/0perator-github/mameui)@[b17bd90268...](https://github.com/0perator-github/mameui/commit/b17bd90268aa6b970b96efcfe4f52040434b000f)
#### Wednesday 2023-10-25 14:59:01 by wilbertpol

msx2_cart.xml: Added 31 items, 29 working. (#11642)

* msx2_cart.xml: Added 31 items, 29 working.

New working software list items
-------------------------------
Aleste (Woomb) [file-hunter]
Arkanoid 2 (Korea) [file-hunter]
Ashguine - Fukushuu no Honoo (Japan, alt 2) [file-hunter]
Daisenryaku MSX2 (Japan, alt) [file-hunter]
Gekitotsu Pennant Race 2 (Japan, sample) [file-hunter]
Hydlide 3 - The Space Memories (Woomb) [file-hunter]
Alien 8 Remake [file-hunter]
Los Amores de Brunilda (v1.01) [file-hunter]
Los Amores de Brunilda (v1.0) [file-hunter]
Barbarian the Duel [MSXdev]
Bomb Jack [file-hunter]
Bomb Jack (alt) [file-hunter]
Booming Boy (demo) [MSX Area]
Bubble Dream [MRC Tenliner Challenge]
DIM X (demo) [file-hunter]
Equivocal (v1.5) [Passion MSX2 Contest]
Equivocal (v1.0) [Passion MSX2 Contest]
Gold Fan [N.I]
Highway Fighter (demo) [file-hunter]
Inferno [msxdev Compo]
Jailbreak (v1.02) [Passion MSX2 Contest]
Jailbreak (alt) [Passion MSX2 Contest]
Jailbreak (alt 2) [Passion MSX2 Contest]
Knight Lore Remake [Retroworks]
Lilly's Saga - The Stones of Evergreen (v1.2) [MSXdev]
Lilly's Saga - The Stones of Evergreen (v1.1) [MSXdev]
Lilly's Saga - The Stones of Evergreen (v1.0) [MSXdev]
La Sorpresa (Spanish) [Oniric Factor]
A Surpresa (Portuguese) [Oniric Factor]

New NOT_WORKING software list additions
------------------------------------------
Ehagaki-yō wāpuro (Japan) [file-hunter]
Life on Earth (demo) [file-hunter]

* Fix capitalisations of Wāpuro and AshGuine

---
## [smclacke/minishell](https://github.com/smclacke/minishell)@[edfb5ab143...](https://github.com/smclacke/minishell/commit/edfb5ab143dddfa829eab9f65b2c82fd560affba)
#### Wednesday 2023-10-25 15:19:09 by smclacke

this MONSTROUSITYYYYYYY works. I HOPE TO FUCK THIS WAS WORTH IT, AND I FIND A WAY TO MAKE IT BETTER, WITHOUT ALL THIS HARD CODING, AND MAYBE WITHOUT THE FUNCTION THAT IS 72 LINES.... AND NOT ANOTHER GODDAMN STRCMP OMG OMG OMG, IF THIS IS NOT REALLY REALLY USEFUL IM GUNNA ... IM GUNNA... IM GUNNA ADD ANOTHER ANOTHER STRCMP :D yyayyyyyyyyy, whyyyy

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[30ce9e53fd...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/30ce9e53fd4538843b0b5d40d8ba04627f61edc7)
#### Wednesday 2023-10-25 16:19:31 by Peter Zijlstra

UPSTREAM: sched/core: Fix ttwu() race

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [Lynx22330/coyote-bayou](https://github.com/Lynx22330/coyote-bayou)@[eb0f0559aa...](https://github.com/Lynx22330/coyote-bayou/commit/eb0f0559aaea59ecb7d9dcaadafbf1755d89c79a)
#### Wednesday 2023-10-25 16:41:15 by Lynx

QuirkFix =Typo fix, Grammar fix, and punctuation=

Changes a lot of different quirk details, added a lot of medical record text, and also added missing "Lose" and "Gain" text for quirks in case an admin wants to give it to someone so that the player can confirm, or an eventual item granting it.

--Changes a lot of grammar, too, for example, like 1071->(1094), its probably not even needed to change it, but it felt a lot easier to read to understand that your max cap went to 25, instead of ONLY 5, to make sure that its clear that it isn't just a bump up to 25 for starter healing, no no, its a permanent 25.

--Some comments, like the radiation one at 1378-79 -> (1404-06), have been made to be a bit more ... vague. Because, well, you just somehow decided out of the god damn blue you're RAD resistant... So you've just decided radiation is basically an afterthought. Does NOT mean you're *IMMUNE* to it. It's a hopeful change that'll make players wonder how resilient they are to radiation, since it depends from person to person. Also. It's their god damn decision apparently if RADS HURT EM OR NOT >:D

--A LOT of the medical record text is to, hopefully, encourage medical personnel to read the medical logs if those even exist on CB. I don't actually know. But, this would also encourage characters and the players to toy around with their medical text if they don't like how cluttered it is from how the medical staff wrote it. It's not intended to be bad; but, every Quirk is ... well, a quirk. This is supposed to be a pretty high end roleplay server (not crazy high since pve duh) but it's intended to have people actually do a lot of smaller things as far as I can tell in-between combat.
(But I may be wrong. Please tell me if I am on discord. Username =   " l_ynx "

I don't think I touched quirk values, as I reverted my change from the empath one back down to 0. I still think its more of a useful quirk; but thats just me.

--A lot of punctuation has been fixed. Some quirks didn't have periods, some did have periods, but too many, and some had a marker at the end, WITH punctuation!.  ;)

---
## [rderekp/The-Grand-Combo](https://github.com/rderekp/The-Grand-Combo)@[5d1cf9752b...](https://github.com/rderekp/The-Grand-Combo/commit/5d1cf9752b0f61d8bbf1463b9f48f70c50deedca)
#### Wednesday 2023-10-25 16:43:31 by ColdSlav

Removed Racist Term

Fuck you Fraggy you should've never joined the team

---
## [spcy-ivy/CPL](https://github.com/spcy-ivy/CPL)@[a92507b061...](https://github.com/spcy-ivy/CPL/commit/a92507b061aa4818386233b26417d1b89bcd060c)
#### Wednesday 2023-10-25 17:10:18 by selectgender

Removed pretentiousness

good god I sounded corny holy fuck

---
## [du-top/sojourn-station](https://github.com/du-top/sojourn-station)@[1de2165959...](https://github.com/du-top/sojourn-station/commit/1de21659596e9f1f472e090251901076f0a5e8d8)
#### Wednesday 2023-10-25 17:10:35 by CactusMouth

Addon - Excel Fortress (Fixed maybe) (#4792)

* Addon - Excel Fortress (Fixed maybe)

* AAAAAAAAAA

* Update _Deep_Forest.dmm

* Slight additions

* Update _Deep_Forest.dmm

* Update _Deep_Forest.dmm

* Finishing Touches

* Adds a proper area code for the dungeon, alongside a brief narration.

* Final Work

Final work for the release (more to come after release)

* Update - No more Bear Heaven

] Reduced number of bears
] Added more guns, including non-excel versions
] Some mines are now activated, and even more have been added. Good luck.
] Two more OKBs added because fuck you
] Power is now within the fort

---------

Co-authored-by: CDB <87905328+cdb-is-not-good@users.noreply.github.com>

---
## [AquillaF/Skyrat-tg](https://github.com/AquillaF/Skyrat-tg)@[d5d78fec30...](https://github.com/AquillaF/Skyrat-tg/commit/d5d78fec30aef1480c47a581eafc6a1b9edc8b13)
#### Wednesday 2023-10-25 17:24:43 by SkyratBot

[MIRROR] Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN [MDB IGNORE] (#24149)

* Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN (#78674)

## About The Pull Request

The Regal Condor come with a magazine and ammo already inside.

The recipe for the magazine now no longer needs TC, but does need donk
pockets (sponsored murder gear, you see) and a hell of a lot more
materials per magazine (you're looking at like 40 sheets of various
materials all up). It also needs you to make the Condor first. But it
comes preloaded with ammo.

The Condor is 1 whole TC more expensive. Also needs some metal. The old
recipe is there in spirit.

The Regal Condor and the magazines come with 10mm Reaper bullets.
They're high damage. They're high AP. They are also hitscan.

## Why It's Good For The Game

Apparently people don't like the Condor. Too much effort for not enough
reward. After all, revolvers exist. 'It must be a joke' they say! 'It's
joke content! I went to all that effort to make it for nothing! That
slut Anne tricked us!'

**Wrong, bitch.**

If you want the Condor to make you shit yourself the moment someone with
it appears on the screen, then fine!

### **You get what you fucking deserve.**

## Changelog
:cl:
balance: Despite earlier reports suggesting that the famous lethality of
the Regal Condor was largely a myth, there has been rumors that the gun
has once again started to display its true killing potential on any
station that it 'manifests'.
/:cl:

* Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[c9bc367f17...](https://github.com/k21971/EvilHack/commit/c9bc367f17339b98f7d626bcab3a22d04a14924f)
#### Wednesday 2023-10-25 17:55:50 by k21971

Wand of Orcus changes.

Previously, the Wand of Orcus was deemed too powerful for any player to
be able to wield. This commit does away with that restriction. Players
(and non-demonic monsters as well) can now wield the Wand of Orcus, but
being in control of such deadly magic comes with a price. The changes:

* when wielding the Wand, health regeneration is completely suppressed
(same as being in the Valley of the Dead)
* wielding the Wand, if not already cursed, will become cursed and weld
itself to the players' hand (if not an Infidel)
* if the Wand is welded and is uncursed/blessed, there is a random
chance it will re-curse itself
* dropping the Wand from inventory, if not already cursed, will curse it
(same behavior as dropping a loadstone)
* maximum hit point drain vs monsters is now more inline with how it
affects the player
* the Wand can be invoked to tame any nearby undead

Not pushing this to the servers just yet, I'd like some review on this,
see if anything else needs to be added or adjusted. I'm thinking the
Wand should not be able to be dual-wielded with another artifact. Max
hit point damage vs monster could probably be tweaked too.

Also in this commit - had to remove the status_hilite entries from the
sysconf tweak, as those options apparently override player configs.

---
## [TheDailySimile/PedalPonder](https://github.com/TheDailySimile/PedalPonder)@[bd5c166e73...](https://github.com/TheDailySimile/PedalPonder/commit/bd5c166e73c5dca4c55d5f9e6ab0c17fef0d896f)
#### Wednesday 2023-10-25 18:07:36 by The Daily Simile

Create Ash : Next Term Phantom@Instrument Oriented Dissolution.html

Ash@straight : "well it was a privilege indeed to meet you personally Ms Santanore to know about your views and ways to dealing with..things.."
Sakura@laughing : "looking at the change of this expression and given what your name hides beneath i guess it's you mean my views and ways of handling..duality#..Lastly Phantom,#,..Ash un..long,#,.."
Ash@straight : "myriads indeed are the adjustments to self or of self to ego but any chance that you'd forfeit tomorrow's match..given how my opponents as ever complain how their bunch don't..incline to their aim only thoughts#.."
Sakura@smile : "well that's the point Ash i really believe if i can't surmount you i can atleast learn more..about myself as per your..methodology in obsessive duairy#.. Conclusion on the Meanings of Lie,#,..Ash+Misty un..long,#,.."
Ash@straight : "well indeed Ms Santanore have a nice rest tonight..(outside)..no Ms Sakura doesn't agree to my proposal..
Brock@frown : "didn't bow down to your ego all that's#..Ash..that feeling,#,..Brock un..long,#,.."
Ash@shrug : "well you know i tried to come to your rescue when i said me can't be as too.."
Violet@angry,was present : "shut up you self decoding yet self knowing b.. that crook is unable to come into terms with i not me unlike your poise seeking yet choice devoted b..#..Ash+Misty..Me-Ly Volt,#,..Violet un..long,#,..
Misty@angry : "you absolute seeing but construction using b.. how dare you challenge the inspection of notion that your point weaving yet feeling using b.. mistakes as corroboration to wonder smoothening#..Brock+Misty..Conclusion Obsession,#,..Misty un..long,#,.."
Brock@scowl : "enough ok you didn't understand how this b.. just fooled you into..forgetting him.."
Misty@scowl : "it not him as formly a notion is as apparent as illusion#..Sakura,Brock+Violet,Gary+Lily,Tracey+Daisy,Ingemar+Blythe,Dentarou+Mahina..End Obsession,#,..Misty un..long,#,.."
Sakura@giggle : "ei Marc what are the repercussions of what you were told Commitment : The Battle of Propositions,#,..Dissolution of Actuality,#,..Sakura un..long,#,.."
Marc@scowl : "if i were you i would've been rather concerned about my self than my inclinations#..Marc..Yeah It's a matter of Skills Mr Litman i very sorry that you came,second best..to the use of..,feel..surely you know my ideological guidelines#..Ash+Misty..yeah that is a win,..shuu..Result That Feeling,#,..Brock un..long,#,.."
Ash@shrug : "well as you insist i would have to choose a pokemon..to the crowd's..likin'....of a Grim prospective.."
Grimmsnarl@unhappy : "why do you irritate me hombre you can't even recognise what is to be battled and what is battling#.."
Ash@shrug : "well i though may be as you were inflecting your clingings using likin' may be you forgot to ask..seein' it.."
Grimmsnarl@giggle : "attacked!..
halt..oh Ketchum self shouts/racin' against whoose doubts?/then you Ketchum in dual bouts/try to defend your self by extendin' about.."
Sakura@giggle : "through nerves of sustainin'/races alone constrainin'/upon question on meain'/lied answer as feelin'.."
Whole female crowd including Violet-Misty@giggle : "then to be or to see/lastly Phantom means i never me.."
Misty@giggle : "and because you're from the affordable shore you refuse to understand the psychoanalysis of the instrument of the elaborative shore..take that you feelin' crook nana#..Brock..Doubt-Clearance Obsession,#,..Misty un..long,#,.."
Brock@scowl : "i see thus that sickening Grimmsnarl was taken from the assortment of..form..cunning indeed Ketchum this game of pros on cons#..Daisy,Violet,Lily,Blythe,Mahina..Playboy Raptures,#,..Ash un..long,#,.."
Ash@shrug : "before the BATTLE begins Mr Santanore unlike Ms Santanore iou already know my inclinations..on self help ain't it.."
Marc@scowl : "Saku lost because of purity of vision thus with her bunch was over the moon understanding instrument oriented dissolutions but purity is a counter indeed to your..analogy obsession#..The Meaning of Lie,#,..Ash un..long,#,.."
Ash@shrug : "fair enough you refuse to submit to..desires fo liberation from obviousness..thus this..Entei.."
Referee@veryAngry : "ai ai you choose a pure fir i'll disqualify you ok.."
Marc@angry : "you lowlife don't create an intrigue of probability on knowledge ok this was only a counter to Defeat : Victory Lie#..Gary&Ingemar+Blythe..who are you,Ash Ketchum Pokemon Master,ego sinister we see,me..you see only compeers..me thus indeed as a counter isn't it so..shh..it was included..
Phantom : The Meaning of Lie..
any noise in thoughtful chantin' of soul?,#,..Ash un..long,#,.."
Entei@giggle : "ei vision eh blur aim boo charred i or thy/or who see as this or i..i..
shh..shh..shh..shh..shuu..uu..uu..blast/or cue cue cue cue cue see why never past.."
Marc@scowl : "i see this is the generalization of..next term..unless i admit defeat and stop my self from venturing into it's randomness i will be deemed a phantom cunning indeed Ash..as Ash means i read in those sickening comics popularized by you..Ash : Next Term..Phantom,#,..Ash : Next Term Phantom,#,..Ash un..long,#,.."

---
## [sunofang/Bubberstation](https://github.com/sunofang/Bubberstation)@[4012db7ce2...](https://github.com/sunofang/Bubberstation/commit/4012db7ce2315160882c5e375ca429fe1c8f20ef)
#### Wednesday 2023-10-25 18:25:18 by SkyratBot

[MIRROR] Adds Blood-drunk and demonic frost miner boss music. [MDB IGNORE] (#23543)

* Adds Blood-drunk and demonic frost miner boss music. (#78123)

Acts as a continuation of PR #77149 for boss music functionality and
implements a BDM and demonic frost miner boss music theme.

More music is good, but I do have some gripes with my own PR. This
particular track relies on instrumentation that when compressed just
doesn't sound as good, and the in-game version is noticeably less
enjoyable that the high quality version. I wish I could help the track
out more, but as is it's already at 811 kb which is barely in line with
file requirements, so i just can't justify bloating the audio file sizes
to make it sound better. You notice this kind of problem a lot with the
higher runtime music and background tracks. It just feels a bit more
clunky than hierophant, but what are you gonna do right?

* Adds Blood-drunk and demonic frost miner boss music.

---------

Co-authored-by: RICK IM RI <77305289+tommysalami3@users.noreply.github.com>

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[dabd196d97...](https://github.com/LumberKing/Tianxia/commit/dabd196d97e3c609f5c3138553aab4bfd3210fed)
#### Wednesday 2023-10-25 18:34:56 by Silversweeper

Misc

- Custom loc setup related to SRS, MOs; actual loc tags TODO.
- Improved some vanilla custom loc; for example, Norse faithful now know better than to refer to "Thor's hammer" as such.
- MNM.3227 can no longer result in the averting of someone else's eyes, and no longer makes assumptions about priestly gender.
- Princess Pingchang is now a special_marshal; she's also very dead, but it's the thought that counts!
- Added Akkadevi (sister of Jayasimha II); between start dates, but she's neat to have. She's a special_marshal.
- Added Umadevi (consort of Veera Ballala II), and set her as a special_marshal.
- Minor adjustments to Liang Hongyu.
- Rudramadevi of the Kakatiyas is now a special_marshal.
- Tribhuwannottunggadewi Jayawishnuwardhani, She Who Will Break All The Loc Strings, is now known as such when she assumes the throne.
- The slavic_pagan _desc doesn't consider it "heathenry", seeing as that's frequently got negative connotations.
- Set up RW holy order creation and grandmaster gender... not that we support it.
- The Jomsvikings now spawn when assorted GHWs unlock around 1100 in RWs with random religions, as opposed to never spawning.
- Minahasans no longer care about councillor gender.
- Added and appended _FEATURES to various religions that have access to noteworthy mechanics not listed, such as government eligibility. Reformed pagans only get guaranteed features listed, so e.g. Eastern syncretism is not listed for Reformed Bön due to Dogmatic rendering them ineligible. To be iterated on after 14.0.0.
- God names starting with "the" are now properly decapitalised.
- Minor tweaks to god names.

---
## [ably/specification](https://github.com/ably/specification)@[028c94f13b...](https://github.com/ably/specification/commit/028c94f13b0eb4a041b321d8d314167c797f42ce)
#### Wednesday 2023-10-25 19:24:53 by Lawrence Forooghian

Distinguish the different meanings of a "message"

The context for this suggested change is ably-js#1398. There, I pointed out
that the specification’s current signatures for `publish` (specifically, the
overloads that accept a `Message` or an array thereof) do not seem to match how
we’re expecting these methods to be used in real life. This is because
`Message`’s `id` and `timestamp` properties are specified as non-optional,
meaning that a user calling `publish` would need to populate these properties.
In reality, we do not expect a user to populate these properties — they are
usually generated by the Ably service.

The easiest way to solve this would be to be to make these properties optional.
However, doing so would unnecessarily remove some useful type information for
_recipients_ of messages — the type system would no longer communicate that
these properties are guaranteed to be populated in a message emitted by the
library.

In this PR, I’m proposing that we distinguish between three separate
concepts of a "message", which I think are perhaps currently being incorrectly
conflated:

1. The data type that a user of the library passes to the `publish` methods

2. The data type that the library emits from methods that expose messages
   published on a channel

3. The data type that describes a serialized message that is transmitted over
   the wire

I’ve named the first one OutgoingMessage, the second one IncomingMessage, and I
believe that the third belongs in the documentation for the Ably protocol, not
the library specification.

OutgoingMessage and IncomingMessage differ from the existing `Message` type in
the following ways:

- OutgoingMessage’s `id` and `timestamp` properties are now optional
- OutgoingMessage does not have `fromEncoded*` methods

- IncomingMessage does not have constructors

I have not yet introduced spec points for these two new types — I will do so if
there is a consensus to move forwards with this approach. For now, see the
changes to the IDL.

Other thoughts:

- I think that, similarly to the Message wire type, the ProtocolMessage type
  should also only be described by the protocol documentation, and not the
  feature spec.

- If we do choose to start leaning more heavily on the protocol documentation,
  then we’ll need to bring it up to date — it looks like it hasn’t been touched
  in quite some time and still mentions `connectionSerial`, for example.

- I’ve kept the exact same list of properties in IncomingMessage and
  OutgoingMessage, since my reading of RSL1j is that a user publishing a
  message should be able to populate any of the properties of the message that
  eventually gets sent over the wire. But if that’s not the case, then we may be
  able to remove some properties from `OutgoingMessage`.

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[9b6af0cbfd...](https://github.com/RalphHightower/RalphHightower/commit/9b6af0cbfd41ede56379656b2cbd3f7d20baef51)
#### Wednesday 2023-10-25 19:29:41 by Ralph Hightower

[docs](doc): CalvinAndHobbes(extended description) 

- Calvin & Hobbes 
   - | [Why Bill Watterson Named his Characters Calvin and Hobbes](https://www.cbr.com/calvin-hobbes-name-inspiration-trivia/ ) |
   - | [10 Lessons Calvin & Hobbes Taught Us About Love](https://www.cbr.com/calvin-and-hobbes-lessons-taught-about-love/#good-friends-love-and-support-each-other ) |
   - | [15 Best Calvin And Hobbes Snowman Comic Strips](https://www.cbr.com/best-calvin-hobbes-snowman-comics/ ) |
   - | [15 Times Calvin & Hobbes Broke Our Hearts](https://www.cbr.com/calvin-hobbes-sad-comics/ ) |
   - | [Greatest Calvin & Hobbes Strips Ever Published](https://www.cbr.com/greatest-calvin-and-hobbes-newspaper-strips/ ) |

---
## [GPeckman/tgstation](https://github.com/GPeckman/tgstation)@[9ff9e4b9a8...](https://github.com/GPeckman/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Wednesday 2023-10-25 19:32:23 by necromanceranne

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
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[0f810e3672...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/0f810e367297e10784692ac52b591c8d2b0f0bb2)
#### Wednesday 2023-10-25 19:44:06 by Coxswain

Adds distorted form

adds some basic features

new 1% sprite dropped

text update

Finished work mechanics

adds basic breaching

should fix linters a bit

It works!!!! Kinda...

adds crumbling armor and hammer of light (beta)

adds cool and important stuff

does a thing

adds apostle and tutorial abnorms

adds the stuff

might fix linters

adds a console proc

adds crumbling armor's proper attack and red queen

does some things

should fix linters

adds a blubbering toad transformation

adds more attacks

brings the tier up

adds big boy attacks

updates some sfx, fixes bugs

adds jump attacks

why does linters care about indentation on comments?

adds suggested changes

should fix some stuff

adds info

adjusts damage numbers

updates an effects and fixes transformations

updates blacklist

lowers stack damage

lowers max qlip to 3

adds bloodbath

adds a new AOE attack

adds halberd apostle

blacklists DF from pink midnight

fixes weirdness

requested changes and sound design improvement

removes armortype

removes armortype for real

---
## [Moltijoe/Yogstation](https://github.com/Moltijoe/Yogstation)@[8370bd28c0...](https://github.com/Moltijoe/Yogstation/commit/8370bd28c0f6c6cb467732f6e7e2748655360912)
#### Wednesday 2023-10-25 19:57:15 by Bop

[PORT] [READY] Refactor sm delam into a different file + New Anomaly+ Anomaly Code improvements + New Resonance Cascade effects + Improved Blob Delam code (#20109)

New resonance cascade effects because old one is boring as shit, this should make the crew panic DEATH RATE: >60%
New hallucination anomaly which creates powerful hallucination pulses.
Each of the reactive armors now have unique negative effects when emp'ed.
Each of the reactive armors now have unique negative effects when emp'ed.
Moves supermatter delamination to its own datum.
Nerf rad anomly particle counts after death
Rad anomaly no longer spin and shoot particles on death, instead shoot at the same time with less particles and release one rad goat only for rad anomaly goat type, should improve performance
Nerfed particle counts of each tick to 5 particles and buff rad pulse to 10000
Nerfed particle counts when anomaly dies to 15 particles and buff rad pulse to 20000
replaces airraid.ogg with a new one from tg
new anomaly and core sprites
new radiation core sprite
fixes overlay of action button for reactive armor
fixes reactive armor sprite not update when active on body
add a fucking supermatter tesla (spawned by SM resonance cascade)
tesla_zap now has dust ability and ignore mob with godmode or spirit
tesla_zap can hit atmos machines, grille and simple animals (except for hostile one and slime)
Improved blob delam code and make the delam more deadly

---
## [Sh3ldar/rpemotes](https://github.com/Sh3ldar/rpemotes)@[3dd8561ba5...](https://github.com/Sh3ldar/rpemotes/commit/3dd8561ba5489b35f058a5ad1ef40407d7f58c59)
#### Wednesday 2023-10-25 20:50:34 by TayMcKenzieSA

Exclusive RPEmotes Emote Requested By TayMcKenzieNZ

added old2 which uses a zimmer frame. custom emote by darks animations, requested by TayMcKenzieNZ for RPEmotes exclusively, not for your shitty scripts. We will literally DMCA your shitty reuploaded bullshit if we find it in there.

---
## [veggiemike/openrvdas](https://github.com/veggiemike/openrvdas)@[8fa272b675...](https://github.com/veggiemike/openrvdas/commit/8fa272b67500f615c2bf4c813d1c39da1ef13b7a)
#### Wednesday 2023-10-25 20:57:11 by Michael D Labriola

UDPReader: increase READ_BUFFER_SIZE and remove `read_buffer_size` param, v1

The UDP header's `length` field sets a theoretical limit of 65,535 bytes
(8-byte header + 65,527 bytes of data) for a UDP datagram.  Technically,
IPV4 or IPv6 headers use up some of that size, so actual maximum data sent
per datagram is slightly less.

UDP receivers should always request the max, though, because if you request
less than what's on the wire, you get what you asked for and the rest gets
tossed on the floor.  There's no built-in error detection/correction in
UDP, so that would mess things up pretty good.

My testing in python shows that you can recv() w/ pretty much any
ridiculously silly large number (655350, aka 10x the max size) on both
Linux and Mac.  We'll have to put some logic into UDPWriter and TCPWriter,
though, because send() is where we run into real-life limits (as opposed
to "theoretical" ones).

Given all that, allowing users to configure the read size via the
`read_buffer_size` parameter is a bad idea: it just allows them to break
things.  So this commit also removes that

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[0788c987ac...](https://github.com/Buildstarted/linksfordevs/commit/0788c987aca57adca910c3a9df6cf6446f5b2370)
#### Wednesday 2023-10-25 21:09:10 by Ben Dornis

Updating: 10/25/2023 9:00:00 PM

 1. Added: Avoiding addictions
    (https://josem.co/avoiding-addictions/)
 2. Added: On Linking Bookmarks
    (https://joshleeb.com/posts/linking-bookmarks.html)
 3. Added: How Databases Store and Retrieve Data with B-Trees
    (https://www.lucavall.in/blog/how-databases-store-and-retrieve-data-with-b-trees)
 4. Added: Unity Killed Modern Proprietary Gaming For Me
    (https://jaylittle.com/post/view/2023/9/unity-killed-modern-proprietary-gaming-for-me)
 5. Added: My 2023 all-flash ZFS NAS (Network Storage) build
    (https://michael.stapelberg.ch/posts/2023-10-25-my-all-flash-zfs-network-storage-build/)
 6. Added: Automattic's Tumblr/ActivityPub integration reportedly shelved
    (https://notes.ghed.in/posts/2023/tumblr-activitypub-integration/)
 7. Added: iLeakage: Browser-based Timerless Speculative Execution Attacks on Apple Devices
    (https://ileakage.com/)
 8. Added: axo blog - System dependencies are hard (so we made them easier)
    (https://blog.axo.dev/2023/10/dependencies)
 9. Added: Are you talking or speaking?
    (https://rory.codes/talking-or-speaking/)
10. Added: Firstborn
    (https://www.sonyasupposedly.com/firstborn/)
11. Added: Crafting boring APIs: lessons learned from implementing fallback handlers in Pavex | Luca Palmieri
    (https://www.lpalmieri.com/posts/api-design-should-be-boring/)
12. Added: Triggering `entr`
    (https://huijzer.xyz/posts/entr-trigger/)
13. Added: It's Fucking Impossible to Stay Healthy
    (https://www.withentropy.com/blog/2023-10-24-its_impossible_to_stay_healthy/)
14. Added: It's 2023, here is why your web design sucks.
    (https://heather-buchel.com/blog/2023/10/why-your-web-design-sucks/)

Generation took: 00:08:55.6267687
 Maintenance update - cleaning up homepage and feed

---
## [carrotman2013/RU-CMSS13](https://github.com/carrotman2013/RU-CMSS13)@[439762cf8a...](https://github.com/carrotman2013/RU-CMSS13/commit/439762cf8aaaa5fa1418924c0db896a57dd30cf9)
#### Wednesday 2023-10-25 21:19:00 by kiVts

tgui research desktop fix (#4592)

# About the pull request
3 out of 4

Have you ever noticed that when you simulate something new, lets say you
called it "gamer juice" and instead, in computer lab it always has "for"
instead of the actual name that you created? this is because "Analysis
of X" Has two words before the name of the chemical while "Simulation
results for X" has 3

TGUI splits it the same way despite having different number of words,
thus, "Simulation results **for** X" - this is where For comes from.

I had two ways to do it, either remove third word, or try to fix it in
tgui, this however, still doesnt include the spaces you can put in the
name.

(tgui is weiiirdd, if I did something funny which I dont get, sorry)
# Explain why it's good for the game
Always annoying to look for correct chemical you did in like ~8 "for"


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: kiVts
fix: Research computer no longer shows "for" for every simulation
result.
/:cl:

---
## [zeroshade/arrow](https://github.com/zeroshade/arrow)@[3beb93af36...](https://github.com/zeroshade/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Wednesday 2023-10-25 21:26:27 by Kevin Gurney

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
## [FLBlagg/New-Government-Mod-2](https://github.com/FLBlagg/New-Government-Mod-2)@[8d8775bc94...](https://github.com/FLBlagg/New-Government-Mod-2/commit/8d8775bc94cf513fb1d79bbed5dfe5ff419617c3)
#### Wednesday 2023-10-25 21:40:46 by FLBlagg

English Localization Ver. 2.2

Ver. 2.2: "The Great Policy Rewrite"

Policy
-- Updated all descriptions
-- 'Rational Law Interpretation' --> 'Rationalist Jurisprudence'
-- 'Liberal Legal Theory' --> 'Egalitarian Jurisprudence'
-- 'Complete Legal Order' --> 'Systematic Legalism'
-- 'Community-Based Law' --> 'Communitarian Legalism'
-- 'Patriarchal Legal Code' --> 'Authoritarian Jurisprudence'
-- 'Imperial Order Argument' --> 'Imperative Legalism'
-- 'Customary Law Interpretation' --> 'Traditionalist Jurisprudence'
-- 'Proportional Representation Election' --> 'Inclusive Electoral Model'
-- 'Large Constituency Election' --> 'Multi-Seat Constituency Model'
-- 'Small Constituency Election' --> 'Single-Seat Constituency Model'
-- 'Proxy Election' --> 'Abstracted Electoral Model'
-- 'Formalistic Election' --> 'Ceremonial Electoral Process'
-- 'Election of Dignitaries' --> 'Elite Electoral Model'
-- 'No Election' --> 'Non-Electoral Governance'
-- 'Direct Election' --> 'Direct Democracy Model'
-- 'House of Representatives and House of Councillors' --> 'Bicameral Representative Model'
-- 'House of Citizens and Federal House' --> 'Federalist Assembly Model'
-- 'House of Commons and House of Lords' --> 'Hereditary and Commoner Assembly'
-- 'Constitutional House' --> 'Formalist Legislative Body'
-- 'Tax-Free Paradise Law' --> 'Taxless Haven Protocol'
-- 'Tax Reduction' --> 'Low-Tax Schema'
-- 'Reduced Tax Law' --> 'Essential Goods Tax Relief'
-- 'Thorough Investigation' --> 'Comprehensive Audit Program'
-- 'Agent Law' --> 'Tax Farming Ordinance'
-- Pay Until You Run Out of Money Law --> Exorbitant Taxation Protocol
-- Made second "Ritual Law" unique
-- Customs Only --> Unwritten Honor System
-- Selling Honors --> Commercial Honors Scheme
-- Anti-Honors Law --> Honor Abolition Act
-- Advanced Honors System --> Evolving Honors Architecture
-- Expression Method --> Informational Governance
-- SNS Golden Rule --> Galactic Connectivity Protocol
-- Removed Guarantee from "Freedom of Press"
-- State-run Media --> Unified Media Directorate
-- Need to Know --> Informational Stratification
-- Demon of Discipline --> Discipline Ascendancy
-- Expansion of Military Curriculum --> Strategic Training Reform
-- Military Goods Export --> War Materiel Export Initiative
-- Officer Rank Purchase System --> Rank Commodification Scheme
-- Authorization of Plunder --> Plunder Legitimization Act
-- Private Embezzlement --> Military Corruption Decree
-- Theological Council --> Divine Oversight Committee
-- Life Ethics Committee --> Biotethical Council
-- Deregulation --> Scientific Freedom Doctrine
-- Special Ethics Regulations for Different Species --> Xenoethical Asymmetry Protocol
-- Protection of Mother Tongue --> Heritage Language Preservation
-- Dialect Protection --> Regional Linguistic Heritage
-- Common Language Education --> Capital Linguistic Standardization
-- Unified Language Education --> Linguistic Uniformity Mandate
-- Galactic Common Language Education --> Universal Galactic Lexicon
-- State Sponsorship --> State-Funded Athleticism
-- Corporate Sponsorship --> Commercial Athletic Patronage
-- Community Based Support --> Grassroots Athletic Movement
-- Individual Effort --> Self-Reliant Athleticism
-- Work First --> Productivity Over Play
-- No Time For Fun --> Work-Only Doctrine
-- Worker's Priority --> Worker-First Legislation
-- General Regulation --> Balanced Regulation
-- Corporate Priority --> Enterprise-Driven Employment
-- Deregulation --> Free Market Labor
-- Government-Led --> State-Directed Research
-- National Sponsorship --> National Research Patronage
-- Private-led --> Privatized Research
-- Holding Back on Intervention --> Restrained Diplomacy
-- Conceal Intervention --> Cloaked Operations
-- Focus on Foreign --> External Intelligence Focus
-- Balance --> Balanced Intelligence
-- Focus on Counterintelligence --> Internal Security Focus
-- Free Will --> Autonomous Robotics
-- Managerial Guidance --> Centralized Robotics Control
-- Appropriate Priority --> Role-Based Robotics
-- Single Member System --> Unicameral Decision-Making
-- Triple Member System --> Multicameral Review
-- Mixed System --> Hybrid Legislative System
-- Commission System --> Committee-Based Legislation
-- Rubber Stamp --> Pro Forma Legislation
-- Trade Promotion --> Trade Expansionism
-- Protective Trade --> Protectionist Policy
-- Supreme Code --> Immutable Charter
-- Traditional Constitution --> Heritage Charter
-- Liberal Constitution --> Progressive Charter
-- Constitutional Law --> Dynamic Charter
-- Unwritten Legal Code --> Customary Governance
-- Gentlemanly Sneer --> Elevated Derision
-- Storm of Irony --> Ironic Rebuke
-- Intellectual Provocation --> Cultured Contempt
-- Vulgar Laughter --> Blunt Ridicule
-- Imperial Data Bank --> Centralized Data Repository
-- Imperial Central Library --> National Manuscript Archive
-- Local Records Archives --> Decentralized Archiving
-- Complete Freedom --> Unrestricted Liberties
-- Self Responsibility --> Liberty with Accountability
-- Civil Liberties Law --> Regulated Liberties
-- Maintaining Order --> Social Stability
-- Community Monitoring --> Community Oversight
-- Continuous Monitoring --> Ubiquitous Surveillance
-- Hereditary Bureaucrat --> Lineage-Based Service
-- Licensed Bureaucrat --> Credential-Based Service
-- Electoral Bureaucracy --> Democratic Service
-- Appointed Bureaucrat --> Nominated Service

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[c75da9d57d...](https://github.com/unit0016/effigy-se/commit/c75da9d57d0d3c5be8c4c729b28f58634681cb30)
#### Wednesday 2023-10-25 22:00:58 by Unit0016

Merge branch 'holy-fucking-shit-its-john-slasher-from-hit-gmod-game-slasher-co-gaming-wow' of https://github.com/effigy-se/effigy-se into slash-me-up-inside

---
## [ChakatStormCloud/Tannhauser-Gate](https://github.com/ChakatStormCloud/Tannhauser-Gate)@[ad3a5d23e4...](https://github.com/ChakatStormCloud/Tannhauser-Gate/commit/ad3a5d23e4c2dd6e5a077db929f87a7444ad4d0e)
#### Wednesday 2023-10-25 23:06:21 by SkyratBot

[MIRROR] buffs embed pulling with hemostats, allows wirecutters to pull embeds too [MDB IGNORE] (#23702)

* buffs embed pulling with hemostats, allows wirecutters to pull embeds too (#78256)

## About The Pull Request
- Wirecutters or tools with wirecutter behaviors are now valid for
plucking embeds.
- Pluck speed no longer **starts** at 2.5 seconds, which is a pretty
dang long time, especially if you have bad embed RNG. I'll do the math
and run some more tests in the morning.
- Wirecutters have a speed malus in regards to plucking embeds. I should
probably make it worse to account for, like, jaws of life or something.
- Plucking embeds with wirecutters now hurts! It hurts way less than
ripping it out with your hands, but it still hurts!

For comparison's sake, bare-handed throwing star removal compared to
possible tools.

![image](https://github.com/tgstation/tgstation/assets/31829017/96730fa5-77b8-4f31-83ba-48d36e4e419b)

## Why It's Good For The Game
Embeds kinda suck to deal with. This is intentional - I get that.

However, hemostat pulling is kind of... kind of bad. Awful, really. 2.5
seconds is a lot of time. I know it's not supposed to be the best
option, but if you've got a tool, I'd at least like to think it'd be
slightly less bad than shoving your fingers into your wound?

## Changelog

:cl:
balance: Pulling embedded items e.g. shrapnel with hemostats is now a
lot faster, and scales appropriately with toolspeed.
balance: You can now pull embedded items with wirecutters, at a speed
penalty.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

* buffs embed pulling with hemostats, allows wirecutters to pull embeds too

---------

Co-authored-by: Hatterhat <31829017+Hatterhat@users.noreply.github.com>
Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

---
## [netket/netket](https://github.com/netket/netket)@[34bd4adde1...](https://github.com/netket/netket/commit/34bd4adde13df35b65f4f055a750dda242fdfa20)
#### Wednesday 2023-10-25 23:27:04 by Filippo Vicentini

Simplification of dispatch logic/definition of new observables (#1605)

Our funny @alleSini99 recently contributed a set of Renyi entropy
estimators, which are defined to inherit from `ÀbstractOperator`, so we
need to define some methods like `ìs_hermitian` that do not make much
sense for such object.

Moreover, to define the gradient, the dispatch rule for this observable
has this ugly-as-hell `TrueT`or `Literal[True]` that nobody besides me
understands.

This PR is an attempt to
 - Simplify the creation of a new generic operator/observable
 - Simplify the definition of signatures for dispatch of expect/grad by:
   - remove `use_covariance` argument from the general interface
- only keep `use covariance` for the expectation value of operators
where it make sense, and it will not be part of the dispatch signature

In practice...

- This introduces a new super type of AbstractOperator which I
call `AbstractObservable`. The difference between Abstract Operator and
AbstractObservable is that an Observable is very general and requires
nothing besides an Hilbert space. No is hermitian or dtype arguments. So
it should cover the most general case.

- Renyi entropy estimator is transitioned to this interface.

- The signature that users must define for expectation value estimators
will now be
```python
@dispatch
def expect(vs: MCState, ob: Reny2Entropy, chunk_size: Optional[int]):
  pass
```
and for gradients will be (the much simpler)
```python
@dispatch
def expect_and_grad(vs: MCState, ob: Reny2Entropy, chunk_size: Optional[int]):
  pass
```

Incidentally, this will make it simple to implement different types of
chunking like @chrisrothUT wants to do in #1590 by dispatching on a
tuple of integers for the chunk size instead of just an integer. Right
now the dispatch logic is very messy and this would not be easy to do.

Note that users are required to specify the chunk size, and if thy don-t
support it they have to explicitly state `chunk_size: None`. I could
relax this requirement but it makes user-defined code future-proofed in
case we add more arguments.

The main problem with those changes is that it breaks user-defined
operators using the past syntax. This is not strictly a problem because
this part of the interface is documented to be unstable, though it's
annoying.
I could add some inspect magic to detect usages of the old signatures
and auto-convert them to the new format and warn. To be experimented
with.

---

