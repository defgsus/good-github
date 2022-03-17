## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-16](docs/good-messages/2022/2022-03-16.md)


1,781,525 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,781,525 were push events containing 2,829,448 commit messages that amount to 202,088,628 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[770ef81a1f...](https://github.com/tgstation/tgstation/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Wednesday 2022-03-16 00:02:19 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[759d24ab14...](https://github.com/GoblinBackwards/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Wednesday 2022-03-16 00:22:19 by san7890

Four Corners, Red Rover: An Exploration in Decal Trends [MDB IGNORE] (#65290)

* Four Corners, Red Rover: An Exploration in Decaled Trends

You there! What exactly is wrong with this photograph?!

You don't need to tell me, I've boxed it out. There's four individual corners for the decalling. This is weird. You may be asking: Why don't they use the "full tile" turf decals? Let me demonstrate.

Look at the difference between the one at left and the one in the middle. The turf decal totally smothers the nice contrast lines afforded to use by the base turf, causing it to have smooth, clammy exterior. This is probably why no mapper ever uses the full turf decal, much to the chagrin of people who stare at how big the size of this repo is.

Now, what's that on the right? Why, it's the new sprite (and pathing I made) to help counter-act this issue! This perfectly lines up with the contrast lines of the base turf, allowing us to have a non-flattened visualization, while not having four fucking turf decals a turf load upon initialization. How epic!

I've also added "contrasted" variants of the "half" and "anticorner" turf decals for future use. I probably won't go through and update this in this PR, but the opportunity remains available.

I may or not map this change across all the maps. We shall see.

* neutral corners

we love vsc

* no wait

i forgot a bunch of potential edgecases so we'll have to go back. yellow should be fine but neutral, dark, blue, and green should get a second look over

* recheck

found some stuff, probably missed out on others. let us commence forth

* MISTAKE

nearly a fucko bwoingo

* final pass

it compiles and i've had enough, someone else can probably figure it out from this point onwards

* #65230 goated my timbs

now we wait for linters to fail

* YOU DIDN'T SAY THAT THE FIRST TIME

LINTERS AAFAFAFF

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[884c1eeb62...](https://github.com/GoblinBackwards/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Wednesday 2022-03-16 00:22:19 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[eeb5465931...](https://github.com/StarStation13/StarStation13/commit/eeb546593148ce940e9adac2c663c453d6557247)
#### Wednesday 2022-03-16 00:24:09 by vincentiusvin

Ordnance Content Update: Scientific Papers (#62284)

How do I play/test/operate this?

Download NT Frontier on any modular computers. It should debrief you on what experiments are available and how to publish.
If you want to do a bomb experiment, make sure it's captured by the doppler array (as usual) and then print the experiments into a disk and publish it.
If you want to do a gas experiment, make the gas and either pump it into a tank and 1) overpressurize it with a "clear" gas like N2 or 2) overpressurize tanks with the gas itself. Make sure you do the overpressurizing in the compressor machine. When tanks are destroyed/ejected leaked gas will get recorded. Print it into a disk and publish it.
For publication, the file needs to be directly present inside the computer's HDD. This means you need to copy it first with the file manager.
Fill the data (if desired, it will autofill with boiler plate if you dont) and send away!
Doing experiments unlock nodes, while doing them well unlocks boosts (which are discounts but slightly more restrictive) which are purchaseable with NT Frontier.
If you are testing this and have access to admin tools, there are various premade bombs under obj/effect/spawner/newbomb

A doc I wrote detailing the why and what part of this PR.
https://hackmd.io/JOakSYVMSh2zU2YL5ju_-Q

---

# Intro

## The Problem(s)

Ordnance, (previously toxins) seems to lack a lot of content and things to do. The gameplay loop consists of making a bomb and then sending it off for credits or using it to refine cores. Ordnance at it's inception originally relies on players experimenting and finding the perfect mix over multiple rounds, but once the recipe for a "do-everything" mix got out, the original charm of individual discoveries becomes meaningless.

Another issue with ordnance is the odd difficulty curve. As a new player, ordnance is almost impossible to decipher, but once you watch a tutorial or read a wiki and can mail a 50k into space, there pretty much isn't anything else to do. Most players will be satisfied at this point without the gameplay loop encouraging them to understand or play more. The only thing you can do afterwards is to sink your teeth in and understand why that particular mix explodes the way it does. This again has a significant difficulty curve, but if you do that, the department doesn't acknowledge or reward that in any way. There are pretty much two huge spikes, with the latter one not really existing inside the department.

TLDR:
* The content being same-y over rounds.
* Odd difficulty curve: 
    1. A new player is oblivious to everything. 
    2. Those in the middle can repeat the final goal consistently without needing to understanding why
    3. There is nothing to justify spending more time in the department after reaching the midgame.

## Abstract

Scientific Papers aim to add a framework to run multiple experiments in ordnance. Adding more experiments scattered across various atmospheric aspects might allow players of various knowledge levels to still have something engaging to do. A new player should have an easier challange than to mail a 50K. While those that already can make bombs should have an easier time understanding why their bombs explode the way it does. Once they fully understand why, they can set their sights on taking advantage of another reaction to set their bomb off or hone one particular reaction down.

## Goals

* Have some intro-level challanges for new players.
* Have some semblance of late-game challanges for more experienced players.
* Explain the mechanics better for those in the middle of the road.
* Incentivize trying new things out in the department.
* Better integrate Ordnance with Experisci

## Boundaries / Dont's

* Do not incentivize people to learn ordnance by using PvP loots.
* Do not shake or change the reaction system by a huge amount.
* Disincentivize having a single god-mix that does everything.
****

# Main design pillars

## A. Framework surrounding the experiments

### A.1. New experiments

Add new experiments to the ExperiSci module. These will come in two flavours: New explosions to do, and various gas synthesis experiments. Both of these are actually supported by the map layout of ordnance right now, but there is no reason to do anything outside of making a 50k as fast as possible.

### A.2. Rewards for experiments: Cash and Techweb Boosts.

Scientific papers will add a separate experiment handling system. A single experiment will be graded into various tiers, each tier corresponding to the explosion size or amount of gas made.  Doing any tier of a specific experiment will unlock the discount for that specific reactions. A single explosion **WILL NOT** do multiple experiments (or even tiers) at once.

On publication, a partner can be selected. A single partner only has a specific criteria of experiments they want. The experiments will then be graded on "how good they are done", with the criteria being more punishing as tier increases. Publication will then reward scientific cooperation with the partnered partner. Players can spend this cooperation on techweb boosts. Techweb boosts are meant to be subservient to discount from experiments and will not shave a node's price to be lower than 500 points.

**Experiments will only unlock nodes, discounts are handled through this boost system.**
This is more for maintainability than anything.

### A.3. On Tedium

*This is a note on implementation more than anything, but I think this helps explains why several things are done.*

Due to the nature of atmospheric reactions in the game (they're all linear), tedium is a very important thing to consider. An experiment should have a sweet spot to aim for, but there should not be a point where further mastery is stopped dead on it's track with a reward cap.

Scientific Papers attempts to discourage this behaviour by having the "maximum score" scale off to infinity but with the rewards being smaller and smaller. The sweet spot is always there to aim for and should be well communicated with players, but on their last submission of an experiment topic players should be encouraged to do their best. There should always be a reward for pushing the system to it's limit as long as it doesn't completely nullify the other subdepartments. This is the reason why there is a hard limit on the number of publications and why the score calculation is a bit more complex than it needed to be.

## B. Gas Synthesis (Early-Mid Game)

Scientific papers will add one new machine that requests a tank to release x amounts of y gas. This will be accomplished by adding a tank pumping machine which will either burst or explode a tank, releasing the gas inside. The gas currently requested are BZ, Nitryl, Halon and Nob.

The overarching goal of this compressor machine is to present a gas synthesis challange for the players and to get them more accustomed to how a tank explodes. The gas synthesis part can always be changed in order to reflect the current state of atmospheric reactions.

## C. Explosion Changes (Mid-Late Game)

### C.1 Cause and effect.

The main theme of the explosion changes is establishing cause and effect of explosions. Reactions that happens inside a tank that's going to explode will be recorded and forwarded to a doppler array. Some experiments will require only a single cause to be present (think of it as isolating a variable). This is currently implemented for nobliumformation and pressure based bombs. Having other reactions occuring besides noblium formation will fail the first one, while having any reactions at all will fail the second one. 

Adding more explosions here will be a slight challange because as of now the game has only two reactions that can reliably make an explosion.

### C.2 Tools upgrade.

Doppler array has now been retrofitted to state the probable cause of an explosion, be it reactions or just overpressurization on gas merging. These should help intermediate players figure out what is causing an explosion.

Added a new functionality to the implosion compressor:
Basically performs the gas merging and reaction that TTV does in a machine and reports the results back as if someone uses an analyzer on them. Here to give players feedback so they can try and understand what is actually going on in a bomb.

## D. Player Interaction

There should be more room for more than 1 player to play ordnance simultaneously. Previously players are also able to split tasks, but this rarely happens because tritium synthesis needs only the gas chamber to be reconfigured. Now, different players can pick different experiments and work on them. Players can also do joint tasks on one single experiment. Gases like noblium will need tritium production and also a cooling module online.

Ordnance can also coordinate with their parent department on what they really need, be it money or research bonuses.

# Potential Changes

The best-case changes that can be implemented if the current roster of content isn't enough is more reactions that can be used in bombs. Eliminating bombs entirely goes against the spirit of the subdepartment, while adding new ones will need a lot of care and consideration.

Another possible change is to implement a "gas payload" bomb. Bombs that has a set number of unreacting gas inside that will increase the heat capacity, reduce the payload, and neccesitates more bespoke mixes.

Adding more gas synthesis experiments is discouraged. The main focus of ordnance should be bombs, with gas synthesis being a side project for ordnance. These are present to ease the introduction to bombs and provide some side content. 
There should be a somewhat well-justified goal in adding new synthesis experiments: e.g. BZ is there as a "tutorial" gas, Nitryl to introduce players to cooling/heating mixes, Halon to a more efficient tritium production, and Nob as a nudge to nobformation bombs and mastery over other aspects.

# Conclusion / Summary

Add more experiments to ordnance that players can take, accomplish this by:
1. Making the players perform gas synthesis or make bombs.
2. Have them collect the data, see if it fits the criteria. Explain why if it fits and why if it doesn't.
3. Have the player publish a paper.

Reward them based on how well did they do, give players agency both on the experiment phase and also publication phase.


---
TLDR: Added new experiment to toxins, added the framework for those experiments existing. Experiments comes in gas synthesis and also bombs but with more parameters. Experiments needs to be published through papers, various choices to be made there.

Implementation notes:

Because of how paper works, ordnance experiments are handled outside of experiment_handler components. My reasoning for this is twofold:

The experiments will be completed manually on publication and if the experiment isn't unlocked yet it will still be completed.
Experiment handler datums have several procs which require an atom-level parent, and I figured this is the most sensible and cleanest way to implement this without changing the experiment handler datum too much.

Small change to /obj/machinery/proc/power_change() signal ordering to adjust the state first and then send the signal. Didn't found any other usage of this signal except mine but barge down my door if it broke something.

Rewrote the ttv merge_gases() code to be slightly more readable.
A small code improvement for thermomachine to use tofixed (my fault).

Ordnance have been updated to enable the publication of papers
Several new explosive and gas synthesis experiments have been added to ordnance
Anomaly compressor has been TGUIzed and now supports simulating the reaction of the gases inside the ttv.
New tank compressor machine for toxins. You can overpressurize tanks with exotic gases and complete experiments.
Several techweb nodes are locked and require toxin experiments to complete.
Toxins can purchase boosts for various techweb nodes.
You no longer need to anchor doppler arrays for it to work.
Doppler array and implosion compressor now supports deconstruction, implosion compressor construction added.
Doppler now emits a red light to denote it's direction and it being on. Doppler not malf.
Implosion compressor renamed to anomaly refinery.
Created a new program tab "Science" for the downloader app. Removed Robotics.
Reworked the code for bombspawner (used in the cuban pete arcade game)

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[ac21ef9078...](https://github.com/Timberpoes/tgstation-nxt/commit/ac21ef9078d88f51a4e198e394ed56e3cc731b45)
#### Wednesday 2022-03-16 00:41:28 by Pickle-Coding

No, we don't want radiation getting released in large pipenets fuck you fuckr uyu! (#65212)

* Make it harder to release radiation in large pipenets. Squares the volume / 2,500 thingy, and adds the requirements to the proto-nitrate bz response and proto-nitrate tritium response gas reactions to release radiation. This will make it significantly harder to release radiation in large pipenets, because releasing radiation in large pipenets makes it harder for people to identify the cause on why they are getting irradiated, which is bad and goes against the modern radiation goals.

Squaring is not enough for deranged people that know we don't want radiation released in large pipenets. Cubes the requirement instead. If someone could get enough gases reacting at once after this, then there is a bigger problem with atmos.

Who had fun seeing everything green, then getting irradiated and not even knowing why? I don't know, because I don't know who put the gases in waste and why we must suffer.

---
## [mwmichalek/MyQ](https://github.com/mwmichalek/MyQ)@[59752e5886...](https://github.com/mwmichalek/MyQ/commit/59752e58865037baf99ad7f8d1a323d42df0e631)
#### Wednesday 2022-03-16 01:14:16 by mwmichalek

For some reason requests to the server aren't going out.  Fuck you!

---
## [GraveofBears/OdinUndercroft-New](https://github.com/GraveofBears/OdinUndercroft-New)@[133e879af3...](https://github.com/GraveofBears/OdinUndercroft-New/commit/133e879af316efff69868572510ea045526e8dc3)
#### Wednesday 2022-03-16 02:21:24 by GraveofBears

updated item manager - even though I dont use it for this mod... fuck it.. it's awesome anyways..
added creature manager in case I want to add a friendly bat to build in the undercroft.
added serversync even though I dont think it does shit with azu's current build of piece manager.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0e904f7032...](https://github.com/tgstation/tgstation/commit/0e904f70328a460af310014891eaadb5968ec31a)
#### Wednesday 2022-03-16 02:56:08 by LemonInTheDark

[MDB IGNORE] Moves non floor turfs off /floor. You can put lattices on lavaland edition (#65504)


About The Pull Request

Alternative to #65354

Ok so like, there was a lot of not floor types on /floor. They didn't actually want any of their parent type's functionality, except maybe reacting to breaking (which was easy to move down) and some other minor stuff.
Part of what we don't want them to have is "plateable" logic.
I should not be able to put floor tiles on the snow and be fine. It's dumb.

Instead, I've moved all non floor types down to a new type, called /misc.

It holds very little logic. Mostly allowing pipes and wires and preventing blob stuff.
It also supports lattice based construction, which is one of the major changes here. I think it makes more sense, and it fixes an assumption in shuttle code that assumed you couldn't place "a new tile" by just hitting some snow with a floor tile.
Oh and lattices don't smooth with asteroid tiles anymore, this looks nicer I think.

Moving on to commits, and minor changes

Changes clf3 to try and burn any turfs it's exposed to, instead of just floors
Moves break_tile down to the turf definition, alongside burn_tile
If you're in basic buildmode and click on anything that's not handled in a targeted way, you just build plating
FUNCTION CHANGE: you can't use cult pylons to convert misc tiles over anymore
Generalizes building floors on top of something into two helper procs on /turf/open, reducing copypasta
Adds a new turf flag, IS_SOLID, that describes if a turf is tangible or not.
Uses this alongside a carpet and open check to replace plating and floor checks in carpet code. This does mean that non iron tiles can be carpeted, but I think that's fine

Moves the /floor update_icon -> update_visuals call to /open
This change is horrificly old, dating back to 8e112f6 but that commit describes nothing about why it was done. Choosing to believe it was a newfriend mistake. Uncomfortable nuking it though, because of just how old it is. Moving down instead

Create a buildable "misc" type off open, moves /dirt onto it
Basically, we want a type we can use to make something support
construction, since that can be a messy bit of logic. Also enough
structure to set things up sanely.

I'm planning on moving most misc turfs onto it, if only because
constructing on a dirt tile with rods should be possible, and the same
applies to most things

Murders captain planet, disentangles /turf/open/floor/grass/snow/basalt

Adds a diggable component that applies the behavior of "digging"
something out from a turf.

Uses it to free the above pain typepath into something a bit more
sensible

The typepaths that aren't actually used by floor tiles are moved onto
/misc

The others are given names that better describe them, and kept in
fancy_floor

Oh and snowshoes don't work on basalt anymore, sorry

Snowed over platings now actually have broken/burned icon states, fixing black holes to nowhere

Misc turfs no longer smooth as floors, so lattices will ignore them

Placing a lattice will no longer scrape the tile it's on

Ok this is a really old one.
I believe this logic is a holdover from kor's baseturf pr
(97990c9)
It used to be that turfs didn't have a concept of "beneath" and instead
just decided what should be under them by induction. This logic of "if
it's being latticed scapeaway to space" made sense then, but has since
been somewhat distorted

We do want to scape away on lattice spawn sometimes, mostly when we're
being destroyed, but not always. We especially don't want to scape away
if someone is just placing a rod, that's dumb.

Adds a path updating script for this change

I've done my best to find all the errors this repathing will pull out, but I may have missed some. I'm sorry.
Why It's Good For The Game

Very old code made better, more consistent turfs for lavaland and icebox, better visuals, minor fix to snowed plating, demon banishment in lattice placement, fixes the icebox mining shuttle not being repairable
Changelog

cl
add: Rather then being tileable with just floor tiles, lavaland turfs, asteroid and snow (among other things) now support lattice -> floor tile construction
fix: Because of the above, you can now properly fix the icebox mining shuttle
refactor: Non floor turfs are no longer typed as floor. This may break things, please yell at me if it does
/cl

---
## [Terminator-J/crdroid_kernel_oneplus_sdm845](https://github.com/Terminator-J/crdroid_kernel_oneplus_sdm845)@[1f51fd987d...](https://github.com/Terminator-J/crdroid_kernel_oneplus_sdm845/commit/1f51fd987d9b056d7a287df058002bf137765ee1)
#### Wednesday 2022-03-16 03:12:24 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [ConsistencyPlus/ConsistencyPlus](https://github.com/ConsistencyPlus/ConsistencyPlus)@[ead15f4e6f...](https://github.com/ConsistencyPlus/ConsistencyPlus/commit/ead15f4e6f887dbb3379e64aafbbcc09b7319cc0)
#### Wednesday 2022-03-16 05:26:08 by Siuol

EnhancedRegistry (#102)

* Made a prototype registry

In this commit I did the following:
Made a prototype "Enhanced" registry.

This is a VERY early prototype, and does not have many features even added. As an extra Siuol bonus, I didnt even test the previous commit on master nor this one!

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

* Fully done registry

In this commit I did the following:
Enhanced the registry, its now for blocks AND items.

This is still a VERY early prototype. And a stupid idea as well, but you have to counterract the amount of effort it takes to maintain the registry somehow.

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

* Completed* Enhanced Registry

In this commit I did the following:
Finished up the enhanced registry for now, it contains most blocks/items. The amount of concerning code here is unreal. It still technically needs support for Mossy/Cobble, but for now, it should work well.

I am very proud of my self. Look important people I did a thing.

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

* No its not 1.18.2 yet guys.

In this commit I did the following:
- Updated models for Sandstone, Red Sandstone, and Soul Sandstone to look improved.
- Cleaned up EnhancedRegistry code.
- Removed BlockColors, replaced with the built-in DyeColor enum.
- Turned Wither Skele drops into a loot table injection on Fabric. Forge has its regular version until I can get to that.

1.18.2 SOON I PROMISE

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

* Oh cmon its close enough.

In this commit I did the following:
- Got us on 1.18.2 to a frame of the loading screen in game.

Ima be honest, I already need a break.

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

* HAHA YES I FINALLY DID IT

In this commit I did the following:
- Got us into the game on Fabric 1.18.2

I already want another break.

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

* Someone else please pick up from here

I have lost like 5 years from my life trying to make this mod work on Forge.

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

* Alright right on schedule yep. (0.5.0-RC2)

Screw the commit names this is 0.5.0-RC2

Signed-off-by: Siuol <43890828+Siuolthepic@users.noreply.github.com>

---
## [WordPress/gutenberg](https://github.com/WordPress/gutenberg)@[3ea2d42b0a...](https://github.com/WordPress/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Wednesday 2022-03-16 06:31:50 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[3304ea21ae...](https://github.com/Koi-3088/ForkBot.NET/commit/3304ea21ae15576306125e0278dab65803258425)
#### Wednesday 2022-03-16 06:48:05 by Koi

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
## [BrandonJorgen/Cavalry](https://github.com/BrandonJorgen/Cavalry)@[d4b8bd64e9...](https://github.com/BrandonJorgen/Cavalry/commit/d4b8bd64e9259beed28548d64f063fae374c07e8)
#### Wednesday 2022-03-16 07:45:08 by Brandon

tested my shit on a railing, it looked like a bitch

love, sleepy brandon

---
## [ShravanakumarGuram/Movielens_Case_Study_Shravan](https://github.com/ShravanakumarGuram/Movielens_Case_Study_Shravan)@[8a19fe1610...](https://github.com/ShravanakumarGuram/Movielens_Case_Study_Shravan/commit/8a19fe161069624712532b272ad02332e42330df)
#### Wednesday 2022-03-16 08:24:14 by ShravanakumarGuram

Movielens Case Study

DESCRIPTION

Background of Problem Statement :

The GroupLens Research Project is a research group in the Department of Computer Science and Engineering at the University of Minnesota. Members of the GroupLens Research Project are involved in many research projects related to the fields of information filtering, collaborative filtering, and recommender systems. The project is led by professors John Riedl and Joseph Konstan. The project began to explore automated collaborative filtering in 1992 but is most well known for its worldwide trial of an automated collaborative filtering system for Usenet news in 1996. Since then the project has expanded its scope to research overall information by filtering solutions, integrating into content-based methods, as well as, improving current collaborative filtering technology.

Problem Objective :

Here, we ask you to perform the analysis using the Exploratory Data Analysis technique. You need to find features affecting the ratings of any particular movie and build a model to predict the movie ratings.

Domain: Entertainment

Analysis Tasks to be performed:

    Import the three datasets
    Create a new dataset [Master_Data] with the following columns MovieID Title UserID Age Gender Occupation Rating. (Hint: (i) Merge two tables at a time. (ii) Merge the tables using two primary keys MovieID & UserId)
    Explore the datasets using visual representations (graphs or tables), also include your comments on the following:

    User Age Distribution
    User rating of the movie “Toy Story”
    Top 25 movies by viewership rating
    Find the ratings for all the movies reviewed by for a particular user of user id = 2696

    Feature Engineering:

            Use column genres:

    Find out all the unique genres (Hint: split the data in column genre making a list and then process the data to find out only the unique categories of genres)
    Create a separate column for each genre category with a one-hot encoding ( 1 and 0) whether or not the movie belongs to that genre. 
    Determine the features affecting the ratings of any particular movie.
    Develop an appropriate model to predict the movie ratings

Dataset Description :

These files contain 1,000,209 anonymous ratings of approximately 3,900 movies made by 6,040 MovieLens users who joined MovieLens in 2000.

Ratings.dat
    Format - UserID::MovieID::Rating::Timestamp
Field 	Description
UserID 	Unique identification for each user
MovieID 	Unique identification for each movie
Rating 	User rating for each movie
Timestamp 	Timestamp generated while adding user review

    UserIDs range between 1 and 6040 
    The MovieIDs range between 1 and 3952
    Ratings are made on a 5-star scale (whole-star ratings only)
    A timestamp is represented in seconds since the epoch is returned by time(2)
    Each user has at least 20 ratings

     

Users.dat
Format -  UserID::Gender::Age::Occupation::Zip-code
Field 	Description
UserID 	Unique identification for each user
Genere 	Category of each movie
Age 	User’s age
Occupation 	User’s Occupation
Zip-code 	Zip Code for the user’s location

All demographic information is provided voluntarily by the users and is not checked for accuracy. Only users who have provided demographic information are included in this data set.

    Gender is denoted by an "M" for male and "F" for female
    Age is chosen from the following ranges:

 
Value 	Description
1 	"Under 18"
18 	"18-24"
25 	"25-34"
35 	"35-44"
45 	"45-49"
50 	"50-55"
56 	"56+"

 

    Occupation is chosen from the following choices:

Value
  	Description
0 	"other" or not specified
1 	"academic/educator"
2 	"artist”
3 	"clerical/admin"
4 	"college/grad student"
5 	"customer service"
6 	"doctor/health care"
7 	"executive/managerial"
8 	"farmer"
9 	"homemaker"
10 	"K-12 student"
11 	"lawyer"
12 	"programmer"
13 	"retired"
14 	 "sales/marketing"
15 	"scientist"
16 	 "self-employed"
17 	"technician/engineer"
18 	"tradesman/craftsman"
19 	"unemployed"
20 	"writer”


Movies.dat
Format - MovieID::Title::Genres
Field 	Description
MovieID 	Unique identification for each movie
Title 	A title for each movie
Genres 	Category of each movie

 

     Titles are identical to titles provided by the IMDB (including year of release)

 

    Genres are pipe-separated and are selected from the following genres:

    Action
    Adventure
    Animation
    Children's
    Comedy
    Crime
    Documentary
    Drama
    Fantasy
    Film-Noir
    Horror
    Musical
    Mystery
    Romance
    Sci-Fi
    Thriller
    War
    Western

    Some MovieIDs do not correspond to a movie due to accidental duplicate entries and/or test entries
    Movies are mostly entered by hand, so errors and inconsistencies may exist

---
## [trjstewart/terraform-provider-cloudflare](https://github.com/trjstewart/terraform-provider-cloudflare)@[7dc1827e5f...](https://github.com/trjstewart/terraform-provider-cloudflare/commit/7dc1827e5f785898adcf04cb796c0710072c64ff)
#### Wednesday 2022-03-16 09:27:58 by Jacob Bednarz

resource/cloudflare_ruleset: improve dashboard collisions

One of the earliest niggles with customers coming from the dashboard to
Terraform was the collision caused by a Ruleset phase being created in
the UI but the Terraform provider also needing to create the same
phase. This was problematic for a few reasons:

- The first was that when you deleted Ruleset rules in the UI, it didn't
  remove the phase. This was intentional but hidden behind the UI and
  only accessible via the API.
- Secondly, when customers wanted to use Terraform, there was an
  assumption they would be starting from scratch and many were not.
- Finally, in the event of a collision, we didn't know which Ruleset the
  customer wanted to use so we error'd out with a link to manually
  resolve which isn't a great solution but made the issue more
  prominent.

I had a chance to rethink through this issue and managed to find a way
that we improve all three points above and remove majority of the pain
points. With the proposed changes, the only time a customer needs to
manually resolve the Ruleset rules is if there are existing rules in the
UI which requires them to be deleted or migrated.

Achieving this requires the assumption that if the Ruleset has no rules,
it is ok to modify. Unfortunately, it's not that simple in practice. If
the phase already exists, we cannot just update it as the `name`
attribute is not writable after creation. Along with this, the `ref` and
`version` values will be automatically incremented causing a permadiff
in Terraform as the customer hasn't actually modified these values but
the backing service (and API) has. To work around this, if we find a
phase with no rules, we recreate it with the provided values which is
essentially the same the same thing as the "happy path" for a new
Terraform resource would be anyway.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[dc52f3bd31...](https://github.com/treckstar/yolo-octo-hipster/commit/dc52f3bd31621a94057e832f64ef266e7574c00a)
#### Wednesday 2022-03-16 09:45:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [donnaken15/FastGH3](https://github.com/donnaken15/FastGH3)@[670f639cef...](https://github.com/donnaken15/FastGH3/commit/670f639cef168a32087d64208fd451174e452270)
#### Wednesday 2022-03-16 10:15:18 by Wesley

major gh3+ stuff

rich presence (outtaken here right now because need to find a way to display metadata from a song PAK instead of from qb.pak, same with currentsong.txt)
made room for both battle note and tap note textures
basic bot star power like in my RB1 DTA patches
16.6MB zones, texture cleaning
chart shuffler, use with section [Shuffle] and Path1,Path2,Path3 (OR MAKE ANOTHER UI, WES, JFC)
i just remembered i need to have a cheats menu, which also reminds me i still need to make a custom pause menu so i can have whatever i want in it
magically deflated some music tools files
thinking of making a release right now with this

---
## [prince-rudh/Rudhra2.0](https://github.com/prince-rudh/Rudhra2.0)@[524af5a879...](https://github.com/prince-rudh/Rudhra2.0/commit/524af5a87988f005379c6aaa5442444847ba41df)
#### Wednesday 2022-03-16 11:20:14 by Prince Rudh

📢 Rudhra Update ⏳Available Now! …

# Contributing to Prince-Rudh

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [ReadMe](https://github.com/prince-rudh/Rudhra2.0/blob/master/README.md).
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you 
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at AsenaDev. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.


### Warning ⚠️

This project is open source. So you are responsible for the changes you make.
It is your responsibility to use these codes. We are not responsible for any bad things you make.

##

---
## [intona/ethernet-debugger](https://github.com/intona/ethernet-debugger)@[3d7aa3aa36...](https://github.com/intona/ethernet-debugger/commit/3d7aa3aa362d7f07134c57268013e08d68c0c803)
#### Wednesday 2022-03-16 11:27:26 by Vincent Lang

nose: redo exit behavior (--exit-on in particular) yet again

The previous commit was wrong and was pushed too soon. We don't actually
want to keep nose running by default if all input died and capturing is
still active.

The behavior as it should be is:

If nose is started with --wireshark or --fifo, we want nose to exit if
capture stops, because it would be annoying to keep the terminal command
line around after Wireshark or the consumer of --fifo is terminated.
Also, it should be possible to start nose without any input in this
case, so we can say input terminating should not be a reason to
terminate nose. This is the behavior of the "no-capture" mode.

If nose is started without any arguments, we're definitely in an
interactive mode. Stopping capture should not exit nose. Losing control
input should exit, even if capture is active. This is the behavior of
the "no-input" mode.

If nose is started with IPC (--ipc-server or similar), the situation is
actually the same as in interactive mode. An IPC connection of any kind
counts as control input, and as long as it exists, we should not exit.
If it gets lost, we should stop even if capture is going on, because we
have to assume something with the IPC master went wrong, and we should
not hog the USB device any longer.

(One problem with --ipc-server was that it would exit anyway if stdin
was closed, which can happen in scripts. This situation was fixed
earlier.)

At least with --fifo, the user might want the behavior that "interactive
mode" defaults to. For that, "--exit-on no-input" can be used.

The other --exit-on modes are probably not terribly useful in general.
But I feel like "default" is needed to do the right (?) thing,
"no-input"/"no-capture" to force the exact behavior, "never" to make the
auto-magic behavior get out of the way, and "always" is sometimes useful
for scripting.

I considered adding a combined "no-input-no-capture" mode, which would
make nose exit if neither input nor capturing was active. This mode of
behavior is actually removed from this commit (used to print "Nothing to
do and no controlling input."), but I couldn't come up with a reason why
anyone would need this.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Wednesday 2022-03-16 13:50:04 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[0327ed966e...](https://github.com/mrakgr/The-Spiral-Language/commit/0327ed966e2357f6bc5cee1b03e172f185031026)
#### Wednesday 2022-03-16 14:16:42 by Marko Grdinić

"8:30am. I might be up early, but that is because I literally didn't get a wink of sleep all night. I worry about my past, I worry about my future, and I worry about my mother.

I've honestly been considering getting a job just so I could get the money to cryofreeze her. The fact that she will likely be dead of cancer before the end of the decade scares me. I have no idea what her state is. For all I know she might end up dead next year. Seeing my dad start to take over some of the cooking duties feels like a slap in the face. I feel so powerless. Can't I do anything for her?

How can I be studying art at a time when I should be curing cancer?

I've been trying not to think about it and it is hard to focus on the goal at hand.

...A path is a path. My old path had it worked would have given me the power to do this, but it didn't.

8:35am. Besides cryofreezing her, the only other option for saving he is to eventually just ask whoever is running the universe for a backup of her. That means leaving her to die in the pursuit of transcendence.

As a plan, that is not something I'd want to rely on. Who knows when and if I will reach that. Emotionally, the Singularity has never felt further away from me. Even if it will happen in 20 years, what does that matter unless I reach it myself?

9:05am. I had plenty of days such as these in the past. As much as they suck I've always had a good night's sleep afterwards. And despite the fatigued state I've always ended up putting away a chunk of work. Despite the frayed nerves, or because of them, I have less distractions going through my mind.

I never feel like resting in this state and always feel like working.

Let me read Frieren and I will watch that course. Let me set the rest of the Nuke files to download.

9:10am. Let me start. First let me watch the two videos in the Houdini section. That will give me a reference that I can aim for myself. After that come the Clarisse parts. No doubt those will be informative. He should be using USD for imports and exports, that keynote talk highligted the compression benefits. After that I'll know what I have to do to adapt my own scene for the export. I'll finish the course of course.

9:40am. Hmmm, how did he export the masks? I'll have to figure that out myself.

9:50am. Yeah, I've been wondering myself how he was going to do the inner part of the skull. He says it took him a while to figure out. I myself have no idea how I would do this.

He says the answer is deceivingly simple. Is he just going to add the skull as a separate object then, not as a part of the heightfield? That is the direction I'd try to go in.

10:10am. Had to take a break. Let me resume.

10:15am. Instead of dragging that big box, he could have just used the bounding box of the skull.

But I am surprised that he is insisting on working with heightfields to the end instead of making the skull a separate object. It would be way easier to export the heightfield, put the skull, and then using a sculpting tool, or hell even simple proportional editing, drag it into shape.

Doing it like this would always have the problem of not having cavities. I really have no idea what he is aiming for 15:30m into part 4.

He could also have decimated the mesh temporarily to get better performance. PolyReduce and Remesh both accept masks too, so he does not have to worry about losing detail in the relevant sections.

19:20m in. Just what is he doing? Converting them to surface VDBs. Why now convert the skull from the start and just union it?

10:35am. What mystifying methods. I have no idea why he did not just input the vdb union the skull and then transfered the attributes. He also dragged those objects around when he should have been snapping.

10:40am. Ah, I see. I didn't have enough sleep so my focus is low, so I did not see that he was outputting the maps as `.exr`s. But on the plus side, I am not distracted.

Hmmm, actually if he is exporting the attributes as expr, was there any need to worry about how they would transfer in the first placE?

10:45am. Now he jumps into Clarisse. But he is not exporting as USD. Nevermind this. What I will do is play around with USD imports and exports on my own. Then I'll get back to the course.

10:55am. I tried exporting, but it just exports everything as one big object. That is what I see in Clarisse. Surely I won't need an USD file per object? Let me check out the docs for the USD export file.

https://www.sidefx.com/docs/houdini/solaris/output.html
https://www.sidefx.com/docs/houdini/solaris/usd.html

This is Solaris related. But what about on the obj context?

11:10am. Let me try the staging stuff.

...Let me take a break against first.

11:25am. My digestion is messed up due to a night like this.

[usd] At least one of the prim in this stage was left-handed!
[usd] Loading a left-handed asset requires a conversion which has an impact on performance. When possible, please re-export as right-handed.

I got this warning, but when exported from Solaris I get all the objects individually. This is going to be a pain. I am going to have to rebuild the pool scene in Solaris.

Let me try partitioning the torus.

11:40am. I guess I'll use the V-Ray shaders.

11:45am. What a piece of crap. I am trying to assign shaders and getting Python exceptions. At least it did not take out Houdini in its entirety.

11:50am. Once again, what a piece of crap. Forget V-Ray. Let me try the regular principled shader.

...Enough. Even the principled shader fails. It is clear to me that linking materials is not Solaris' strong suit. I am really amazed at how buggy these programs can be at even the most basic of things.

12am. This has taken me completely by surprise. What was I supposed to be doing?

Forget about doing any kind of shading or material assignment in Houdini. Let me just try some attribute partitioning on the box.

12:15pm. Nope, it does not seem to be working. I can't see where these attributes are exported. I tried setting a shading layer rule, but it is not working for me. I am out of ideas.

12:20pm. But I basically know how to do the scene. The rest does not matter too much. I should watch some Solaris tutorials in order to properly figure it out. Actually since they are hours long, I should start by watching Clarisse shading layer tutorials.

https://www.youtube.com/results?search_query=clarisse+shading+layer

Yeah, there some to be short and sweet 12m tutorials here. I should be watching this. Let me have breakfast here first though.

1:05pm. Done with both breakfast and chores. Let me study the shading layers.

https://youtu.be/p_2kX9gFSgs
Shading Layers Best Practices

https://youtu.be/p_2kX9gFSgs?t=283

This is tedious. Let me take another break. I want to read Dark Lady. After that I'll watch the thing.

1:25pm. Let me resume. There is so many details in this video. I need to find it in myself to focus.

https://youtu.be/p_2kX9gFSgs?t=350

What are these shading groups?

> Specifying Shading Groups
> A shading group is an item component. To specify a component in a path you need to use the character >. For example, if you wish to specify a rule locating a specific shading group, you would write: project://f40_layer0>car_paint

1:35pm. I can't figure this out right now. Let me just watch more of the tutorial.

https://forum.isotropix.com/viewtopic.php?p=18009
Shading groups: houdini/zbrush

///

Hello,

I have been trying to figure out how to setup shading groups in my 2 modeling softwares but cant quite figure it out. I use zbrush and houdini for modeling and i would like to be able to make the groups in either one of those packages if possible. I do not have access to any other softwares, so i cant just import to for example maya and make them.

Zbrush: Is it possible to make shading groups in clarrise from polygroups in zbrush? or is it even possible to make them in zbrush?

Houdini: I tried grouping primitives/points but clarisse doesnt recognize it. Maybe i have not exported it correctly from houdini. So same question as for zbrush, is it possible to make shading groups in houdini that clarisse can see?

thank you.

///

Oh, this is exactly what I've been looking for.

1:40pm. Yeah, my brain is slow right now. I actually had the idea that maybe I needed to create actual groups, but then promptly forgot about it until I got confirmation. Let me try it.

1:50pm. I hate Houdini. Everything is so complicated in Solaris. Nothing is obvious. Let me finish the tutorial.

https://forum.isotropix.com/viewtopic.php?f=21&t=6337
Clarioni - Houdini link to Clarisse -> Dev Thread

Hmmm, what is this? Never expected to see something like this. It hasn't seen development in over a year though. Skip.

https://www.youtube.com/watch?v=XeR9Ut79bT0
Use Houdini Attributes Inside Clarisse iFX

This video might be exactly what I want. Let me take a look.

https://youtu.be/XeR9Ut79bT0?t=533

Here are the properties. The fatigue is hitting me very hard right now and I am having to force myself to keep my eyelids open. Let me see if I can figure out how to export groups and I will go to bed.

2:35pm. I tried exporting groups at the sop level and it is not working for me.

It only seems to work on points. Let me also try point groups.

Let me ask Stormz. I can't figure it out.

2:50pm. I see. I imported the spaceship and I see the shop_materialpath attribute. I can only be that.

Oh, indeed, the `shop_material` path works when exporting `.obj`s. What about USD?

Maybe USD needs some other attribute. Or it needs the shading group to be set in the stage context? With the material linker being so broken fat chance. No, I don't think you can select individual geometry in LOPs.

https://youtu.be/mpkVvMHOvmc
Working With USD

Let me watch some of these, I really want to go to bed.

https://www.youtube.com/results?search_query=houdini+export+usd

Let me watch the first with which on exporting to Unreal. I just want to figure this out and then I will go to bed. I am dying here.

3:10pm. Nevermind. I asked in two different place. I'll ask on odforce if I do not get an answer by tomrrow. Let me go to bed.

It is not an urgent thing to know by any means, I just got hung up on figuring it out. I can dedicate tomorrow to the course. I did well enough today given the condition I am in."

---
## [lluni/CyberCodeOnline](https://github.com/lluni/CyberCodeOnline)@[6d5cb134f2...](https://github.com/lluni/CyberCodeOnline/commit/6d5cb134f217d2cfa2a14edfd3a81d4748a74fdc)
#### Wednesday 2022-03-16 14:38:19 by S0M3_DUD3

Updated german commen used curse words

Translations
		"Arschfresse" - Analface
		"Arschlecker" - Anallicker
		"Arschficker" - Analfucker
		"Pimmel" - other word for dick
		"Schwanzlutscher" - dicksucker
		"Kanacke" - curse word for imigrants
		"Fettsack" - "Fat guy"
		"Schlampe" - "Bitch"
		"Mutterficker" - "Motherfucker"
		"Assi" - curse word for jobless
		"Aushilfsnazi" - nazi thing

---
## [mwbranstad/opentitan](https://github.com/mwbranstad/opentitan)@[29b8d2c3e7...](https://github.com/mwbranstad/opentitan/commit/29b8d2c3e7fde48a117a31241c508bd4325f5b88)
#### Wednesday 2022-03-16 15:10:03 by Rupert Swarbrick

[dv,verilator] Make multiple sim_ctrl extensions play nicely

I'd finally got annoyed enough about not being able to pass "-t" in
the middle of a command line to figure out what was going on. It turns
out that by default getopt_long rearranges its arguments to put all
positional args at the end. That's nice, because it allows you code to
easily support stuff like

   my_program -a -b positional0 -c -d positional1

and, post-parse, it will find positional0 and positional1 as the last
two arguments. (If long enough in the tooth, you might remember having
to do "my_program -a -b -c -d positional0 positional1" for some
programs: this is what getopt fixes for us!)

Unfortunately, this behaviour plays havoc when more than one parser
wants to look at argv at once. For example, suppose you have

   my_program --some-args ARG --no-args

and you parse this twice. The first parser understands --no-args and
the second understands --some-args. With the default behaviour and ":"
at the start of the optstring, the first parser will ignore the
unknown --some-args argument and move the positional ARG to the end.
But then the second parser sees

  my_program  --some-args --no-args ARG

and tries to pass "--no-args" as the value to "--some-args". Much
confusion ensues...

Fortunately, we can pass '-' at the start of optstring to disable this
behaviour. The result is harder to parse if you're interested in
positional arguments (which is why this isn't the default behaviour)
but works when you have multiple parsers that have to place nicely
together.

Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

---
## [sysad-001/sysad-001](https://github.com/sysad-001/sysad-001)@[be0f5551bc...](https://github.com/sysad-001/sysad-001/commit/be0f5551bc954ad7caaaafad4175e94eafb96938)
#### Wednesday 2022-03-16 15:16:40 by sysad-001

Add files via upload

this shit sucks  its kinda funny. i could make it better but EH.

---
## [Salanto/webAO](https://github.com/Salanto/webAO)@[6a85cb575d...](https://github.com/Salanto/webAO/commit/6a85cb575dd37a6ea01233ed148effcf0f6590d4)
#### Wednesday 2022-03-16 15:26:22 by stonedDiscord

use the fucked up and instead of & for offsets

FUCK YOU WHOEVER DID THIS

---
## [RevolutionPi/linux](https://github.com/RevolutionPi/linux)@[194f7e9c8f...](https://github.com/RevolutionPi/linux/commit/194f7e9c8f4a5590170ae4537ebadc30d98ba1c2)
#### Wednesday 2022-03-16 15:39:44 by Vladimir Oltean

net: dsa: be compatible with masters which unregister on shutdown

[ Upstream commit 0650bf52b31ff35dc6430fc2e37969c36baba724 ]

Lino reports that on his system with bcmgenet as DSA master and KSZ9897
as a switch, rebooting or shutting down never works properly.

What does the bcmgenet driver have special to trigger this, that other
DSA masters do not? It has an implementation of ->shutdown which simply
calls its ->remove implementation. Otherwise said, it unregisters its
network interface on shutdown.

This message can be seen in a loop, and it hangs the reboot process there:

unregister_netdevice: waiting for eth0 to become free. Usage count = 3

So why 3?

A usage count of 1 is normal for a registered network interface, and any
virtual interface which links itself as an upper of that will increment
it via dev_hold. In the case of DSA, this is the call path:

dsa_slave_create
-> netdev_upper_dev_link
   -> __netdev_upper_dev_link
      -> __netdev_adjacent_dev_insert
         -> dev_hold

So a DSA switch with 3 interfaces will result in a usage count elevated
by two, and netdev_wait_allrefs will wait until they have gone away.

Other stacked interfaces, like VLAN, watch NETDEV_UNREGISTER events and
delete themselves, but DSA cannot just vanish and go poof, at most it
can unbind itself from the switch devices, but that must happen strictly
earlier compared to when the DSA master unregisters its net_device, so
reacting on the NETDEV_UNREGISTER event is way too late.

It seems that it is a pretty established pattern to have a driver's
->shutdown hook redirect to its ->remove hook, so the same code is
executed regardless of whether the driver is unbound from the device, or
the system is just shutting down. As Florian puts it, it is quite a big
hammer for bcmgenet to unregister its net_device during shutdown, but
having a common code path with the driver unbind helps ensure it is well
tested.

So DSA, for better or for worse, has to live with that and engage in an
arms race of implementing the ->shutdown hook too, from all individual
drivers, and do something sane when paired with masters that unregister
their net_device there. The only sane thing to do, of course, is to
unlink from the master.

However, complications arise really quickly.

The pattern of redirecting ->shutdown to ->remove is not unique to
bcmgenet or even to net_device drivers. In fact, SPI controllers do it
too (see dspi_shutdown -> dspi_remove), and presumably, I2C controllers
and MDIO controllers do it too (this is something I have not researched
too deeply, but even if this is not the case today, it is certainly
plausible to happen in the future, and must be taken into consideration).

Since DSA switches might be SPI devices, I2C devices, MDIO devices, the
insane implication is that for the exact same DSA switch device, we
might have both ->shutdown and ->remove getting called.

So we need to do something with that insane environment. The pattern
I've come up with is "if this, then not that", so if either ->shutdown
or ->remove gets called, we set the device's drvdata to NULL, and in the
other hook, we check whether the drvdata is NULL and just do nothing.
This is probably not necessary for platform devices, just for devices on
buses, but I would really insist for consistency among drivers, because
when code is copy-pasted, it is not always copy-pasted from the best
sources.

So depending on whether the DSA switch's ->remove or ->shutdown will get
called first, we cannot really guarantee even for the same driver if
rebooting will result in the same code path on all platforms. But
nonetheless, we need to do something minimally reasonable on ->shutdown
too to fix the bug. Of course, the ->remove will do more (a full
teardown of the tree, with all data structures freed, and this is why
the bug was not caught for so long). The new ->shutdown method is kept
separate from dsa_unregister_switch not because we couldn't have
unregistered the switch, but simply in the interest of doing something
quick and to the point.

The big question is: does the DSA switch's ->shutdown get called earlier
than the DSA master's ->shutdown? If not, there is still a risk that we
might still trigger the WARN_ON in unregister_netdevice that says we are
attempting to unregister a net_device which has uppers. That's no good.
Although the reference to the master net_device won't physically go away
even if DSA's ->shutdown comes afterwards, remember we have a dev_hold
on it.

The answer to that question lies in this comment above device_link_add:

 * A side effect of the link creation is re-ordering of dpm_list and the
 * devices_kset list by moving the consumer device and all devices depending
 * on it to the ends of these lists (that does not happen to devices that have
 * not been registered when this function is called).

so the fact that DSA uses device_link_add towards its master is not
exactly for nothing. device_shutdown() walks devices_kset from the back,
so this is our guarantee that DSA's shutdown happens before the master's
shutdown.

Fixes: 2f1e8ea726e9 ("net: dsa: link interfaces with the DSA master to get rid of lockdep warnings")
Link: https://lore.kernel.org/netdev/20210909095324.12978-1-LinoSanfilippo@gmx.de/
Reported-by: Lino Sanfilippo <LinoSanfilippo@gmx.de>
Signed-off-by: Vladimir Oltean <vladimir.oltean@nxp.com>
Tested-by: Andrew Lunn <andrew@lunn.ch>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: Philipp Rosenberger <p.rosenberger@kunbus.com>

---
## [Gman-HLA-sbox-modder/shitter](https://github.com/Gman-HLA-sbox-modder/shitter)@[4d41c47103...](https://github.com/Gman-HLA-sbox-modder/shitter/commit/4d41c471034e58a907c8e6b2c4a2c962c6849512)
#### Wednesday 2022-03-16 16:29:42 by ian

Shitter 3 Is finally fucking ready to be made lets goooooo (kinda want to test if that one twitter bot works lol))

---
## [Dragon-Seeker/ConsistencyPlus](https://github.com/Dragon-Seeker/ConsistencyPlus)@[79b91cba15...](https://github.com/Dragon-Seeker/ConsistencyPlus/commit/79b91cba15e90c970ad5c9b67cbbc45306fbdbdc)
#### Wednesday 2022-03-16 18:05:37 by Dragon-Seeker

Update to 1.18.2

I hate my life

Disable the wthit plugin to run the forge datagen... Idk why it breaks but who cares

---
## [SilverCelestine/BoH-Celestine](https://github.com/SilverCelestine/BoH-Celestine)@[4c2f15f287...](https://github.com/SilverCelestine/BoH-Celestine/commit/4c2f15f2878ae22583fe06fd0fe40ad609e69cb4)
#### Wednesday 2022-03-16 18:16:21 by SilverCelestine

Tiro Update

Re-Adjusts Tiro skills yet again...

Adds some basic skills that Tiro's should all have. Balancing them under Alates and between other off ship roles.

Allows prommies to be tiros again because fuck you.

---
## [openSUSE/systemd](https://github.com/openSUSE/systemd)@[0863a55ae9...](https://github.com/openSUSE/systemd/commit/0863a55ae95fe6bf7312b7a864d07a9e3fbee563)
#### Wednesday 2022-03-16 18:20:49 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>
(cherry picked from commit de90700f36f2126528f7ce92df0b5b5d5e277558)
(cherry picked from commit 367041af816d48d4852140f98fd0ba78ed83f9e4)

---
## [howlieT/crosswordedlovers](https://github.com/howlieT/crosswordedlovers)@[4662bf0b37...](https://github.com/howlieT/crosswordedlovers/commit/4662bf0b373fd8a16a4c129875d05b1dc0f91ff2)
#### Wednesday 2022-03-16 18:43:36 by Misha

Main variation 1

from Rooms import Room

from Items import Item

from time import sleep



# Kitchen

kitchen = Room("kitchen")

kitchen.set_description("""

The Kitchen

-----------------------------

A small bright room, there is a cooker beside the door, 

and a sink under one window, opposite the door a second window overlooks the garden.

Everything is bright and light, the linoleum is yellow, the cupboards are cream,

the trims are blue""")





# Things in the Kitchen



# White Goods, sort of

kettle = Item("kettle")

kettle.set_description("A cream coloured electric kettle, useful for boiling water")



cooker = Item("cooker")

cooker.set_description("A white gas cooker with 4 rings on the hob and a grill at the top. Good for cooking on.")



# Cutlery, plates etc

mug = Item("mug")

mug.set_description("A mug for drinking out of, it commemorates the death of Princess Diana")



plate = Item("plate")

plate.set_description("A white ceramic plate with a blue rim, slightly chipped")



knife = Item("Knife")

knife.set_description("A table knife, good for spreading, less good for stabbing")



fork = Item("fork")

fork.set_description("An ordinary fork, for eating with, or in a pinch for whisking")



tea_spoon = Item("tea spoon")

tea_spoon.set_description("A spoon for small jobs, like fishing tea bags out of a mug")



spoon = Item("spoon")

spoon.set_description("A regular desert spoon, the sort you might eat cereal with.")



# Pen and Paper

newspaper = Item("newspaper")

newspaper.set_description("""

A newspaper, headlines on the front, sports on the back, mostly news in the middle,

the crossword is near the end""")



biro = Item("biro")

biro.set_description("A useful pen for making notes, or doing the crossword with. Mightier than a sword?")



# Fridge and Contents

fridge = Item("fridge")

fridge.set_description("""

A cold storage for the kind of things you keep in a kitchen. Milk, some orange juice, some cheese, 

half a jar of strawberry jam of unknown origin, some mustard that might possible predate decimal currency.""")



milk = Item("milk")

milk.set_description("A bottle of milk, half full. Or half empty, depending on how you think")



jam = Item("jam")

jam.set_description("Half a jar of strawberry jam, provenance unknown")



mustard = Item("mustard")

mustard.set_description("""

The remains of some very old mustard, a very lurid shade of yellow. 

Smells firey, like it might take your nose hairs""")



cheese = Item("cheese")

cheese.set_description("Some regular yellow cheese, a small bit. The kind mice are supposed to like. A good snack.")



# Furniture

kitchen_table = Item("kitchen table")

kitchen_table.set_description("A small wooden table with painted white legs and top")



kitchen_chair = Item("kitchen chair")

kitchen_chair.set_description(" A painted white chair with a yellow seat cushion. One of a pair.")



kitchen_window = Item("kitchen window")

kitchen_window.set_description("A window, you can see the garden out of it.")



# Bedroom

bedroom = Room("bedroom")

bedroom.set_description("""

The Bedroom 

----------------------------

The walls are blue, there is a table with a lamp on it on either side of

the bed on the east wall. On one side, there is a small stack of books and an alarm clock. 

The furniture is pine, the curtains are darker blue and match the carpet.

There is a pine chest  of drawers against the west wall.

""")



# Things in the Bedroom

# Furniture

bed = Item("bed")

bed.set_description("An orange pine frame double bed, the coverlet and pillows are blue")



side_table_books = Item("side table with books on")

side_table_books.set_description("A side table with a small stack of books on")



side_table_empty = Item("side table without books on")

side_table_empty.set_description("A side table with nothing on it, no one uses this side of the bed regularly")



chest_of_drawers = Item("chest of drawers")

chest_of_drawers.set_description("A chest of five drawers, orange pine. For storing clothes in. A hairbrush is on top.")



curtains = Item("curtains")

curtains.set_description("Dark blue curtains to keep the daylight out")



bedroom_window = Item("bedroom window")

bedroom_window.set_description("A window, you can see the garden out of it.")

# Small Objects

alarm_clock = Item("alarm clock")

alarm_clock.set_description("""

A small battery powered alarmclock, silver, with what looks like glow in the dark paint on the hands.""")



table_lamp = Item("lamp")

table_lamp.set_description("A side lamp for reading by in bed")



top_book = Item("top book")

top_book.set_description("The top book in the stack, its not written in a recognisable language")



second_book = Item("second book")

second_book.set_description("""

A copy of Charles Dickens Great Expectations, there's a bookmark two thirds of the way through""")



bottom_book = Item("bottom_book")

bottom_book.set_description("A copy of War and Peace, but it doesn't look like it's ever been opened.")



hairbrush = Item("hairbrush")

hairbrush.set_description("A black plastic hairbrush with white spikes. For brushing hair.")



# Clothes

pyjamas = Item("pyjamas")

pyjamas.set_description("Pyjamas, for sleeping in.")



underwear = Item("underwear")

underwear.set_description("""

It's what you wear under your clothes. You could go without it, but that sort of thing tends to be frowned upon.""")



shirt = Item("shirt")

shirt.set_description("A clean shirt to wear, it's pale blue, that's nice")



trousers = Item("trousers")

trousers.set_description("Clean trousers to wear, they're dark green")



jumper = Item("jumper")

jumper.set_description("A nice navy blue jumper that someone knitted, it smells very faintly of lemons.")



# Hall

hall = Room("hall")

hall.set_description("""

The Hall

------------------------------

There is not much natural light in here. Some comes through the glass panels

in the front door. There is a coat stand on the east wall, there is a key hook 

on the west wall. At the southern end you can see the kitchen. A door on the east wall leads to the bedroom,

a door on the west wall leads to the bathroom.

""")



# Things in the Hall

coat_stand_dict = {"look": """

A wooden stand for hanging coats on, maybe hats and scarves too. You can put umbrellas in the base

""", "use" : " You hang your jacket on the coat stand"}



coat_stand = Item("coat stand", coat_stand_dict)

# coat_stand.set_description({"look": """

# A wooden stand for hanging coats on, maybe hats and scarves too. You can put umbrellas in the base

# """, "use" : " You hang your jacket on the coat stand"})





key_hook = Item("key hook")

key_hook.set_description("Hooks for hanging keys on, there's a spare set here for the front door.")



door_mat = Item("door mat")

door_mat.set_description("A scratchy brown mat for getting the dirt off your shoes when you come in")



# Bathroom

bathroom = Room("bathroom")

bathroom.set_description("""

The Bathroom

--------------------------

This room is white. There is a toilet and a sink and a bathtub with a shower. 

The shower curtain is also white, and is slightly mouldy at the base. The glass 

in the window is frosted. There is a mirrored cabinet above the sink. There is

a towel on the radiator.

""")



# Things in the Bathroom

# Fixtures and Fittings

bathtub = Item("bathtub")

bathtub.set_description("A regular white ceramic bathtub, the sort with silver handles in the sides to help you stand")



shower_curtain = Item("shower curtain")

shower_curtain.set_description("A white shower curtain to keep the water inside the tub, slightly mouldy.")



sink = Item("sink")

sink.set_description("A white ceramic sink for washing your hands and brushing your teeth, that sort of thing.")



toilet = Item("toilet")

toilet.set_description("A toilet, white with a plastic seat. Could probably use a scrub.")



mirrored_cabinet = Item("mirrored cabinet")

mirrored_cabinet.set_description("A mirrored cabinet for storing things in, look into it and see your reflection")



bathroom_window = Item("bathroom window")

bathroom_window.set_description("A frosted window, you can't see out of it.")



# In the Cabinet

tooth_mug = Item("tooth mug")

tooth_mug.set_description("""

A slightly chipped tooth mug, white ceramic with a blue rim, looks like it matches the kitchen plate""")



toothbrush = Item("toothbrush")

toothbrush.set_description("A nice green toothbrush, to brush yur teeth with")



toothpaste = Item("toothpaste")

toothpaste.set_description("Mint flavoured toothpaste, the kind with coloured stripes in")



floss = Item("floss")

floss.set_description("A tub of floss, for flossing your teeth")



hair_gel = Item("hair gel")

hair_gel.set_description("A tub of hair gel, slightly sticky, for styling")



deodorant = Item("deodorant")

deodorant.set_description("A stick of roll on deodorant, for making yourself smell less")



# Garden

garden = Room("garden")

garden.set_description("""

The Garden

-----------------------

A smallish, squarish sort of a garden on the southern side of the house but only accessible from the front. 

There is a tree at the end,

the lawn looks to be in need of mowing. There are beds of flowers up both sides which buzz lazily

with bees and other insects. There is a small set of bistro furniture just beside the house.

On the wall behind the tree, a cat snoozes in the sun.

""")



# Garden Items

# Furniture etc

garden_table = Item("garden table")

garden_table.set_description("A metal table in the garden, dark grey, slightly rusty in places, warm from the sun.")



garden_chair = Item("garden chair")

garden_chair.set_description("A metal chair in the garden, one of two, matches the table.")



cat = Item("cat")

cat.set_description("A small black cat, snoozing")



# Plants

tree = Item("tree")

tree.set_description("""

A deciduous tree with lots of bright green foliage, tall and somewhat wizened, 

it appears to be a fruit tree, maybe an apple tree?""")



left_flowers = Item("left hand flower bed")

left_flowers.set_description("""

The left hand flowerbed, a vibrant range of flowers, buzzing with life. Primulas and pansies, some tulips,

there a peach coloured rose brush right at the end""")



right_flowers = Item("right hand flower bed")

right_flowers.set_description("""

The right hand flowerbed, a vibrant range of flowers, buzzing with life. Marigolds and nasturtiums, irises, anemones,

a lobelia explodes onto the grass.""")



# Linking Rooms

hall.link_room(garden, "north")

hall.link_room(kitchen, "south")

hall.link_room(bathroom, "west")

hall.link_room(bedroom, "east")

kitchen.link_room(hall, "north")

bedroom.link_room(hall, "west")

bathroom.link_room(hall, "east")

garden.link_room(hall, "south")



# Linking Items to Rooms

# Kitchen Links

kitchen_table.link_item(kitchen, "use")



# Hall Links

coat_stand.link_item(hall, "use")

key_hook.link_item(hall, "use")



# Movement and Interaction Commands

current_room = hall

current_item = coat_stand



# Command Finder



def command_finder(old_string):

    new_string = ''

    for x in old_string:

        if x == ' ':

            return new_string

        else:

            new_string += x





while True:

    sleep(1)

    print("\n")

    current_room.get_description()

    current_room.get_details()

    command = input("> ")

    command_finder(command)

    if command in ["north", "south", "east", "west"]:

        current_room = current_room.move(command)

    else:

        if command in ["use", "look", "read", "wear", "open", "break", "sit", "spread"]:

            current_item = current_item.use(commamd)



    #    else:

    #       if command == ["talk"]:

    #            if inhabitant is not None:

    #                inhabitant.talk()

    #        else:

    #            print("Who are you talking to?")

---
## [tarikulnayem94/ISTQB-Interview-Questions-and-Answers.](https://github.com/tarikulnayem94/ISTQB-Interview-Questions-and-Answers.)@[80d9e6fb30...](https://github.com/tarikulnayem94/ISTQB-Interview-Questions-and-Answers./commit/80d9e6fb30ced8694b337403fceeea1b83c9639c)
#### Wednesday 2022-03-16 19:03:04 by Tarikul Nayem

ISTQB-Interview-Questions-and-Answers.

ISTQB-FL
ADVANCED TOP INTERVIEW QUESTIONS AND ANSWERS

**1. What is Exploratory Testing?**
Exploratory testing is a hands-on approach in which testers are involved in minimum planning and maximum test execution. The planning involves the creation of a test charter, a short declaration of the scope of a short (1 to 2 hour) time-boxed test effort, the objectives and possible approaches to be used. The test design and test execution activities are performed in parallel typically without formally documenting the test conditions, test cases, or test scripts. This does not mean that other, more formal testing techniques will not be used. For example, the tester may decide to use boundary value analysis but will think through and test the most important boundary values without necessarily writing them down. Some notes will be written during the exploratory-testing session so that a report can be produced afterward.

**2. What is “use case testing”?**
In order to identify and execute the functional requirement of an application from start to finish “use case” is used and the technique used to do this is known as “Use Case Testing.”

**3. What is the difference between the STLC (Software Testing Life Cycle) and SDLC (Software Development Life Cycle)?**
SDLC deals with the development/coding of the software while STLC deals with validation and verification of the software

**4. What is the traceability matrix?**
The relationship between test cases and requirements is shown with the help of a document. This document is known as a traceability matrix.

**5. What is Equivalence partitioning testing?**
Equivalence partitioning testing is a software testing technique that divides the application input test data into each partition at least once of equivalent data from which test cases can be derived. This testing method reduces the time required for software testing.

**6. What are white box testing and list the types of white box testing?**
The white box testing technique involves the selection of test cases based on an analysis of the internal structure (Code coverage, branches coverage, paths coverage, condition coverage, etc.) of a component or system. It is also known as Code-Based testing or Structural testing. Different types of white box testing are
1. Statement Coverage
2. Decision Coverage

**7. In white box testing, what do you verify?**
In white-box testing following steps are verified.
1. Verify the security holes in the code
2. Verify the incomplete or broken paths in the code
4. Verify the flow of structure according to the document specification
5. Verify the expected outputs
6. Verify all conditional loops in the code to check the complete functionality of the application
7. Verify the line by line coding and cover 100% testing

**9. What is black box testing? What are the different black-box testing techniques?**
Black box testing is the software testing method that is used to test the software without knowing the internal structure of the code or program. This testing is usually done to check the functionality of an application. The different black box testing techniques are
1. Equivalence Partitioning
2. Boundary value analysis
3. Cause-effect graphing

**10. What is the difference between static and dynamic testing?**
Static testing: During the Static testing method, the code is not executed, and it is performed using the software documentation. Dynamic testing: To perform this testing the code is required to be in an executable form.

**11. What are verification and validation?**
Verification is a process of evaluating software at the development phase. It helps you to decide whether the product of a given application satisfies the specified requirements. Validation is the process of evaluating software after the development process and checking whether it meets the customer requirements.

**12. What are the different test levels?**
There are four test levels
1. Unit/component/program/module testing
2. Integration testing
3. System testing
5. Acceptance testing

**13. What is Integration testing?**
Integration testing is a level of software testing process, where individual units of an application are combined and tested. It is usually performed after unit and functional testing.

**14. What do Test Plans consist of?**
Test design, scope, test strategies, approaches are various details that the Test plan document consists of.
1. Test case identifier
2. Scope
3. Features to be tested
4. Features not to be tested
7. Test strategy & Test approach
8. Test deliverables
9. Responsibilities
10. Staffing and training
11. Risk and Contingencies

**15. What is the difference between UAT (User Acceptance Testing) and System testing?**
System Testing: System testing is finding defects when the system undergoes testing as a whole; it is also known as end-to-end testing. In such type of testing, the application suffers from beginning till the end. UAT: User Acceptance Testing (UAT) involves running a product through a
series of specific tests which determine whether the product will meet the needs of its users.

**16. Mention the difference between Data-Driven Testing and Retesting?**
Retesting: It is a process of checking bugs that are actioned by the development team to verify that they are fixed. Data-Driven Testing (DDT): In the data-driven testing process, the application is tested with multiple test data. The application is tested with a different set of values.
**17. What are the valuable steps to resolve issues while testing?**
• Record: Log and handle any problems which have happened
• Report: Report the issues to a higher-level manager
• Control: Define the issue management process

**18. What is the difference between test scenarios, test cases, and test scripts?**
The difference between test scenarios and test cases is that Test scenario: A Test Scenario is any functionality that can be tested. It is
also called Test Condition or Test Possibility.
Test Cases: It is a document that contains the steps that have to be executed; it has been planned earlier.
Test Script: It is written in a programming language and it’s a short program used to test part of the functionality of the software system. In other words, a written set of steps should be performed manually.

**19. What is a Latent defect?**
Latent defect: This defect is an existing defect in the system which does not cause any failure as the exact set of conditions has never been met

**20. What are the two parameters which can be useful to know the quality of test execution?**
To know the quality of test execution, we can use two parameters
• Defect reject ratio
• Defect leakage ratio
Parameters for quality of test execution

**21. What is the function of the software testing tool “phantom”?**
Phantom is freeware and is used for windows GUI automation scripting language. It allows us to take control of windows and functions automatically. It can simulate any combination of keystrokes and mouse clicks as well as menus, lists, and more.

**22. Explain what Test Deliverables are?**
Test Deliverables are a set of documents, tools, and other components that have to be developed and maintained in support of testing. There are different test deliverables at every phase of the software development lifecycle
• Before Testing
• During Testing
• After the Testing

**23. What is mutation testing?**
Mutation testing is a technique to identify if a set of test data or test cases is useful by intentionally introducing various code changes (bugs) and retesting with original test data/ cases to determine if the bugs are detected.

**24. What are all things you should consider before selecting automation tools for the AUT?**
• Technical Feasibility
• Complexity level
• Application stability
• Test data
• Application size
• Re-usability of automated scripts
• Execution across environment

**25. How will you conduct Risk Analysis?**
For the risk analysis following steps need to be implemented
1. Finding the score of the risk
2. Making a profile for the risk
3. Changing the risk properties
4. Deploy the resources of that test risk
5. Making a database of risk

**26. What are the categories of debugging?**
Categories for debugging
1. Brute force debugging
2. Backtracking
3. Cause elimination
4. Program Slicing
5. Fault tree analysis

**27. What is fault-masking explain with example?**
When the presence of one defect hides the presence of another defect in the system, it is known as fault masking. Example: If the “Negative Value” causes a firing of unhandled system exception, the developer will prevent the negative values input. This will resolve the issue and hide the defect of unhandled exception firing.

**28. Explain what Test Plan is? What is the information that should be covered in Test Plan?**
A test plan can be defined as a document describing the scope, approach, resources, and schedule of testing activities and a test plan should cover the following details.
• Test Strategy
• Test Objective
• Exit/Suspension Criteria
• Resource Planning
• Test Deliverables

**29. How can you eliminate the product risk in your project?**
It helps you to eliminate product risk in your project, and there is a simple yet crucial step that can reduce the product risk in your project.
• Investigate the specification documents
• Have discussions about the project with all stakeholders including the developer
• As a real user walk around the website

**30. What is the common risk that leads to project failure?**
The common risk that leads to a project failure are
• Not having enough human resource
• Testing Environment may not be set up properly
• Limited Budget
• Time Limitations

**31. On what basis you can arrive at an estimation for your project?**
To estimate your project, you have to consider the following points
• Divide the whole project into the smallest tasks
• Allocate each task to team members
• Estimate the effort required to complete each task

**32. Explain how you would allocate a task to team members?**
Task Member
• Analyze software requirement specification
• All the members
• Create the test specification • Tester/Test Analyst
• Build up the test environment • Test administrator
• Execute the test cases • Tester, a Testadministrator
• Report defects • Tester

**33. Explain what is testing type and what are the commonly used testing type?**
To get an expected test outcome, a standard procedure is followed which is referred to as Testing Type. Commonly used testing types are
• Unit Testing: Test the smallest code of an application
• API Testing: Testing API created for the application
• Integration Testing: Individual software modules are combined and tested
• System Testing: Complete testing of the system
• Install/Uninstall Testing: Testing done from the point of client/customer view
• Agile Testing: Testing through Agile technique

**34. While monitoring your project what all things do you have to consider?**
The things that have to be taken into consideration are
• Is your project on schedule
• Are you over budget
• Are you working towards the same career goal
• Have you got enough resources
• Are there any warning signs of impending problems
• Is there any pressure from management to complete the project sooner

**35. What are the common mistakes that create issues?**
• Matching resources to wrong projects
• Test manager lack of skills
• Not listening to others
• Poor Scheduling
• Underestimating
• Ignoring the small problems
• Not following the process

**36. What does a typical test report contain? What are the benefits of test reports?**
A test report contains the following things:
• Project Information
• Test Objective
• Test Summary
• Defect The benefits of test reports are:
• Current status of project and quality of product are informed
• If required, stakeholders and customers can take corrective action
• A final document helps to decide whether the product is ready for release

**37. What is test management review and why it is important?**
Management review is also referred to as Software Quality Assurance or SQA. SQA focusses more on the software process rather than the software
work products. It is a set of activities designed to make sure that the project manager follows the standard process. SQA helps the test manager to benchmark the project against the set standards.

**38. What are the best practices for software quality assurance?**
The best practice for an effective SQA implementation is
• Continuous Improvement
• Documentation
• Tool Usage
• Metrics
• Responsibility by team members
• Experienced SQA auditors

**39. When is RTM (Requirement Traceability Matrix) prepared?**
RTM is prepared before test case designing. Requirements should be traceable from review activities.

**40. What is the difference between the Test matrix and the Traceability matrix?**
Test Matrix: Test matrix is used to capture actual quality, effort, the plan, resources and time required to capture all phases of software testing Traceability Matrix: Mapping between test cases and customer requirements is known as Traceability Matrix

**41. In manual testing what are stubs and drivers?**
Both stubs and drivers are part of incremental testing. In incremental testing, there are two approaches namely the bottom-up and the top-down approaches. Drivers are used in bottom-up testing and stub is used for a top-down approach. In order to test the main module, the stub is used, which is a dummy code or program.

**42. What is the step you would follow once you find the defect? Once a defect is found you would follow the step**
a) Recreate the defect
b) Attach the screenshot
c) Log the defect

**43. Explain what is “Test Plan Driven” or “Key Word Driven” method of testing is?**
This technique uses the actual test case document developed by testers using a spreadsheet containing special “key Words”. The keywords control the processing.

**44. What is the DFD (Data Flow Diagram)?**
When a “flow of data” through an information system is graphically represented, then it is known as Data Flow Diagram. It is also used for the
visualization of data processing.

**45. Explain what LCSAJ is?**
LCSAJ stands for ‘linear code sequence and jump.’ It consists of the following three items
a) Start of the linear sequence of executable statements
b) End of the linear sequence
c) The target line to which control flow is transferred at the end of the linear sequence

**47. Explain what N+1 testing is?**
The variation of regression testing is represented as N+1. In this technique, the testing is performed in multiple cycles in which errors found in the test cycle ‘N’ are resolved and re-tested in test cycle N+1. The cycle is repeated unless there are no errors found.

**48. What is Fuzz testing and when it is used?**
Fuzz testing is used to detect security loopholes and coding errors in software. In this technique, random data is added to the system in an attempt to crash the system. If vulnerability persists, a tool called fuzz tester is used to determine potential causes. This technique is more useful for bigger projects but only detects a major fault.

**49. Mention the main advantages of the statement coverage metric of software testing are? The benefit of statement coverage metric is that**
a) It does not require processing source code and can be applied directly to object code
b) Bugs are distributed evenly through the code, due to which percentage of executable statements covered reflects the percentage of faults discovered

**50. How to generate test cases for the “replace a string” method?**
a) If characters in new string > characters in the previous string. None of the characters should get truncated
b) If characters in new string< characters in the previous string. Junk characters should not be added
c) Spaces after and before the string should not be deleted
d) String should be replaced only for the first occurrence of the string

**51. How will you handle a conflict amongst your team members?**
• I will talk individually to each person and note their concerns
• I will find a solution to the common problems raised by team members
• I will hold a team meeting, reveal the solution and ask people to cooperate

**52. Mention what are the categories of defects?**
Mainly there are three defect categories
• Wrong: When a requirement is implemented incorrectly
• Missing: It is a variance from the specification, an indication that a the specification was not implemented or a requirement of the customer is not met
• Extra: A requirement incorporated into the product that was not given by the end customer. It is considered a defect because it is a variance from the existing requirements.


ISTQB-Interview-Questions-and-Answers.

---
## [silont-project/kernel_xiaomi_surya](https://github.com/silont-project/kernel_xiaomi_surya)@[6d9a225aaa...](https://github.com/silont-project/kernel_xiaomi_surya/commit/6d9a225aaa2e4c81644225476152e54fc5bd9043)
#### Wednesday 2022-03-16 19:32:50 by Peter Zijlstra

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
Signed-off-by: azrim <mirzaspc@gmail.com>

---
## [Jalesen/tgstation](https://github.com/Jalesen/tgstation)@[2209c36036...](https://github.com/Jalesen/tgstation/commit/2209c36036c5c0c303443fd4a6304da9384e5107)
#### Wednesday 2022-03-16 20:04:50 by san7890

Fixes Weird Area Definition on DeltaStation (#64986)

So, there I was. Pondering the blobbosity of Auxiliary Base Construction. Deciphering and unclothing the issue in my mind in order to better comphrehend it. I was there for a few moments, until this ugly beast of a fucking area definition caught my eye:

Hideous. Repugnant. I was relishing the thought of dissecting Auxiliary Base Construction into fifteen million more areas (it _will_ lessen obtusities) when that scraggletooth of an utterly mortifying error forced me into a visceral rage: the likes of which have never been experienced on this planet Earth.

---
## [masseyke/elasticsearch](https://github.com/masseyke/elasticsearch)@[37ea6a8255...](https://github.com/masseyke/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Wednesday 2022-03-16 22:13:57 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [vtkhatri/dwm](https://github.com/vtkhatri/dwm)@[67d76bdc68...](https://github.com/vtkhatri/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-03-16 22:16:21 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[8b1ec33143...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/8b1ec331432234f358b26ee1627c10358ccae6a7)
#### Wednesday 2022-03-16 22:29:51 by LeonY24

P90 (#12125)

* P90 SMG

le new gun for new away mission we're planning to make

* Update p90.dm

* includes p90.dm

my fucking retard ass hadnt shit included bruh

---
## [CoolGuyMK/commit-gen](https://github.com/CoolGuyMK/commit-gen)@[98852c2bd6...](https://github.com/CoolGuyMK/commit-gen/commit/98852c2bd66f5bb29376ee25e293d3920f273dd9)
#### Wednesday 2022-03-16 22:38:51 by MK ッ

I'm a barbie girl...

I'm a Barbie girl in the Barbie world Life in plastic, it's fantastic! You can brush my hair, undress me everywhere Imagination, life is your creation I'm a Barbie girl in the Barbie world Life in plastic, it's fantastic! You can brush my hair, undress me everywhere Imagination, life is your creation Come on, Barbie, let's go party! (Ah-ah-ah-yeah)

---
## [LordGenry/configs-tips-tweaks](https://github.com/LordGenry/configs-tips-tweaks)@[fdd027eb09...](https://github.com/LordGenry/configs-tips-tweaks/commit/fdd027eb0948412cbf248c8926a4e7d1a6551818)
#### Wednesday 2022-03-16 22:38:59 by Pavel

Russian-Warship-Go-Fuck-Yourself

русский корабль - іДи наХуй

---

