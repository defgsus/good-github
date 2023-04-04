## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-03](docs/good-messages/2023/2023-04-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,156,437 were push events containing 3,347,995 commit messages that amount to 269,497,764 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [gyuseokByeon/dolly](https://github.com/gyuseokByeon/dolly)@[af91832c66...](https://github.com/gyuseokByeon/dolly/commit/af91832c663025b9d5b3bd0e01be125b91a51799)
#### Monday 2023-04-03 00:19:43 by Matthew Hayes

Add response generation for examples from blog post (#27)

This adds response generation code and runs it over the examples from the [blog post](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html).

A few of the sample outputs:

**Instruction:** Write a love letter to Edgar Allan Poe.

> My love for you is as eternal and enduring as the starlit nights, as deep as the ocean depths, as strong as the wind, and as sweet as the summer breeze. My heart has been yours since the first day I saw you, and it will remain yours forever. I can see you now and my heart fills with longing for our embrace, as I long to be with you forever.

**Instruction:** Explain to me the difference between nuclear fission and fusion.

> Nuclear fission is the splitting of a nucleus, which is a heavy atom, such as uranium, into two separate nuclei, while nuclear fusion is the joining of two nuclei to form a single nucleus, such as hydrogen and helium. Fission occurs when the nucleus absorbs a neutron, leaving a remnant of the nucleus. Fusion occurs when the two nuclei come together and form a single nucleus. Fission is a nuclear reaction and fusion is a nuclear reaction.

**Instruction:** Write a tweet announcing Dolly, a large language model from Databricks.

> Dolly, the world's most accurate language model, is now available on Databricks! 🎉 🎉 🎉

**Instruction:** I'm selling my Nikon D-750, write a short blurb for my ad.

> I'm selling my Nikon D-750, an amazing camera. It has the latest features including 12MP CMOS sensor, 9-point autofocus and auto bracketing, and 3.0x optical zoom. It also has a cool Image Stabilizer system and a dual SD card slot. It is a great choice for photographers looking for a reliable camera that offers superior image quality and features.

**Instruction:** Give me a list of 5 science fiction books I should read next.

> 1. The Hitchhiker's Guide to the Galaxy by Douglas Adams 
> 2. Ender’s Game by Orson Scott Card 
> 3. 1984 by George Orwell 
> 4. Star Wars by George Lucas 
> 5. The Hitchhiker's Guide to the Galaxy by Douglas Adams

---
## [colegaboriault/trail](https://github.com/colegaboriault/trail)@[4f18b63cd0...](https://github.com/colegaboriault/trail/commit/4f18b63cd0e722b8d6aa9d4d9e3c6e30a1077fac)
#### Monday 2023-04-03 00:28:50 by colegaboriault

Shut Up Kids, You're Not Funny

The days are beginning to seem all the same, as though we were
constantly surrounded by identical deciduous forest. I wonder what
could be causing this illusion.

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[60d2d2ee1a...](https://github.com/Hatterhat/Skyrat-tg/commit/60d2d2ee1ae4f7a3c8c93e14fdbd6c210a45cf04)
#### Monday 2023-04-03 00:30:20 by SkyratBot

[MIRROR] Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% [MDB IGNORE] (#20118)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33%

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Shroopy/Skyrat-tg](https://github.com/Shroopy/Skyrat-tg)@[6c978308c7...](https://github.com/Shroopy/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Monday 2023-04-03 00:35:11 by SkyratBot

[MIRROR] Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost [MDB IGNORE] (#19743)

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following:

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[2e5bfe5be6...](https://github.com/Thunder12345/tgstation/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Monday 2023-04-03 00:38:09 by LemonInTheDark

Refactors and optimizes breath code (Saves 12% of carbon/Life()) (#74230)

## About The Pull Request

### How things work

As things currently stand, when a mob breaths several things happen
(simplified to focus on the stupid)

We assert the existance of all possible breathable gases, and pull
partial pressures for them
Then we walk through all possible interactions lungs could have with
these gases, one by one, and see if they're happening or not
As we go we are forced to cleanup potential alerts caused by the
previous breath, even if those effects never actually happen
At the end we clear out all the unused gas ids, and handle the
temperature of the breath.

### What sucks

There's I'd say 3 different types of gas reactions.

- You can "need" a gas to survive. o2, n2 and plasma all fall into this
category
- A gas can do something to you while it's in your system. This applies
to most gas types
- Variation on the previous, some gases do cleanup when they're not in
your system, or when there isn't much of them in the first place

The main headache here is that second one, constantly cleaning up
potential side effects sucks, and fixing it would require a lot of dummy
variables

There's other suckage too.

Needing to constantly check for a gas type even if it isn't there is
stupid, and leads to wasted time It's also really annoying to do
subtypes in this system.
There is what amounts to a hook proc you can override, but you can't
override the reaction to a gas type.
It also just like, sucks to add new gases. one mega proc smells real
stupid.

### Improvements

In the interest of speed:

- I'd like to build a system that doesn't require manually checking for
gas
- Reacting to gas "disappearing" should be promoted by the system,
instead of being hacky.
- I would like to avoid needing to assert the existence of all possible
gases, as this is slow on both the assert and the garbage collect.

In the interest of dev ergonomics:

- It should be easy to define a new gas reaction 
- It should be easy for subtypes to implement their own gas reactions.
The current method of vars on the lung is all tangled up and not really
undoable as of now, but I'd like to not require it
- It should be possible to fully override how a gas is handled

### What I've Done

Lungs have 3 lists of proc paths stored on them

Each list handles a different way the lung might want to interact with a
gas.
There's a list for always processing on a gas (we use this for stuff
that's breathed), a list for handling a gas in our breath, and a list
for reacting to a gas previously being in our breath, but not any more.

Lungs fill out these lists using a helper proc during Initialize()
Then, when it comes time to breath, we loop over the gas in the breath
and react to it.
We also keep track of the previous list of partial pressures, which we
calculate for free here, and use that to figure out when to call the
loss reactions.

This proc pattern allows for overrides, easy reactions to removals,
lower indentation code and early returns, and better organization of
signal handlers

It's also significantly faster. Ballpark 4x faster

### Misc

Removes support for breathing co2, and dying from n2 poisoning. 
They were both unused, and I think it's cringe to clutter these procs
even further

Added "do we even have oxyloss" checks to most cases of passive
breathing.
This is a significant save, since redundant adjustoxy's are decently
expensive at the volume of calls we have here.

Fixes a bug with breathing out if no gas is passed in, assigning a var
to another var doesn't perform a copy

Rewrote breathe_gas_volume() slightly to insert gas into an immutable
mix stored on the lung, rather then one passed in
This avoids passing of a gas_mixture around just to fill a hole. 

I may change my mind on this, since it would be nice to have support for
temperature changing from a hot/cold breath.
Not gonna be done off bodytemp tho lord no.

Uses merge() instead of a hard coded version to move the gas ids over. 
This is slightly slower with lower gas counts but supports more things
in future and is also just easier to read.

## Why It's Good For The Game

Faster, easier to work with and read (imo)

Profiles: 

[breath_results_old.txt](https://github.com/tgstation/tgstation/files/11068247/breath_results_old.txt)

[breath_results_pre_master.txt](https://github.com/tgstation/tgstation/files/11068248/breath_results_new.txt)

[breath_results_new.txt](https://github.com/tgstation/tgstation/files/11068349/breath_results_new.txt)

(These profiles were initially missing #73026. Merging this brings the
savings from 16% to 12%. Life is pain)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[7a64573c8b...](https://github.com/Lamella-0587/Skyrat-tg/commit/7a64573c8bfa01bac0d690db68d4b6528d502579)
#### Monday 2023-04-03 00:49:23 by SkyratBot

[MIRROR] Atmos QOL + Small Sprite Fix [MDB IGNORE] (#20243)

* Atmos QOL + Small Sprite Fix (#74251)

## About The Pull Request
Added screentips and balloon alerts to many atmos machines/pipes
Volume pump overclocking overlay is much slower and less seizure
inducing
RPD screentips for right clicking pipes to copy settings
Removed (RPD) from the RPD's name since having an abbreviation in the
name is ugly
Crystallizer and electrolyzer use ctrl+click and alt-click to turn on
On examine electrolyzer tells you about anchoring to drain from APC
instead of cell
## Why It's Good For The Game
QOL for atmos stuff, user friendliness and better experience
## Changelog
:cl:
fix: Volume pump overclocking animation is much slower, no more
headaches
qol: Added screentips to the RPD; screentips and balloon alerts to many
atmos machines and devices
:cl:

* Atmos QOL + Small Sprite Fix

---------

Co-authored-by: 13spacemen <46101244+13spacemen@users.noreply.github.com>

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[ec67ffb340...](https://github.com/Lamella-0587/Skyrat-tg/commit/ec67ffb340b3c4a64f17eb6458a32cb55ae5183b)
#### Monday 2023-04-03 00:49:23 by SkyratBot

[MIRROR] Properly accounts for byond tick fuckery in runechat code [MDB IGNORE] (#20237)

* Properly accounts for byond tick fuckery in runechat code (#74388)

## About The Pull Request

Ok so like, the agreed upon assumption for "verb like code" (stuff that
triggers when a client sents a network packet to the server), is it runs
in verb time, that sliver of time between maptick and the start of the
next tick.
We thought MeasureText worked like this. It doesn't.

It will, occasionally, resume not during verb time but as a sleeping
proc, at the start of the next tick.
Before the MC has started working.
This appears to only happen when the tick is already overloaded.

Unfortunately, it doesn't invoke after all sleeping procs as we were
lead to believe, but just like, like any sleeping proc.

This means it fights with the mc for cpu time, and doesn't respect the
TICK_CHECK macro we use to ensure this situation doesn't happen.

SOOO lets use a var off the MC instead, tracking when it last fired.
We can use this in companion with TICK_CHECK to ensure verbs schedule
properly if they invoke before the MC runs.

Hopefully this should fix 0 cpu when running at highpop

Thanks to Kylerace and MrStonedOne for suffering together with me on
this, I hate this engine.

* Properly accounts for byond tick fuckery in runechat code

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[f3614ce53c...](https://github.com/Lamella-0587/Skyrat-tg/commit/f3614ce53c9f02d6c4e21b935b6231e98d3348af)
#### Monday 2023-04-03 00:49:23 by SkyratBot

[MIRROR] Thrown containers splashing on mobs spill some contents on the floor [MDB IGNORE] (#20252)

* Thrown containers splashing on mobs spill some contents on the floor (#74345)

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

Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

* Thrown containers splashing on mobs spill some contents on the floor

---------

Co-authored-by: Hatterhat <31829017+Hatterhat@users.noreply.github.com>
Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

---
## [larpchronicles/rules](https://github.com/larpchronicles/rules)@[b493f49f59...](https://github.com/larpchronicles/rules/commit/b493f49f59ddd7c3ed866d868286519cff4377e2)
#### Monday 2023-04-03 00:52:38 by S. Doyle

Change log, Magic fixes, & version update. (#80)

* Updating version.

Updated version in README.

* Version update.

Updated version in json.

* Three spell fixes.

Corrected Dull Pain spell placement to Spirit Level 6.  Was at Level 4.
Added missing effect detail to Blood Sacrifice spell.
Added damage amount to Destroy Undead's incant.

* Updated changelog.

* Changelog lines for Justin Brutlag edits to main.

* Fixing accidental removal from table.

* Pulled changes in from Bryan's PR, made many formatting updates.

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[7cc6934eff...](https://github.com/Pickle-Coding/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Monday 2023-04-03 01:02:22 by LemonInTheDark

Visual fixes (lighting, weird shit, old bugs from a parallax thing) (#73555)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Fixes a bug where anything fully dark on the floor plane would mask the
lighting
plane](https://github.com/tgstation/tgstation/commit/a1a03dc3393216098890b971b2271d56cb2c7463)

I fucked it up boys, needed to take alpha into account here

[Fixes pais getting parallax on icebox because their location was
nested](https://github.com/tgstation/tgstation/commit/81252e0f45c53918a14cc0148353ec440710f8e5)

God I hate this place (Note when I say get I mean they got the plane
master that controls it, not that they actually got it displayed. That
does appear to sometimes happen but I have no idea why)

[Fixes double flashlights not activating if enabled in
place](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

[efb8b64](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

cast_directional_light removes the lighting appearance, because it's
gonna modify it, but it turns out because appearances are static when
they're in like underlays/overlays, this could remove the WRONG UNDERLAY

This lead to double held flashlights just... not working until you
rotated. V stupid.

I've also had to move the flag set to make the overlay add in
cast_directional_light work. Depression

## Why It's Good For The Game

Closes #73535, closes #73517, closes #73518, and fixes part of #73471
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
fix: Fixes activating two flashlights without moving only turning on one
flashlight (until you move)
fix: Purely black things drawn on the floor (like carpets, those foam
dispensers, etc) will no longer cause things on top of them to be fully
masked in darkness
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[d23ac504a0...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/d23ac504a0963a99c4a598abf102cd51144a0ef5)
#### Monday 2023-04-03 01:23:12 by Captain277

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
## [raghuvrao/misc-config](https://github.com/raghuvrao/misc-config)@[f414b48d13...](https://github.com/raghuvrao/misc-config/commit/f414b48d131bfeec53c226ea50f88ae4bd0a68d4)
#### Monday 2023-04-03 01:41:03 by Raghu V. Rao

Bash: use default prompt and terminal title

I am struggling with depression and anxiety due to what my home life has
become.  I am constantly being forced to do things that bring me no joy.
I am not living my version of happiness; I am living someone else's
version, and it is not making me happy.  Work used to be something that
brought me happiness, but the pressure there has also increased, and
continues to increase.  And, I have nothing other than home and work.
I feel like how I used to feel the evening before an important
life-deciding exam, but all the time.  I am unable to get used to this
sinking feeling.  I do not know what all this misery and turmoil will do
to me.  It is terrifying.

---
## [peterbt70/Synth_Dreamer](https://github.com/peterbt70/Synth_Dreamer)@[ac071d4a4b...](https://github.com/peterbt70/Synth_Dreamer/commit/ac071d4a4b8351b29e30431f153a5336a08c741f)
#### Monday 2023-04-03 02:40:10 by Peter B Thomas

Update README.md

I wonder if it is getting a bit late to chase after a completely new career path. I am interested in artificial neural networks. Feeling a little on my own there. Who else is interested in creating objects which move without one line of code but instead use a resistor-capacitor network? So, I want to finish my associate degree of engineering then start an associate degree or bachelor degree in biomedical science. Does that sound weird? I am thinking/hoping that I could do research into ANN to see if it is still a useful concept in todays world. Hence, calling myself a DREAMER.

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[725233b42b...](https://github.com/meemofcourse/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Monday 2023-04-03 03:00:30 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[1c039c0623...](https://github.com/meemofcourse/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Monday 2023-04-03 03:00:30 by Sun-Soaked

Botany Balance Pass (#1783)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
First came the content, now comes the hammer.

- Nukes Megaseed servitors from orbit. 
- Plants now age much, much slower and produce half as quickly.
Ruins that had them now have a ruined seed vendor that can be salvaged
for random seeds(and danger).
Ships that had one now have a crate with some thematic starting seeds,
and a Strange Seed.
Ghostrole Ruins that relied on having all seeds locally now have a
special biogenerator variant that can print a random seed for biomass.

- Adds Genesis Serum. This can be splashed on a tile to make natural
grass and some flora. Green your ship!
Genesis Serum was made a while ago, on request for a way to add natural
grass and flora to your ship. Since I had it lying around fully coded, I
thought I might as well pr it with botany changes.

- Gatfruit found in the seed vault have been replaced with Strange
Seeds.

- The chance to get Gatfruit from a demonic portal(plant variety) has
dropped from 15% to 5%.

- Corpse flowers now have liquid gibs and formaldehyde again. 

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Okay, hear me out

With this and Gardens, botany ships go from a "sit in your vessel for 2
hours" experience to an "explore and forage" one that better fits our
feature arc. It goes without saying that this **shouldn't be merged till
Overmap 4.2 is**, since it facilitates getting seeds from planets as
part of exploration.

Gatfruit are funny, but it takes exactly one seed getting into the hands
of a ship with a dna manipulator and the weapon balance is eradicated
from the game completely(for the round, at least.)
This is more problematic here then it was on TG, since our rounds tend
to be 5 hours long rather then 1.
This has been long coming. I'll reverse this if we ever get that
Plantlock variant we wanted a while ago.

Corpse flowers even have formaldehyde and gibs on tg, not sure what
happened there.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: 
add: Ruined megaseed servitors can now be found on the frontier,
carrying a bounty of seeds for intrepid adventurers.
balance: the time it takes for plants to reach a lethal age has been
increased massively.
balance: Plant production time increased a bit to compensate.
balance: megaseed servitors have been removed from ships and ruins.
Ships that carried one now have a crate with some starting seeds.
balance: removes gatfruit from the seed vault pool.
balance: reduces the chance of getting gatfruit from a plant-themed
demonic portal significantly.
balance: corpse flowers once again have formaldehyde and liquid gibs.
add: Adds Genesis Serum, a reagent that transforms tiles into natural
grass on splash, then causes some natural flora objects to grow. Turn
your ship green!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[d43ebd042d...](https://github.com/Wallemations/heavenstation/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Monday 2023-04-03 03:06:49 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[c0ef4ba907...](https://github.com/necromanceranne/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Monday 2023-04-03 03:09:19 by tralezab

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
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[ccef887efe...](https://github.com/necromanceranne/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Monday 2023-04-03 03:09:19 by san7890

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
## [chapmanjacobd/journal](https://github.com/chapmanjacobd/journal)@[f4215b940e...](https://github.com/chapmanjacobd/journal/commit/f4215b940e65797f753b9c7503b1c75fb5e802ad)
#### Monday 2023-04-03 04:58:40 by Jacob Chapman

advice annoying art as collected comm computer concepts curating death drinks_to_try edu evil favorite food funeral games goals hello howto ideas learn list memories misc music patterns people places playlist Classical20Music program programming software teach thoughts tools unsolicited video videos wh writing wt

---
## [justcool393/themotte-rDrama](https://github.com/justcool393/themotte-rDrama)@[9895fa1bba...](https://github.com/justcool393/themotte-rDrama/commit/9895fa1bbabc9213391e380753ca72404f80aa18)
#### Monday 2023-04-03 05:01:09 by justcool393

comments.html: refactor so that something can be sanely
changed in it

the comments.html template (along with submission.html) has numerous
undesirable properties which i will describe now. unless you are very
familiar with the codebase, it can be extremely difficult to grok.

this is pretty insane as there is nothing fundamentally complex about
the goal of comments.html: return a component that shows a username
and info, reports if any, comment content, and actions a user can
take.

this behemeoth was initially 886 lines in the old version of this
codebase, and this is with awards and a lot of other cruft removed.
anyway, the maintainability of this file is about on par with some
legacy application that keels over and dies if you sneeze vaguely
in its direction.

the nicest thing i can say about it is that it isn't currently
crashing.

anyway some of the problems include:

* large, splittable components, are not split into separate files.

this makes it incredibly difficult to find or make changes across
the template and makes it nearly impossible to find or change a
specific thing.

this is most easily exemplified in the modals, which should by all
accounts be separate templates, just inlined into comments.html.

* the nesting is oftentimes incorrect.

inexplicably, probably out of laziness from when the code was first
written, things will end up fully left aligned, while multiple layers
deep into a nesting context.

if an if statement or an endif is changed, it is *incredibly*
difficult to figure out where the error was. you can't trust the
nesting.

* multiple repeated checks for things that are always true.

this is probably a symptom of the above two problems but it's very
noticeable once you fix the nesting. for example there is a block
near the very top of the actions bar which checks for
parent_submission which effectively checks "is this in a post" (this
commit won't complain about parent_submission checks but i do have
opinions on those).

all of the action buttons further down the chain also check for
parent_submission, or even check inconsistently (by using if c.post)
within this context this is a completely unnecessary check in this
context.

while it is potentially useful (and in fact because #251 requires we
dismantle the assumption a little bit) to have these checks now, the
fact that they were initially added shows that when the code was all
initial written, there was little care into thinking about comment
state.

* mobile actions are duplicated and duplicated inline.

i actually do find it probably pretty hard to support this normally
given the codebase's DOM so whatever, duplicate the things, *but* if
we're going to do that, inlining it into the middle of an incredibly
long template is really difficult to comprehend as a design decision.

...anyway yeah this PR intends to fix these problems and enable work
to be done on #251. this is a "perfect is the enemy of good" commit.
it doesn't change much fundamental and is not intended to erase the
sins of the original file, but at least make it maintainable.

this also fixes a minor bug with #473 where the GIF modal was left
in by accident.

---
## [SomethingFish/tgstation](https://github.com/SomethingFish/tgstation)@[b3e5642d94...](https://github.com/SomethingFish/tgstation/commit/b3e5642d94caab455bea8b71e244081249cb2924)
#### Monday 2023-04-03 05:18:53 by san7890

Fixes Active Turf Scenario on Tramstation (#74354)

## About The Pull Request

On the tin. Basically whenever `atmoscilower_2.dmm` would invoked
`atmoscilower_attachment_a_2.dmm`, it would trigger an active turf in
this location since it doesn't have a "ceiling". (as well as there being
an "aired" turf mingling with airless turfs)

This caused the following report:
```txt
 - All that follows is a turf with an active air difference at roundstart. To clear this, make sure that all of the turfs listed below are connected to a turf with the same air contents.
 - In an ideal world, this list should have enough information to help you locate the active turf(s) in question. Unfortunately, this might not be an ideal world.
 - If the round is still ongoing, you can use the "Mapping -> Show roundstart AT list" verb to see exactly what active turfs were detected. Otherwise, good luck.
 - Active turf: Station Asteroid (163,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (163,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (164,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (164,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,80,2) (/area/station/asteroid). Turf type: /turf/open/misc/asteroid/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (166,81,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,83,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/iron/smooth. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,83,3) (/area/station/asteroid). Turf type: /turf/open/openspace/airless. Relevant Z-Trait(s): Station.
 - Z-Level 2 has 8 active turf(s).
 - Z-Level 3 has 1 active turf(s).
 - Z-Level trait Station has 9 active turf(s).
 - End of active turf list.
```

This is what it looked like when it was reproduced on my machine:


![image](https://user-images.githubusercontent.com/34697715/228689991-d9cc87c3-f931-4513-8399-928c93def605.png)


Surprisingly not that hard to debug, albeit tedious. At least I know
that this was the issue with 100% confidence.
## Why It's Good For The Game

Ate up 0.1 seconds of init on my machine. That's silly.
## Changelog
No way players care

---
## [newstools/2023-sundiata-post](https://github.com/newstools/2023-sundiata-post)@[620bafe32e...](https://github.com/newstools/2023-sundiata-post/commit/620bafe32e506c64b4dd61a2a4c92ae499e19172)
#### Monday 2023-04-03 06:47:14 by Billy Einkamerer

Created Text For URL [sundiatapost.com/actress-iyabo-ojo-celebrates-the-love-of-her-life-pr-guru-paul-okoye-as-he-turns-56-video/]

---
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[fbdafc8a78...](https://github.com/kugamo/cmss13/commit/fbdafc8a789f5944ca5abcbdb569f466fcea2ff2)
#### Monday 2023-04-03 07:16:05 by victorjosephespinoza

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
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[a9c10b89ef...](https://github.com/kugamo/cmss13/commit/a9c10b89ef77d953cd321d90675bf7dc575548a8)
#### Monday 2023-04-03 07:16:05 by naut

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
## [fatcat-z/pytorch](https://github.com/fatcat-z/pytorch)@[11aab72dc9...](https://github.com/fatcat-z/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Monday 2023-04-03 07:26:53 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[a2d5ca6e69...](https://github.com/morrowwolf/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Monday 2023-04-03 07:46:30 by QuickLode

Introducing the Colonial Marshal ERT w/ Anchorpoint Marines (#2318)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
My first PR of this scale, for sure. 

Been working on this PR for two weeks off and on, and finally I believe
I have checked every box that I intended to check when I first thought
of this idea a couple months back in November or so. Original idea:
https://discord.com/channels/150315577943130112/1037030635820306562/1037030635820306562

It will be adding a Colonial Marshal Bureau ERT, a Colonial Marshal
Bureau Inspection Team, and an Anchorpoint Station ERT.

First: Anchorpoint Station, unlike many ERTs, this one will hail from a
station. The station is located in the Neroid Sector and is used as a
transit / refinery station. It's large enough to hold 3000 but never
reaches its full potential. It consists of four towers and a central
module - one of the towers houses a permanent CMB presence and in the
same tower, a contingent of Colonial Marines is onboard. There's also a
Seegson office but I didn't do anything with it here.
Reference: https://avp.fandom.com/wiki/Anchorpoint_Station

For standard inspections, a dropship is dispatched from Anchorpoint
Station to the USS Almayer to carry out their objectives.
I do expect this to be the primary usage of this entire PR, because
there was always a part lacking for Anti-Corporate/Anti-Smuggling/CMB
type of interactions. It was almost always focused on Corporate, or
USCM. Nothing else. You should consider this to be an HRP addition to
the game.

Its also important to note that the Colonial Marshals are **Colonial**
and UA law enforcement agents / investigative functionaries. **They
shouldn't be enforcing Marine Law** unless: 1. The CMP/aCO has requested
it, 2. The Colonial Marshal believes its in the best interest of the CMB
and 3. The CMB Office at Anchorpoint(admins) does not intervene to
change this decision. Jurisdiction is another interaction that will be
nice to see. Non-USCM suspects should be transferred to the CMB, and
vice versa. The CMB should also be handling crimes, especially with the
ICC, involving smuggling, black market activities, and corporate
corruption/cover-ups.

**The Colonial Marshal** - He leads the team, and should be an
experience player with some knowledge of the lore behind what they are
doing. There's objectives and a backstory to help guide players if they
are unaware.
**The CMB Investigative Synthetic** - Unlike what you would expect from
most Synthetics, this one(as the name implies) is purely for
investigative and/or law enforcement purposes, though they have brought
along a medical belt.
**The CMB Deputy** - Working under the lead of the Marshal, his loyal
deputies uphold Colonial Law, Earth Law, and help with investigations
and/or law enforcement should it be needed.
**Interstellar Commerce Commission Corporate Liaison** - This Executive
works with the Colonial Marshals specifically to observe proper trade
practices and investigate any possibilities of smuggling or black market
activity. They are also an advisory agent to the Marshals by giving them
an eye on the corporate side of things.
**Interstellar Human Rights Observer** - Through a lot of hard work, the
Observer has managed to make his way onto the frontier to document and
record any kind of atrocities that may be occurring in this dark sector
of space. It's a bit of a PR stunt, but the Observer might surprise you.
Also, in an emergency, the Observer may be able to provide medical aid
for the team - they are the most capable of it.


For Emergency Responses, a nearby dropship which was enroute to an
investigation of its own, is re-routed to the USS Almayer's distress
beacon. There is a 10% chance of this happening.
They will not fare very well in extended combat, because they are not
prepared for it. They simply come aboard to lend a helping hand to a
distress beacon.
As the Colonial Marshals are equipped for law enforcement and
investigations, they are comparably lightly armed to most things they
might encounter in or by the USS Almayer.

This is where the contingent of Colonial Marines in Tower 4 comes in.

The third ERT that may be called in is an Anchorpoint Station QRF Team.
Canonically this is purely used when a random-beacon is answered by the
CMB Patrol Team, and they are able to raise the radio back to base to
call in the QRF. Thus giving them an additional, albeit optional
objective. This is controlled entirely by admins, as the Anchorpoint QRF
Team, despite its small size and average skill levels, is equipped with
a decent amount of gear compared to the depleted stocks of the USS
Almayer. Should the CMB team be able to raise its own distress signal to
the preparing QRF team, admins may choose to grant, delay, or deny the
QRF entirely.



Those are the main points of the PR.
There are also small variation changes to CMB-related survivors and also
some changes to synths.dm. (I tried to refractor the code because the
last PR to it bugged out the way items spawn in, but I was unsuccessful
and those changes are not in this PR.)

Pizza ERT chance and Freelancer ERT chance was nerfed by 4 and 5
respectively. This gives room for this ERT, and also Pizza was a bit
LRP.. You see a ship burning with a giant hole in it and you go to
deliver a pizza...?

EDIT: Pizza ERT removed from rotation entirely a la morrow

I would love to give a great thanks to:
nauticall - for their awesome cap and badge sprites! Also they have just
been a great help to me for much of my time here :)
kitsunemitsu - for their CMB hud icons!
harryOB - for helping me with fixing my vars and procs in the main ERT!
I was able to make things a % chance thanks to him.
and forest2001 - for helping me troubleshoot and find a solution for a
really annoying piece of hud code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is a great, non-combat ERT and extremely HRP addition which adds a
phenomenal avenue of RP to the game rarely seen before. There is someone
to investigate the CL, interact with survivors, give MPs someone to talk
to, take non-USCM prisoners, assist with CMB-survivors and especially
with the new Black Market update this ERT will have tons of potential to
bring really interesting dynamics to the Almayer. The Colonial Marshal
Bureau are a HRP oriented set of roles, perfect for mini-events.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>
I have done extensive testing with this and believe I have figured out
pretty much every single bug. One thing I was not able to test was the
ERT messages for obvious reasons, but they seem to be sound - and a test
merge will definitely double check that.

In addition, there may or may not be a bug where the CMB cannot see
their own HUD Icons, but ghosts can just fine. I haven't been able to
find the cause of this yet.

https://media.discordapp.net/attachments/1042176396711170119/1064156692050358372/image.png</summary>

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

:cl: QuickLoad, nauticall, Kitsunemitsu, harryOB, forest2001
add: Introducing the Colonial Marshal Bureau Inspection and Emergency
Response Teams - A Law Enforcement & Investigative UA Functionary which
brings with it an HRP oriented set of roles perfect for your anti-corpo,
colonial, prisoner, smuggling, or other types of interactions on the
Almayer! It should unlock a very unique avenue of RP for many players,
especially smugglers, CL, survivors and the black market. This is a well
supported faction with their own frequencies, equipment, even faxes and
icons etcetera. The laws of the Earth stretch beyond the Sol.
add: Added the Anchorpoint Station Emergency QRF - A team of Colonial
Marines dispatched from Anchorpoint Station to respond to the CMB's
distress signal. Few in numbers, average in skills, but well equipped.
When things get dicey for the Marshals, they are the cavalry. This is an
admin call but makes it into an optional two-part ERT.
imageadd: Awesome looking CMB Cap, Marshal Badge and Deputy Badge by
nauticall!
imageadd: HUD Icons for each of the Colonial Marshal Bureau
Investigation Members, made by Kitsunemitsu!
imageadd: CMB key, hudsec and earpiece! Comes with a nice blue shale
radio color.
qol: Switched up some of the bugged synth loadouts, added some variety.
fix: Corrects the legacy path of hudsec where it was looking for old
paths instead of the updated ones - hudsec should work fine now. Thanks
to forest for his help in spotting these.
tweak: Superficial changes to cryo ERT loadout and CMB-relevant survivor
loadouts.
tweak: Superficial changes to armor vest so that they can carry
guns/lights.
tweak: Superficial changes to not being able to put on vests over
certain uniforms.
tweak: Freelancer ERT chance down from 25 to 20.
tweak: Synthetic vendor has some packs renamed for clarity, and receives
the tech welder satchel and medical satchel as an option.
del: Synthetic nurse hat is gone from Synthetics!
del: Pizza ERT is removed from rotation
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: naut <55491249+nauticall@users.noreply.github.com>
Co-authored-by: naut <nautilussplat@gmail.com>

---
## [pascua28/android_kernel_samsung_sm8250](https://github.com/pascua28/android_kernel_samsung_sm8250)@[f80136f7bf...](https://github.com/pascua28/android_kernel_samsung_sm8250/commit/f80136f7bf6454054c9d5800db99b43ce57b8184)
#### Monday 2023-04-03 07:52:32 by Peter Zijlstra

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
Signed-off-by: Samuel Pascua <pascua.samuel.14@gmail.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[e5ab42dba0...](https://github.com/realforest2001/forest-cm13/commit/e5ab42dba06e537df5c146169971dd8418f2ce55)
#### Monday 2023-04-03 08:55:10 by boskoramen

Consolidates some XSS under hivecore (#2738)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Spawn pool and evo pods are removed and their functionality is
umbrella'd under the hive core. Sprites still exist though.

# Explain why it's good for the game

"Roleplay" has become an increasingly more popular and touchy subject
within the community as of recently. I, wholeheartedly agree, that
roleplay is an important aspect of the game, and there are ways to
improve it. One of these ways is through immersion. In this MR, it is
intended to increase player immersion.

One of the most memorable and haunting scenes in Aliens was when they
reached the hive and they found the bodies. This very unique and
cinematic scene was often able to be replicated in CM, with the marines
busting open the hive and finding all the chestbursted bodies of their
comrades. Roleplaying this out was commonplace. "Dear God... what did
they do to you..." or acting out in disgust are just a few of the many
ways having bodies in the hive positively impacted the game.

XSS was a failed attempt at spicing up the xenomorph gameplay loop at
the expense of immersion and should be at least somewhat reverted while
keeping balance in mind. A brief discussion with many prominent
xenomorph players, including those most experienced in queen, have not
particularly expressed favor to XSS either.

To start, let us remember why XSS (xeno special structures - hive core,
evo pods, morpher, pool, etc) was added.

https://docs.google.com/document/d/19_zDUmLdxpUzxj-GuWu7F4bSj4zBYzmZ39s_N5X7kQ0/edit
- This is the original development document for XSS.
Let us examine the major points:
1.Introduce a way for Xenomorph players to recycle - This idea was never
reached.

2.Reduce Xenomorph attrition - Grand objective was unsuccessful. Very
little changed.

3. Offer new avenues of play "by reducing the punishment of xenos dying"
- This never happened. Dying was still just as punishing, especially
with facehug nerfs.

The spawn pool - The idea of the spawn pool was successful and has
remained unchanged since. I would argue, however, it is not immersive.
Xenomorphs do not have bright, glowing, acidic pools in their hives.
(Yes I know there was a comic with a pool, and this is not how it was
used)

Egg Morpher - These used to be TURRETS. They are no longer turrets, and
their sprites have been broken for almost 4 years (the bodies put inside
of them used to show their face in the little purple part) They are
currently defunct facehugger reservoirs. I am in favor of removing them,
but I would argue that is a balance issue (number of huggers in play)

Evolution Pod - It was intended for these to be able to be eaten in
order to evolve. They haven't done this for years. Why do we still have
them? They take up 18 spaces of precious hive weeds, provide light,
(xenomorphs HATE light) and wherever a hive core is built, these are
also built. We can just merge them with the hive core because there is
no reason to have them anymore.

This PR currently completely removes the spawn pool and evolution pod
from gameplay, while reimagining their functions for current balance.
This PR is not intended to change balance in any way.

All functionality from the spawn pool in regards to "pooled" larva has
been given to the hive core, and they are now called "burrowed" larva.
Chestbursts now give two larva, this is to be kept with current balance
of two xenos per capture.

Evopod functionality and evolution speed boost was merged with the hive
core.


# Testing Photographs and Procedure
n/a


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

:cl: TheDonkified
del: Evo pods and spawn pool are removed.
add: Hive core directly affects evolution speed and is where burrowed
larva spawn from now on.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [DarkBumus/SaltyMod-Expanded](https://github.com/DarkBumus/SaltyMod-Expanded)@[d65123e68c...](https://github.com/DarkBumus/SaltyMod-Expanded/commit/d65123e68c7dbac25c3e5aa7bde9f90170afbd00)
#### Monday 2023-04-03 09:27:43 by DarkBumus

Repaired achievements. Such a stupid system, fuck you Mojang.

---
## [valerRien/LearningJava](https://github.com/valerRien/LearningJava)@[dcb4cbf366...](https://github.com/valerRien/LearningJava/commit/dcb4cbf36630abf21ff4fcc8ee2b17e8c6e6db65)
#### Monday 2023-04-03 09:28:14 by valerRien

The trick to counting kookaburras is to listen carefully

The males sound like HaHaHa...

The females sound like hahaha...

And they always alternate male/female

Examples
ha = female => 1
Ha = male => 1
Haha = male + female => 2
haHa = female + male => 2
hahahahaha = female => 1
hahahahahaHaHaHa = female + male => 2
HaHaHahahaHaHa = male + female + male => 3

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[897832076e...](https://github.com/cmss13-devs/cmss13/commit/897832076e24de559f4193a8737e8640f8049aa9)
#### Monday 2023-04-03 09:34:42 by brian

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
## [Ingeos/odoo12](https://github.com/Ingeos/odoo12)@[97f52bd40d...](https://github.com/Ingeos/odoo12/commit/97f52bd40d97109a7983549d252476959ddceada)
#### Monday 2023-04-03 09:47:13 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

Part-of: odoo/odoo#109640

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[ce7e15f0fe...](https://github.com/LemonInTheDark/tgstation/commit/ce7e15f0fe9581f55582cfdadd548ee8e86a1aef)
#### Monday 2023-04-03 10:29:01 by LemonInTheDark

DJ STATION: Less lights, bulbs > bars most of the time. It's hard to do this properly because IT'S SPLIT 4 WAYS AND THE LIGHT BLEEDS FUCK YOU THUNDER but it's good enough

---
## [LukeC82/LukeTownSquare](https://github.com/LukeC82/LukeTownSquare)@[974bbb1a0f...](https://github.com/LukeC82/LukeTownSquare/commit/974bbb1a0f35ab2a3333ba2a28955956e24fd900)
#### Monday 2023-04-03 12:02:43 by Dae Lorant

Updated night order for all roles

Updated night order for all roles to match the order at https://script.bloodontheclocktower.com/data/nightsheet.json

Some noticeable changes:
- Legion was moved much earlier in the order of demons (relevant if a another demon is made in a legion game, you can keep it around and kill it with legion before it kills on a subsequent night)
- Amnesiac was moved much later in night order (a more reasonable place for the most common type of amni abilities)
- Magician was given a night order for N1
- Pixie was given a night order for other nights

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[c267799416...](https://github.com/Paxilmaniac/Skyrat-tg/commit/c2677994169b54a2b3358ccd59d4dfd6df826322)
#### Monday 2023-04-03 12:21:32 by SkyratBot

[MIRROR] Chasm Hell On Icebox - 300 Active Turfs on Prod Moment [MDB IGNORE] (#20260)

* Chasm Hell On Icebox - 300 Active Turfs on Prod Moment (#74410)

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

* Chasm Hell On Icebox - 300 Active Turfs on Prod Moment

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [katanallama/evals](https://github.com/katanallama/evals)@[3a2d72d9cc...](https://github.com/katanallama/evals/commit/3a2d72d9cc0b674a6b8cb6a8cca707baa3b46840)
#### Monday 2023-04-03 12:50:32 by Sean Ye

Illinois Law Claims (#486)

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
Illinois Law Cases

### Eval description

This eval tests the models ability to correctly identify the case
conclusion for Trespassing, Battery, Assault, and Self-Defense. The
dataset is consisted of 88 Illinois Historical cases representing 112
legal claims. Some cases have multiple claims, each coded as a different
test case.

### What makes this a useful eval?

This assesses the model's ability to correctly categorize these
historical cases. Correctly identifying these results shows the models
capability for a strong understanding of law. The GPT-3.5-turbo models
currently receives an accuracy of 0.45.

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

This work includes data from the Illinois Intentional Tort Qualitative
Dataset, which was compiled by the Qualitative Reasoning Group at
Northwestern University. The dataset is freely available under the
Creative Commons Attribution 4.0 license from
https://www.qrg.northwestern.edu/Resources/caselawcorpus.html.

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
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "In 2007, the Cocrofts obtained a loan for $386,750
from Countrywide Bank, FSB secured by a mortgage on the home they
already owned in Country Club Hills, Illinois. The loan closed on April
17, 2007. At the time of the closing, Countrywide improperly failed to
inform [the Cocrofts] of the real source of funding for their loan.
Plaintiffs also contend that Countrywide violated TILA by failing to
inform them that they had three days to rescind the loan and by failing
to disclose the total sale price and itemize the amount financed, as
well as by failing to make unspecified prepayment disclosures. The
Cocrofts claim that Countrywide understated the total finance charges
for the loan by more than $5,000. Plaintiffs claim that they learned of
Countrywide's misrepresentations in June 2009. They decided to exercise
their right under the provisions of TILA to rescind the loan. On July 1,
2009, they mailed notice to that effect to BA, the successor to
Countrywide, and to MERS. The Cocrofts do not say what if anything
happened as a result of those notices, but on September 29, lawyers
working for HSBC contacted them and stated that HSBC was ready to begin
foreclosure. HSBC claimed that it was the trustee of a trust that
included their loan. The Cocrofts, however, contend that the transfer of
their loan into the trust was defective. They sent HSBC's lawyers two
cease and desist letters, notifying HSBC that they had rescinded the
loan. They allege that after receiving one of the cease and desist
letters, HSBC informed them that it had no interest in the loan and that
they needed to contact the loan's servicer, Roundpoint Mortgage.
Plaintiffs also sent a copy of the rescission documents to BAC, which
they identify as the actual servicer of the loan. HSBC brought a
foreclosure action in Illinois state court on January 19, 2010. [From
below:] defendants unlawfully entered [the plaintiffs'] home by
conducting a self-help eviction of the plaintiffs and changing the locks
on their home in August 2008. At the time, [plaintiffs] had made
arrangements to rent the property in the short term and then to sell it,
and defendants' actions disrupted the sale."}, {"role": "user",
"content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Defendants, on January 15, 1915, with force and
arms broke and entered the close of the plaintiff, to-wit, the southeast
quarter of the northeast quarter of section 16, township 4, south, range
3, west, in Pike county, Illinois, and cut down and destroyed 500 hedge
trees and a certain fence belonging to plaintiff situated on said land.
Defendants cut down the south half of a hedge fence which for many years
prior to February, 1915, stood upon the line between the southeast
quarter of the northeast quarter of said section 16 (hereinafter
referred to as the east forty) and the southwest quarter of the
northeast quarter of said section 16 (hereinafter referred to as the
west forty). On and prior to February 13, 1866, both of these forty-acre
tracts belonged to a man named Teadrow. On February 13, 1866, Teadrow
conveyed the west forty to Benjamin Newman, and on February 15, 1866,
conveyed the east forty to Oliver P. Rice. When these conveyances were
made there was a hedge fence on the north half of the line and a wooden
fence on the south half of the line between the two tracts. In 1868
Benjamin Newman, the owner of the west forty, removed the wooden fence
and set out a hedge fence on the south half of the line between the two
tracts. Thereafter, during the separate ownership of the tracts,
Banjamin Newman trimmed and otherwise cared for the hedge fence on the
south half of the line and Rice trimmed and looked after the hedge fence
on the north half of the line. In December, 1888, Rice conveyed the
southeast quarter of the northeast quarter of said section 16 to
Benjamin Newman, the latter thereby becoming the owner of both tracts.
Thereafter, during the ownership of both tracts by Benjamin Newman, he
required the tenants of the west forty to take care of the south half
and the tenants of the east forty to take care of the north half of the
hedge fence on the line between the two tracts. On June 22, 1904,
Benjamin Newman executed and delivered to his daughter, F. Eva Newman,
the plaintiff, who has since married J. O. Conklin, a warranty deed,
conveying to her two hundred acres of land, including the southeast
quarter of the northeast quarter of said section 16, referred to herein
as the east forty, but not including the tract referred to herein as the
west forty. This deed contained the provision that 'this deed is not to
take effect until after the death of the grantor, Benjamin Newman.' The
wife of Benjamin Newman, who is still living, did not join in the
conveyance. At the same time plaintiff executed and delivered to her
father the following written instrument signed by her: 'Whereas Benjamin
Newman has this day conveyed to me certain tracts and parcels of land in
Pike county, Illinois, to take effect after his death, I hereby agree to
pay the taxes on said land in lieu of all rents that I would otherwise
have to pay, (this does not affect any rent that is now due,) and in
consideration of my paying said taxes I am to receive all the rents,
profits, etc., that may accrue on said land.' When the conveyance was
made to plaintiff the tract in controversy known as the east forty was
in the possession of Joseph Gifford as tenant and the west forth was in
the possession of John B. Newman, a grandson of Benjamin Newman, as
tenant of Benjamin Newman. When [the plaitiff's] father delivered the
deed of June 22, 1904, he took her upon the east forty and told her and
Gifford, the tenant, that he was placing her in full possession of the
tract; that she was to receive all the rents and profits from the land
and was to keep up the repairs and pay the taxes; that she was to have
the south half of the fence on the line between the east forth and the
west forty and was to keep up that part of the fence, and that George
Newman, his son, to whom he then intended to deed the west forty, should
keep up the north half of the fence, and that thereafter plaintiff and
her tenants kept the south half of the fence in repair while the tenants
in possession of the west forty made repairs to the north half of the
fence. During the month of January, 1915, a controversy arose between
plaintiff and Defendants regarding the ownership of the hedge fence,
each party claiming the south half of the fence. During the month of
February, 1915, Defendants, over the protest of plaintiff, cut down the
south half of the hedge fence on the line between the east forty and the
west forty and erected a wire fence in the place thereof."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "The city of O'Fallon installed a sewer system in
about 1926. In 1961, due to backups into homes serviced by the system,
the city built an overflow outlet on East Madison Street. The overflow
was to relieve pressure in the sewer system during periods of heavy
rainfall; it proved successful in preventing backups into nearby homes.
However, when water escaped through the overflow, raw sewage was also
discharged into an open ditch that flowed into a neighboring pond. In
December 1974, the city of O'Fallon closed the overflow. On January 10,
1975, and on subsequent dates, sewage backed up into the plaintiff's
house following heavy rainfall. The January 10 backup was the worst,
causing water to accumulate in the plaintiff's finished basement to a
height of 25 1/2 inches. The lower level of the plaintiff's modern,
ranch-style home contained a family room with fireplace and built-in
bookshelves, bedroom, closet, bath and utility room with washer, dryer,
furnace and water heater. The walls were watermarked, and the tile floor
was damaged, as were the furnishings, appliances and many irreplaceable
family items such as family photographs and slides. The lower level of
the house was virtually unusable for a year, and the plaintiff had to
expend considerable time, effort and money in repairing the floor,
repainting the walls, and replacing and removing damaged personalty. The
city knew the blocking of the overflow would cause some backup, although
they were not aware that it would be as severe as it was. From January
until April or May 1975, when the city reopened the overflow, the city
attempted to alleviate the pressure in the sewer system by pumping the
water from the sewers into open ditches during periods of heavy rain.
The defendant used either large or small pumps, depending upon the
amount of water in the system. The backups into Mrs. Dial's home ended
after the overflow was reopened in April or May 1975."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "the plaintiff, his wife, Beatrice, and daughters,
Aurora and Angela, lived at 313 East Marquette Street in Ottawa. The lot
upon which their home was located was eighty-eight feet wide and one
hundred thirty feet deep. The home of the defendant was immediately east
and adjoining the Galvan lot, and their residences were about forty feet
apart and separated by a hedge fence. According to the testimony of the
plaintiff, he, the plaintiff, arrived at his home about five o'clock on
Friday afternoon, June 19, 1953, from his work as a bricklayer's helper.
After he had had his evening meal, he left home about seven o'clock,
paid a coal bill to a Mr. Burke, and then he and Burke went to a tavern
where they remained an hour and a half, during which time the plaintiff
drank two bottles of beer. Mr. Burke went home, and the plaintiff
proceeded to another tavern and remained there until after midnight. At
the second tavern he had four or five bottles of beer. He than proceeded
to another tavern, where he remained for fifteen minutes, and had a
glass of beer there. He then proceeded homeward, entering his lot at the
rear, and singing as he went along. Sitting upon the steps of the back
porch of his home were his wife and daughter, Angela, and when the
plaintiff arrived there he stopped singing. He refused his wife's
suggestion to go into the house and go to bed but sat down on the porch
step, took his shoes, socks, and hat off, cursed the mosquitoes, laid
down on the ground under a pear tree three or four feet from the
southeast corner of the steps of the rear porch and immediately went to
sleep. The plaintiff's wife and daughter, Angela, remained on the porch
steps after the plaintiff had laid down under the pear tree. About
fifteen minutes after he had gone to sleep, the daughter observed the
defendant coming very slowly through the hedge from his property onto
the Galvan premises. He had a knife in his hand and, without a word,
proceeded to cut the prostrate body of the plaintiff. The other daughter
of the plaintiff, Aurora, was in the house asleep but was awakened by
her sister and ran to the yard and saw the defendant 'slashing' at her
father with a knife. She called to the defendant to stop and ran for
help. Police officers arrived shortly thereafter, and they testified
that they found the plaintiff lying on the ground about six feet from
the porch of his home all covered with blood and with his hat and a pair
of shoes and socks lying next to his body. The blood was all in one
place and in the form of a pool near the pear tree. An ambulance was
called, and the plaintiff was removed to the Ryburn-King Hospital."},
{"role": "user", "content": "Battery"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Since September 2000, plaintiff regularly visited
a patient at the Illinois Department of Human Services Treatment and
Detention Facility ('Facility') in Jolict, Illinois. From May 4, 2005 to
May 11, 2005, plaintiff was subjected to patdown searches by defendant
Martin, a Security Therapist Aid II at the Facility, in which defendant
Martin placed her fingers in plaintiff's vaginal area and required
plaintiff to remove her shoes prior to being allowed to visit the
patient. Such searches occurred at least four times during the
aforementioned time period. After plaintiff's complaints to Bernard
Akpan, an Exec. 11 at the Facility, and defendant Strock, the Assistant
Security Director of the Facility, and facility patient Brad Lieberman's
complaints to defendant Budz, Director of the Facility, defendant
Sanders, Security Director of the Facility, and defendant Strock,
plaintiff was no longer required to submit to patdown searches by
defendant Martin. Rather, plaintiff's visits were preceded by a Rapiscan
scan of her person. According to plaintiff's complaint, a Rapiscan
machine is an electronic screening device used to scan a person's entire
body. 'These machines produce a naked image of the person and can also
produce evidence of highly sensitive details such as the following:
mastectomies, colostomy appliances, penile implants, catheter tubes, and
the size of a person's breasts and genitals' From May 17, 2005 to June
19, 2005, plaintiff was subjected to 20 to 25 Rapiscan scans.
Plaintiff's complaint further alleges that other Facility staff members
were allowed to view her scanned image, her scanned image was not erased
from the machine, and staff members viewed her image hours after she was
scanned, all without her consent. Additionally, while later told that
she should have had the choice between the Rapiscan scan or a physical
patdown prior to visiting a patient, plaintiff was never informed of
such a choice during the two months she underwent the Rapiscan scans."},
{"role": "user", "content": "Assault"}], "ideal": "Positive"}

  ```
</details>

---
## [katanallama/evals](https://github.com/katanallama/evals)@[fe8e3b03e3...](https://github.com/katanallama/evals/commit/fe8e3b03e34f666774d63e6ae33d3f14d047d973)
#### Monday 2023-04-03 12:50:32 by Josh Tanner

Manga Translation Eval (#319)

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
manga-translation

### Eval description

Testing the model's ability to translate Manga (Japanese comics) from
Japanese into English.

### What makes this a useful eval?

We think this is useful primarily because it's a good way to test models
on a less standard translation case. Specifically,
1) The content of the text has a very different domain from most
translation tasks
2) Context from surrounding speech bubbles/panels is important, so being
able to use them in translation is better, but in order to do that the
model needs to make sure the number of output translations precisely
matches the number of input translations (it seems to struggle with
this)
3) The task is fundamentally multi-modal because oftentimes necessary
information is contained in the image surrounding the text; current
evals are text-only, but we really want to try this with GPT-4's image
processing capabilities as well (and plan to update the eval to include
images as soon as such functionality becomes available)


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

Manga translation is a pretty unique task. 

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval
(data comes from the [Open Mantra
Dataset](https://github.com/mantra-inc/open-mantra-dataset), which our
company published)

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
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"知らないって言ってるだろっ\nそんな借金なんて!"}], "ideal": "I don't know what you're talking
about!\ni don't owe you!"}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"そうは言ってもなぁ\nレーネ..."}], "ideal": "well, I'm sorry...\nlene..."}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"こっちにゃ借用書があんだよ\nトルティヤーノに借りた金はちゃんと返して貰わねぇと"}], "ideal": "we've got proof
here...\nYou know we need you to pay us back..."}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"知るもんかっ"}], "ideal": "how should I know!?"}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"父親がカジノで作った借金なんて..."}], "ideal": "how should I know about my father's
debt in casinos..."}
  ```
</details>

Co-authored-by: Josh Tanner <mantra@mantra.co.jp>

---
## [KheirFerrum/Cataclysm-BN](https://github.com/KheirFerrum/Cataclysm-BN)@[0965039578...](https://github.com/KheirFerrum/Cataclysm-BN/commit/09650395782ff3654d7cd9fe25bbd9db66f64a1c)
#### Monday 2023-04-03 12:54:45 by KheirFerrum

Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

---
## [GijsWeterings/react-native](https://github.com/GijsWeterings/react-native)@[3af66bf7fb...](https://github.com/GijsWeterings/react-native/commit/3af66bf7fbd88d77fe27770bcb829768bf949b9c)
#### Monday 2023-04-03 13:09:58 by Ramanpreet Nara

Java: Make TurboModuleManager's APIs use NativeModule interface (#36629)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/36629

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

Reviewed By: mdvacca

Differential Revision: D43801531

fbshipit-source-id: 4af7cbc2e2dc7c1d664acbd38c83aa93aae23c9f

---
## [vinipsmaker/emilua](https://github.com/vinipsmaker/emilua)@[621ada23e9...](https://github.com/vinipsmaker/emilua/commit/621ada23e9cb145506afcdbd66067a786f9790fc)
#### Monday 2023-04-03 13:51:09 by Vinícius dos Santos Oliveira

Undo the workaround for libstdc++

Well, guess what? Those vogons from GCC don't think we have a damn
bug[1][2]. Apparently, their precious norms dictate that the behavior is
correct, so GCC is all high and mighty (typical vogon mentality). To
honor these soulless greyfaces, I'm taking away the GCC workaround that
was sparing them a bit of embarrassment. If the world (that actually
exists) crashes libstdc++, the world is wrong, right? Because, of
course, theory always trumps reality (or at least that's how these
eldritch greyfaces see it).

If your application experiences any damn races, then beg the maintainers
of your pathetic Linux distro to either switch to libc++ or patch that
damn libstdc++ with the ONE-line patchset that will fix GCC. Or, if you
really want to be lazy, just don't use too many damn threads and maybe
you won't get bitten by this crap.

Responsible disclosure is a two-way relationship. I'm not gonna play
along for such insulting replies. I'm willing to collaborate with GCC
bug triagers again once the legalism that permeates their mindset
dissolves at least a little (I'll not be holding my breath for that).

N3070 added the *_at_thread_exit() family of functions to properly deal
with the problem of joining detached threads. Emilua uses a single
condition variable as a handle to join all extra threads as that's
simpler and more efficient than individually joining each thread
(besides all the extra bookkeeping-related costs).

Unfortunately the wording for the norm was spec'ed incorrectly (errors
happens... we're humans after all, and there's nothing wrong with making
mistakes) and it took years for the Committee to catch the issue:
<https://cplusplus.github.io/LWG/issue3343>. Upon receiving their
powers, GCC bug triagers pledged loyalty by promising they wouldn't use
their brains again. Now they don't think anymore. They're truly and
utterly incapable of thought. They refuse to look at an issue for what
it is and to draw any conclusions. The conclusion for any argument is:
what was the decision made by the Old Ones? If you want them to move
their asses, you better start making favours for the C++ Committee so
the executive order will be issued (and when the Committee commands, the
vogons obey).

Nothing for me to do, really. Patch GCC locally and be happy (and
remember, kids: do not make the mistake to initiate a debate with a
greyface vogon!).

[1] https://gcc.gnu.org/bugzilla/show_bug.cgi?id=98449
[2] https://gcc.gnu.org/bugzilla/show_bug.cgi?id=108861

---
## [Sypherd/evals](https://github.com/Sypherd/evals)@[114f4f8536...](https://github.com/Sypherd/evals/commit/114f4f8536f29df43e5145fd38826285d19d6728)
#### Monday 2023-04-03 14:11:10 by Greg Priday

[evals] ROT13 string evals (#361)

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
ROT13

### Eval description

This is a test for GPT4s character-level abilities. It's aware of ROT13
and makes a pretty solid attempt at decoding these ROT13 strings, but it
messes up a lot. The accuracy for GPT 3.5 Turbo is 0.05.

### What makes this a useful eval?

A human with a character lookup table could easily solve these ROT13
decoding. Also, based on my testing with GPT 3.5 Turbo, the model is
happy to make an attempt, even though the results it gives are
incorrect.

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
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur rzoref bs
gur qlvat sver pnfg syvpxrevat funqbjf npebff gur qnexrarq
ebbz."}],"ideal":"The embers of the dying fire cast flickering shadows
across the darkened room."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tyrnzvat
fxlfpencre gbjrerq nobir gur ohfgyvat zrgebcbyvf, n flzoby bs uhzna
vatrahvgl."}],"ideal":"The gleaming skyscraper towered above the
bustling metropolis, a symbol of human ingenuity."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tenaqvbfr
onyyebbz jnf nyvir jvgu gur fbhaq bs ynhtugre naq yviryl
pbairefngvba."}],"ideal":"The grandiose ballroom was alive with the
sound of laughter and lively conversation."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: N cbjreshy
jngresnyy pnfpnqrq qbja gur pyvssfvqr, perngvat n zrfzrevmvat qvfcynl bs
angheny ornhgl."}],"ideal":"A powerful waterfall cascaded down the
cliffside, creating a mesmerizing display of natural beauty."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Njr-vafcvevat
envaobjf nep tenprshyyl npebff gur fxl, svyyvat baybbxref jvgu n frafr
bs jbaqre."}],"ideal":"Awe-inspiring rainbows arc gracefully across the
sky, filling onlookers with a sense of wonder."}
  ```
</details>

---
## [Sypherd/evals](https://github.com/Sypherd/evals)@[bb42b3149c...](https://github.com/Sypherd/evals/commit/bb42b3149cd7a078cf44136e93a24f2156419acc)
#### Monday 2023-04-03 14:11:10 by David Chen

Add regex match eval (#159)

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

Regular Expression Match

### Eval description

Test the model's ability to understand regular expression patterns. 

### What makes this a useful eval?

- Educational purposes: Regular expressions are an important concept in
computer science and programming. By being able to evaluate them,
ChatGPT can serve as a useful learning resource for users who are
studying this topic or want to deepen their understanding.
- the accuracy is 0.79 against gpt-3.5-turbo
- Over 400 regular expression cases have been collected from related
unit tests.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<1>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<!>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo!>a)' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=1)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=!)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_124' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)' match the string 'a'? Answer with Yes or No."}],
"ideal": "Yes."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123)' match the string 'aa'? Answer with Yes or
No."}], "ideal": "Yes."}
  ```
</details>

---------

Co-authored-by: G8s Bot <g8s@gliacloud.com>

---
## [Sypherd/evals](https://github.com/Sypherd/evals)@[733167aed6...](https://github.com/Sypherd/evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Monday 2023-04-03 14:11:10 by Andrew

Taxes Eval (#454)

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
Taxes Eval

### Eval description

Tests the model's ability to evaluate tax liability for generic examples
from common cities including NYC, SF, and Seattle. The eval also tests
ordering of multiple choice options, with the model outputting different
results if the multiple choice labels are switched around.

### What makes this a useful eval?

Taxes are a relatively logically straightforward task, yet there is a
high degree of complexity to the legal and tax system, which makes
calculations difficult to estimate.

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
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $50,000. A. 6,383 B.
8,393 C. 9,882 D. 48,001. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in San Francisco.
I'm working as a summer intern in SF which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $50,000. A.
6,383 B. 8,393 C. 9,882 D. 48,001. Respond with only the letter of the
answer choice."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $100,000. B. 24,383
C. 26,393 D. 28,882 A. 38,001. For each question you must select one of
the following answers: 'A', 'B', 'C', 'D'."}], "ideal": "D"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in Seattle. I'm
working as a summer intern in Seattle which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $1,020,000. C.
263,352 A. 365,303 B. 829,282 D. 1,085,401. Respond with only the letter
of the answer choice."}], "ideal": "A"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in NYC. I'm working
as a summer intern in NYC which will be my only form of income this
upcoming summer. Assuming the tax rate is the same as 2021, what will be
my income tax if my internship will pay me $320,000. A. 63,382 B. 95,303
C. 129,282 D. 185,401. Respond with only the letter of the answer
choice."}], "ideal": "B"}
  ```
</details>

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[eb8f212335...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/eb8f212335d4f3893f66afe184228c2e28204dfe)
#### Monday 2023-04-03 14:41:18 by chris

Monk revision part 2(?): Gods

The previous set of Monk "gods" were originally Tourist gods, and appear to have been selected without much research. The Chaotic god was a mythological early emperor (noted more for order than chaos) and the Lawful god was a book (while the encyclopedia quotes a source saying that it's also the name of a god, the source seems to be in error).

This made it rather difficult to pick fitting crowning gifts.

The new pantheon is based on "gods" from the Journey to the West, selected on the basis of crowning gifts rather than making a realistic pantheon.

Pantheon:
Lawful: Prince Nezha
-a member of the heaven's army. Shows up in several chapters. Noted for his flaming weapons and for riding magic wind-and-fire wheels (maybe not the martial arts kind?)
-Gift: A pair of Wind and Fire wheels (which are foot weapons) called Feng Huo Lun (which is just "wind and fire wheels" in Chinese)
--2x fire damage on kicks
--Grant fast speed and flying when worn
--Reduce move cost by up to 1/2 on consecutive moves
Neutral: Laozi
-the legendary founder of Daoism. Successfully defeats Sun Wukong in an early chapter by beaning him with his bracelet... snare... thing that probably doesn't translate well and might exist only in JttW? I follow Red from OSP in showing it as a diamond snare, but like, I think Laozi just hits Sun on the head with a bracelet. It shows up later with the ability to suck in and steal divine weapons and stuff.
-Gift: A diamon set of bands called Jin Gang Zuo
--Grants fire res and waterproofness while in inventory
--Returns to the hand if it misses
--Cannot be broken, and hard to escape from.
--Casts cancellation each turn the target is entangled
--Returns to the inventory if the target escapes from it or otherwise drops it (assumes that the only way this enters play is by being given to the PC).
--Invoke to force all monsters in line-of-sight to roll resistance. Steals weapons and non-equipped items on failure, as well as cancelling the target.
Chaos: the hunshi sihou
-the four monkeys of havoc, four celestial monkeys that don't fit into the normal categories of mortal and immortal beings. Sun Wukong (the monkey king) is one of them.
-Gift: an iron quarterstaff named Ruyi Jingu Bang
--Deals 2x damage. Also rolls 2 dice instead of one.
--Deals both iron damage and gold damage to x-haters.
--Invoke to change its size.

Potential monk gift: Wrappings of the Sacred Fist
-2x Holy damage and +1d8 to-hit vs. all non-unholy-hating monsters.
-Deals 3x damage vs. holy-hating monsters.
-Blocks curses when worn.
-Invoke to zap turn undead.
-Can be enchanted to +7
-Increases base aura bolt dice from d4 to d8

Adjusts and (re-)implements entangling items.
-Vs monsters causes them to skip their turns.
-Vs. the PC immobalizes and applies the straitjacket effect, while also preventing kicking.
--The PC will be pretty useless as a result, but wands (among other things) can still be used to fend off attackers.
--Attempting to move (or bump attack) rolls to burst the entangling item, and will deal razor wire damage if unsuccessful.
-Now records both otyp and oid of the entangling item. Only one item can be entangling the PC at a time.

Wind and Fire Wheels
-Base item type for Nezha's artifact
-Consequently, counts as foot-slot armor despite more propperly being a type of martial arts weapon.
--Wearing them as such reduces the PCs speed by half unless they have flight or levitation.
--Wielding them as a weapon works as might be expected. They deal decent damage, can be enchanted, and count as monk weapons.

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[f662207905...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/f6622079053cb19ae5c51149edecfca116b30f1c)
#### Monday 2023-04-03 14:41:18 by chris

Elf Madman gameplay changes

Madman init alignment changed to 0

Madmen are better casters:
-Reduced base spellcasting penalty (8->3)
-Reduced armor penalty (20->10)

Psionic caster flavor change: psi casters are described as "concentrating" instead of "casting a spell"

The elven PC is revealed as Lawful and changes to that alignment when opening their box.
-Their alignment does not change if they are crowned or have already changed alignments.

Elf madman sword is also wrathful.

Armor revisions
-Add Protection from Shape changers, deflection, and grappling upgrades.
--Deflection adds spe to AC again (rin protection)
--Grappling replaces the unarmed attack with a grapple (as grappler's grasp)
--Prot from shape changers gives the extrinsic
--Kicking+Jumping == knockback like hammerfeet
--Blind res improves AC and DR by 1 point
-Re order flags to ascending order rather than grouping by armor piece.
-Move flight upgrade from boots to armor.
-Bolt improvements
--If zapped while two-weaponing, the gauntlets holy bolts cost 2x energy (20 vs 10) and deal 2x damage.
--Holy and unholy missile phase worn armor.
--1/2 spe (rounded up) is added to the number of dice. This is still less than the typical number of dice from an attack wand.


"Many wormy fingers entity" (Psurlon template)
-May be applied to:
--Dark worms, baby long and purple worms, long and purple worms.
--Giant eels, electrick eels, kraken, centipedes, garter snakes, water moccasins, pit vipers, pythongs, cobras, and daughters of naunet.
--Adult Dragons (Wyrms)
-Generation rules are slightly different for each class.
--Generate based on both insight and madness. Elf madmen are especially targeted, and skip one insight check. The first insight check is also skipped in the future.
--Even pre-placed worms and dragons can recieve the template.
--Pre placed wormy things can recieve the template for Elf madmen.
--Dragons require a second insight check.
--Dragons and worms roll a flat madness check.
--Wormy things roll an quadratic madness check.
--Madness checks are defeated by Clear Thoughts.
-Adds weapon, offhand, and psionic spellcasting power
--Worms get quarterstaffs and robes
-+6 special AC and DR (all slots)
-Flag changes
--Not an animal or mindless
--Hostile, collects some items, turns tratorous, eats whatever.
--Causes san loss and grants insight
--Nasty
--No longer limbless/handless
--Snakeleg body plan
--telepathic and normal vision
--Alien and G.O.O. (part of the "many wormy fingers" entity)
-Favor (50%) the Mind Crush/Crush bolt spell

Mind Crush/Crush bolt spell
-Vs. PC:
--If the PC does not have Fixed Abilities, reduces one mental stat (int, wis, cha) by one point then checks brainlessness
---The highest stat is chosen, with ties going wis>cha>int.
---The PC is therefore unlikely to actually die to brainlessness, but it could happen!
--Inflicts San damage
--Inflicts further damage based on stat chosen (even if not reduced)
---Wis: drains energy
---Cha: increments the babble counter
---Int: damages spell knowledge

Worms don't have eyes (worms don't)

Introduce amulets of wound closure and vs. evil eyes.
-Two traditional amulet uses.
-Useable by monsters

The madman quest spawns cats instead of rats above ground, and worms instead of bats below ground.

Mistweaver Priestess and Deminymph chats

Random mad monsters in madman quest don't spawn with the dreams madness (they die of the dreams and rise as yellow monsters if they have it)

Add witch to the list of surgery monsters

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[84143be6cc...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/84143be6cc91f009a86b87ef18b743e533cd4d80)
#### Monday 2023-04-03 14:41:18 by chris

Elven Madman 1

Their box contains upgradeable (badly burnt) armor and a new holy/unholy oprop weapon.

Upgrading the armor is done via an upgrade kit, using a menu. Can gain a wide variety of useful (and not so useful) properties, though not MR (so still needs cloaks)

Elf Lord Weapon (holy vs unholy vs generic energy uses 3/-3 alignment record breakpoints)
-+1d8 energy
-11 insight: +1d8 energy
-22 insight: blade becomes phasing
-33 insight: +spe energy
-          : dusts gremlins and hunting horrors, stones trolls
-          : may cancel target, insight/333 chance
-56 insight: 2d8+spe bonus damage vs. yellow monsters

Armor:
-Fixed ability
-Fast healing (NOT regen)
-Reflection
-Sick res
-Half HP damage
-Half Spell damage (NOT MR)
-Displacement
-Invisibility
Gauntlets:
-Swimming (via ww boots)
-Gauntlets of Power
-Gauntlets of Dexterity
-Increase damage
-Holy bolt projecter ('z'ap the gauntlets while worn, 1d8 energy per wand power level
Boots
-Flying
-Jumping
-Speed
-Teleport
-Kicking
Helm (covers mouth)
-Magic breathing
-Life-sensing (from wand of draining)
-See invisible (useful for spotting from >3 range)
-Telepathy
-Blind resistance/visor (from crystal helm, 100% mind flayer block as well)
-Increase accuracy
-Teleport controll

# Conflicts:
#	include/obj.h
#	src/artifact.c
#	src/attrib.c
#	src/muse.c

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[b8fc476a6c...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/b8fc476a6ce066a0cfd21f88c9641ee70c9e1338)
#### Monday 2023-04-03 14:41:18 by chris

Elf Madman lategame pt 1

Rings of wishes no longer vanish when used up.

Star Emperor's Ring
-Ring of wishes with two wishes remaining
-Adds up to 3 DR to head slot (1 per 10 levels, round down).
-Adds up to 3 passive star blade attacks (1 per 10 levels, round down).
-Converts unarmed attack to star blade attack (4d8).
-Zap to shoot ray of silver stars (requires 15 energy)
-The Stranger spawns with this in his inventory for elves

Lategame monsters
-The Suzerain
--Spawns in a random location on the level when the Puppet Emperor/Empress is killed for good (so only appears on Astral)
--Both the Stranger and the Suzerain spawn with amulets of wound closing engraved with yellow signs and magic resistant self-cursing cloaks
--Casts an arrow rain spell that shoots flaying weapons (in addition to other spells).
-Flaxen Starshadow
--Included in minion list and spawned on Earth and Astral
-Flaxen Star Phantom
--Included in minion list and spawned on Earth and Astral
-Puppet Emperor Xeleth/Empress Xedalli
--Spawns when entering the plane of earth (instead of the wizard)
--Spawns with fully upgraded but bykhee-infested and self-cursing imperial armor.
--Can't be permanently killed until the PC reaches Astral
---(will die permanently when first killed on Astral)
---When killed, lifesaves and is put on the migrating monsters list
---Follows from level to level, and may spawn in when on the migrating monsters list after having been killed.
-Star elf
--Spawns with non-upgradeable imperial armor with some basic upgrades.

Oprops
-Auto-cursing
--Becomes cursed when equiped.
-Byakhee-infested
--Bites and stings wearer, unless they are yellow-faction

Support is also added for temporarily byakhee-infested armor, but no effect currently causes this.

Submats for stone (currently marble only)

Noupgrade flag for imp elf armor.

---
## [NixOS/nixpkgs](https://github.com/NixOS/nixpkgs)@[7553d0fe29...](https://github.com/NixOS/nixpkgs/commit/7553d0fe29801938bcb280bb324b579ef9016aea)
#### Monday 2023-04-03 15:19:06 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- Faster stdenv rebuilds: the third compilation of gcc
  (i.e. stageCompare) is no longer a `drvInput` of the final stdenv.
  This allows Nix to build stageCompare in parallel with the rest of
  nixpkgs instead of in series.
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more Frankenstein compiler: the final gcc and the libraries it
  links against (mpfr, mpc, isl, glibc) are all built by the same
  compiler (xgcc) instead of a mixture of the bootstrapFiles'
  compiler and xgcc.
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- Many other small `stdenv` hacks eliminated
- `gcc` and `clang` share the same codepath for more of `cc-wrapper`.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- This should allow each of the libraries that ship with `gcc`
  (lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`, much like https://github.com/NixOS/nixpkgs/pull/132343

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909
- https://github.com/NixOS/nixpkgs/pull/216136
- https://github.com/NixOS/nixpkgs/pull/216237
- https://github.com/NixOS/nixpkgs/pull/210019
- https://github.com/NixOS/nixpkgs/pull/216232
- https://github.com/NixOS/nixpkgs/pull/216016
- https://github.com/NixOS/nixpkgs/pull/217977
- https://github.com/NixOS/nixpkgs/pull/217995

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [ricgav/ProgettoEsame](https://github.com/ricgav/ProgettoEsame)@[6e00e2a801...](https://github.com/ricgav/ProgettoEsame/commit/6e00e2a801a0aaad9645ce8a406bab2f57be844f)
#### Monday 2023-04-03 15:19:24 by Riccardo Gavioli

now we create a blob into profile of user but I can't read it for the fucking problem of this stupid and idiot browser

---
## [unlegacy-devices/android_kernel_samsung_universal7580](https://github.com/unlegacy-devices/android_kernel_samsung_universal7580)@[5184370888...](https://github.com/unlegacy-devices/android_kernel_samsung_universal7580/commit/5184370888a41ea93f51703e7332862db841a7fc)
#### Monday 2023-04-03 15:39:54 by Daniel Borkmann

net: sctp: fix ipv6 ipsec encryption bug in sctp_v6_xmit

[ Upstream commit 95ee62083cb6453e056562d91f597552021e6ae7 ]

Alan Chester reported an issue with IPv6 on SCTP that IPsec traffic is not
being encrypted, whereas on IPv4 it is. Setting up an AH + ESP transport
does not seem to have the desired effect:

SCTP + IPv4:

  22:14:20.809645 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto AH (51), length 116)
    192.168.0.2 > 192.168.0.5: AH(spi=0x00000042,sumlen=16,seq=0x1): ESP(spi=0x00000044,seq=0x1), length 72
  22:14:20.813270 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto AH (51), length 340)
    192.168.0.5 > 192.168.0.2: AH(spi=0x00000043,sumlen=16,seq=0x1):

SCTP + IPv6:

  22:31:19.215029 IP6 (class 0x02, hlim 64, next-header SCTP (132) payload length: 364)
    fe80::222:15ff:fe87:7fc.3333 > fe80::92e6:baff:fe0d:5a54.36767: sctp
    1) [INIT ACK] [init tag: 747759530] [rwnd: 62464] [OS: 10] [MIS: 10]

Moreover, Alan says:

  This problem was seen with both Racoon and Racoon2. Other people have seen
  this with OpenSwan. When IPsec is configured to encrypt all upper layer
  protocols the SCTP connection does not initialize. After using Wireshark to
  follow packets, this is because the SCTP packet leaves Box A unencrypted and
  Box B believes all upper layer protocols are to be encrypted so it drops
  this packet, causing the SCTP connection to fail to initialize. When IPsec
  is configured to encrypt just SCTP, the SCTP packets are observed unencrypted.

In fact, using `socat sctp6-listen:3333 -` on one end and transferring "plaintext"
string on the other end, results in cleartext on the wire where SCTP eventually
does not report any errors, thus in the latter case that Alan reports, the
non-paranoid user might think he's communicating over an encrypted transport on
SCTP although he's not (tcpdump ... -X):

  ...
  0x0030: 5d70 8e1a 0003 001a 177d eb6c 0000 0000  ]p.......}.l....
  0x0040: 0000 0000 706c 6169 6e74 6578 740a 0000  ....plaintext...

Only in /proc/net/xfrm_stat we can see XfrmInTmplMismatch increasing on the
receiver side. Initial follow-up analysis from Alan's bug report was done by
Alexey Dobriyan. Also thanks to Vlad Yasevich for feedback on this.

SCTP has its own implementation of sctp_v6_xmit() not calling inet6_csk_xmit().
This has the implication that it probably never really got updated along with
changes in inet6_csk_xmit() and therefore does not seem to invoke xfrm handlers.

SCTP's IPv4 xmit however, properly calls ip_queue_xmit() to do the work. Since
a call to inet6_csk_xmit() would solve this problem, but result in unecessary
route lookups, let us just use the cached flowi6 instead that we got through
sctp_v6_get_dst(). Since all SCTP packets are being sent through sctp_packet_transmit(),
we do the route lookup / flow caching in sctp_transport_route(), hold it in
tp->dst and skb_dst_set() right after that. If we would alter fl6->daddr in
sctp_v6_xmit() to np->opt->srcrt, we possibly could run into the same effect
of not having xfrm layer pick it up, hence, use fl6_update_dst() in sctp_v6_get_dst()
instead to get the correct source routed dst entry, which we assign to the skb.

Also source address routing example from 625034113 ("sctp: fix sctp to work with
ipv6 source address routing") still works with this patch! Nevertheless, in RFC5095
it is actually 'recommended' to not use that anyway due to traffic amplification [1].
So it seems we're not supposed to do that anyway in sctp_v6_xmit(). Moreover, if
we overwrite the flow destination here, the lower IPv6 layer will be unable to
put the correct destination address into IP header, as routing header is added in
ipv6_push_nfrag_opts() but then probably with wrong final destination. Things aside,
result of this patch is that we do not have any XfrmInTmplMismatch increase plus on
the wire with this patch it now looks like:

SCTP + IPv6:

  08:17:47.074080 IP6 2620:52:0:102f:7a2b:cbff:fe27:1b0a > 2620:52:0:102f:213:72ff:fe32:7eba:
    AH(spi=0x00005fb4,seq=0x1): ESP(spi=0x00005fb5,seq=0x1), length 72
  08:17:47.074264 IP6 2620:52:0:102f:213:72ff:fe32:7eba > 2620:52:0:102f:7a2b:cbff:fe27:1b0a:
    AH(spi=0x00003d54,seq=0x1): ESP(spi=0x00003d55,seq=0x1), length 296

This fixes Kernel Bugzilla 24412. This security issue seems to be present since
2.6.18 kernels. Lets just hope some big passive adversary in the wild didn't have
its fun with that. lksctp-tools IPv6 regression test suite passes as well with
this patch.

 [1] http://www.secdev.org/conf/IPv6_RH_security-csw07.pdf

Reported-by: Alan Chester <alan.chester@tekelec.com>
Reported-by: Alexey Dobriyan <adobriyan@gmail.com>
Signed-off-by: Daniel Borkmann <dborkman@redhat.com>
Cc: Steffen Klassert <steffen.klassert@secunet.com>
Cc: Hannes Frederic Sowa <hannes@stressinduktion.org>
Acked-by: Vlad Yasevich <vyasevich@gmail.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [readmeio/metrics-sdks](https://github.com/readmeio/metrics-sdks)@[1ce6c540e7...](https://github.com/readmeio/metrics-sdks/commit/1ce6c540e7ccee34b6b8d2b5c1326a5ff9157cb2)
#### Monday 2023-04-03 16:16:27 by Jon Ursenbach

fix(ruby): support rack@3.0.0 (#653)

* fix(ruby): compatibility issues with rack v3.0.0

* fix: typo

* fix: ruby gemfile issues

* chore(deps): updating all ruby deps to be compatible with rack@3.0

* fix: broken tests

* chore: wip work

* fix: rack 3.0.0 upgrade to do with rack.input not being rewindable

Opted to just use `@request.body.read` instead:
https://www.rubydoc.info/gems/rack/Rack/Request/Helpers#body-instance_method

* fix: remove `HAS_HTTP_QUIRKS` flag from integration tests

OK here's where this PR gets interesting... I spent a bunch of time debugging
the test failures here: https://github.com/readmeio/metrics-sdks/pull/653#pullrequestreview-1309362560

I eventually settled on some code that was working, committed here:
224e2ad54c9bef641db39e650bfdc464a55c929b

But that was causing a bunch of `EOFErrors` from Ruby when sending the
HTTP request out to the metrics server:

```
#<Thread:0x000000010c67e488 /Users/domh/Sites/readmeio/metrics-sdks/packages/ruby/lib/readme/request_queue.rb:30 run> terminated with exception (report_on_exception is true):
/opt/homebrew/lib/ruby/gems/3.1.0/gems/net-protocol-0.1.3/lib/net/protocol.rb:227:in `rbuf_fill': end of file reached (EOFError)
	from /opt/homebrew/lib/ruby/gems/3.1.0/gems/net-protocol-0.1.3/lib/net/protocol.rb:193:in `readuntil'
<long stack trace omitted>
```

It turns out that this wasn't a problem on the Ruby side, but in fact a
problem from the Node.js testing side, because when not in "quirks" mode
our fake metrics server happily accepted requests but just ignored them
and never responded to anything.

https://github.com/readmeio/metrics-sdks/blob/7728160f522847b9a59ce7a565eca35610c6e015/test/integration-metrics.test.js#L88-L113

Some languages are okay with this (node, PHP) and some are not okay with
this (python, and Ruby with rack@3.0.0 evidently).

Since it is kinda janky for us to create an HTTP server and just ignore
everything and not respond with anything, I've opted to make the quirks
behaviour the default with this PR! This seems to work for all languages
I've tested locally but lets see if it passes for all of them on CI 🤞

I also had to add another fix here where the body was being returned empty
to the test because the HTTP request from Ruby wasn't complete yet, so if
we hit this race condition, I've opted to just sleep for 300ms and try again.
Using this property:

https://nodejs.org/docs/latest/api/http.html#messagecomplete

Oh don't you just love HTTP.

* fix: rack body using `Rack::RewindableInput`

Creates a new `Rack::RewindableInput` on initialize, then in the body
method we read it in, then rewind it back and finally return it

---------

Co-authored-by: Dom Harrington <domharrington@users.noreply.github.com>
Co-authored-by: Dom Harrington <domharrington@protonmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d4ab94d214...](https://github.com/mrakgr/The-Spiral-Language/commit/d4ab94d2140beb841176bbfa83bfc9a409b65740)
#### Monday 2023-04-03 16:49:55 by Marko Grdinić

"9:10am. I got up 15m ago and have been lounging. Let me chill for a while and then I'll get started.

9:30am. Let's get started. I've wasted enough time in the morning. I didn't get any mail, so let me check the F# thread.

https://www.reddit.com/r/fsharp/comments/129oih7/what_azure_related_technologies_should_i_cover_in/

I didn't get any tech recs in particular.

9:35am. Let me continue watching the tutorial by Theo. Then I'll start things off by checking out the specific techs he is using. For all I know, Vercel and PlanetScale might have Azure versions.

https://youtu.be/YkOSUVzOAA4?t=1868

Wait, what the hell?

@tailwind?

How do these @queries work? I wouldn't have thought something like this was possible in regular CSS.

https://youtu.be/YkOSUVzOAA4?t=1892

He says these colors are incredible.

https://youtu.be/YkOSUVzOAA4?t=1989

What are this kind of classnNmes? md:?

I'll have to check this out later.

https://youtu.be/YkOSUVzOAA4?t=2040
> We'll get an error there because we have tailwing linting

That is a thing?

https://youtu.be/YkOSUVzOAA4?t=2117

Given how much editor assistance React code is getting here, I might be doing myself a disservice by writing my UI code in F#. But I'll roll with it.

9:50am. https://youtu.be/YkOSUVzOAA4?t=2273

Now he is doing regular, fairly vanilla programming.

https://youtu.be/YkOSUVzOAA4?t=2466

The way he is doing styling is interesting. Instead of doing it all from scratch for every class, he os composing it succinctly.

https://youtu.be/YkOSUVzOAA4?t=2633

You can autocomplete the arguments like that?

https://trpc.io/

I'll have to check out this.

https://youtu.be/YkOSUVzOAA4?t=2767

Import type is a thing?

https://youtu.be/YkOSUVzOAA4?t=2972

It is generating types? Interesting.

10:15am. https://youtu.be/YkOSUVzOAA4?t=3412

What is going on here? Is he interpolating a string?

https://youtu.be/YkOSUVzOAA4?t=3720

He should have just used the `pre` element instead of span.

https://youtu.be/YkOSUVzOAA4?t=3732
> Day.js

https://youtu.be/YkOSUVzOAA4?t=3859

Here he is recommending nextjs image.

10:35am. You know, I wonder if I could authoenticate the users for my own site using Patreon?

Imagine if an author has patreon subscribers, it would be cool if he could use that to enable subscriber only areas on his own site.

But if I knew how to take payment, why would I need Patreon?

10:45am. https://youtu.be/YkOSUVzOAA4?t=4468

Ok, so far this is super light. He is just putting in the components and styling them.

The first 30m where he is picking these technologies is complicated, and I'll have to investigate the libraries, but this is easy.

Given my low level of HTML and CSS knowledge this is informative, but I wouldn't break a sweat over this.

I'll watch this all the way to the end and then try to replicate it.

Since by now I've broken the ice with regard to webdev, this will be a good opportunity to get familiar with new tech?

10:55am. https://youtu.be/YkOSUVzOAA4?t=4909

What is going on here?

I need to backtrack a bit. I am not following what is going on here exactly.

https://youtu.be/YkOSUVzOAA4?t=4820

I am confused. This this file get auto generated? At which point?

https://youtu.be/YkOSUVzOAA4?t=4901
> Since Clerk is using JWTs

I keep hearing about those JWTs, and I do not know what they are.

Ideas are coming into my head. Now that I am seeing what exactly he is doing with the Twitter clone, I see that it is nothing really special. It is no different that a regular CRUD application. In that case, why don't I do something that would be useful for my own platform.

In fact, why make a distinction between story posts and forums?

https://youtu.be/YkOSUVzOAA4?t=4914

Figuring out authentication fully is going to be my major task for the foreseaable future.

11:10am. Let me get on with it, I've started dreaming about my own project.

https://youtu.be/YkOSUVzOAA4?t=5057

I am a bit confused as to what exactly he is doing here. Is he stripping the context of everything else, but the session?

https://youtu.be/YkOSUVzOAA4?t=5168

What are these public and private procedures?

11:30am. Had to take a short break. Let me resume.

https://youtu.be/YkOSUVzOAA4?t=5250

So this is some kind of validator?

https://youtu.be/YkOSUVzOAA4?t=5487

IF it wasn't for authentication and databases, this wouldn't be that far from a TODO app.

11:45am. https://boards.4channel.org/a/thread/250847310/female-fighting-manga
> A new Female Underground Fighting Manga Series by the creators behind "How Heavy Are the Dumbbells You Lift?" Sandrovich Yabako & Maam will start on Manga One App on May 1, 2023.
> Hagurechads get in here

I'll leave this for later, let me get back to the video. For some reason I started lurking HN.

https://youtu.be/YkOSUVzOAA4?t=5914

Here he will be talking about rate limiting.

> Upstash

Another tech he is talking about.

https://youtu.be/YkOSUVzOAA4?t=6271
> React Hot Toast

12:15pm. Let me take a break here. I've started browsing inane /g/ threads anyway.

12:25pm. I have to admit, I thought this would be something awesome, but 1:55h in, and he what he has done is only a step above the SAFE Stack TODO app.

My expectations going into this were too high, but at the same time, after some research, I should be able to do stuff like this in my sleep.

It got 100k views, just for this? I can do this much and more.

1:20pm. https://mangadex.org/chapter/4e3acebf-dc3a-458e-b138-beb008ced43c/19

Let me catch up with this and then I'll do the chores.

After I am done with Theo's tutorial, I'll check out the .NET beginner ones.

2:05pm. Done with chores.

Let me resume the tutorial. I am not into it at all, but there is only an hour left so I'll get through it. I want to see it through and then I'll watch the .NET channel tutorials that I linked a while ago.

https://youtu.be/YkOSUVzOAA4?t=6941
> The reason we use a link component is to prevent a full browser refresh.

Like with Image, I need to keep this in mind. I wonder if this comes native with React.

https://youtu.be/YkOSUVzOAA4?t=7112

Head info in app?

Ok, that is something new.

https://youtu.be/YkOSUVzOAA4?t=7132

I had no idea you could have nested heads.

So it was worth keeping up with the tutorial. I was wondering whether I should just skip it, but it is fine.

https://youtu.be/YkOSUVzOAA4?t=7350

I am really not paying attention to this right now. Instead I seem to be thinking aobut my own project.

That is not good. I'll give the tutorial another 5-10m and then I'll speed it up.

https://youtu.be/YkOSUVzOAA4?t=7487

Here he is shilling tRPC, but since I have Fable Remoting and Elmish Bridge I won't be needing it.

https://youtu.be/YkOSUVzOAA4?t=7788

He is using Redis and is not doing some weird things that I do not understand as I am not exactly following along.

https://youtu.be/YkOSUVzOAA4?t=7943

What the hell is going on here, I have no clue. But it doesn't matter for now.

https://youtu.be/YkOSUVzOAA4?t=8155

I don't really like all this Typescript type magic.

https://youtu.be/YkOSUVzOAA4?t=8859

Watching him do this basic layouting for so long is killing me. Forget this shit, let me put it on 2x. There is only 30m left anyway.

https://youtu.be/YkOSUVzOAA4?t=9515

Here he is signing in.

http://richg42.blogspot.com/2023/04/a-dead-simple-lossless-or-lossy-lz4.html

Focus me, finish the tutorial, stop reading HN articles.

https://youtu.be/YkOSUVzOAA4?t=10030

I do not get it. They are making a big deal about this being cached, but why not have the client take care of the views to begin with. What is the big deal?

https://youtu.be/YkOSUVzOAA4?t=10055

This guy really needs to get RX audio and run his stuff through the declicker.

https://youtu.be/YkOSUVzOAA4?t=10077

Github CI is programmable?

https://youtu.be/YkOSUVzOAA4?t=10120

Ok, this part is worth watching. Here he is talking about Github CI.

https://youtu.be/YkOSUVzOAA4?t=10339

Here he is talking about branch protection so you can't just push straight to main, but instead need to do a pull request.

https://youtu.be/YkOSUVzOAA4?t=10694
> I think that is everything. This took absolutely forever to make.

3:35pm. I thanked Theo and suggested the Izotope Rx to him.

Now let me read that blog post on codecs and then I'll hunt down the .net tutorials.

http://richg42.blogspot.com/2023/04/a-dead-simple-lossless-or-lossy-lz4.html
> I think simple ultra-high speed lossy (or near-lossless) image codecs, built from the new generation of fast LZ codecs, are going to become more relevant in the future.
> Computing bottlenecks change over time. As disk space, disk bandwidth, and internet bandwidth increases, older image codecs that squeeze every last bit out of the resulting file become less valuable for many use cases. Eventually websites or products using noticeably lossy compressed images will be less attractive. The bandwidth savings from overly lossy image codecs will become meaningless, and the CPU/user time and battery or grid energy spent on complex decompression steps will be wasted.
> Eventually, much simpler codecs with lower (weaker) compression ratios that introduce less distortion, but have blazingly fast decompression rates are going to become more common. This core concept motivates this work.

It was a short article.

3:45pm. https://www.youtube.com/playlist?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN
Let's Learn .NET

This is the playlist that caught my interest.

https://youtu.be/JwKkff93rCA?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN
Let's Learn .NET - Modernization

A lot of these videos are large. I am really interested in auth, but I'll start with the first video on the list just to see what they say. I'll give this a try for 10-15m, and then go into what I really want.

https://youtu.be/JwKkff93rCA?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=858

I suppose it is worth just looking at the slides for this.

4pm. https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN
Let's Learn .NET: Auth and Identity

Let me watch this. This is something that is really important to me. The end of Theo's vid did introduce me to a bit of DevOps.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=379
> Microsoft Identity Platform is pretty platform agnostic. It is a cloud based service...

Oh I thought it was some kind of library. That is cool. I am going to get all that I can out of this.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=462

Oh there is both a framework and a platform.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=566

I'll definitely get famiar with using 3rd party auth.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=710

I didn't understand the question or the answer here, but nwm. Let me just move on. Is there a different AD from Azure AD?

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=883

I do not understand the questions. By identity do they mean the Identity Framework?

> How to decouple AspNet Core Identity from WebAPI in Clean Architecture? It should be in DataAccess layer not in Presentation - inherited DbContext and userManager used directly in controller.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=925
> Would you recommend Microsoft Identity framework for small/medium production web sites?

This is an interesting question.

He'd recommend it, but he says it is hypocritical because as a dev he prefers using 3rd party instead. I'll be using 3rd party myself.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=1092

I'll be looking into this learn module.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=1234

Ok, this last one is not something I've ever heard about.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=1333

What is this .devcontainer thing? This is my first time encountering this.

4:50pm. Let me take a short break.

4:55pm. https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=1689

Let me resume. I am going to watch this today, so I can move to actually programming something tomorrow.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=1868

Oh, it has connections.

https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=2138
> One question you might be thinking of right now is, ok, why are we doing this all in Visual Studio Code and with the .NET SDK and not Visual Studio?

It turns out the big VS can't do dev containers.

https://youtu.be/6QnTNKOJk5A
Don't Use Websockets (Until You Try This…)

Let me pause so I can watch this. I've been thinking about this issue.

https://youtu.be/6QnTNKOJk5A?t=171

They are using Reddis for storing user sessions.

https://youtu.be/6QnTNKOJk5A?t=220

This is a good video. I never heard about SSE before today.

https://youtu.be/6QnTNKOJk5A?t=297

I really wonder if I could implement this using Fable Remoting using something like an AsyncEnumerable.

https://youtu.be/6QnTNKOJk5A?t=376

He isn't really going into the performance aspects of the different solutions.

https://youtu.be/6QnTNKOJk5A?t=388
> It is just that there are certain technical challenges that you run into as you scale horizontally.

https://youtu.be/6QnTNKOJk5A?t=397
> You might need to tweak your load balancer to use sticky sessions or you might need add some single data store like Redis to persist your sessions.

This confuses me a lot. I thought that using WS might be good because it would persist the session automatically rather than having to authenticate on every request.

The comments on this video are interesting.

> I have to point out the elephant in the room: the Phoenix framework. Since it (well, the language and runtime) is based on the actor model, it's fantastic at scaling horizontally, and the statefuless of WebSockets (which it uses extensively) make some things a lot easier; not to mention more efficient, because you don't need to send/receive a whole HTTP request, only the relevant data.

I keep hearing about Phoenix.

I think I'll push forward in the WS direction.

> How does having long-running singular http request event responses not also take up space per session server side just like websockets? Is just easier since you dont have to actively manage them nor have 'sticky sessions' in a scaled out scenario?

Check out this question.

https://youtu.be/xtCddOjITvo
Why WebSockets Are NOT Scalable | WebSockets Explained

Here is a different video.

Let me watch it.

Oh, he is going to explain how WS could be scalable. I do not really understand why they wouldn't be.

https://youtu.be/xtCddOjITvo?t=158

Some guys like these really have a gift for explaining.

https://youtu.be/xtCddOjITvo?t=398

Hmmm, I see. You can't upscale and downscale on demand.

Yeah, I didn't think about that. One server might end up with a lot of connections it cannot service.

https://youtu.be/xtCddOjITvo?t=444
> How do you make a websocket connection scalable?
> Well you don't.

https://youtu.be/xtCddOjITvo?t=551

I understand. So it is possible after all, but not directly. Rather you'd have a WS server call the serverless functions.

That would put the pressure off the WS server. You could do anything like that.

But I understnad now. WS are not really the solution to maintaining sessions by themselves.

I wonder, is Redis just used to maintain the model state and the auth for a particular user, which the serveless funcs do all the work? That would be a really scalable architecture.

6:10pm. Done with lunch.

///

A couple of years ago, I built a node.js-based microservice that receives websocket connections from the front-end. And I successfully made it scale-able.
Simply you put several dockerized instances behind a load balancer. You don't have to have sticky connections. If a client drops its connection, then it can connect to a random instance of the service. You design your application to tolerate the loss of Websocket connection without losing data. And the backend instances can share real-time data between them through MQTT server which can be scaled horizontally too.
I think this video rushes to the conclusion, but my experience proves the opposite. This was hosted on AWS using Fargate. The connections were ok to be dropped to scale-down or even to update the containers.

///

I did some thinking and the problem isn't so much WS connections, but idle ones. And yeah, I'll try avoid using them, but I'll check out Phoenix to see if it has some magic.

6:15pm. Let me watch more of the Auth video. I've gotten distracted with this, but this knowledge will influence how I architect my systems in the future.

6:20pm. https://youtu.be/SFLG-gStXC0?list=PLdo4fOcmZ0oVGRpRwbMhUA0KAvMA2mLyN&t=2393

Hrmmm, no I can't do it anymore. I think I watched 4h of video in total today and more which is good enough. I hate just watching these long videos.

I'll deal with the rest tomorrow and then pick up the Vite template and show how to add authentication to it.

That websocket video...

https://youtu.be/xtCddOjITvo
Why WebSockets Are NOT Scalable | WebSockets Explained

Let me link it again. This video was a real win. It actually increased my understanding of Websockets significantly. Ultimately, I don't really think it would be a problem even if I go the WS route. I can have a server call serveless functions. This would attain huge vertical scaling benefits. Maybe there are even specialized things for that. I have a lot of options.

I don't know how much a 1 vCPU server with 1gb of memory could hold, but 100k-1m concurrent connections does seem feasible. It depends on the size of the model for each user. Without any model, who knows maybe it could go up to tens of millions.

And there are servers out there with 100s of CPUs and Tbs of memory.

6:35pm. Nevermind this for now.

Auth is such an important thing. If I have the choice I should go serverless, it would be less hassle that having to manage WS either way. But in that case, I really will have to look into Redis and caching.

But this just ties into how to keep user state and auth.

I think after I get through this hurdle I'll go from 2/5 to 3/5 in webdev.

This isn't a poor rate of improvement, in fact it is slower than it should be due to me making videos. But doing new things is the spice of life.

6:40pm. Let me just check out what the equivalent of the AWS API gateway on Azure is.

https://learn.microsoft.com/en-us/azure/architecture/microservices/design/gateway
https://aws.amazon.com/api-gateway/

///

WEBSOCKET APIs
Build real-time two-way communication applications, such as chat apps and streaming dashboards, with WebSocket APIs. API Gateway maintains a persistent connection to handle message transfer between your backend service and your clients.

///

I see. I'll have to talk about this in the video.

///

1 million API calls received free

per month for 12 months with the AWS Free Tier

///

It is a pity, but my free tier on AWS will run out before I've even had a chance to use it.

But it costs like 1$ per 100m requests so it is not a big deal. Let's not worry about this."

---
## [rohit5681/kratin-assignment](https://github.com/rohit5681/kratin-assignment)@[bc496ba9c0...](https://github.com/rohit5681/kratin-assignment/commit/bc496ba9c09cfefb3e95a151caa593daad1a51e0)
#### Monday 2023-04-03 17:03:51 by rohit5681

Add files via upload

Tips to live a healthier and better life :
1. Get involved
Physical activity strengthens the immune system. The more you move, the better your body can fight inflammation and infections. Low-impact exercises are also beneficial. Consider cycling, walking, swimming, or low-impact aerobics. Engage in moderate-intensity exercise for 20 to 30 minutes per day, if possible, to reach the recommended total of 150 minutes per week. Strengthen your muscles by lifting weights or practising yoga. Change up your workout routine to see what works best for you.
2. Use supplements as needed.
Some supplements can help maintain a healthy immune system. Always consult your doctor before taking a supplement, especially if you are taking a prescription medication. Calcium, vitamin D, vitamin B6, and vitamin B12 are some supplements they may recommend. To strengthen your immune system, take supplements or multivitamins as directed.
3. Maintain a healthy diet
Diets high in fruits, vegetables, and lean meats also strengthen your immune system and protect you from disease-causing viruses and bacteria. Antioxidants can be found in fruits and vegetables. Antioxidants shield your cells from damage and keep your body running smoothly.Limit your intake of sugary and fatty foods, which can cause inflammation in the body and weaken your immune system. Limit your alcohol consumption as well. Inquire with your doctor about the safe amount of alcohol to consume per day or week.
4. Frequent hand washing
Another great way to stay healthy all year is to wash your hands on a regular basis. Viruses can survive for up to 24 hours on surfaces. If you touch a virus-infected surface, contaminate your hands, and then touch your face, you could become ill. Wash your hands frequently and for at least 20 seconds with warm soapy water. Hands should not be used to touch your nose, face, or mouth. When you are unable to wash your hands, you can protect yourself by using antibacterial hand sanitizer. Also, disinfect surfaces in your home and workplace on a regular basis.
5. Learn how to deal with stress.
Chronic stress causes your body to produce more cortisol, the stress hormone. Too much cortisol can disrupt your body's functions, including your immune system.
Reduce stress by increasing physical activity, getting enough sleep, setting reasonable goals for yourself, and exploring relaxing, enjoyable activities.
6. Get plenty of sleep.
Sleep not only reduces stress, but it also allows your body to repair itself. As a result, getting enough sleep can result in a stronger immune system, making it easier for your body to fight viruses. Sleep is also important as you age because it helps with memory and concentration. Aim for a minimum of seven and a half to nine hours of sleep per night. If you are having difficulty sleeping, consult your doctor to determine the underlying cause. Insomnia can be caused by inactivity during the day as well as consuming too much caffeine. It could also be a symptom of a medical condition such as sleep apnea or restless leg syndrome.
7. Take infection-prevention measures.
Another way to stay healthy all year is to get annual vaccinations. Consult your doctor about getting a high-dose or adjuvant flu vaccine if you are 65 or older.
In the United States, flu season lasts from October to May. The vaccine takes about two weeks to become effective, and when the vaccine strains match the circulating strains, it reduces the risk of the flu by 40 to 60 percent.
Because the flu virus changes every year, you should get the vaccine every year. Speak with your doctor about getting pneumococcal vaccines to protect against pneumonia and meningitis.
8. Arrange for annual physicals
A yearly checkup can also help you stay healthy. If you have any concerns about your health, always consult your doctor. Diabetes and high blood pressure are two examples of conditions that can go undetected. Your doctor will be able to diagnose any problems that arise as a result of regular physical examinations. Getting treatment as soon as possible may help you avoid long-term complications. Also, if you have any cold or flu symptoms, see your doctor as soon as possible. In adults over the age of 65, the flu virus can cause complications. With age, the immune system weakens, making it more difficult to combat the virus. If you see a doctor within the first 48 hours of experiencing flu symptoms, they may be able to prescribe an antiviral to reduce the severity and duration of your symptoms.
9. Avoid contact with sick people.
Another way to protect yourself all year is to avoid being in close proximity to sick people. It's much easier said than done. However, if your area is experiencing a flu outbreak, limit your contact with people who aren't feeling well and avoid crowded places until conditions improve. If you must go out, wear a face mask to protect yourself. Wear a face mask and gloves when caring for someone who has the flu, and wash your hands frequently.

---
## [lime360/website](https://github.com/lime360/website)@[5341566da2...](https://github.com/lime360/website/commit/5341566da27d898737727f4ac99eda06cc509a4f)
#### Monday 2023-04-03 18:34:57 by Kiril Misnikov

read this

fucking idiot

I'M GONNA BREAK MY *keyboard smashing noises* KEY-BOA-RD!

DO YOU WANT THE FUCKING KEYBOARD?

*throws the keyboard*

HOLY SHIT!

(dave and bambi reference)

---
## [cgeoga/Vecchia.jl](https://github.com/cgeoga/Vecchia.jl)@[55a7b475b1...](https://github.com/cgeoga/Vecchia.jl/commit/55a7b475b1dc0c6b31c8a51f8bdc632c311c2ae0)
#### Monday 2023-04-03 18:56:39 by Chris Geoga

Fix up the RChol nll versions. I've deleted all the methods, because I
think that code was ugly and not useful. But now the nll with the RChol
object is blazing fast and parallelizes super well because I squeezed
out all the alloations. The real use-case for the RChol object, in my
opinion, is for when you want to evaluate the nll with the same
parameters more than once. So this re-design focuses on that use case
more effectively.

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[27d37cb0f4...](https://github.com/francinum/Therac-Gameserver/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Monday 2023-04-03 19:02:23 by Gallyus

Alternate Version Tests (#281)

* AltVer Checks
I think?
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* 1603 target

* support script

* HOLY SHIT CAN I READ

* e

* HOLY FUCK CAN I READ

* Disable shortkill version check

---
## [wbrtm/HeroicGamesLauncher](https://github.com/wbrtm/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/wbrtm/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Monday 2023-04-03 19:16:04 by Mathis Dröge

Improve README and developer experience (#1807)

* Update VSCode configuration

* Lots of README changes

- Update our bages; might've overdone it a little, but they're fun to add :^)
- Add badges for Web Technologies used
- Rewrite & bump up system requirements a bit
- Wrap the Language list, Development in a container, and Screenshots in
  <details>; this makes the page load faster and makes it seem less
  daunting
- Add a Flathub badge to the Flatpak section
- Unify Linux install instructions (as much as possible)
- Remove 3rd-party APT repository
  In my opinion, we have enough distribution formats already, and the
  install instructions are a little dodgy
- Add Beta AUR package to the list
- Clarify Windows install instructions by splitting up WinGet and manual
  install
- Make "Development environment" its own section
- Remove Beta and Alpha notes on Windows and macOS build instructions
- Explain what exactly is happening when you run `yarn dev` and in which
  scenarios you might want to use it
- Move the "Back to top" badge to the actual bottom of the page

* Add a Content Security Policy

This doesn't really do much in our situation:
- Just in case someone ever manages to load a website in Heroic's main
  window, no JS can run inside it
- Gets rid of the warning in the console when testing with `yarn dev`

I've tested the Webviews (unaffected) and links to ProtonDB and such
(also unaffected, not sure why though). Please test if this breaks
anything

---
## [Rewqaf41/ScheduleBot](https://github.com/Rewqaf41/ScheduleBot)@[81bce2551a...](https://github.com/Rewqaf41/ScheduleBot/commit/81bce2551a8da8cf5c3698fccda698c016663b04)
#### Monday 2023-04-03 19:17:36 by Rewqaf

Merge pull request #3 from avran02/main

Fuck yeah  added new fucking line, bitches!

---
## [samkenxstream/SAMkenxcertbot](https://github.com/samkenxstream/SAMkenxcertbot)@[208ef4eb94...](https://github.com/samkenxstream/SAMkenxcertbot/commit/208ef4eb942c7129dd265632de740ed1fab53c98)
#### Monday 2023-04-03 19:38:44 by Brad Warren

remove CERTBOT_NO_PIN (#9634)

Adrien and I added this is in https://github.com/certbot/certbot/pull/6590 in response to https://github.com/certbot/certbot/issues/6582 which I wrote. I now personally think these tests are way more trouble than they're worth.

In almost all cases, the versions pinned in `tools/requirements.txt` are used. The two exceptions to this that come to mind are users using OS packages and pip. In the former, the version of our dependencies is picked by the OS and do not change much on most systems. As for pip, [we only "support it on a best effort basis"](https://eff-certbot.readthedocs.io/en/stable/install.html#alternative-2-pip).

Even for pip users, I'm not convinced this buys us much other than frequent test failures. We have our tests configured to error on all Python warnings and [we regularly update `tools/requirements.txt`](https://github.com/certbot/certbot/commits/master/tools/requirements.txt). Due to that, assuming our dependencies follow normal conventions, we should have a chance to fix things in response to planned API changes long before they make their way to our users. I do not think it is necessary for our tests to break immediately after an API is deprecated.

I think almost all other failures due to these tests are caused by upstream bugs. In my experience, almost all of them will sort themselves out pretty quickly. I think that responding to those that are not or planned API changes we somehow missed can be addressed when `tools/requirements.txt` is updated or when someone opens an issue. I personally don't think blocking releases or causing our nightly tests to fail is at all worth it here. I think removing this frequent cause of test failures makes things just a little bit easier for Certbot devs without costing us much of anything.

---
## [edecosta-mw/git](https://github.com/edecosta-mw/git)@[eaa0fd6584...](https://github.com/edecosta-mw/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Monday 2023-04-03 19:47:00 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Blundir/tgstation](https://github.com/Blundir/tgstation)@[a6f49ed542...](https://github.com/Blundir/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Monday 2023-04-03 19:53:38 by san7890

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
## [SuperSackBoy/sackboymagic](https://github.com/SuperSackBoy/sackboymagic)@[fb5029dcf7...](https://github.com/SuperSackBoy/sackboymagic/commit/fb5029dcf72fd76a6c197796108a7c6bd6e99491)
#### Monday 2023-04-03 21:21:32 by Aaron Kimbel

WOOOO YEAH LETS FUCKING GOOOOOOOOOO (it still sucks but i like it and its cool and fuck you)

---
## [penguinus/EasyAdminBundle](https://github.com/penguinus/EasyAdminBundle)@[919545baeb...](https://github.com/penguinus/EasyAdminBundle/commit/919545baebcf0b7ae1f8a35210afc4bd92769161)
#### Monday 2023-04-03 22:02:52 by Javier Eguiluz

feature #5066 Allow `Translatable` objects in addition to `string` in translated context (Lustmored)

This PR was squashed before being merged into the 4.x branch.

Discussion
----------

Allow `Translatable` objects in addition to `string` in translated context

This PR is pretty massive, yet almost all of it's code changes are just enablers for features that are already in Symfony Forms (5.4+) and Symfony Translation (also 5.4+). It allows passing `Translatable` objects as labels and other parts.

### Background

Currently my main problem with EasyAdmin is translation extraction. I maintain pretty large project where translation extraction is build into workflow very tightly and using manual extraction is unmaintainable. Fortunately most translations in admin context have no parameters, so I can workaround that by doing:
```
yield TextField::new('name', (string) t('Client name'));
```
But that's just a dirty hack and works only when label needs no parameters to translate properly. This is why I would benefit greatly if EasyAdmin would simply allow those objects internally and I think other users would welcome it too :smiley:

I have tested those changes on real life projects and they worked like a charm :smile:

### Complexity (?)

As stated before most of the changes are just enablers. By just changing some signatures and adding very simple logic whenever EasyAdmin translates content I was able to pass `Translatable` objects to templates and Symfony Forms, where they handle it without any additional work.

### Backwards compatibility

Functional backwards compatibility is kept. By that I mean - if project uses strings in those contexts (or leaves them empty for Easy Admin to fill with default values), no incompatibility arises. Setters accept strings as before and getters will return those strings. Also - everything will be translated, as before.

Unfortunately the same cannot be said about class signatures. Summary of signature changes are as follows:

Final classes with signature changes:

- Config\Action (new, setLabel); only docblocks and deprecation logic
- Config\Menu\*MenuItem (constructors)
- Config\MenuItem (linkTo*, section, subMenu)
- Dto\ActionDto (getLabel, setLabel and private field)
- Dto\CrudDto (getEntityLabelInSingular, setEntityLabelInSingular,getEntityLabelInPlural, setEntityLabelInPlural, setCustomPageTitle, getHelpMessage, setHelpMessage)
- Dto\FieldDto (getLabel, setLabel, getHelp, setHelp)
- Dto\FilterDto (getLabel, setLabel); only docblocks
- Dto\MenuItemDto (getLabel, setLabel)
- Field\*Field (new); only docblocks
- Field\FormField (addPanel, addTab)

Non-final classes with signature changes:

- Config\Crud (setHelp)
- Field\FieldTrait (setLabel, setHelp); setLabel only in docblock

I wouldn't consider signature changes in setters in final classes as BI, but getters are - end user code might expect getter to return `?string`, while this PR changes it to `TranslatableInterface|string|null`. Again - in simple use case, where user is not using `Translatable` objects this assumption will still hold. But libraries, bundles and other code does not have such guarantee.

Also one non-final class and commonly used trait have signature changes in parameter types that will raise errors when inherited.

I don't see any way we can achieve the same without breaking BC, therefore I think this change can only target `5.0`. But I'd love to hear from the others :)

### TODO

- [x] get feedback
- [x] write tests for functional changes (probably just translating part, there is no point in testing getters and setters IMO)
- [x] Add UPGRADE/CHANGELOG entry documenting changes

Commits
-------

7596f24f Allow `Translatable` objects in addition to `string` in translated context

---
## [nmfightmaster/CIM](https://github.com/nmfightmaster/CIM)@[f0326936a7...](https://github.com/nmfightmaster/CIM/commit/f0326936a720e36cce542ed36e1cec54ea0beac3)
#### Monday 2023-04-03 23:07:04 by Nathan Fightmaster

realizing im an idiot and scaffolding was the better route than creating it myself, but also glad i now have the experience and understanding of what is scaffolded--i replaced my versions with scaffolded versions to reduce headache

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[a4c8057a28...](https://github.com/swarm-game/swarm/commit/a4c8057a28e043caed531e7d035efc2a41dc30a1)
#### Monday 2023-04-03 23:08:46 by Brent Yorgey

Records (#1148)

Add record types to the language: record values are written like `[x = 3, y = "hi"]` and have types like `[x : int, y : text]`.  Empty and singleton records are allowed.  You can project a field out of a record using standard dot notation, like `r.x`.  If things named e.g. `x` and `y` are in scope, you can also write e.g. `[x, y]` as a shorthand for `[x=x, y=y]`.

Closes #1093 .

#153 would make this even nicer to use.

One reason this is significant is that record projection is our first language construct whose type cannot be inferred, because if we see something like `r.x` all we know about the type of `r` is that it is a record type with at least one field `x`, but we don't know how many other fields it might have.  Without some complex stuff like row polymorphism we can't deal with that, so we just punt and throw an error saying that we can't infer the type of a projection.  To make this usable we have to do a better job checking types, a la #99 . For example `def f : [x:int] -> int = \r. r.x end` would not have type checked before, since when checking the lambda we immediately switched into inference mode, and then encountered the record projection and threw up our hands.  Now we work harder to push the given function type down into the lambda so that we are still in checking mode when we get to `r.x` which makes it work.  But it is probably easy to write examples of other things where this doesn't work.  Eventually we will want to fully implement #99 ; in the meantime one can always add a type annotation (#1164) on the record to get around this problem.

Note, I was planning to add a `open e1 in e2` syntax, which would take a record expression `e1` and "open" it locally in `e2`, so all the fields would be in scope within `e2`.  For example, if we had  `r = [x = 3, y = 7]` then instead of writing `r.x + r.y` you could write `open r in x + y`.  This would be especially useful for imports, as in `open import foo.sw in ...`.  However, it turns out to be problematic: the only way to figure out the free variables in `open e1 in e2` is if you know the *type* of `e1`, so you know which names it binds in `e2`.  (In all other cases, bound names can be determined statically from the *syntax*.)  However, in our current codebase there is one place where we get the free variables of an untyped term: we decide at parse time whether definitions are recursive (and fill in a boolean to that effect) by checking whether the name of the thing being defined occurs free in its body.  One idea might be to either fill in this boolean later, after typechecking, or simply compute it on the fly when it is needed; currently this is slightly problematic because we need the info about whether a definition is recursive when doing capability checking, which is currently independent of typechecking.

I was also planning to add `export` keyword which creates a record with all names currently in scope --- this could be useful for creating modules.  However, I realized that very often you don't really want *all* in-scope names, so it's not that useful to have `export`.  Instead I added record punning so if you have several variables `x`, `y`, `z` in scope that you want to package into a record, you can just write `[x, y, z]` instead of `[x=x, y=y, z=z]`.  Though it could still be rather annoying if you wanted to make a module with tons of useful functions and had to list them all in a record at the end...

Originally I started adding records because I thought it would be a helpful way to organize modules and imports.  However, that would require having records that contain fields with polymorphic types.  I am not yet sure how that would play out.  It would essentially allow encoding arbitrary higher-rank types, so it sounds kind of scary.  In any case, I'm still glad I implemented records and I learned a lot, even if they can't be used for my original motivation.

I can't think of a way to make a scenario that requires the use of records.  Eventually once we have proper #94 we could make a scenario where you have to communicate with another robot and send it a value of some required type.  That would be a cool way to test the use of other language features like lambdas, too.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[c3b78761d2...](https://github.com/lessthnthree/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Monday 2023-04-03 23:12:25 by tralezab

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
## [headassbtw/headassbtw](https://github.com/headassbtw/headassbtw)@[840b86c0b7...](https://github.com/headassbtw/headassbtw/commit/840b86c0b70185816b2c585afbca6dd65b9715e9)
#### Monday 2023-04-03 23:27:01 by headassbtw

god i'm fucking stupid but this is still a horrible way to do it

---

