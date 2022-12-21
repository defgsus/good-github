## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-20](docs/good-messages/2022/2022-12-20.md)


2,163,197 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,163,197 were push events containing 3,186,325 commit messages that amount to 259,196,702 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [apollographql/apollo-server](https://github.com/apollographql/apollo-server)@[32cca948be...](https://github.com/apollographql/apollo-server/commit/32cca948be82764e9d076be171b5c1657d412899)
#### Tuesday 2022-12-20 00:00:42 by Trevor Scheer

Update CS:CI config (#7254)

CS:CI has reported that node 18 is now supported, meaning we should be
able to simplify some config and remove a workaround.

Also add missing packages to the ci.json.

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[32a86ad184...](https://github.com/TaleStation/TaleStation/commit/32a86ad18489a5ed8eaa2d5ccea51d4c004dd89e)
#### Tuesday 2022-12-20 00:02:22 by TaleStationBot

[MIRROR] [MDB IGNORE] Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins (#3723)

* Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins (#71989)

This one is fun.

On every /turf/Initialize and /atom/Initialize, we try to set
`smoothing_groups` and `canSmoothWith` to a cached list of bitfields. At
the type level, these are specified as lists of IDs, which are then
`Join`ed in Initialize, and retrieved from the cache (or built from
there).

The problem is that the cache only misses about 60 times, but the cache
hits more than a hundred thousand times. This means we eat the cost of
`Join` (which is very very slow, because strings + BYOND), as well as
the preliminary `length` checks, for every single atom.

Furthermore, as you might remember, if you have any list variable set on
a type, it'll create a hidden `(init)` proc to create the list. On
turfs, that costs us about 60ms.

This PR does a cool trick where we can completely eliminate the `Join`
*and* the lists at the cost of a little more work when building the
cache.

The trick is that we replace the current type definitions with this:

```patch
- smoothing_groups = list(SMOOTH_GROUP_TURF_OPEN, SMOOTH_GROUP_FLOOR_ASH)
- canSmoothWith = list(SMOOTH_GROUP_FLOOR_ASH, SMOOTH_GROUP_CLOSED_TURFS)
+ smoothing_groups = SMOOTH_GROUP_TURF_OPEN + SMOOTH_GROUP_FLOOR_ASH
+ canSmoothWith = SMOOTH_GROUP_FLOOR_ASH + SMOOTH_GROUP_CLOSED_TURFS
```

These defines, instead of being numbers, are now segments of a string,
delimited by commas.

For instance, if ASH used to be 13, and CLOSED_TURFS used to be 37, this
used to equal `list(13, 37)`. Now, it equals `"13,37,"`.

Then, when the cache misses, we take that string, and treat it as part
of a JSON list, and decode it from there. Meaning:

```java
// Starting value
"13,37,"

// We have a trailing comma, so add a dummy value
"13,37,0"

// Make it an array
"[13,37,0]"

// Decode
list(13, 37, 0)

// Chop off the dummy value
list(13, 37) // Done!
```

This on its own eliminates 265ms *without space ruins*, with the
combined savings of turf/Initialize, atom/Initialize, and the hidden
(init) procs that no longer exist.

Furthermore, there's some other fun stuff we gain from this approach
emergently.

We previously had a difference between `S_TURF` and `S_OBJ`. The idea is
that if you have any smoothing groups with `S_OBJ`, then you will gain
the `SMOOTH_OBJ` bitflag (though note to self, I need to check that the
cost of adding this is actually worth it). This is achieved by the fact
that `S_OBJ` simply takes the last turf, and adds onto that, meaning
that if the biggest value in the sorting groups is greater than that,
then we know we're going to be smoothing to objects.

This new method provides a limitation here. BYOND has no way of
converting a number to a string at compile time, meaning that we can't
evaluate `MAX_S_TURF + offset` into a string. Instead, in order to
preserve the nice UX, `S_OBJ` now instead opts to make the numbers
negative. This means that what used to be something like:

```dm
smoothing_groups = list(SMOOTH_GROUP_ALIEN_RESIN, SMOOTH_GROUP_ALIEN_WEEDS)
```

...which may have been represented as

```dm
smoothing_groups = list(15, MAX_S_TURF + 3)
```

...will now become, at compile time:

```dm
smoothing_groups = "15,-3,"
```

Except! Because we guarantee smoothing groups are sorted through unit
testing, this is actually going to look like:

```dm
smoothing_groups = "-3,15,"
```

Meaning that we can now check if we're smoothing with objects just by
checking if `smoothing_groups[1] == "-"`, as that's the only way that is
possible. Neat!

Furthermore, though much simpler, what used to be `if
(length(smoothing_groups))` (and canSmoothWith) on every single
atom/Initialize and turf/Initialize can now be `if (smoothing_groups)`,
since empty strings are falsy. `length` is about 15% slower than doing
nothing, so in procs as hot as this, this gives some nice gains just on
its own.

For developers, very little changes. Instead of using `list`, you now
use `+`. The order might change, as `S_OBJ` now needs to come first, but
unit tests will catch you if you mess up. Also, you will notice that all
`S_OBJ` have been increased by one. This is because we used to have
`S_TURF(0)` and `S_OBJ(0)`, but with this new trick, -0 == 0, and so
they conflicted and needed to be changed.

* Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins

* fixes

* oops

* i hate this entire module

* what if i just kill you how about that

* uh

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[da65cf0c23...](https://github.com/TaleStation/TaleStation/commit/da65cf0c23f052e291eb3aaafb564e7e6decf8f8)
#### Tuesday 2022-12-20 00:02:28 by TaleStationBot

[MIRROR] [MDB IGNORE] refreshes syndi-kits and syndicate surplus crates, introduces shared limited stock (#3737)

* refreshes syndi-kits and syndicate surplus crates, introduces shared limited stock (#71869)

## About The Pull Request

After all, the Syndicate loves a good throwback.


![C6O47fPhAB](https://user-images.githubusercontent.com/116288367/207737104-3d24574f-02e0-433d-8ea7-6825ca4cb970.png)

This PR does a few things with the goal of reimplementing and
revitalizing syndicate traitor kits and the syndicate surplus crate.
Of note is that I have added in a way for limited stock items to share
their limited stock.

Following maintainer guidance the syndicate traitor kits have increased
in price and as a result some of the lower value ones have been
adjusted. I've given all active bundles current TC costs per item
knowing full well they will be inaccurate eventually.

<details>
  <summary>Changes as a result of my audit of syndikits</summary>
    
### UNCHANGED
Recon, Spai, Stealthy, Screwed, Sniper, Nukie Meta, Implants
Mad Scientist, Bees

Lord Singuloth is also unchanged and disabled, I think that it should
turn into a new supermatter themed kit maybe. outside of current scope.

### Gun Kit
Replaced emag with doorjack and gave it a chameleon holster, literally
moved 1 tc elsewhere

### Murderer
replaced emag again, no additions its a lot of tc and Just Good

### Hacker
added doorjack, otherwise unchanged

### Sabotage
no changes other than adding in extra bombs it didnt have

### James Bond
gave him some gadgets with the freedom implant, emp flashlight, and one
x4. also a cyanide pill and deck of cards for fun

### Ninja
Added in miner Jump Boots, smoke spell, and doorjack. dont just want it
to be space ninja

### Dark Lord
Added in new lightning bolt spell granter and made the desword default
to red. probably overbudget.

### White Whale
dehydrated carp added so you can ride it alongside the ones you grenade
out. hard to imagine changing this

### Mr Freeze
changed temperature gun to be cryo only so that i could give him the
cryo thermal pistol. cold attacks only.

### 2006 Traitor
doorjack.

</details> 

tl;dr theyre all about 30 tc worth of shit more or less some are more
but thats what rarity should be for
you can only buy from one type of syndicrate per round


![QOF1WO7CC6](https://user-images.githubusercontent.com/116288367/207739417-00ae6b81-b6aa-4774-a4bb-f2d880988ff4.gif)

Next up is the return of the surplus crate. 
Crate is generated, gives you gear **based on your progression at the
time of buying the crate**, you can use it all at the start and get some
chameleon kits and not a lot of dangerous weapons or wait till later.
I've changed the weight on some items here and there and given weight to
role and species locked items, though I will admit that latter is
unimportant because I set moth lanterns to be unable to appear in these
two crates.


![dreamseeker_t8abXysKqK](https://user-images.githubusercontent.com/116288367/206761978-96e2a51e-f9a5-48e4-a863-a9198fa15ea2.gif)

But who cares about that your eyes instantly went to the United Surplus
Crate and the United Surplus Key lets be honest.

The united surplus crate is 80 TC worth of uplink items relative to your
current progression when you purchase it and gives you a locked box. It
**will explode if you try to break it** so be careful with it. It gives
you 80 TC and costs 20 TC because it is impossible to open without key.
The rub of course is that the Syndicate forbids agents from buying more
than one surplus item of any kind, you need to find another traitor and
make them buy you a key to open your box. Or I guess you can share the
box?


![dreamseeker_ts0AZeiyfy](https://user-images.githubusercontent.com/116288367/207740388-3f688bba-5d71-48d2-8079-671bbed7e54e.gif)

Regardless, if the crate is opened with any other means it doesn't spawn
its contents, you need 2 traitor uplinks.
Both of these items have a 30 minute timer because you don't want a
crate that has 5 emp flashlights in it. You at least want one energy
sword.

I did a lot of code shit and changed various things to be proc based to
allow for more editing and interjection of things, as I wrote in code
comments making a crate thats locked to a specific set of progression
just means changing the proc that generates a list of valid uplink items
to check items' progression values to a specified value instead of your
characters progression.

Ok I think that goes over everything more or less????

## Why It's Good For The Game

I've heard that people liked these and I think they are quite fun, being
able to go from "i dunno what to do as a traitor" to "ah, of course, I
will become the Bombler" is a fun thing to be able to have, and people
like to get a bunch of random shit in the mail. Some of it even feels
free!!!!!!!!!!!!!!!!!!! Brain points go up!!!

The division of procs allows for more creativity with this system than
existed before as well as other possibilities for interacting with the
uplink handler in funny ways.

## Changelog

:cl:
add: the syndicate is once again distributing syndi-kits, some now with
new technology
add: a fresh batch of syndicate surplus crates have been sent out,
though they seem a bit lighter than before
add: in an effort to encourage cooperation, a traitor can now purchase
either the new United Surplus Syndicate Crate or its key, but not both
add: lightning bolt book granter for wizard event and one syndie-kit
bundle
add: temperature gun that only makes things colder for one syndie-kit
bundle
code: it is now possible to have uplink items share limited stock
bal: role-restricted items no longer can be delivered by the stray
syndicate drop pod event
/:cl:

* refreshes syndi-kits and syndicate surplus crates, introduces shared limited stock

* slowly converting back to tg

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[4cce4bcf10...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/4cce4bcf10aabec33f0652b07034bfe71bfca66a)
#### Tuesday 2022-12-20 00:18:55 by SkyratBot

[MIRROR] Minor plane cube cleanup [MDB IGNORE] (#18223)

* Minor plane cube cleanup (#72038)

## About The Pull Request

[Fixes area lighting not working on turf change in multiz
cases](https://github.com/tgstation/tgstation/commit/7b92deffbca92a834cb0a361fd685de51a12ea53)

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part.
Stupid shit resolved

[Fixes some uses of plane masters that only specified one rather then
all](https://github.com/tgstation/tgstation/commit/a59ec96d29710b967bf8b3ffe8210b230cb194b3)

We almost never only want to show SOME hidden planes.
Should really make a helper for this someday

* Minor plane cube cleanup

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [SecurityLab-CodeAnalysis/tgstation_tgstation](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation)@[44008f485d...](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation/commit/44008f485d6d72537935cfa8a3a5b6140eece744)
#### Tuesday 2022-12-20 00:25:16 by Jacquerel

Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

---
## [Ziemas/pcsx2](https://github.com/Ziemas/pcsx2)@[87abacc632...](https://github.com/Ziemas/pcsx2/commit/87abacc63264f9cf554cddf02973e0fc9cd2af77)
#### Tuesday 2022-12-20 01:05:43 by RedDevilus

GameDB: Fix multiple games + maintenance

- Area 51: Half Pixel Normal vertex for lighting and other places
- Shrek 2: Basic mipmapping which kinda half fixes the sun missing
- Galaxy Angel II: Normal vertex which reduces misalignment
- Forgotten Realms - Demon Stone: Clamping Mode extra + preserve which will solve the occasional SPS + missing demo entry.
- Spyro Dawn of dragon: SW clut + sprite which doesn't make you vomit from the overbloomification and looks similar to the software renderer
- Castlevania Curse of darkness half sprite which will enlarge the font similar to software renderer + some missing fixes that were available on the Europe and America versions but not Japanese.
- Drakengard 1 + 2 (Also know as Drag-on Dragoon) : Partial (no hashcache) to avoid slow transitions and other areas. Adds missing Japanese Drakengard 1
- Urban reign: Partial texture preloading to fix performance issues in the gameplay
- Onimusha Warlord: Partial preloading to fix performance issues
- Sniper Elite: Fix sky lighting
- Maintenance that add spaces in the titles for Disc1of1 to Disc 1 of 1 and more...

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[590847bdf7...](https://github.com/Wallemations/heavenstation/commit/590847bdf742b1e53f05ea700d48ec0676cdcf43)
#### Tuesday 2022-12-20 01:10:29 by Andrew

Biogenerator tweaks, leather makes more belts and clothing (#71175)

## About The Pull Request

### Revamped the biogenerator UI:


https://user-images.githubusercontent.com/3625094/200973283-b703f21b-c747-493e-98d9-043eef86d410.mp4

### Changed biogenerator icon to use layers and see the biomass level:


https://user-images.githubusercontent.com/3625094/201396065-caeaa412-6676-46f6-875e-efa2dca34985.mp4

### Biogenerator rebalance:

- Now you don't need the beaker to print solid products.
- Biogenerator now accepts all food, not just plants.
- Biogenerator now treats all nutriment subtypes as nutriments, so
vitamins and proteins also turn into biomass.
- Biomass now has the same units as other reagents (you get 5 biomass
from 5 nutrient with tier 1 parts).
- Doubled the cost of all items and reagents. (biomass generation
reduced by 10 and prices - by 5)
- Chemicals output amounts are now in units and you can select how much
you want to output exactly. It will not let you specify more than the
size of container or above 50 units with one button click.
- Reduced the amount of stored items and introduced a limit to the
biomass, both tied to the matter bin tier.

### Recipes changes:

Made biogenerator more dumb by moving the clothing out from the
biogenerator designs, and extending leather recipes instead.

The biogenerator is a grinder/recycler style machine so it doesn't make
sense that it outputs clothing.
Also you need to make leather to craft the toolbelt, while you can't do
the same to craft job-specific belts.
Now you can print leather in biogenerator and craft the leather clothing
by using the leather in-hand.
And the rice hat is now crafted from bamboo, instead of biogenerator.

Also added paper to the biogenerator recipes as it makes stuff from
cellulose and barely anyone knows that you can craft paper from 1 log
and 50 water. And paper is needed in large quantities to craft some
items, like paper frames.

And it doesn't output a pack of rolling paper. It's dumb now. It prints
the rolling paper sheets instead.

## Why It's Good For The Game

Biogenerator had terrible UX and backend logic. I didn't improve much on
BE though, but now it should be less frustrating to use.

Also I hate how biogenerator is superior to all other means of obtaining
its products. It doesn't make sense to grow and grind wheat, for
instance, when you can just throw shit into biogenerator and get the
flour fast. And the costs are ridiculous - you can get a couple of
bottles of fertilizers just from one medium potato.

It honestly begs for more nerfing, at least to make the nutriment -
chemicals exchange rate 1:1.

The reason for the biomass cap is because people use it as a sink for
veggies and generate infinite biomass. Maybe the limit will make them
care more about the part upgrade and offload some of the veggies to the
fridge for the Cook.

Also it was weird that biogenerator could tailor some things, while
others have to be crafted in-hand. Now you can print leather and craft
all types of belts and leather clothing.

## Changelog
:cl:
refactor: biogenerator UI revamped
qol: biogenerator no longer requires beaker for materials, monkey cubes
and nori
balance: biogenerator accepts all food, not just plants
balance: biogenerator treats all nutriment subtypes as nutriments
(vitamins, protein, etc.)
balance: biogenerator product prices doubled
balance: biogenerator biomass storage is limited depending on the level
of matter bins
balance: cowboy boots recipe moved from crafting to leather recipes
balance: leather clothing & belt recipes moved from biogenerator to
leather recipes
balance: rice hat recipe moved from biogenerator to bamboo recipes
balance: biogenerator now outputs rolling paper sheets instead of a pack
add: biogenerator can now print paper
imageadd: biogenerator icons now use overlays, have emissive layer and
indicate the biomass volume
/:cl:

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[1a226283e5...](https://github.com/ThePiachu/cmss13/commit/1a226283e5c108dffcb74746af5d36ba29d51058)
#### Tuesday 2022-12-20 01:34:22 by Diegoflores31

vamp lurker strain (#955)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds a new strain for lurker (vampire is the name for now but i can be
changed i just lack the creativity) has less health than the average
lurker but its faster and slashes faster but deals less damage .

**### BASE STATS**
health : 390
armor : 20 
slash damage : 35
speed : 0.1 faster than base lurker // for reference cloaked speed is
0.2
slash speed : 2


Vamp lurker cannot cloak but has a larger kit of abilities focused on
dealing damage and healing making it a high risk high reward backliner
with skill based abilities rather than just stun.
### **Abilities :**

**Rush:** 
Shorter version of pounce (4 tiles) instead of stunning it will daze and
slightly screenshake the target .
damage : 30
cooldown : 6 seconds and 3 if you land it.

**Flurry:**
AOE attack that deals damage to the targets in front of you in a 1x3
area . if landed it will heal you by the same amount and apply a small
slow for the user ( very short second slow)
damage: 30
heal : 30
cooldown : 3 seconds if missed 

**Tail Jab:**
Targeted attack will deal a small amount of damage to the target and
knock him away from you . if you use it on a target in critical state it
will execute it healing you a LOT.
damage : 30
Execution damage : 80 with penetration
cooldown : 7 seconds 
heal : 150
critical state : this occurs when the target either paincrits or falls
INCONCIOUS

## Why It's Good For The Game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->
Lurker lacks strains and i looked up in the Trello that Lurker strain
was required . i tried to follow the indicators but kinda ended up with
something else i guess but i really like how it ended so i am making
this PR to see what you think about it.


## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: diegoflores31
add: Added a new strain for lurker "Vampire".
add: Vampire Lurker exchanges all of your abilities for a fast paced
combat style more focused into dealing damage and
mobility.
add: Active 1 : Rush . Pounces for a maximun of 4 tiles and slashes the
objetive once on impact . applying a screenshake and daze to the target
. Landing this ability reduces the cooldown by half. (cooldown 6
seconds)
add: Active 2 . Flurry : unleashes a 1X3 slash at the targeted direction
that slows your enemies on impact healing you by 30 hp . (cooldown 3
seconds)
add: Active 3 : Tail Jab : Attacks your enemies from a maximun of 2
tiles away while dealing a small amount of damage ( 20) and knocking
them down . if you attack a enemy that is on critical state it will deal
80 damage with penetration and heal you by 150 hp. (cooldown 7 seconds)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Shad0vvs <rtwdevelopment@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[bba6239bc1...](https://github.com/ThePiachu/cmss13/commit/bba6239bc19510ecd235acc31ec75783751f9bcc)
#### Tuesday 2022-12-20 01:34:22 by Stan_Albatross

sniper sentries rebalance (#1951)

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

halves sniper sentry range reduces accuracy a bit ups firerate 

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

being shot at from far offscreen is awful, this should make sniper
sentry a bit more of a threat when it does come into play while not
being able to hit you from half the map away

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
balance: halved the sniper sentry's range to 10 tiles
balance: reduced the sniper sentry's accuracy by 20%
balance: reduced the sniper sentry's delay between shots from 2s to
1.25s
balance: reduced the plasma sentry's range to 10 tiles
balance: reduced the plasma sentry's delay between shots from 10s to 7s
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [EdwardNashton/mojave-sun-13](https://github.com/EdwardNashton/mojave-sun-13)@[fe5d6c7b56...](https://github.com/EdwardNashton/mojave-sun-13/commit/fe5d6c7b568d550f403eb892ed47ffaf6b4fd28c)
#### Tuesday 2022-12-20 01:35:36 by Technobug14

Agriculture (#2230)

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

---
## [acarrasco/advent_of_code](https://github.com/acarrasco/advent_of_code)@[c627733e1a...](https://github.com/acarrasco/advent_of_code/commit/c627733e1a23022ca551e48fb09291c322129774)
#### Tuesday 2022-12-20 01:57:28 by Alejandro Carrasco

Year 2022 - day 19

This was a tough cookie! When I read it in the morning I felt absolutely
discouraged, since I had been having trouble with the previous days...

But after the whole day minding my own business I got back home and
decided to give it a go. The first part wasn't that difficult, it was
just a matter of doing an exhaustive exploration of all the options with
some caching.

For the second part that didn't work. I was already in bed when I realized
that given that the factory can only produce one robot at a time, there
is no point in having more robots than what are actually needed to
produce the requirements to build one geode cracking robot per turn.

With that and a more efficient state representation (tuples instead of
dicts) the search could finish in a few minutes.

An extra optimization that I was considering was to group equivalent
states ignoring the amount of geodes and geode-cracking robots, but it
wasn't needed in the end.

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[29d766e25f...](https://github.com/Ryll-Ryll/tgstation/commit/29d766e25f18c5030972562ed649832077cdfc95)
#### Tuesday 2022-12-20 02:19:48 by LemonInTheDark

Fixes attempting to offset floating planes (#71490)

## About The Pull Request

This is a dumb idea, and leads to fucked rendering on occasion

## Why It's Good For The Game

Fixes another portion of #70258, a player will no longer have a hidden
antag hud if they move down a z level after getting an antag. We were
trying to offset the floating plane of their image, and it went to shit.
Also fixes a bug with observers not having antag huds for the combo hud
to see. We were only giving them one on mind.on_transfer, rather then on
mind assignment. I hate mindcode

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[a753229ee2...](https://github.com/LemonInTheDark/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Tuesday 2022-12-20 03:38:56 by GoldenAlpharex

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
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[35b5ac0c4e...](https://github.com/LemonInTheDark/tgstation/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Tuesday 2022-12-20 03:38:56 by Fikou

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
## [space-wizards/space-station-14](https://github.com/space-wizards/space-station-14)@[168bad2ef2...](https://github.com/space-wizards/space-station-14/commit/168bad2ef25cc25c2cffea788f643425b858be6d)
#### Tuesday 2022-12-20 04:07:25 by Nemanja

multi-handed item component (#12523)

* multi-handed item component

* pretty fucking obvious missed portion of this

* holy shit was i on crack wtf was that code

* DEWIT RIGHT

---
## [softcerv/Skyrat-tg](https://github.com/softcerv/Skyrat-tg)@[1c76ea5334...](https://github.com/softcerv/Skyrat-tg/commit/1c76ea533439dcd7fca15a2dd500a44dc6158883)
#### Tuesday 2022-12-20 04:11:18 by SkyratBot

[MIRROR] Changes our map_format to SIDE_MAP [MDB IGNORE] (#18070)

* Changes our map_format to SIDE_MAP (#70162)

## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Changes our map_format to SIDE_MAP

* Modular!

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [BrynGhiffar/pj_projectservice](https://github.com/BrynGhiffar/pj_projectservice)@[8d0238c8ce...](https://github.com/BrynGhiffar/pj_projectservice/commit/8d0238c8cebbc07200e4ea98c63180b7302b7d54)
#### Tuesday 2022-12-20 05:17:01 by Bumskee

fixed the stupid ass bug it was all just because of cursor type object is messing with our fucking workflow

---
## [wahello/terminal](https://github.com/wahello/terminal)@[b4b6636b49...](https://github.com/wahello/terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Tuesday 2022-12-20 06:39:22 by Mårten Rånge

Relax shader strictness in RELEASE mode (#13998)

Disables strictness and warnings as errors for custom pixel shaders in
RELEASE. Windows terminal is not telling the user why the shader won't
compile which makes it very frustrating for the shader hacker.

After trying the recent preview none of my shaders loaded anymore in
Windows Terminal Preview which made me very sad. I had no idea what was
wrong with them. After cloning the git repo, building it, fighting an
issue that prevent DEBUG SDK from being used I finally was able to
identify some issues that were blocking my shaders.

> error X3556: integer modulus may be much slower, try using uints if possible.
> error X4000: use of potentially uninitialized variable (rayCylinder)

While the first one is a good warning I don't think it is an error and
the tools I use didn't flag it so was hard to know.

The second one I was staring at the code and was unable to identify what
exactly was causing the issues, I fumbled with the code a few times and
just felt the fun drain away.

IMHO: I want it to be fun to develop shaders for windows terminal.
Fighting invisible errors are not fun. I am not after building
production shaders for Windows Terminal, I want some cool effects. So
while I am as a .NET developer always runs with Warning as errors I
don't think it's the right option here. Especially since Windows
Terminal doesn't tell what is the problem.

However, I understand if the shaders you ship with Windows Terminal
should be free of errors and silly mistakes, so I kept the stricter
setting in DEBUG mode.

## Validation Steps Performed

Loaded Windows Terminal in RELEASE and DEBUG mode and validated that
RELEASE mode had reduced strictness but DEBUG retained the previous more
restrictive mode.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[d823151ada...](https://github.com/san7890/bruhstation/commit/d823151ada4bb9e0ccf65d6c448c5df78b28a3c7)
#### Tuesday 2022-12-20 07:05:12 by san7890

Guards against uplink failsafe code being the same as unlock code

There's probably a better way to do this to be honest, but I think it's silly for both to potentially be the same and this should work alright.

Traitor UI only shows Unlock/Failsafe Code if you have it

There are cases in which you don't have an unlock code (if the uplink is implanted in you from the start) and you obviously don't always start with with a failsafe code (need to buy it). So, let's only fill in this fields in the UI should they exist.

There might be something to be said about wanting to ensure that people remember that they can check this UI screen to find the failsafe code should they lose it later, and I wouldn't mind changing the string to be something like "Failsafe: None" in that case. However, I just thing something like:

```txt
Code:
Failsafe:
```

is silly.

---
## [Clumsy0420/Rise6Launcher](https://github.com/Clumsy0420/Rise6Launcher)@[4976804721...](https://github.com/Clumsy0420/Rise6Launcher/commit/497680472131129a7feaa82f04ed1eac12807bfd)
#### Tuesday 2022-12-20 07:45:02 by Clumsy0420

Revert "fuck you clusmy"

This reverts commit 2093f895742c352a3cb5f246c4c62d8e5b2e6662.

---
## [radnyi/My_new_projects_AI](https://github.com/radnyi/My_new_projects_AI)@[4544e695db...](https://github.com/radnyi/My_new_projects_AI/commit/4544e695dbb7a06df33bf994ee77b6cb0ca0c365)
#### Tuesday 2022-12-20 08:29:51 by radnyi

A

Final project for the Building AI course of Univerity of Helsinki

Summary
This AI project target is to be able to identify for each main cosmetic scent (such as rose, pine, mint...) several set of images that have together a high probability to conjure the main scent when you see one of these AI-sorted set of images in a picture on a web page.

In this AI project we would use only images to trigger scents. It would not use a scent-generating device. You can include the project in the general category of "Digital scent technology" but a very specific branch of this technology which tries to generate scents memories by using only images.

Background
The problem I want to solve is the problem of e-commerce selling products with high olfative charateristics and that do not have currently the way to convey these scents to their customers. I want to be able offer them a list of image proxy for each of the scents they need to convey.

By putting their product inside a composition with the adequate images set, they will be able to summon the right scent memory by trying to use the scent experiences printed in the customer brain and triggered by the set of image.

The categories of products that would benefit of a solution for this problem are : cosmetics, perfumes, cooked dishes, and in fact any product with a scent, or mix of scents, that need to be sold on a e-commerce web site.

How is it used?
One concrete example : I am selling on a e-commerce website a candle that smells like lemon and pine. How do I maximize the probability to summon the right lemon-pine scent memory when the customer is looking at the picture of my candle?

We could say "put a lemon and a pine" behind your candle on a picture with the three items combined but it is far from satisfying and experience tends to show that a picture with a lemon-pie summon better the memory of lemon scent than the picture of a lemon. So what do I do if I am a e-commerce marketer to promote my lemon and pine candle using images?

Therefore my AI solution would give you the capability to sort any bank of image into adequate subsets that are usually triggering the memory of a set of scents when you are looking at these subsets of images. For example if I have 10 main scents in my products and a bank of 1000 images, I would like to classify my bank in 10 lists, one for each scent. And each list would contain a number of set of images that have a high probability to trigger the scent I am trying to recall.

By using my sorted bank of images, a e-commerce professional would be able to market efficiently its beautifully smelling products on the web by putting them in a picture that usually can generate the right scent memories he wants to generate for each product.

The AI solution I will describe below could be used in theory on any available bank of images for any list of scents.

Data sources and AI methods
The global methodology I would use is a combination of brain imaging and deep learning.

The steps I am seeing are :

1/ COLLECT

one big bank of images containging simple items in each picture (i.e : a lemon, a pine, a rose, a daisy....)
one list of main scents that can be easily transported and stored
a brain imaging set (not so easy)
a group of people that are ready to participate to the classification process
2/ RECORD BRAIN IMAGES FOR A BANK OF PICTURES AND A DIVERSE GROUP OF PERSONS

you use the brain imagery to show the images (and any subset of images you have the time to show - for example you try all the pairs)
you store the brain image generated by each picture for each subject
3/ RECORD BRAIN IMAGES A FIRST IMAGE BANK TO A SET OF SCENTS

you then have each sujects smelling all the samples of scents that you want to classify
you store the brain image generated by each picture for each subject
4/ AI CLASSIFICATION

using AI methods you identify the brain images corresponding to pictures that match the best with brain images corresponding to scents
the available AI algorithms for comparing pair of images are very mature and you can use very simple algorithms such MSE in python or very complex ones combining deep learning approaches (CNN, Siamese networks, deep neural networks...)
you will never have perfect match but you will have probable matches because your are trying to trigger memories of odours using analogy in the brain with images you see
the quality of the classification will evidently depends of the numer of persons you are able to put through this brain image recording process
the efficiency of the classification will depend too of the content of your bank of image : maby your bank is not able at all to generate this right scent memory and your best match will be a very distant match with the brains area activated which are not the right ones whatever the picture you show to whatever the person in your group.
5/ GENERALISATION

when you have reached your first classified bank of image you can use it to classify a new bank of pictures using the same AI methods of image similarity without having to records any brain of any person : you are just trying to use a new picture (or a set of pictures) which have sufficient similarity with one set of your original bank in order to get a high probability of trigerring a particular scent memory to a maximum of potential customers.
Challenges
You need a lot of subjects to generate good results and you need brain imaging systems so the initial classification would be time-consuming and expansive. But my idea is to classify an "proto-bank" with brain imaging which would be used to classified other banks of pictures with only AI methods and therefore it will reduces the costs for a new bank of images that has not already been classified through brain imaging : you use only your proto-bank and the new bank.

But the main challenge I see is to find the right diverisity of people that will maximize your results. All this project is based upon the scientific knowledge that a specific image you are looking at it able to trigger the memory of a scent (similar to madeleine de Proust) and therefore you need the right memories in the brain of the persons that will volunteer for the recording. But to get the samed memories than the ones of your customers you need to compose thoroughly your sample of people : the same culture, the same background, similar experiences, etc... If you are using a sample of people that have never smelt a lemon you will get nothing whatever the pictures in your bank.

You can simplify this challenge by marketing : if your product is targeting one very specific segment of customers you will select your sample of people only inside this specific segment of customers and you will have higher probabilities of triggering the same scent memories by seing the same picture between a customer C and one person of your sample... But everything there is based upon similarities and not identities.

What next?
It seems that the main focus in 2021 is to try to generate scents by digital-devices and not by pictures therefore my project would not get the most help firstly but I think that it will come because as a customer I prefer something very simple such as the right set of pictures than putting an electrod in my nose to get the actual scent of having a sample of scents to use in my own room.

Maybe we could find a bank of images already classified into "the-right-picture-for-the right-scent" through brain imaging and then the project would easily kickstart because it would only be a python project having an input unclassified bank of pictures and an output classified bank of pictures thanks to comparison with your proto-bank.

Acknowledgments
I want to thank my loved wife who is the creator of an e-commerce company creating and selling natural cosmetics and has forever be faced with this business problem of triggering scents without any scent on its website. Thank you my Dear for having given me this business problem. I dot not have the applied AI solution but I know that it will exist someday because it is not so difficult using the above technics, it requires just time and money :-)

---
## [saravanakumar-2003/Saravana-Kumar-C-practice](https://github.com/saravanakumar-2003/Saravana-Kumar-C-practice)@[2fbe2982f5...](https://github.com/saravanakumar-2003/Saravana-Kumar-C-practice/commit/2fbe2982f5203852eaf7ecba22b193fd478f6f9b)
#### Tuesday 2022-12-20 08:35:40 by saravanakumar-2003

Create Team Flash

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

Input & Output Format:

Input consists of 4 integers.

First value consists of x1.

Second value consists of y1.

Third value consists of x2.

Fourth value consists of y2.

Output consists of two float values.

Sample Input
2

4

10

15

Sample Output


6.0
9.5

---
## [saravanakumar-2003/Saravana-Kumar-C-practice](https://github.com/saravanakumar-2003/Saravana-Kumar-C-practice)@[d447623ea8...](https://github.com/saravanakumar-2003/Saravana-Kumar-C-practice/commit/d447623ea815c8ad712bf1594dd3b6c933f3a981)
#### Tuesday 2022-12-20 08:36:25 by saravanakumar-2003

Create The Chronicles of Narnia

Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia. Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in his small hut.It was time for Lucy to return to her family and so she bid good bye to Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as it was already dark.He told her to see the trees while returning back and said that the first tree with two digits number will help her find the way and the way to go back to her home is the sum of digits of the tree and that numbered way will lead her to the tree next to the wardrobe where she can find the others.Lucy was already confused, so pls help her in finding the route to her home.... 

Input Format:
Input consists of an integer corresponding to the 2-digit number.
Output Format:
Output consists of an integer corresponding to the sum of its digits.

Sample Input
23

Sample Output
5

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cf02f62298...](https://github.com/tgstation/tgstation/commit/cf02f622986932af8fb09e48cbdf5ec0ac567cf5)
#### Tuesday 2022-12-20 08:51:55 by LemonInTheDark

useless update_appearance reduction, emissive_blocker micro optimization (saves a second of init) (#71658)

## About The Pull Request

[Saves 0.2 seconds of init time. 50% of emissive
blockers](https://github.com/tgstation/tgstation/commit/8318b648f6d32844aacbfb4c309152cd45801f5c)

Emissive blockers are a decent expense during init, even these, which
are the ones that update outside of initialize.
I've inlined them, removed some redundant vars and checks, reduced the
arg count, and shifted some things around. This ends up saving 200ms, or
50% of its total cost.

I also shifted mutable_appearance about a bit. it's not a massive
saving, but it is technically faster

[Prevents a few redundant appearance_updates, saves 0.8 seconds of
init](https://github.com/tgstation/tgstation/commit/5475cd778b66b22b1e2c8d86b2c6d59fb84f219a)

Prequisit info: update_appearance is decently expensive
It's good then to only do it if we have a reason to, right?

Me and moth were shooting the shit about just general init time, and we
came up with the idea of tracking which update_appearances actually
"worked" and which didn't.

That bit comes later, let's enjoy the fruits of that work first

First, holograms were calling update_appearance on process, for almost
no reason.
I patched the one event they don't already "react" to, and then locked
it behind a change decection if.
good for live, doesn't impact init.

Next, decals. If you add a decal to something before it inits, it'll
react to the after successful init signal.
The trouble is the same atom could have its appearance updated from this
MORE then once, since decals can be stacked on tiles, and signal
unregisters don't work once the signal is sent.
So we add a flag to track if we've had this happen to us or not, so it
only happens once.
saves 80 ms

Power! lots of things call power_change on init, often more then once.
We'll update appearance for each of those calls, even if only one is an
actual change.
That's silly, better to track what sort of power we're using for our
appearance and go off that changing

This was taking about 300ms. Really stupid

Icon smoothing. After emissive blockers were added, any change to
something's icon smoothing would lead to an update_appearance call.
Nasty shit, specially cause of walls, which don't even use emissive
blockers.
Ok then, so we'll always update appearance for movables, and will allow
turfs that are interested to hook it manually.
Not many of those anyhow
This is slightly a dev ux thing, but it saves 600ms so I think it's
worth it. Rare case anyway

Telecomms:
telecomm machines were updating appearance on process. This is to cover
for them turning on/off on process.
Better then to just check if on actually changed.
This cost adds up midgame, doesn't impact init tho

Materials:
There's this update_appearance call in material on_apply. it doesn't do
anything.
The logs will lie to you and say it does, but it's just like reapplying
emissives. It doesn't need to exist
Saves like 50ms

Canisters:
Live thing, lots of time wasted updating appearance for no reason, lets
see if we change anything first yes?

[Uses defines to wrap update_appearance for
tracking](https://github.com/tgstation/tgstation/commit/4fa82e1c9d93577aadb3c743f17196331f62e67c)

[Undoes _update_appearance changes, instead reccomends 2 regexes to
use](https://github.com/tgstation/tgstation/commit/a8c8fec57a4e43d1fa636b5ac68459903faa9fc5)

I need file and line number for my tracking, so I need to override
update_appearance calls, and also preferably not require every override
of update_appearance to handle dummy file + line args.

So instead, I created a wrapper proc that checks to see if appearanaces
match (they're unique remember, the two of the same visual appearance
will be equivalent)
The trouble is I can't intercept JUST proc calls, or JUST function
definitions with defines. it needs to be both.

So I renamed the /update_appearance proc to /_update_appearance

this way I can capture old uses, and don't need to worry about merge/dev
brain skew

~~It does mean that all update_appearance proc definitions now look
weird tho.
My profiling is leaking into dev ux. I wish I had better templating.~~

**The above is no longer being pr'd**, it's instead just recommended via
a few regexes adjacent to the define.
Smelled wrong anyhow

[Adds a setter for panel_open, so I can update_appearance on
it](https://github.com/tgstation/tgstation/pull/71658/commits/cf1df8a69fc1a816391d085ee7419b14f9fe9167)

## Why It's Good For The Game

Speed

---
## [vlebourl/ha-temperature-feels-like](https://github.com/vlebourl/ha-temperature-feels-like)@[0708b10542...](https://github.com/vlebourl/ha-temperature-feels-like/commit/0708b10542333382703e5232b06cd0b862664985)
#### Tuesday 2022-12-20 09:26:07 by Vincent Le Bourlot

Update units conversion for HA 2022.10+ (close #93)
<!--
  You are amazing! Thanks for contributing to our project!
  Please, DO NOT DELETE ANY TEXT from this template! (unless instructed).
-->
## Breaking change
<!--
  If your PR contains a breaking change for existing users, it is important
  to tell them what breaks, how to make it work again and why we did this.
  This piece of text is published with the release notes, so it helps if you
  write it towards our users, not us.
  Note: Remove this section if this PR is NOT a breaking change.
-->

## Proposed change
<!--
  Describe the big picture of your changes here to communicate to the
  maintainers why we should accept this pull request. If it fixes a bug
  or resolves a feature request, be sure to link to that issue in the
  additional information section.
-->

## Type of change
<!--
  What type of change does your PR introduce to Home Assistant?
  NOTE: Please, check only 1! box!
  If your PR requires multiple boxes to be checked, you'll most likely need to
  split it into multiple PRs. This makes things easier and faster to code review.
-->

- [ ] Dependency upgrade
- [ ] Bugfix (non-breaking change which fixes an issue)
- [ ] New feature (which adds functionality to an this integration)
- [ ] Breaking change (fix/feature causing existing functionality to break)
- [ ] Code quality improvements to existing code or addition of tests

## Example entry for `configuration.yaml`:
<!--
  Supplying a configuration snippet, makes it easier for a maintainer to test
  your PR. Furthermore, for new integrations, it gives an impression of how
  the configuration would look like.
  Note: Remove this section if this PR does not have an example entry.
-->

```yaml
# Example configuration.yaml

```

## Additional information
<!--
  Details are important, and help maintainers processing your PR.
  Please be sure to fill out additional details, if applicable.
-->

- This PR fixes or closes issue: fixes #
- This PR is related to issue:

## Checklist
<!--
  Put an `x` in the boxes that apply. You can also fill these out after
  creating the PR. If you're unsure about any of them, don't hesitate to ask.
  We're here to help! This is simply a reminder of what we are going to look
  for before merging your code.
-->

- [ ] The code change is tested and works locally.
- [ ] There is no commented out code in this PR.
- [ ] The code has been formatted using Black (`black --fast custom_components`)

If user exposed functionality or configuration variables are added/changed:

- [ ] Documentation added/updated to README.md

<!--
  Thank you for contributing <3
-->

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[6dd4839ef3...](https://github.com/carshalash/tgstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Tuesday 2022-12-20 10:40:12 by carshalash

Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.


![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.


![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[00e7d5d746...](https://github.com/carshalash/tgstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Tuesday 2022-12-20 10:40:12 by GoldenAlpharex

*hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[500aaccb50...](https://github.com/treckstar/yolo-octo-hipster/commit/500aaccb5030bbe818b3942f52bc4160101cd655)
#### Tuesday 2022-12-20 12:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Manaball123/funny-gpt-overwrite](https://github.com/Manaball123/funny-gpt-overwrite)@[58810c4a32...](https://github.com/Manaball123/funny-gpt-overwrite/commit/58810c4a32514cf99a542119d5a309897b23eda8)
#### Tuesday 2022-12-20 12:33:51 by Mana

unfucked the repo

i mean the main.cpp is basically the only source file so it should be pretty easy to compile it u can literal;ly just create a new project and copy and paste this into it
i mean sure it kinda defeats the purpose of a git but who the fuck would wanna contribute to shit like this, like this shit isnt hard to make at all and there really is no point in "making it better" cuz this shit can already brick pcs by itself
also do people even read these i actually tried to see if i can see the comments of a commit but i couldnt figure out how so im assuming its not something that is very convenient to do(that or im retarded)
anyways thx for reading through my schizo rant

---
## [simoheinonen/EasyAdminBundle](https://github.com/simoheinonen/EasyAdminBundle)@[919545baeb...](https://github.com/simoheinonen/EasyAdminBundle/commit/919545baebcf0b7ae1f8a35210afc4bd92769161)
#### Tuesday 2022-12-20 12:55:14 by Javier Eguiluz

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
## [sr229/garrysmod-chatsounds](https://github.com/sr229/garrysmod-chatsounds)@[b57b3d8d45...](https://github.com/sr229/garrysmod-chatsounds/commit/b57b3d8d45f8dd4c014640f92eced35d940d4a36)
#### Tuesday 2022-12-20 13:54:24 by Ayane

My name is Skyler White yo (#428)

* My name is Walter Hartwell White.

I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead, murdered by my brother-in-law Hank Schrader. Hank has been building a Virtual Youtuber empire for over a year now and using me as his recruiter. Shortly after my 50th birthday, Hank came to me with a rather, shocking proposition. He asked that I use my Live2D knowledge to recruit talents, which he would then hire using his connections in the Japanese utaite world. Connections that he made through his career with Niconico. I was... astounded, I... I always thought that Hank was a very moral man and I was... thrown, confused, but I was also particularly vulnerable at the time, something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me on a ride along, and showed me just how much money even a small indie channel could make. And I was weak. I didn't want my family to go into financial ruin so I agreed. Every day, I think back at that moment with regret. I quickly realized that I was in way over my head, and Hank had a partner, a man named Motoaki Yagoo Tanigo, a businessman. Hank essentially sold me into servitude to this man, and when I tried to quit, Yagoo threatened my family. I didn't know where to turn. Eventually, Hank and Yagoo had a falling out. From what I can gather, Hank was always pushing for a greater share of the business, to which Yagoo flatly refused to give him, and things escalated. Yagoo was able to arrange, uh I guess I guess you call it a hit on my brother-in-law, and failed, but Hank was seriously injured, and I wound up paying his medical bills which amounted to a little over 77,000. Upon recovery, Hank was bent on revenge, working with a man named Riku Tazumi , he plotted to kill Yagoo, and did so. In fact, the bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen in the ranks to become the head of the Cover Corp, and about that time, to keep me in line, he took my children from me. For 3 months he kept them. My wife, who up until that point, had no idea of my vtubing activities, was horrified to learn what I had done, why Hank had taken our children. We were scared. I was in Hell, I hated myself for what I had brought upon my family. Recently, I tried once again to quit, to end this nightmare, and in response, he gave me this. I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. I... All I could think to do was to make this video in hope that the world will finally see this man, for what he really is.

---
## [Kinglove936/Rocky](https://github.com/Kinglove936/Rocky)@[d7af747388...](https://github.com/Kinglove936/Rocky/commit/d7af747388a597f8926a634e58cca8018147af9f)
#### Tuesday 2022-12-20 13:58:36 by Start on that earth

Update README.md

# HHVM

[HHVM page](https://hhvm.com) |
[HHVM documentation](https://docs.hhvm.com/hhvm/) |
[Hacklang page](http://hacklang.org) |
[General group](https://www.facebook.com/groups/hhvm.general/) |
[Dev group](https://www.facebook.com/groups/hhvm.dev/) |
[Twitter](https://twitter.com/HipHopVM)

HHVM is an open-source virtual machine designed for executing programs written in [Hack](http://hacklang.org). HHVM uses a just-in-time (JIT) compilation approach to achieve superior performance while maintaining amazing development flexibility.

HHVM should be used together with a webserver like the built in, easy to deploy [Proxygen](https://docs.hhvm.com/hhvm/basic-usage/proxygen), or a [FastCGI](https://docs.hhvm.com/hhvm/advanced-usage/fastCGI)-based webserver on top of nginx or Apache.

## Installing

If you're new, try our [getting started guide](https://docs.hhvm.com/hhvm/getting-started/getting-started).

You can install a [prebuilt package](https://docs.hhvm.com/hhvm/installation/introduction#prebuilt-packages) or [compile from source](https://docs.hhvm.com/hhvm/installation/building-from-source).

## Running

You can run standalone programs just by passing them to hhvm: `hhvm example.hack`.

If you want to host a website:
* Install your favorite webserver. [Proxygen](https://docs.hhvm.com/hhvm/basic-usage/proxygen) is built into HHVM, fast and easy to deploy.
* Install our [package](https://docs.hhvm.com/hhvm/installation/introduction#prebuilt-packages)
* Start your webserver
* Run `sudo /etc/init.d/hhvm start`
* Visit your site at `http://.../main.hack`

Our [getting started guide](https://docs.hhvm.com/hhvm/getting-started/getting-started) provides a slightly more detailed introduction as well as links to more information.

## Contributing

We'd love to have your help in making HHVM better. If you're interested, please read our [guide to contributing](CONTRIBUTING.md).

## License

HHVM is licensed under the PHP and Zend licenses except as otherwise noted.

The [Hack typechecker](hphp/hack) is licensed under the MIT [License](hphp/hack/LICENSE) except as otherwise noted.

The [Hack Standard Library](hphp/hsl) is licensed under the MIT [License](hphp/hsl/LICENSE) except as otherwise noted.

## Reporting Crashes

See [Reporting Crashes](https://github.com/facebook/hhvm/wiki/Reporting-Crashes) for helpful tips on how to report crashes in an actionable manner.

## Security

For information on reporting security vulnerabilities in HHVM, see [SECURITY.md](SECURITY.md).

## FAQ

Our [user FAQ](https://docs.hhvm.com/hhvm/FAQ/faq) has answers to many common questions about HHVM, from [general questions](https://docs.hhvm.com/hhvm/FAQ/faq#general) to questions geared towards those that want to [use](https://docs.hhvm.com/hhvm/FAQ/faq#users).

There is also a FAQ for [contributors](https://github.com/facebook/hhvm/wiki/FAQ#contributors) to HHVM.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4cd592edfe...](https://github.com/mrakgr/The-Spiral-Language/commit/4cd592edfea836ff7d35bfb5ad131ad306f8a0fb)
#### Tuesday 2022-12-20 14:51:16 by Marko Grdinić

"2:15pm. I am feeling dizzy from all the thinking and the chores. Finally I can enjoy breakfast for a bit. Now that I've had time to compare programming and writing, they are not close in terms of intensity.

2:35pm. https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0

I'll keep this model in mind for when I get back to prompting.

3:20pm. No replies yet. Are the questions I am asking difficult? Probably he just has work to take care of. It will take a few more days before I have the first backend operational, so it is no big deal.

3:25pm. Right now, let me focus on testing out the new C backend. I have faith in the refc passes, but all the changes to the codegen might have wrecked something by accident. I'll know right away when I look at the diffs.

```c
void HeapDecref0(Heap0 * x){
    if (x != NULL && --(x->refc) == 0) { HeapDecrefBody0(x); free(x); }
    }
}
Heap0 * HeapCreate0(bool v0){
    Heap0 * x = malloc(sizeof(Heap0));
    x->refc = 1;
    x->v0 = v0;
    v0->refc++;
    return x;
}
```

Some borken syntax and bools being incref'd.

```fs
            | REFC_INCR ->
                match t' with
                | YUnion t when t.Item.layout = UStack -> Some $"USIncref{(ustack t).tag}(&({f v}));"
                | YPrim t when t <> StringT -> None
                | _ -> Some $"{f v}->refc++;"
            | REFC_SUPPR ->
                match t' with
                | YUnion t when t.Item.layout = UStack -> Some $"USSuppref{(ustack t).tag}(&({f v}));"
                | YPrim t when t <> StringT -> None
                | _ -> Some $"{f v}->refc--;"
```

Ah wait, this would affect even macros.

Ah, how annoying. Well whatever. Let me do them all in turn.

```fs
    and refc_change' (f : int * Ty -> string) (refc_flag : REFC) (x : TyV []) : string [] =
        Array.choose (fun (L(i,t')) ->
            let v = i,t'
            let inline g decref =
                match refc_flag with
                | REFC_INCR -> Some $"{f v}->refc++;"
                | REFC_DECR -> Some (decref())
                | REFC_SUPPR -> Some $"{f v}->refc--;"
            match t' with
            | YUnion t ->
                match t.Item.layout with
                | UStack ->
                    match refc_flag with
                    | REFC_INCR -> Some $"USIncref{(ustack t).tag}(&({f v}));"
                    | REFC_DECR -> Some $"USDecref{(ustack t).tag}(&({f v}));"
                    | REFC_SUPPR -> Some $"USSuppref{(ustack t).tag}(&({f v}));"
                | UHeap -> g (fun () -> $"UHDecref{(uheap t).tag}({f v});")
            | YArray t -> g (fun () -> $"ArrayDecref{(carray t).tag}({f v});")
            | YFun(a,b) -> g (fun () ->  $"{f v}->decref_fptr({f v});")
            | YPrim StringT -> g (fun () ->  $"StringDecref({f v});" )
            | YLayout(a,Heap) -> g (fun () ->  $"HeapDecref{(heap a).tag}({f v});")
            | YLayout(a,HeapMutable) -> g (fun () ->  $"MutDecref{(mut a).tag}({f v});")
            | _ -> None
            ) x
```

This should fix bools getting incremented.

Now let me fix the broken syntax.

```fs
let print_decref s_fun name_fun type_arg name_decref =
    line s_fun (sprintf "void %s(%s * x){" name_fun type_arg)
    let _ =
        let s_fun = indent s_fun
        line s_fun (sprintf "if (x != NULL && --(x->refc) == 0) { %s(x); free(x); }" name_decref)
    line s_fun "}"
```

That should do it. Let me move on.

3:45pm. https://cee.studio/

Right now I am trying this. How did the commands to enable memory checking work?

DTS_REPORT_UNRELEASED_MEMORY=1 DTS_REPORT_ALL_MEMORY_SPACES=1 DTS_MEMORY_UNINIT_CHECK=disabled ./a.out
DTS_REPORT_UNRELEASED_MEMORY=1 DTS_REPORT_ALL_MEMORY_SPACES=1 ./a.out

I just need to build and then run one of these commands.

Let me go through them all in turn. I tested it on the last one so far.

I'll want to check the rest."

---
## [Kordasauter/roprime-simulator.com](https://github.com/Kordasauter/roprime-simulator.com)@[c3fddaaff1...](https://github.com/Kordasauter/roprime-simulator.com/commit/c3fddaaff104f5f13c0c0acd7acfcf3d0340ce56)
#### Tuesday 2022-12-20 15:11:20 by Kordasauter

Triple Trouble Update

20/12/2022:
Has been added :
Triple Trouble Update
Horror Toy Factory
Monsters
Decorated Evil Tree
Wicked Vice Plant Manager
Vicious Cookie
Corrupt Cruiser
Evil Dwelling Box
Creepy Demon
Malicious Baby Ghost
Dancing Marionette
Abandoned Teddy Bear
Celine Kimi
Cards
Decorated Evil Tree Card
Vicious Cookie Card
Evil Dwelling Box Card
Creepy Demon Card
Malicious Baby Ghost Card
Dancing Marionette Card
Abandoned Teddy Bear Card
Celine Kimi Card
Equipments and enchantments
Old Parasol
Red Lantern
Hurt Mind
Kind Heart
Lush Rose
Evil Spirit Gloves
Celine''s Ribbon
Noble Cross
Nightmare Pyramids
Monsters
Verit (Nightmare)
Mummy (Nightmare)
Minorous (Nightmare)
Mimic (Nightmare)
Arclouse (Nightmare)
Ancient Mummy (Nightmare)
Amon Ra (Nightmare)
Cards
Nightmare Verit Card
Nightmare Mummy Card
Nightmare Minorous Card
Nightmare Mimic Card
Nightmare Arclouse Card
Nightmare Ancient Mummy Card
Nightmare Amon Ra Card
Undersea Tunnel (6th floor)
Monsters
King Dramoh
Sropho
Pot Dofle
Sedora
Kraken
Cards
King Dramoh Card
Sropho Card
Pot Dofle Card
Sedora Card
Kraken Card

---
## [mach0/subsurface.github.io](https://github.com/mach0/subsurface.github.io)@[ad4b82193b...](https://github.com/mach0/subsurface.github.io/commit/ad4b82193be920f3b90c6a31a757368dcc202c54)
#### Tuesday 2022-12-20 15:12:24 by Dirk Hohndel

small updates to deal with horizontal lines

I wonder if the magic that creates them isn't more trouble than it's worth.
Maybe it would be better to make them explicit? This seems hacky...

This commit also has a couple of tiny edits to the things Jason brought
over from the old FAQ.

Signed-off-by: Dirk Hohndel <dirk@hohndel.org>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[0dd70b12e5...](https://github.com/cmss13-devs/cmss13/commit/0dd70b12e5142b3b0f14bf237765c1e643fe8a3f)
#### Tuesday 2022-12-20 15:33:18 by Stan_Albatross

removes unused nanoui templates (#2012)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

none of these templates are used anywhere

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui

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
del: Removed ten unused nanoui templates. Don't worry, they'll all be
going away soon.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [newstools/2022-the-daily-sun](https://github.com/newstools/2022-the-daily-sun)@[7f4bb752ac...](https://github.com/newstools/2022-the-daily-sun/commit/7f4bb752acdc8aed3c07cb64f817414872365cce)
#### Tuesday 2022-12-20 15:37:46 by Billy Einkamerer

Created Text For URL [www.snl24.com/dailysun/news/cop-who-killed-his-2-girlfriends-commits-suicide-20221220]

---
## [Pewtro/Details-Damage-Meter](https://github.com/Pewtro/Details-Damage-Meter)@[b8851987bb...](https://github.com/Pewtro/Details-Damage-Meter/commit/b8851987bb559f42624ddbcef3336bed8f0c31cd)
#### Tuesday 2022-12-20 16:05:40 by Flamanis

Update SpecSpellList for DF live

Removals:
Shaman - Healing Stream Totem is usable by all specs
Druid - Survival Instincts is on both Guardian and Feral
Druid - Adaptive Swarm is used by multiple specs
Paladin - Avenging wrath is usable by all specs
Warlock - Grimoire of Sacrifice is usable by both Aff and Destro
Rogue - Shiv is usable by all specs
Hunter - Marksman and BM hunters have the same Kill Command. Survival does not.

Additions:
Hunter - BM gets Cobra Shot
Hunter - Survival has different Kill Shot and Muzzle (Interrupt) ids
Warrior - Protection has Spell Block
Evoker - Devastation has another ID for Eternity Surge (Kinda just added this one in for safety)
Priest - Discipline has Purge The Wicked talent which replaces Shadow Word Pain
Mage - Arcane Mage's Arcane Familiar
Paladin - Protection has Blessed Hammer and Blessing of Spellwarding
Druid - Balance has Wild Mushroom, and different spell ids for Moonkin Form, Starfire, and Starsure
Druid - Guardian has a different id for Berserk that the 'modifiers' are consolidated into
Monk - Mistweaver has Mana Tea
Demon Hunter - Vengeance has Sigil of Silence and Fracture
Demon Hunter - Havoc has Blur
Death Knights - Added the primary strikes. Heart Strike (Blood), Obliterate (Frost), Festering Strike (Unholy)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[12d3f00303...](https://github.com/mrakgr/The-Spiral-Language/commit/12d3f00303f64de00bc58123b7fb6b8807c6867c)
#### Tuesday 2022-12-20 16:33:07 by Marko Grdinić

"```
// Does the partial evaluator optimize unused match cases?
union t = A : heap i32 * mut (heap u64) | B : heap f64
inl main () =
    inl ~a, ~b, ~c = B (heap 5), B (heap 2), B (heap 1)
    match (join a,b,c) with
    | A, _, _ => 1i32
    | _, A, _ => 2
    | _, _, A => 3
    | _ => 4
```

I've decided to modify `test39`. I want to see if some of the branches are getting generated correctly.

4:30pm. Have a bunch of unused variable warnings. They don't matter. I am assuming the C compiler will optimize them away.

4:50pm. Done. All tests pass now. Let me push out a new version of Spiral.

4:55pm. I published it on the VS Code marketplace, but why does the NPX command no longer work?

Hmmm...remember how I complained yesterday that cmd doesn't work. It seems that npm doesn't work either. What is happening?

...Uninstalling all those old Python version really wrecked my computer. I need to figure out why npm and cmd commands are not working.

```
PS C:\Users\Marko> where cmd
PS C:\Users\Marko>
```

This is really bizzare.

`cmd` is in the system32 directory, but it is not working.

https://answers.microsoft.com/en-us/windows/forum/all/cmdexe-no-longer-opens-after-uninstalling-python/9ca0dd4a-4eff-4a21-ad30-16d6a8e28790

> Can you check if running "cmd.exe /d" launches the Command Prompt correctly?

Oh this does launch it.

> reg delete "HKCU\SOFTWARE\Microsoft\Command Processor" /v "Autorun" /f

Oh it worked!

I just googled 'window command not working after python uninstall' and it was near the top of the search list. No way I would have figured it out on my own. `npm` is working as well.

> Published mrakgr.spiral-lang-vscode v2.2.6

Whops.

> Unpublishing is not supported at the moment because that might break others who depend on a published extension. We could consider going for an approach like npm, i.e. allow to unpublish only in certain circumstances:

Ah, whatever. It doesn't matter.

5:20pm. My god, how long can it take to publish? At any rate, I am done.

Let me paste what I've written a few entries ago.

///

12:35pm. That's about it. Now I'll have to go though the test cases again and even run them. The purpose of this is to make tail loops faster. I realized during the night that depending on where the jump is made, the compuler could potentially optimize the jump so skips both the decrement and the increment of the reference right at the start of the loop.

For example...

```c
void foo(Heap0 * a) {
    a->refc++;
    ...
    if (cond) {
        a->refc--;
        foo(a);
        }
    }
```

Consider something like this. When the tail call loop optimization is done, instead of jumpting right at the start of the function, it could skip the `a->refc++;` and the `a->refc--;` parts.

When you inline foo once, you see that the inc and dec refs are right next to each other and can be eliminated.

But with the previous function that I had...

```c
void HeapRefc0(Heap0 * x, REFC_FLAG q){
    if (x != NULL) {
        int refc = (x->refc += q & REFC_INCR ? 1 : -1);
        if (!(q & REFC_SUPPR) && refc == 0) {
            HeapRefcBody0(x, REFC_DECR);
            free(x);
        }
    }
}
```

You had things like this. An optimizing compiler is going to have a hard time optimizing this. A particular logical issue that was present here before is that increfing could potentially free the object. Now that is no longer a problem. You just have an increment and a decrement. And they are inlined instead of hidden behind functions.

One consequence is that I can no longer read unitialized objects from arrays, but the assignment to them should be fine. This is perfectly acceptable. The only times I've used nullables is by mistake in F#. Maybe I've used null strings, but that is about it.

...Well, I am doing a search through the project and it does seem like I've used them on occasion. But they are hardly necessary or irreplaceable.

///

This is basically the reason to do it like this. Replacing function calls with simple increment and decrement operations opens the door to optimizing them away in tail calls.

```c
void HeapDecref0(Heap0 * x){
    if (x != NULL && --(x->refc) == 0) { HeapDecrefBody0(x); free(x); }
}
```

Also, I much rather prefer the decrement to be like this. It is very succinct and understandable compared to those boolean operations I had going last time. Remember that it took me time to understand what was going on. I had forgotten that REFC_SUPPR was supposed to be 2 10 in binary and so on. This on the other hand is crystal clear.

I think now I can say that I've done ref counting properly. Maybe in the future I'll extend the heap and mut types so they take in disposal pointers. That would allow them to handle file handle and other kinds of resources instead of just memory. It would be easy to add too.

But it doesn't matter right now. What I should focus next is dealing with the Python backend. Once I have it, I can begin work on the UPMEM composite backend. After I have that I can begin work on the generic map, fold and filter kernels. And once I have that I'll be able to write an article for HN.

I'll also do a C based UPMEM backend as well.

I am not sure if doing this will benefit me much, but it will be a good showcase of my skills."

---
## [MervineN/Business-Statistical-Analysis](https://github.com/MervineN/Business-Statistical-Analysis)@[31db37cd5d...](https://github.com/MervineN/Business-Statistical-Analysis/commit/31db37cd5d9a9fd649ed5bb1c86d14e4f42f1083)
#### Tuesday 2022-12-20 19:05:47 by MervineN

Update README.md

### Conclusion :
I analyzed a dataset of the response of 100 randomly selected users divided into two groups(samples)-the treatment and the control group.The treatment group is served the new landing page and the control group is served the old landing page.My conclusions from the analysis made are:

* 54.0% of users in the dataset converted to subscribers of the news portal and 46.0% of users in the dataset did not convert to suscribers of the news portal.
* There are 3 unique languages in this dataset that users use to view the landing page.The most choosen language used, is the French and Spanish language.
* In this dataset,the time spent on the page by users ranges from ~0.19(minimum ) to ~10.7(maximum) minutes.The average time spent by users on the landing page is ~ 5.38 minutes.
* Visually when we compare the time spent on the page distribution of the two samples(treatment and control group),**it seems the users spend more time on the new landing page than the old landing page and hence statistically,we have enough evidence to say that this holds.**
* 33.0% of users who viewed the new landing page(treatment group) and 21.0% of users who viewed the old landing page(control group),converted to subscribers of the news portal.Visually,it seems the proportion of users who visit the new landing page and get converted to subscribers of the news portal is more than the proportion of users who visit the old landing page and get converted to subscribers of the news portal.Hence statistically,**we have enough evidence to say that the conversion rate for the new page is greater than the conversion rate for the old page.**
* From the sample,21.0% of users who choosed English language,18.0% of users who choosed French language and 15.0% of users who choosed Spanish language to view the landing page, converted to subscribers of the news portal.Even though visually from the sample,it seems that the users who choosed English language had the highest converted status ,statistically,**there is not enough evidence to say that the converted status depends on the preferred language.**
* When we compare the sample mean time spent on the new landing page for different language users,even though visually it seems as if the mean time spent on the new landing page differs among the three different language users,**there is enough statistical evidence to say that the mean time spent on the new page is same for the different language users.**

### Business Recommendations :

* From the above analysis and conclusions,the new landing page created by the design team of the company which suggest that it might be more captivating as the users spend more time on it.The new landing page is hence more effective to gather new subscribers.If the new landing page is maintained and why not perfected ,it might gather many more subscribers.
* Eventhough statistically,they have been evidence that converted status is independent of preferred language which visually shows other wise,i think it's better for the company to carry out further investigations on users about this inorder to have a deeper insight and better viewers-news portal experience which might attract many more subscribers.
* I suggest the company should further investigate subscription method and find ways to facilitate subscription.This is because some users though they spent alot of time on the new landing page,yet they don't subscribe.May be subscription method to the news portal is quite complex or time demanding for some users which might find it quite hard to subscribe eventhough they enjoy the news portal .

---
## [SimonN/lix-unstable](https://github.com/SimonN/lix-unstable)@[f5e9992668...](https://github.com/SimonN/lix-unstable/commit/f5e9992668527452733834ec9dc6066a46033789)
#### Tuesday 2022-12-20 19:41:16 by Simon Naarmann

Remove 6 Gaps, add Private Room

Remove 6 Gaps, 5 Builders from Quirky. On Lemmings Forums, we think
it's not pulling its weight as a puzzle, even if we were to fix it
so that no single builder can cross 2 gaps, and you'd need 2 builders
to cross 3 gaps.

Move Ferry Tale from Lovely into Quirky. It's hard enough.

Add Private Room Without Room, a new level by mobius, to Lovely.
This fills Ferry Tale's old slot.

---
## [DolevSeri/EKrut_final](https://github.com/DolevSeri/EKrut_final)@[6970ff2664...](https://github.com/DolevSeri/EKrut_final/commit/6970ff26642768c32923de7868107420bcc0ad90)
#### Tuesday 2022-12-20 20:21:42 by DolevSeri

Merge pull request #13 from DolevSeri/Dolev_Work

fuck you

---
## [DolevSeri/EKrut_final](https://github.com/DolevSeri/EKrut_final)@[45e06a3f0f...](https://github.com/DolevSeri/EKrut_final/commit/45e06a3f0f09a1bd2e22404ae033a09baec0980d)
#### Tuesday 2022-12-20 20:25:43 by DolevSeri

Merge pull request #14 from InbarMizrahi1/inbar_work

fuck you too

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[229a2e6ed2...](https://github.com/cmss13-devs/cmss13/commit/229a2e6ed24998b2b97421ae421cfe25b77ae1b1)
#### Tuesday 2022-12-20 20:34:14 by Stan_Albatross

Teleporter tgui and minor refactor (#1997)

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

converts teleporters to tgui and removes some shitcode

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui


![image](https://user-images.githubusercontent.com/66756236/208460209-8f260838-1da1-49af-8d6c-44efcc974efb.png)


![image](https://user-images.githubusercontent.com/66756236/208458960-7bd162fd-e2fe-4c23-a3f6-257cb73516f5.png)


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
ui: swapped teleporters to use tgui.
fix: teleporter consoles now have actual sprites!
code: "improved" some teleporter code.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [gonzus/AdventOfCode](https://github.com/gonzus/AdventOfCode)@[438093190d...](https://github.com/gonzus/AdventOfCode/commit/438093190d9fd66974c9955681056e1e115a7dd0)
#### Tuesday 2022-12-20 20:44:07 by Gonzalo Diethelm

2022 day 19

This is an awful, ugly, randomized brute-force solution.

I basically could not be arsed to come up with a good pruning strategy
for selecting the robots to build, as well as getting rid as early as
possible of useless tree branches.  Instead, I just choose randomly
whether to build each type of robot and run it a gazillion times,
keeping track of the best results so far.

On my M1 laptop part 1 takes 19s and part 2 takes 30s.

Shameful.

---
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[a9fda932e2...](https://github.com/Floofies/tgstation/commit/a9fda932e2a9d8cf20f5f74fdcbdbcca86d580e6)
#### Tuesday 2022-12-20 21:06:32 by Tim

Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u 
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.


![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

---
## [newstools/2022-sundiata-post](https://github.com/newstools/2022-sundiata-post)@[80f0c24291...](https://github.com/newstools/2022-sundiata-post/commit/80f0c242913dceae34c9b1f213290dd39429430c)
#### Tuesday 2022-12-20 21:18:46 by Billy Einkamerer

Created Text For URL [sundiatapost.com/south-african-police-officer-accused-of-killing-his-two-girlfriends-commits-suicide-in-prison-cell/]

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[6941110757...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/6941110757ed63b66f157c138ca450bc0d182017)
#### Tuesday 2022-12-20 22:15:40 by AmyBSOD

Finish the motherfucking artifacts

Gaaaaaaaaaaaaah. I don't want to have to see any nethack code for the next month now because this was such a pain in the butt. Also, I want to sleep for 25 hours straight and have a bonus of €200 transferred to my account as a compensation for all the hard work I put into coding those artifacts.

---
## [bluerise/openbsd-src](https://github.com/bluerise/openbsd-src)@[0cffdb45a9...](https://github.com/bluerise/openbsd-src/commit/0cffdb45a9bb573ce4665f5540d1a0d50ff2e37f)
#### Tuesday 2022-12-20 22:30:52 by tb

acme-client: fix SAN-handling insanity

The revoke process, which does a lot more than revoking a cert, wants to
know the SANs in the cert to be revoked or renewed and check them against
the ones configured in the config file.

To find out which ones are, it prints the SAN extension to a BIO using
X509V3_EXT_print(), slurps that into a buffer, tokenizes the undocumented
output string and plucks out the "DNS:" names. This is reminiscent of
node's hilarious CVE-2021-44532 and on about the same level of crazy, but
fortunately not security relevant.

Get the SAN extension as a GENERAL_NAMES from libcrypto, then we have an
actual data structure to work with, which allows us to access the DNS names
without problems. This simplifies things quite a bit, but the actual logic
in this file remains unmodified. Be careful about ASN1_IA5STRINGs and do
not assume they are C strings.

Tested by florian, millert, Renaud Allard, thanks!

ok florian jsing

---
## [Unit2E/tgstation](https://github.com/Unit2E/tgstation)@[3c187487b1...](https://github.com/Unit2E/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Tuesday 2022-12-20 22:38:43 by MrMelbert

Renews a bunch of old roundend new reports that got lost. Plus, some roundend report QoL for cult and revs. (#71284)

## About The Pull Request

A few roundend reports got lost from moving to dynamic and other prs.
This PRs re-allows them to occur. Namely: "Wizard Killed" (lost in
dynamic), "Blob nuked" (lost in dynamic), "Cult escaped" (lost in cult
rework), and "Nuke Ops Victory" (station destroyed via nuke) (lost from,
what I can see, an oversight / accidental swap of report values).

Additionally, small roundend report QOL for cult: Removes antag datums
from spirit realm ghosts after being dusted, so they do not show up on
the report. And in reverse, heads of staff who were dusted / destroyed
in revolution rounds are now also shown in roundend reports.

## Why It's Good For The Game

Some of these reports are dead, which is is a shame because I think
they're cool and fun.

## Changelog

:cl: Melbert
qol: Successfully fending off a blob now has a cross station news report
again. More pressing reports will take priority over it, though.
qol: Successfully killing a wizard (and all of their apprentices) now
has a cross station news report again.
qol: If more than half of a cultist team manages to escape on the
shuttle (rather than summoning Nar'sie), they will send a unique cross
station news report. This is still a loss, by the way. Summon Nar'sie!
qol: Nuclear Operatives successfully nuking the station now has its
unique cross station news report again, and no longer uses the generic
"The station was nuked" report.
qol: Nuking the station to stop a blob infection now has a unique cross
station news report again. Good luck convincing admins to allow this.
qol: Cult ghosts from "Spirit Realm" no longer persist on the cult's
team after being desummoned, meaning they will not show up on roundend
report.
qol: Heads of staff will now always show up on revolution roundend
report - even if their body was fully destroyed.
/:cl:

---
## [Danielkaas94/TheNoitaGifCollection](https://github.com/Danielkaas94/TheNoitaGifCollection)@[87b214e678...](https://github.com/Danielkaas94/TheNoitaGifCollection/commit/87b214e6789499649b403b932723ff1d8aff34a5)
#### Tuesday 2022-12-20 22:39:45 by Danielkaas94

🔨 THE EMPEROR NEED MOAR WIDTH! 🔨
    • Victory needs no explanation, defeat allows none.
    • The difference between heresy and treachery is ignorance.
    • Heresy grows from idleness.
    • Cleanse, Purge, KILL!
    • Faith without deeds is worthless.
    • We are the Space Marines! We are the Emperor’s fury!
    • The Emperor guides my blade
    • Walk softly, and carry a big gun
    • For the Emperor!
    • Without him there is nothing.
    • Work earns Salvation.
    • Prayer cleanses the soul, Pain cleanses the body.
    • Cowards die in shame.
    • Fear denies faith.
    • Hope is the first step on the road to disappointment.
    • Only in death does duty end 💀

---
## [nimblemachines/muforth](https://github.com/nimblemachines/muforth)@[5043786e38...](https://github.com/nimblemachines/muforth/commit/5043786e38d776d6dd38df152ac026b0a07a56e3)
#### Tuesday 2022-12-20 23:42:10 by David Frech

[arm] O frabjous day! Working USB firmware for STM32F303/F072!!!!!

Late last night I realized that I the "variable" defining word was
wrong, and wouldn't work for code compiled into flash.

I fixed it, re-compiled the USB test code, and it immediately worked!

This is after trying over and over to get it to work, and basically
giving up on ST and the STM32. It turned out to be a stupid simple
mistake on my part.

I've made a few small changes to the USB code, including commenting out
the possibly offensive "manufacturer string" and replacing it with
something banal.

I've also made the USB code the "out of the box" code that the STM32F072
Discovery and F3 Discovery board files load.

You too can try this at home!

  ./muforth -f target/ARM/board/stm32f072b-discovery.mu4

OR

  ./muforth -f target/ARM/board/stm32f3-discovery.mu4

then

  jtag
  flash-image
  verify

Reset the board, plug into the "user USB" jack, and watch your favorite
OS enumerate the board. I've had success with Linux and Windows 10.

Pressing the reset switch will disconnect from the USB, and the board
will re-enumerate.

It doesn't do anything more than that, but the hard part was getting to
this point. Adding code to process vendor requests to turn it into a
chat target is pretty easy.

Super exciting!!!!

---

