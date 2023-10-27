## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-10-26](docs/good-messages/2023/2023-10-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,470,093 were push events containing 3,767,339 commit messages that amount to 290,343,762 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 72 messages:


## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[6f8b1ed350...](https://github.com/TaleStation/TaleStation/commit/6f8b1ed350605c20e0338a6a7e37d39de3dc47b5)
#### Thursday 2023-10-26 00:00:29 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic skeletons (#8313)

Original PR: https://github.com/tgstation/tgstation/pull/79206
-----

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

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[240fe18e1d...](https://github.com/TaleStation/TaleStation/commit/240fe18e1df68a8a2e6194f0bfa99da66f1e0478)
#### Thursday 2023-10-26 00:01:40 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic drones (#8295)

Original PR: https://github.com/tgstation/tgstation/pull/79109
-----
## About The Pull Request

Fixes #68825
Fixes #72249
Fixes #70184

Converts maintenance drones to use the basic mob framework. As drones
don't use AI, this was mostly a perfunctory conversion, but I took the
opportunity to clean up drone code a bit and fixed a few bugs.

Noteworthy changes:
- Drones now have a `can_unhack` field. This is set to FALSE on
syndrones, because unhacking them doesn't make them stop being evil but
does cause some weirdness. Syndrones are unused right now, but you never
know.
- Drones use the Dextrous component for hand-having.
- Drones no longer have an internal ID card, instead being given
all-access with the `simple_access` component.
- Picking up drones now works the same as for other mobs, instead of
pointlessly copying the code into `attack_hand`. As a consequence, it is
now possible to punch drones if you want to for some reason.
- Drones can now reboot/cannibalize dead drones without being in combat
mode.
- Cannibalizing a drone that contains a client no longer runtimes - the
client is ghosted ahead of time.
- Drones now have TRAIT_ADVANCEDTOOLUSER, allowing them to properly
interact with machines.
- Trying to screwdriver a dead drone now gives a balloon alert about why
you can't do that.

In addition to these changes, I cleaned up the code quite a bit,
organizing things better and placing more useful comments throughout.
And removing a hell of a lot of single-letter variable names.

I will note that this PR does _not_ address #72129. The issue there is
that sprites for drones-as-hats are entirely nonexistent, and I'm not a
spriter. It shouldn't be too hard to fix if someone makes dronehat
sprites, though!

## Why It's Good For The Game
Kills 8 more simple animals.

In addition to that, drones were clearly a bit neglected, so this fixes
them up a bit and makes the code a little bit clearer. Maybe not that
much clearer, but it's something. It certainly leaves them in a better
place for further work if anyone wants to do that. Plus, a bunch of bugs
and other jankiness are fixed now, which is nice.

## Changelog
:cl:
refactor: Maintenance Drones now use the basic mob framework. This
shouldn't come with any noticeable gameplay changes, but please report
any bugs.
fix: Drones can now interact normally with electrified doors.
fix: Drones' built-in tools can no longer be placed in storage objects
and/or thrown on the floor.
fix: Drones can now perform right-click interactions correctly, such as
deconstructing reinforced windows.
fix: Drones can now reboot or cannibalize other drones without being in
combat mode.
/:cl:

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9ff9e4b9a8...](https://github.com/tgstation/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Thursday 2023-10-26 00:03:24 by necromanceranne

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[071f6063e6...](https://github.com/tgstation/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Thursday 2023-10-26 00:03:24 by carlarctg

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[ada7d697ba...](https://github.com/TaleStation/TaleStation/commit/ada7d697ba1fa5ec548b8cc275b9615d360a0c09)
#### Thursday 2023-10-26 00:04:23 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic Constructs: Artificer (#8254)

Original PR: https://github.com/tgstation/tgstation/pull/79015
-----
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

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[c0a9077b12...](https://github.com/TaleStation/TaleStation/commit/c0a9077b1296076e76692102b94d0e1b81572877)
#### Thursday 2023-10-26 00:04:23 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds missing default biotypes to some damage procs (#8259)

Original PR: https://github.com/tgstation/tgstation/pull/79102
-----
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

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[cdb19971b7...](https://github.com/TaleStation/TaleStation/commit/cdb19971b7a9b7b96d5897e990d2892eae680dc8)
#### Thursday 2023-10-26 00:04:23 by TaleStationBot

[MIRROR] [MDB IGNORE] [NO GBP] Fixes scream for me, and also fixes literally EVERY INSTANCE of non-random puncture wounds (#8258)

Original PR: https://github.com/tgstation/tgstation/pull/79043
-----
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

Co-authored-by: nikothedude <59709059+nikothedude@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[ff0aea800b...](https://github.com/Jacquerel/orbstation/commit/ff0aea800b0ce03346d7a655deadf8b53d7f098d)
#### Thursday 2023-10-26 00:27:25 by carlarctg

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
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[0e3b7d842b...](https://github.com/Sonic121x/Skyrat-tg/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Thursday 2023-10-26 00:59:01 by SkyratBot

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
## [mike-snyder-tfs/PuTTYNG](https://github.com/mike-snyder-tfs/PuTTYNG)@[c19e7215dd...](https://github.com/mike-snyder-tfs/PuTTYNG/commit/c19e7215ddd1d6a890fdb94d89bc5ccb46151363)
#### Thursday 2023-10-26 01:01:58 by Simon Tatham

Replace mkfiles.pl with a CMake build system.

This brings various concrete advantages over the previous system:

 - consistent support for out-of-tree builds on all platforms

 - more thorough support for Visual Studio IDE project files

 - support for Ninja-based builds, which is particularly useful on
   Windows where the alternative nmake has no parallel option

 - a really simple set of build instructions that work the same way on
   all the major platforms (look how much shorter README is!)

 - better decoupling of the project configuration from the toolchain
   configuration, so that my Windows cross-building doesn't need
   (much) special treatment in CMakeLists.txt

 - configure-time tests on Windows as well as Linux, so that a lot of
   ad-hoc #ifdefs second-guessing a particular feature's presence from
   the compiler version can now be replaced by tests of the feature
   itself

Also some longer-term software-engineering advantages:

 - other people have actually heard of CMake, so they'll be able to
   produce patches to the new build setup more easily

 - unlike the old mkfiles.pl, CMake is not my personal problem to
   maintain

 - most importantly, mkfiles.pl was just a horrible pile of
   unmaintainable cruft, which even I found it painful to make changes
   to or to use, and desperately needed throwing in the bin. I've
   already thrown away all the variants of it I had in other projects
   of mine, and was only delaying this one so we could make the 0.75
   release branch first.

This change comes with a noticeable build-level restructuring. The
previous Recipe worked by compiling every object file exactly once,
and then making each executable by linking a precisely specified
subset of the same object files. But in CMake, that's not the natural
way to work - if you write the obvious command that puts the same
source file into two executable targets, CMake generates a makefile
that compiles it once per target. That can be an advantage, because it
gives you the freedom to compile it differently in each case (e.g.
with a #define telling it which program it's part of). But in a
project that has many executable targets and had carefully contrived
to _never_ need to build any module more than once, all it does is
bloat the build time pointlessly!

To avoid slowing down the build by a large factor, I've put most of
the modules of the code base into a collection of static libraries
organised vaguely thematically (SSH, other backends, crypto, network,
...). That means all those modules can still be compiled just once
each, because once each library is built it's reused unchanged for all
the executable targets.

One upside of this library-based structure is that now I don't have to
manually specify exactly which objects go into which programs any more
- it's enough to specify which libraries are needed, and the linker
will figure out the fine detail automatically. So there's less
maintenance to do in CMakeLists.txt when the source code changes.

But that reorganisation also adds fragility, because of the trad Unix
linker semantics of walking along the library list once each, so that
cyclic references between your libraries will provoke link errors. The
current setup builds successfully, but I suspect it only just manages
it.

(In particular, I've found that MinGW is the most finicky on this
score of the Windows compilers I've tried building with. So I've
included a MinGW test build in the new-look Buildscr, because
otherwise I think there'd be a significant risk of introducing
MinGW-only build failures due to library search order, which wasn't a
risk in the previous library-free build organisation.)

In the longer term I hope to be able to reduce the risk of that, via
gradual reorganisation (in particular, breaking up too-monolithic
modules, to reduce the risk of knock-on references when you included a
module for function A and it also contains function B with an
unsatisfied dependency you didn't really need). Ideally I want to
reach a state in which the libraries all have sensibly described
purposes, a clearly documented (partial) order in which they're
permitted to depend on each other, and a specification of what stubs
you have to put where if you're leaving one of them out (e.g.
nocrypto) and what callbacks you have to define in your non-library
objects to satisfy dependencies from things low in the stack (e.g.
out_of_memory()).

One thing that's gone completely missing in this migration,
unfortunately, is the unfinished MacOS port linked against Quartz GTK.
That's because it turned out that I can't currently build it myself,
on my own Mac: my previous installation of GTK had bit-rotted as a
side effect of an Xcode upgrade, and I haven't yet been able to
persuade jhbuild to make me a new one. So I can't even build the MacOS
port with the _old_ makefiles, and hence, I have no way of checking
that the new ones also work. I hope to bring that port back to life at
some point, but I don't want it to block the rest of this change.

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[a8edd9004f...](https://github.com/Zergspower/tgstation/commit/a8edd9004f1875bd3be409e2f382933a74bf8a40)
#### Thursday 2023-10-26 01:04:19 by carlarctg

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
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[4b73b37d60...](https://github.com/Zergspower/tgstation/commit/4b73b37d60dbff8746ffb3e1eb0f6ff51895fffc)
#### Thursday 2023-10-26 01:04:19 by jimmyl

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
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[b65f729901...](https://github.com/Jacquerel/orbstation/commit/b65f729901fdb342b832fb3365d72afd076f8c3b)
#### Thursday 2023-10-26 01:10:14 by lizardqueenlexi

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
## [Abdelghafour29/monopolygo](https://github.com/Abdelghafour29/monopolygo)@[412d62e4c1...](https://github.com/Abdelghafour29/monopolygo/commit/412d62e4c1f1f86ef8ca53beed592d27235662e5)
#### Thursday 2023-10-26 01:10:51 by Abdelghafour29

MONOPOLY GO FREE DICE LINK 2023

Are you looking to get ahead in the game of Monopoly Go? Well, look no further because I've got the inside scoop on how to get those coveted Monopoly Go free dice rolls that will give you an edge over your opponents. I've been using this fantastic website to get free dice rolls since the game came out, and it has never failed me once. Here's how it works.
 
How to Get Fre Dice Rolls in Monopoly Go
First, pick up your phone and navigate to 5souq.shop . Once you land on the site, look for the "Play" button to kick things off. The next step is to key in your Monopoly Go username when prompted. 
After you've entered your username, hit the "Continue" button and watch as the site works its charm. It will swiftly hunt down your username and alert you when it's found it! All that’s left is to press “Play” to get into the action.
However, there's one small step before you can get your hands on those dice rolls. It's a quick security check to confirm that you're not some pesky bot trying to game the system. But don't sweat it; this process is fast and straightforward, designed solely to make sure real people like yourself are the ones reaping these incredible rewards
What Can You Do With Monopoly Go Free Dice Rolls
Imagine your advantage over opponents when you can access almost unlimited dice rolls. You'll be able to travel around the board faster, acquire more properties, and become the ultimate Monopoly Go champion. So why wait? Head to 5souq.shop and start winning those free dice rolls in Monopoly Go today!
Is This Monopoly Go Glitch Site Safe?
But hold on, you might wonder if this is safe and legitimate. Well, let me assure you that I've been using this website since the game was released, and I've never encountered a single issue. It's completely safe and legitimate to use.
Here's a golden nugget: the website we're talking about works like magic to supercharge your Monopoly Go gameplay. How, you ask? It offers an endless supply of dice rolls! This means no more waiting or relying on luck – it’s all there for your gaming pleasure.
So, grab this golden chance to amp up your Monopoly Go prowess. Snag those free dice rolls and start crushing it. It’s time to rule the game board and let your buddies know who's boss in Monopoly Go!
Don't forget, Monopoly Go is more than just a race to the finish line; it's a strategic battlefield of negotiation and chance. Think on your feet, make each extra dice roll count, and pounce on every golden opportunity that comes knocking.
Grab your smartphone, load up Rolls Glitch, and let the games begin! Happy rolling!
How to Get Free Dice on Monopoly Go?
Monopoly Go Free Dice, the digital rendition of the classic board game we all know and love, has taken the gaming world by storm. However, one element often stands between players and a seamless gaming experience: the need for free dice on monopoly go. In this article, we'll delve into the strategies and secrets on how to get free dice on Monopoly Go hack, enhancing your gameplay without breaking the bank
A. Brief Overview of Monopoly Go free dice
Monopoly Go free dice hack combines the nostalgia of the traditional Monopoly hack board game with the convenience of digital gaming. Players buy, sell, and trade properties in a virtual world, aiming to bankrupt their opponents.
B. Importance of Free Dice in Monopoly go
Dice are the lifeblood of Monopoly Go free dice, determining the player's moves and, ultimately, their success in the game. Acquiring free dice can significantly impact the gaming experience, providing a competitive edge without the need for in-game purchases.
C. monopoly go free dice
Traditionally, players obtain free dice in monopoly go  While this is a straightforward method, it may pose challenges for those not willing to claim free dice and rolls on monopoly go hack.
D. Challenges Faced by Players to get free dice links monopoly go
Many players find it frustrating to get free dice links monopoly go or struggle with limited resources. This can hinder the enjoyment of the game and claim free dice link.
E. Strategies to get Free Dice Links on monopoly go
Developing effective strategies to get free dice links on monopoly go discord involves understanding the community dynamics and staying engaged with fellow players. This section explores successful approaches for free dice rolls monopoly go hack.
While the quest for free dice links is legitimate, players must exercise caution to avoid to get free dice link monopoly go. Stick to official channels and recognized community forums.
Monopoly Go free dice encourages community engagement, allowing players to share free dice links with friends. While direct sharing may not be built into the game, community platforms provide avenues for sharing
F. monopoly go dice hack
Monopoly Go dice hack offers daily login bonuses and rewards, including free dice hack. Regularly logging in and engaging with the game ensures a steady supply of monopoly go dice hack to bolster your dice collection.
Keep an eye on special in-game events and promotions, as they often feature exclusive free dice hack on monopoly go discord as rewards. Active participation during these events can significantly increase your dice inventory.
The Role of Free Dice in Monopoly Go

As discussed in the comprehensive guide above, free dice in Monopoly Go serve as a valuable in-game resource. Acquiring them can enhance a player's strategic options and overall gaming experience. The pursuit of free dice adds an exciting dimension to the gameplay, encouraging players to explore different avenues within the virtual world of Monopoly Go.

Whether you're a seasoned Monopoly enthusiast or a newcomer to the game, Monopoly Go provides an engaging and interactive platform to experience the timeless joy of property management, negotiation, and strategic decision-making.

In conclusion, Monopoly Go successfully translates the classic board game into the digital era, embracing the evolving landscape of online gaming while preserving the essence of Monopoly's enduring appeal. So, roll the virtual dice, make shrewd deals, and aim for victory in the dynamic world of Monopoly Go.

Other Ways to Get Monopoly Go dice and rolls :

In the vibrant world of Monopoly Go, there are various avenues and strategies for acquiring additional dice and rolls beyond the traditional methods. Let's explore some alternative ways to bolster your collection and enhance your gameplay experience.

1. Participate in In-Game Events:
Keep an eye on special in-game events organized by the developers.
Events may offer bonus dice and rolls as rewards for completing specific challenges or milestones.

2. Daily Login Rewards:
Many games, including Monopoly Go, feature daily login rewards.
Logging in regularly can earn you free dice and additional rolls, providing a consistent boost to your resources
.
3. Refer-a-Friend Programs:
Check if Monopoly Go has a refer-a-friend program.
Inviting friends to join the game could result in bonus dice or rolls as a reward for expanding the player community.

4. Watch Advertisements:
Some games offer players the option to watch short advertisements in exchange for in-game rewards.
Look for opportunities to watch ads and earn free dice or additional rolls.

5. Complete Surveys and Offers:
Explore the in-game options for completing surveys or engaging with sponsored offers.
Participating in these activities might earn you bonus dice and rolls.

6. Join Online Forums and Communities:
Engage with the Monopoly Go community on forums and social media.
Fellow players may share tips and information about special promotions or events that offer free dice.

7. Participate in Developer Livestreams:
Some game developers host livestream events.
Participating in these events or contests could lead to exclusive rewards, including free dice and additional rolls.

8. Complete Achievements and Challenges:
Explore the game's achievements and challenges system.
Successfully completing specific in-game challenges often results in rewards, including extra dice for your collection.

9. Check for Limited-Time Promotions:
Keep an eye on the game's official website or social media channels for announcements of limited-time promotions.
These promotions may offer exclusive opportunities to earn free dice and rolls.

10. Utilize Redemption Codes:
Some games provide redemption codes that players can enter for special rewards.
Check official announcements or community forums for any available redemption codes.
By exploring these alternative methods, you can expand your arsenal of dice and rolls in Monopoly Go. Remember to stay engaged with the game's community and remain vigilant for announcements and opportunities that could lead to 
additional in-game resources. Happy rolling!

How To Get Free Dice Links in Monopoly Go?

As of my last knowledge update in September 2022, there isn't a standardized method for obtaining free dice in Monopoly Go through direct links or URLs. Game developers often implement various strategies to distribute rewards, including free dice, such as in-game events, promotions, or giveaways.

To find opportunities for free dice in Monopoly Go, consider the following:

free spins monopoly go:
To get free spins in Monopoly Go follow the official social media platforms (Facebook, Twitter, Instagram).
Developers often announce events or share links to claim free spins on these games.

free dice monopoly go discord:
Regularly check discord to get free dice hack.
Game developers may provide links or codes for free dice as part of special promotions.

monopoly go dice hack:
Engage with the Monopoly Go hack community on official forums or fan websites.
Players often share information about ongoing promotions and freebies.

Participate in Events:
Join in-game events or discourd.
These events often provide opportunities to earn free dice link as rewards.
Email Newsletters:

Subscribe to newsletters from the game developers.
Developers may occasionally send out newsletters with links or codes for in-game rewards.
It's essential to note that the availability of free dice and the methods to obtain them can change based on the game's updates and promotional activities. Always ensure that any links or promotions you explore are legitimate and directly affiliated with the official Monopoly Go hack channels.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0d5f9907a2...](https://github.com/tgstation/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Thursday 2023-10-26 01:30:55 by Jacquerel

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
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[0788c987ac...](https://github.com/vdaular-dev/linksfordevs/commit/0788c987aca57adca910c3a9df6cf6446f5b2370)
#### Thursday 2023-10-26 02:02:45 by Ben Dornis

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
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[eb0f0559aa...](https://github.com/ARF-SS13/coyote-bayou/commit/eb0f0559aaea59ecb7d9dcaadafbf1755d89c79a)
#### Thursday 2023-10-26 02:06:34 by Lynx

QuirkFix =Typo fix, Grammar fix, and punctuation=

Changes a lot of different quirk details, added a lot of medical record text, and also added missing "Lose" and "Gain" text for quirks in case an admin wants to give it to someone so that the player can confirm, or an eventual item granting it.

--Changes a lot of grammar, too, for example, like 1071->(1094), its probably not even needed to change it, but it felt a lot easier to read to understand that your max cap went to 25, instead of ONLY 5, to make sure that its clear that it isn't just a bump up to 25 for starter healing, no no, its a permanent 25.

--Some comments, like the radiation one at 1378-79 -> (1404-06), have been made to be a bit more ... vague. Because, well, you just somehow decided out of the god damn blue you're RAD resistant... So you've just decided radiation is basically an afterthought. Does NOT mean you're *IMMUNE* to it. It's a hopeful change that'll make players wonder how resilient they are to radiation, since it depends from person to person. Also. It's their god damn decision apparently if RADS HURT EM OR NOT >:D

--A LOT of the medical record text is to, hopefully, encourage medical personnel to read the medical logs if those even exist on CB. I don't actually know. But, this would also encourage characters and the players to toy around with their medical text if they don't like how cluttered it is from how the medical staff wrote it. It's not intended to be bad; but, every Quirk is ... well, a quirk. This is supposed to be a pretty high end roleplay server (not crazy high since pve duh) but it's intended to have people actually do a lot of smaller things as far as I can tell in-between combat.
(But I may be wrong. Please tell me if I am on discord. Username =   " l_ynx "

I don't think I touched quirk values, as I reverted my change from the empath one back down to 0. I still think its more of a useful quirk; but thats just me.

--A lot of punctuation has been fixed. Some quirks didn't have periods, some did have periods, but too many, and some had a marker at the end, WITH punctuation!.  ;)

---
## [StrawWagen/termhunter](https://github.com/StrawWagen/termhunter)@[2b2b134138...](https://github.com/StrawWagen/termhunter/commit/2b2b134138cd73febdab4fd475e22e20583678bd)
#### Thursday 2023-10-26 02:31:11 by StrawWagen

Weapons compatibility + many more tweaks

Changed default weapon drop count + changed var's name
Added var to disable extreme unstucking ( teleporting ) termhunter_doextremeunstucking, default 1

Buffed fists damage overall, from 4 hits to kill, to 3 hits.
Overcharged terminator 1 hit kills.

Bot will now try and test up any weapon it can, not just ones that expect npcs.
Added polished support for m9k + m9kr + MW base.
To facilitate this, added more player function hacks.
Added new system to override problem functions in weapons, works 'recursively' through the wep and it's bases.
Bot now is much better at guessing weapon ranges.
Bot now properly judges weapons in singleplayer.

Added new weapon holstering system, bot will intelligently put weapons on its back/hip, required lots of work throughout the ai to get this right.

Behaviour changes:
Bot will bait out enemies with staring if there's other bots closing in on them
Bot will now immediately react if the enemy is in god mode, or has more than 10000 health.
Fixed bot trying to jump over it's enemy.
Bot will not stop staring if they're standing in a room's only exit.
When a weapon kills a bot, they will then try and pick that one up over others.
Fearful bots will overcome their fear of an enemy player if they die enough.
Bots will wait a very short time before they start firing at enemies ( <1s )
Stalking enemies will now slowly close in on their enemies.
Bots with long range weapons will snipe more often, and for longer.
RPG shoots faster, and the bot will try and splash damage their enemy.

---
## [juliet-gobran/portfolio](https://github.com/juliet-gobran/portfolio)@[1dc5ebb06c...](https://github.com/juliet-gobran/portfolio/commit/1dc5ebb06ce3406b30a41c2f05b0af935c64b005)
#### Thursday 2023-10-26 03:21:17 by Juliet Gobran

Ready to be deployed... thank fuck

after PAINFUL debugging & the stupid 'public' directory issues.... IT IS READY FOR PROD

---
## [dacook/openfoodnetwork](https://github.com/dacook/openfoodnetwork)@[c12389be13...](https://github.com/dacook/openfoodnetwork/commit/c12389be139f6d07040c46964ae54015bf6944e9)
#### Thursday 2023-10-26 03:24:39 by David Cook

Disable form elements in a disabled-section

I chose to use the 'elements' collection rather than choosing which elements to include (ie this supports inputs, textareas, buttons and anything else I didn't think of). It could be a bit simpler if we assume the element is a form. Even simpler if it's a fieldset (that has a disabled property). But I didn't want to limit it too much.

Unfortunately JS is quite ugly compared to Ruby. And 'prettier' made it uglier in my opinion.

---
## [catapultam-habeo/pyrelight-server](https://github.com/catapultam-habeo/pyrelight-server)@[a7b605d123...](https://github.com/catapultam-habeo/pyrelight-server/commit/a7b605d123faee410e76b0c1d7b856a0ede85898)
#### Thursday 2023-10-26 03:49:01 by catapultam-habeo

Attempt to generalize item varient checks

oops

I'm so tired of being stupid

oops

Revert "Modulo item checks"

This reverts commit 41d8659cc06a4afb13017d944af7775decacbfb2.

Revert "trying to fix apparently broken bst epic?"

This reverts commit aa0c0f79601c13ece1ee6b007b72dc6793be5cba.

trying to fix apparently broken bst epic?

debugging beastlord epic

more

fcsk

f

bah

f

f

fuck

f

f

f

f

Modulo item checks

test

---
## [UBCFormulaElectric/Consolidated-Firmware](https://github.com/UBCFormulaElectric/Consolidated-Firmware)@[48ee00ec77...](https://github.com/UBCFormulaElectric/Consolidated-Firmware/commit/48ee00ec772e45a997365bdf7dadaecc117a31e9)
#### Thursday 2023-10-26 04:31:19 by Gus Tahara-Edmonds

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
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[2a74c23d62...](https://github.com/shiptest-ss13/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Thursday 2023-10-26 04:49:08 by Imaginos16

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
## [TheDailySimile/PedalPonder](https://github.com/TheDailySimile/PedalPonder)@[5b4b64877a...](https://github.com/TheDailySimile/PedalPonder/commit/5b4b64877af3f8ca85ab385ddc4c9e1c152cfd2f)
#### Thursday 2023-10-26 05:41:51 by The Daily Simile

Update Ash : Next Term Phantom@Instrument Oriented Dissolution.html

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
Ash@shrug : "before the BATTLE resumes Mr Santanore unlike Ms Santanore you already know my inclinations thus may be the reason why you despite not being a general trainer and yet to intervene in a interregional final without anyone complaining against your choice..is all because of your deep knowledge on my inclinations..on self help ain't it.."
Marc@scowl : "Saku lost because of purity of vision thus with her bunch was over the moon understanding instrument oriented dissolutions but purity is a counter indeed to your..analogy obsession#..The Meaning of Lie,#,..Ash un..long,#,..and hence i having recalled my practice of connections between non self and desires intervened#..Light upon Darkness,#,..Marc un..long,#,.."
Ash@shrug : "fair enough you refuse to submit to..desires for liberation from obviousness..thus this..joy of..Yiyui!.."
Referee@veryAngry : "ai ai you choose associate fire to signify the volatility of self commitment to a chosen ego along with darkness of absolute witness i'll disqualify you ok.."
Marc@angry : "you lowlife don't create an intrigue of provability to your thoughts on own memorial knowledge ok this was only a counter to Defeat : Victory Lie#..Gary&Ingemar+Blythe..who are you,Ash Ketchum Pokemon Master,ego sinister we see,me..you see only compeers..me thus indeed as a counter isn't it so..shh..it was included..
Phantom : The Meaning of Lie..
any noise in thoughtful chantin' of soul?,#,..Ash un..long,#,.."
Yiyui@giggle : "ei vision eh blur aim boo charred i or thy/or who see as this or i..i..
shh..shh..shh..shh..shuu..uu..uu..blast/or cue cue cue cue cue see why never past.."
Marc@scowl : "i see this is the generalization of..next term..unless i admit defeat and stop my self from venturing into it's randomness i will be deemed a phantom cunning indeed Ash..as Ash means i read in those sickening comics popularized by you..Ash : Next Term..Phantom,#,..Ash : Next Term Phantom,#,..Ash un..long,#,.."
[Brock@CoOrdinator,Dentarou@CoOrdinator Slate
Tracey@P.Doctor Skechit
Daisy@P.Doctor,Violet@CoOrdinator,Lily@Psychic-Dark,Misty@Ghost-Fairy]@Pebblefog,Mintale
....
[Marc@Psychic-Dark,Sakura@Local Santanore
Ingemar@P.Doctor,Mahina@CoOrdinator Iptil
Blythe@P.Doctor,Ayub@Ghost-Fairy Birch]@Duskneon,Paldea

{Juritared,Decolore}

Gary+Lily
Brock+Violet
Ingemar+Blythe
Ayub+Sakura
..
Dentarou+Mahina
Tracey+Daisy
Ash+Misty
Marc

Marc@scowl : "so all along it was a trick to deny the truth only to be the more..engaging#.."
Ayub@giggle : "practicing.. it's said devotion is best practiced as is infatuation in denial of freedom of self through detachment why#..The Milestones of Self-Sufficiency,#,..Ayub un..long,#,.."
Misty@giggle : "yeah yeah you tried to deny the subsuming of absolute as a self consumed way to assurance thus upon instrument agnostic apocalypse of thoughts had to admit defeat to..Victory : Defeat Try..nana.." 
Sakura@giggle,trying to dance with Ayub : "iii!..no your should dance with me again to that tune you questing yet method using b..#..The Milestones to Self-Dissolution,#,..Ayub+Sakura un..long,#,..that tune.. was so..um.."
Ayub@scowl,taking Sakura away : "intellectual yeah..i only waited to be able to earn..a penny.. physical not conscious thus..honourably..let's go#..Ayub+Sakura..Conclusive Witness Obsession,#,..Ash+Misty un..long#,.."
Lily@giggle : "ei Gary why the agnostic method is not active but potent only#..The Pivot Agnostics->Version->Lily flower,#,..Lily un..long,#,..
Gary@frown : "don't be so overhappy Lil when that curse appeared at Juritared it was a travesty and that lowlife still chose..my,MY hometown#..Gary..No Now Fire you oozin'/yet i alone choosin'/then is  no self you have?/as own as i do have..
yo! now fire blasts/potential with self clash/then where am i just seer's side/Lastly Ash thus means no more to find..
ann..,how did that baby survive,..that question is never going to be answered with the decolourised..shh..self ain't it Gary rhyming with parry,nature says sorry bye#..Phantom : The Meaning of Lie,#,..Ash+Misty un..long,#,.."

---
## [cyphar/runc](https://github.com/cyphar/runc)@[1bbef636f7...](https://github.com/cyphar/runc/commit/1bbef636f75a7a7b2666368b34481f843a69853b)
#### Thursday 2023-10-26 06:41:05 by Aleksa Sarai

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
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[e4c3900e4f...](https://github.com/morrowwolf/cmss13/commit/e4c3900e4f087444308138e9d05b4da9c774f6a9)
#### Thursday 2023-10-26 07:00:12 by riot

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
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[de5c69661f...](https://github.com/morrowwolf/cmss13/commit/de5c69661f8d33425123894028702f64239f861b)
#### Thursday 2023-10-26 07:00:12 by kiVts

DFB property changes. (#4590)

# About the pull request
part 2 out of 4 
This does a **big** touch up on defibrillation property in research

Well, to start off, max_level = 1 was removed. It appears warcrimes
forgot to remove it since process proc has benefits explicitly for
higher levels. I would call it a bug(oversight rather).

Second: Ghosts get notified when the chem starts to try and defib you,
so you dont just wonder how did you stand up, and pretty neat too.

Third: The >6 level of defib to apply healing like with actual item
defib is too high, so we move requirement down to >1 but make it heal
much, much worse at levels lower than 5.
eg it took 20 units to heal ~20 brute at level 3(you will literally
perma lmao), at level 5, however, this will go at around 2.5 per life
tick, level 8 will give 4 damage heal.
This is a balance change(buff) But hardly so since its research,
Research is already neglecting most of the time this property.

Fourth: removes one letter var, This whole file is entombed with them
but Im not doing that for now.

# Explain why it's good for the game


Defib property is way too underused and crudely made. This fixes it,
partially.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: kiVts
add: Ghosts get notified when they are being revived by DFB property
balance: DFB property healing threshold lowered, You can create DFB
property higher than one.
/:cl:

---------

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [thebitz420/thebitz](https://github.com/thebitz420/thebitz)@[e5fbe49517...](https://github.com/thebitz420/thebitz/commit/e5fbe4951757b20229c3484eebc3c0437af62cb4)
#### Thursday 2023-10-26 07:52:40 by Thebitz420

Create README.md

Introduction

The use of medical cannabis has been a topic of growing interest and debate in recent years. With changing laws and evolving attitudes, it's important to recognize the significance of medical cannabis in the field of healthcare. This article will delve into the importance of medical cannabis and how it is contributing to the well-being of patients, while making reference to the services provided by The Bitz 420 (https://thebitz420.uk/), a platform that facilitates access to medical cannabis products.

Pain Management
One of the primary reasons medical cannabis is gaining acceptance is its effectiveness in pain management. Many patients suffering from chronic pain, whether due to conditions like arthritis, multiple sclerosis, or even cancer, have found relief through the use of medical cannabis. Its natural analgesic properties provide a safer alternative to traditional pain medications, which often come with adverse side effects.

The Bitz 420, a trusted source for medical cannabis products in the UK, offers patients discreet access to a variety of strains and forms, including THC bud, vapes, and edibles, making it convenient for individuals seeking effective pain management solutions.

Mental Health Benefits
Beyond physical ailments, medical cannabis has shown promise in addressing mental health issues. It has been used to alleviate symptoms associated with anxiety, depression, and post-traumatic stress disorder (PTSD). The cannabinoids in cannabis interact with the endocannabinoid system, which plays a crucial role in regulating mood and emotions.

The Bitz 420 recognizes the importance of medical cannabis in mental health treatment and offers a selection of products, including calming strains and products that promote relaxation.

Managing Seizures
In recent years, medical cannabis has gained widespread attention for its effectiveness in managing seizures, particularly in patients with epilepsy. Studies have shown that specific strains of cannabis, such as those high in CBD (cannabidiol), can significantly reduce the frequency and intensity of seizures. This discovery has been life-changing for many individuals who had previously exhausted conventional treatment options.

The Bitz 420 offers access to THC bud and various products that cater to patients seeking seizure management options.

Reducing Inflammation
Inflammation is at the root of many chronic diseases, and medical cannabis is emerging as a valuable tool in reducing inflammation. Its anti-inflammatory properties can benefit patients with conditions like arthritis, Crohn's disease, and other autoimmune disorders. By mitigating inflammation, patients experience less pain and better overall health.

Supporting Cancer Patients
Cancer patients often endure the debilitating side effects of chemotherapy, including nausea, loss of appetite, and pain. Medical cannabis can help alleviate these symptoms, making the treatment process more bearable. Additionally, some studies suggest that cannabis compounds may have anti-cancer properties, which opens up possibilities for future treatments.

Conclusion

The importance of medical cannabis cannot be overstated. It offers a natural and effective alternative for pain management, mental health support, seizure control, inflammation reduction, and aiding cancer patients. Services like The Bitz 420 (https://thebitz420.uk/) play a crucial role in ensuring that patients in the UK have access to high-quality medical cannabis products while maintaining privacy and discreet shipping options.

As the medical community continues to explore the potential benefits of medical cannabis, it's becoming clear that this plant has the power to transform the lives of patients, offering relief and hope in the face of challenging health conditions.

---
## [DGamerL/Paradise](https://github.com/DGamerL/Paradise)@[c4e96e4ca0...](https://github.com/DGamerL/Paradise/commit/c4e96e4ca062342e19a84f6af76dd22ade3cc3bf)
#### Thursday 2023-10-26 08:11:19 by Alexios

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
## [Hitsquid/projectpixel.github.io](https://github.com/Hitsquid/projectpixel.github.io)@[ad0e77893a...](https://github.com/Hitsquid/projectpixel.github.io/commit/ad0e77893a9c6235562fa69dc7e6996a244e65cc)
#### Thursday 2023-10-26 08:20:48 by swaggest17

I have an announcement to make. Shadow the Hedgehog is a bitch ass motherfucker. He p

---
## [ROOT0616/New-Government-Mod-2](https://github.com/ROOT0616/New-Government-Mod-2)@[8d8775bc94...](https://github.com/ROOT0616/New-Government-Mod-2/commit/8d8775bc94cf513fb1d79bbed5dfe5ff419617c3)
#### Thursday 2023-10-26 08:23:41 by FLBlagg

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
## [ROOT0616/New-Government-Mod-2](https://github.com/ROOT0616/New-Government-Mod-2)@[021539322f...](https://github.com/ROOT0616/New-Government-Mod-2/commit/021539322f4167d2550f4ca3c828d9bf593eda64)
#### Thursday 2023-10-26 08:23:41 by FLBlagg

English Localization V2.0

Ver 2.0 "The Great Civic Re-Write"

Civics
-- Updated all descriptions to be more detailed and readable
-- 'Non-Retention Force' --> 'Pacifist Protectors'
-- 'Loose Building Codes' --> 'Lax Building Codes'
-- 'The Advanced Glory System' --> 'Sanctum of Valor'
-- 'Careless and Creative' --> 'Bohemian Enclave'
-- 'Steady Hand' --> 'Immutable Order'
-- 'Tongue-In-Cheek Survivalist' --> 'Grim Realists'
-- 'Slow and Steady' --> 'Methodical Trust'
-- 'Ruthless Realist' --> 'Machiavellian Pragmatism'
-- 'Smooth Traffic' --> 'Frictionless Traffic'
-- 'Space Security HQ' --> 'Cosmic Constabulary'
-- 'Random Birth Rate' --> 'Unpredictable Demography'
-- 'Trading Nations' --> 'Commerce Nexus'
-- 'Virtual Society' --> 'Digital Habitat'
-- 'Local Level Education System' --> 'Decentralized Enlightenment'
-- 'Chief Secretary System' --> 'Technocratic Socialism'
-- 'Lord of War' --> 'Warlord Hegmony'
-- Added 'Stellar' to 'Knights'
-- 'Honorable Imperial System' --> 'Imperial Honor'
-- 'Guiding Principle' --> 'Doctrine of Loyalty'
-- 'Freedom In Obedience' --> 'Controlled Liberty'
-- 'Court Politics' --> 'Intricate Court'
-- 'Apprenticeship' --> 'Master-Apprentice Guilds'
-- 'Demonstration Culture' --> 'Culture of Protest'
-- 'Ultimate Freedom of Thought' --> 'Boundless Thought'
-- 'Common Values' --> 'Unified Ideals'
-- 'Conquer Together' --> 'Unity in Diversity'
-- 'Emigration Fascination' --> 'Starbound Wanderlust'
-- 'Contempt For Others' --> 'Galactic Contempt'
-- 'Gentlemanly Disgust' --> 'Elegant Exclusion'
-- 'Erasing The Traces' --> 'Redaction'
-- 'Big Ship Policy --> 'Dreadnought Diplomacy'
-- 'Military Regime' --> 'Stratocracy'
-- 'Prosperity Advocate' --> 'Harmony Merchants'
-- 'Faith In Machines' --> 'Techno-Theology'
-- 'Mass Cultural Consumption' --> 'Culturephiles'
-- 'Longing For The Future' --> 'Futurist Zeal'
-- 'Experimental Practice' --> 'Reality Tinkerers'
-- 'Economic Primitivism' --> 'Neo-Primitivism'
-- 'Development Dictatorship' --> 'Autocratic Progressivism'
-- 'Economic Deregulation' --> 'Laissez-Faire Systems'
-- 'Aggressive Intelligence Agency' --> 'Covert Galactic Operations'
-- 'Information Operation' --> 'Info-Warfare Directorate'
-- 'Looking Outwards' --> 'Panopticon'
-- 'Broker Of Smiles' --> 'Serene Diplomats'
-- 'Defensive Intelligence Agency' --> 'Shield of Secrecy'
-- 'Non-Interference In Internal Affairs' --> 'Sovereign Sanctity'
-- 'Interest Representation' --> 'Proxy Diplomats'
-- 'Natural Adaptation' --> 'Biological Harmony'
-- 'Extinction Prevention Methods' --> 'Ark of Life'
-- 'Faith In Nature' --> 'Sacred Biomes'
-- 'Infrastructure Construction' --> 'Foundation Builders'
-- 'Self-Righteous Heroes' --> 'Smug Saviors'
-- 'Human Rights For Sale' --> 'Rights as Assets'
-- 'Monetary Substitute For Punishment' --> 'Justice by Coin'
-- 'Securing Real Benefits' --> 'Harvesters of Prosperity'
-- 'Highly Productive Consumer Society' --> 'Cycle of Excess'
-- 'Agricultural Cooperative' --> 'Agri-Syndicates'
-- 'Patriotic Education' --> 'Civic Indoctrination'
-- 'Charity Fund' --> 'Voluntary Redistribution'
-- 'Vassal System' --> 'Feudal Advisors'
-- 'Advanced Supply Officers' --> 'Logistical Autocrats'
-- 'Ignoring Minor Crimes' --> 'Selective Justice'
-- 'Self-Management System' --> 'Worker Autonomy'
-- 'International Development Assistance' --> 'Galactic Benefactors'
-- 'Block Economy' --> 'Inward Economists'

---
## [grafbase/grafbase](https://github.com/grafbase/grafbase)@[2b23d835dc...](https://github.com/grafbase/grafbase/commit/2b23d835dc0af57b1c6a25f8f143d9692e953429)
#### Thursday 2023-10-26 10:06:29 by Tom Houlé

composition: first bits

This commit is a proposal for a general crate structure for supergraph
composition. Everything is a suggestion and up for discussion. It is
definitely very far from complete, and some areas (error reporting) are
just sketched.

What this commit _does_ contains: a proposed public API with a compose
function:

```rust
pub fn compose(subgraphs: &Subgraphs) -> CompositionResult
```

Where `CompositionResult` is SDL for a supergraph and diagnostics.

As well as the general flow, a test suite and the two following
composition rules as a proofs of concept:

- Declaration of different kinds cannot be merged. For example if you
  have `type User { ... }` and `interface User { ... }` in two different
  subgraphs, this is a composition error.
- Objects can be merged as long as their fields do not overlap (no name
  collision). This is the simplest rule of object merging. Handling any
  directive at all is out of scope for this PR.

Here is a non-exhaustive list of design choices that may be
controversial and that we may want to discuss:

- Subgraphs are considered as a whole set, and the supergraph is an
  entirely separate data structure. There is a possibly viable
  alternative path: merging subgraphs pair-wise, with the resulting
  merged schema being the supergraph. I'm not sure I see all the
  tradeoffs clearly, but a few thoughts:

  - We can probably produce better diagnostics (errors) with global
    knowledge of all the subgraphs.
  - Supergraph SDL looks very different from the union of the subgraph
    schemas with additional rules. We would need to filter out, add
    attributes in non obvious ways to post-process the last remaining
    schema at the end of pair-wise merges.

- Composition is separate from validation of individual subgraph
  schemas, but it assumes valid schemas as input.

- Composition produces a SDL string for a supergraph, not a structured
  representation. This is because the requirements of the consumers are
  not known, and a data structure designed for rendering to SDL will
  look different from a data structure for the same supergraph but aimed
  at efficiently resolving queries. For example, `@key` directives will
  matter a great deal for composition, but as far as I can tell, they're
  not in the supergraph SDL.

  This API proposed in this commit picks the easy solution and only
  designs for rendering. The `Supergraph` type is opaque and write only
  however, so we should be able to change how it is organized internally
  relatively easily if we decide we want to use it for something other
  than rendering as GraphQL SDL in the future.

  So I see two questions to resolve:

  - Does it make sense to have a common data structure to represent a
    GraphQL schema, or do we opt for specialized data structures like
    `Subgraphs` in this commit? I think specializing is worth the
    effort, for separation of concerns and simplicity.
  - If we do want specialized data structures, should composition build
    the supergraph data structure or just SDL, and leave the supergraph
    schema data structure implementation to the router?

- String interning from the start. The main argument against doing this
  now is that it would be premature optimization. On the other hand, we
  know that when merging many subgraphs, we will store, manipulate and
  compare many strings.

  - Storage is cheaper with interning: we have only one copy of each
    string in memory.
  - Manipulation is easier with interning: since `StringId`s are `Copy`,
    we don't need to worry about lifetimes (unlike `&str`), and we don't
    need to worry about ownership and allocation (unlike `String`)
  - Comparison is cheaper: comparing small integers is cheaper than
    comparing strings.

- Efficient data access patterns from the start. More specifically,
  avoid doing anything `O(n²)` or worse on the number of types in the
  supergraph, or the number of fields in a type (think about `Query`).
  Composing large supergraphs out of many subgraphs in a reasonable
  amount of time is a requirement. It does mean that we have to maintain
  extra data structures as "secondary indexes".

---
## [seberg/numpy](https://github.com/seberg/numpy)@[af55348f5c...](https://github.com/seberg/numpy/commit/af55348f5cbe338a86ed032812ee11e8714be673)
#### Thursday 2023-10-26 10:27:07 by Sebastian Berg

API: Allow comparisons with and between any python integers

This implements comparisons between NumPy integer arrays and arbitrary valued
Python integers when weak promotion is enabled.

To achieve this:
* I allow abstract DTypes (with small bug fixes) to register as loops (`ArrayMethods`).
  This is fine, you just need to take more care.
  It does muddy the waters between promotion and not a bit if the
  result DType would also be abstract.
  (For the specific case it doesn't, but in general it does.)
* A new `resolve_descriptors_raw` function, which does the same job as
  `resolve_descriptors` but I pass it this scalar argument
  (can be expanded, but starting small).
  * This only happens *when available*, so there are some niche paths were this cannot
    be used (`ufunc.at` and the explicit resolution function right now),
    we can deal with those by keeping the previous rules (things will just raise
    trying to convert).
  * The function also gets the actual `arrays.dtype` instances while I normally ensure that
    we pass in dtypes already cast to the correct DType class.
    (The reason is that we don't define how to cast the abstract DTypes as of now,
    and even if we did, it would not be what we need unless the dtype instance actually had
    the value information.)
* There are new loops added (for combinations!), which:
  * Use the new `resolve_descriptors_raw` (a single function dealing with everything)
  * Return the current legacy loop when that makes sense.
  * Return an always true/false loop when that makes sense.
  * To achieve this, they employ a hack/trick: `get_loop()` needs to know the value,
    but only `resolve_descriptors_raw()` does right now, so this is encoded on whether we use
    the `np.dtype("object")` singleton or a fresh instance!
    (Yes, probably ugly, but avoids channeling things to more places.)

Additionally, there is a promoter to say that Python integer comparisons can just use
`object` dtype (in theory weird if the input then wasn't a Python int,
but that is breaking promises).

---
## [TheDailySimile/PedalPonder](https://github.com/TheDailySimile/PedalPonder)@[0e09976e5a...](https://github.com/TheDailySimile/PedalPonder/commit/0e09976e5a299a87cc191338a4d998d5f5c83416)
#### Thursday 2023-10-26 10:51:50 by The Daily Simile

Update Ash : Next Term Phantom@Instrument Oriented Dissolution.html

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
Marc@scowl : "if i were you i would've been rather concerned about my self than my inclinations#..Marc..Yeah It's a matter of Skills Mr Santanore i very sorry that you came,second best..to the use of..,feel..surely you know my ideological guidelines#..Ash+Misty..yay i won! no i lost! well well still a draw!,..shuu..Result That Feeling,#,..Brock un..long,#,.."
Ash@shrug : "well as you insist i would have to choose a pokemon..to the crowd's..likin'....of a Grim prospective.."
Grimmsnarl@unhappy : "why do you irritate me hombre you can't even recognise what is to be battled and what is battling#.."
Ash@shrug : "well i though may be as you were inflecting your clingings using likin' may be you forgot to ask..seein' it.."
Grimmsnarl@giggle : "attacked!..
halt..oh Ketchum self shouts/racin' against whoose doubts?/then you Ketchum in dual bouts/try to defend your self by extendin' about/as you Ketchum use ego/to do yet never to see so/thus when you Ketchum want freedom/novel you think thoughts can discern..
thus Ketchum results never renews for you/yet i rejoice as me when you struggle to see me as you.."
Sakura@giggle : "through nerves of sustainin'/races alone constrainin'/upon question on meain'/lied answer as feelin'.."
Whole female crowd including Violet-Misty@giggle : "then to be or to see/lastly Phantom means i never me.."
Misty@giggle : "and because you're from the affordable shore you refuse to understand the psychoanalysis of the instrument of the elaborative shore..take that you feelin' crook nana#..Brock..Doubt-Clearance Obsession,#,..Misty un..long,#,.."
Brock@scowl : "i see thus that sickening Grimmsnarl was taken from the assortment of..form..cunning indeed Ketchum this game of pros on cons#..Sakura,Daisy,Violet,Lily,Blythe,Mahina..Playboy Raptures,#,..Ash un..long,#,.."
Ash@shrug : "before the BATTLE resumes Mr Santanore unlike Ms Santanore you already know my inclinations thus may be the reason why you despite not being a general trainer and yet to intervene in a interregional final without anyone complaining against your choice..is all because of your deep knowledge on my inclinations..on self help ain't it.."
Marc@scowl : "Saku lost because of purity of vision thus with her bunch was over the moon understanding instrument oriented dissolutions but purity is a counter indeed to your..analogy obsession#..The Meaning of Lie,#,..Ash un..long,#,..and hence i having recalled my practice of connections between non self and desires intervened#..Light upon Darkness,#,..Marc un..long,#,.."
Ash@shrug : "fair enough you refuse to submit to..desires for liberation from obviousness..thus this..joy of..Yiyui!.."
Referee@veryAngry : "ai ai you choose to associate fire to signify the volatility of self commitment to a chosen ego along with darkness of absolute witness i'll disqualify you ok.."
Marc@angry : "you lowlife don't create an intrigue of provability to your thoughts on own memorial knowledge ok this was only a counter to Defeat : Victory Lie#..Gary..who are you,Ash Ketchum Pokemon Master,ego sinister we see,me..you see only compeers..me thus indeed as a counter isn't it so..shh..it was included..
Phantom : The Meaning of Lie..
any noise in thoughtful chantin' of soul?,#,..Ash un..long,#,.."
Yiyui@giggle : "ei vision eh blur aim boo charred i or thy/or who see as this or i..i..
shh..shh..shh..shh..shuu..uu..uu..blast/or cue cue cue cue cue see why never past.."
Marc@scowl : "i see this is the generalization of..next term..unless i admit defeat and stop my self from venturing into it's randomness i will be deemed a phantom cunning indeed Ash..as Ash means i read in those sickening comics popularized by you..Ash : Next Term..Phantom,#,..Ash : Next Term Phantom,#,..Ash un..long,#,.."
[Brock@CoOrdinator,Dentarou@CoOrdinator Slate
Tracey@P.Doctor Skechit
Daisy@P.Doctor,Violet@CoOrdinator,Lily@Psychic-Dark,Misty@Ghost-Fairy]@Pebblefog,Mintale
....
[Marc@Psychic-Dark,Sakura@Local Santanore
Ingemar@P.Doctor,Mahina@CoOrdinator Iptil
Blythe@P.Doctor,Ayub@Ghost-Fairy Birch]@Duskneon,Paldea

{Juritared,Decolore}

Gary+Lily
Brock+Violet
Ingemar+Blythe
Ayub+Sakura
..
Dentarou+Mahina
Tracey+Daisy
Ash+Misty
Marc

Marc@scowl : "so all along it was a trick to deny the truth only to be the more..engaging#.."
Ayub@giggle : "practicing.. it's said devotion is best practiced as is infatuation in denial of freedom of self through detachment why#..The Milestones of Self-Sufficiency,#,..Ayub un..long,#,.."
Misty@giggle : "yeah yeah you tried to deny the subsuming of absolute as a self consumed way to assurance thus upon instrument agnostic apocalypse of thoughts had to admit defeat to..Victory : Defeat Try..nana.." 
Sakura@giggle,trying to dance with Ayub : "iii!..no your should dance with me again to that tune you questing yet method using b..#..The Milestones to Self-Dissolution,#,..Ayub+Sakura un..long,#,..that tune.. was so..um.."
Ayub@scowl,taking Sakura away : "non-intellectual yeah..i only waited to be able to earn..a penny.. physical not conscious thus..honourably..let's go#..Ayub+Sakura..Conclusive Witness Obsession,#,..Ash+Misty un..long#,.."
Lily@giggle : "ei Gary why the agnostic method is not active but potent only#..The Pivot Agnostics->Version->Lily flower,#,..Lily un..long,#,..
Gary@frown : "don't be so overhappy Lil when that curse appeared at Juritared it was a travesty and that lowlife still chose..my,MY hometown#..Gary..No Now Fire you oozin'/yet i alone choosin'/then is  no self you have?/as own as i do have..
yo! now fire blasts/potential with self clash/then where am i just seer's side/Lastly Ash thus means no more to find..
oh trapped in past of my/counterin' thus am free i/oh castle of soul now handle reason/action why ever fought potential's treason?..
Kutus Kutus Reason Bites/To be Me I races against my life..
Kutus Kutus Want Bites/Why I you never in my side?..
Kutus Kutus Seer Lies/Ash means seen nothing to find
ann..,how did that baby survive those cursed demons of the castle those dimensional riges of hellfire just how is it NO!..is that the Phantom,no it can't be no um..normal as i it must be Ash eho tamed that Phantom,um..wait wait is it what is called illusion that what never is,..this ambiguity is never going to be answered with the decolourised..shh..self counterin' the truth of self of hence..ain't it Gary rhyming with parry,nature says sorry bye#..Phantom : The Meaning of Lie,#,..Ash+Misty un..long,#,.."

---
## [m4rcyonstation/FargowiltasSouls](https://github.com/m4rcyonstation/FargowiltasSouls)@[86d8c82782...](https://github.com/m4rcyonstation/FargowiltasSouls/commit/86d8c82782b369c46f97d171967ff8622484413f)
#### Thursday 2023-10-26 11:31:45 by m4rcyonstation

adam new effect wah wah

adamantite damage buffed from 50%/33% to 70%/50% this might be a bit strong
homing weapons get down to 60/40 still a buff
spread increases while shooting

also fix mythril being a little BITCH and having "fargoplayer" instead of "modplayer" unlike EVERY OTHER FUCKING INSTANCE, INCLUDING IN THE SAME FUNCTION ASSHOLE anyway its fixed

(fix me being stupid and fucking up stuff FOR REAL #3

i hate how you can see me struggle as i merge stuff the wrong way and have to try to fix it all)

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[e014f5e257...](https://github.com/sourcegraph/sourcegraph/commit/e014f5e2573057a43ae61bf9ed8b68dba685a282)
#### Thursday 2023-10-26 12:12:15 by Felix Kling

Enable bazel for web-sveltekit and make it available in production builds (#55177)

## Bazel

It took me some time to figure out how to make it work. I don't claim that this is the best setup (because I don't really have an idea what I'm doing here), I just tried to get things working. The main issues had been around loading the generate `client/*` packages and importing `*.scss` files.

### Loading `@sourcegraph/*` packages

Unlike our other build tools, SvelteKit/vite load the application into Node for pre-rendering. This happens regardless whether pre-rendering/server-side-rendering is enabled or not (these settings live in the source code because they can be enabled/disabled per route).
Long story short I had to configure vite to also process any `@sourcegraph/*` packages in order to make them compatible with node.

You might wonder why that's not necessary when running vite directly in the repo? In the repo the `@sourcegraph/*` dependencies are all links to the corresponding `client/*` packages. Vite detects that and automatically treats them as "sources", not dependencies.

### SCSS files

Somewhat related to the previous point, the built `@sourcegraph/*` packages do not contain any source SCSS files, only the generated CSS files. So importing SCSS files via `@sourcegraph/.../....scss` doesn't work. Furthermore, the generate code in the packages themselves import SCSS files, which also doesn't work.

The "fix" for this is to rewrite any `*.scss` file imports to `*.css` file imports, but only inside those packages or only referencing files inside those packages. That's what we do in our `webpack.bazel.config.js` file as well.

However, for global styles we need the SCSS files. I added a new target for copying those to the sandbox.

---

Additionally this PR makes the following changes:

- Rearrange style imports to remove unnecessary duplication and reduce the number of callsites that import from `@sourcegraph/*` packages.
- Remove React integration with Notebooks and Insights. It was broken anyway at the moment and removing it reduces the number of dependencies and therefore points of failure.
- Added a new target to copy the image files used by the prototype into the sandbox.
- Disables gazelle for the sveltekit package for the time being. Type checking won't pass anyway because the code in the other client packages don't follow the same restrictions as `client/web-sveltekit`.
- Updated the main header and dev server to proxy requests for notebooks, code insights and user settings to sourcegraph.com.


## Production build integration

These changes make it possible to serve the SvelteKit version for search and repo pages when the `enable-sveltekit` feature flag is turned on.

I aimed to make as few changes to the existing routing and handler code as possible to 

- server the SvelteKit index page for search and repo routes
- make all other SvelteKit assets accessible via the `/.assets/` route

In a nutshell, this is how it works now:

- When building for development, the SvelteKit build process will output its files to `ui/assets/`, the same folder where webpack puts its files. To avoid conflicts with webpack generated files, all SvelteKit files are put in a subdirectory.
  - For production something similar happens except that bazel will copy all the files into a target directory
- When accessing a search or repo route, we check, just before the response is rendered, whether to render the SvelteKit version or the React version. The challenge here was that we use the same handler for a lot of routes. `sveltekit.go` maintains a separate list of routes for which the SvelteKit version is available. This way I only had to add a check to three handler functions. And of course the feature flag must be enabled for the user/instance.
- Because the SvelteKit files are stored in the same location as the webkit ones, serving those files via the `/.assets/` route "just works". Well, mostly. In order for the SvelteKit page to use the correct root-relative path I had to create a custom adapater, `sgAdapter`, which updates the URLs in the index page accordingly (I tried a lot of other approaches, some would have required changes to the assets handler... this was the more "contained" solution). 

Caveat: This is not ready to be officially tested:

- Navigating between the React and SvelteKit versions does not always work as expected. Because of client side routing, navigating to e.g. the search page from the React app will load the React version of the site. The client side code needs to be updated to enforce a server refresh. I'll look into that in a future PR.
- The SvelteKit version is relatively incomplete. Code intel, new search input, repo settings pages, etc are all missing. Most of this work is tracked in #55027. But before we spend more time getting things feature complete we want to do limited testing with the prototype in prod.
- I wasn't able to get SvelteKit rebuilding to work reliably with `sg start enterprise-bazel`. For now it only builds the files once at start so that they exist. I'll look into improving the developer experience when running the full server locally in the future. For now, running `sg start web-sveltekit-standalone` is good enough.
- Switching between the React and the SvelteKit version is definitely noticeable during development. I suspect to be faster in production (React is faster in production). Whether or not we go this route remains to be seen. Maybe we are embedding React pages into SvelteKit instead. At this point we just need to try how SvelteKit feels in production.
- The SvelteKit `index.html` page lacks many things that the React `app.html` file has (e.g. preview links, analytics, observeability, etc). These have to be added eventually, but those are not necessary either for this initial test.

---
## [beetlejuicetr/PsychonautStation](https://github.com/beetlejuicetr/PsychonautStation)@[2ab4fa3a92...](https://github.com/beetlejuicetr/PsychonautStation/commit/2ab4fa3a923a8d1930547d47110823aeed8163f4)
#### Thursday 2023-10-26 12:46:33 by carlarctg

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
## [beetlejuicetr/PsychonautStation](https://github.com/beetlejuicetr/PsychonautStation)@[9073290d8a...](https://github.com/beetlejuicetr/PsychonautStation/commit/9073290d8ac18476a5165c6df6dcf062b70c635a)
#### Thursday 2023-10-26 12:46:33 by ArcaneMusic

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
## [beetlejuicetr/PsychonautStation](https://github.com/beetlejuicetr/PsychonautStation)@[db8eca7bf3...](https://github.com/beetlejuicetr/PsychonautStation/commit/db8eca7bf3366a97163c0abd6574bee82bd38fd3)
#### Thursday 2023-10-26 12:46:33 by Ghom

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
## [ShigeakiAsai/mame](https://github.com/ShigeakiAsai/mame)@[18ce563d3f...](https://github.com/ShigeakiAsai/mame/commit/18ce563d3f21fd266e7d8dc22b6e19655d385db0)
#### Thursday 2023-10-26 12:48:24 by wilbertpol

msx1_flop.xml: Added 105 working items, and replaced one item. (#11511)

* Replaced Konami Game Collection 3: Shooting Series (Japan) with a better dump. [file-hunter]

New working software list items (msx1_flop.xml)
-------------------------------
10 Programas Serie Oro (Spain) [file-hunter]
20 Programas Serie Oro (Spain) [file-hunter]
747 400b Flight Simulator (Europe, cracked) [file-hunter]
Alfabet en Deelsom (Netherlands) [file-hunter]
Alien Panic (Spain) [file-hunter]
Andon (Japan, hacked) [file-hunter]
Duad-MSX (Japan) [file-hunter]
Engels + Procenten (Netherlands) [file-hunter]
Fracta (Brazil) [file-hunter]
Graphos III (Brazil) [file-hunter]
Gruta de Maquine (Brazil)
The Iron Gauntz (Japan, prototype) [file-hunter]
Konami Game Collection 1: Action Series (Japan, alt) [file-hunter]
Konami Game Collection 4: Sports Series 2 (Japan, alt) [file-hunter]
Lettergrijper + Geld (Netherlands) [file-hunter]
Manuscript (United Kingdom) [file-hunter]
MSX Compilation 5 (Netherlands) [file-hunter]
MSX PageMaker DeLuxe (Brazil) [file-hunter]
Music Creator (Netherlands) [file-hunter]
Professional Data Retrieve (Brazil) [file-hunter]
Professional Paint (Brazil) [file-hunter]
Professional Publisher (Brazil, cracked) [file-hunter]
Rekenen tot 20 + Optellen en aftrekken tot 100 + Taalbedrijf (Netherlands) [file-hunter]
SF Zone 1999 (Japan) [file-hunter]
Simulador Profesional de Tenis (Spain) [file-hunter]
Super Procole (Japan) [file-hunter]
Super Procole 2 (Japan) [file-hunter]
Super Procole 3 (Japan) [file-hunter]
Supersellers 1 (Netherlands) [file-hunter]
Twin Hammer (Korea) [file-hunter]
The Wood (Spain) [file-hunter]
Woordmaker en Cijferend Vermenigvuldigen (Netherlands) [file-hunter]
Word Plus (Brazil) [file-hunter]
Wordstore+ (Netherlands) [file-hunter]
Zen (United Kingdom) [file-hunter]
3D Maze [Chalky]
666 - Uma Aventura Macabra [file-hunter]
8192 Story Tower [NAGI-P SOFT]
Baruko [file-hunter]
Blinky's Scary School [file-hunter]
Bounce Mania [MSXdev]
Burner Burst [file-hunter]
Buster Mystery [file-hunter]
City (Japan) [file-hunter]
Defence (v1.3) [MSXdev]
Galaxy Zone [aburi6800]
Ghosts'n Goblins (v1.1.0) [file-hunter]
Hibernated 1 - This Place is Death [file-hunter]
Hibernated 1 - Eight Feet Under [file-hunter]
JUMPER [NAGI-P SOFT]
Kame Graphics [file-hunter]
Kill Mice [MSXdev]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
Las Aventuras de Rudolphine Rur (Spanish, xmessage) [Dwalin]
Last War [NAGI-P SOFT]
Last War II [NAGI-P SOFT]
Logic (Russia) [file-hunter]
Mars [NAGI-P SOFT]
Mars II [NAGI-P SOFT]
May The Force Be With You [Cobinee]
Maze Chase [JLTurSan]
Micro Rocketz [MSXdev]
Mood Land [file-hunter]
Muhonmourn 3 (v1.1) [MSXdev]
Muhonmourn 3 (v1.1, with Ninja Tap support) [file-hunter]
Muhonmourn 3 (v1.0) [file-hunter]
Nibbles [file-hunter]
Oceano [file-hunter]
Paint-it (rev2) [file-hunter]
Paint-it (rev1) [file-hunter]
Paint-it [file-hunter]
Palhada City (Brazil) [file-hunter]
Penguin Catcher (v1.1) [MSXdev]
Penguin Catcher (v1.0) [file-hunter]
Pyramid Quest [Crappysoft]
Raftoid [PlattySoft]
Roger Dice (Spain) [oniric-factor]
Search for Mum (Netherlands) [file-hunter]
Sim City [file-hunter]
Storm Rescue [Concurso MSX-BASIC]
Stripgirl [file-hunter]
SubCommander (v1.02) [MSXdev]
SubCommander (older) [file-hunter]
Super Adventure [file-hunter]
The Tower of Gold [MSXdev]
UZIX (v1.0.0) [UZIX]
Wash Man (v2.8) [MSXdev]
Wash Man (v1.9) [file-hunter]
Wash Man (v1.5) [file-hunter]
Wash Man (v1.3) [file-hunter]
Wash Man (v1.2) [file-hunter]
Wash Man (v1.1) [file-hunter]
Wash Man (v1.0) [file-hunter]
Wired Shooting [Cobinee]
MSXMAS Demo [file-hunter]
Xadrama [file-hunter]
Xarchon [file-hunter]
XOR [Chalky]
XOR (older) [file-hunter]
Yellow Submarin [file-hunter]
Yobai [file-hunter]
Zero Gravity [file-hunter]
The zoBITRONics Inc [Hannu Töyrylä]
Zone TNT [MSXdev]
La Abadia del Crimen (Spain, alt) [file-hunter]

---
## [Yrzhe/yrzhe](https://github.com/Yrzhe/yrzhe)@[b44f30ec69...](https://github.com/Yrzhe/yrzhe/commit/b44f30ec69ad8f326404952ae5ca879d7eb463f3)
#### Thursday 2023-10-26 12:53:08 by Renzhe Yu

Rename 在朋友们的帮助下社交亲密度对情绪调节相关大脑活动的影响.html to With a little help from my friends: The effect of social proximity on emotion regulation-related brain activity.html

---
## [kevinsung/documentation](https://github.com/kevinsung/documentation)@[6a7124e86c...](https://github.com/kevinsung/documentation/commit/6a7124e86cc8621826a4d6397110db903c7b2635)
#### Thursday 2023-10-26 12:53:28 by Eric Arellano

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
## [Sentious/matrix-js-sdk](https://github.com/Sentious/matrix-js-sdk)@[31f38550e3...](https://github.com/Sentious/matrix-js-sdk/commit/31f38550e3fb0ed7312e52b896985477b22f01c3)
#### Thursday 2023-10-26 12:58:17 by David Baker

Refactor & make base64 functions browser-safe

We had two identical sets of base64 functions in the js-sdk, both
using Buffer which isn't really available in the browser unless you're
using an old webpack (ie. what element-web uses). This PR:

 * Takes the crypto base64 file and moves it out of crypto (because
   we use base64 for much more than just crypto)
 * Makes them work in a browser without the Buffer global
 * Removes the other base64 functions
 * Changes everything to use the new common ones
 * Adds a comment explaining why the function is kinda ugly and how
   soul destroyingly awful the JS ecosystem is.
 * Runs the tests with both impls
 * Changes the test to not just test the decoder against the encoder
 * Adds explicit support & tests for (decoding) base64Url (I'll add an
   encode method later, no need for that to go in this PR too).

---
## [ashutoshchettri/android_kernel_xiaomi_alioth](https://github.com/ashutoshchettri/android_kernel_xiaomi_alioth)@[eabfb54e48...](https://github.com/ashutoshchettri/android_kernel_xiaomi_alioth/commit/eabfb54e48d66557e0e44973eb58ebeac8396a2c)
#### Thursday 2023-10-26 15:17:55 by Peter Zijlstra

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
Signed-off-by: NotZeetaa <rodrigo2005contente@gmail.com>

---
## [pachyderm/pachyderm](https://github.com/pachyderm/pachyderm)@[eaec20a639...](https://github.com/pachyderm/pachyderm/commit/eaec20a639587f6344de9db92549d26fcdef2752)
#### Thursday 2023-10-26 15:49:08 by Jonathan Rockway

Dynamic k8s API for starlark scripts (#9350)

This adds a Kubernetes library for starlark scripts. It uses the dynamic
k8s client, which is the least horrible option. (The other options were
to use reflection against the static client, or generate a starlark
client from the OpenAPI specs.) I didn't use reflection because the
static client can't access dynamic resources; say we want to dump Istio
configs, you can't do that with the static client. I didn't do the
codegen because I thought it would take too long, but in the end not
doing it took too long. (We'd have to ship the compiler, though, for the
same Istio reason above.) Dynamic is the least bad, but it's not great.

It's actually amazing how bad the Kubernetes API is. I used to think
they had a good reason for not using protos + grpc, but nope, they did
not. Instead they just made a pretty bad implementation of grpc (oh but
with versions!) Looking forward to version 2.0.

The dynamic client is horrible in many regards. We have to figure out
that Kubernetes has a thing called "pods" by querying the server. That's
literally not compiled into the client anywhere!!! These methods do not
take contexts (and the bug for this is closed with "who cares why would
that need a context?"), so creating a k8s starlark client can take
unbounded time. Unfortunate, but actually very difficult to fix.

Kubernetes also has the concept of "subresources", which pod logs are
one of. The dynamic client has no clue how to handle these; it has code
to handle them, but it gets it totally wrong.

The library is designed to keep charging along in case of errors; error
objects have the same API surface as the result objects, and when the
debug dumper sees them it writes an error file instead of the requested
file. This is necessary because starlark errors are fatal; the script
cannot continue when there's an error.

To get a taste of the API, here's a script that dumps pipeline RCs as
JSON, and all associated pods:

```python
def dump_rcs():
    rcs = k8s.replicationcontrollers.list(labels = {"suite": "pachyderm", "app": "pipeline"})
    for rc in rcs:
        name = rc["metadata"]["name"]
        dump("%s/rc.json" % name, json.encode(rc))
        pods = k8s.pods.list(labels = rc["spec"]["selector"])
        for pod in pods:
            podname = pod["metadata"]["name"]
            dump("%s/pod-%s.json" % (name, podname), json.encode(pod))

if "replicationcontrollers" in dir(k8s) and "pods" in dir(k8s):
    dump_rcs()
```

You can also open up a shell and write something like `pods = k8s.pods`
and `print(pods)` or `dir(pods)` to see the functions available.

Finally, if you are wondering about the starlark.go change that sets
`ReassignGlobals` to true... it turns out no code reads the other fields
in that struct; if it's false, then you can't have top-level for loops
or if statements 😂. We are totally OK with those things, so we enable
them here.

---
## [Shaharyar-54/Build-Con](https://github.com/Shaharyar-54/Build-Con)@[1d3e180ef8...](https://github.com/Shaharyar-54/Build-Con/commit/1d3e180ef824fffee0a036efb7b76eda36fa14b5)
#### Thursday 2023-10-26 16:07:57 by Shaharyar Nadeem

Add files via upload

🏠 Home Section: Our Home section is your gateway to an extensive world of real estate opportunities. We've meticulously curated three distinct pages, each designed to cater to various property needs. Whether you're searching for the perfect home, a thriving commercial space, or an investment opportunity, we've got you covered. It's all about finding the property that suits your unique vision and requirements.

🏢 About Section: Here, we offer an intimate look into Build Con's identity and mission. We're not just about properties; we're about crafting dreams. Discover how our agency's passion and dedication have led us to become a trusted name in the real estate industry. We're more than just a company; we're a community of individuals committed to transforming your real estate aspirations into reality.

🛠️ Services Section: At Build Con, our services are founded on three pillars: "Best Quality," "Sustainability," and "Integrity." Each project we take on reflects our unwavering commitment to delivering exceptional quality. We prioritize sustainability to ensure a brighter, greener future for our clients. Above all, integrity is our guiding principle, ensuring honest and transparent interactions at every step of the journey. It's not just about property; it's about building trust and long-lasting relationships.

📸 Portfolio Section: Our portfolio is a testament to our expertise and success. It's not just a showcase of properties; it's a visual journey through our achievements. We take immense pride in presenting the properties we've had the privilege of working on. From breathtaking homes to lucrative commercial ventures, each project reflects our dedication to excellence and client satisfaction.

👥 Team Section: Behind the scenes at Build Con are the talented individuals who make the magic happen. Meet our team, the creative and dedicated professionals responsible for bringing your real estate dreams to life. Their expertise, enthusiasm, and unwavering commitment to your goals ensure a seamless and rewarding real estate experience.

📞 Contact Section: We've made it effortless for you to reach out and connect with us. Our user-friendly contact form is your direct line to our team. If you have questions, need assistance, or are ready to take the next step in your real estate journey, simply complete the form and hit "Submit." We're here to assist you every step of the way.

---
## [langchain-ai/langchain](https://github.com/langchain-ai/langchain)@[dff24285ea...](https://github.com/langchain-ai/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Thursday 2023-10-26 16:42:20 by Nikhil Jha

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
## [SlippingGittys-Discord-Themes/SlideToUnlock](https://github.com/SlippingGittys-Discord-Themes/SlideToUnlock)@[e42e3513ac...](https://github.com/SlippingGittys-Discord-Themes/SlideToUnlock/commit/e42e3513ac4866f9b7369340f2016d9fa5c8e756)
#### Thursday 2023-10-26 16:46:16 by Vozer

"thanks discord"-- and thank you

SlideToUnlock was the first Discord theme I created, and as a result has led to nearly 3 years of some of the greatest times I've ever had online. I was in a very dark place back in 2021, and having the friends (some I'd go as far as to call brothers and sisters) I made really pulled me out of it. 

I look back at this theme and see all of the glaring issues with it, comparing it to some of the new and arguably better designed themes which I have made today. While I would much rather not focus any of my attention on it Slide so that I can continue to work on much more meticulous projects, I can still appreciate what this theme gave me. 

Look out for Swipe Up To Unlock, a new Discord theme coming soon! ... Just kidding, that's never going to exist.

thanks https://syndishanx.github.io/Website/Update_Classes.html

---
## [JarRaid/HorrorGame](https://github.com/JarRaid/HorrorGame)@[227bec7b9d...](https://github.com/JarRaid/HorrorGame/commit/227bec7b9d91f1256063442bbff6d438a2877c60)
#### Thursday 2023-10-26 16:50:28 by salataa1

Chandelier and window 4 update

Added other andrew's shitty ass chandelier that i had to basically redo the unwrap for. made it as pretty as I could. If he submits one in his push for the merge, use this one instead. also changed the alpha map on the top down view of the church window to reflect the nursery location we're going with

---
## [instructure/canvas-lms](https://github.com/instructure/canvas-lms)@[63f603a397...](https://github.com/instructure/canvas-lms/commit/63f603a39787f3f206c9082762bc54934d55fc6d)
#### Thursday 2023-10-26 17:27:53 by Ryan Hawkins

Remove old non-InstUI tool config forms

why:
- we feature flagged these, as it was a user-facing UI change. However,
  it made the code atrociously ugly and resulted in duplicated tests. We
  have turned the flag on and no one got upset, so all is well. The
  changes were very subtle anyways.
- Also, speeds up the remaining tests significantly just by replacing
  userEvent.type with userEvent.paste. As in, they take half as long
  now. Still way slower than I would like, but it'll do for now.

closes INTEROP-8132

closes FOO-3829

test-plan:
- checkout this commit and make sure your front-end assets are rebuilt.
- go to any spot the tool configuration forms can be found, such as on
  the course settings page, and make sure each of the forms loads and
  you can actually use them. We thoroughly tested the forms back when we
  first added them, so you don't have to do that much.
- make sure your screenreader can advance through the forms in a
  sensible manner.

Change-Id: Ic9979e3dd2a83d9826901a2d59ea0d3e78426c1a
Reviewed-on: https://gerrit.instructure.com/c/canvas-lms/+/330905
Tested-by: Service Cloud Jenkins <svc.cloudjenkins@instructure.com>
Reviewed-by: Tucker Mcknight <tmcknight@instructure.com>
QA-Review: Tucker Mcknight <tmcknight@instructure.com>
Product-Review: Ryan Hawkins <ryan.hawkins@instructure.com>

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[404a7cd290...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/404a7cd29063f00078f85d8171612085a611b271)
#### Thursday 2023-10-26 17:44:29 by san7890

Fixes Space Dragon Attacking (#78964)

Fixes #78953

## About The Pull Request

Basically the gist is that Space Dragon's special attack code was on
`AttackingTarget()` rather than whatever the hell simple animals
controlled by clients use (I didn't bother enough to look into the chain
to remember this). This was the complete wrong proc to use, and it NEVER
got executed. Anyways, we just hook into the signal for whatever the
simple animal proc is as well as clean up all the code, make everything
pretty, and most importantly:

MAKE THE DAMN CODE WORK
## Why It's Good For The Game

Either someone did not test their code at all, or some weird esoteric
change in the attack chain changed this somehow? I'm not sure when or
why this happened but it is guaranteed to be fixed now.

The code cleanup and tinkering I did means that it's gonna be about 10%
easier to port this over to a basic mob eventually (not doing a full
refactor when this shit is this broken, the code added here is modular
enough to the point where it's plug-n-play).
## Changelog
:cl:
fix: Space Dragons can now, once again, tear down walls and eat corpses.
They also have regained their special damage modifier when attacking
mechs.
/:cl:

---
## [PhilipVinc/netket](https://github.com/PhilipVinc/netket)@[34bd4adde1...](https://github.com/PhilipVinc/netket/commit/34bd4adde13df35b65f4f055a750dda242fdfa20)
#### Thursday 2023-10-26 17:50:22 by Filippo Vicentini

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
## [AnywayFarus/Fluffy-STG](https://github.com/AnywayFarus/Fluffy-STG)@[a6301c9445...](https://github.com/AnywayFarus/Fluffy-STG/commit/a6301c9445f474b3ad4ffae6ad66f51c5286a6a5)
#### Thursday 2023-10-26 17:53:26 by SkyratBot

Supermatter Delamination Balance Changes (Real) [MDB IGNORE] (#23670)

* Supermatter Delamination Balance Changes (Real) (#77996)

## About The Pull Request

lord forgive me I fucked up the merge conflict

The supermatter delamination countdown timer (how long it takes to go
boom-boom after hitting 0 integrity) has been lowered from 30 seconds to
13 seconds.
Removing a sliver from the supermatter, the traitor objective, will
further lower that down to 3 seconds.
Changes the wording on the mood effects from the supermatter
delaminating slightly.
The crystal uses SPAN_COMMAND on its final countdown, which means it
talk bigger.

## Why It's Good For The Game

Currently I feel that the supermatter delamination countdown overstays
its welcome. Ideally it provides tension to get the hell out, or perhaps
to make a risky last second play to try and save the supermatter.
However right now its at 30 seconds, which gives no danger of staying in
engineering right up to integrity 0, and keeps the tension at a high
note for too long, almost to the point of awkwardness. 13 seconds is a
good balance between get-the-fuck-out while still giving some leeway for
engineers to escape and crewmembers to jump in lockers, and feels quick
enough to give that danger that the supermatter should provide.
Additionally, removing a sliver from the supermatter lowers the cooldown
to 3 seconds. Right now this is one of the harder tasks a traitor can be
tasked with, while giving relatively little payoff sabatoge-wise. To the
point where I have seen engineers just let the traitor do it, as the
debuff it gives to the supermatter is minor. Now it makes the
supermatter delaminate almost immediately after hitting 0 integrity,
which means it will likely catch some engineers in the blast if a
traitor did it stealthy. This also makes it more risky to try and fix a
delamination if the engineering/security team did not stop the sliver
from being removed. All meaning succeeding at this task should be more
rewarding and damaging.
Finally the mood descriptions for the mood effects you get when a
supermatter delaminates have been changed. Currently they are pretty
gamey, and represent what the player might be thinking more than their
character. Additionally they were not very descriptive of where they
came from, which could be confusing.

## Changelog

:cl: Seven
balance: The supermatter delamination countdown has been lowered from 30
to 13 seconds
balance: Removing a sliver from the supermatter further lowers that down
to 3 seconds
balance: The supermatter crystal uses bigger text on its final countdown
spellcheck: Some supermatter delamination related mood descriptions have
been edited to explain the mood effect better
/:cl:

---------

Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@ users.noreply.github.com>

* Supermatter Delamination Balance Changes (Real)

* Update scram.dm

---------

Co-authored-by: Lufferly <40921881+Lufferly@users.noreply.github.com>
Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@ users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [TheDailySimile/ReticenceVat](https://github.com/TheDailySimile/ReticenceVat)@[578725b7ec...](https://github.com/TheDailySimile/ReticenceVat/commit/578725b7ec081a519170619e42c68fea5b4b4902)
#### Thursday 2023-10-26 18:11:33 by The Daily Simile

Create Misty : If Assumptions Inquired On The Meaning Of Lie.html

[Brock@Ghost-Fairy,Dentarou@CoOrdinator Slate
Tracey@P.Doctor Skechit
Daisy@P.Doctor,Violet@CoOrdinator,Lily@CoOrdinator,Misty@Ghost-Fairy Waterflower]@Pebblefog,Mintale
..
[Gary@CoOrdinator Oak
Ingemar@P.Doctor,Marc@HoF Iptil
Blythe@P.Doctor,Mahina@Local(8-8) Ortiz]@Duskneon,Paldea

Sheena@P.Agent McShin

Gary+Lily
Tracey+Daisy
Marc+Misty
..
Brock+Violet
Ingemar+Blythe
Dentarou+Mahina

Alola,Decolore
Johto,Fiorre

Mintale,Kalos
Paldea,Galar

Kitakami,Lental
Unova,Tundra

Hisui,Hoenn
Ransei,Sinnoh

20(6)-22(2)@Mintale(W/D-W/D)[Marc&Mahina,Brock&Misty]
22(9)-24(5)@Unova(W/D-W/D)
25(0)-26(8)@Hisui(W/D-W/D)#BoD
->27(0)-27(8)@TeamSic[Marc&Brock]
28(0)-29(8)@Johto(W/D-W/D)
30(3)-31(11)@Kalos(W/D-W/D)[Marc&Mahina]
32(6)-34(2)@Fiorre(W/D-W/D)#GoC
34(9)-36(5)@Hoenn(W/D-W/D)
37(0)-38(8)@Tundra(W/D-W/D)
39(3)-40(11)@Galar(W/D-W/D)#CoE
41(6)-43(2)@Decolore(W/D-W/D)
43(9)-45(5)@Sinnoh(W/D-W/D)
46(0)-47(8)@Lental(W/D-W/D)#PoL
48(3)-49(11)@Paldea(W/D-W/D)
50(6)-52(2)@Kitakami(W/D-W/D)
52(9)-54(5)@Ransei(W/D-W/D)#HoF
54(9)-[55(5)@TeamLegend
55(9)-57(5)@Alola


Marc@laughing : "well after Ransei i had nothing left to do in my travelling career Mihi had same results and straightaway said after we both get into Hall of Fame that now my journey having completed i'll mingle with Dentie's method of seclusion as that relativity nuzzling b.. did with my method of exclusion for like 25 years#..The Boomerang of Exact Normalcy,#,..Dentarou+Mahina un..long,#,..so anyhow i was a bit uneasy because of my confusion as to why i shouldn't travel Alola#..and given our background i could travel alone but it wouldn't be that much fun afterall after like 34 years of travelling with my family#..Mist was only unhappy this time cause she wasn't in general training#..Baby Gyarados,#,..Misty laughs..lot,#,..so i told Sheenie after like pondering over everything that well i really don't want to go but i'll have an extended holiday there visit a few gyms Mist is also tired after 24 years of gym leading..without that feeling#..so said 3 months will travel around that's all after 3 month break..Sheenie said ofcourse you absolutely right but just 24 years late that's all#..but that's for memories only for existence far far heinous things were happening most unfortunate for Sheenie only as the very next morning unfolded#..Sheena..The Meaing of Lie,all un..long,#,.."
TeamLegend@frown : "this is the place of the erstwhile Juritared Volcano Castle,Juritared Town,Alola..and your parents Ms McShin were the last victims of this place mythical creatures,SPIRITS to be precise used to stroll here when your parents trying to chase after some fugitives being from Nephrosum Region Secret Services tried to chase them here..they never survived whatever they faced as we certainly know#..but your parents after a day that is spending an unfortunate night here were running away through this slope maniacally as if they had seen..something.. downwards a few of their mates were awaiting with you about to celebrate being aware of their last signal never from the Castle complex anyhow but as they were befuddle you all were ambushed and then a fight took place then you then being 3 infact that being your birthday ran away to that castle followed by the ambushers who had eliminated all your defenders chased you there..and all logical equations end here as a 3 year old kid moved away faster than..A Reshiram#..herd#..who were..influenced#..then you being the last evidence some horrific moron among them decided to charge into the abandoned haunted castle on the tip of a volcano..with a couple of Incineroars#..may they find solace Ms McShin how did you survive the most dreadful volcanic eruption..ever#.."
Sheena@struggling to flee,exasperated : "you lowlifes my bro will never fall into your traps..,
TeamLegend@straight : "be specific Ms McShin..you're a pious person thus we understanding your psychology have carried your objects of worships..with due veneration.."
Sheena@crying out : "you..you demons leave that..no.."
TeamLegend@crude : "it's only a false rosary Ms McShin..we love to negotiate more#..(surprised)..no..(alarmed)..no how.."
Sheena@exasperated : "you..you just destroyed my devotional method you..i wish i could curse you but i know it's only my failure not to expand self.."
Ei then then nuzzle caution wind/of consciousness's whim/coincidence of spiritual/now faced as actual..
Seer why i never i/yet i use my as if my/tell what's actual/why happiness never virtual..
Lastly Phantom oh My/Ash means seer bye..
Sheena@frown : "i want to be as scared as them as seemingly dead but somehow i feel you know about that rosary and my practices..just as..ME..why#..Sheena..The Meaning of Lie,#,.."
Self too I/Thus so My/Quest so If/Poise..Ever Clicks..
The Least..shh..aspirin'..greetin's compeer..as you escape self do memorize to understand non selves as I : In Case A Meaning to Apply..shh..Phantom : All but I..
Marc@scowl : "so Team Legend has someone named Ash Ketchum,Pokeon Master?.."
Sheena@frown : "that's the only problem.."
Misty@angry : "shut up you poise indicating yet consumption using b.. my Marc ain't going anywhere sans me#..whoose Phantom of I hum#.."
Misty : If Assumptions Inquired
Misty@scowl : "who thought this nonsensical wordplay for me..um..but it is a lie too.."
Marc+Misty@timid : "No! It's Phantom!.."
Sheena@scowl : "the meaning of lie..sly..extremely sly#..Phantom : The Meaning of Lie,#,..all un..long,#,.."

---
## [AugustUu/Aggroculture2](https://github.com/AugustUu/Aggroculture2)@[0766ab98b8...](https://github.com/AugustUu/Aggroculture2/commit/0766ab98b878a8c8c9a7b1fc0fdef15ab66b5e9a)
#### Thursday 2023-10-26 18:19:26 by Rnguyen2019

I added tomato

Imagine that you’re a horticulturalist with limited land and space to grow. And imagine you are what they call an original thinker, unusually gifted in lateral thinking. Well, one day you’re minding your own business, eating your mashed potatoes with a tomato salad on the side, and you get to think... what if you could grow potatoes and tomatoes on one plant? That would give you a double crop and you could produce twice as much food on that small plot of land that you own? If this was a cartoon, a flashing light bulb would appear above your head!

You grow a huge wild beard, and start digging up the bodies of deceased tomatoes and potatoes. You build a giant machine that uses enormous amounts of electricity and you start to laugh like a maniac as you create your own vegetable-Frankenstein.

It might sound crazy, but it is not as unrealistic as it seems. Okay, we can leave out the Frankenstein scene, and actually no genetic modification is necessary either. That’s because tomatoes and potatoes are actually related to each other. They are both members of the nightshade family just like sweet peppers, chilli peppers, eggplants, tomatillos, tamarios, pepinos, pimentos, paprika, and cayenne peppers.

---
## [thulasiram1234/Pasture-dream-garden](https://github.com/thulasiram1234/Pasture-dream-garden)@[7ef08363ee...](https://github.com/thulasiram1234/Pasture-dream-garden/commit/7ef08363ee2677fa2aafb8cc7a9c8f872cd85a68)
#### Thursday 2023-10-26 18:50:03 by thulasiram1234

Add files via upload

Key Features:
      1.Home Page: A welcoming introduction to your dream garden with a captivating image.
      2.About Page: Share your inspiration and vision for the garden.
      3.Photo Gallery: Showcase high-quality images of the garden, including plants, landscaping, and design elements.
      4.Plant Database: Create a database of the plants you'd like in your dream garden. Include photos, care instructions, and planting tips.Interactive Garden Planner: If you 
         want an advanced feature, consider an interactive garden planner tool that allows visitors to virtually design their own dream garden based on your inspiration.
      5.Blog: Regularly update a blog with gardening tips, progress reports, and personal experiences related to your dream garden.
      6.Contact Page: Allow visitors to get in touch with you for questions, comments, or collaborations.
Design and Visuals:
      Choose a soothing color scheme that complements the garden theme.Use high-quality images and possibly videos to showcase your dream garden.Ensure the website is mobile-friendly for a seamless user experience.

---
## [heyujjwal/Ahead-app-ug](https://github.com/heyujjwal/Ahead-app-ug)@[89a2d72d50...](https://github.com/heyujjwal/Ahead-app-ug/commit/89a2d72d50cbfcca988f711215a518ce71168ef0)
#### Thursday 2023-10-26 18:52:31 by Ujjwal Gupta

Update of README.md

Description:
The Ahead App is a groundbreaking mobile application that empowers individuals to master their emotions and enhance their emotional intelligence (EQ). This GitHub repository contains the code and resources for the Ahead App, which offers science-driven, bite-sized tools to boost EQ, ultimately leading to more fulfilling personal and professional lives.

Features:

Personalized Emotional Intelligence Coaching
Anonymous Social Skills Rating
User Privacy Assurance
Job Opportunities
Contact Information
Getting Started:
To get started with the Ahead App, you can clone this repository and follow the installation and setup instructions provided in the documentation.

Contributing:
We welcome contributions from the open-source community. Please check our contribution guidelines and code of conduct for more details on how to contribute to this project.

License:
The Ahead App is protected by copyright. All rights are reserved to Ahead App. For licensing details, please refer to the LICENSE file.

Contact:
For inquiries or support, you can reach out to us at hi@ahead-app.com.

Download the App:
You can download the Ahead App from the Apple Store to start your journey toward mastering emotional intelligence and leading a more fulfilling life.

---
## [Ayushomega14/Text-Based-Adventure-Game-with-GUI-database-using-PYTHON](https://github.com/Ayushomega14/Text-Based-Adventure-Game-with-GUI-database-using-PYTHON)@[6438dbce9c...](https://github.com/Ayushomega14/Text-Based-Adventure-Game-with-GUI-database-using-PYTHON/commit/6438dbce9c6533b412b15ceb70fb30ec06046dcf)
#### Thursday 2023-10-26 18:55:46 by Ayushomega14

python code for game

This Python project is an immersive text-based adventure game with a graphical user interface (GUI) created using Tkinter. It offers a thrilling gaming experience by seamlessly integrating with a MySQL database to manage characters, monsters, inventory items, and health items.

Key Features:

Character Creation and Selection: Players can create their own character by entering a name and choose from a pre-defined list of characters fetched from a MySQL database. Each character has unique abilities.

Inventory Management: The game provides a user-friendly inventory management system. Players can view and organize their character's inventory, which includes weapons, shields, and other items. Inventory items are stored in the database, allowing for dynamic gameplay.

Monster Encounters: To keep players engaged, the game features randomized monster encounters. Players must strategize and engage in real-time combat with monsters. Each battle is unpredictable and challenging.

Room Exploration: The game offers a diverse world with different settings. Players can explore various rooms, each with its own vivid description, creating an immersive environment.

Health Management: Characters have a health bar, and players can restore health using health items found in the game. Health items are associated with characters and stored in the database.

GUI Interface: The graphical user interface (GUI) is powered by Tkinter, ensuring an engaging and user-friendly experience for players.

Dynamic Gameplay: The game keeps players on their toes with dynamic gameplay, random encounters, and real-time combat mechanics. Strategy is key to surviving the adventure.

Extensible Database Integration: The code is designed to integrate with a MySQL database, making it easy to add new characters, monsters, inventory items, and health items as your game evolves.

This repository serves as a valuable resource for game developers, Python enthusiasts, and those interested in database integration within gaming applications. You can use this code as a foundation for your own text-based adventure games or learn from its integration of Python, Tkinter, and MySQL for GUI-driven gaming experiences.

Feel free to explore, modify, and enhance this code to create your own captivating text-based adventure games or use it as a reference for similar projects. Whether you're a gamer or a developer, this repository offers an exciting journey into the world of interactive storytelling.

---
## [VickiMorris/BeeStation-Hornet](https://github.com/VickiMorris/BeeStation-Hornet)@[c7c02f65fb...](https://github.com/VickiMorris/BeeStation-Hornet/commit/c7c02f65fbb0baa3332551fbd04cce308abfa077)
#### Thursday 2023-10-26 19:01:40 by VickiMorris

fuck my stupid baka life

Adds glass-pack improv shells (lower damage, can embed though)
Adds improvised 9mm (same damage, high variance in accuracy)
Lowers Improv shell pellets, variance, damage. Adds AP & increases minimum range
Adds so many revolver sprites (To show open/closed cylinder)

---
## [AsifAli78/Google-Maps-Data-Scrapper](https://github.com/AsifAli78/Google-Maps-Data-Scrapper)@[7b5a644f59...](https://github.com/AsifAli78/Google-Maps-Data-Scrapper/commit/7b5a644f59002fa55a9715b5b5c8e0f929aebff7)
#### Thursday 2023-10-26 19:14:02 by Asif Ali

Add files via upload

🌟 Get 120 Potential Customers in 2.5 Minutes! 🤖

Hola! 🌟

I am Google Maps Scraper, created to help you find new customers and grow your sales. 🚀

Why Scrape Google Maps, you may ask? Here's why it's the perfect ground for hunting B2B customers:

📞 Direct Access to Phone Numbers: Connect with potential clients directly, drastically reducing the time it takes to seal a deal.

🌟 Target the Cream of the Crop: Target rich business owners based on their reviews, and supercharge your sales.

🎯 Tailored Pitching: With access to categories and websites, you can customize your pitch to cater to specific businesses and maximize your sales potential.

Countless entrepreneurs have achieved remarkable success by prospecting leads from Google Maps, and now it's your turn!

Let's delve into some of my remarkable features that entrepreneurs love:

💪 Rapid Lead Generation: I can scrape a whopping 1200 Google Map Leads in just 25 minutes, flooding you with potential sales prospects.

🚀 Effortless Multi-Query Scraping: Easily scrape multiple queries in one go, saving you valuable time and effort.

🌐 Unlimited Query Potential: There's no limit to the number of queries you can scrape, ensuring you never run out of leads.

In the next 5 minutes, you'll witness the magic as I extract 120 Leads from Google Maps for you, opening up a world of opportunities.

Let's get started generating Google Maps Leads by following these simple steps:

1️⃣ Clone the Magic 🧙‍♀️:

git clone https://github.com/omkarcloud/google-maps-scraper
cd google-maps-scraper
2️⃣ Install Dependencies 📦:

python -m pip install -r requirements.txt
3️⃣ Let the Rain of Google Map Leads Begin 😎:

python main.py

🤔 FAQs
❓ I want to scrape search results for a specific search query. How can I do that?
A: Open the file src/config.py and update the keyword with your desired search query.

For example, if you want to scrape leads about Digital Marketers in Kathmandu 🇳🇵, modify the code as follows:

queries = [
    {
        "keyword": "digital marketers in kathmandu",
    },
]
Note: You will be able to scrape up to 120 leads per search due to Google's scrolling limitation. Technically, there is no way possible to bypass this limitation.

❓ Can I scrape more than one query using this script?
A: Easy! Open src/config.py and add as many queries as you like.

For example, if you want to scrape restaurants in both Delhi 😎 and Bangalore 👨‍💻, use the following code:

queries = [
    {
        "keyword": "restaurants in delhi",
    },
    {
        "keyword": "restaurants in bangalore",
    }
]
❓ I want to scrape only the first 5 results. How can I do that?
Absolutely! Open src/config.py and modify the max_results parameter.

For example, if you want to scrape the first 5 restaurants in Bangalore, use the following code:

queries = [
    {
        "keyword": "restaurants in Bangalore",
        "max_results": 5,
    }
]
❓ How to Scrape Additional Information like Website, Phone, Geo Coordinates, Price Range?
You may upgrade to the Pro Version of the Google Maps Scraper to scrape additional data points, like:

🌐 Website
📞 Phone Numbers
🌍 Geo Coordinates
💰 Price Range
And 26 more data points like Owner details, Photos, About Section, and many more!

---
## [veggiemike/openrvdas](https://github.com/veggiemike/openrvdas)@[73b330a195...](https://github.com/veggiemike/openrvdas/commit/73b330a1958e8a1fa940ca8743cbdf9c9fd7d002)
#### Thursday 2023-10-26 19:47:55 by Michael D Labriola

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
## [JFranze7/JFranze7](https://github.com/JFranze7/JFranze7)@[4c035e2111...](https://github.com/JFranze7/JFranze7/commit/4c035e2111ff75444167b073da82ad74b22ac199)
#### Thursday 2023-10-26 20:02:59 by Jared

Update README.md

 I've always been a huge fan of technology. After 8 years of technical recruiting I decided it was time to get my hands dirty and work with the technology I've talked with candidates about for so long. I've been tinkering with computers since the early days of wifi when I'd change my parents wifi name to "JaredRulez" as a kid. I'm excited about this new chapter of life and all the cool tech there is to learn.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[e120ab795b...](https://github.com/cmss13-devs/cmss13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Thursday 2023-10-26 20:19:16 by fira

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
## [nafmo/git-gui-l10n-sv](https://github.com/nafmo/git-gui-l10n-sv)@[8f23432b38...](https://github.com/nafmo/git-gui-l10n-sv/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Thursday 2023-10-26 20:34:05 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [Towelstation13/towelstation13](https://github.com/Towelstation13/towelstation13)@[94bac8d9c2...](https://github.com/Towelstation13/towelstation13/commit/94bac8d9c21d92d0740a7759515d45734dae9489)
#### Thursday 2023-10-26 20:52:54 by SkyratBot

[MIRROR] Human sounds now depend on body type [MDB IGNORE] (#23999)

* Human sounds now depend on body type (#78632)

## About The Pull Request

So there's currently a problem where our human sounds are dependent on
whether you are a male or female, however we have 4 genders in-game.
This leads to scream sounds being female if you're anything but a Male,
and gasp shock sounds being male if you're anything but a Female. This
is very inconsistent, and I think as a better way of handling this, it
should all be handled by Bodytype, since we only have 2 and is a
separate choice from gender. This means regardless of gender, you can
still choose what sounds your character will make.

## Why It's Good For The Game

Mostly explained in the about section, this lets people who play as
they/them & it/its to decide what they should sound like.
I guess as a bonus, it means men now appear more like women if they
choose the female bodytype, and vice versa. Or at least I think it's a
bonus? I'm not really knowledgeable in this sort of stuff.

I kinda have the same argument as why I think TTS should be accurate.
You should be able to customize your character to how you want it, and I
think that choosing the non-male/female ones shouldn't give you
inconsistent voices.

## Changelog

I actually don't know what to label this.

:cl:
code: Your bodytype now decides what gendered sounds you make.
/:cl:

* Human sounds now depend on body type

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [ma44/mojave-sun-13](https://github.com/ma44/mojave-sun-13)@[736422fac8...](https://github.com/ma44/mojave-sun-13/commit/736422fac8d84c8e054853fd2b205cc993250c21)
#### Thursday 2023-10-26 21:29:56 by Technobug14

Field Transfusions & Fixes Sprites/Runtime (#2152)

* Working field transfusions

As far as I can tell, no runtimes or bugs. Should be good to go. Could maybe do with some polish? But otherwise it works great.

* Fixes energy weapon bugs

Fixes a runtime related to emptying cells from energy weapons, and fixes an overlay bug and inventory icon bug on the cells themselves.

* Bug fixes

read above, fixes a few bugs/errors

* Broken as hell

Supposed to add new IV bag sprites and overlays that would change as the bag gets emptier. Multiple bugs both with transfusion and the icon/overlay. Right now, the icon currently disappears once the object is on the ground and I can't tell why. Secondly, the overlay has the visual bugs and could probably do with a more thorough system to apply it? The bugs on transfusion are mostly due to a lack of sanity checks, where it will continue to be attached to someone from many tiles away when thrown/dropped, etc.

* Shit

HATE HATE HATE this sucks and it is buggy as hell

* Fix icon/overlay updates

* Mostly working

Still some broken stuff, you can attach IV bags if you're not next to someone and do it from inside containers, also fixes the world states for the police and military 10mm pistol

* Finishing touches

Couple of bug fixes, fixes 10mm police/military world sprite, etc etc. Should be good to go.

Co-authored-by: Koshenko <koshenko@pm.me>
Co-authored-by: Koshenko <53068134+Koshenko@users.noreply.github.com>

---
## [msysnk/Nike-ecommerce-website](https://github.com/msysnk/Nike-ecommerce-website)@[19191526a1...](https://github.com/msysnk/Nike-ecommerce-website/commit/19191526a16a37d232eb4ad107fb3ab9ae9ce564)
#### Thursday 2023-10-26 22:13:50 by msysnk

Update README.md

🌐 Welcome to [ file:///C:/Users/hp/Downloads/5.-ecommerce-2%20(2)/5.%20ecommerce%202/index.html ] - Your Ultimate Online Shopping Destination!

Embark on a seamless online shopping experience crafted with a blend of cutting-edge technologies. Our capstone project, meticulously developed using JavaScript, HTML, and PHP, brings you a feature-rich E-commerce platform.

🛍️ Shop with Ease: Immerse yourself in a user-friendly interface designed with HTML to provide an intuitive and visually appealing browsing experience. Navigate effortlessly through diverse product categories and discover a world of quality goods.

💡 Dynamic and Responsive: Powered by JavaScript, our website is not just static web pages but a dynamic and responsive platform. Enjoy real-time updates, interactive features, and a website that adapts to your device, ensuring a seamless experience whether you're on a desktop or a mobile device.

💻 Behind the Scenes with PHP: The robust functionality of our website is driven by PHP, handling tasks from processing orders to managing user accounts. Secure transactions and a smooth checkout process are guaranteed, thanks to the server-side magic of PHP.

🔒 Secure Transactions: Rest easy knowing that your transactions are safeguarded by the security features implemented through PHP. Our commitment to your privacy and data security is unwavering.

🌟 Capstone Craftsmanship: This website is not just a showcase of skills; it's a testament to the culmination of knowledge and expertise. The integration of JavaScript for dynamic elements, HTML for seamless structure, and PHP for powerful server-side functionality showcases the depth of understanding and skill development throughout this capstone project.

🚀 Experience the Future of E-commerce: As you explore [ file:///C:/Users/hp/Downloads/5.-ecommerce-2%20(2)/5.%20ecommerce%202/index.html ], you're not just interacting with a capstone project; you're glimpsing the future of online shopping. The harmonious marriage of JavaScript, HTML, and PHP creates an environment that's not just a virtual storefront but an immersive journey for every shopper.

---
## [bparees/api](https://github.com/bparees/api)@[5b82635ef1...](https://github.com/bparees/api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Thursday 2023-10-26 22:45:11 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[227b6c32f6...](https://github.com/silicons/Citadel-Station-13-RP/commit/227b6c32f62bd5c690dff60166bc581b9908e2c4)
#### Thursday 2023-10-26 22:47:18 by SpartanKadence

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
## [TheDoctor12/android_frameworks_base](https://github.com/TheDoctor12/android_frameworks_base)@[c45a8270cb...](https://github.com/TheDoctor12/android_frameworks_base/commit/c45a8270cb9ea08c9f4ab1289bc3f3a708cf514c)
#### Thursday 2023-10-26 22:49:34 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [LazennG/bad-idea-box](https://github.com/LazennG/bad-idea-box)@[9db2f06363...](https://github.com/LazennG/bad-idea-box/commit/9db2f06363bc325a0e8eadfdf7266e55def4d7c1)
#### Thursday 2023-10-26 23:05:25 by Scrambledeggs

Fuck you *Ungreens your Peacekeepers* (#20053)

* Sprites Part 1: I hate transparency

* Sprites Part 2: Electric Booogaloo

* lack of transparency fixed

* More sprite fixes

* Tacmask and sprites

* Tacprod inactive and nocell sprites

* Tacprod Animation Part 1: Bugs galore

* Tacprod Animation Part 2: Tacmask revengance

* white beret

---

