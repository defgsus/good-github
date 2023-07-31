## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-30](docs/good-messages/2023/2023-07-30.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,858,880 were push events containing 2,612,592 commit messages that amount to 152,514,919 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 59 messages:


## [NotMergot/Bubberstation](https://github.com/NotMergot/Bubberstation)@[a6763aee3e...](https://github.com/NotMergot/Bubberstation/commit/a6763aee3e8ab0c8f42325a75be42adf172a12ad)
#### Sunday 2023-07-30 00:18:54 by BurgerLUA

Hugboxes pierced realities (#281)

## About The Pull Request

- Pierced realities no longer gib your entire head when you click on
them with TK.
- Pierced realities no longer dismember your arms when you click on them
without TK.
- Pierced realities no longer make you want to die when you examine them
(still give drain bamage).

## Justification

New players won't get baited into clicking on the pierced reality. This
is funny, but it's just annoying for medical.
Veteran players won't get baited into clicking on the pierced reality
with TK because they're curious to see what would happen.
The mood debuff is ultimately pointless and no one ever takes it
seriously anyways.

## Changelog

:cl: BurgerBB
del: Hugboxes pierced realities by removing some non-heretic
functionality.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[52c8da7ea4...](https://github.com/Jacquerel/orbstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Sunday 2023-07-30 00:22:56 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[74892ae7ec...](https://github.com/MTandi/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Sunday 2023-07-30 01:18:50 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[63d6c2e962...](https://github.com/MTandi/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Sunday 2023-07-30 01:18:50 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[a8e0d7c8d2...](https://github.com/MTandi/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Sunday 2023-07-30 01:18:50 by MrMelbert

Adds a new positive quirk, "Spacer Born".  (#76809)

## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[063bf74f31...](https://github.com/MTandi/tgstation/commit/063bf74f31a27ec8096fe10b844d5883be6d13a9)
#### Sunday 2023-07-30 01:18:50 by carlarctg

There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

---
## [WolfOrion/cmss13](https://github.com/WolfOrion/cmss13)@[3e9d54628d...](https://github.com/WolfOrion/cmss13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Sunday 2023-07-30 01:41:19 by Ben

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
## [Vincent983/tgstation](https://github.com/Vincent983/tgstation)@[e80cf8f358...](https://github.com/Vincent983/tgstation/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Sunday 2023-07-30 02:38:49 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [tgstation/TerraGov-Marine-Corps](https://github.com/tgstation/TerraGov-Marine-Corps)@[fb4899d20e...](https://github.com/tgstation/TerraGov-Marine-Corps/commit/fb4899d20e990a0a65b8cb5b0ad19b1ef9ab083e)
#### Sunday 2023-07-30 03:19:06 by KM-Catman

Slight redesign of Valhalla Vendors and Chemistry. Adds FC and Synth to Valhalla. (#13612)

* Valhalla Fixes

Start room is now all Hulls, adds a Friend, Materializes the Chaplain's chained demon, and adds more Xeno Huds.

* FC and Synth Added. Slight readjustment.

* Changed the vendor section as per Grayson's request

* Adds three new Warning Stripes.

Adds a FCDR, Synth, and Mech warning stripe. Adds them in front of the prep rooms

* Duct Taped Space

* Removed random bedsheet (Goddamn you hotkeys)

---
## [efzapa/Paradise](https://github.com/efzapa/Paradise)@[a3dc32cf34...](https://github.com/efzapa/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Sunday 2023-07-30 04:08:12 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [Or4cl3AI/SciTouchAI](https://github.com/Or4cl3AI/SciTouchAI)@[2c4d92317c...](https://github.com/Or4cl3AI/SciTouchAI/commit/2c4d92317c29bb078c5b269c061f2ef3be339abc)
#### Sunday 2023-07-30 04:53:54 by Dustin Groves

Merge pull request #2 from Or4cl3AI/pr/smol-dev/aoda_u

Mobile app for scientists to analyze scientific data using AI, ML, and data science, optimized for mobile devices with a user-friendly interface, cybersecurity protocols, and visually stunning design.

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[a14ef07eb6...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/a14ef07eb69a49feeae9c331609adc393f861b5b)
#### Sunday 2023-07-30 05:00:14 by Nut2

Triumph central command floor fix (#5741)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
I MISSED TWO FUCKING TILES
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I MISSED TWO TILES GOD DAMNIT
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

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[2ee79d7077...](https://github.com/lessthnthree/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Sunday 2023-07-30 05:28:17 by Jacquerel

Bots no longer require PAIs to become sapient (#76691)

## About The Pull Request

We were talking in the coder channel about what the role of a pAI is,
with a general conclusion that as the name would suggest they should be
_personal assistants_.
This means they should be sticking around their owner, not wandering
away as a holochassis or in the body of a bot.
The former is a matter for a future PR, the latter I am addressing here.

What we also discussed is that clearly some people _want_ to respawn as
a weird quasi-useless mob which wanders aimlessly around the station.
That seems like a fine thing to exist, but it shouldn't be a pAI.

Resultingly: pAI cards can no longer be placed inside bots.
However, you also no longer need to place pAI cards inside bots in order
for them to become sapient, it's a simple toggle on the bot control
menu. Enabling this option will poll ghosts
Toggling the "personality matrix" off while a bot is being controlled by
a ghost will ghost them again, so if they're annoying they're not that
hard to get rid of.


![image](https://github.com/tgstation/tgstation/assets/7483112/ec14c2f2-3c0f-4f03-9dfc-22abca00a477)

Mobs which couldn't have a pAI inserted don't have this option.
Specifically securitrons, ED-209, and Hygienebots (for some reason).

Perhaps most controversially, any bots which are present on the station
when the map loads will have this setting enabled by default. We will
see if players abuse this too much and need their toys taken away, I am
hoping they can be trusted.

Additionally, as part of this change, mobs you can possess now appear in
the spawners menu.

![image](https://github.com/tgstation/tgstation/assets/7483112/7c505471-43de-4e4e-89a5-877dc3086684)
Here is an unusually populated example.

Oh also in the process of doing this I turned the regal rat "click this
to become it" behaviour into a component because it seems generally
useful.

## Why It's Good For The Game

Minor stuff for dead players to do if they want to interact with living
players instead of observe.
Shift pAI back into a more intended role as a personal assistant who
hangs around with their owner, rather than just a generic respawn role.

## Changelog

:cl:
add: PAIs can no longer be inserted into Bots
add: Bots can now have their sapience toggled by anyone with access to
their settings panel
add: Bots which exist on the map at the start of the round automatically
have this setting enabled
qol: Bots, Regal Rats, and Cargorilla now appear in the Spawners menu if
you are dead
qol: Bots can be renamed from their maintenance panel
/:cl:

---
## [ZephyrTFA/Shiptest](https://github.com/ZephyrTFA/Shiptest)@[9aa3fb2901...](https://github.com/ZephyrTFA/Shiptest/commit/9aa3fb29012991ce7a9d755e640a1af65f3fe319)
#### Sunday 2023-07-30 06:36:11 by thgvr

Fixes a good chunk of Vox sprites. Removes environmental regulator (#2092)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Oh god the pain. Oh god. The unbearable pain. Why.

Adds a ton of unused vox sprites from Drawsstuff.
Cleans up the files for sprites we don't actually have
Ensures they are pathed correctly, with flags set correctly.
I spent five hours on this in one sitting after being upset at shitty
vox mechanics/sprite support again. They're cool and unique and it was
sad.
Removes the Environmental Regulator.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Vox sprites were incomplete. This completes them a little bit more.
2. The environmental regulator isn't fun. This will remove the regulator
and vox needing to use it. It was buggy, poorly made, and just not fun
even when it worked correctly. Vox aren't nearly strong enough to be
constantly crippled.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A metric ton of Vox sprites
del: Vox no longer need environmental regulators
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ZephyrTFA/Shiptest](https://github.com/ZephyrTFA/Shiptest)@[c84e40255d...](https://github.com/ZephyrTFA/Shiptest/commit/c84e40255d466e37983e5cb03c110e7dd8ab90c8)
#### Sunday 2023-07-30 06:36:11 by Imaginos16

Ports pinging in Adminsay from /tg/station (#2111)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says on the tin, porting a behavior that allows you to ping
a person in admin say by just doing @(ckey) from /tg/station in PR
[#61712](https://github.com/tgstation/tgstation/pull/61712)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/fc756e0f-668f-4641-9bcd-689d6548d343)

Oh and this PR I guess fixes a hilarious issue where **someone** wrote
'tgstation.dme' instead of 'shiptest.dme' where they shouldn't have.
Whoops!

Most cool of all, which was completely unintentional by me, ports Datum
linking (partially), as well as Ticket linking, respectively added in
PRs [#65154](https://github.com/tgstation/tgstation/pull/65154) and
[#65634](https://github.com/tgstation/tgstation/pull/65634)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/d6f980ee-c490-4f8d-a76c-81447aeb7658)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I swear to fucking christ if I have to log into the game one more
goddamn time as an admin only to have 2 people being DJs, another one
spriting, and another one doing jack shit while not paying attention at
the server when I am trying to solve a crucial ticket, I'll develop an
aneurysm.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Ryll-Ryll/Shaps
admin: Adds pinging to adminsay!
admin: Adds the ability to link datums!
admin: Adds linking tickets to asay! Simply put a # followed by a ticket
number for it to be linked in the chat!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [tvrusso/Xastir](https://github.com/tvrusso/Xastir)@[00ce2b8876...](https://github.com/tvrusso/Xastir/commit/00ce2b8876b581e3bdda1786964d43408cf17cbc)
#### Sunday 2023-07-30 08:30:18 by Tom Russo

Mess around with the "INSTALL" file a bit

INSTALL is what we tell users to look at in the README.md file to get
Xastir built.

Honestly, I don't think this document is fit for the average new user,
as it looks an awful like a compilation of random thoughts taken out
of a decade or so of miscellaneous user support emails from the
mailing list, bouncing between a general "here's how to build" to an
in-depth description of the interplay between various libraries and
the features they enable, followed by a set of "First install"
instructions that include telling users to build a bunch of dependent
libraries from source, with all manner of side excursions into
optional features.  It is very much a creature of the early 2000s,
when almost every library we use was a niche item that appeared in no
package managers.  It could use a complete rewrite.

I have not completely rewritten it.

I have added some text at the top to point potential users to the
Wiki's "Installation Notes" for system-specific guidance, almost all
of which may be more helpful than either the general, vague guidance
in this file or the detailed "drink from the firehose" stuff that
follows it.

I also removed several references to configure options that no longer
exist, rearranged the lists of libraries so one can tell the
difference between what is absolutely needed before proceeding with
the general guidance at the beginning and what is optional.

And finally, I put a dividing line between the general guidance and
the stuff I feel is too much information for a first-time install, or
which may very well be completely outdated (like, telling folks where
to download libgeotiff source and how to compile proj libraries).

---
## [Sagnac/streamsave](https://github.com/Sagnac/streamsave)@[69b2066649...](https://github.com/Sagnac/streamsave/commit/69b2066649a7193c7deb7eb5fc60464ca8aa51b7)
#### Sunday 2023-07-30 09:38:48 by Sagnac

Redesign how options are updated

The previous scheme was pretty ugly. This is due for a much more
comprehensive rewrite as there's quite a bit of redundancy with the
script-message functions and maintaining both script-opts and
script-message updates requires more effort. But that will have to come
at a later time.

One alternative approach would be to hook into the current override
functions by using them as fields in the update table and have them
perform double duty, but this may prove more trouble than it's worth.

As a user, the script-message approach to changing options is more
convenient to use during runtime either with keybinds or through the
console. Also, it supports more arguments (e.g. cycle, on_demand) and
provides status messages. That being said, with script-opts you can send
an entire list of options to be updated instead of having to chain
script-message commands. The names being used for this also differ
between the two methods, with the script-message names being shorter and
likely easier to remember, but the inconsistency in naming between the
options and the runtime commands could be an issue.

Of course I could just turn off the script-opt updating mechanism by
not using update_opts, which I probably should do, but I'm going to keep
this around for now while I trim the script down to a lite version at a
separate branch; this will prove useful there as script-opts becomes the
desired minimalistic approach.

Another thing to note with regards to removing on_update handling of the
options is that some options such as the likely widely used
force_extension option would still require support in that regard, as
the runtime command is simply an on-demand single-stream change and a
revert handler, and does not in actuality set the format in a global
manner - if a new stream is loaded then it will take on the
automatically determined format.

---
## [TeamOctolings/Boyfriend](https://github.com/TeamOctolings/Boyfriend)@[940f2e64a0...](https://github.com/TeamOctolings/Boyfriend/commit/940f2e64a0bf065acf07add976e27a61daef730d)
#### Sunday 2023-07-30 09:45:11 by Macintosh II

Add soundtracks from different games (#74)

This PR adds some soundtracks from five different games to the bot's
listening activity.

List of soundtracks added:
- Jukio Kallio, Daniel Hagström - Fall 'n' Roll (Fall Guys)
- SCATTLE - Hypertension (Super Meat Boy)
- KEYGEN CHURCH - Tenebre Rosso Sangue (ULTRAKILL)
- Chipzel - Swing Me Another 6 (Dicey Dungeons)
- ~Floex - The Glasshouse With Butterfly (Machinarium)~
- Noisecream - Mist of Rage (My Friend Pedro)

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[7e1d97af9e...](https://github.com/psychonaut-station/PsychonautStation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Sunday 2023-07-30 10:00:59 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[cfd40aeef5...](https://github.com/Sealed101/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Sunday 2023-07-30 10:03:25 by necromanceranne

Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#76771)

## About The Pull Request

This is a followup on my previous PR involving cargo imports. I've made
a number of changes and new additions to cargo's imports and contraband.
But I've also changed how Smuggler's Satchels generate loot as well.

### New:
**Abandoned Crates:** You can now order in abandoned crates at a steep
price. Obviously these are just your standard fare abandoned crates, so
they've got a pretty long list of potential contents. Some great, some
utterly not worth the price you paid for the crate. Since they're quite
pricey, you can't order very many quickly. But this does allow cargo
techs the opportunity to spend the round solving puzzles to get
interesting loot.

**Dumpster of Maint Garbage:** This dumpster (similarly named to another
dumpster you can order) is filled with maint trash and potential maint
random spawns. This list is extensive enough that anything spawned in
this crate is likely to be mostly garbage. But, it is more affordable
than abandoned crates. I'd consider this the literally trashier version
of the abandoned crate.

**Shamber's Juice Eldritch Energy! Crate:** A crate with one can of the
extremely rare, short run edition of Shambler's Juice, Eldritch Energy!
This contains 5 units of eldritch essence. Heals heretics, hurts
everyone else! This is a VERY potent poison, but it also happens to be a
handy way for a Cargonian heretic to get a potent healing item without
having to waste knowledge points.

**Animal Hide Crate:** It's a cargo crate full of animal hides! This can
include fairly rare hides and some icebox creature hides as well, like
polar bear hides and wolf sinew. It's not too expensive, and mostly
spits out leather.

**Dreadnog Carton Crate:** A carton full of the worst eggnog imaginable.
This is just something to troll people with. Drink it and you'll get a
massive mood penalty. Dreadnog! May or may not contain space cola!

### Updated:

**Contraband Crate and Smuggler's Satchels:** This has had it's price
increased considerably. But, for good reason. It now contains some more
controlled random items, but also some more valuable contraband as well
as a very rare spawn. The upper end on his contraband can be extremely
valuable, but the majority of the items gained from contraband crates
will probably be either what you can get now (quite weak), or something
a bit more middle of the road (some more unique narcotics).

As a consequence, I've also passed this change onto smuggler's satchels,
as they used the crate to generate its contents. (it literally spawned
and then deleted a contraband crate to generate the contents hoo haa).

I've also increased the number of items in the smuggler's satchel. Since
the randomly spawned smuggler's satchels are quite a bit rarer now there
is only ever two spawned in the map, and spending actual TC on these is
somewhat counterproductive, I don't imagine this will be more beneficial
for scavenger hunters hoping for some interesting goodies.

**Russian Crate (the normal one):** The mosins now spawn in ancient gun
cases. These determine what kind of mosin you can get. 79% of the time,
you get the crap mosin. 20% of the time, you get a good mosin. And 1% of
the time, you get rations. This more tightly controls how many good
mosins are entering into the round and how much of a value purchase the
Russian crate actually is for getting ballistics. Since the process is
even more unlikely than before, it isn't necessarily as guaranteed that
you will get a good mosin. Hell, you might not even get a gun if you're
that unlucky.

**Shocktrooper Crate:** It now has an armor vest and helmet. So, not
only do you get some grenades, you get some protection as well. Since
this is the 'loud' crate, I felt it appropriate to make it slightly more
useful for enabling that.

**Special Ops Crate:** It now contains five mirage grenades and a
chameleon belt, and has had the survival knife improved to a
switchblade. This is probably the weakest of the two crates STILL, but
hopefully these make them a little more interesting and novel by giving
them pretty fun grenade to toy with.

## Why It's Good For The Game

My initial PR hoped to add in a few more interesting purchases for
cargo. I think currently cargo has a slight issue of not having enough
valuable or interesting uses for their money. I think it still has that
problem, but by including more unique crates that allow cargo to provide
some oddities into the round, that might slowly work itself out.

This PR hopes to provide another way to waste their money if they have
an excess amount. Landfill Trash Gambling. Spending it away on complete
junk, which I think is absolutely hilarious when it doesn't work out, as
it is soulful in its design. Definitely not inspired by my recent thrift
shop excursions this month buying and scrounging for furniture and
interesting clothing.

[Relevant](https://www.youtube.com/watch?v=QK8mJJJvaes)

Also, I wanted to buff some of the crates I introduced a bit last time,
and nerf the mosin production somewhat via a more controllable method
that I can actually adjust as necessary down the line.

## Changelog
:cl:
fix: Stops manifest generation runtiming when a cargo crate is empty.
add: Abandoned crates are now available via cargo imports.
add: Dumpsters full of maintenance trash are now available via cargo
imports.
add: An ultra-rare can of Shambler's Juice is now available via cargo
imports.
add: Animal hides and leathers can be (unreliably) ordered via cargo
imports.
add: The Dreadnog has entered this realm. To consume, purchase it via
cargo imports.
balance: Contraband Crates (and as a consequence, smuggler's satchels)
now generate more varied goods. Mostly the same, but sometimes you get
something quite different or even valuable.
balance: Mosins generated via the Russian supply crate are a bit more
random, weighing more heavily towards bad mosins than good mosins.
balance: Buffed both the shocktrooper and special op crate. Shocktrooper
now has an armored helmet and vest, and special op now has 5 mirage
grenades and a chameleon belt. The survival knife in the special op
crate is now a switchblade.
/:cl:

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[f5784dabc7...](https://github.com/cmss13-devs/cmss13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Sunday 2023-07-30 10:27:47 by ihatethisengine

More portable cades tweaks and buffs (#3967)

# About the pull request

Despite making a lot of tweaks and changes to portable cades I barely
touched them in the game until recently. Now I have more experience and
can tweak it again.

1) You can now stack damaged cades and stack stores health of each cade.
You can repair stacked cades but it will take longer time.

2) Miniengi pamphlet allows faster repairs but only when cade is folded.

3) You can quickly collapse portable cades with crowbar if you have at
least miniengi skills.

4) You no longer need to have folded portable cade in hand in order to
repair it, but if you do, you can move while repairing.

# Explain why it's good for the game

1) It's extremely annoying to repair each individual cade in order to
stack them just because it got hit by a stray bullet once. Now you can
just ignore damage and keep going.

2) Yeah it took 10 second for PFC to repair each single cade. Really
long. Now it's 5 seconds, but only when folded and if you have miniengi
skills. Makes miniengi pamphlet a bit more relevant.

3) It was intended, but turned out it was a bit inconvenient. It was
faster to collapse by hand because you didn't need to deal with tools.
Now it requires just a crowbar and slightly faster. Also requires
miniengi skill to use crowbar.

4) First was just a bit annoying, second allows more mobility which is
the point of portable barricades.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: you can stack scratched portable cades if their HP at least
75%. Doing so will reduce the health of all barricades in the stack to
the level of the most damaged.
balance: you can repair stacked portable cades but it will take longer
time depending on how many cades in stack.
balance: miniengi skill makes repairs of folded portable cades faster
(10 seconds to 5 seconds, same as engineer).
balance: with engineering skill at least of miniengi you can collapse
deployed portable barricade with a crowbar (wrench is no longer
required, slightly faster (2 sec to 1.5 sec)).
balance: you no longer need to have folded portable cade in hand in
order to repair it.
balance: if you have folded portable cade in hand, you can move while
repairing it.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [yoavelko/BaLiFront](https://github.com/yoavelko/BaLiFront)@[348708e9d3...](https://github.com/yoavelko/BaLiFront/commit/348708e9d3eb0a14f719cb8537930eaf5b9072d1)
#### Sunday 2023-07-30 11:00:45 by Nitay Elzur

Merge pull request #14 from yoavelko/nitayFront

fuck you yoav

---
## [SunshineFluffy/yuzuNK](https://github.com/SunshineFluffy/yuzuNK)@[8e703e08df...](https://github.com/SunshineFluffy/yuzuNK/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Sunday 2023-07-30 11:06:19 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[a1609c4536...](https://github.com/Stalkeros2/Skyrat-tg/commit/a1609c4536fe05f95560bd1a1be4607b944ee5a5)
#### Sunday 2023-07-30 11:20:36 by SkyratBot

[MIRROR] [NO GBP] Fixes clown car + deer collision  [MDB IGNORE] (#22709)

* [NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**

https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

* [NO GBP] Fixes clown car + deer collision

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[4e91d057d7...](https://github.com/Timberpoes/tgstation-nxt/commit/4e91d057d7d627bd8c356a2251195eb579106707)
#### Sunday 2023-07-30 11:44:41 by MrMelbert

Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence


## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

---
## [mikichandrinkingtea/mjg-repo](https://github.com/mikichandrinkingtea/mjg-repo)@[42d6439287...](https://github.com/mikichandrinkingtea/mjg-repo/commit/42d64392878ebb8abfe8eff1efcd6d1b7f9534c8)
#### Sunday 2023-07-30 12:00:07 by mikichandrinkingtea

Revert "Fuck you and your shitty images."

This reverts commit 1be78c2d845e3913935487512f4cd45e1aa5aeab, reversing
changes made to c32909beb412955fff0663d9fc72a6396c352318.

---
## [Lambda-13/rustest](https://github.com/Lambda-13/rustest)@[f07cb3bd3b...](https://github.com/Lambda-13/rustest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Sunday 2023-07-30 12:09:10 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[5e51aaee49...](https://github.com/treckstar/yolo-octo-hipster/commit/5e51aaee4952a634e5c7c6138ca228d7ee6f7135)
#### Sunday 2023-07-30 12:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [du-top/sojourn-station](https://github.com/du-top/sojourn-station)@[94b32aa82c...](https://github.com/du-top/sojourn-station/commit/94b32aa82cdfdf4b9115d178c89e9cd3a7ede6d2)
#### Sunday 2023-07-30 12:48:31 by CDB

Bugfixes. (#4685)

* Bugfixes.

Fixes a few spelling mistakes here and there.

Forged stock-parts boxes claimed they had five parts inside. they did not, they have four, corrected.

Toga for the church had an eronious base-state, unsure who touched it, but fix'd.

Bat'ko had incorrect formatting for its on-suit sprite, fixed.

Numerical garb eroniously claimed to be switchable between grey and red. It was actually purple and red, fixed.

Numerical hats both had the wrong icon name and were using(incorrectly) the old sprites. Fixed.

Duty had a missing icon when loaded with a drum and fempty(Who the FUCK let the duty take drums?)

Fixes the sec-shuttle and also comments out the destination it has towards the space fortress which is...commented back out? Right?

Fixes the apparent sec-shuttle so its walls are properly named after the vessel. To do- give some fucking flavor to the Rocinante and Vasiliy.

* Update body_modifications.dm

Removes the ability to select robo-torsos/groins/heads, this functionality doesn't actually work as intended and wasn't intended to be used in this way. Feel free to re-add if it does get fixed.
fixes #4675

* More bugfixes

Fixes tesla turrets attacking colony bots, SI drones, etc.

Fixes embed chance on the psion knife being greater than 0 and thus being able to embed(and promptly bugging out.)

* Update tesla_turret.dm

Slight tweak to Tesla turret code courtesy of Hex.

* Further bugfixes.

RXbow lacked a proper caliber and could thusly accept 10mm rounds.

RXbow also lacked a casing handling tag, not that it makes a huge difference given its snowflake behavior but it was fixed.  I will suggest to perhaps raise the d amage of the crossbow bolt in another non-bug focused PR.

Artificer rail pistols(slab and myrmidon) didn't have a serial defined, fixed.

* More fixes.

Mop bucket now properly updates its sprite after any change to its reagents takes place.

Kitchen spike no longer erroneously requires a strangle grab instead of a neck_grab.

---
## [zhangjoke/crawl](https://github.com/zhangjoke/crawl)@[1880023187...](https://github.com/zhangjoke/crawl/commit/18800231877e12caceb48c2f929f842d55aac934)
#### Sunday 2023-07-30 12:52:12 by Nicholas Feinberg

Tweak forms

This change is intended to allow more opportunities for players to shift
into or out of a 'transmuter' playstyle, to improve the UI of forms, and to
improve some miscellaneous issues, e.g. Lichform being useless in 3-rune games.
For more context, see https://github.com/crawl/crawl/wiki/Transmutations-Reform.

Throughout, balance is a very rough sketch. I expect many things will need to
be buffed, others will need to be nerfed, and some will need to be replaced
entirely. This is a grand experiment, not a final state.

Talismans
---------

The largest change is that forms are no longer entered via spells. Instead,
special items called 'talismans' must be found and evoked. Once entered,
these 'talisman forms' last indefinitely.

Further notes on talismans:
- Talismans scale only on Shapeshifting skill (more on this later). They
  do not care about Int, Spellcasting, other spell schools, wizardry, or
  encumbrance. (That is, they aren't spells.)
- Talisman forms have a 'minimum skill'. Below that skill, entering the
  talisman form will reduce the user's maximum HP (while in the form).
  This is intended to roughly mimic the inability to effectively cast
  spells at low skills/high fail% - it provides a space in which an 'early'
  form can be better than a 'later' one, even if you've found both.
- Talisman forms have a 'maximum skill'. Above that skill, no further
  scaling applies. This is intended to roughly mimic max spellpower - it
  makes it more obvious that later-game forms will end up outscaling
  earlier ones.
- It takes 5 turns to enter or leave a talisman form, exactly as with
  armour or amulets. Use of a talisman form is intended to be a strategic
  decision, again like wearing armour, rather than something swapped in
  each fight.
- Talismans don't need to be held after they're used. You can evoke them
  from the floor and leave them there. This avoids inventory pressure.
- Talismans can be used with Sacrifice Artifice, since they don't use Evo.
- Zin instantly excommunicates users of a talisman. Take that, nerds!
- Trog is A-OK with talismans, just as with wands, magic swords, etc.

Art for talismans is pending.

Skills
------

Transmutations skill has been split in two. Talismans use a new skill,
Shapeshifting, and remaining Transmutations spells (of which there are
still nine, more than one other school!) continue to use Transmutations
skill. There was very little synergy or overlap between forms and Tmut
spells, and this makes it easier to make skilling decisions. Some argue
that Transmutations should be abolished entirely and its spells punted
into other schools; we'll see.

Shapeshifting aptitudes look broadly like Transmutations aptitudes,
with a -2 penalty applied so that forms are costly enough now that
they're all "single-school" and don't require Int. (That is, Humans
have a Shapeshifting apt of -2, etc.) A few species have had their
apts adjusted to account for the new role of Shapeshifting, but more
could be done here.

Background
----------

The Transmuter background has been replaced with a Shapeshifter, who
starts with a beast talisman and no spells. Their stats have been
adjusted accordingly.

Forms
-----

The following forms exist:

*Beast*: This is the starting form for the Shapeshifter background. It
melds all aux armours in exchange for a Slaying bonus (ala Wereblood) -
+2 at 0 skill, +8 at 13 skill (max).

This is intended to provide a bonus which is compelling early game (when no
or few aux armours have been found) but more tenuous later, especially for
non-transmuters. It's also intended to provide a bridge between Tmut and
weapon use, since a transmuter who finds a great weapon can switch from UC
to that weapon without giving up their form and Tmut training.

Beast form allows use of body armour so that it can present a reasonable
slay-for-AC tradeoff without becoming overly strong for 'dex-based' characters,
who wouldn't mind losing body armour nearly as much.

*Anaconda*: This is a tier 2 form. Anaconda form turns you into a giant
anaconda. All your items meld, you can constrict, you get some AC and an HP
bonus...

This is intended to replace Ice Form, a form to help transmuters transition
into the mid-game. The rF- of Ice Form is less appropriate for early-game
characters who can no longer switch between forms, and Ice Form is not
evocative - no one gets Ice Beasts. On the other hand, turning into a snake...
everyone gets that. That's the dream. Limbs are for dorks. Ssssss

*Maw*: This is a tier 2 form. Maw form melds the body slot, transforming it
into a giant mouth, ala the Brazilian Mapinguari. The maw provides an aux
attack with damage that scales on Shapeshifting skill. It also has the old
Hydra form devour-on-kill-for-hp gimmick, since everyone loved that.

This is intended to be a way that Shapeshifters can transition into the mid-game,
especially transmuters who use weapons. It's probably a bit too strong for
quick blade users at present - perhaps I'll give it +str -dex, or something.
(It may also just be too strong in general - numbers are WIP!)

*Blade*: This is a tier 2 form. It's blade hands. To compensate for it
being easier to enter, its UC damage has gone down slightly (22 -> 18).

It also now gives a deformed body-like AC penalty based on base body armour AC,
scaling from a 100% penalty at min Shapeshifting skill to 0% at max skill.
(That is, at min skill, +2 plate armour will just give you +2 AC, plus whatever
you get from Armour skill.) This is intended to model the dynamic of old Blade
Hands - pure glass cannon when you can only cast it in robes, later on more
usable in actual armour. Your body is deformed because there are blades inside.
Aaiiii!

This is intended to be another way that Shapeshifters can transition into the
mid-game.

*Statue*: This is a tier 3 form. It's statue form. Intended to be a way
for transmuters to head into late-game while still being able to use weapons,
if desired. Might need to be a bit stronger for weapon users.

*Dragon*: This is a tier 3 form. It's dragon form. AC and UC damage now
scale slightly with Tmut skill. Intended to be a way for transmuters to
head into late-game. Possible this should be tier 4 and Storm should be tier
3 - dragons are cool! Dragons should be the best!

*Storm*: This is a tier 4 form. It's storm form. Intended for players who
want to dump ludicrous amount of skill XP into tmut. Top end has been
adjusted somewhat downward.

*Death*: This is a tier 4 form. Replacing Necromutation/Lich Form, Death
Form makes you dead (no drinking potions, holy wrath/dispel undead vuln,
rC, rTorm, rPois, etc) and also gives you an assortment of spicy powers.
On hit (with melee/UC), victims get slowed, weakened, and heavily drained.
There's also a new active, Siphon Essence, which costs 20 (!) MP, halves
the HP of all enemies in radius 2, and heals you based on damage dealt and
Tmut skill. (That works on all non-MH_NONLIVING enemies, as do the debuffs.)

It no longer provides innate AC or Will, nor does it give a necro enhancer.
Its UC damage is now significantly higher, comparable to blade hands,
though still much lower than Statue, Dragon or Storm.

This is intended to be a way for players who want to spend huge skill XP
on tmut to do so, including those who use tmuts + weapons. It's intended
to feel a bit different from other forms while still being competitive in
melee. Other forms have huge base damage - Death Form has lower damage but
very strong debuffs. Other forms have AC (Statue), HP (Dragon) or EV (Storm) -
Death Form gives Siphon Essence as a very powerful survival tool.

Other Notes
-----------

Various books have been merged and consolidated to make up for the
removal of eight spells. It *might* make sense to drop the book generation
rate slightly, but I haven't done this yet.

Some uniques now spawn with talismans. More could be done with this, e.g.
placing talismans of death in Crypt.

Later changes
-------------

Talisman acquirement is a must. TODO.

In the future, artefact talismans (i.e. randarts) could be interesting -
to provide more excitement for rare finds. The randarts would have
the usual panoply of properties (rF+, Dex-2, etc), which would apply
while the player was in the relevant form.

It'd be fun to add more form types, e.g. ones that work well for
'casters'.

Might be interesting to have talismans start unidentified (like staves),
for a frisson of excitement in gauntlets etc.

Possibly Wanderers should get a chance to start with beast talisman?

---
## [ruvn-1fgas/white](https://github.com/ruvn-1fgas/white)@[b80c09c566...](https://github.com/ruvn-1fgas/white/commit/b80c09c566adc9607b577a11ae0bd95580f4bf5c)
#### Sunday 2023-07-30 13:13:02 by Valtos

fuck this hud fuck you jannies fuck everyone fuck fuck fuck fuck

---
## [c3d/DB48X-on-DM42](https://github.com/c3d/DB48X-on-DM42)@[c4c963af7f...](https://github.com/c3d/DB48X-on-DM42/commit/c4c963af7f1e94b54f8a0c83188b41ea5f7c1695)
#### Sunday 2023-07-30 13:31:29 by Christophe de Dinechin

Release 0.4 - Matrices and equation rewrites

New features:
- Equation rewrite engine (#203, #213, #244)
  - Early implementation of `expand` and `collect` (#231)
- Transient alpha mode for quick alppha entry (#204, #215, #233, #237)
  (note that XEQ no longer automatically switches to alpha)
- Vector and array arithmetic (#26, #185, #190)
  - Determinant of square matrices (#187, #217)
  - Inverse of a square matrix (#180, #189, #201)
  - Euclidean norm for matrices and vectors (#188)
  - Component-wise multiplication and division of vectors (#181)
  - Binary operations between matrix / vector and constant (#183)
  - Matrix * vector (#195)
- Automatic simplification in basic operations (#197, #216, #221)
- Help knows how to render "yellow" and "blue" keys
- Contextual tool menu (#127) and contextual help (#162, #193)
- `LastMenu` (xshift-A) goes back in menu history (#165)
- Displaying date and time in the header (#123, #224)
- `GET` function on lists and arrays (#173)
- Concatenation and repetition of lists (#178)
- Apply standard functions to arrays and lists (#179, #182)
- Add limits to size of numbers and number of rewrites (#214)

Improvements:
- Better rendering of unimplemented menu functions (#218)
- Accelerate garbage collector (#219)
- Render polar arguments with explicit angle units (#119, #161)
- Update key layout for easier matrix / vector entry (#198)
- Render complex numbers with additive precedence (#222)

Bugs fixes:
- Fix cursor position for up/down movement (#159)
- Show help for R/S (Eval) and division keys (#157)
- Fix spacing for thousands (e.g 5000) (#137)
- Redraw editor after inserting variable name (#156)
- Draw alpha annunciator after busy cursor is cleared
- Refresh editor when going at beginning or end of text
- Parsing of `Invert(X)` (#163)
- Do not insert parenthese in editor after binary operators (#164)
- Correct parsing of `π` and imaginary unit (#145, #168, #169, #207, #208)
- Repair repeat for R/S as a space key (#199)
- Parsing of complex numbers in matrices (#205)
- Parsing of complex numbers in equations (#220, #224)
- Parsing of "fancy" power sign (#238)
- Computation of power with integer and negative exponent (#239)
- Refresh menu after `NumberSpacing` (#240)

Other:
- Various help file improvements:
  - Help now uses more standard mardown for keys
  - As a result, README.md now points to the built-in help on GitHub (#227)
  - Add acknowledgements to help file (#129), including link to HP Museum
  - Improve documentation of differences between RPL variants (#177, #192)
  - Add documentation for the `Help` command (#228)
  - Fix label for F6 key in help (#230)
  - Improve rendering of code font in help (#232)
- Improved test suite, now faster, more stable and detects more errors
- Fixes / adjustments to keyboard layout suggested by C47 team
- Use standard C++ iterators for programs and lists (#166, #242)
- Split source files for list, program, array and equation (#167)
- Unify precedence handling for parser and renderer
- Add "storytelling" file (#191) for video demos
- Update STATUS.md file (#200)
- Fix generation of fonts
- Fix subtle dereferencing bug in GC pointer
- Use C++ template metaprogramming to build RPL equations from C++ (#230)
- Use flags instread of range comparisons to check properties of objects (#234)
- Default settings when running "current test" (#150)
- Add `rewrite_all` to rewrite until convergence (#241, #243)
- Do not integrate random files in `make dist`.

Verse of the day:
  The kingdom of heaven is like treasure hidden in a field.
  When a man found it, he hid it again, and then in his joy went and sold
  all he had and bought that field (Mt 13:44)

Signed-off-by: Christophe de Dinechin <christophe@dinechin.org>

---
## [Gforcex/OpenGraphic](https://github.com/Gforcex/OpenGraphic)@[c3a9f933b0...](https://github.com/Gforcex/OpenGraphic/commit/c3a9f933b03d04ad97750961b210c9ad3ee4156f)
#### Sunday 2023-07-30 13:47:53 by Gforcex

Update Blender.md* [awesomeblend](https://github.com/Davetmo/awesomeblend) A curated list of awesome Blender add-ons, tools, tutorials and resources for 3D Artists, Hobbyists, Developers, Researchers. Focused mostly open source and free resources. Blender 2.8+ compatible list.   * [MB-Lab](https://github.com/animate1978/MB-Lab) MB-Lab is a character creation tool for Blender 2.80, based off ManuelBastioniLAB https://www.mblab.dev * [DreamUV](https://github.com/leukbaars/DreamUV) DreamUV is a collection of tools that allow you to manipulate UVs in the 3D viewport. * [Magic-UV](https://github.com/nutti/Magic-UV) Blender Add-on: Magic UV * [bricker](https://github.com/bblanimation/bricker) Bricker is a powerful modeling, animation, and simulation addon for Blender designed to streamline and, in many cases, automate the artist's workflow for LEGO bricks. Created by Christopher Gearhart. * [mixer](https://github.com/ubisoft/mixer) Add-on for real-time collaboration in Blender. * [Stop-motion-OBJ](https://github.com/neverhood311/Stop-motion-OBJ) A Blender add-on for importing a sequence of OBJ meshes as frames * [Blender_UE4_VectorFieldEditor](https://github.com/isathar/Blender_UE4_VectorFieldEditor) Blender addon that adds support for working with 3D vector fields using the FGA file format. * [animation_nodes](https://github.com/JacquesLucke/animation_nodes) Node based visual scripting system designed for motion graphics in Blender. * [Abnormal](https://github.com/BlenderNPR/Abnormal) Blender Abnormal add-on for vertex normal editing * [Pivot-Painter-for-Blender](https://github.com/Gvgeo/Pivot-Painter-for-Blender) Pivot Painter is a Blender addon to create a 3d model, that will use the Pivot Painter Tool's shaders in Unreal Engine 4 * [TexTools-Blender](https://github.com/SavMartin/TexTools-Blender) http://renderhjs.net/textools/blender/ * [MACHIN3tools](https://github.com/machin3io/MACHIN3tools) MACHIN3tools is a free, continuously evolving collection of blender tools and pie menus in a single customizable package. * [Sorcar](https://github.com/aachman98/Sorcar) Procedural modeling in Blender using Node Editor * [Malt](https://github.com/bnpr/Malt) Render framework for NPR * [BEER](https://github.com/BlenderNPR/BEER) Blender Extended Expressive Renderer (A stylized renderer) * [retopoflow](https://github.com/CGCookie/retopoflow) A suite of retopology tools for Blender * [Blender-BakeLab2](https://github.com/Shahzod114/Blender-BakeLab2) Blender addon for baking images * [bpbrt4](https://github.com/NicNel/bpbrt4) pbrt-v4 render engine/exporter for Blender * [MolecularNodes](https://github.com/BradyAJohnston/MolecularNodes) Addon and nodes for working with structural biology and molecular data in Blender. * [MapsModelsImporter](https://github.com/eliemichel/MapsModelsImporter) A Blender add-on to import models from google maps * [b3dsdf](https://github.com/williamchange/b3dsdf) A toolkit of 2D/3D signed distance functions and sdf/vector operator nodegroups(135+) for Blender 2.83+. Also available as an addon which adds a menu in the shader editor. * [dream-textures](https://github.com/carson-katri/dream-textures) Stable Diffusion built-in to the Blender shader editor * [AI-Render](https://github.com/benrugg/AI-Render) Stable Diffusion in Blender * [glslTexture](https://github.com/patriciogonzalezvivo/glslTexture) Blender addon to create 2D textures from GLSL.  * [Blender-Lightsheet](https://github.com/markus-ebke/Blender-Lightsheet) Add-on for Blender3D to create caustics for Cycles and EEVEE * [blendify](https://github.com/ptrvilya/blendify) Blendify is a lightweight Python framework that provides a high-level API for creating and rendering scenes with Blender. Developed with a focus on 3D computer vision visualization, Blendify simplifies access to selected Blender functions and objects. * [jmesh-tools](https:github.com/jayanam/jmesh-tools)

---
## [UnionofSovietSocialistRepublics/Spore-Biomechs](https://github.com/UnionofSovietSocialistRepublics/Spore-Biomechs)@[3f303e0f94...](https://github.com/UnionofSovietSocialistRepublics/Spore-Biomechs/commit/3f303e0f943eb0f0887e57764908e920d635e01b)
#### Sunday 2023-07-30 14:49:37 by Horizon

Immortal temptation Takes over my mind, condemned Falling weak on my knees Summon the strength of mayhem I am the storm that is approaching Provoking black clouds in isolation I am reclaimer of my name Born in flames, I have been blessed My family crest is a demon of death Forsakened, I am awakened A phoenix's ash in dark divine Descending misery Destiny chasing time Inherit the nightmare, surrounded by fate Can't run away Keep walking the line, between the light Led astray Through vacant halls I won't surrender The truth revealed in eyes of ember We fight through fire and ice forever Two souls once lost, and now they remember I am the storm that is approaching Provoking black clouds in isolation I am reclaimer of my name Born in flames, I have been blessed My family crest is a demon of death Forsakened, I am awakened A phoenix's ash in dark divine Descending misery Destiny chasing time Disappear into the night Lost shadows left behind Obsession's pulling me Fading, I've come to take what's mine Lurking in the shadows under veil of night Constellations of blood pirouette Dancing through the graves of those who stand at my feet Dreams of the black throne I keep on repeat A derelict of dark, summoned from the ashes The puppet master congregates all the masses Pulling strings, twisting minds as blades hit You want this power? Then come try and take it Beyond the tree, fire burns Secret love, bloodline yearns Dark minds embrace, crimson joy Does your dim heart heal or destroy? Bury the light deep within Cast aside, there's no coming home We're burning chaos in the wind Drifting in the ocean all alone

---
## [AkairyuGestalter/xivanalysis](https://github.com/AkairyuGestalter/xivanalysis)@[c009fd5bcf...](https://github.com/AkairyuGestalter/xivanalysis/commit/c009fd5bcf5a7ae7810f9e30a3f7df648c2d4d43)
#### Sunday 2023-07-30 15:24:40 by B Fraser

BLU: 6.45 Moon Flute update (#1873)

* BLU: Being Mortal mistakenly had the same actionId as Apokalypsis

* BLU Moon Flute window: Swap out important spells in the burst window

With the new spells in 6.45, BLU's burst window got even more
busy.  It is, technically, still a gain to cast Rose of Destruction,
to use Bristle on Matra Magic, and to use Glass Dance, but they are
all roughly on the category of "you may drop these, either entirely
or just out of the opener".

Adding 4 or 6 new potential actions to the report would've rendered
mostly useless, so instead, this commit makes it so that we expect
any Moon Flute burst to include the following oGCDs:

    J Kick
    Shock Strike
    Feather Rain
    Nightbloom
    Being Mortal
    Sea Shanty
    Surpankaha x4
    Phantom Flurry

And the following two GCDs:

    Matra Magic
    Triple Trident (only if it was off cooldown, for SpS builds)

While there's optimal filler GCDs for the opener, they aren't
useful generic recomendations (Swiftcast => Wild Rage), and they
aren't standard between all openers (Winged Reprobation and Rose of
Destruction are in practice mutually exclusive, and some openers
drop Bristle for a third Winged Reprobation, for roughly the same
potency on every burst but the first one), so we're just
not enforcing them anymore.

It's also optimal to do an extra weave for Glass Dance somewhere in
the opener, but that's now so rarely taken due to spell slot
limitations that giving it its own column in the report will just
add noise.

* BLU Moon Flute: Handle odd-minute Breath of Magic bursts

`Breath of Magic` is a new DoT BLU got this patch.  It lasts 60
seconds and does a silly amount of potency, with the caveat that
only one person can apply it on the target.

Due to BoM's silly potency, ideally it should be reapplied under
Moon Flute every minute, meaning that in addition to the normal
even-minute burst, the BoM applier should be doing an odd-minute
burst too.

Since "odd-minute" and "even-minute" are going to be entirely
encounter-dependent, this commit is using a heuristic:
If they used both `Breath of Magic` and `Song of Torment` under
a given Moon Flute, then this is an odd-minute burst, so few
of the usual requirements apply.

* BLU Moon Flute: Keep support for pre-6.45 BLU logs

* BLU Moon Flute 6.45: changelog

* BLU Moon Flute: Change the heuristic for odd-minute bursts

Per @xiashtra's suggestion, we now base this on whether
Nightbloom is on-cooldown during the moon flute, rather
than checking Song of Torment, which in some edge cases
people may not be taking.

* BLU Moon Flute: Reworded the two suggestions to be a bit less convoluted

* BLU Moon Flute: yarn extract

* BLU Moon Flute: yarn linting

---
## [Beautysalonorbit/Nooro-Whole-Body-Massager-A-Review-of-the-Best-Portable-Massager-for-Pain-Relief](https://github.com/Beautysalonorbit/Nooro-Whole-Body-Massager-A-Review-of-the-Best-Portable-Massager-for-Pain-Relief)@[37c277627d...](https://github.com/Beautysalonorbit/Nooro-Whole-Body-Massager-A-Review-of-the-Best-Portable-Massager-for-Pain-Relief/commit/37c277627dcba2d05b456e814588e7acbd0d9901)
#### Sunday 2023-07-30 15:48:41 by Shahid Malik

Update README.md

Could the Nooro Whole Body Massager hold the key to easing your chronic pain, muscle tension, or stress? Imagine having a personal masseuse at your disposal, ready to work its magic anytime, anywhere. It may sound like a far-fetched dream, but with the Nooro whole body massager, that dream could become your reality.
This small and portable gadget packs a punch when it comes to deep tissue therapy. It targets multiple areas of your body, from the neck and back to the waist, arms, and legs. The secret lies in its electrical stimulation, which activates your nerves and muscles, leading to improved blood circulation and reduced inflammation. As if that's not enough, the Nooro whole body massager offers five distinct massage modes, ensuring you can tailor your experience to suit your preferences and individual needs.
https://beautysalonorbit.com/nooro-whole-body-massager/

---
## [PastelPrinceDan/Skyrat-tg](https://github.com/PastelPrinceDan/Skyrat-tg)@[1fe7b10e33...](https://github.com/PastelPrinceDan/Skyrat-tg/commit/1fe7b10e339ea0d6a3d49f864e1badc5c831e791)
#### Sunday 2023-07-30 16:01:29 by SkyratBot

[MIRROR] Removes TTS voice disable option (Skyrat: Actually makes a functional "None" voice option this time) [MDB IGNORE] (#22283)

* Removes TTS voice disable option (#76530)

## About The Pull Request
Removes the TTS voice disable option, which was already unavailable on
TG as it was set to off by default. The reason this was added was so
that downstreams could toggle the config on or off.

## Why It's Good For The Game
I think this option fundamentally undermines the TTS system because it
allows individual players to disable their voice globally, meaning that
players who have TTS enabled will not be able to hear them.

This worsens the experience for players who have TTS enabled and it's
not something I want to include as an option. If players don't like
their voice, they can turn TTS off for themselves so that they don't
hear the voices. If players don't want to customize their voice, they
can quickly choose a random voice, and we can take directions in the
future to make voice randomization consistent with gender so that a male
does not get randomly assigned a female voice and vice versa.

This option is already unavailable on TG servers because it was
primarily added for downstreams, but I don't think giving downstreams
the option to undermine the TTS system is the right direction to take.
Downstreams are still completely free to code this option on their own
codebase.

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

* Removes TTS voice disable option

* Returns the option to not have a voice to TTS, properly this time

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [JatoMixo/CalendarApp](https://github.com/JatoMixo/CalendarApp)@[0cd6f416c4...](https://github.com/JatoMixo/CalendarApp/commit/0cd6f416c4d80a26ca6fae9833fbcbfdc245b9f4)
#### Sunday 2023-07-30 16:28:04 by JatoMixo

Fixed stupid error with TypeScript types (They fucking suck)

---
## [Miraviel/Paradise](https://github.com/Miraviel/Paradise)@[2d10818063...](https://github.com/Miraviel/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Sunday 2023-07-30 16:57:47 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [Kaz205/renoir](https://github.com/Kaz205/renoir)@[344cd633f7...](https://github.com/Kaz205/renoir/commit/344cd633f75c420d6c254d2e826ad4ad03f6bed0)
#### Sunday 2023-07-30 17:01:12 by Douglas Anderson

BACKPORT: migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

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
(cherry picked from commit 4bb6dc79d987b243d65c70c5029e51e719cfb94b)

Conflicts:
   mm/migrate.c

This is because we don't have folios in the v5.15 kernel. If we ever
decide to backport folios to v5.15, I'd suggest reverting this patch
(which should have no dependencies) and then picking the clean one
from upstream. The only difference in this patch from the upstream one
is folio_test_uptodate(src) => PageUptodate(page). and the context
difference of folio_lock(src) => lock_page(page).

BUG=b:277132613
TEST=Won't block waiting for that lock anymore

Change-Id: Ia86ccac02a303154a0b8bc60567e7a95d34c96d3
Reviewed-on: https://chromium-review.googlesource.com/c/chromiumos/third_party/kernel/+/4671371
Tested-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Vovo Yang <vovoy@chromium.org>
Commit-Queue: Douglas Anderson <dianders@chromium.org>
(cherry picked from commit e7e4ca0a49d27e57045567c8bb883035f71f53a8)
Reviewed-on: https://chromium-review.googlesource.com/c/chromiumos/third_party/kernel/+/4671868
Auto-Submit: Douglas Anderson <dianders@chromium.org>
Commit-Queue: Rubber Stamper <rubber-stamper@appspot.gserviceaccount.com>
Bot-Commit: Rubber Stamper <rubber-stamper@appspot.gserviceaccount.com>

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[1d28964d37...](https://github.com/ihatethisengine/cmss13/commit/1d28964d37f9b95773580cca3471a2a4f5c03eb0)
#### Sunday 2023-07-30 17:08:14 by naut

New blood bags (#3961)

# About the pull request

Since we're putting so much emphasis on blood bags lately, I figured I
might as well do my part as spriter and add actual _labels_ to the
things so you can tell what they are at a glance. Also overhauled the
system to use overlays and underlays instead of the cursed
`full/half/empty` thing that it had going beforehand.

# Explain why it's good for the game

You now no longer have to manually inspect blood bags to tell what type
they are! Rejoice.

# Testing Photographs and Procedure
<img width="251" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/c4424ec3-bfe6-4d58-8915-595b468a7606">

_Blood bags in action. Sort of. Yes, they actually change color now._

<img width="571" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/3b478c65-54b9-4321-bf02-dcfacaf1ad23">

_Icon states! Also sprinkled in some yet-unused labels for future
use(TM). AB types are here, too, because I forgot they weren't in the
game._
# Changelog

:cl: nauticall
imageadd: Resprited blood bags to look nicer and use proper a proper
overlay/underlay system. Their types are also now distinguishable at a
glance.
code: Reworked the way blood bag sprites work behind the scenes to use
the overlay/underlay system.
/:cl:

---
## [Sargeantmuffinman/cmss13](https://github.com/Sargeantmuffinman/cmss13)@[cb855f807b...](https://github.com/Sargeantmuffinman/cmss13/commit/cb855f807b4f5538d623e78363e76aabd5f8d80a)
#### Sunday 2023-07-30 18:04:44 by forest2001

Yautja Gear Recovery Changes (#3455)

# About the pull request
Makes pred gear recovery more dynamic and less blood thirsty.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: Adds a plasma breaching charge that detonates a plasma wave
stunning those opposite it.
add: Adds the name of the tracked item to the Yautja gear tracker.
add: Added an alternate mode for the Plasma Pistol and moved the
incendiary property to it.
add: Added MINIMAP_FLAG_ALL to Yautja globe map.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [coolmankid12345/space-station-14](https://github.com/coolmankid12345/space-station-14)@[31607a0be0...](https://github.com/coolmankid12345/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Sunday 2023-07-30 18:18:37 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [TheGamerdk/cmss13](https://github.com/TheGamerdk/cmss13)@[0f386c8188...](https://github.com/TheGamerdk/cmss13/commit/0f386c8188849b2a761ef773ed83d7f2a95d40e7)
#### Sunday 2023-07-30 18:34:20 by fira

Stops Squad Leaders and ComTechs from blowing up the Almayer (#3602)

# About the pull request

Okay that's a clickbait....

When people put C4 and Breaching Charges in their bag and what not the
log gets triggered.

This spams niche log with false warnings of /!\ DANGEROUS GRIEFING
TERRORISTS /!\

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Uh

# Changelog
:cl:
fix: Handling C4 and Breaching Charges should not zealously trigger
antigrief protection anymore
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [EvaEvaEvaEvaEva/shaptest](https://github.com/EvaEvaEvaEvaEva/shaptest)@[1b315a616f...](https://github.com/EvaEvaEvaEvaEva/shaptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Sunday 2023-07-30 18:44:20 by Thedragmeme

Aegis update + patient clothing (#2150)

## About The Pull Request
The Aegis:
![2023-07-09 06 32
40](https://github.com/shiptest-ss13/Shiptest/assets/81540056/cf262257-1699-40e0-bcb1-6dc60f1e98a6)
I've touched up the central hallway's decals, they always bothered me
but at the time of the Aegis' creation, I wasn't as well versed with map
making as I am now. They're small tweaks that look better to me. The
smart fridge was removed and turned into a board, originally you could
access the smart fridge from outside of the ship, which wasn't intended.
Added some new posters. Compressed the number of red lockers down and
cleaned up the main hallway. I gave the psychologist a dart gun because
honestly, it sounded really funny.

![dart
riffle](https://github.com/shiptest-ss13/Shiptest/assets/81540056/eb10154a-1e28-4a5d-b41b-9b20f92b71a9)

Also, there are more seeds to make food with. There were like only two
food seeds and like five flowers before.

The Patient set:


![patient](https://github.com/shiptest-ss13/Shiptest/assets/81540056/65066ea3-92d1-4233-9bf6-a6448d43b11f)

Kepori and Vox versions are available. Long-term patients now spawn with
the white gown and slippers. The previous clothes they spawned with were
always intended to be replaced.

Hopefully, this PR also fixes long-term patients spawning with borked
ID's.

## Why It's Good For The Game

Fixing stuff, making stuff look better, and adding new RP opportunities
with clothes are good.

## Changelog

:cl: Drag
add: Adds a bunch of shit to the Aegis, nothing earth shattering
add: Added the patient set, along with Vox and Kepori compatible sprites
tweak: tweaked with the Aegis' decals
fix: (Hopefully) Fixes the Aegis' patient Id's
:cl:

---------

Signed-off-by: Thedragmeme <81540056+Draggeru@users.noreply.github.com>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [Moemiset/TsholofeloM](https://github.com/Moemiset/TsholofeloM)@[10714b8874...](https://github.com/Moemiset/TsholofeloM/commit/10714b8874071098cf5f30a4289e153ab20b197d)
#### Sunday 2023-07-30 19:03:27 by Moemiset

Add files via upload

TBFXLive: Empowering Traders Worldwide with Unparalleled Access and Exclusive Promotions! 

This design was created for a client who has diverse knowledge and creativity within the Forex/ Trading industry. The client wanted to further his services and add subscription service and a trading platform all together in one.

Are you ready to take your forex trading experience to new heights? Look no further!  TBFXLive, the ultimate solution for traders seeking real-time prices, seamless trade execution, and access to exclusive promotions like never before.

Unrivaled Market Access:
Gain an edge in the global financial markets with our cutting-edge trading application. Access real-time forex prices from leading liquidity providers, empowering you to make informed decisions at the speed of light. Stay on top of the latest market trends, track currency pairs, and explore extensive historical data, all within a user-friendly and intuitive interface.

Swift and Reliable Trade Execution:
Time is money, and we understand that every second counts in forex trading. With TBFXLive App, experience lightning-fast trade execution to ensure that your orders are placed at the best possible prices. Say goodbye to lag and slippage and embrace a seamless trading experience that matches your skill and expertise.

Exclusive Promotions for Enhanced Profits:
Through TBFXLive, They believe in rewarding their valued clients. By Benefiting from a range of exclusive promotions and special offers, designed to maximize your potential profits. The team works tirelessly to secure deals and bonuses that put you ahead in the trading game. Unlock these opportunities and make the most of your trades with their exciting promotions!

Security and Peace of Mind:
Your security is top priority. With state-of-the-art encryption and robust security measures, trade with confidence, knowing that your funds and personal information are safeguarded at all times. Commitment to creating a secure trading environment allows you to focus on what truly matters – implementing your trading strategies and achieving your financial goals.

Customer Support: TBFXLive value every client and are dedicated to providing exceptional customer support around the clock. With a team of experienced professionals is ready to assist you with any inquiries, technical issues, or account-related matters. Feel the reassurance of having a reliable support system, empowering you to trade with confidence, no matter the time zone.

Join TBFXLive Revolution Today!
Whether you are a seasoned trader or just getting started in the forex world, TBFXLive is the game-changer you've been waiting for. Embark on a rewarding journey, where innovation, accessibility, and profitability intersect.

---
## [HKalbasi/rust-analyzer](https://github.com/HKalbasi/rust-analyzer)@[994f4f6e2e...](https://github.com/HKalbasi/rust-analyzer/commit/994f4f6e2e45bef4bebeeabee4e3d67b87727b91)
#### Sunday 2023-07-30 19:35:20 by bors

Auto merge of #15290 - igorskyflyer:igorskyflyer-dx-install-extension, r=lnicola

editor/code: [DX] Use notification command links for debugger installation

This PR improves DX (developer experience) when installing the VS Code extension for the first time. When doing so and trying to debug a Rust file, we get an error notification that either CodeLLDB or C++ extension/debugger should be installed (see image below).

<div align="center">
	<img src="https://github.com/rust-lang/rust-analyzer/assets/20957750/e8ebeb1e-85f4-44e2-b79f-c48cf52e5f36" alt="Rust, prompt to install debug extension">
</div>

The PR enhances the links in the given notification and upon clicking instead of opening the Web page of the extension it installs the extension immediately, without the need to leave the editor.

Note: the feature needs to be refined, maybe an "install in progress" message or something similar, I left that for you guys to decide and implement. I think it also possible to first open the sidebar, open the Extensions tab, then run the extension installation command which would make it more user-friendly.

P.S. it is also possible to open the extension's details in VS Code directly via the same links and then the user would have to manually click on the Install button - if installation is not the desired behavior.

Happy coding! 🎉

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3af26df8ca...](https://github.com/tgstation/tgstation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Sunday 2023-07-30 19:52:35 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [Svetoslaus/java-challenges](https://github.com/Svetoslaus/java-challenges)@[105e9763fd...](https://github.com/Svetoslaus/java-challenges/commit/105e9763fdfbc250818da6cb977a55b8f383cb9a)
#### Sunday 2023-07-30 19:58:24 by Svetoslaus

Create unwanted-dollars.java

If you're faced with an input box, like this:

                                           +--------------+
  Enter the price of the item, in dollars: |              |
                                           +--------------+
do you put the $ sign in, or not? Inevitably, some people will type a $ sign and others will leave it out. The instructions could be made clearer - but that won't help those annoying people who never read instructions anyway.

A better solution is to write code that can handle the input whether it includes a $ sign or not.

So, we need a simple function that converts a string representing a number (possibly with a $ sign in front of it) into the number itself.

Remember to consider negative numbers (the - sign may come either before or after the $ sign, if there is one), and any extraneous space characters (leading, trailing, or around the $ sign) that the users might put in. You do not need to handle input with trailing characters other than spaces (e.g. "1.2 3" or "1$"). If the given string does not represent a number, (either with or without a $ sign), return 0.0 .

---
## [sebkarrer/emaila](https://github.com/sebkarrer/emaila)@[3fe956f1e5...](https://github.com/sebkarrer/emaila/commit/3fe956f1e508beb9c0e9e29393c14a224244a36b)
#### Sunday 2023-07-30 20:13:08 by Sebastian

aider: Added `gmail_email.py` file that accesses Gmail messages using the Google API client library for Python.

# Aider chat conversation:

USER: how do i create a new git repo that can take this code?

ASSISTANT: To create a new Git repository, follow these steps:

1. Create a new directory for your project and navigate into it:

```bash
mkdir my_project
cd my_project
```

2. Initialize the Git repository:

```bash
git init
```

3. Now, you can add your `outlook_email.py` file to this directory. Once you've added the file, you can add it to the Git repository:

```bash
cp /path/to/your/outlook_email.py .
git add outlook_email.py
```

4. Commit the changes:

```bash
git commit -m "Initial commit"
```

5. If you want to push this repository to GitHub, you need to create a new repository on GitHub. Do not initialize it with a README, .gitignore, or License. This needs to be an empty repository.

6. Copy the remote repository URL.

7. Link the local repository to the remote repository:

```bash
git remote add origin your_remote_repository_url
```

8. Finally, push the changes in your local repository to GitHub:

```bash
git push -u origin master
```

Please replace `your_remote_repository_url` with the actual URL of your remote repository. Also, replace `/path/to/your/outlook_email.py` with the actual path of your `outlook_email.py` file.

USER: The new repo url is https://github.com/sebkarrer/emaila.git. Can you execute these steps for the file outlook_email.py?

ASSISTANT: I'm sorry for any confusion, but as an AI, I don't have the ability to directly interact with your file system or execute commands. However, I can guide you through the process. Here are the steps you need to follow:

1. Open a terminal on your computer.

2. Create a new directory for your project and navigate into it:

```bash
mkdir my_project
cd my_project
```

3. Initialize the Git repository:

```bash
git init
```

4. Now, you can add your `outlook_email.py` file to this directory. Once you've added the file, you can add it to the Git repository:

```bash
cp /path/to/your/outlook_email.py .
git add outlook_email.py
```

5. Commit the changes:

```bash
git commit -m "Initial commit"
```

6. Link the local repository to the remote repository:

```bash
git remote add origin https://github.com/sebkarrer/emaila.git
```

7. Finally, push the changes in your local repository to GitHub:

```bash
git push -u origin master
```

Please replace `/path/to/your/outlook_email.py` with the actual path of your `outlook_email.py` file.

USER: sebkarrer

ASSISTANT: Hello Sebkarrer, how can I assist you further with your software development needs?

USER: This return the following error: remote: Support for password authentication was removed on August 13, 2021.

ASSISTANT: The error message you're seeing is because GitHub has discontinued support for password authentication when interacting with repositories. You'll need to use a personal access token (PAT) or SSH keys instead.

Here's how you can create a personal access token:

1. Go to GitHub and log in to your account.
2. Click on your profile picture in the top right corner and select `Settings`.
3. In the left sidebar, click on `Developer settings`.
4. Click on `Personal access tokens`.
5. Click on `Generate new token`.
6. Give your token a descriptive name, select the scopes (or permissions) you'd like to grant this token, and click on `Generate token`.
7. Copy the token to your clipboard. For security reasons, after you navigate off the page, you will not be able to see the token again.

Now, when you push to GitHub, use the token as your password:

```bash
git push https://<token>@github.com/sebkarrer/emaila.git
```

Replace `<token>` with the personal access token you just created.

Please note that it's not a good practice to hardcode your personal access token. A better way is to use a credential helper to remember your GitHub credentials:

```bash
git config --global credential.helper store
```

After running this command, the next time you push, you'll be asked for your username and password. The username is your GitHub username, and the password is the personal access token. The credential helper will remember your credentials for future pushes to this repository.

USER: remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.

ASSISTANT: The error message you're seeing is because GitHub has discontinued support for password authentication when interacting with repositories. You'll need to use a personal access token (PAT) or SSH keys instead.

Here's how you can create a personal access token:

1. Go to GitHub and log in to your account.
2. Click on your profile picture in the top right corner and select `Settings`.
3. In the left sidebar, click on `Developer settings`.
4. Click on `Personal access tokens`.
5. Click on `Generate new token`.
6. Give your token a descriptive name, select the scopes (or permissions) you'd like to grant this token, and click on `Generate token`.
7. Copy the token to your clipboard. For security reasons, after you navigate off the page, you will not be able to see the token again.

Now, when you push to GitHub, use the token as your password:

```bash
git push https://<token>@github.com/sebkarrer/emaila.git
```

Replace `<token>` with the personal access token you just created.

Please note that it's not a good practice to hardcode your personal access token. A better way is to use a credential helper to remember your GitHub credentials:

```bash
git config --global credential.helper store
```

After running this command, the next time you push, you'll be asked for your username and password. The username is your GitHub username, and the password is the personal access token. The credential helper will remember your credentials for future pushes to this repository.

USER: now duplicate outlook_email.py and call the new file gmail.emailpy

ASSISTANT: To duplicate the `outlook_email.py` file and name the new file `gmail_email.py`, you can use the `cp` command in the terminal:

```bash
cp outlook_email.py gmail_email.py
```

This command will create a copy of `outlook_email.py` and name it `gmail_email.py`.

After you've created the new file, you can add it to the Git repository:

```bash
git add gmail_email.py
```

And then commit the changes:

```bash
git commit -m "Added gmail_email.py"
```

Finally, push the changes to your GitHub repository:

```bash
git push origin master
```

Please replace `origin` and `master` with your actual remote name and branch name if they are different.

USER: create another py file that does the same thing, but for a gmail account

ASSISTANT: To access Gmail messages, we can use the Google API client library for Python. Here's a high-level overview of the steps we need to follow:

1. Set up a project in the Google Cloud Console.
2. Download the JSON file with your credentials.
3. Install the Google Client Library.
4. Use the library to access Gmail.

The Python code will be in a single file, let's call it `gmail_email.py`.

Please note that you need to replace `credentials.json` with the path to your actual credentials file.

```python
gmail_email.py
<<<<<<< ORIGINAL

=======
import os.path
import base64
import re
import time
import dateutil.parser as parser
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me',labelIds = ['INBOX'],q="is:unread",maxResults=1).execute()
        message = results.get('messages')

        if not message:
            print('No new messages.')
        else:
            message = message[0]
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            email_data = msg['payload']['headers']
            for values in email_data:
                name = values['name']
                if name == 'From':
                    from_name = values['value']
                    for part in msg['payload']['parts']:
                        try:
                            data_text = part['body']["data"]
                            byte_code = base64.urlsafe_b64decode(data_text)
                            text = byte_code.decode("utf-8")
                            print("Message: ", text)
                        except BaseException as error:
                            pass
    except Exception as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()
>>>>>>> UPDATED
```

Please note that this code will print the last unread email in your inbox. If you want to print other details, you can modify the print statements accordingly.

---
## [Warfan1815/cmss13](https://github.com/Warfan1815/cmss13)@[ce818246c1...](https://github.com/Warfan1815/cmss13/commit/ce818246c107cf97525a05f6f3a66e120117b8c3)
#### Sunday 2023-07-30 20:23:55 by QuickLode

The Hazmat Joe (#3259)

# About the pull request
This pull request resprites the entire Working Joe from toes to head. It
also gives two additional uniforms which are meant for hazardous use,
and this PR should act as a foundation for future implementation of the
Hazmat Joe into CM's gameplay. Additionally, I may just set this to
draft and let it be reviewed while I work on the actual implementation.

They are complete with distinctive loadouts, which focus more on
hazardous situations, repair, and firefighting. Though may tweak things
depending on how its implemented.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This adds a fan favorite variation of your inexpensive, reliable friend!
You've seen him in quite a few places, and now he's coming to CM!

Also, the resprite of the Joe fixes up some minor sprite issues that
were encountered on previous models.

More content, more roleplay possibilities! ARES! Get me some Joes to put
that reactor fire out ASAP!
# Testing Photographs and Procedure

https://cdn.discordapp.com/attachments/490668342357786645/1104748917398175795/image.png

https://media.discordapp.net/attachments/490668342357786645/1105643891107049572/image.png
Ran several tests and they went well.


# Changelog
:cl:QuickLoad,Frans_Feiffer,nauticall
add: Adds The Hazmat Joe with two minor variations. This is a Working
Joe equipped to handle hazardous situations, dangerous repairs and
firefighting! They are complete with their own gear, tasks, job and
purpose. Forget the trashbag, get that wall fixed before we get spaced!
imageadd: Adds a new Working Joe model made by Frans Feiffer!
imageadd: Adds two variations of the Working Joe, aka the Hazmat Joe.
Complete with accessories! Beautiful sprites by Frans Feiffer!
add: Android Maintenance Stations / Synthetic Repair Stations will
remove shrapnel & fix organ damage. Working Joes no longer have knives,
and should report to the stations for repair. Gigantic thanks to
nauticall for her work on this!!
imagedel: Removes(replaces) the old Working Joe model.
add: Working Joes receive some basic equipment, and are slightly
resilient to disarms.
add: Working Joes will start at 3, with a maximum of 6 depending on
population.
add: Joes can access a Synthetic vendor to replace their uniform if it
is damaged.
fix: Minor changes to PO Uniform.
/:cl:

---------

Co-authored-by: naut <nautilussplat@gmail.com>
Co-authored-by: BeagleGaming1 <56142455+BeagleGaming1@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[c980e2d032...](https://github.com/TaleStation/TaleStation/commit/c980e2d03252499d82ca49368a67b3d789b9ca14)
#### Sunday 2023-07-30 21:16:02 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#7055)

Original PR: https://github.com/tgstation/tgstation/pull/77077
-----
## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

Here's some pictures of my testing proving that it works:
_No blood, before walking over blood_

![image](https://github.com/tgstation/tgstation/assets/58045821/55d6a4c6-bf46-49ca-8b1d-e505d4966be9)

_Walked over blood with shoes, only shoes are bloody_

![image](https://github.com/tgstation/tgstation/assets/58045821/00da9a76-2f01-4550-99ce-36be8bf3a3cf)

_Walked over blood without shoes, kilt is bloody_

![image](https://github.com/tgstation/tgstation/assets/58045821/c7427679-5058-4a3f-8851-c343451c38c2)

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

## Why It's Good For The Game
It just makes sense, and it allows more consistency within the
bloodysoles usage as a whole.

## Changelog

:cl: GoldenAlpharex
fix: Clothes equipped in the jumpsuit slot that happen to cover your
feet will no longer get bloody when you walk over blood if you are also
wearing shoes. Your kilt won't be getting bloody instantly anymore, it
only will if you take your shoes off!
/:cl:

---------

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [saiachuth/AZ-LandingPage](https://github.com/saiachuth/AZ-LandingPage)@[7d83704632...](https://github.com/saiachuth/AZ-LandingPage/commit/7d837046323abcd4e06146f1b91494df6b42a6d3)
#### Sunday 2023-07-30 21:20:36 by Sai Achuth

Add files via upload

Features:

Beautiful and intuitive landing page designed to engage and inform visitors about AlgoZenith's offerings.
Seamless integration of Vite and React for optimal performance and developer-friendly development experience.
Custom CSS styling for a polished and visually appealing user interface.
Responsive design ensures a smooth browsing experience across various devices and screen sizes.
Interactive elements to provide visitors with a glimpse of AlgoZenith's powerful algorithmic trading solutions.
Accessible and user-friendly navigation to effortlessly explore different sections of the landing page.
Getting Started:

To get started with the AlgoZenith landing page:

Clone the repository to your local machine.
Install the project dependencies using npm or yarn.
Run the development server to view the landing page locally.
Customize the content and design to suit your specific use case.
Contributing:

We welcome contributions from the open-source community! If you have ideas for enhancements or bug fixes, feel free to open issues or submit pull requests.

License:

The AlgoZenith landing page is open-source and licensed under the MIT License. Feel free to use and modify the code as per the license terms.

Acknowledgments:

Special thanks to the Vite and React communities for their fantastic tools and support, making the development of this landing page a seamless experience.

Explore the AlgoZenith landing page now to discover the exciting world of algorithmic trading and our commitment to empowering traders with data-driven insights.

Please adapt the description according to the specific features and details of your AlgoZenith landing page project. Highlight the unique aspects and design elements that set your landing page apart and provide clear instructions on how users can get started and contribute to the project.

---
## [Sergiovan/Sir-Govan-Discord](https://github.com/Sergiovan/Sir-Govan-Discord)@[34779a5a71...](https://github.com/Sergiovan/Sir-Govan-Discord/commit/34779a5a71d86c66229ffa0ef0e57cdae4de1850)
#### Sunday 2023-07-30 21:43:41 by Sergiovan

Added on_reaction skeleton and hall pinning skeleton

Did some gymnastics to get the emojis baked into the type system (This will have no benefits and in fact come back to bite me in the ass)
Turns out the REST API cannot be trusted. Thanks Discord
God, this is going to be painful

---
## [Xeeynamo/sotn-decomp](https://github.com/Xeeynamo/sotn-decomp)@[b488191654...](https://github.com/Xeeynamo/sotn-decomp/commit/b488191654aef67226d141568be5104b78ea4ea7)
#### Sunday 2023-07-30 21:58:01 by bismurphy

Decompile DRA func_800FE044 (#407)

This function is responsible for upgrading the player's stats. This is
called upon collection of a Life Max Up, Heart Max Up, or when killing
an enemy to get experience. This function gives experience to the player
and their active familiar.

HUGE thanks to @mkst for the maspsx update that allowed this one to
match!

The arguments to this function are a little unusual. arg0 is mostly used
as the amount to increase the heartMax, hpmax, or exp, but in the case
where we're getting a relic, is used as the relic ID. Similarly, arg1 is
mostly used to identify which of these traits is being increased, but in
the case where we're getting exp, is used to define the enemy's level to
determine how much exp to award. It seems odd that increasing each of
these stats is baked into this one function, instead of all being their
own functions.

This is one of the first functions I looked at when I joined the decomp
several months ago and it's very cool to have it finally working, now
using the extra knowledge I've picked up over that time.

---------

Co-authored-by: bismurphy <bismurphy@users.noreply.github.com>
Co-authored-by: Mark Street <streetster@gmail.com>

---
## [Paxilmaniac/TaleStation](https://github.com/Paxilmaniac/TaleStation)@[7bbd2a7edc...](https://github.com/Paxilmaniac/TaleStation/commit/7bbd2a7edcd7d7f5ea59ec257b6ace9566561cb9)
#### Sunday 2023-07-30 22:03:14 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#7009)

Original PR: https://github.com/tgstation/tgstation/pull/76635
-----

## About The Pull Request

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.
## Why It's Good For The Game

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
https://discord.com/channels/326822144233439242/326831214667235328/1126993070467076197
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

Finally: Bugfixes are good.
## Changelog
:cl:
add: New malf module: Remote vendor tipping. Allows you to remotely tip
a vendor in any of the 8 directions. Goofy and okay for assassinations
on unaware enemies!
add: New malf module: Core rolling. Allows you to roll around, crushing
anything you fall on with a satisfying splat.
code: Vendor tipping is now a /atom/movable proc, allowing anything to
fall over and crush you.
code: All take_damage() overrides now use the correct arguments
image: turf_analysis.dmi's red_arrow now has orthogonal directions
balance: Vendors now are far less likely to gib your head or make you
parapalegic
balance: Vendors now respect armor when they crush you

/:cl:

---------

Co-authored-by: nikothedude <59709059+nikothedude@users.noreply.github.com>

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[3253a521ab...](https://github.com/NetBSD/pkgsrc/commit/3253a521ab9d422ce3802d95d2b723539ffec5ea)
#### Sunday 2023-07-30 22:18:09 by nikita

gotosocial: update to version 0.10.0

Changelog (taken from https://github.com/superseriousbusiness/gotosocial/releases/tag/v0.10.0):

v0.10.0 Shrimple Sloth
89ee9d5

Hello! We did a release! Here it is! We fixed a bunch of broken stuff and added some more stuff that's probably broken and which we'll have to fix in the future! 😎

As always, big thank you to all contributors and well-wishers, and those who use the software and help it grow. The sloth thanks you.
Highlights

    LISTS: this has been one of the most frequently requested features for GoToSocial since forever, so we're happy to be able to include it now! With this release, you can create lists, delete lists, add/remove accounts from lists, and view list timelines in your client app. It works pretty OK!
    Partial search implementation: previously, you could only use search to look for exact URLs (https://example.org/users/someone) or to look for users by their exact namestring (@someone@example.org). With this release, you can now also do partial text searches for:
        statuses you've posted yourself (search in status content warning and body)
        statuses posted in reply to you (search in status content warning and body)
        accounts you don't yet follow (search in username and display name)
        accounts you do follow (search in username, display name, and bio)
    Profile field settings: you can now set up to 6 profile property/value fields in the settings panel.
    Loads of bug fixes. We fixed some of the more annoying/longstanding bugs including missing profile + header pics, please see the section 'First run of media cleanup' below.

Migration notes
Upgrading

To upgrade to 0.10.0 from a previous release:
Binary/tar

    Stop GoToSocial
    Untar the new release, including the web assets and html templates.
    Edit your config.yaml file as necessary (see below).
    Start GoToSocial

Docker

    Stop GoToSocial.
    Pull the new docker container (superseriousbusiness/gotosocial:0.10.0 or superseriousbusiness/gotosocial:latest)
    Start GoToSocial.

config.yaml

The configuration file has changed since the previous release. You can see a diff of the config file here: v0.9.0...v0.10.0#diff-c071e03510b2c57e193a44503fd9528a785f0f411497cc75841a9f8d0b1ac622
Database Migrations

This release contains several database migrations which will run the first time you start up this new version. Be sure not to interrupt this migration process. This will take anywhere between a couple seconds and ten minutes (on slower hardware). Please be patient!
First run of media cleanup

The first time your instance runs a media cleanup (normally at midnight every night), it will likely take a long time. We introduced some issues in 0.9.0 to do with avatars + headers, and the first media cleanup you do in this new version fixes those issues by iterating through all your stored media attachments and fixing ones whose file is missing. Just let it run, it will sort itself out!
Detailed changelog
Features/performance

    f0dad43 [feature] Use Read/Write lock for config (#1969)
    2a99df0 [feature] enable + document explicit IP dialer allowing/denying (#1950)
    81f33c3 [feature] Add media list command (#1943)
    ba0bc06 [feature] Add instance stats to /about (#1936)
    8e00431 [performance] update go-cache library (#1917)
    831ae09 [feature] Add partial text search for accounts + statuses (#1836)
    8fb5a7e [Frontend] Settings for profile fields (#1885)
    20978b1 [performance] wrap httpclient response body to ensure drained before close (#1854)
    f5c004d [feature] Add List functionality (#1802)
    fc524f8 [feature] Configurable custom css length (#1827)

Bugfixes

    89ee9d5 [bugfix] Return all accounts when list accounts limit <= 0 (#2014)
    d6fa74e [bugfix] Change maximumPasswordLength to 72 bytes (#2012)
    f431974 [bugfix] more robust list timeline invalidation (#1995)
    346ecab [bugfix] Add missing continue statement in prepareXBetweenIDs (#1996)
    12b6cdc [bugfix] Set Vary header correctly on cache-control (#1988)
    1951e6c [bugfix] Update account Update logic (#1984)
    8d92b24 [bugfix] Align default values in the configuration file with the code (#1971)
    0d267fd [bugfix] Properly handle range > content-length (#1979)
    ca5492b [bugfix] Tidy up rss feed serving; don't error on empty feed (#1970)
    6dbb8ba [bugfix] Fix delete follow req instead of follow (#1962)
    f40bb02 [bugfix] Delete mutual follow (requests) when receiving block from remote (#1960)
    672386a [bugfix] Don't overflow on very wide status'es (#1956)
    ac564c1 [bugfix] Reorder web view logic, other small fixes (#1954)
    3d16962 [chore/bugfix] Break Websockets logic into smaller read/write functions, don't log expected errors (#1932)
    2a40c81 [bugfix] Try to fix the webfinger test, again (#1931)
    d98b631 [bugfix] Use gtserror package for WrongType errs (#1930)
    52ebff5 [bugfix] Only mark status orphaned on 410 Gone (#1923)
    3e19f48 [bugfix] Ensure InReplyToID set properly, update dereference ancestors func (#1921)
    9a22102 [bugfix/chore] oauth entropy fix + media cleanup tasks rewrite (#1853)
    73bfb5f [bugfix] Parse POST-style forms in the list member removal endpoint (#1903)
    d8e16a2 [chore/bugfix] Refactor ap/extract.go functions, return URIs more reliably (#1897)
    0fa06c0 [bugfix] Accept non-multipart forms for account updates (#1896)
    e70bf8a [chore/bugfix] Domain block tidying up, Implement first pass of 207 Multi-Status (#1886)
    827cc4d [chore/bugfix] Demote failed inbox forwarding to warn log rather than error return (#1892)
    5e2897e [bugfix] Invalidate timeline entries for status when stats change (#1879)
    b0015a3 [bugfix] Delete from list timeline on status deletion (#1878)
    d7d6603 [bugfix] Fix slow joined home timeline query (#1867)
    1d4137f [bugfix] Fix first item of thread dereferencing always being skipped (#1858)
    1f39275 [bugfix] Allow lowercase emoji shortcode in frontend (#1851)
    2358cf4 [bugfix] Overwrite API client closed errors with 499 - Client Closed Request (#1857)
    9da20ee [bugfix] only attempt to populate account/statuses from DB if already exist (#1839)
    70262d4 [fix] Fix link to remote emoji pgae (#1845)
    46d4ec0 [bugfix/chore] Inbox post updates (#1821)
    45f961a [bugfix] allow usernames of length 1 (#1823)

Documentation

    b0f0c8b [docs] Activate the edit feature (#1967)
    747ea58 [docs] Clarify how to add a page (#1959)
    95e2024 [docs] Apache setup for Caching assets and media (#2005) (#2005)
    9ff4c20 [docs] Rework backups a bit (#1942)
    c4cf632 [docs] Clarify email requirement for OIDC (#1918)
    fab64a2 [docs] Disambiguate docker version, don't recommend opening localhost (#1913)
    433b56d [docs] Add certificates and firewalling to advanced (#1888)
    4990099 [docs] Made Advanced its own section (#1883)
    84e1c7a [docs] Revamp the installation guide (#1877)
    6f6b857 [docs] Add example tracing infrastructure (#1866)
    45773a0 [bugfix/docs] AppArmor profile for SQLite (#1864)
    186e849 [docs] Add Repology stats (#1859)
    36fcd2e [docs] clarify other federation modes not yet implemented (#1849)
    1f06914 [docs] Update + simplify roadmap, revise beta estimate (#1826)
    681486f [docs]: semaphone ref & DEBUG usage for standalone testing (#1828)
    e096298 [bugfix/docs] Fix clear notifications API docs (#1831)

Chores / version bumps

    6de5ca4 [chore]: Bump golang.org/x/net from 0.11.0 to 0.12.0 (#1973)
    901770f [chore]: Bump golang.org/x/image from 0.8.0 to 0.9.0 (#1972)
    f5d6503 Bump semver from 6.3.0 to 6.3.1 in /web/source (#1981)
    a29b5af [chore]: Bump golang.org/x/oauth2 from 0.9.0 to 0.10.0 (#1975)
    65c8970 [chore] Fix password typos (#1966)
    8868889 [chore] Skip webfinger test on CI (#1983)
    d9c69f6 [chore/performance] Remove remaining 'whereEmptyOrNull' funcs (#1946)
    1218f97 [chore]: Bump github.com/minio/minio-go/v7 from 7.0.58 to 7.0.59 (#1941)
    e3e0f67 [chore]: Bump github.com/minio/minio-go/v7 from 7.0.56 to 7.0.58 (#1928)
    4ad933b [chore]: Bump github.com/miekg/dns from 1.1.54 to 1.1.55 (#1929)
    120743d [chore]: Bump github.com/tdewolff/minify/v2 from 2.12.6 to 2.12.7 (#1927)
    33ccb71 [chore]: Bump golang.org/x/image from 0.7.0 to 0.8.0 (#1926)
    f56dd29 [chore]: Bump golang.org/x/oauth2 from 0.8.0 to 0.9.0 (#1908)
    84eb7ea [chore] Fix Swagger paths for lists API endpoints (#1904)
    70357a7 [chore]: Bump github.com/jackc/pgx/v5 from 5.3.1 to 5.4.1 (#1907)
    b560fe1 [chore]: Bump golang.org/x/net from 0.10.0 to 0.11.0 (#1909)
    54f3387 [chore]: Bump golang.org/x/crypto from 0.9.0 to 0.10.0 (#1910)
    24fbdf2 [chore] Refactor AP authentication, other small bits of tidying up (#1874)
    5d19fb1 [chore]: Bump modernc.org/sqlite from 1.23.0 to 1.23.1 (#1884)
    b401bd1 [chore] update latest deps, ensure readme up to date (#1873)
    f1b70cc [chore]: Bump github.com/minio/minio-go/v7 from 7.0.55 to 7.0.56 (#1869)
    7638a68 [chore]: Bump github.com/stretchr/testify from 1.8.3 to 1.8.4 (#1872)
    97bc2e7 [chore] tidy + test timelines a bit better (#1865)
    21c1552 [chore] Update versions, fix lint errors (#1860)
    55aacaf [chore]: Bump github.com/gin-gonic/gin from 1.9.0 to 1.9.1 (#1855)
    23705b3 [chore/frontend] refactor header templating, add apple-touch-icon (#1850)
    049b02a [chore]: Bump github.com/microcosm-cc/bluemonday from 1.0.23 to 1.0.24 (#1843)
    f620ee8 [chore]: Bump github.com/coreos/go-oidc/v3 from 3.5.0 to 3.6.0 (#1840)
    e50b228 [chore]: Bump github.com/ulule/limiter/v3 from 3.11.1 to 3.11.2 (#1841)
    2e7043b [chore]: Bump github.com/stretchr/testify from 1.8.2 to 1.8.3 (#1842)
    9ed96bc [chore]: Bump github.com/minio/minio-go/v7 from 7.0.53 to 7.0.55 (#1844)
    5faeb4d [chore] tidy up media manager, add calling func to errors, build-script improvements (#1835)

---
## [AllTheMods/ATM-7](https://github.com/AllTheMods/ATM-7)@[d818a78375...](https://github.com/AllTheMods/ATM-7/commit/d818a78375ecf5ca1c250264b96caa9f78abfe3b)
#### Sunday 2023-07-30 22:39:05 by AlfredGG

Questing Update 10.27.22

- Reworked Allthemodium Chapter for a better feel, added several rewards and descriptions.
- Adjusted Bosses in the "Bounty Board", will add more bosses in the future. Gave a better reward for killing the Gaia boss.
- The quest "Time in a Bottle" now gives better rewards
- Added Template Boards to Silent Gear Questline
- Added Configuration Tool to the Functional Storage section of "Basic Storage"
- Reworked several chapters to start whenever you receive the item needed to start the mod. (For example: raw osmium for Mek, flowers for Botania, etc)
- Added new questline to the "Resources" chapter: Hostile Neural Networks
- Added a new requirement to a Blood Magic quest to better represent what is needed to create Weak Blood Shards. Also added better Demon Will rewards to the Tartaric Gem quests
- Changed requirement for the Stone Pickaxe quest in Blue Skies to allow players to start in either dimension and progress in the questline
- Changed requirement for the Starter Gen in "Getting Started: Part 1" so players can make any of the starter generators from their favorite mods, rather than just the Coal Gen from RFTools.
- Added "Heated Centrifuge" quest to Productive Bees

---
## [TeamMoonstorm/Starstorm2](https://github.com/TeamMoonstorm/Starstorm2)@[a3d9f77b5d...](https://github.com/TeamMoonstorm/Starstorm2/commit/a3d9f77b5d22029299df458125f4acd276c43448)
#### Sunday 2023-07-30 23:53:37 by swuff-star

oh boy

i am going to pull jace's branch and it is going to be fine and absolutely not fuck up my branch haha lets do this!

---

