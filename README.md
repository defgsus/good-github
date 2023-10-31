## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-10-30](docs/good-messages/2023/2023-10-30.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,448,706 were push events containing 3,730,192 commit messages that amount to 295,296,671 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 70 messages:


## [furrycactus/tgstation](https://github.com/furrycactus/tgstation)@[9cf089361e...](https://github.com/furrycactus/tgstation/commit/9cf089361e8cea86d2415de0535b1a28f517e040)
#### Monday 2023-10-30 00:24:47 by Rhials

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
## [furrycactus/tgstation](https://github.com/furrycactus/tgstation)@[404a7cd290...](https://github.com/furrycactus/tgstation/commit/404a7cd29063f00078f85d8171612085a611b271)
#### Monday 2023-10-30 00:24:47 by san7890

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
## [Nobelium-XVIII/tgstation](https://github.com/Nobelium-XVIII/tgstation)@[ff0aea800b...](https://github.com/Nobelium-XVIII/tgstation/commit/ff0aea800b0ce03346d7a655deadf8b53d7f098d)
#### Monday 2023-10-30 00:24:53 by carlarctg

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
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[8353e9d0f4...](https://github.com/ARF-SS13/coyote-bayou/commit/8353e9d0f49d99bea467d640fa35a3b37cda513b)
#### Monday 2023-10-30 00:37:20 by Tk420634

Decompressing Coy_verbs

Fuck you splurt, I'm coming for you assholes.

---
## [deathrobotpunch/tgstation](https://github.com/deathrobotpunch/tgstation)@[157fafeaa9...](https://github.com/deathrobotpunch/tgstation/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Monday 2023-10-30 00:39:38 by lizardqueenlexi

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
## [deathrobotpunch/tgstation](https://github.com/deathrobotpunch/tgstation)@[f3d81edb00...](https://github.com/deathrobotpunch/tgstation/commit/f3d81edb00b07160bc046ab0d79457e60aefba0e)
#### Monday 2023-10-30 00:39:38 by Paxilmaniac

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
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[66f726dfe3...](https://github.com/DATA-xPUNGED/DataStation/commit/66f726dfe31dae0a14feaed8718c41e40e82af09)
#### Monday 2023-10-30 00:53:42 by SyncIt21

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
## [Nobelium-XVIII/fulpstation](https://github.com/Nobelium-XVIII/fulpstation)@[c797bf79ea...](https://github.com/Nobelium-XVIII/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Monday 2023-10-30 00:55:08 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [Stalkeros2/Skyrat](https://github.com/Stalkeros2/Skyrat)@[5f2df10d44...](https://github.com/Stalkeros2/Skyrat/commit/5f2df10d44d04bfe391a0c064a44a4815f0058d4)
#### Monday 2023-10-30 01:04:59 by SkyratBot

[MIRROR] Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay [MDB IGNORE] (#24628)

* Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay (#79275)

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

* Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay

---------

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [EvanZhouDev/TheDonutProject](https://github.com/EvanZhouDev/TheDonutProject)@[cb324fa132...](https://github.com/EvanZhouDev/TheDonutProject/commit/cb324fa1328ea9bc3e2a9910a44b1e962fbe08ab)
#### Monday 2023-10-30 01:14:12 by IOKG04

It... kinda works now

It still messes up quite a bit of stuff, doesnt fill stuff with spaces to make them a perfect donut, doesnt take a lot of stuff into account and is very poorly optimized, but it kinda works, and with that im happy for the day

Lets hope i remember what i coded tomorrow... (I followed pretty much no common patterns n stuff, so it isnt a guaranty, but if I do there should be a donut.ascii.svg tomorrow :D)

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[c539a469d5...](https://github.com/ReturnToZender/ReturnsBubber/commit/c539a469d59849c15a115b319ec5953904863321)
#### Monday 2023-10-30 01:27:04 by SkyratBot

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9e18c6575a...](https://github.com/tgstation/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Monday 2023-10-30 02:27:48 by lizardqueenlexi

Basic Pirate NPCs (#79284)

## About The Pull Request

Converts hostile pirate NPCs to basic mobs - specifically, a subtype of
trooper. As their behavior is not meaningfully distinct from other
troopers, this conversion mostly just sticks them on the existing AI
behavior while keeping the rest the same.

Pirates do have one new thing going for them, though, to differentiate
them from other troopers. They use the new **plundering attacks**
component, which means that every time they land a melee attack, they
steal money from the bank account of whoever they hit. This requires the
target to be wearing an ID with a linked bank account, so it's not the
hardest thing in the world to hide your money from them - but it's still
something to be wary of! If killed, any mob with this component will
drop everything they've stolen in a convenient holochip.
## Why It's Good For The Game

Takes down 5 more simplemobs, and (I think) converts the last remaining
trooper-type enemy to be a basic trooper. (It's possible there's more
I've forgotten that could use the same AI, though.)

The money-stealing behavior is mostly good because I think it's funny,
but it also makes the pirates something a little distinct from "yet
another mob that runs at you and punches you until you die". They still
do that, but now there's a little twist! This can be placed on other
mobs too, if we want to make any other sorts of thieves or brigands.
## Changelog
:cl:
refactor: Pirate NPCs now use the basic mob framework. They'll be a
little smarter in combat, and if you're wearing your ID they'll siphon
your bank account with every melee attack! Beware! Please report any
bugs.
/:cl:

---
## [hllhnd/bfbfe](https://github.com/hllhnd/bfbfe)@[4b108d3887...](https://github.com/hllhnd/bfbfe/commit/4b108d388779aae1455d97da1c12d8a4f1152af0)
#### Monday 2023-10-30 02:36:13 by Reperak

Disable find_set_to_zero optimization due to miscompilation

In extremely rare cases, the find_set_to_zero optimization can cause a miscompilation, the only known reproducer being Erik Bosman's Mandelbrot set generator, which spams the output with "DADADADADADADADADA" ad infinitum.

It wasn't the instruction reordering. It wasn't the instruction merging. It was the fucking set to zero detection. You know, the incredibly fucking basic optimization that detects code like `[-]`? Yeah, somehow that optimization can be broken. Fantabulous.

When I wrote the optimization passes I did my fucking homework to make sure it wouldn't break shit, but somehow this (rather impressive) regular program brings BFBFE to its knees in a way that every Brainfuck compliance test you can throw at it simply cannot.

I don't know why this breaks. I don't even know *what* this breaks. All I know is that it breaks, and it's bullshit, but at the end of the day I'd rather have larger output than broken output.

If by some chance anyone wants to tackle the challenge of figuring out how the Mandelbrot set breaks BFBFE and writing a fix for it, you'll have earned my utmost respect.

End communication.

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[274c21e88b...](https://github.com/yogstation13/Yogstation/commit/274c21e88bb7d291188caf1a1058b10497cd9295)
#### Monday 2023-10-30 03:49:20 by Molti

[PORT] help, i just wanted to give visuals to being wet, now i've ported an entire fire_stacks refactor (#20735)

* oh god

* Update atoms_movable.dm

* Update atoms_movable.dm

* oh god oh fuck what have i done

* Update life.dm

* Update Hallucination.dm

---
## [AzerothWarsLR/WarcraftLegacies](https://github.com/AzerothWarsLR/WarcraftLegacies)@[9ece9d400f...](https://github.com/AzerothWarsLR/WarcraftLegacies/commit/9ece9d400f11c5f70b9ea0d56a3ac5cf4b497b13)
#### Monday 2023-10-30 04:04:28 by Madsen

Implemented Gilneas mini rework (#2551)

Gilneas:
Protectors 19g -> 16g
Removed Towers from most Creep camps,
Locked Worgen Shamans behind Shrine of the Wolf God Quest
Cyclone cannon now requires T3 (castle)
Removed Caster upgrades on Worgen shaman (buffed Mana, mana regen and attack dice to compensate)
Thunderclap on gilneas and Fel horde elites 65dmg -> 85dmg
Fixed tooltip on Caster building and Clarity on Casters upgrade level
Harvest - Witch Healing wave repalced with Thorn Ward
Harvest Witch Spiritual Guidance 800 -> 600 mana
Darius:
New Quest: "The Rebel" Unlocks Darius Crowley
Darius Crowley now starts lvl 7
Darius Crowley Q Changed to Maiming strike, R changed from Ressurection to Greater Stormbolt
GreyGuard:
Greyguard hp 1050 -> 1250
Greyguard hpregen 1hps -> 1.5hps
Worgen:
Worgen hp 950hp -> 1100hp
Worgen Attack cooldown 2.6 -> 2.0
Worgen can now only regen at night.
Worgen Hp regen 1hps -> 3hps
Worgen limit 8 -> 12
Gilneas Heroes:
Darius Crowley Strength per level 2.7 -> 3
Darius Crowley Hp points maximum (base) 100 -> 200
Tess Greymane Hp points maximum (base) 100 -> 200
Genn Greymane Hp points maximum (base) 100 -> 200
Tess Spell Kit rework

Lordaeron:
Alexandros now got Innate Holy light instead of Divine shield
re aranged creeps in caer darrow to make it easier to creep

Miseclanious:
Rain of Arrows cd on all levels 30s -> 9s

Issues solved:
#2548 #2525 #2524 #2523 #2512 #2401 #2400

---
## [Diegoflores31/cmss13-D](https://github.com/Diegoflores31/cmss13-D)@[3e9d54628d...](https://github.com/Diegoflores31/cmss13-D/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Monday 2023-10-30 05:17:04 by Ben

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
## [Diegoflores31/cmss13-D](https://github.com/Diegoflores31/cmss13-D)@[d26452bb9a...](https://github.com/Diegoflores31/cmss13-D/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Monday 2023-10-30 05:19:32 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [shorthills-ai/langchain](https://github.com/shorthills-ai/langchain)@[dff24285ea...](https://github.com/shorthills-ai/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Monday 2023-10-30 05:23:20 by Nikhil Jha

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
## [aleemon/asx_energy_scrape](https://github.com/aleemon/asx_energy_scrape)@[878fe86b65...](https://github.com/aleemon/asx_energy_scrape/commit/878fe86b6563e2f8661f4bc29dd0e5c9d06f370c)
#### Monday 2023-10-30 06:06:11 by aleemon

Update clean.R

Overwrite perpetual trades files, fix the datatype for date (fuck you Excel)

---
## [Isratosh/tgstation](https://github.com/Isratosh/tgstation)@[764b998b1d...](https://github.com/Isratosh/tgstation/commit/764b998b1d5df5fce7df0d2ecd1b1758445a8b3e)
#### Monday 2023-10-30 06:44:45 by carlarctg

Adds a Syndicate Monkey Agent beacon uplink item (#79012)

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

Co-authored-by: ATH1909 <42606352+ATH1909@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [hanyang-tony/git](https://github.com/hanyang-tony/git)@[8f23432b38...](https://github.com/hanyang-tony/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Monday 2023-10-30 07:18:51 by Johannes Schindelin

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
## [Kallitty/qface](https://github.com/Kallitty/qface)@[70201bcdfe...](https://github.com/Kallitty/qface/commit/70201bcdfe84361694d63d011a21331322a388f5)
#### Monday 2023-10-30 07:46:17 by Kallitty

Create README.md

Introducing Qface: Bridging the Gap in Social Media

In a rapidly evolving digital landscape, Qface emerges as the revolutionary social media app designed to transcend boundaries and connect people from all corners of the globe. With a core mission of fostering safe, meaningful interactions, Qface redefines the way we engage with others in the virtual realm.

In a world where physical distance can often separate us, Qface breaks down these barriers, allowing you to engage, share, and connect like never before. This innovative platform is designed to offer its users a captivating and secure experience that encourages authentic human connections.

Qface is more than just a social media app; it's a space where friendships are forged, ideas are exchanged, and experiences are shared, all while ensuring privacy and security are at the forefront. Whether you're connecting with loved ones on the other side of the world, making new friends, or exploring shared interests with like-minded individuals, Qface is your digital bridge to a world of endless possibilities.

Join us on Qface, where distance is no barrier, and the joy of social interaction knows no bounds. Experience a safer, more connected, and enriching world of online relationships with Qface.

---
## [wojtekmaj/berry](https://github.com/wojtekmaj/berry)@[6460b597fa...](https://github.com/wojtekmaj/berry/commit/6460b597fad141ff1b3fb792a2c53514ceb07b8b)
#### Monday 2023-10-30 07:49:06 by Tom Szwaja

docs: fix old info in contributing guide (#5779)

**What's the problem this PR addresses?**
<!-- Describe the rationale of your PR. -->
<!-- Link all issues that it closes. (Closes/Resolves #xxxx.) -->

EDIT: I just saw that #5776 beat me to it. However, the version I
propose adds clarity imho as well as links to relevant resources.

---

The instructions in the 'Writing documentation' section gave false
information (I assume it was simply outdated), making it harder for
people to contribute.

Pls tag for Hacktoberfest.
...

**How did you fix it?**
<!-- A detailed description of your implementation. -->

* Revised the 'Writing documentation' section so that it aligns with our
current project structure
* Fixed broken links
* Provided links to the tech we use  
...

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
- [ ] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

Co-authored-by: Maël Nison <nison.mael@gmail.com>

---
## [TheBronJameOffical/lobotomy-corp13](https://github.com/TheBronJameOffical/lobotomy-corp13)@[74616938ea...](https://github.com/TheBronJameOffical/lobotomy-corp13/commit/74616938ea851883011b75d31426e8effdbcd32e)
#### Monday 2023-10-30 07:59:58 by The Bron Jame Offical

⎓⚍ᓵꖌ FUCK||𝙹⚍YOU, CURSE OF VIOLET NOON

more joke EGO

fucked around with fluid sack code for this one

Added ᓵ⚍∷ᓭᒷ 𝙹⎓ ⍊╎𝙹ꖎᒷℸ ̣  リ𝙹𝙹リ

---
## [Offroaders123/MCA-Buffer](https://github.com/Offroaders123/MCA-Buffer)@[2ed3b544ed...](https://github.com/Offroaders123/MCA-Buffer/commit/2ed3b544edff454f5223fccec520cba51cb0a463)
#### Monday 2023-10-30 08:04:41 by Offroaders123

Chunk Header Compression Byte

Next demo of reading content. Trying to get all of the values in one map iteration, rather than looping over things multiple times. Going to take multiple versions to find what works the best, just like the reading code needed to do.

https://wiki.vg/Region_Files#Chunk_Header

Yeah, turns out the read Chunk bytes were one byte too long when reading from the source Region file, and it's because of this small overlook I missed when implementing the Region logic. The length of the Chunk data for Region Entries includes the compression flag byte, but I remove that when doing the Entry building, so I added the handling for that to make it the one byte shorter as it needs to be. Thankfully the whole Region continued to parse fully correct with no errors, so it was a silent little bug that wasn't causing errors, it just wasn't implemented right. That also works out great because all of the Chunks are compressed, and the trailing bytes always happened to be zeros, meaning zlib just ignored them when decompressing. Had it been plain NBT, it would've failed, and had it been non-zeros I think zlib would have failed too. I might be mis-remembering whether that's the case for zlib, I thought I heard that somewhere though.

Flamingosis; thinking of listening to parts of The Incident after this, I think because I was thinking about my old PE worlds from my phone, and that's when I was listening to that album a lot, when I made those worlds just before starting high school. So essentially I was thinking about Minecraft during that time period, which reminded me about that music.

---
## [cyphar/runc](https://github.com/cyphar/runc)@[02d02948df...](https://github.com/cyphar/runc/commit/02d02948dfa4b6ea99522cc8ab5f72f297c95000)
#### Monday 2023-10-30 08:13:55 by Aleksa Sarai

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
## [harryob/cmss13](https://github.com/harryob/cmss13)@[de5c69661f...](https://github.com/harryob/cmss13/commit/de5c69661f8d33425123894028702f64239f861b)
#### Monday 2023-10-30 08:22:28 by kiVts

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
## [gradle/gradle](https://github.com/gradle/gradle)@[2805c3fda2...](https://github.com/gradle/gradle/commit/2805c3fda24da90bb9544ec197335259d983b2cd)
#### Monday 2023-10-30 08:45:31 by bot-gradle

Merge pull request #26874 Improve performance of RelativePath canonicalization

This is a follow-up to https://github.com/gradle/gradle/pull/24943.

There was some uncertainty as to whether that change resulted in a detectable drop in performance in Gradle's overall performance tests. I put together [some benchmarks](https://github.com/AlexLandau/gradle-relative-path-perf) looking at the constructor method that was modified, and based on my probably-non-representative sample of test cases, the new implementation took around 3.4x as long as the one that did not perform canonicalization.

The version in this PR skips running canonicalization checks on segments that come from existing `RelativePath` objects, which have already been canonicalized. This implementation actually performs better than the original, pre-canonicalization implementation in my benchmark test; I would take this with a grain of salt, as I do not have experience with JMH and may have used a poor setup or poor choice of test cases. (There's at least some evidence that for the range of test cases attempted, copying into the array with a for loop is faster than `System.arraycopy`, which would explain this. This could, of course, vary across JVM versions and other factors.)

### Contributor Checklist
- [x] [Review Contribution Guidelines](https://github.com/gradle/gradle/blob/master/CONTRIBUTING.md)
- [x] Make sure that all commits are [signed off](https://git-scm.com/docs/git-commit#Documentation/git-commit.txt---signoff) to indicate that you agree to the terms of [Developer Certificate of Origin](https://developercertificate.org/).
- [x] Make sure all contributed code can be distributed under the terms of the [Apache License 2.0](https://github.com/gradle/gradle/blob/master/LICENSE), e.g. the code was written by yourself or the original code is licensed under [a license compatible to Apache License 2.0](https://apache.org/legal/resolved.html).
- [x] Check ["Allow edit from maintainers" option](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) in pull request so that additional changes can be pushed by Gradle team
- [ ] Provide integration tests (under `<subproject>/src/integTest`) to verify changes from a user perspective
- [ ] Provide unit tests (under `<subproject>/src/test`) to verify logic
- [ ] Update User Guide, DSL Reference, and Javadoc for public-facing changes
- [x] Ensure that tests pass sanity check: `./gradlew sanityCheck`
- [x] Ensure that tests pass locally: `./gradlew <changed-subproject>:quickTest`

### Reviewing cheatsheet

Before merging the PR, comments starting with
- ❌ ❓**must** be fixed
- 🤔 💅 **should** be fixed
- 💭 **may** be fixed
- 🎉 celebrate happy things

Co-authored-by: Alex Landau <alandau@cs.stanford.edu>

---
## [minghsuanwu/Open-Assistant](https://github.com/minghsuanwu/Open-Assistant)@[b9c60ed582...](https://github.com/minghsuanwu/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Monday 2023-10-30 09:53:14 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [James-h-1969/NicsFavsA3](https://github.com/James-h-1969/NicsFavsA3)@[6982d86fa5...](https://github.com/James-h-1969/NicsFavsA3/commit/6982d86fa5eafd7ac5b4b5eac3c42526593ad0ed)
#### Monday 2023-10-30 09:57:58 by Alex Gray

No Fuck you

I will not push this code for you fuck you. ┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻

---
## [ginsanjimi/ginsanjimi](https://github.com/ginsanjimi/ginsanjimi)@[d8dbfd664f...](https://github.com/ginsanjimi/ginsanjimi/commit/d8dbfd664ff449dbacc38dfba3a4c2e6d761e382)
#### Monday 2023-10-30 10:17:56 by ginsanjimi

Create Man Utd defeat

Erik ten Hag has said Manchester United's heavy derby defeat to Manchester City was one of his worst days as manager at Old Trafford.

City cruised to a 3-0 win on Sunday thanks to two goals from Erling Haaland, including a first-half penalty, and another from Phil Foden.

Ten Hag has suffered some dismal results as United manager, but asked whether the latest defeat to Pep Guardiola's side made it one of his worst days in the job, he said: "Yes."

He added: "Of course, it is disappointing, but last year we had many highlights. When you lose a derby in the way we lose, that is disappointing.

"First half we had a very good game plan and the execution was also very good. It was toe-to-toe first and it was very similar, but then the penalty changed the moment. Then, in the second half we chose to become more offensive and it is 2-0 too quickly. From that point on it was a difficult game."

United have now lost five of their first 10 league games for the first time since 1986 and sit eighth in the Premier League table, already 11 points behind leaders Tottenham.

https://sketchfab.com/3d-models/taylor-swift-the-eras-tour-film-completo-ita-37a24d6ad11e4c1a8b4c22fe9852c839
https://sketchfab.com/3d-models/totally-killer-film-completo-ita-dd72180e42c24300a2f5032601a3e0a1
https://sketchfab.com/3d-models/once-upon-a-studio-film-completo-ita-b4ff07859a684797a1249d2643555a5f
https://sketchfab.com/3d-models/saw-x-film-completo-ita-ee45d2a5d5df4a6f819b9ff2e5bb335f
https://sketchfab.com/3d-models/the-burial-il-caso-okeefe-film-completo-ita-6d0394b75e29446a9495d60f2cfd3f7f
https://sketchfab.com/3d-models/five-nights-at-freddys-film-completo-ita-db04d136ccee4a298fd4aa4ff7283f0f
https://sketchfab.com/3d-models/killers-of-the-flower-moon-film-completo-ita-97f3cd25982d4aaaa75a3c94182ff4dc
https://sketchfab.com/3d-models/the-marvels-film-completo-ita-beb1fe6a27ac4e2ab1f0bb95ee508084
https://sketchfab.com/3d-models/the-creator-film-completo-ita-758b41cbfc764d95b9484731fbfeb6df
https://sketchfab.com/3d-models/reptile-film-completo-ita-8190d0a375b14cad98f2119bfd0d4fc2
https://sketchfab.com/3d-models/taylor-swift-the-eras-tour-pelicula-completa-cbc46c1290de4af2a971eca6becaa8fc
https://sketchfab.com/3d-models/dulces-y-sangrientos-16-pelicula-completa-8038fcbcde924479a025911e1b47c08a
https://sketchfab.com/3d-models/habia-una-vez-un-estudio-pelicula-completa-ce0bf3c36cf6498d8315faab46063626
https://sketchfab.com/3d-models/saw-x-el-juego-del-miedo-pelicula-completa-cd87090cba98444c86934c93adb312b3
https://sketchfab.com/3d-models/enterrando-una-ambicion-pelicula-completa-91c1015e30184b10a6677ff4c12bacee
https://sketchfab.com/3d-models/five-nights-at-freddys-pelicula-completa-ea702f6c5ade4e6b91a06c08abc692e6
https://sketchfab.com/3d-models/los-asesinos-de-la-luna-pelicula-completa-2c21e8d554824654bdff4909aa051ac2
https://sketchfab.com/3d-models/the-marvels-pelicula-completa-066b4e13714949c681220628fdbc29a8
https://sketchfab.com/3d-models/resistencia-pelicula-completa-761db1fba3b042499d962284c3ecf911
https://sketchfab.com/3d-models/reptiles-pelicula-completa-latino-29e49f70f5a44dc298c7d750ffa4f58c
https://sketchfab.com/3d-models/nezd-taylor-swift-the-eras-tour-teljes-film-5d88a05d92a04486b27d93b84ae48eb6
https://sketchfab.com/3d-models/nezd-gyilkos-a-multbol-teljes-film-d96ff0d59e314590bcd5b68ae8da20f7
https://sketchfab.com/3d-models/nezd-volt-egyszer-egy-studio-teljes-film-fa7c9a9ab1c34e6f8ec0ab3c10a62d74
https://sketchfab.com/3d-models/nezd-furesz-10-teljes-film-598eaea46d7e417689910e357592e3cf
https://sketchfab.com/3d-models/nezd-a-temetes-teljes-film-83b5b1133271490b9255c369cb083da8
https://sketchfab.com/3d-models/nezd-ot-ejjel-freddy-pizzazojaban-teljes-film-43d62de1941c407f9fee4f1816d4479f
https://sketchfab.com/3d-models/nezd-megfojtott-viragok-teljes-film-bf438270bec748ac8ff55bd68efc8d44
https://sketchfab.com/3d-models/nezd-marvelek-teljes-film-49aeacf656c0453687a9c4a867cd438d
https://sketchfab.com/3d-models/nezd-az-alkoto-teljes-film-32fb19919e2846c9a9f3d0177765dce3
https://sketchfab.com/3d-models/nezd-hidegver-teljes-film-9d6f9a6772ac4db694359027a1367fae
https://sketchfab.com/3d-models/taylor-swift-the-eras-tour-filme-completo-86f0378ba69c418f809aaac3f2c6177a
https://sketchfab.com/3d-models/dezesseis-facadas-filme-completo-bec6df9fb4e14241b4639ff27f5250ee
https://sketchfab.com/3d-models/era-uma-vez-um-estudio-filme-completo-12c016360c774b53ad23a49e45ca0aa2
https://sketchfab.com/3d-models/jogos-mortais-x-filme-completo-2a2355bb24434092a427d97a189f0758
https://sketchfab.com/3d-models/o-proprio-enterro-filme-completo-5fd43f49bff041eda45a085d3f7f9e34
https://sketchfab.com/3d-models/freelance-filme-completo-469f0e3539824a6f8824b351069939bf
https://sketchfab.com/3d-models/assassinos-da-lua-das-flores-filme-completo-dcefc3f6f2204ed281a3ca6694ba304c
https://sketchfab.com/3d-models/as-marvels-filme-completo-87cdaa88f3a54a7094c4d1f506e5335d
https://sketchfab.com/3d-models/resistencia-filme-completo-f897fa0ed42e4a4799ff07c89979eb16
https://sketchfab.com/3d-models/camaleoes-filme-completo-dfb63797370d42abb4518ca6e7a31bcc

It is now seven defeats from 14 games in all competitions this season but Ten Hag said he is confident his team are making progress.

"The three games before we won and the spirit is very good," Ten Hag said. "I think we are on the way up. The start was difficult but now we are on the way up. When injuries are getting back we will be getting stronger. We have to be patient but I am happy with some injuries coming back and then our side will be stronger."

Afterwards, Ten Hag said he stood by his decision to drop Raphaël Varane and Sergio Reguilón to the bench in favour of Jonny Evans and Victor Lindelöf while also defending his decision to replace striker Rasmus Højlund midway through the second half after the substitution was greeted with loud boos from the United fans inside Old Trafford.

"I have to protect Rasmus Højlund and I have to protect the team," Ten Hag added.

"He is putting so much effort in pressing, going in the transitions, going the long ways, fighting a tough opposition.

"He is not used to it, three games in a week, so I have to protect him and the team, to bring some energy in. We have bench players, Mason Mount and [Alejandro] Garnacho, we know he can change games."

---
## [jbwittner/bankwiz_frontend](https://github.com/jbwittner/bankwiz_frontend)@[6f3cb0b3a1...](https://github.com/jbwittner/bankwiz_frontend/commit/6f3cb0b3a1fadf17394304202d4d6310a2cc795c)
#### Monday 2023-10-30 10:24:07 by Jean-Baptiste WITTNER

add makefile (#28)

* I hate this fucking language.

* SHIT ===> GOLD

---
## [sthagen/AliveToolkit-alive2](https://github.com/sthagen/AliveToolkit-alive2)@[e031ebd9c1...](https://github.com/sthagen/AliveToolkit-alive2/commit/e031ebd9c18be1a4fc7f37ab193b4b158b92dd9a)
#### Monday 2023-10-30 10:25:02 by Flash Sheridan

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
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[e7caf52c21...](https://github.com/realforest2001/forest-cm13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Monday 2023-10-30 10:59:20 by fira

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
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[e120ab795b...](https://github.com/realforest2001/forest-cm13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Monday 2023-10-30 10:59:20 by fira

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
## [NourhAlmutairi/Note-Taking-Website](https://github.com/NourhAlmutairi/Note-Taking-Website)@[1a4100310b...](https://github.com/NourhAlmutairi/Note-Taking-Website/commit/1a4100310ba18c4684560d219815fd6e8c184bce)
#### Monday 2023-10-30 10:59:41 by Noura

Note-Taking Website

Website Overview:

Our note-taking website is a user-friendly online platform designed to help you capture, organize, and retrieve your notes effortlessly. Whether you're a student, professional, or simply looking for a digital space to jot down your thoughts, our website is here to simplify your note-taking experience.

---
## [VannyBuns/Kurisu](https://github.com/VannyBuns/Kurisu)@[4e203bc17a...](https://github.com/VannyBuns/Kurisu/commit/4e203bc17a55bd0bd087f9e1ce0b891da8bfa916)
#### Monday 2023-10-30 11:09:49 by dany

Revamp code for seasonal commands (#816)

* Revamp code for seasonal commands

This should get tested for bugs/user friendlyness first
before getting merged.

* Holy fucking shit I hate python duck typing so much

* Address pr review

* Fix potential logic error for season fetching

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[2a74c23d62...](https://github.com/meemofcourse/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Monday 2023-10-30 11:15:56 by Imaginos16

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
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[bf4671ff83...](https://github.com/meemofcourse/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Monday 2023-10-30 11:15:56 by retlaw34

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
## [LanceSmites328/LC13Master](https://github.com/LanceSmites328/LC13Master)@[aee88dbf1f...](https://github.com/LanceSmites328/LC13Master/commit/aee88dbf1f49f56eb6db836939354aef09b70aae)
#### Monday 2023-10-30 11:17:00 by The Bron Jame Offical

Purple Tear Weapon (#1513)

Power effects this die x2

Oh boy, this ones funny.

Adds PT file, Weapon Sprites, and Sounds.

Inhands and Status sprites added

fucking oopsx2

added guard stance effect and force boost

added mirage storm

guard stance shield fix

adjusted sleep times

mirage storm tweaks

moved ability to the charging type (thanks blue sicko)

1 charge per hit, no refunds

buff at the end of mirage storm

I love running 4 for loops in a single proc

think i fucked up in the last branch, oh well!

mirage storm reset

fuck. nevermind charging type does not work at all

refined mirage storm a bit

ability now works in a (hopefully) non weird way

new beam baby

fuck it, it works

I FORGOR

got rid of a redundancy or two

---
## [semrush/intergalactic](https://github.com/semrush/intergalactic)@[e4574fbd64...](https://github.com/semrush/intergalactic/commit/e4574fbd64f2e75baf579ff2d4b949889d194d8c)
#### Monday 2023-10-30 11:55:57 by Michael Sereniti

[checkbox] simplified and advanced use (#775)

## Motivation and Context

We have long lasting issue with several input controls:
It's exposed as a single component but contains two DOM nodes and
distributes it with mechanism named `getInputProps`.
This a stupid and weird api because setting your own %input-props%
overrides default props distribution and makes backward compatibility of
component extremely complex.

Usage of that mechanism indicates that component api is not designed
well and requires backward compatible changes.

Affected components list: `filter-trigger`, `checkbox`, `input-mask`,
`radio`, `switch`.

This PR changes api of the checkbox component and allows user to have to
more control over component without using `getInputProps` overriding.

Also this PR includes removing use of `hoistProps` core enhance from the
component.

## How has this been tested?

All existing tests work well. Also I've manually tested changed
component playground and examples.

## Screenshots:

<img width="699" alt="Screen Shot 2023-09-21 at 17 52 58"
src="https://github.com/semrush/intergalactic/assets/31261408/72947b60-3c88-4b50-8268-01c0ae41fa88">

<img width="699" alt="Screen Shot 2023-09-21 at 17 53 13"
src="https://github.com/semrush/intergalactic/assets/31261408/6e206915-ae82-4268-a73a-f0922de6e3e0">

## Types of changes

<!--- What types of changes does your code introduce? Put an `x` in all
the boxes that apply: -->

- [ ] Bug fix (non-breaking change which fixes an issue).
- [x] New feature (non-breaking change which adds functionality).
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected).
- [x] Nice improve.

## Checklist:

<!--- Go over all the following points, and put an `x` in all the boxes
that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
here to help! -->

- [x] My code follows the code style of this project.
- [x] I have updated the documentation accordingly or it's not required.
- [x] Unit tests are not broken.
- [x] I have added changelog note to corresponding `CHANGELOG.md` file
with planned publish date.
- [ ] I have added new unit tests on added of fixed functionality.

---------

Co-authored-by: ilyabrower <ilia.brauer@semrush.com>
Co-authored-by: semrush-ci-whale <semrush-ci-whale@users.noreply.github.com>

---
## [Biki-das/react-1](https://github.com/Biki-das/react-1)@[1ebedbec2b...](https://github.com/Biki-das/react-1/commit/1ebedbec2bec08e07c286ea6c3cff62737a0fd3a)
#### Monday 2023-10-30 12:42:20 by Sebastian Markbåge

Add Server Context deprecation warning (#27424)

As agreed, we're removing Server Context. This was never official
documented.

We've found that it's not that useful in practice. Often the better
options are:

- Read things off the url or global scope like params or cookies.
- Use the module system for global dependency injection.
- Use `React.cache()` to dedupe multiple things instead of computing
once and passing down.

There are still legit use cases for Server Context but you have to be
very careful not to pass any large data, so in generally we recommend
against it anyway.

Yes, prop drilling is annoying but it's not impossible for the cases
this is needed. I would personally always pick it over Server Context
anyway.

Semantically, Server Context also blocks object deduping due to how it
plays out with Server Components that can't be deduped. This is much
more important feature.

Since it's already in canary along with the rest of RSC, we're adding a
warning for a few versions before removing completely to help migration.

---------

Co-authored-by: Josh Story <josh.c.story@gmail.com>

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[300bfa58f1...](https://github.com/argilla-io/argilla/commit/300bfa58f1a7469019921f921f411f1c25bcd984)
#### Monday 2023-10-30 12:43:24 by Ayan Joshi

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
## [TenorioLucass/numpy](https://github.com/TenorioLucass/numpy)@[af55348f5c...](https://github.com/TenorioLucass/numpy/commit/af55348f5cbe338a86ed032812ee11e8714be673)
#### Monday 2023-10-30 13:01:58 by Sebastian Berg

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
## [mpusz/wg21-papers](https://github.com/mpusz/wg21-papers)@[d7adc57ad0...](https://github.com/mpusz/wg21-papers/commit/d7adc57ad089589a919bfc2cd065fa6094286069)
#### Monday 2023-10-30 15:06:59 by Chip Hogg

Update "quantity as numeric type" text for R1

The only actual edit I've made was to add a line in the common unit
computation, which makes it easier to understand.

I've also collected a variety of feedback about other sections on the
paper.  This feedback was harder to translate cleanly into edits, but I
wanted to find _some_ home for it.  Additionally, even if I _could_ make
edits, it may not be wise to do so, because we want to minimize changes
before the committee discusses it next week.  So I'll add this feedback
to the PR summary.

- 4.6: What are some concrete use cases for `kind_of<...>`?  I have a
  hard time seeing the motivation --- both for this feature, and for the
  rules at the end (e.g., arithmetic with a kind and non-kind produces a
  non-kind).

- 6.4.1: I don't understand the meaning of the equality operator for
  dimensions, nor its implementation.  Does it not break transitivity,
  which is a critically important property for an equality operator?  If
  B and C both derive from A, then each would compare equal with A, but
  not with each other.  Do we even _want_ equality of dimensions?
  Wouldn't we be better off by providing separately named functions for
  different kinds of equivalence?

- 6.4.3: What is a "canonical unit"?  I'm not familiar with this
  concept.

- 7.4: What does this mean?  What is the "reference unit" of a unit?
  I'm not familiar with this concept.

- 7.5: Subjectively, the chapter feels awfully big for something so
  speculative.  Are we sure we want to go into this much detail before
  we have accumulated much more (any?) real world experience?

- 7.5.1: Multiplication of vectors is mathematically defined using
  geometric algebra.  The product is the "geometric product".  It
  produces, essentially, a complex number (the sum of a real part and a
  bivector part, the latter of which encodes information about the plane
  spanned by the vectors).  This is part of my worry with the system of
  characters: there's not Just One System in mathematics, and we may
  exclude or make awkward certain important use cases.

- 7.5.2: If we _do_ go this route, I expect we'll want more characters
  than just scalar, vector, and tensor.  The current setup would allow
  adding the result of a cross product of two vectors to another vector,
  but this seems like a missed opportunity to prevent errors.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[22fec01a5e...](https://github.com/treckstar/yolo-octo-hipster/commit/22fec01a5e8368749ae20e18120184f4895026e8)
#### Monday 2023-10-30 15:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Kaz205/kernel_common](https://github.com/Kaz205/kernel_common)@[e58e929f50...](https://github.com/Kaz205/kernel_common/commit/e58e929f50863a9ae3cf0a841b5820f03dccd68c)
#### Monday 2023-10-30 15:39:26 by Douglas Anderson

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

---
## [thornAvery/jep-hack](https://github.com/thornAvery/jep-hack)@[56bf3ef2b0...](https://github.com/thornAvery/jep-hack/commit/56bf3ef2b0271590f239a8eb467b72fb62936530)
#### Monday 2023-10-30 15:46:22 by Llinos Evans

Finish Lake of Rage "town"

Well, sort of. There's still a lot you can do with Pryce's House, it needs more things.

I want to make it so Pryce only appears when the Red Gyarados has been defeated. Maybe he can give a TM or something too.

This commit does the following;
- Fix the weird landmarking because I was a dumb stupid idiot.
- Adds all the relevant signs.
- Adds Pryce's House over where the gym was. Just a cute, quaint little place.

---
## [VivekKumar62/Password-Generator](https://github.com/VivekKumar62/Password-Generator)@[7522c1687e...](https://github.com/VivekKumar62/Password-Generator/commit/7522c1687e56a36f33056095a0967e119e6d0e9d)
#### Monday 2023-10-30 16:22:42 by Vivek Kumar

Add files via upload

A password generator website is an online tool or service designed to create strong, random, and secure passwords for various online accounts and applications. These websites are typically user-friendly and provide a convenient way for individuals to generate unique passwords that are difficult for hackers to guess or crack. Here's a description of a typical password generator website:

Title: Password Generator

Description:
A Password Generator website is your one-stop solution for creating robust and uncrackable passwords to enhance your online security. With the increasing need for secure online accounts, our user-friendly tool ensures your sensitive data remains protected.

Key Features:

Customization: Tailor your password to meet specific requirements, such as length, character types (uppercase letters, lowercase letters, numbers, special characters), and avoid ambiguous characters.

Strength Indicator: A built-in strength indicator helps you gauge the security level of your password, ensuring it's strong enough to thwart malicious attempts.

Randomization: Generate entirely random passwords with a single click. This prevents the use of predictable patterns or easily guessable combinations.

No Storage: We don't store or save any of the passwords you generate, prioritizing your privacy and security.

User-Friendly: Our intuitive interface ensures that even those with minimal technical expertise can create strong passwords effortlessly.

Copy and Paste: Easily copy the generated password to your clipboard and paste it where needed. Quick and convenient!

Accessibility: Access the tool from any device with an internet connection, making it readily available whenever you need it.

No Registration: No need to create an account or provide personal information. It's hassle-free and straightforward.

Multi-Language Support: Available in multiple languages for a global user base.

Open Source: (Optional) For transparency, some password generators provide open-source code for review and verification.

Using our Password Generator website, you can fortify your online security, protect your accounts, and gain peace of mind knowing your information is safe from unauthorized access. Say goodbye to weak, easily guessable passwords and welcome the era of digital security.

Remember, creating a strong and unique password for each of your online accounts is an essential practice to safeguard your digital life.

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[e014f5e257...](https://github.com/sourcegraph/sourcegraph/commit/e014f5e2573057a43ae61bf9ed8b68dba685a282)
#### Monday 2023-10-30 16:29:09 by Felix Kling

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
## [spacesweedkid-27/Deklarative-Programmierung-WS23-CAU-Kiel](https://github.com/spacesweedkid-27/Deklarative-Programmierung-WS23-CAU-Kiel)@[a8699512b5...](https://github.com/spacesweedkid-27/Deklarative-Programmierung-WS23-CAU-Kiel/commit/a8699512b53fd5a1e007608e7d28c83969086330)
#### Monday 2023-10-30 17:04:52 by Henri Heyden

Fuck your dumb ass prechecker that fails with light warnings because you want to annoy me.

---
## [aiguofer/arrow](https://github.com/aiguofer/arrow)@[3beb93af36...](https://github.com/aiguofer/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Monday 2023-10-30 17:27:41 by Kevin Gurney

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
## [VickiMorris/BeeStation-Hornet](https://github.com/VickiMorris/BeeStation-Hornet)@[4be515717e...](https://github.com/VickiMorris/BeeStation-Hornet/commit/4be515717e50cfd4dc5ac97a861ab6e04dd9f188)
#### Monday 2023-10-30 17:31:23 by VickiMorris

shitcode compiles, will tear out later

On second thought, I'm just gonna make the musket itself a reagent container instead of adding an internal one and fucking around with shittons of snowflake code. It compiles in the current state but is a bullshit stupid implementation of how I want it to work bluh bluh bluh

---
## [Gosth15/android_kernel_xiaomi_sm8475](https://github.com/Gosth15/android_kernel_xiaomi_sm8475)@[3a9710df43...](https://github.com/Gosth15/android_kernel_xiaomi_sm8475/commit/3a9710df435e28979f771cd9780d127ec5029fd9)
#### Monday 2023-10-30 17:48:34 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[fa9196f1bb...](https://github.com/GeoB99/reactos/commit/fa9196f1bbbe0e5abc0531d30c21afabb65110d2)
#### Monday 2023-10-30 18:35:12 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [FreddyZeng/iTerm2](https://github.com/FreddyZeng/iTerm2)@[41484379d7...](https://github.com/FreddyZeng/iTerm2/commit/41484379d704cfc6c7c24b778e51acc246087032)
#### Monday 2023-10-30 18:36:51 by George Nachman

Turn off the idiotic xcode 15 console. I'm so tired of this shit

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d31c21ff1b...](https://github.com/tgstation/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Monday 2023-10-30 19:15:44 by jimmyl

new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles


https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566



https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past


https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range


https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that


https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae



## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [ickshonpe/bevy](https://github.com/ickshonpe/bevy)@[3ee9edf280...](https://github.com/ickshonpe/bevy/commit/3ee9edf280c530f35a51049ec92fcfa552998614)
#### Monday 2023-10-30 20:01:01 by Ethereumdegen

add try_insert to entity commands (#9844)

# Objective

- I spoke with some users in the ECS channel of bevy discord today and
they suggested that I implement a fallible form of .insert for
components.

- In my opinion, it would be nice to have a fallible .insert like
.try_insert (or to just make insert be fallible!) because it was causing
a lot of panics in my game. In my game, I am spawning terrain chunks and
despawning them in the Update loop. However, this was causing bevy_xpbd
to panic because it was trying to .insert some physics components on my
chunks and a race condition meant that its check to see if the entity
exists would pass but then the next execution step it would not exist
and would do an .insert and then panic. This means that there is no way
to avoid a panic with conditionals.

Luckily, bevy_xpbd does not care about inserting these components if the
entity is being deleted and so if there were a .try_insert, like this PR
provides it could use that instead in order to NOT panic.

( My interim solution for my own game has been to run the entity despawn
events in the Last schedule but really this is just a hack and I should
not be expected to manage the scheduling of despawns like this - it
should just be easy and simple. IF it just so happened that bevy_xpbd
ran .inserts in the Last schedule also, this would be an untenable soln
overall )

## Solution

- Describe the solution used to achieve the objective above.

Add a new command named TryInsert (entitycommands.try_insert) which
functions exactly like .insert except if the entity does not exist it
will not panic. Instead, it will log to info. This way, crates that are
attaching components in ways which they do not mind that the entity no
longer exists can just use try_insert instead of insert.

---

## Changelog

 

## Additional Thoughts

In my opinion, NOT panicing should really be the default and having an
.insert that does panic should be the odd edgecase but removing the
panic! from .insert seems a bit above my paygrade -- although i would
love to see it. My other thought is it would be good for .insert to
return an Option AND not panic but it seems it uses an event bus right
now so that seems to be impossible w the current architecture.

---
## [CatsheeDev/grocerystorerblx.github.io](https://github.com/CatsheeDev/grocerystorerblx.github.io)@[a43c2fcbd1...](https://github.com/CatsheeDev/grocerystorerblx.github.io/commit/a43c2fcbd115f26a5cced388d2c9d82471419487)
#### Monday 2023-10-30 20:12:39 by Cats

i remember when taking blood last Thursday i almost jumped out of the seat while they were still extracting that shit like holy shit they had to pin me down cuz i almost got up

---
## [ofaruk0169/todoAndroidKotlin](https://github.com/ofaruk0169/todoAndroidKotlin)@[a3f6591c4f...](https://github.com/ofaruk0169/todoAndroidKotlin/commit/a3f6591c4f619bfd2fd45dadc83c5acde9be5a0f)
#### Monday 2023-10-30 20:23:54 by Omare Faruk

I have gone over the layout refresher from the course I am following. I will be implementing recycler view (again) tomorrow morning. Worked hard and got in front of the computer today so do feel like I have accomplished a lot. I passed my theory test for driving too so I am not being too hard on myself anymore. I am a little tired of being hard on myself, I work hard in my life. Yes, not everything goes to plan, but God loved a trier. Passing my theory today made me realise that the effort I put in does pay off, I think that's why sometimes I feel so depressed in regards to coding, i put in so many hours and im still not a developer. But things take time and I know I'll get to where I need to be as I put in my concistent effort I know I can put in

---
## [ayissijoachim122/sas.com](https://github.com/ayissijoachim122/sas.com)@[f2d17e7603...](https://github.com/ayissijoachim122/sas.com/commit/f2d17e7603369d4d1b2c29b54a6540bcd49ad0cd)
#### Monday 2023-10-30 20:38:34 by AYISSI  JOACHIM

Create generator-generic-ossf-slsa3-publish.yml

                       email  ayissijoachim.72@gmail.com
E-mail
mobile@ecwid.com
place
Adresse
https://www.societe.com
verified_user
Règles de confidentialité
https://www.lightspeedhq.com/legal/privacy-policy/
https://share.vimeo.com/ayissijoachim.72
Dear Manager,

 thank you for visiting and validating my company from my city and my account has been checked all correct thank you thank you but I would have to send you other documents such as an administrative letter from our company with the members of administration and company stamp making liver thank you I beg you to be able to program all my funds for bank investment real estate investment bank loan lottery in bank States A States for program and investment loan and repayable to the Company Establishment Ayissi Joachim cella will be for life and also for the other investment in the program with my country Cameroon cella guide has worked with reliable investment agreements such as agriculture tourism trade and transport a general guide with global business climates with the world here is what we intend to do


Contact: AYISSI JOACHIM
E-mail: xxxjoachim122@yahoo.com
CellPhone: 237694616643
Software: Rent - Payment Platform Whitelabel
Country: Cameroon - Cameroon e Cameroun
Message: Name: AYISSI Joachim
              Address e_mail : ayissi_joachim@yahoo.com
              Phone. : (237) 677 89 16 02/694 61 66 43


Bank  Name : Union  Bank  PLC
BANK  ADRESSE: PObox 15569  Douala  Cameoon
Bank Account Name :   AYISSI  JOACHIM
Bank ACCOUNT  NUMBER  : 00410017574
BANK SWIFT : UCMACMCX
IBAN :CM21  10023  00040  00410017574  54

____________________________________________________
NEW IDENTIFICATION
              Name: ETABISSEMENT  AYISSI  JOACHIM
              Address e_mail : xxxjoachim122@yahoo.com
              BP. : 17474  DOUALA - Cameroon
              Phone. : (237) 677 89 16 02
              Bank Name - UNITED  BANK OF AFRICA
               IBAN :  CM21 10033  05207  07016001289  65
            AccounT ,Naime ; ETS  AYISSI  JOACHIM
            Account  Number ; 07016001289
            BANK CODE      SWIFT : UNAFCMCX
_________________________________________________

Bank  Name : Union  Bank  PLC
BANK  ADRESSE: PObox 15569  Douala  Cameoon
Bank Account Name :   AYISSI  JOACHIM
Bank ACCOUNT  NUMBER  : 00410017574
BANK SWIFT : UCMACMCX
IBAN :CM21  10023  00040  00410017574  54

Logo Google Cloud Bienvenue
Vous travaillez dans
.@JoachimAyi47226
https://www.instagram.com/ayissi_joachim
https://twitter.com/JoachimAyi47226
https://www.facebook.com/joachim.ayissi
https://www.pinterest.com/ayissijoachim/
https://www.linkedin.com/ayissijoachim
https://www.youtube.com/@ayissijoachim4632
https://github.com/ayissijoachim122
  ayissijoachim122/AYISSI-JOACHIM
Numéro du projet : 868342099878
ID du projet : confident-abode-401217
Tableau de bord
Recommandations
@ayissijoachim sur #Vimeo https://vimeo.com/876431318 

- Identification requirements in the provisions of the new Regulations
in force in CEMAC States, following IMF reforms.
- Provisions for the fight against money laundering and the financing
of terrorism ; justification of transfers above 10,000 (ten thousand)
USD more favorable for anenterprise than a physical person .
- Need to provide the KYC of the Principal (YOU) and th

---
## [Majkl-J/Bubberstation](https://github.com/Majkl-J/Bubberstation)@[e39a44e462...](https://github.com/Majkl-J/Bubberstation/commit/e39a44e4628fd8846287360e8988ff265276bfec)
#### Monday 2023-10-30 21:03:16 by SkyratBot

[MIRROR] Fixes display of appearance type in VV [MDB IGNORE] (#24092)

* Fixes display of appearance type in VV (#78725)

## About The Pull Request

Appearance vars are awful to detect. They have a type var you can
access, for an appearance the value of this var is `/image`. However
`istype(appearance, /image) == 0`. This is good enough for
identification, you might think this just means detecting appearance
would be something like `if(thing.type == /image && !istype(thing,
/image))`, but there's a problem with this: `istype(appearance, /datum)
== 0`. For that matter it seems like all istypes that check if an
appearance is some type fail, so you can't know that it's safe to access
the `.type` var to do that earlier combined check.

Now we get into magic territory, `istype(new /image, appearance) == 1`.
I have no clue internally why this is the case but it seems to be unique
to appearances, and so can be used to identify them from a previously
unknown var. You have to rule out that the thing you're checking is a
path, it would pass the check if the value were `/image` then, but this
is simple enough.

I hate having to know all this, so now you know this too.

:cl: ninjanomnom
admin: Appearance vars in VV now display instead of being left blank
/:cl:

* Fixes display of appearance type in VV

---------

Co-authored-by: Emmett Gaines <ninjanomnom@gmail.com>

---
## [ariever/Shiptest](https://github.com/ariever/Shiptest)@[f07cb3bd3b...](https://github.com/ariever/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Monday 2023-10-30 21:13:17 by Bjarl

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[6d51cb8174...](https://github.com/Buildstarted/linksfordevs/commit/6d51cb8174394d6155113cd61a72d3be0c556d80)
#### Monday 2023-10-30 21:16:08 by Ben Dornis

Updating: 10/30/2023 9:00:00 PM

 1. Added: eval should not be a built-in function
    (https://nickdrozd.github.io/2023/10/27/python-eval.html)
 2. Added: For Maximum Accessibility, Be Careful About Using a .dev Domain
    (https://macarthur.me/posts/dot-dev-problems)
 3. Added: Self-hosted analytics: How to track 53% more views
    (https://cretezy.com/2023/self-hosted-analytics)
 4. Added: Mean vs. median
    (https://jensrantil.github.io/posts/mean-vs-median/)
 5. Added: Why designers design forms
    (https://grillopress.github.io/2023/10/27/why-we-design-forms.html)
 6. Added: 🥦 The Curse of Healthiness | vincelwt.com
    (https://vincelwt.com/healthy)
 7. Added: I'm a hacker, but it's not what you think
    (https://www.biccs.tech/posts/being-a-hacker-is-not-what-you-think)
 8. Added: Daylight confusion week - Tyler Cipriani
    (https://tylercipriani.com/blog/2023/10/29/daylight-confusion-time/)
 9. Added: How to sell your micro startup as a solopreneur
    (https://marclou.beehiiv.com/p/how-to-sell-your-micro-startup)
10. Added: Gregory Szorc's Digital Home | My User Experience Porting Off setup.py
    (https://gregoryszorc.com/blog/2023/10/30/my-user-experience-porting-off-setup.py/)
11. Added: Checking References
    (https://www.kevinfox.dev/checking-references.html)
12. Added: Microretros
    (https://jensrantil.github.io/posts/microretros/)
13. Added: Deploying Rails on a single server with Kamal
    (https://nts.strzibny.name/deploying-rails-single-server-kamal/)
14. Added: You're Gonna Need A Bigger Browser
    (https://berjon.com/bigger-browser/)
15. Added: My Data-Backed Battle and Defeat of Hypertension
    (https://dennisforbes.ca/articles/treating_high_blood_pressure.html)
16. Added: Why I Am a Pluralist
    (https://www.radicalxchange.org/media/blog/why-i-am-a-pluralist/)
17. Added: not easy
    (https://meskhetian.com/not-easy/)
18. Added: On .NET Live - Scheduling background jobs with .NET
    (https://youtube.com/watch?v=7M0lDPCeM10)
19. Added: Everything wrong with tech in 2023 (in no particular order) — Joan Westenberg
    (https://joanwestenberg.com/blog/everything-wrong-with-tech-in-2023-in-no-particular-order)
20. Added: The Church of AGI
    (https://blog.piekniewski.info/2023/10/21/the-church-of-agi/)
21. Added: Wolverine and Serverless
    (https://jeremydmiller.com/2023/10/30/wolverine-and-serverless/)

Generation took: 00:15:54.3644083
 Maintenance update - cleaning up homepage and feed

---
## [JarRaid/HorrorGame](https://github.com/JarRaid/HorrorGame)@[227bec7b9d...](https://github.com/JarRaid/HorrorGame/commit/227bec7b9d91f1256063442bbff6d438a2877c60)
#### Monday 2023-10-30 21:21:53 by salataa1

Chandelier and window 4 update

Added other andrew's shitty ass chandelier that i had to basically redo the unwrap for. made it as pretty as I could. If he submits one in his push for the merge, use this one instead. also changed the alpha map on the top down view of the church window to reflect the nursery location we're going with

---
## [RealistikOsu/USSR](https://github.com/RealistikOsu/USSR)@[dfab799c85...](https://github.com/RealistikOsu/USSR/commit/dfab799c8504b65441a41540dc46ad4cb883eac8)
#### Monday 2023-10-30 22:22:31 by Skylar

promotion pls :pleading_face: :trollface: (#55)

* promotion pls :pleading_face: :trollface:

* fuck you realistic dash :trollface:

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[1e890af39d...](https://github.com/mullenpaul/cmss13/commit/1e890af39d7c4b6233439fbaa8693a3918e35f5c)
#### Monday 2023-10-30 22:33:25 by Steelpoint

Revolver Heavy Ammo Effect Change (#4706)

# About the pull request

This PR changes heavy ammo for the Revolver to knockback a mob and slow
them down instead of stunning it.

# Explain why it's good for the game

Combat balance is a precarious and often difficult conversation to hold,
ergo I'll lay my biases out on the table at first. I'm a marine main at
heart, but I have played a lot of xeno recently to gain a better
understanding of their side of the story, enough that I feel confident
to make these assertions.

My belief is that the heavy ammo of the revolver is a negative concept
for the game, and it needs to be removed, due to its stun factor.

The issue here is readability and prediction. When you see a RPG, you
know that it can fire a devastating warhead that can stun and kill T3s.
When you see a Warrior, you know it can leap to 4 tiles to stun and drag
a Human, when you hear a CAS strike you know exactly what is about to
drop. When you see a Queen you know she can stun screech and neuro stun
you.

But the issue with the Revolver is it has no obvious tell. It is a small
item, that can be fit inside backpacks, holsters, pouches, belts, armour
slots. It has no obvious advance warning when you are going to fire it.
There is no special uniform requirement making a revolver user standout
amongst the crowd. There is no tell.

The problem with the stun revolver is simply that is is a hard counter
to all T1s and most T2s. Its ability to stun allows it to perform an
attack that is uncounterable to a xeno as a xeno has no way to predict
who may be carrying one. A xeno can tell who a Specialist is, a xeno can
tell who has a shotgun or flamer or sniper or RPG, you can tell when a
mortar is being prepared, or a CAS strike or even an OB. You can see the
smartgunner. Even the Scout, a literal cloaked Marine, has to uncloak to
fire. You can not tell who has a revolver until they pull it out and
stun you. Once you are stunned you die.

A xeno equilivant would be if any Xeno could be carrying a special tool
that lets them grab a marine from 7 tiles away and pull them in plus
stun them for 2 seconds. But any xenomorph could be using it, including
a Lesser Drone.

Perhaps the heavy revolver could be reworked to do something else, but
ultimately the only reason anyone takes this ammo is for the stun.
Anything else is beating around the bush.

Those are my reasoning's, I'll leave the rest to the powers' that be. 

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Revolver Heavy ammo no longer stuns targets it strikes, it will
instead knock them back and slow them down for a short time.
/:cl:

---------

Co-authored-by: Steelpoint <alexander.henley@hotmai.com>

---
## [JustDownloadin/WideRising](https://github.com/JustDownloadin/WideRising)@[ae46fe6ed8...](https://github.com/JustDownloadin/WideRising/commit/ae46fe6ed8fea772dc8aee0c640b4f54c56d8ab2)
#### Monday 2023-10-30 22:45:22 by JustDownloadin

Update WideRisingStyle.user.css

Lots of stuff going on:

-Reorganized the document to make it easier to navigate. Makes working on it easier, and lets the user see the code more clearly in case they want to tweak something manually beyond the options already given by the userstyle.

-Fixed the Forums page, now it should adjust according to the width chosen by the user just like the rest of the site.

-Added the affectionately called "Silly Mode": a small collection of additional features made just for fun. As of now, Silly Mode does the following: 1) Replaces the adblock warning image ("Flight Rising relies on adverts to run, etc etc...") with pure CSS text for the sake of aesthetics, since the original image is very low-res and hard to read. 2) Hides a random separator image in the Nesting Grounds that's ugly as hell and I don't even know why it was there in the first place ??. 3) Adds a top margin to the new hatchling screen in the Nesting Grounds to let the UI breathe a little, especially when widening the layout.
There's an extra feature that was originally meant for Silly Mode but I decided to make a separate style for in case people find it helpful and don't want any of the other stuff. It shows what materials get turned into what at Baldwin's Bubbling Brew, and you can download it here: https://github.com/JustDownloadin/BaldwinMatsHelper  . I may include it in Wide Rising in the future though, we'll see. Most of the code is already done, it'd just be a matter of how to integrate the options themselves to this style (if they should be any different at all to begin with).

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[3b38037121...](https://github.com/Bubberstation/Bubberstation/commit/3b38037121f5d3459209877e9b43246fcf987b69)
#### Monday 2023-10-30 22:48:46 by BurgerLUA

[Testmerge Ready] Adds the RB-MK2 Reactor, Makes Tritium buyable from Cargo (#598)

## About The Pull Request


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/5985d911-ece0-42b9-b73a-08976488a2af)

This PR adds tritium based nuclear combustion reactors that converts
tritium into power. The reactor itself is only 1 tile in size and you
are expected to build multiple reactors in order to get a good source of
power going. It is currently obtainable by research, and the rods and
machine itself can be printed at the engineering protolathe, It can be
upgraded via stock parts for crazy power generation.

More tritium in a rod means less time to manage it, but it also means
that the rod's pressure can possibly get too high. There is nothing
stopping you from filling it up with other gases to moderate it, such as
freon if you're brave.

The RB-MK2 engine requires a source of cooling, but not too much
cooling, in order to produce a good amount of power. There is a safety
feature to prevent it from running too hot or too overpressured, but
that can be disabled by cutting the safety wire. There are also several
wires to allow for signal based management if you feel so inclined to
add such a thing to the setup.

### Current wire setup:

| Wire | Pulse | Cut | Mend  |
| --- | --- | --- | --- |
| Overclock | Enables/Disables overclocking | Nothing | Disables
overclocking |
| Activate | Toggles the reactor on/off | Turns reactor off | Turn
reactor on |
| Disable | Turns reactor off | Nothing | Turns reactor off |
| Throw | Ejects the rod, if off | Nothing | Ejects the rod, if off |
| Lockdown | Toggles vents open/closed | Nothing | Turns vents off |
| Safety | Toggles safety on/off | Turns safety off | Turns safety on |
| Limit | Increases the cooling limit percent by 5% | Nothing | Resets
the cooling limit to 0%

### How to Operate

1. Construct the RB-MK2 on a powergrid inside a room with cooling.
1. Fill an RB-MK2 rod with 50 moles of room temperature tritium.
2. Insert the rod into the RB-MK2
3. Wrench the RB-MK2 to turn it on.
4. Let the RB-MK2 run hot, but not too hot to the point where the RB-MK2
rod bursts.
5. If it jams, use a crowbar on it. Or a plunger.
6. If it is too damaged, use a welder on it.
7. ????
8. Profit.

### Tips
- To turn the machine on, insert a rod filled with tritium in the hole
and then wrench it. If you don't have a wrench, you can pulse the
activate wire while the rod is in.
- Rods should be filled up with at most 50 moles of tritium, but more
can be added if you're feeling dangerous.
- You can put other gasses inside a rod if you want said gasses to leak
out during processing.
- The RB-MK2 can be upgraded. Matter bins increase the internal buffer's
volume, servos increase the pressure at which the fans will release gas,
and capacitors will increase the power output of the reactor (this can
result in higher temperature gains) per mole of tritium.
- Overlocking increases tritium consume and gives off more heat, but
provides more power.
- To activate the machine, use a wrench on it. It is considered active
when the rod is all the way down.
- An exposed rod (inactivated machine) is more affected by external
temperatures than an inactive rod. This can sometimes be worse than it
being unexposed if the exterior turf temperature is too hot.
- The machine will only process tritium (and generate power) wile
active.
- Opening the vents (aka disabling lockdown) allows processed gas to
escape out of the buffer and allow exterior temperature to influence the
internal rod temperature.
- Closing the vents will prevent exterior temperature from affecting the
rod, and prevent waste gas from escaping. This is useful for if you want
to increase the temperature by closing the vent or in cases of a chamber
fire.
- Throwing the rod, or removing it manually, prevents the rod from
taking on any more heat/cooling. This does not stop internal reactions,
if there are any inside the rod.
- Increasing the cooling limit will reduce the cooling effect external
air has on the rod. This is useful to increase if your cooling setup
makes the rod too cold to process power effectively.
- There is a safety feature on the machine where if the rod gets too hot
or too overpressured, it will automatically turn off and expose itself
to external air. Disabling safeties is only useful if you want the
machine to blow up, or if you don't want the rod to automatically expose
itself (in case of a chamber fire).
- Goes good with radiation shielding as tritium is a byproduct of
radiation shielding, and radiation shielding requires a lot of power to
function.



## TODO

- [x] Actually make sure it works (it doesn't).
- [x] ~~Introduce liquid reagent cooling mechanics where water puddles
can help with cooling management.~~ Not possible because liquid reagents
are shit.
- [ ] Balance it so it isn't more of a pain in the ass to manage than a
supermatter.
- [x] Maybe add safety features like temperature monitoring and other
stuff so engineers aren't 100% blind.
- [x] Replace Burgerstation default Supermatter setup with this one.
- [x] Testmerge!
- [x] Get feedback from engineer mains.

## Why It's Good For The Game

More sources of funny power is good.

## Changelog

:cl: BurgerBB
add: Adds the RB-MK2 reactor.
add: Makes Tritium buyable from cargo.
/:cl:

---------

Co-authored-by: StrangeWeirdKitten <95130227+StrangeWeirdKitten@users.noreply.github.com>

---
## [vindalyn/2000s_website](https://github.com/vindalyn/2000s_website)@[71f5ef6440...](https://github.com/vindalyn/2000s_website/commit/71f5ef6440b30bbd28b63509eea28363b3b6b0ae)
#### Monday 2023-10-30 23:37:00 by Vindalyn

i hate myself. -> generalized svelte code, wasted ten hours of my life, realized that something is wrong with either window or column, couldn't find the issue, gave up, decided to do variable length paddings. i hate myself.

---

