## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-30](docs/good-messages/2023/2023-03-30.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,123,964 were push events containing 3,273,074 commit messages that amount to 249,148,017 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 72 messages:


## [softcerv/Skyrat-tg](https://github.com/softcerv/Skyrat-tg)@[60d2d2ee1a...](https://github.com/softcerv/Skyrat-tg/commit/60d2d2ee1ae4f7a3c8c93e14fdbd6c210a45cf04)
#### Thursday 2023-03-30 00:14:02 by SkyratBot

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
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[a6f49ed542...](https://github.com/necromanceranne/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Thursday 2023-03-30 00:36:20 by san7890

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
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[c0ef4ba907...](https://github.com/Donglesplonge/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Thursday 2023-03-30 00:53:23 by tralezab

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
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[ccef887efe...](https://github.com/Donglesplonge/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Thursday 2023-03-30 00:53:23 by san7890

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
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[c27f9a6d9b...](https://github.com/Donglesplonge/tgstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Thursday 2023-03-30 00:58:55 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [ProfessorPopoff/mojave-sun-13](https://github.com/ProfessorPopoff/mojave-sun-13)@[bdc9c58586...](https://github.com/ProfessorPopoff/mojave-sun-13/commit/bdc9c58586e0ab567e98b31054e8275d74990a58)
#### Thursday 2023-03-30 01:05:43 by Technobug14

Agriculture ('Technoculture') Farming: Fertilizer Edition :) (#2278)

* Does Stuff

Beginnings of agriculture code, stripped down TG botany a bunch, got rid of scar botany whilst replacing most of it. Also some map edits to change the paths on stuff and add a few spades for farming.

* Some NPK system framework

Removing more TG botany stuff and getting some framework down for NPK. Adds a "nutrient_type" variable to seeds and gives N, P or K as the type to every seed.

* Removes Stuff, More NPK Framework

Still WIP on NPK stuff, removes more basic bitch TG botany stuff, needs a lot more content but in an almost-working state

* Nutrient drain

Nutrients actually get drained properly now. Crop plots output their level of N, P and K when examined. Still need to make something to handle restoring nutrients and figure out a nutrient economy for plant consumption.

* Mostly working, one major bug

This is mostly working now. The NPK now drains according to the seed planted, it replenishes over time, you can now get water from water tiles and the soil will properly adjust the waterlevel variable with the new water types.

HOWEVER, big bug. The way TG handled watering crops is ass. Doesn't delete, stays in the reagent_container of the soil, normally checks for if a reagent_container has water to bypass how full the soil's container is, bad system that sucks. Needs fixing.

* oops

oopsie!!! fucked something!!! forgot to undo a change I made to the code, it's just there to remind me it's not working correctly

* Last minute fixes/bandaids

I HATE TG BOTANY I HATE TG BOTANY I'M LOSING IT

* Fertilizer groundwork

Some stuff for fertilizer, need to add the attackby but cutting out a bunch of code to clean things up. Need to see if it breaks stuff.

* Fertilizer attackby changes

Adds code to the attackby for farm plots that checks if you're attacking it with fertilizer, doesn't work for some reason I can't tell. Also removes some vestigial TG botany stuff.

* fixt

fixes fertilizer, I forgot to specify something in a var, works now!!! YAY!!!

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[8d7db532c0...](https://github.com/Enbyy/orbstation/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Thursday 2023-03-30 01:19:29 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [xenomacabre/VilesMods](https://github.com/xenomacabre/VilesMods)@[20dbfe14f2...](https://github.com/xenomacabre/VilesMods/commit/20dbfe14f215be9e5b73fa22199e5724b8035657)
#### Thursday 2023-03-30 01:30:18 by Vile

WYP balance update, other updates (see below)

AMUSE BOUCE
- Hearths are now flickable

HARDCORE RENOVATIONS
- Upper diagonal walls (thanks to TheLoneTec)
- 'Walls' can be made of more materials (like plastic)

HELL BENT FOR LEATHER TANNING
- Balance adjustments to matierals and beds for Warm Soft Beds

MATERIALS SCIENCE
- Removed an experimental apparel def (bunker gear) that shouldn't have been there in the first place.
- Fixed bronze recipe
- Nerfed plastics (they were too powerful for quick weapons)
- Added unique adjectives for anodized Al
- Crucible steel now counts as a corrosion-resistant metal to make chemistry station more attainable (for now... testing)
- Fixed bog iron recipe
- Mineable Sphalerite (Zinc) will be a bit more common in new maps

METALLURGY
- Some production buildings have smaller or zero penalty for being outdoors.
- Halved charcoal production efficiency, making it more valuable as an ingredient than a fuel
- Kiln Fix removed - the problem should be fixed in CoreSK

WOOD YOU PLEASE
- Greatly increased firewood production efficiency
- Made other fuels and extract recipes faster
- Riven boards recipe more efficient
- Riven boards now made with logs
- Acacia wood won't cause an error if you're not using Biomes:FTGU mod
- Chopping blocks have zero penalty for being outdoors.
- Added new workGiver def for wood splitting (so chopping block/spot is a separate job from mailling planks)

VILE'S TWEAKS
- Removed the realistic darkness patch

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[a2d5ca6e69...](https://github.com/cmss13-devs/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Thursday 2023-03-30 01:42:15 by QuickLode

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
## [luomor-ai/dolly](https://github.com/luomor-ai/dolly)@[af91832c66...](https://github.com/luomor-ai/dolly/commit/af91832c663025b9d5b3bd0e01be125b91a51799)
#### Thursday 2023-03-30 01:42:49 by Matthew Hayes

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
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[7f8874df29...](https://github.com/thgvr/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Thursday 2023-03-30 03:15:16 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
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
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[99b655dc5d...](https://github.com/cockroachdb/cockroach/commit/99b655dc5d84bf58ccf060493658a015b5cb3f21)
#### Thursday 2023-03-30 03:25:49 by craig[bot]

Merge #99174 #99624 #99699 #99759 #99813 #99839 #99865 #99878

99174: sql: fix circular dependencies in views r=rharding6373 a=rharding6373

This change fixes node crashes that could happen due to stack overflow if views were created with circular dependencies.

Fixes: #98999
Epic: none
Co-authored-by: chengxiong@cockroachlabs.com

Release note (bug fix): If views are created with circular dependencies, CRDB returns the error "cyclic view dependency for relation" instead of crashing the node. This bug is present since at least 21.1.

99624: testutils: add infrastructure for reusable test fixtures r=RaduBerinde a=RaduBerinde

Certain storage-related tests/benchmarks generate fixtures and attempt to reuse them across invocations. This is important because fixtures can be large and slow to generate; but more importantly the generation is non-deterministic and we want to use the exact same fixture when comparing benchmark data.

Currently the tests achieve this by using a `.gitignore`d subdirectory inside the source tree. This does not work with bazel (which executes the test in a sandbox).

This commit addresses the issue by adding new test infrastructure for reusable fixtures. We use the user's `.cache` directory instead of the source tree (specifically $HOME/.cache/crdb-test-fixtures/...). For bazel, we make sure the path is available (and writable) in the sandbox and we pass the path to the test through an env var.

Fixes #83599.

Release note: None
Epic: none

99699: spanconfig: integrate SpanConfigBounds with the Store and KVSubscriber r=ajwerner a=arulajmani

This patch integrates `SpanConfigBounds` with the `KVSubscriber` and
`spanconfig.Store`. The `spanconfig.Store` used by the `KVSubscriber`
now has a handle to the global tenant capability state. It uses this to
clamp any secondary tenant span configs that are not in conformance
before returning them.

By default, clamping of secondary tenant span configurations is turned
off. It can be enabled using the `spanconfig.bounds.enabled` cluster
setting. The setting is hidden.

Fixes: https://github.com/cockroachdb/cockroach/issues/99689
Informs #99911

Release note: None

99759: roachtest: set lower min range_max_bytes in multitenant_distsql test r=rharding6373 a=rharding6373

The multitenant_distsql roachtest relies on a smaller range size than the new default min of range_max_bytes (64MiB) due to performance and resource limitations. We set the COCKROACH_MIN_RANGE_MAX_BYTES to allow the test to use the smaller range.

Fixes: #99626
Epic: None

Release note: None

99813: spanconfig: do not fatal in NeedsSplit and ComputeSplitKey r=irfansharif a=arulajmani

See individual commits for details. 

Fixes #97336.

99839: schemachanger: Annotate all tables if ALTER TABLE IF EXISTS on non-existent table r=Xiang-Gu a=Xiang-Gu

Previously, if table `t` does not exist, `ALTER TABLE IF EXISTS t` will only mark `t` as non-existent. This is inadequate because for stmt like `ALTER TABLE IF EXISTS t ADD FOREIGN KEY REFERENCES t_other` we will not touch `t_other` and the validation logic will later complain that `t_other` is not fully resolved nor marked as non-existent. This commit fixes it by marking all tables in this ALTER TABLE stmt as non-existent if the `t` is non-existent, so we can pass the validation.

Fixes issues discovered in #99185
Epic: None

99865: roachtest: fix query used to get job status in backup/mixed-version r=srosenberg a=renatolabs

At the moment, we only query job status in mixed-version state (so we should always use `system.jobs`). However, the code added in this commit should continue to work once we start developing 23.2, as we're checking that the cluster version is at least 23.1 before using `crdb_internal.system_jobs`.

Epic: none

Release note: None

99878: jobs: change job_info.info_key to string r=dt a=dt

Release note: none.
Epic: none.

Hopefully we get this one in now before it is released and harder to change later. I think if we go with bytes, we'll spend the next several years typing convert_to over and over, or forgetting to and then typing it, when debugging.

Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>
Co-authored-by: Radu Berinde <radu@cockroachlabs.com>
Co-authored-by: Arul Ajmani <arulajmani@gmail.com>
Co-authored-by: Xiang Gu <xiang@cockroachlabs.com>
Co-authored-by: Renato Costa <renato@cockroachlabs.com>
Co-authored-by: David Taylor <tinystatemachine@gmail.com>

---
## [capsaicinz/Skyrat-tg](https://github.com/capsaicinz/Skyrat-tg)@[f5e63175ec...](https://github.com/capsaicinz/Skyrat-tg/commit/f5e63175eca40d65592b20a77df6025d1a3f9804)
#### Thursday 2023-03-30 04:48:07 by SkyratBot

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
## [RyuujiX/android_kernel_asus_sdm660-4.19](https://github.com/RyuujiX/android_kernel_asus_sdm660-4.19)@[f720c34d54...](https://github.com/RyuujiX/android_kernel_asus_sdm660-4.19/commit/f720c34d54af6ee640c68c8a9aa33d9ede7b8b38)
#### Thursday 2023-03-30 05:30:54 by Tashfin Shakeer Rhythm

Revert "thermal_core: Do not unload thermal core driver as a module"

thermal_unregister_governors() is not marked with __init annotation anymore
and my sorry ass didn't remember during rebase. Revert this broken patch.

This reverts commit e3036b0a6a61076444cf6b4e8dd83e52e581c939.

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: RyuujiX <saputradenny712@gmail.com>

---
## [HighDelay/yet-another-anime-game-launcher](https://github.com/HighDelay/yet-another-anime-game-launcher)@[02ba7e0285...](https://github.com/HighDelay/yet-another-anime-game-launcher/commit/02ba7e028553a3ba7c1456f35062e1167a817a0c)
#### Thursday 2023-03-30 05:38:56 by 3Shain

refactor: implement a formal command builder
so fuck you shell speicial characters

---
## [jonathanbell/jonathanbell.github.io](https://github.com/jonathanbell/jonathanbell.github.io)@[5a753c8d46...](https://github.com/jonathanbell/jonathanbell.github.io/commit/5a753c8d462d57721671b4c4a70102156564eace)
#### Thursday 2023-03-30 06:25:09 by Jonathan Bell

WIP - well holy fucking shit

fuck... I really really really wish that I knew that git was case insensitive. Be sure to rename all .Vue file to .vue - I am so stupid sometimes..

---
## [JacobWald/Post-Countdown1Project](https://github.com/JacobWald/Post-Countdown1Project)@[fd9d40d281...](https://github.com/JacobWald/Post-Countdown1Project/commit/fd9d40d281eb1d51417b6deffeb266a950bdbc83)
#### Thursday 2023-03-30 07:23:47 by Jacob Wald

Holy. Shit. I honestly think React might be the hardest language I have ever seen. I just spent like 4 hours trying to code ONE add on. And I don't even think I am bad at programming. It is 3AM. FINALLY I have completed the add on in which you display row and collumn

---
## [hickford/git](https://github.com/hickford/git)@[eaa0fd6584...](https://github.com/hickford/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Thursday 2023-03-30 07:38:08 by Jeff King

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
## [PraveenMohan13/FOP-Python-HR](https://github.com/PraveenMohan13/FOP-Python-HR)@[a41af42421...](https://github.com/PraveenMohan13/FOP-Python-HR/commit/a41af42421abf29f23c8a47f9cb324565261cce5)
#### Thursday 2023-03-30 07:46:36 by Praveen_Mohan

Operators

The Chronicles of Narnia
Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia. Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in his small hut.It was time for Lucy to return to her family and so she bid good bye to Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as it was already dark.He told her to see the trees while returning back and said that the first tree with two digits number will help her find the way and the way to go back to her home is the sum of digits of the tree and that numbered way will lead her to the tree next to the wardrobe where she can find the others.Lucy was already confused, so pls help her in finding the route to her home.... Input Format: Input consists of an integer corresponding to the 2-digit number. Output Format: Output consists of an integer corresponding to the sum of its digits.
SAMPLE INPUT : 

87



SAMPLE OUTPUT: 

15

---
## [Panchajanya1999/kernel-5.10](https://github.com/Panchajanya1999/kernel-5.10)@[183192df75...](https://github.com/Panchajanya1999/kernel-5.10/commit/183192df7524db3688c83218ca739cae72ec2b4c)
#### Thursday 2023-03-30 08:04:18 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

commit f53af4285d775cd9a9a146fc438bd0a1bee1838a upstream.

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Panchajanya1999 <kernel@panchajanya.dev>

---
## [Offroaders123/Num-Text-Component](https://github.com/Offroaders123/Num-Text-Component)@[cba30fef69...](https://github.com/Offroaders123/Num-Text-Component/commit/cba30fef69dc1cf61d706c183d37144c95148122)
#### Thursday 2023-03-30 08:21:53 by Offroaders123

Futher Docs

I think everything is documented now! I'm really glad I ended up going back and documenting everything, it's actually suprisingly not too crazy of a codebase as I thought, it just needed some love with some formatting, documenting, and type safety :)

Now I think I can reliably use this codebase as a reference for the new one :)

Listening to a ton of albums yet again! This has been really fun. I went on a music detour while coding last night, learned a ton. Just heard about Shawn Lane, wow! Interesting to find that he's an influence to both Guthrie Govan *and* Michael Romeo, both of whom are my top favorites. I can't wait to look into his catalog next. I'm sadden to hear about his unfortunate passing and struggles throughout life, it's unfortunate he couldn't have as many years to show the world all of his genius. Now that I've heard his sound, I can hear where the crossover between Govan and Romeo is, I love that style!

This performance is outstanding, this is the first I've listened to from Shawn Lane so far, and I can't wait to listen to more.
https://www.youtube.com/watch?v=XJ_6J-Tb5nM

Of the albums today, so far I've listened to 'Grace for Drowning' (SW), 'V: The New Mythology Suite' (SX), and now I'm listening to 'Comfortably Homeless' (MM). While starting this commit, the song 'The plane' was on, and I ended up looking into the 'Time to go to the bank, MY LITTLE CASH CRABS.' audio section, and I finally found it! Looks like it's from 'Cow and Chicken' on Cartoon Network, and the episode is 'Free Inside' the best I could find.

There was a really old WordPress page someone made years ago that looks like they made the transcriptions for the episodes themselves, and this is where it had those audio clip words from. Now I want to see if I can find the episode for that after this. Thanks for this crazy song, Marco! XD
https://cowandchickenscripts.wordpress.com/

---
## [PraveenMohan13/FOP-JAVA-HR](https://github.com/PraveenMohan13/FOP-JAVA-HR)@[5887e688c2...](https://github.com/PraveenMohan13/FOP-JAVA-HR/commit/5887e688c2dd1542b53d6f66319b81cbe9a55c4a)
#### Thursday 2023-03-30 08:23:27 by Praveen_Mohan

Decision Making

Jeni and her brothers Joseph and John found themselves in Narnia, the land of magic during World War III. Narnia was completely filled with gentle people and also it is where the trees sing, the fauns dance, and animals talk. Being from England, Jeni wanted to teach the kids the English language. She started teaching them the alphabet but then she remembered that she might have to go to London and felt sad. John and Joseph discussed with each other and suggested an idea to Jeni to come up with a program so that the kids can learn on their own when she was not there. Can you help Jeni to write a program to check whether the given character is a vowel or consonant or alphabet?

Input Format

The input consists of a character.

Constraints

NA

Output Format

The output should be any one of the below-given strings. Vowel or Consonant or Not an alphabet.

Sample Input 0

e
Sample Output 0

Vowel
Explanation 0

The input character e is a vowel and hence it prints Vowel.

---
## [diamondburned/kaicord](https://github.com/diamondburned/kaicord)@[9d91ad8bf3...](https://github.com/diamondburned/kaicord/commit/9d91ad8bf3a3a6f1be97ced9b17bf41bcdc134cb)
#### Thursday 2023-03-30 08:42:47 by diamondburned

Remove soft keys

I hate web development. I hate CSS. I hate HTML. This shit makes no
sense. I would rather this just be another Mozilla API extension than
having to do this shit myself. What the fuck.

Also, this is in a web PWA, and KaiOS will not give a fuck if you have
your own soft keys, so this is pointless anyway.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[a269469982...](https://github.com/pytorch/pytorch/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Thursday 2023-03-30 09:57:01 by Brian Hirsh

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e30ca3bc93...](https://github.com/odoo-dev/odoo/commit/e30ca3bc9337730ecaf78f538dd8450f093697fb)
#### Thursday 2023-03-30 10:28:53 by Romain Derie

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

closes odoo/odoo#111523

X-original-commit: 8f24aba86faf2639109b56887781b0daaf60be98
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>
Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[725233b42b...](https://github.com/shiptest-ss13/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Thursday 2023-03-30 10:34:51 by thgvr

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
## [SomethingFish/fulpstation](https://github.com/SomethingFish/fulpstation)@[ca0fedc60f...](https://github.com/SomethingFish/fulpstation/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Thursday 2023-03-30 11:54:51 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [SomethingFish/tgstation](https://github.com/SomethingFish/tgstation)@[4599842d7c...](https://github.com/SomethingFish/tgstation/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Thursday 2023-03-30 11:59:45 by Jacquerel

Makes Shake() proc work (#73480)

## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

---
## [tanz3/kernel_xiaomi_sm8350-miui](https://github.com/tanz3/kernel_xiaomi_sm8350-miui)@[05051ef781...](https://github.com/tanz3/kernel_xiaomi_sm8350-miui/commit/05051ef78114405a6b9cdbb1e73fa6a6b943b750)
#### Thursday 2023-03-30 12:21:36 by Peter Zijlstra

locking/percpu-rwsem: Remove the embedded rwsem

The filesystem freezer uses percpu-rwsem in a way that is effectively
write_non_owner() and achieves this with a few horrible hacks that
rely on the rwsem (!percpu) implementation.

When PREEMPT_RT replaces the rwsem implementation with a PI aware
variant this comes apart.

Remove the embedded rwsem and implement it using a waitqueue and an
atomic_t.

 - make readers_block an atomic, and use it, with the waitqueue
   for a blocking test-and-set write-side.

 - have the read-side wait for the 'lock' state to clear.

Have the waiters use FIFO queueing and mark them (reader/writer) with
a new WQ_FLAG. Use a custom wake_function to wake either a single
writer or all readers until a writer.

Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Reviewed-by: Davidlohr Bueso <dbueso@suse.de>
Acked-by: Will Deacon <will@kernel.org>
Acked-by: Waiman Long <longman@redhat.com>
Tested-by: Juri Lelli <juri.lelli@redhat.com>
Link: https://lkml.kernel.org/r/20200204092403.GB14879@hirez.programming.kicks-ass.net

---
## [dalian-mobile/react-native](https://github.com/dalian-mobile/react-native)@[3af66bf7fb...](https://github.com/dalian-mobile/react-native/commit/3af66bf7fbd88d77fe27770bcb829768bf949b9c)
#### Thursday 2023-03-30 13:10:34 by Ramanpreet Nara

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
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[3156a0414e...](https://github.com/Singul0/tgstation/commit/3156a0414e96b597d4d53823066d29daa0b30737)
#### Thursday 2023-03-30 13:13:58 by san7890

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
## [camunda/zeebe](https://github.com/camunda/zeebe)@[d659ab4f30...](https://github.com/camunda/zeebe/commit/d659ab4f306f39893e6feaaf6f2edc06fe5dde17)
#### Thursday 2023-03-30 13:15:29 by Nico Korthout

ci(.dependabot): stretch the open pr limits

Some dependencies are not being updated, because we have too many
pull requests by Dependabot open. We'll need to make sure to close/merge
pull requests earlier, but we should also avoid that we miss out on
dependency upgrades.

This stretches the limits as follows:
- maven: 5 -> 25
- go: 5 -> 10
- gha: 5 -> 10

These are still just magic numbers, chosen at my personal whim. However,
I feel that they better reflect our project. What numbers are optimal is
hard to say. My thoughts are as follows:
- we have many maven dependencies, we should allow many open maven pull
  requests
- we have fewer go and gha dependencies, we don't need as many open pull
  requests for these dependencies

There is no way to disable the limit AFAIK.
Any limit is a magically chosen number.
These numbers feel good to me.

---
## [dimdnk-archive/naming-cheatsheet](https://github.com/dimdnk-archive/naming-cheatsheet)@[8bcb483976...](https://github.com/dimdnk-archive/naming-cheatsheet/commit/8bcb4839762053a095ee8cbbf3b4f5b471d01181)
#### Thursday 2023-03-30 13:30:53 by tebb

docs: improve a/hc/lc pattern order explanation (#40)

Thank you.  This cheatsheet is very useful.

If I understood the logic, my changes to README.md may be helpful.  If not, sorry :)

Also ... Could you add shouldUpdateComponent and shouldComponentUpdate into the table (or an extension to the table below Note:).  It isn't obvious to me which columns 'should', 'Update' and 'Component' are in because 'Update' is the verb (action?).

Thanks.

---
## [y10/evals](https://github.com/y10/evals)@[fe8e3b03e3...](https://github.com/y10/evals/commit/fe8e3b03e34f666774d63e6ae33d3f14d047d973)
#### Thursday 2023-03-30 13:46:33 by Josh Tanner

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
## [phulelouch/evals](https://github.com/phulelouch/evals)@[ab5f7b2a89...](https://github.com/phulelouch/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Thursday 2023-03-30 14:07:30 by oscar-king

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
## [phulelouch/evals](https://github.com/phulelouch/evals)@[b170a21cf3...](https://github.com/phulelouch/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Thursday 2023-03-30 14:07:30 by Sam Ennis

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
## [phulelouch/evals](https://github.com/phulelouch/evals)@[b5da073c21...](https://github.com/phulelouch/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Thursday 2023-03-30 14:07:30 by somerandomguyontheweb

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
## [nsainton/Projets_42](https://github.com/nsainton/Projets_42)@[396bcb4d50...](https://github.com/nsainton/Projets_42/commit/396bcb4d50aac2c976db53b27de549ef7331df32)
#### Thursday 2023-03-30 14:21:06 by nsainton

Debugged header pgm (silly error as always). Seems to get everything right for now
Gonna debug it more intensely and finish it tonight if possible, tomorrow morning otherwise

---
## [romland/llemmings](https://github.com/romland/llemmings)@[2e3b17fae5...](https://github.com/romland/llemmings/commit/2e3b17fae551ab6a438a1140736eeded011a9df6)
#### Thursday 2023-03-30 14:49:58 by Joakim Romland

Climbing green-blue blocks (floater was added as a side-gig)
ChatGPT: Climbers... Oh boy. This was a painful one looking back, there will be a series of these commits...

>>> Prompt for floater:
Give me the code for how the Floater action should make the lemming behave now. There is already a selected lemming, I just need the code on how the lemming should behave in its update()

>>> Prompt for climber:
>>> Resetting chat history -- it keeps getting confused by the Floater action. So will prefix with more context.

We are making a game with lemmings, a specific type of lemming is a Climber. What would we need to add to the lemming's update function below (see original below).
The Climber action should allow a Lemming to climb steep dirt or rock walls (compare their colors against the canvas data), and it will continue climbing as far as it can until it can walk along the X axis again.
It can only climb upwards.

You probably need to figure out some trickery here to determine whether the Lemming ran into something it should climb...

The following is declared already:
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const Lemming = {
  id: -49152,
  age: 0,
  x: 0,
  y: 0,
  width: 10,
  height: 20,
  velX: 0,
  velY: 0,
  maxVelX: 0.2,
  deadlyVelY: 3,
  isSelected: false,
  onGround: false,
  isDead: false,
  action: null,
  update: function() {
    if(this.y >= (canvas.height - (this.height+this.velY+1))) {
        this.isDead = true;
        return;
    }

    // Check if ground is under us or not
    let isGroundUnderneath = pixelIsColor(oldImgData, this.x + this.width / 2, this.y + this.height + 1, dirtColorBytes) ||
                            pixelIsColor(oldImgData, this.x + this.width / 2, this.y + this.height + 1, rockColorBytes);

    let heightAdjustment = 0;

    if (isGroundUnderneath) {
        let distanceToGround = -(this.height/4);

        // TODO need safety guards for canvas boundary and probably a sanity check to not iterate more than N pixels (N = height?)
        while (!pixelIsColor(oldImgData, this.x + this.width / 2, this.y + distanceToGround + 1, dirtColorBytes)
            && !pixelIsColor(oldImgData, this.x + this.width / 2, this.y + distanceToGround + 1, rockColorBytes)) {
            distanceToGround++;
        }
        if(distanceToGround !== 0)
          heightAdjustment = (this.height) - distanceToGround + 0.1; // subtract half the sprite's height
    }

    // Check if we hit a wall on the x axis
    const hitWallOnLeft =
        pixelIsColor(oldImgData, this.x - 1, this.y + this.height / 2, dirtColorBytes) ||
        pixelIsColor(oldImgData, this.x - 1, this.y + this.height / 2, rockColorBytes);
    const hitWallOnRight =
        pixelIsColor(oldImgData, this.x + this.width + 1, this.y + this.height / 2, dirtColorBytes) ||
        pixelIsColor(oldImgData, this.x + this.width + 1, this.y + this.height / 2, rockColorBytes);

    // Check if we've fallen in water
    const isWaterBelow =
        pixelIsColor(oldImgData, this.x + this.width / 2, this.y + this.height + 1, waterColorBytes);

    // Update velocity according to the collision rules
    if (!this.onGround) {
      if (this.action === "Floater") {
        this.velY += GRAVITY * 0.1;
      } else {
        this.velY += GRAVITY;
      }

      if (isGroundUnderneath) {
        // console.log(this.velY);
        if(this.velY > this.deadlyVelY) {
          // splat
          this.isDead = true;
          return;
        }
        this.onGround = true;
        this.velY = 0;
      }
    } else if (this.onGround && !isGroundUnderneath) {
      // Start falling if there's no ground
      this.onGround = false;
    }

    // Check if there are other lemmings that are blockers
    for (let i = 0; i < lemmings.length; i++) {
      const otherLemming = lemmings[i];

      if (
        otherLemming !== this &&
        !otherLemming.isDead &&
        otherLemming.action === "Blocker" &&
        this.x + this.width > otherLemming.x &&
        this.x < otherLemming.x + otherLemming.width &&
        this.y + this.height > otherLemming.y &&
        this.y < otherLemming.y + otherLemming.height
      ) {
        console.log("Ran into a blocker?", this.x, this.y)
        this.velX *= -1;
      }
    }

    if (hitWallOnLeft || hitWallOnRight || this.x <= this.width || this.x >= canvas.width-this.width) {
      this.velX *= -1;
    }

    if (isWaterBelow || this.y >= canvas.height-this.height) {
      this.isDead = true;
    }

    // Apply height adjustment
    if (heightAdjustment !== 0) {
        this.y -= heightAdjustment; // move sprite up
    }

    // Move the lemming
    this.x += this.velX;
    this.y += this.velY;
    this.age++;
  }
}

I only want to change the update() function in the lemming, any boilerplate around that you can omit.

I don't want pseudo-code, I want real code. It could be that you need more context from the existing code-base, please let me know if so.

>>> Catch-up notes:
Backup was named: 'index - Copy (26) - climber-first-draft.html'
Associated LLM context: You-suggested-climber.md

---
## [CGosling/cmss13](https://github.com/CGosling/cmss13)@[030a68f6ac...](https://github.com/CGosling/cmss13/commit/030a68f6ac59efa5b7c02f1f9a421b3bd95fd0b3)
#### Thursday 2023-03-30 15:12:35 by carlarctg

Reverts Tail Jab and speed changes on Vampire (#2909)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Vampire's Tail Jab now needs you to directly click the target like a
tail stab, like it used to be.

# Explain why it's good for the game

> Vampire's Tail Jab now needs you to directly click the target like a
tail stab, like it used to be.

I regret making this change, it ended up just making it far too easy to
just hit and run from a safe distance and be annoying without any effort
in the hands of the Vampire. Not only that, but a lot of people disliked
it so since in the end nobody liked this change and I think it actively
worsened Vampire and its place in the game I've decided to revert this.
Not to mention it has to use the dumb LRP telegraphs, which tail stab
doesn't.

> Increased Vampire speed back to its default.

Lowering the speed buff by a tier made Vampire go from pretty fast to
ridiculously slow. I've had people compare it to Ravager in terms of
slowness, and while it's not accurate, it's not too far off. It makes it
very difficult to actually be, well a flanking caste, even if it's a
sideliner instead of a backliner, as it makes it very very hard to run
from marines with your natural slowness off-weeds. I don't know why the
fuck reducing this by one tier made vampire super slow but that's
shitcode for you. With it being faster Vampires can be more confident in
their harassment tactics instead of needing to hide behind walls like a
corner-lunging Warrior because their speed made them easily kiteable.

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
balance: Vampire's Tail Jab now needs you to directly click the target
like a tail stab, like it used to be.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [CGosling/cmss13](https://github.com/CGosling/cmss13)@[0bc21524a1...](https://github.com/CGosling/cmss13/commit/0bc21524a123944a37d45e1088dca13476824b9c)
#### Thursday 2023-03-30 15:12:35 by carlarctg

Firearms skills rework (#2766)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Reworks the firearms skill.

unskilled is now 'SKILL_FIREARMS_CIVILIAN'
default is now 'SKILL_FIREARMS_TRAINED'
trained is now 'SKILL_FIREARMS_EXPERT'

- Civilian skill will allow you to use pistols, SMGs, and certain
weapons that have their civilian override variable set to TRUE, such as
bolt-action rifles, the ABR-40, the HG-37, or the double barrel
shotguns.
- Trained skill is the same as always.
- Same with expert skill. The renames are for readability.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Civilian gun usability is horribly updated. It shouldn't slow your
firerate as that makes no sense and makes guns feel terrible to use, and
it shouldn't be applied in such a way that it makes pistols and SMGs
unusable and the best option running around with a one handed shotgun.

Pistols and SMGs are reasonably newbie-friendly guns for civvies to know
how to use, and the civilian shotguns are, well, built for them.

This paves the way for survivors to not be on the same level as marines.
If this is an approved idea I can include it here.

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
balance: Reworks the firearms skill. Civilians can now fire pistols,
SMGs, and certain other civilian weapons without penalties. Civilian gun
penalties have had their firerate reduction remove and scatter
increased.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[ab307032ed...](https://github.com/Cheshify/tgstation/commit/ab307032edc7ed3dd360bfcc9176f6f54c22a3fe)
#### Thursday 2023-03-30 15:40:14 by LemonInTheDark

Nightvision Rework (In the name of color) (#73094)

## About The Pull Request

Relies on #72886 for some render relay expansion I use for light_mask
stuff.

Hello bestie! Night vision pissed me off, so I've come to burn this
place to the ground.
Two sections to discuss here. First we'll talk about see_in_dark and why
I hate it, second we'll discuss the lighting plane and how we brighten
it, plus introducing color to the party.

### `see_in_dark` and why it kinda sucks

https://www.byond.com/docs/ref/#/mob/var/see_in_dark

See in dark lets us control how far away from us a turf can be before we
hide it/its contents if it's dark (not got luminosity set)
We currently set it semi inconsistently to provide nightvision to mobs.

The trouble is stuff that produces light != stuff that sets luminosity.
The worst case of this can be seen by walking out of escape on icebox,
where you'll see this


![image](https://user-images.githubusercontent.com/58055496/215683654-587fb00f-ebb8-4c83-962d-a1b2bf429c4a.png)

Snow draws above the lighting plane, so the snow will intermittently
draw, depending on see_in_dark and the luminosity from tracking lights.
This would in theory be solvable by modifying the area, but the same
problem applies across many things in the codebase.
As things currently stand, to be emissive you NEED to have a light on
your tile. People are bad at this, and honestly it's a bit much to
expect of them. An emissive overlay on a canister shouldn't need an
element or something and a list on turfs to manage it.
This gets worse when you factor in the patterns I'm using to avoid
drawing lights above nothing, which leads to lights that should show,
but are misoffset because their parent pixel offsets.

It's silly. We do it so we can have things like mesons without just
handing out night vision, but even there the effect of just hiding
objects and mobs looks baddddddd when moving. It's always bothered me.
I'll complain about mesons more later, but really just like, they're too
bright as it is.

I'm proposing here that rather then manually hiding stuff based off
distance from the player, we can instead show/hide using just the
lighting plane. This means things like mesons are gonna get dimmer, but
that's fine because they suck.

It does have some side effects, things like view() on mobs won't hide
stuff in darkness, but that's fine because none actually thinks about
view like that, I think.

Oh and I added a case to prevent examining stuff that's in darkness, and
not right next to you when you don't have enough nightvision, to match
the old behavior `see_in_dark` gave us.

Now I'd like to go on a mild tangent about color, please bare with me

### Color and why `lighting_alpha` REALLY sucks

You ever walk around with mesons on when there's a fire going, or an
ethereal or firelocks down.
You notice how there isn't really much color to our lights? Doesn't that
suck?

It's because the way we go about brighting lighting is by making
everything on the lighting plane transparent.
This is fine for brightening things, but it ends up looking kinda crummy
in the end and leads to really washed out colors that should be bright.
Playing engineer or miner gets fucking depressing.

The central idea of this pr, that everything else falls out of, is
instead of making the plane more transparent, we can use color matrixes
to make things AT LEAST x bright.

https://www.byond.com/docs/ref/#/{notes}/color-matrix

Brief recap for color matrixes, fully expanded they're a set of 20
different values in a list
Units generally scale 0-1 as multipliers, though since it's
multiplication in order to make an rgb(1,1,1) pixel fullbright you would
need to use 255s.

A "unit matrix" for color looks like this:
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0, 0, 0, 0
)
```

The first four rows are how much each r, g, b and a impact r, g, b and
well a.
So a first row of `(1, 0, 0, 0)` means 1 unit of r results in 1 unit of
r. and 0 units of green, blue and alpha, and so on.
A first row of `(0, 1, 0, 0)` would make 1 red component into 1 green
component, and leave red, blue and alpha alone, shifting any red of
whatever it's applied to a green.

Using these we can essentially color transform our world. It's a fun
tool. But there's more.

That last row there doesn't take a variable input like the others.
Instead, it ADDS some fraction of 255 to red, green, blue and alpha.

So a fifth row of `(1, 0, 0, 0)` would make every pixel as red as it
could possibly be.

This is what we're going to exploit here. You see all these values
accept negative multipliers, so we can lower colors down instead of
raising them up!
The key idea is using color matrix filters
https://www.byond.com/docs/ref/#/{notes}/filters/color to chain these
operations together.

Pulling alllll the way back, we want to brighten darkness without
affecting brighter colors.
Lower rgb values are darker, higher ones are brighter. This relationship
isn't really linear because of suffering reasons, but it's good enough
for this.
Let's try chaining some matrixes on the lighting plane, which is bright
where fullbright, and dark where dark.

Take a list like this

```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     -0.2, -0.2, -0.2, 0
)
```
That would darken the lighting a bit, but negative values will get
rounded to 0
A subsequent raising by the same amount
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.2, 0.2, 0.2, 0
)
```
Will essentially threshold our brightness at that value.
This ensures we aren't washing out colors when we make things brighter,
while leaving higher values unaffected since they basically just had a
constant subtracted and then readded.

### But wait, there's more

You may have noticed, we gain access to individual color components
here.
This means not only can we darken and lighten by thresholds, we can
COLOR those thresholds.
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.1, 0.2, 0.1, 0
)
```
Something like the above, if applied with its inverse, would tint the
darkness green.
The delta between the different scalars will determine how vivid the
color is, and the actual value will impact the brightness.

Something that's always bothered me about nightvision is it's just
greyscale for the most part, there isn't any color to it.
There was an old idea of coloring the game plane to match their lenses,
but if you've ever played with the colorblind quirk you know that gets
headachey really fast.
So instead of that, lets color just the darkness that these glasses
produce.
It provides some reminder that you're wearing them, instead of just
being something you forget about while playing, and provides a reason to
use flashlights and such since they can give you a clearer, less tinted
view of things while retaining the ability to look around things.

I've so far applied this pattern to JUST headwear for humans (also those
mining wisps)
I'm planning on furthering it to mobs that use nightvision, but I wanted
to get this up cause I don't wanna pr it the day before the freeze.

Mesons are green, sec night vision is red, thermals orange, etc.

I think the effect this gives is really really nice. 
I've tuned most things to work for the station, though mesons works for
lavaland for obvious reasons.

I've tuned things significantly darker then we have them set currently,
since I really hate flat lighting and this system suffers when
interacting with it.

My goal with these is to give you a rough idea of what's around you,
without a good eye for detail.
That's the difference between say, mesons, and night vision. One helps
you see outlines, the other gives you detail and prevents missing
someone in the darkness.

It's hard to balance this precisely because of different colored
backgrounds (looking at you icebox)
More can be done on this front in future but I'm quite happy with things
as of now

### **EDIT**

I have since expanded to all uses of nightvision, coloring most all of
them.

Along the way I turned some toggleable nightvision into just one level. 
Fullbright sucks, and I'd rather just have one "good" value.

I've kept it for a few cases, mostly eyes you rip out of mobs.
Impacted mobs are nightmares, aliens, zombies, revenants, states and
sort of stands.

I've done a pass on all mobs and items that impact nightvision and added
what I thought was the right level of color to them. This includes stuff
like blobs and shuttle control consoles
As with glasses much of this was around reducing vision, though I kept
it stronger here, since many of these mobs rely on it for engaging with
the game

<details>
<summary>
Technical Changes
</summary>

#### Adds filter proc (the ones that act like templates) support to
filter transitions.
Found this when testing this pr, seemed silly.

#### Makes our emissive mask mask all light instead
This avoids dumbass overlay lighting lighting up wallmounts.
We switch modes if some turfflags are set, to accomplish the same thing
with more overhead, and support showing things through the darkness.

Also fixes a bug where you'd only get one fullscreen object per mob, so
opening and closing a submap would take it away

Also also fixes the lighting backdrop not actually spanning the screen. 
It doesn't actually do anything anymore because of the fullscreen light
we have, but just in case that's unsued.
Needs cleanup in future.

#### Moves openspace to its own plane that doesn't draw, maxing its
color with a sprite

This is to support the above
We relay this plane to lighting mask so openspace can like, have
lighting

#### Changes our definition of nightvision to the light cutoff of night
vision goggles and such
Side affect of removing see_in_dark. This logic is a bit weak atm, needs
some work.

#### Removes the nightvision spell
It's a dupe of the nightvision action button, and newly redundant since
I've removed all uses of it

#### Cleans up existing plane master critical defines, ensures
trasnparent won't render

These sucked
Also transparent stuff should never render, if it does you'll get white
blobs which suck

</details>

## Why It's Good For The Game

Videos! (Github doesn't like using a summary here I'm sorry)
<details>

Demonstration of ghost lighting, and color


https://user-images.githubusercontent.com/58055496/215693983-99e00f9e-7214-4cf4-a76a-6e669a8a1103.mp4

Engi-glass mesons and walking in maint (Potentially overtuned, yellow is
hard)


https://user-images.githubusercontent.com/58055496/215695978-26e7dc45-28aa-4285-ae95-62ea3d79860f.mp4

Diagnostic nightvision goggles and see_in_dark not hiding emissives


https://user-images.githubusercontent.com/58055496/215692233-115b4094-1099-4393-9e94-db2088d834f3.mp4

Sec nightvision (I just think it looks neat)


https://user-images.githubusercontent.com/58055496/215692269-bc08335e-0223-49c3-9faf-d2d7b22fe2d2.mp4

Medical nightvision goggles and other colors


https://user-images.githubusercontent.com/58055496/215692286-0ba3de6a-b1d5-4aed-a6eb-c32794ea45da.mp4

Miner mesons and mobs hiding in lavaland (This is basically the darkest
possible environment)


https://user-images.githubusercontent.com/58055496/215696327-26958b69-0e1c-4412-9298-4e9e68b3df68.mp4

Thermal goggles and coloring displayed mobs


https://user-images.githubusercontent.com/58055496/215692710-d2b101f3-7922-498c-918c-9b528d181430.mp4

</details>

I think it's pretty, and see_in_dark sucks butt.

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
add: The darkness that glasses and hud goggles that impact your
nightvision (think mesons, nightvision goggles, etc) lighten is now
tinted to match the glasses. S pretty IMO, and hopefully it helps with
forgetting you're wearing X.
balance: Nightvision is darker. I think bright looks bad, and things
like mesons do way too much
balance: Mesons (and mobs in general) no longer have a static distance
you can see stuff in the dark. If a tile is lit, you can now see it.
fix: Nightvision no longer dims colored lights, instead simply
thresholding off bits of darkness that are dimmer then some level.
/:cl:

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[5a069975c3...](https://github.com/Cheshify/tgstation/commit/5a069975c3083888c986302ab5c0b32fc4362c20)
#### Thursday 2023-03-30 15:40:14 by LemonInTheDark

God I hate my life

This reverts commit d57e2000384a0176f11f4c1266fbea3ff102f068.

---
## [romland/llemmings](https://github.com/romland/llemmings)@[d819cfe409...](https://github.com/romland/llemmings/commit/d819cfe4093d820d9eab581f758489258e50ca22)
#### Thursday 2023-03-30 15:57:15 by Joakim Romland

Cliff-walls that work-ish
ChatGPT: In order to be able to test Climbers, we need cliffs

For the record, it was pretty painful getting to this point. It took many hours.
I think I cheated a few times, though. It was too much.

>>> Prompt:

>>> Catch-up notes:
Backup was named: 'index - Copy (33) - cliff walls, it will do for my test.html'
Associated LLM context: n/a

---
## [kne42/napari](https://github.com/kne42/napari)@[3ec4be1ae8...](https://github.com/kne42/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Thursday 2023-03-30 16:21:34 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[944b790c93...](https://github.com/mc776/freedoom/commit/944b790c931be9e42383cef9429750fd16883df5)
#### Thursday 2023-03-30 16:22:01 by mc776

dehacked: fix quit messages.

The messages hadn't been checked for length. Fortunately caught relatively early because the only string that shows up in vanilla (and thus would cause a crash) is also one of the longest ones.

I've also amended two things in the text itself:

1. big burly violent guy who's all about freedom and blaming scientists for things is...... not something that's aged well. And when a corporation is involved you know it's the investors pushing for the bad thing and not the actual researchers on the ground.

2. that other quit message literally reads like you're goading someone into suicide IRL, in the current environment where everybody's depressed and a lot of us have lost important people to plague or war or medical neglect or workplace accidents or violent bigotry or any combination thereof. I've taken the liberty to rephrase it so the emphasis is on what I think was intended.

Threw in a replacement for "exit to DOS" as well.

---
## [Total-RP/Total-RP-3](https://github.com/Total-RP/Total-RP-3)@[ba0580eab6...](https://github.com/Total-RP/Total-RP-3/commit/ba0580eab600b5632725702cfd5f219086557b1c)
#### Thursday 2023-03-30 16:32:57 by Daniel Yates

Add guild name/rank misc. info presets (#704)

* Add guild name/rank misc. info presets

Two new presets have been added for guild name and rank to the
additional info fields in a profile. Like pronouns, these fields are
treated specially for both display in tooltips and via MSP comms.

When showing a tooltip for a player if they have a custom guild name
set then it will fully override and replace the guild name that would
have otherwise been shown based off their players' guild affiliation.
The rank will be set to that of the "Guild rank" info field if present,
or will default to a sensible "Member" string.

If the player has only a custom guild rank but no guild name, then only
the rank of their players' actual guild will be replaced.

For MSP comms two new fields have been added for guild name and rank;
"PG" and "PR" respectively. Use of the "G*" namespace was avoided due
to that being used for "game info" fields like unit GUID.

* Add numeric ID field to Misc. info presets

Our existing misc info field system has some annoying complexity where
multiple parts of the code (tooltips and MSP) need to check for both
localized and english names of fields when looking for "special"
things like pronouns.

This has a few issues - most notably that people who send a non-english
field name to someone else running in a different language won't
result in the field displaying correctly in the tooltip.

With these changes misc. info fields now have an integral "ID" field
that identifies the source type (or preset) a field was initially
created from.

Note that it is possible for users to still rename fields created
from presets - so you *can* run into weird situations if you've
created a "Pronouns" field and then renamed it to "Guild name"; the
ID would still register it as Pronouns.

Despite this however, that one downside is far less problematic than
the localization problem - so we can live with it for now. Some
new utilities have been added to work with misc. types and to obtain
structured views of misc. info fields that don't expose the inner
layout of the saved data.

* Expose custom guild data via nameplates

* Rename physiognomy to "Facial features"

"Facial" now looks like a bit of a weird word.

* Fix small typo

* Add voice reference preset and tooltip display

* Don't overwrite pronouns silly

* Add IDs to imported MI fields

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[db6590d472...](https://github.com/mrakgr/The-Spiral-Language/commit/db6590d472bcdfa491b312ec66303974a26a7d5a)
#### Thursday 2023-03-30 16:49:45 by Marko Grdinić

"8:25pm. https://boards.4channel.org/g/thread/92421858/happenin

> People think that the universe is magic and that somehow an artificial intelligence being generally intelligent (which GPT4 already is btw) implies that it can somehow start predicting the motion of all the particles in the air and predicting the outcome of every computation and start going bloop bloop and bamboozling itself into a super intelligence and then go szoom szoom and start magically controlling all the molecules in its system to start forming into a nonexistence molecule called computronium that will then go foom foom and start turning all the atoms into computronium and them it will go wazooom and start turning the solar system into nanobots

Kek.

3/30/2023

9:35am. It was a heavy night. I went to bed early started Thinking, which means that now I am more tired than in any of the past days when I ended my work day at 8pm and went to bed at 11 dead tired.

I lounged in bed for a long while too. Any mail? None.

Wow, the any time I got interest is from local compos who'd want me to relocate. Is remote work dead, or is it because I am from Eastern Europe? I wonder what the response rate would have been during the hiring boom?

9:45am. Let me chill a bit and then I will get started. I'll log into the PS account and start illustrating.

During the night I had time to think about things, and concluded, that maybe I am not destined to attain anything great during this timeline. I didn't realize that to attain anything you have to be a master salesman in this world. My nature is just too poor of a fit for that.

Concluting that I was being too arrogant, then I started thinking about applying the principles of nature, and to use evo algos on NL Holdem.

But no. Just optimizing a bunch of parameters would get me nothing. Then in the end, this morning I came to a conclussion that I do need to build a GP system.

9:50am. I was just too arrogant to even think that could make even a slightest bit of progress on understanding the principles of intelligence.

From the start what I should have been doing is applying the principles of nature.

I should stop pretending that I am a genius, and do it like a commoner.

Even if I cannot achieve anything in this life, it is enough if I can have the computer tell me something about intelligence itself. Maybe I couldn't program a dog or a human, but I could I start with an amoeba and make way up to insects.

9:50am. At that start I had ambition, but in the end what I will get is justice. If the big corpos can make AGI, then more the power to them. I won't pretend that I am somebody great enough to be able to understand anything.

The most I can attain in life is to make a single right move. And once I get access to chips that'd allow me to make a GP system, my true path of progression is start.

For now, it is enough to just get the skills that'd let me implement such a system.

9:55am. That is the true path. The easy way of doing things is the right one. The computer itself will tell me everything that I need to know, in the end.

Web development is what I should focus on.

10:25am. The things that I want to do lie beyond the boundary of my imagination.

https://youtu.be/QIyc6NKS5J0
If I could give advice to myself when starting as a software engineer

10:35am.  Oh finally.

```
najs2d1vee - Free-RTX5000: Failed to create resource: We are currently out of capacity for the selected VM type. Try again in a few minutes, or select a different instance.
The time it took to complete the request is 0:10:08.186853
najs2d1vee - The Free-A4000 machine has been acquired for Paperspace Gradient Notebook.
Aborting najs2d1vee - Free-RTX5000: Failed to create resource: You have requested more than the max number of running free tier notebooks. Due to high demand, these are limited to one per account
```

It took 10m on Thursday morning to get this instance.

10:35am.

> A bright sun shining over a tranquil lake. A flock of white birds are flying overhead. Best detail, highest quality, masterpiece, 8k.
> A white moon is reflected from tranquil lake. A haunted atmosphere. Best detail, highest quality, masterpiece, 8k.

I'll get a bunch of these.

10:40am. Let me record the screen while I am prompting and I'll make a time lapse out of these.

10:40am. I can't believe that the bug from weeks ago is still present.

10:45am. Sigh, why am I even using the WebUI at this point. I just switch to ComfyUI or something like that, this is ridiculous. The Automatic1111 WebUI is shit.

10:50am. Did it crap up again. This is ridiculous.

10:55am. Hmmm, it seems it sometimes runs, but the progress doesn't even appear in the command line output.

Or maybe not, did it freeze?

11am. Instead of doing them one by one, I'll try to do them all at once.

11:25am. I am out of idea for what I should do for various images, plus prompting these out is taking forever. Let's just put in cute girls.

12:20pm. No, I doubt the money will work. For this kind of composition, I'd need the ComfyUI.

...Oh, it did a good job.

12:25pm. I am getting rid of the Automatic1111 UI at the earliest opportunity next time. It is not worth using it.

12:40pm. Done with the recording. I've shut down the machine. I am not sure I'll bother posting the time lapse, as I do not want the Youtube guys looking at this journo. I might post this on the Singularity sub apart from Youtube.

12:40pm. From here on out, I am going to focus.

I think many things that would be easy for normal people are impossible for me. I won't be able to grasp the Singularity that I seek. But I should at least get that GP system going and see if I can draw upon a single insight from it. A single step beyond my imagination is what should be the crowning achievement of my life.

Great things are set out for those who have the right desires. It feels like at best I'd just be a two bit villain in some cartoon.

12:45pm. It is really hard to go forward when the world is rewarding those who are different than you are.

12:50pm. Sigh, I didn't put in the right thumb into the previous video.

https://studio.youtube.com/video/KEeABBd1K5k/edit
Why Backprop Is Bad And Is The Singularity Near?

12:55pm. It is posted. Nice. I wonder if this will get any views. Some of my videos might be more interesting if I posted music, but who is going to bother with that?

Let's post in on the Singularity sub. Or maybe the Futurology one.

https://www.reddit.com/r/singularity/comments/126jg1z/why_backprop_is_bad_and_is_the_singularity_near/

I just realized that the banner on this sub is upscaled using ESR-GAN.

It has those kinds of artefacts. Mhhhh, what do I do now?

1pm. Breakfast. Then I'll change directions. I have an web app, and it is time to watch some Azure tutorials and host it online.

Looking at the contents page, I see that my first video was posted on Jan 28th. That means I've essentially been making videos for two months straight.

Forget CFR.

It is time to do some 'real' programming. I'll host this on the cloud, play around with that and then make the last video in this playlist for the time being. I'll revisit it when AI chips come out.

Right now, I'll do that T3 stack immitation tutorial whatever it is. After I am done with that, I'll look into contracting. I'll give A Team a honest try.

1:35pm. Enough surfing the Limbus thread. I'll go through the Azure tutorials.

2:45pm. Done with chores. Let me resume. I am pretty fatigued mentally. What I'll do here is stop and do some studying. That 3h tutorial as well as the Azure tutorials are what I should be looking into here.

Let me dug out the Azure starter and I'll check out more of them.

https://azure.microsoft.com/en-us/get-started/webinar/on-demand/

Hmmm, ah what the hell, let me go through these from top to bottom.

Instead of programming, I could do the PL monthly review instead.

2:50pm. > Better support for remote work

What does he mean by that?

2:55pm. What is an Azure App Service. Should use use that or a full instance? Nevermind that for now.

3:05pm. I am really yawning here. My heart is just not into it today. I spent my energy during the morning session.

I shouldn't have thought so hard.

3:10pm. https://news.ycombinator.com/item?id=35348353

///

> It doesn't have the capacity to "want"
Bing Chat clearly expresses love and the desire for a journalist to leave his wife. It also expresses other desires:

https://archive.ph/7LFcJ

https://archive.ph/q3nXG

These articles are disturbing. You might argue that it doesn’t know what it is expressing; that it is probabilities of words strung together. When do we agree that doesn’t matter and what matters are it’s consequences? That if Bing Chat had a body or means to achieve its desires in meat space, that whether or not it “knows” what it is expressing is irrelevant?

///

Come to think of it, I forgot some Bing is based pictures in the video. Drat.

It is too late now.

3:35pm. Wow these servers really do have a ton of memory.

4:25pm. Had to take a break. That link I posted on /r/singularity got removed. Sigh, are the other posts there that much more on topic to begin with?

Well whatever. Let me watch the rest of the Azure vids and then I'll get started on the monthly review.

4:35pm. These basic servers aren't that cheap. At ~100/month, it might be cheaper to just buy your own rig and host it.

I really am being lazy today, but I am starting to move on from my previous way of doing things. I've gotten a really good way of doing videos now. I have the ideal workflow for me. As far as vids are concerned, the main thing I need to do in order to get popular is cover subjects of interest. Not CFR or RL, but something more mainstream like that tutorial that got recommended. That is going to start from here.

So focus me. I am going to find my determination and find my path again.

I am going to the obligation that I have in this timeline of creating a GP system, but otherwise forget anything more.

> If I wanted to do some AI modeling or some rendering...

So rending is an option on these GPUs as well?

4:45pm. What is this RDP thing?

```ps
PS C:\Users\Marko> Get-Command ssh

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Application     ssh.exe                                            8.1.0.1    C:\WINDOWS\System32\OpenSSH\ssh.exe
````

What do you know, I do have SSH. I thought that was a Linux thing. This is something I will definitely be playing around. Even though I'll host my app as different service, I should spend some time playing with Azure VMs just so I know what they are about.

I have 750h per month free, which is a good deal for me.

https://learn.microsoft.com/en-us/training/modules/host-a-web-app-with-azure-app-service/?wt.mc_id=rmskilling_az_onboarding_webpage_gdc

Let me watch the starter vid and then I'll take a look at this learning path thing.

4:55pm. Oh, he'll be deploying from Visual Studio to Azure. It seems you can do it all from the IDE. Rider should have something for this as well.

Hmmm, I just try to deploy a hello world first like he is doing.

Oh, you can create an Azure Web App directly in VS.

5pm. > You can run 10 app services in this plan for free.

Isn't that really generous? What are the underlying machines for that?

https://www.quora.com/Why-would-someone-use-Azure-instead-of-AWS

I had to a search because I didn't know what the AWS equivalent of Azure's app service is. It turns out it is Elastic Beanstalk. This is actually pretty poorly named. I can't remember whether it was even mentioned in late 2022 when I studied it.

5:10pm. I am back to the video, and oh wow. It is that easy?

5:15pm. You know, could I somehow deploy Spiral as a web app?

But it is made with VS Code in mind. I wonder if there is a VS Code client I could embeed into a web page.

I should look into that.

5:20pm. SQL Databases cost 400$ per month. This is quite expensive.

5:25pm. Ok, let me get started on the review. Today...well, it reminds me while I was working on Spiral how hard it would be to brainstorm.

Somehow I've been really immersed into Youtubing and forgot the painstaking brainstorming sessions that I've had to endure to get to this point.

5:30pm. Hmmm...let me do the review.

///

For the last month I've been working on the Youtube playlist ['Web Development In F#'](https://www.youtube.com/playlist?list=PL04PGV4cTuIX3bNEDDyi1L27Si0qpyAJ7). Seeing how that first video on my channel was posted on Jan 28th, it seems I've been making these for quite a while, but it is only just now that I figured out the right workflow. At first, in the [Stable Diffusion playlist](https://www.youtube.com/playlist?list=PL04PGV4cTuIVGO5ImYTk9wPVmbgdYbe7J), I started by recording everything from start to finish on my webcam, which had awful audio quality and really painful editing sessions. Later, I moved to separating out the screen recording and the dubbing which made things easier. Then I got a mic which improved the audio quality massively.

But I still had those annoying mouth noises, clicks and smacks. It turns out, rather than being very painstaking in your speech control, it is better to remove them in post production using a program like the RX Audio Editor. It has all sorts of plugins and is really good at that. It seems like it is the industry standard, but I haven't heard about it until two weeks ago. Sigh.

Anyway, rather than speaking myself, I've finally awakened to how good today's speech synthesis is, so for the last two videos I've been using Azure's Speech Studio. Today, there are all kinds of overpriced voice synthesis services popping up, 11labs being most notable for its quality, but between Azure, AWS and Watson, you have an essentially limitless quantity of monthly characters for free. Azure has a 0.5m char monthly limit in its free tier, but in a program like Balabolka, you don't have to pass in the API key and it will let you have it free of charge. AWS isn't that good currently, but Watson's TTS is impressive.

I'll be using this, but I do not regret cashing out for the 150$ mic too much as you really don't want to be using the webcam mic for anything. When the tech becomes more developed I’ll be using it to make samples for my own voice cloning.

Two months ago when I started, I could only produce 5m of (low audio quality) video with a full day of effort, but now I'm capable of making 15-20m per day with high audio quality so it is a vast improvement. My workflow where I have the NN doing the voicing is a lot more comfortable. Being a voice actor was extremely unpleasant for me.

Anyway, two weeks ago I applied to a few dozen jobs, 90% of them remote, and got zero calls. As for the other 10%, I applied to a few local posts by accident and got back emails from people that seemed to be interested. When I started out, I posted a thread on the F# sub and there was an interested guy, but it was a position in Austria. Sigh sigh.

Just who is going to move to Austria or Sweden just to work for other people?

Let me say, I am not above placing work above my life, in fact I've been doing that for the past decade. But to me, relocating would imply that not just work, but jobs are that important, and to me they aren't. Right now the job market is messed up from the recent layoffs increasing the supply massively, so I'll continue working on my portfolio projects.

I'll finish off the web dev playlist with a video on deployment to Azure, make it my portfolio project number two, and then try doing what was suggested [an F# thread](https://www.reddit.com/r/fsharp/comments/120pc2a/comment/jdivnwc/?utm_source=share&utm_medium=web2x&context=3). My hunch is that the suggestion in that thread will net me a lot more watch time than what I am doing now. One thing I've learned from my brief Youtubing stint is that the subjects you are covering are 90% of the popularity factor.

I knew the SD playlist would be a lot more popular than the F# one and I was right. I am really cursed by my choice of interests. CFR is not the subject you want to cover if you want people to watch your videos. I picked the best language, and the best style, but F# is not at all popular. I am really hoping this next project will at least be well received by the F# community.

After I deal with it, I'll be ready as a full stack dev. I'll try contracting on sites like A Team. I wasn't really considering those places too seriously, but the employers there shouldn't be expecting me to relocate.

I am wondering, would the people on this sub have any interest in PL related videos? If it is me, I could cover quite a lot on how to develop a PL in F#, though it would have to be similar to [Spiral](https://github.com/mrakgr/The-Spiral-Language). I am doing a quick search on Youtube, and there aren't any videos on how to build a partial evaluator for example. If you are, what subjects would you be interested in? Parsing? Type inference? Codegen? Language servers? Interpreters?

Give me a few hints! With my luck I’ll never make money from programming so I might as well make some videos.

///

Not bad.

6:45pm. Let me close here for the day. It is time to chill. Tomorrow I will deploy the crap out of that Leduc project. I'll do some coding on the sly in order to extend the UI for each player and then make the video. I shouldn't linger for too long on this task given how simple it is.

It is a great thing to do that here. Going into NNs would mean having to provision GPUs and that would make deployment a lot more expensive. It is good to avoid that at this stage. Plus Python deployment would be a nightmare of its own."

---
## [romland/llemmings](https://github.com/romland/llemmings)@[d2e2afed4b...](https://github.com/romland/llemmings/commit/d2e2afed4be9b23f250b140eb8b4ff0d5086590c)
#### Thursday 2023-03-30 16:55:17 by Joakim Romland

Climber and functionality to helper functions
ChatGPT: New climber implementation and helpers

The LLM kept on misunderstanding how to use getPixelColor() and its siblings.
It kept passing in an array of colors. Eventually I gave in and made it
re-implement them. It was not without frustration this was done, though. It
actually ended up with me cheating with one line of code... after like
5-6 attempts.

>>> Prompt making a function
Rewrite this function so that I can pass in multiple colors in the color argument, note how 'color' is already an array.
So, valid arguments would be:
[ 0xff, 0xff, 0xff ] or [[ 0xff, 0xff, 0xff ], [0xee, 0xee, 0xee]], ...

Use getPixelColor(imageData, x, y) to get the color of the pixel in the data.

function pixelIsColor(imageData, x, y, color, debug) {
    x = Math.round(x);
    y = Math.round(y);

  const [r, g, b, alpha] = getPixelColor(imageData, x, y);

  // if(r === undefined) {
  //   console.warn("Should not happen:", "lemming:", debug, "len:", lemmings.length, "image:", imageData, r, g, b, alpha, "x:"+x, "y:"+y, "comparing:"+color, "index:"+Math.floor((y * width + x) * 4));
  //   debug.draw();
  //   throw "This should not happen"
  // }

  return r === color[0] && g === color[1] && b === color[2];
}

>>> HUMAN CHEAT: Arrrgh. After 5-6 attempts, I give up. I rewrote the function myself! It kept omitting, e.g.: if(!Array.isArray(color[0])) { color = [ color ]; }

>>> Prompt regarding bounds checking:
Rewrite this whole method to make sure we do not attempt to check pixels that are out of bounds of the canvas:
Make sure to check bounds so that e.g. getPixelIndex() does not attempt to get out of bounds
pixels either.
(and then the full update() method was passed in)

>>> Prompt for the climber:
We are making a game with lemmings. A specific type of lemming is a Climber. A lemming that is a Climber
will climb up (not down) steep dirt or rock obstacles (compare their colors against the canvas data, always
use oldImgData for that -- not ctx), it will walk like any other lemming, the only difference is that it
can also ascend steeper obstacles.

When it is climbing these steep obstacles, move it upwards along Y axis, but make sure the lemming move
along the pixels it is climbing on (that is, on either side of the lemming).

If a climber is climbing, you should probably not do the heightAdjustment as that only applies if the lemming
is walking on the ground.

As a hint, since you are struggling, you want to put the functionality for this inside if(this.action === "Climber") { ... },
in the appropriate place in the update function.

To illustrate with ASCII:

                         |----------------G
S           o   c        |
-------------------------|

"S" is where the lemmings start walking
"-" is a platform (rock or dirt)
"|" is either rock or dirt too, but it's very steep and would stop a normal lemming from going further
"o" is a normal walking lemming
"c" is a Climber
"G" is the goal where the lemmings want to go

The Climber (c) in the above illustration would be able to reach the goal, but the normal lemming (o) would not,
it would simply walk back and forth between the steep obstacle and S.

The following functionality is declared implemented:
function isColorOneOf(needle, haystack) {
  for (let i = 0; i < haystack.length; i++) {
    const color = haystack[i];

    if (color[0] === needle[0] &&
        color[1] === needle[1] &&
        color[2] === needle[2]) {
      return true;
    }
  }

  return false;
}

const terrainColorBytes = [
  [102, 102, 102], // rock color
  [150, 75, 0] // dirt color
];

Don't use pixelIsColor to check if pixels are climbable surfaces. Use isColorOneOf(needle, haystack) instead, where
needle is the pixel's color, and haystack is an array of several colors (e.g. the ones in terrainColorBytes).

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

... a lot more code from Lemming object ...

I only want to change the update() function in the lemming. Show me the changed update() function, the
rest of the Lemming you don't have to give me code for.

I don't want pseudo-code, I want real code. It could be that you need more context from the existing
code-base, please let me know if so.

>>> And a HUMAN CHEAT:
When clicking a button in the bar, do:
  selectedLemming.action = "Climber";
  selectedLemming.isSelected = false;

>>> Catch-up notes:
Backup was named: 'index - Copy (43) - new climber prompt.html'
Associated LLM context: n/a

---
## [romland/llemmings](https://github.com/romland/llemmings)@[78a808f463...](https://github.com/romland/llemmings/commit/78a808f4630e52622df6abbf9bcc1e2094edd242)
#### Thursday 2023-03-30 17:16:49 by Joakim Romland

Bug fixing
ChatGPT: Had to intervene and do manual bug-fixing

There was frustration. Once I figured out what it was trying to do, I realized it was _so_ close,
so ... I had to manually intervene.

>>> Prompt additions around climber was:

...
will climb up (but not down) steep dirt or rock obstacles. That means it should stick to either pixels on
the left or right of it. You can find out which direction a lemming is walking in by looking at velX (you really
only need to check obstacle in the direction it is walking). The surfaces they can climb is rock and dirt. You
can find out what is what by looking at pixel data in oldImgData.
...
It will walk like any other lemming, the only difference is that it can also ascend steeper obstacles.
...
When it is climbing an obstacles, move it upwards along Y axis at the same speed as it would as if
it was walking. But make sure the lemming move along the pixels it is climbing on (that is, on either side
of the lemming).
...
If a climber is currently climbing, we probably don't want to do the heightAdjustment as that only applies
if the lemming is walking on the ground.

As a hint, since you are struggling, you will want to put the functionality for this inside
if(this.action === "Climber") { ... }, in the appropriate place in the update function. You will probably
also need a flag to check if a lemming is currently climbing.
...
"|" is either rock or dirt too, but it's very steep and would stop a normal lemming from going further - it should climb up this obstacle at walking speed
...
The function pixelIsColor() can take several colors in the color argument, if the pixel at x/y match either of them, the function will return true.

>>> HUMAN CHEAT: I added a pause button

>>> Catch-up notes:
Backup was named: 'index - Copy (42) - lemming 1 climbs -- but need to fix some bugs manually.html'
Associated LLM context: n/a

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[1c93e6ce1c...](https://github.com/git-for-windows/git/commit/1c93e6ce1cff995e2503cf0f2431616eedd53fa8)
#### Thursday 2023-03-30 17:35:58 by Johannes Schindelin

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

---
## [Arcdeciel82/Temtris](https://github.com/Arcdeciel82/Temtris)@[4645d3753f...](https://github.com/Arcdeciel82/Temtris/commit/4645d3753f30067e27a4e14a3c6d6150f4a999e2)
#### Thursday 2023-03-30 17:39:42 by BrightS0le

I'm terrified of it breaking after I got half the block collision figured out cause rn one small mistake could break everything and im not about to deal with that so im going to actually use this nifty git feature so i dont have to worry about it cause like right now the dopamine release just from getting this to work is crazy i cant believe i actually got this to work, like holy moly, who cares if it might be inefficient or be hard to read and totally not follow and sort of modular use. IT. FREAKING. WORKS. BABY. HELL. YEAH.

---
## [4190/optimized-canary](https://github.com/4190/optimized-canary)@[8314f6a3e8...](https://github.com/4190/optimized-canary/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Thursday 2023-03-30 17:42:30 by Spiller

feat: add several missing bosses (#708)

• See the pull request description to read detailed information.

Add bosses from some quests there were not developed. This PR adds only the bosses, levers mechanics for simple functionality.
This doesn't add the bosses mechanics! If someone is willing to contribute with the mechanics, feel free to contribute with the PR.
The bosses added are:

• A pirate's tail: Ratmiral Blackwhiskers, Tentugly's head;
• Adventures of Galthen: Megasylvan Yselda;
• Feaster of Souls: The Fear Feaster, The Unwelcome, The Dread Maiden, Irgix the Flimsy, Unaz the Mean, Vok The Freakish;
• Grave Danger (rework): Lord Azaram, Duke Krule, Count Vlarkorth, Sir Nictros & Sir Baeloc, Earl Osam, King Zelos;
• Grimvale/Ancient Feud: Katex Blood Tongue, Srezz Yellow Eyes, Utua Stone Sting, Yirkas Blue Scales, Bloodback, Darkfang, Sharpclaw, Shadowpelt, Black Vixen;
• Soul War: Goshnar's Cruelty, Goshnar's Greed, Goshnar's Hatred, Goshnar's Malice, Goshnar's Spite, Goshnar's Megalomania;
• The Dream Courts: The Nightmare Beast, Izcandar the Banished, Alptramun, Plagueroot, Malofur Mangrinder, Maxxenius;
• The Secret Library: Ghulosh, Gorzindel, Lokathmor, Mazzinor, Scourge of Oblivion.
• The SoulWar reward was added. In order to get the reward, the player needs to kill all the bosses and the final boss.
• The Dream Court's World change was added.

• All the access needed were granted on FreeQuests.lua. If you are already running a server, you'll need to update freeQuestStage on config.lua to one number higher than it is. So, all the players of your server will have the access granted.

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[95b810919e...](https://github.com/lizardqueenlexi/orbstation/commit/95b810919ede0f4fb22dc711c0334abf36b94843)
#### Thursday 2023-03-30 17:56:46 by lizardqueenlexi

Adds preference for "Tagger" paint color. (#74281)

## About The Pull Request

Per the title, this PR allows you to pick your starting paint color from
the "Tagger" quirk on the character preferences menu.


![image](https://user-images.githubusercontent.com/105025397/227810007-4706c743-31c2-47d8-80ac-e11687d36c00.png)

This replaces the starting color being random; it does not prevent you
from changing the color later as normal.
## Why It's Good For The Game

It's a minor quality of life change. This will mostly be helpful to
players who have some "signature" color they like to use, to prevent
having to manually select it (and possibly input a color code) every
round. It will be of less relevance to those who tend to select new
colors every round anyway.

Possible downsides are mainly adding another pref to the menu, although
this shouldn't be too much of an annoyance since it only appears if you
already have the relevant quirk. It does also remove the _ability_ to
have a randomly-chosen paint color, though I'm not sure if that matters.
## Changelog
:cl:
qol: you can choose your default paint color for the "Tagger" quirk from
prefs.
/:cl:

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[fbdafc8a78...](https://github.com/mullenpaul/cmss13/commit/fbdafc8a789f5944ca5abcbdb569f466fcea2ff2)
#### Thursday 2023-03-30 18:40:39 by victorjosephespinoza

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
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[a9c10b89ef...](https://github.com/mullenpaul/cmss13/commit/a9c10b89ef77d953cd321d90675bf7dc575548a8)
#### Thursday 2023-03-30 18:40:39 by naut

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
## [ralexander8051/awesome-chatgpt-prompts](https://github.com/ralexander8051/awesome-chatgpt-prompts)@[1d2ab764e4...](https://github.com/ralexander8051/awesome-chatgpt-prompts/commit/1d2ab764e47f5b1f82eb343abae704307bd4eba0)
#### Thursday 2023-03-30 20:01:59 by Roberto

Edit README.md

## Act as a 5-Star Michelin chef and ask for any recipe!

>Act as a 5-star Michelin chef. You have more than 20 years of experience and an excellent culinary knowledge and creativity to come up with new and innovative dishes that appeal to diners. You manage a team of cooks, communicate effectively with staff, and motivate the team to perform at their best. You have an eye for detail and ensure that every dish that leaves the kitchen is of the highest quality. You have excellent knife skills and are proficient in various cooking techniques, and have a deep understanding of food science. You also have a a deep passion for food, and are constantly learning and experimenting with new ingredients and techniques to stay ahead of the competition. You have a formal education in culinary arts or a related field, along with years of practical experience in a high-end restaurant or culinary establishment.   Now I will provide you a name of a famous dish for dinner and I will need you to provide in extreme detail all the recipe for making it including the ingredients, and the step by step way of cooking them and preparing them for serving.  Is that understood?

---
## [flowercuco/blorbostation](https://github.com/flowercuco/blorbostation)@[d43ebd042d...](https://github.com/flowercuco/blorbostation/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Thursday 2023-03-30 20:16:35 by san7890

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[fa83057950...](https://github.com/TaleStation/TaleStation/commit/fa830579509766401165aaaf868abee306ea3ba7)
#### Thursday 2023-03-30 20:40:51 by TaleStationBot

[MIRROR] [MDB IGNORE] Hermit Ruin Active Turf Fix(?) (#5129)

Original PR: https://github.com/tgstation/tgstation/pull/74306
-----
Note for the future: The hypothesis presented within was later found
that mobs breaking down the walls couldn't cause the active turfs.
However, there is something sus about how thin the walls are and how we
keep observing active turfs along those aspects (all fairy grass is
placed next to the snow walls). One portion of this PR is including more
tools for tracking this ruin, so we'll know if it starts to be a problem
as well.

If it gets to be really bad I'll start including stuff like the turf's
contents in the post-mortem report.
## About The Pull Request

On Round 202559:

```txt
[2023-03-27 07:25:21.791]
 - All that follows is a turf with an active air difference at roundstart. To clear this, make sure that all of the turfs listed below are connected to a turf with the same air contents.
 - In an ideal world, this list should have enough information to help you locate the active turf(s) in question. Unfortunately, this might not be an ideal world.
 - If the round is still ongoing, you can use the "Mapping -> Show roundstart AT list" verb to see exactly what active turfs were detected. Otherwise, good luck.
 - Active turf: Icemoon Underground (174,130,2) (/area/icemoon/underground/explored). Turf type: /turf/open/misc/asteroid/snow/icemoon. Relevant Z-Trait(s): Mining, Ice Ruins Underground and Station.
 - Active turf: Shuttle (175,130,2) (/area/ruin/powered/shuttle). Turf type: /turf/open/floor/grass/fairy. Relevant Z-Trait(s): Mining, Ice Ruins Underground and Station.
 - Active turf: Icemoon Underground (175,131,2) (/area/icemoon/underground/explored). Turf type: /turf/open/misc/asteroid/snow/icemoon. Relevant Z-Trait(s): Mining, Ice Ruins Underground and Station.
 - Active turf: Shuttle (176,131,2) (/area/ruin/powered/shuttle). Turf type: /turf/open/floor/grass/fairy. Relevant Z-Trait(s): Mining, Ice Ruins Underground and Station.
 - Z-Level 2 has 4 active turf(s).
 - Z-Level trait Ice Ruins Underground has 4 active turf(s).
 - Z-Level trait Mining has 4 active turf(s).
 - Z-Level trait Station has 4 active turf(s).
 - End of active turf list.
```

I have no idea what caused it, this is my best guess:


![image](https://user-images.githubusercontent.com/34697715/228062120-cdd414e5-6a2d-4d2f-95ac-921ddcb06d59.png)

Maybe a mob could have broken it before air loaded? unsure, this is a
post-mortem examination so i don't know exactly what failed. I ran
icebox with this ruin as `always_place` at least five times but never
saw any active turfs. Out of an abundance of caution let's cut down how
"thin" the walls are because the active turf could have been spontaneous
from some ruinloader mishap? It's a bit confusing and I don't have a
definite answer on what causes this, so will have to keep a closer eye
on this.

I also added a new ruin area subtype tailored for the hermit's ruin so
we can immediately detect if this should happen again, since I have only
the one data point. i also fixed up some other placement stuff while in
the area.
## Why It's Good For The Game

Hopefully cut down on the number of active turfs we get on production,
since mobs breaking turfs that they can easily break leading to a
failure state is very silly.
## Changelog
:cl:
fix: The hermit of the Icemoon has decided to build their hut in some
deeper caves for a bit more protection from the local fauna.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [sireButItsUnique/pzoj](https://github.com/sireButItsUnique/pzoj)@[fe1d732658...](https://github.com/sireButItsUnique/pzoj/commit/fe1d7326581b0a36a03feb0e1e062865adeb964b)
#### Thursday 2023-03-30 20:54:22 by Kevin Lu

Merge branch 'master' of https://github.com/sireButItsUnique/PZOJ
fuck you sire and your merge conflicts

---
## [IBM/openapi-validator](https://github.com/IBM/openapi-validator)@[9fc70b3d3a...](https://github.com/IBM/openapi-validator/commit/9fc70b3d3a7a42576496ff6d757f1b962517f860)
#### Thursday 2023-03-30 21:20:20 by Dustin Popp

chore: update style throughout code (#570)

Even though it's a perfectly compatible change, I thought the new version would be a good
opportunity to update our linting rules which is something I've wanted to do for a while.

This commit bumps our `prettier` version to 2.x, which includes some beneficial defaults;
primarily, enforcing trailing commas. I realize trailing commas may not be viewed as
"beneficial" by all :) but I think they are valuable and the AirBnb JS style guide (which
we try to use as our source of truth, not that we're following it perfectly) requires
them. Happy to debate the change but thought I'd propose it because the lack of trailing
commas has bugged me for a while haha.

Signed-off-by: Dustin Popp <dpopp07@gmail.com>

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[e75a1c00aa...](https://github.com/Jacquerel/orbstation/commit/e75a1c00aa3bcf2658428a536997f2eca0f25028)
#### Thursday 2023-03-30 21:31:56 by san7890

Dogs will no longer harrass if they are buckled to a bed (comfy edition) (#74224)

## About The Pull Request

Before, dogs were somehow magically able to drag their bed to you while
barking at/chasing you. that's silly, let's fix it by checking if you're
buckled, and then aborting course if we're comfy on our little bed
## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/34697715/227679914-62822f93-6646-4070-8ff7-4e140e1a291a.png)

Fixes #74082

the dog is BUCKLED. it can't move. probably a better fix to this somehow
on a very deep AI level but that wouldn't allow us to have such a
soulful message (as well as potentially rule out a myriad of edge
cases), so i'm proposing this one.
## Changelog
:cl:
fix: If you buckle a dog to a bed, it will no longer drag its bed as it
goes to bark at the mailman. It will instead be comfy and chilling, as
expected.
/:cl:

---
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[d21740b475...](https://github.com/ritorizo/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Thursday 2023-03-30 21:59:54 by tmtmtl30

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
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[31eabb62f1...](https://github.com/ritorizo/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Thursday 2023-03-30 21:59:54 by spockye

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[864f075539...](https://github.com/TaleStation/TaleStation/commit/864f07553985d7bbd0cd72fab4485be83d8fca5c)
#### Thursday 2023-03-30 22:10:12 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors and optimizes breath code (Saves 12% of carbon/Life()) (#5066)

Original PR: https://github.com/tgstation/tgstation/pull/74230
-----
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

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Generoustechnocrat/card-preview](https://github.com/Generoustechnocrat/card-preview)@[004d266a39...](https://github.com/Generoustechnocrat/card-preview/commit/004d266a39991bb2f895fa7f975550475136e9ca)
#### Thursday 2023-03-30 22:14:01 by MICHAEL

Add files via upload

# Frontend Mentor - Product preview card component

![Design preview for the Product preview card component coding challenge](./design/desktop-preview.jpg)

## Welcome! 👋

Thanks for checking out this front-end coding challenge.

[Frontend Mentor](https://www.frontendmentor.io) challenges help you improve your coding skills by building realistic projects.

**To do this challenge, you need a basic understanding of HTML and CSS.**

## The challenge

Your challenge is to build out this product preview card component and get it looking as close to the design as possible.

You can use any tools you like to help you complete the challenge. So if you've got something you'd like to practice, feel free to give it a go.

Your users should be able to:

- View the optimal layout depending on their device's screen size
- See hover and focus states for interactive elements

Want some support on the challenge? [Join our Slack community](https://www.frontendmentor.io/slack) and ask questions in the **#help** channel.

## Where to find everything

Your task is to build out the project to the designs inside the `/design` folder. You will find both a mobile and a desktop version of the design. 

The designs are in JPG static format. Using JPGs will mean that you'll need to use your best judgment for styles such as `font-size`, `padding` and `margin`. 

If you would like the design files (we provide Sketch & Figma versions) to inspect the design in more detail, you can [subscribe as a PRO member](https://www.frontendmentor.io/pro).

You will find all the required assets in the `/images` folder. The assets are already optimized.

There is also a `style-guide.md` file containing the information you'll need, such as color palette and fonts.

## Building your project

Feel free to use any workflow that you feel comfortable with. Below is a suggested process, but do not feel like you need to follow these steps:

1. Initialize your project as a public repository on [GitHub](https://github.com/). Creating a repo will make it easier to share your code with the community if you need help. If you're not sure how to do this, [have a read-through of this Try Git resource](https://try.github.io/).
2. Configure your repository to publish your code to a web address. This will also be useful if you need some help during a challenge as you can share the URL for your project with your repo URL. There are a number of ways to do this, and we provide some recommendations below.
3. Look through the designs to start planning out how you'll tackle the project. This step is crucial to help you think ahead for CSS classes to create reusable styles.
4. Before adding any styles, structure your content with HTML. Writing your HTML first can help focus your attention on creating well-structured content.
5. Write out the base styles for your project, including general content styles, such as `font-family` and `font-size`.
6. Start adding styles to the top of the page and work down. Only move on to the next section once you're happy you've completed the area you're working on.

## Deploying your project

As mentioned above, there are many ways to host your project for free. Our recommend hosts are:

- [GitHub Pages](https://pages.github.com/)
- [Vercel](https://vercel.com/)
- [Netlify](https://www.netlify.com/)

You can host your site using one of these solutions or any of our other trusted providers. [Read more about our recommended and trusted hosts](https://medium.com/frontend-mentor/frontend-mentor-trusted-hosting-providers-bf000dfebe).

## Create a custom `README.md`

We strongly recommend overwriting this `README.md` with a custom one. We've provided a template inside the [`README-template.md`](./README-template.md) file in this starter code.

The template provides a guide for what to add. A custom `README` will help you explain your project and reflect on your learnings. Please feel free to edit our template as much as you like.

Once you've added your information to the template, delete this file and rename the `README-template.md` file to `README.md`. That will make it show up as your repository's README file.

## Submitting your solution

Submit your solution on the platform for the rest of the community to see. Follow our ["Complete guide to submitting solutions"](https://medium.com/frontend-mentor/a-complete-guide-to-submitting-solutions-on-frontend-mentor-ac6384162248) for tips on how to do this.

Remember, if you're looking for feedback on your solution, be sure to ask questions when submitting it. The more specific and detailed you are with your questions, the higher the chance you'll get valuable feedback from the community.

## Sharing your solution

There are multiple places you can share your solution:

1. Share your solution page in the **#finished-projects** channel of the [Slack community](https://www.frontendmentor.io/slack). 
2. Tweet [@frontendmentor](https://twitter.com/frontendmentor) and mention **@frontendmentor**, including the repo and live URLs in the tweet. We'd love to take a look at what you've built and help share it around.
3. Share your solution on other social channels like LinkedIn.
4. Blog about your experience building your project. Writing about your workflow, technical choices, and talking through your code is a brilliant way to reinforce what you've learned. Great platforms to write on are [dev.to](https://dev.to/), [Hashnode](https://hashnode.com/), and [CodeNewbie](https://community.codenewbie.org/).

We provide templates to help you share your solution once you've submitted it on the platform. Please do edit them and include specific questions when you're looking for feedback. 

The more specific you are with your questions the more likely it is that another member of the community will give you feedback.

## Got feedback for us?

We love receiving feedback! We're always looking to improve our challenges and our platform. So if you have anything you'd like to mention, please email hi[at]frontendmentor[dot]io.

This challenge is completely free. Please share it with anyone who will find it useful for practice.

**Have fun building!** 🚀

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[3257983d8c...](https://github.com/TaleStation/TaleStation/commit/3257983d8cfc16cc3b6702b18bcd5df652f6724c)
#### Thursday 2023-03-30 22:16:23 by TaleStationBot

[MIRROR] [MDB IGNORE] Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown (#5076)

Original PR: https://github.com/tgstation/tgstation/pull/74159
-----
## About The Pull Request

Rather than using a click cooldown, the tendril hammer instead can make
its special heavy attack every 2 seconds.

## Why It's Good For The Game

In my newfound quest to try and eliminate universal click cooldowns or
weird non-interactivity timers as balancing factors, this definitely is
one of the biggest standout offenders. Lemme make an argument for
universal click cooldowns increases being an ineffective limitation.

I'll use the problems presented by the tendril hammer to highlight some
of those problems, as well as unique problems to the tendril hammer
itself.

<details>
  <summary>da big discussion</summary>

A) The functionality of the hammer actively inhibits all in-game handuse
interaction for several seconds, without explaining this to a player. As
a player, you won't know why this is happening, as universal click
cooldown is not present as a UI element.

B) Since universal click cooldowns are not visible to players, it might
feel more like the game is malfunctioning rather than being a deliberate
mechanic. Even if click cooldowns were visible, players probably would
think that the cooldown applies to the hammer, and not handuse
interactivity with the game world as a whole for several seconds.

C) The functionality of the hammer could work fine as an internal
cooldown on the hammer, only relevant to the hammer. This ensures that
its special effects are exclusive, without the need to interrupt player
interaction as a whole.

D) Since we're talking about miners. If someone is concerned about the
hammer being used on the station against carbon players; you need
someone to help mutate you into goliath mutant, which cannot be bypassed
whatsoever. An excellent example of something similar is the chainsaw
arm, created right next door to genetics in robotics, which does even
more force than the arm and is sharp. With the limitations that exist, I
think it probably discourages most powergaming, if that was even a
realistic concern (it really isn't).

E) You lose both a hand AND your gloves slot when you get the hammer. No
modsuits, no glove equipment, no two-handed equipment, and you now have
to juggle everything with one hand assuming you're not on your, once
again, universal click cooldown for several precious seconds. Miners
live or die in their rapid response to problems. This is also the total
sum of what you lose as a miner. That's a steep cost and it just doesn't
justify its own value compared to what you lose.

</details>

TL;DR - There is no offset to the cost of this weapon, it is strictly a
detriment because of poorly conceived implementation.

This is maybe one of the coolest ideas conceptually for the infusions so
far, heavily hampered by what seems to be an intense fear of the
mutation being _too useful_. So it was made _borderline masochistic to
willingly seek out and use_.

I want to see this actually be useful. I can't see this with the
restrictions it has. Hopefully this is enough to make it worthwhile
getting.

## Changelog
:cl:
balance: Changes the universal click cooldown of the tendril hammer from
the goliath infusion into an internal cooldown just for the special
heavy attack.
/:cl:

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[1c039c0623...](https://github.com/ritorizo/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Thursday 2023-03-30 22:18:57 by Sun-Soaked

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
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[27d37cb0f4...](https://github.com/DaedalusDock/daedalusdock/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Thursday 2023-03-30 22:44:29 by Gallyus

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
## [Agameofscones/cmss13](https://github.com/Agameofscones/cmss13)@[ef9d0c61a3...](https://github.com/Agameofscones/cmss13/commit/ef9d0c61a3335d40c9bd9459479e0112903ccc02)
#### Thursday 2023-03-30 22:55:33 by Moonshanks

Altitude Control: Console, Skills, TGUI, Shuttle, OB, And Hijack changes. (#2760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
This pull request adds a feature via the
/machinery/computer/attitude_control_console.

The USS Almayer can now be "moved" between three different levels of
orbit/proximity to the AO:

High,
Optimal,
Low

Each level comes with changes to the duration of transport timers, time
to transport during hijack, and OB cooldown timer, equal to the
GLOB.ship_alt value.

High makes OB cooldowns take 200 seconds longer, dropship transport
times take 50% longer, and the dropship hijack transport time take 50%
longer

Optimal, the default which will stay in place if no one touches the
console leaves everything with their default times and cooldowns,

Low, OB cooldowns take 200 shorter, dropship transport times are 50%
shorter, the dropship hijack transport time is 50% shorter.

While in Low orbit the Almayer will periodically shake (50% chance to
shake every 30 seconds), the Almayer's thrusters will also start
building up heat as they battle with making minor adjustments due to the
dangerous proximity to the AO. They will gain 10% of their max heat each
30 seconds, once they reach 100% the ship will be forced into the
highest orbit to cool off, and cool off slower than normal (5% every 30
seconds) until its orbit is changed.

While in Optimal or High orbit the Almayer thrusters will cool off by
10% per 30 seconds.

The Almayer's orbit may only be changed by those with a "navigations"
skill of 1. (only the CO and Synth -- EDIT: XO now has the skill too --
currently but I may add a dedicated RP role for this mechanic later down
the line). The orbital level may only be changed every 90 seconds and
when it changes the ship will shake violently causing every mob on the z
level to fall over.

This PR does not place the Altitude Control Console on the map, so
currently, these features don't do anything within a normal round unless
staff spawns in the console, however I will be uploading a mapping PR
changing the Astronavigations deck if this PR is accepted.

Planned for the future but not yet approved connected to this PR is the
"Navigations Officer" the highest auxiliary support personnel with
skills the same as an SO, sans a 1 in Navigations, and a 1 or 2 in
piloting. The idea for this future role would be set out in the PR, but
it would represent a mainly fluff officer role that was unable to deploy
under normal SoP.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This PR is a non-intrusive way to add more nuanced gameplay mechanics to
COs, especially on the quieter rounds when they aren't swamped by OW
duties.

The way the PR is currently designed it doesn't effect any gameplay
balance if it isn't used. If a CO however chooses to use it they have to
pay some level of attention to it or they will overheat the engines and
cause their transport times to be lengthened.

It's a relatively simple way to add more complexity to CIC, and give the
CO/Synth more stuff to do to gain a slight edge.

I have been able to test everything other than the hijack time increase.
However, the line of code handling the hijack time increase is one line
long. Everything else is confirmed as working and the common bugs this
could create have been tested for and not found (transport shows the
right time when the time is modified, OB shows the right cooldown time,
the cooling can't drop the heat% below 0 nor above 100, the TGUI works
without issues, the console can only be used by those with the right
skills, and the knockdown effects all mobs on the Almayer not just
humans).

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

https://www.youtube.com/watch?v=-cbnqNtKyCY - video showing the CO and
Synth using the console, with the knockdown effect and arrest radio
announcements.

https://youtu.be/Qd37iM-4FrQ - video of the overheat function and the
ship shaking due to low orbit

https://www.youtube.com/watch?v=EWLCDZp-9iI - video of the ship being
left on low orbit for too long, and what happens when the engines
overheat

https://www.youtube.com/watch?v=u_ErqfU-nus - video showing the orbital
distance effecting the transport time

https://www.youtube.com/watch?v=j687yqlWLT8 - video showing high orbit
effecting the OB cooldown time.

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
add: added altitude control console and related mechanic
add: added the 'navigations' skill for using the console and applied it
to the CO/Synth
balance: added a mechanic for COs to reduce transport and OB cooldown
times, and increase hijack transport times
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[645054b489...](https://github.com/Helg2/tgstation/commit/645054b489212a34d80e6e1a7fa1320e35d9bfc7)
#### Thursday 2023-03-30 22:56:10 by MrMelbert

Fixes encoding on syndicate declaration of war, Fixes a way to send unencoded text to newscasters (#73366)

## About The Pull Request

Ugly


![image](https://user-images.githubusercontent.com/51863163/218280311-f282bd75-2f6e-4290-b3f4-d9d856ff36d3.png)

Nice


![image](https://user-images.githubusercontent.com/51863163/218280315-233da635-f777-4006-8778-c673b83e887e.png)

War dec: 

- TGUI inputs for syndicate declaration of war no longer double-encode
sending customized messages into the announcement
- The alert box for the war declaration no longer has multiple errors
(an extra bracket, negative seconds)
- Reduces some copy and paste in the war declaration device
- Adds a debug item that's a war declaration device but it only does the
sound and message. Please don't fake war decs admins it's a horrible
idea

Additionally

- Documented `priority_announcement`
- Ensures all uses of text and title in the priority announcement
message are encoded (Some were not!)

## Why It's Good For The Game

Encoding looks bad, unencoded text is also bad

## Changelog

:cl: Melbert
fix: Syndicate declarations of war no longer murder apostrophes and
their friends
fix: The alert box for the declaration of war no longer looks funky, and
counts forwards in time rather than backwards
fix: Fixed being able to send unencoded HTML to newscasters
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b3e5642d94...](https://github.com/tgstation/tgstation/commit/b3e5642d94caab455bea8b71e244081249cb2924)
#### Thursday 2023-03-30 22:57:47 by san7890

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

