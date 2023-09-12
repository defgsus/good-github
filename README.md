## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-11](docs/good-messages/2023/2023-09-11.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,398,198 were push events containing 3,649,246 commit messages that amount to 286,577,933 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 59 messages:


## [sirdarckcat/linux-1](https://github.com/sirdarckcat/linux-1)@[1548b060d6...](https://github.com/sirdarckcat/linux-1/commit/1548b060d6f32a00a2f7e2c11328205fb66fc4fa)
#### Monday 2023-09-11 00:06:22 by Linus Torvalds

Merge tag 'topic/drm-ci-2023-08-31-1' of git://anongit.freedesktop.org/drm/drm

Pull drm ci scripts from Dave Airlie:
 "This is a bunch of ci integration for the freedesktop gitlab instance
  where we currently do upstream userspace testing on diverse sets of
  GPU hardware. From my perspective I think it's an experiment worth
  going with and seeing how the benefits/noise playout keeping these
  files useful.

  Ideally I'd like to get this so we can do pre-merge testing on PRs
  eventually.

  Below is some info from danvet on why we've ended up making the
  decision and how we can roll it back if we decide it was a bad plan.

  Why in upstream?

   - like documentation, testcases, tools CI integration is one of these
     things where you can waste endless amounts of time if you
     accidentally have a version that doesn't match your source code

   - but also like the above, there's a balance, this is the initial cut
     of what we think makes sense to keep in sync vs out-of-tree,
     probably needs adjustment

   - gitlab supports out-of-repo gitlab integration and that's what's
     been used for the kernel in drm, but it results in per-driver
     fragmentation and lots of duplicated effort. the simple act of
     smashing an arbitrary winner into a topic branch already started
     surfacing patches on dri-devel and sparking good cross driver team
     discussions

  Why gitlab?

   - it's not any more shit than any of the other CI

   - drm userspace uses it extensively for everything in userspace, we
     have a lot of people and experience with this, including
     integration of hw testing labs

   - media userspace like gstreamer is also on gitlab.fd.o, and there's
     discussion to extend this to the media subsystem in some fashion

  Can this be shared?

   - there's definitely a pile of code that could move to scripts/ if
     other subsystem adopt ci integration in upstream kernel git. other
     bits are more drm/gpu specific like the igt-gpu-tests/tools
     integration

   - docker images can be run locally or in other CI runners

  Will we regret this?

   - it's all in one directory, intentionally, for easy deletion

   - probably 1-2 years in upstream to see whether this is worth it or a
     Big Mistake. that's roughly what it took to _really_ roll out solid
     CI in the bigger userspace projects we have on gitlab.fd.o like
     mesa3d"

* tag 'topic/drm-ci-2023-08-31-1' of git://anongit.freedesktop.org/drm/drm:
  drm: ci: docs: fix build warning - add missing escape
  drm: Add initial ci/ subdirectory

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[7d600bf36a...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/7d600bf36a691d4be27e852eed0106a1564d7aee)
#### Monday 2023-09-11 00:10:46 by TheObserver-sys

More plants, new chems, new carpet generation techniques, plantcell buff, and the drills now have a GPS signal! (#5912)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/4d3a51f1-7d2b-4d56-9971-7f33d76610f1)

![image](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/assets/58029438/608ba481-2499-4bf0-a25c-cc503655bf7d)

New! Exciting! Things! YEEHAW!

Okay, hype aside, this adds two plants from Main -- the third, and most
powerful sister of the ambrosia family, and the better grass, carpet!

Ambrosia Gaia: A difficult plant to keep alive, being very vulnerable to
weeds, pests, and any amount of toxins in the tray, as well as voracious
when it comes to nutrients and water. In exchange, the plant produces a
very, very powerful healing agent: Earthsblood.

For the cost of your brain, your ability to gauge how injured you are,
and when it works again, the ability to see clearly, your body will be
repaired in miraculous ways! (4/4 Brute Burn, 4 tox, 10 oxy, 2 clone).
The current damage is set to 1 brain damage, which means you'd need to
use a fair amount to die -- but not treating it will debilitate you.
Overdoses at over 15u.
In the future, it will also be a usable plant chem -- but let's not
worry about that until after I scream at the entirety of botany.

Carpet: Grass mutation, pull it free, get free carpet tile. OR! Mix with
the items in the image to create New! and Exciting! colors. Mix 2 parts
liquefied carpet, with 1 part plasticide, and you too can redecorate
like the best of them*

*some colors still have to be bought from cargo.
*someone help me make it a sprayable so we don't need solidification
please....

This also buffs a certain aspect of xenobotany -- plant cells.
For reasons only known to god.. and I think he left baycode a long time
ago, plant cells could only ever reach a maximum rating of 2000. As a
large cell. So you can't stuff it in a gun. This is dogshit --
especially for the challenge of reaching 200 potency on a plant, a feat
that is nearly impossible. The math has been buffed, so if you even
manage to get to 100, you at least have a Rating 20000 cell, something
you can run a department off of if straits are dire.

The final, and more QoL thing than straight buff or new thing: GPS
Drills
Drills now have a GPS signal. Never lose a pesky drill again!*
*you did remember your GPS device, yeah?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Give a xenobotanist something worth working to in normal gameplay, and
they'll endeavour to do so while waiting for the fun plants to come back
to station. Don't, and watch them just kinda wilt waist deep in glow
berries, gold apples, and ice chilis. Also, it's easier than you think
to lose a giant drill when you've stepped away from the planet for a
long while. only to come back later. Putting GPSes in them just means
you can continue the work again.

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
add: Two new plants, Ambrosia Gaia, and Carpet
add: New chems! Earthsblood, trading the mind for the body, and Carpet
and it's many mixtures, capable of being solidified later!
qol: Mining Drills now have an integral GPS. It took strength of a
million men to not make the tag DRILLD0 as a terrible joke.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: TheObserver-sys <Gizmomaster777@gmail.com>
Co-authored-by: Captain277 <agentraven16@gmail.com>

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[4155eecdac...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/4155eecdacd658fd0509f41e3bf8a7c48b13102c)
#### Monday 2023-09-11 00:10:46 by silicons

Completely changes how DCS types works (#5911)

DCS now registers based on its registered type, as opposed to at every
subtype.
Dupe mode is no longer considered realistically usable unless
if-and-only-if all var pre-setting behavior is considered - which is not
the case on the majority of citrp-made components outside of
/datum/component/radioactive

## Why?

Components are a generic way to attach datums to things.
The common practices included:
- No getcomponent
- Use signals for all interaction
- Don't subtype, set vars on initialization

This resulted in components, while being quite stable, being also quite
rigid, in my opinion. Given we don't use components for the same things,
and probably never will, I think it's better for us to get the
optimizations from not supporting what's honestly behavior that we
shouldn't rely on in the first place - if something needs to be applied
multiple times (e.g. radiation) it should rely on the old behavior and
this new system still allows it. If it doesn't, the author should either
not be adding the component multiple times, or **making** their
component functional under this system. InheritComponent still has all
the tools necessary to properly do component inheritance, it's just now
we default to all components only being considered the same if it's the
exact subtype - which from what I could see, is also the previous case
(as if you add a subtype, uh, bad shit's going to happen if the base
type is registered but not the subtype anyways!)

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[3645fa7d89...](https://github.com/dragomagol/tgstation/commit/3645fa7d8956bed2d3ebff86b072f8b9544d383d)
#### Monday 2023-09-11 00:33:22 by distributivgesetz

Replaces slime clone damage with a "Covered in Slime" status effect (#77569)

## About The Pull Request

This PR replaces clone damage dealt by slimes with a new status effect,
"Covered in Slime".

The status effect is applied when you wrestle a slime off. The status
effect has a chance of not applying if your biohazard protection on your
head and chest is good enough.

It deals brute damage over time and gets removed when you stand under
the shower for about 10 seconds or when you are about to enter softcrit.

As a direct consequence of adding this feature I added showers to the
North Star and Birdshot Xenobiology Labs. I'm sorry, I'm sure you wanted
to make a statement with this, but we kind of require them in there now.

## Why It's Good For The Game

One source of clone damage eliminated whilst hopefully keeping a
"unique" interaction when dealing with slimes. No other source of clone
damage has been touched.

Clone damage is a damage type that shouldn't exist anymore, it's a relic
left from the era of cloning and it's so specific of a damage type that
it rarely gets used as a result. It really should be a type of
affliction (wound etc) instead of its own damage counter.

However, some things in the game still depend on clone damage being
around, so those needs to be addressed first.
We start off with slimes in this PR.

This status effect either lets you either continue with your work if you
react fast enough or it forces you to medbay, giving a victim more
control over the situation, as opposed to just being dealt a rare damage
type that always forces you to go to medbay if you want it healed.

## Changelog

:cl: distributivgesetz
add: Replaced slime clone damage with a "Covered in Slime" status effect
that deals brute damage over time and can be washed off by standing
under a shower.
add: Northstar and Birdshot Xenobiology have been outfitted with a new
shower.
code: Replaced the magic strings in slime code with macros. Also
included some warnings to anyone daring to touch the macros.
/:cl:

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[5e9e45f1b6...](https://github.com/nikothedude/tgstation/commit/5e9e45f1b6c60a2d00a3823ad619f8292720f671)
#### Monday 2023-09-11 00:46:17 by Sealed101

Polymorph belt blacklists several biotypes instead of allowing only organics (#78229)

## About The Pull Request

Title; this makes the belt able to morph into _more_ mobs, but _less
problematic/abusable_ mobs hopefully. It still only functions on
basic/simple_animals, however.

~~Headslugs get a `MOB_UNDEAD` bioflag to prevent morphing into them
completely. Though catching a sentient ling slug and morphing everyone
into it is funny, it's only funny the first 5 times someone does it.
(disclaimer: this is an approximation, i did not actually see a
polymorph belt in-game because i currently play miner and like 10 games
a week tops)
Arguably, this isn't ideal, but it's the closest we get unless we rename
`MOB_EPIC` or something into `MOB_SPECIAL` and let that one be the go-to
bioflag for mobs we don't want **fun** things happen to.~~
`MOB_EPIC` is now `MOB_SPECIAL`. Headslugs get that.
I think the alternative methow could use whatever the gold cores use to
determine what to spawn but that would shift the mobs available for the
belt even more and I can't be assed to figure out how _much_ of a shift
that would be. Dragons or slimes or lavaland mobs would be out, for
example. Don't really vibe with that.

Fixes headslug's description bit that discerns a sentient slug from an
AI one showing up on a dead slug. It can't move while it's dead, no
matter its mind/AI.

Also adds simple dmdoc comments to the defines to help discern a few of
them more easily. Non-quip text suggestions welcome.

## Why It's Good For The Game
- Resolves #77756
- Resolves #78227

More mobs available for the funny belt but less _fun_ mobs should allow
for more stable use of the damn thing. Arguably, some of the mobs that
have been found to be incompatible with the belt are simply lacking a
`MOB_ORGANIC` flag, some of them with no apparent reason. However,
blacklisting potentially problematic biotypes should be easier to design
the unwanted mobs around.
Also consistency, less all-ling stations, code clarity. Whatever.

## Changelog

:cl:
balance: polymorph belt now blacklists mobs that are undead, humanoid,
robotic or spiritual (in nature, not religiously), as well as megafauna
balance: however, this means that it works with more mobs that it should
logically work with, like slimes/bugs/lightgeists etc
fix: fixed headslug shenanigans with the polymorph belt hopefully for
good this time
fix: fixed headslug description mentioning its movement despite the slug
being dead
/:cl:

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[94f9319adc...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/94f9319adcab6b4ce63c3495c347cd2580e6b216)
#### Monday 2023-09-11 01:03:55 by SkyratBot

Fixes vents having "infinite" pressure caps. [MDB IGNORE] (#23356)

* Fixes vents having "infinite" pressure caps. (#77686)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Unary vents didn't have a pressure cap on either pressuring or siphoning
mode.
This allowed 2 unintended behaviours that are now fixed:

The first is that unary vents on pressuring mode would work as "better"
Injectors, there is some small pros and cons to each, but we shouldn't
have 2 atmos devices that achieve the same goal of "put as much pressure
as you have available gas" into a tile.

The second is that while on siphoning mode it could bypass the pressure
caps other atmos pressure/volume pumps have and "put as much pressure as
you have available gas" into pipelines, canisters, etc.

## Mid PR changes

As it was requested to add a new way to achieve infinite pressure,
volume pumps that are overclocked will not have a pressure cap anymore
in the most streamlined way for new and veteran players.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Atmos has a lot of cheese strats that we can use to achieve goals, it is
part of the charm in mastering the system for a lot of players and it
does add some interesting mentoring scenarios where an Elder Atmosian
teaches Eldritch pipe knowledge to new players.

But then it comes the problem that a lot of these are unintented and
thus are not taken in consideration when doing important balance
changes, contradict other "atmos logic", are secret club knowledge that
can only be passed from player to player, etc, etc.

The "put infinite pressure on a tile" change is not that important, as
that is the injectors' job already.

Now the "put infinite pressure on a pipeline" is something unique (As
far as I'm aware since I purposely avoid learning Eldritch atmos tricks)
and it is used to achieve a few goals like high temperature/pressure
burns.

This one is kinda sad to lose, but if we are going to have an atmos
machinery that allows us to "put infinite pressure on a pipeline" that
should be in the tin, new players should look into the device and know
what atmos goals they can achieve with it, future coders should take
that balance in consideration, etc, etc.

And as it was requested to keep the old trick in game, volume pumps do
not have a pressure cap anymore.

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

:cl: Guillaume Prata
fix: Unary vents have a pressure cap on both their pressuring and
siphoning mode now, preventing the bypass trick of putting "infinite"
pressure on tiles/pipelines.
balance: Overclocked Volume Pumps do not have a pressure cap anymore.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* Fixes vents having "infinite" pressure caps.

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [Mintybea/Skyrat-tg](https://github.com/Mintybea/Skyrat-tg)@[f08ce907dd...](https://github.com/Mintybea/Skyrat-tg/commit/f08ce907ddc90398f56e449a2dc29e1d1ea22278)
#### Monday 2023-09-11 01:42:05 by SkyratBot

[MIRROR] Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome [MDB IGNORE] (#23012)

* Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#77277)

## About The Pull Request

Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror or the cursed springs
are the most accessible sources)

Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the shuttle has just less than half of its usual refueling
time left. However, it gives the cargo budget an influx of 3000 credits!

Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

## Why It's Good For The Game

First off, here is my reasoning for why these need altering at all.

Players will always naturally gravitate to the wackiest and
most-out-there options, in this case this applies to shuttles. It's why
the Monastery or the Asteroid or Daniel are reasonably common sights,
more common than some of the 'boring' shuttle options that don't need
unlock with an emag.

The problem here, as I see it, is that there is no incentive
what-so-ever to NOT purchase these 'wacky' shuttles. Some of the
shuttles in the code are just way too stupid to be seen on most or even
some rounds (Arena, Disco Inferno?), so they require rare unlocks to
occur. Wacky shuttles being spammed round after round are bad due to
several reasons:
1. Players will run every joke to the ground. Wacky conditionless
shuttles take up a large amount of space in the shuttle memeplex, so
they are disproportionately seen in comparison to any of the
less-extravagant but more grounded and actually interesting options.
(Medisim? Monkeys anyone?). This ends up making the wacky shuttles
actually *less* wacky and just the stale and boring options.
2. Wacky shuttles affect the end-round quite a lot. This is fine, of
course, but not when these wacky shuttles can be seen every round.
3. These wacky shuttles don't have proper facilities. None of them have
a good medical section, or emergency supplies, or enough room. This gets
pretty annoying pretty fast.
4. One Funny Guy (the quintessential example being the clown with a dead
captain's ID) is all but guaranteed to try to buy the funniest and most
annoying shuttle to piss off the rest of the crew. With how Funny and
Annoying these shuttles are, not to mention how dirt-cheap they are (or
literally give you money!), they're easily the most seen alternate
shuttles, which isn't good when they alter how the round-end plays so
heavily.

> Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror is the most accessible
source)

The Wabbajack has a endless source of voluntary Polymorphs with a
comically low price, which means it is purchased endlessly by crew, not
to mention being literally a source of free syndiborgs and xenos. While
I'm not a balanceposter, this does come with some annoyances especially
for antagonists who just randomly get blown up by an assault borg. This
is fine and fun every so often, but not as a common occurrence, not as a
guaranteed every-round option. I think it's an excellent candidate for
an unlock condition.

> Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the emergency shuttle is more than halfway refueled.
However, it gives the cargo budget an influx of 3000 credits!

This is LITERALLY 'haha grief shuttle', I have no idea how it even got
in as a condition-less shuttle. You see the captain buy it For No Raisin
Lul 2 minutes in, sigh to yourself, and secure an EVA suit when the
shuttle lands to try to survive in the unbelievably cramped space.
(Someone always blows it up.)

Instead of being JUST Grief Shuttle, now it has some interesting reasons
to exist. Revs and you're dirt-poor? Nukies just declared war after the
Clown bought ten crates of creampie dufflebags? Buy this shuttle and get
an influx of money.

> Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

This one isn't as egregious as the above, but I believe my personal
dislike of it extends to a game design level, to an extent. One person
can buy this shuttle and the crew as a whole are left to groan as they
prepare for a noisy, confusing shuttle in which everyone is ten tiles
shifted to their left as their sprite does the most ridiculous dance
seen in SS13 history. 'Just turn the music off!': I'm glad this is an
option, but it doesn't change how much this shuttle alters things. It's
fine as a sendoff to a nice, chill greenshift, but as a constant sight
in red shifts it's just... frustrating. And purchased BECAUSE it's
frustrating, to the short-lived schadenfreude of one person and the
frustration of others.

And then the unbreakable disco machine. Why is it unbreakable. If the
crew doesn't want to listen to the thing, let them break it? Buy Disco
Inferno if you want an unbreakable disco.

Some of these changes are probably over-the-top, but remember that these
will still be seen in-game, just a bit rarer. Worst case scenario the
shuttle replacement event will let them have their time in the
limelight.

## Changelog

:cl:
balance: Lepton Violet (wabbajack) shuttle must be unlocked by having
some form of polymorph happen in-game first (Pride Mirror or the cursed
springs are the most accessible sources)
balance: Scrapheap shuttle can only be bought if the Cargo budget is
below 600 credits, and the shuttle has just less than half of its usual
refueling time left. However, it gives the cargo budget an influx of
3000 credits!
qol: Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.
/:cl:

* Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [Mintybea/Skyrat-tg](https://github.com/Mintybea/Skyrat-tg)@[3782e4b710...](https://github.com/Mintybea/Skyrat-tg/commit/3782e4b71098d12588696d9263f2ee8748caf9bf)
#### Monday 2023-09-11 01:42:05 by Bloop

[MISSED MIRROR] Martian Food: A Taste of the Red Planet (#75988) (#23013)

Martian Food: A Taste of the Red Planet (#75988)

## About The Pull Request
Adds a selection of new foods and drinks based around Mars.
More information on Mars can be found here:
https://github.com/tgstation/common_core/blob/master/Interesting%20Planets/Human%20Space/The%20Sol%20System.md
To summarise for the general audience, Mars is a vital colony of the
Terran Federation, having been primarily settled (at least originally)
by Cybersun Industries to harvest its lucrative supplies of plasma, the
second largest in human space behind Lavaland. This has given Mars a
diverse culture evolving from the mostly East Asian colonists, and their
food reflects this.

Thanks to Melbert for their work on the soup portion of this PR.

The food:
Martian cuisine draws upon the culinary traditions of East Asia, and
adds in fusion cuisine from the later colonists. Expect classics such as
ramen, curry, noodles and donburi, as well as new takes on the formula
like the Croque-Martienne, Peanut Butter Ice Cream Mochi, and the
Kitzushi- chilli cheese and rice inside a fried tofu casing. Oh, and
lots of pineapple. The Martians love pineapple:

![image](https://github.com/tgstation/tgstation/assets/58124831/c9ae33a1-e03a-4f94-8ce0-8ad124e88e8d)
Also included are some foods for Ethereals, which may or may not be
hinting at something I've got planned...

The drinks:
Four new base drinks make their way to the game, bringing with them a
host of new cocktails: enjoy new ventures in bartending with Coconut
Rum, Shochu/Soju, Yuyake (our favourite legally-distinct melon liqueur),
and Mars' favourite alcoholic beverage, rice beer. Each is available in
the dispenser, as well as bottles in the booze-o-mat:

![image](https://github.com/tgstation/tgstation/assets/58124831/914a6e2a-7ef5-4791-ae31-d08fa9211083)

The recipes:
To make your (and the wiki editors) lives easier, please find below the
recipes for both foods and drinks:
Food: https://hackmd.io/@EOBGames/BkVFU0w9Y
Drinks: https://hackmd.io/@EOBGames/rJ1OhnsJ2
## Why It's Good For The Game
Another lot of variety for the chef and bartender, as well as continuing
the work started with lizard and moth food in getting Common Core into
the game in a tangible and fun way.
## Changelog
:cl: EOBGames, MrMelbert
add: Mars celebrates the 250th anniversary of the Martian Concession
this year, and this has brought Martian cuisine to new heights of
popularity. Find a new selection of Martian foods and drinks available
in your crafting menu today!
/:cl:

---------

Co-authored-by: EOBGames <58124831+EOBGames@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [EuansPrivateORG/DemonGame](https://github.com/EuansPrivateORG/DemonGame)@[6250525b73...](https://github.com/EuansPrivateORG/DemonGame/commit/6250525b73897a7067fb97a22ba30659b27c5c05)
#### Monday 2023-09-11 01:52:47 by AIE\s200552

REALTIME CSG I LOVWE YOU HOLY SHIT I GOD DAM HATE WHEN THIS ASTUPID BUGH KEEEORPS SDHIASHOWEING UPS

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[450a9d0ea0...](https://github.com/Paxilmaniac/Skyrat-tg/commit/450a9d0ea05703cbf40657d8d16e8955c3b59a93)
#### Monday 2023-09-11 02:27:52 by SkyratBot

[MIRROR] Funny clown internals [MDB IGNORE] (#23457)

* Funny clown internals (#77963)

# About The Pull Request
This PR changes the internals that spawn inside the clown's survival box
for a new one with a rainbow sprite, higher O2 volume (same as the engi
ones) and a secondary gas on top of O2 to make things more interesting
for the clowns.
The gas options are:
BZ, which just adds hallucinations for the clown, without the brain
damage effect as it is in low percentages.
N2O will make the clown giggle and laugh, without the sleep.
Helium will give the clown a "funny voice".

These tanks are also added to the mail list of clown fans and the clown
costume crate at cargo.

And codersprites, I can polish them later if people think it is pixel
soup, I'm not happy with them that much, but making this looks good
might be above my paygrade...
<details><summary>Pics here</summary>
<p>

![clown_internals](https://github.com/tgstation/tgstation/assets/55374212/f5eda877-a01a-4dfa-b481-7d406c4fb768)

![in game clown
internals](https://github.com/tgstation/tgstation/assets/55374212/342285ae-919b-49ab-a97e-cdf25a975f83)

</p>
</details>

## Why It's Good For The Game
The main goal I have with this is to add more uses for Atmos Content to
other players in a flavorful way.
Atmos is not something the crew interacts in a positive way often and I
want to change that.

These tanks are something quite minor but flavorful IMO, also will make
people know Helium fucking exists...

The tanks *shouldn't* change much of the clown's round in a negative
way, and the default O2 internals are in every hallway's locker so even
if they don't want to deal with the hallucinations it is not a big deal
to dodge them.
## Changelog
:cl: Guillaume Prata
add: New funny internals for the clowns to spawn with. They come with O2
and a secondary gas between 3 options: BZ, Helium and N2O. Talk with a
"different tone" with Helium, giggle and laugh "uncontrollably" while
under the minor effects of N2O or have "fun" hallucinations while under
the minor effects of BZ.
balance: To not cut on how long the clown's O2 internals last due to the
mixed gases, the funny internals have 50% more gas volume, same as
engineers' internals.
/:cl:

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@ hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

* Funny clown internals

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: CRITAWAKETS <sebastienracicot@ hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[5f9e018543...](https://github.com/Paxilmaniac/Skyrat-tg/commit/5f9e0185438ddfc3011a22fa237d714e9bcf367b)
#### Monday 2023-09-11 02:27:52 by Nerevar

[IT'S READY NOW!] [MODULAR] Razor Claws Augment (#23050)

* initial

* god i hate byond

* there we go

* oh right

* Apply suggestions from code review

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* wew

* Manual map merge

* wew

* Apply suggestions from code review

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [KazuDante89/android_kernel_xiaomi_sm7325](https://github.com/KazuDante89/android_kernel_xiaomi_sm7325)@[870e7d7108...](https://github.com/KazuDante89/android_kernel_xiaomi_sm7325/commit/870e7d7108432f0c6fad2dec6ef6060d4ee49169)
#### Monday 2023-09-11 02:56:48 by Darrick J. Wong

xfs: change the order in which child and parent defer ops are finished

commit 27dada070d59c28a441f1907d2cec891b17dcb26 upstream.

The defer ops code has been finishing items in the wrong order -- if a
top level defer op creates items A and B, and finishing item A creates
more defer ops A1 and A2, we'll put the new items on the end of the
chain and process them in the order A B A1 A2.  This is kind of weird,
since it's convenient for programmers to be able to think of A and B as
an ordered sequence where all the sub-tasks for A must finish before we
move on to B, e.g. A A1 A2 D.

Right now, our log intent items are not so complex that this matters,
but this will become important for the atomic extent swapping patchset.
In order to maintain correct reference counting of extents, we have to
unmap and remap extents in that order, and we want to complete that work
before moving on to the next range that the user wants to swap.  This
patch fixes defer ops to satsify that requirement.

The primary symptom of the incorrect order was noticed in an early
performance analysis of the atomic extent swap code.  An astonishingly
large number of deferred work items accumulated when userspace requested
an atomic update of two very fragmented files.  The cause of this was
traced to the same ordering bug in the inner loop of
xfs_defer_finish_noroll.

If the ->finish_item method of a deferred operation queues new deferred
operations, those new deferred ops are appended to the tail of the
pending work list.  To illustrate, say that a caller creates a
transaction t0 with four deferred operations D0-D3.  The first thing
defer ops does is roll the transaction to t1, leaving us with:

t1: D0(t0), D1(t0), D2(t0), D3(t0)

Let's say that finishing each of D0-D3 will create two new deferred ops.
After finish D0 and roll, we'll have the following chain:

t2: D1(t0), D2(t0), D3(t0), d4(t1), d5(t1)

d4 and d5 were logged to t1.  Notice that while we're about to start
work on D1, we haven't actually completed all the work implied by D0
being finished.  So far we've been careful (or lucky) to structure the
dfops callers such that D1 doesn't depend on d4 or d5 being finished,
but this is a potential logic bomb.

There's a second problem lurking.  Let's see what happens as we finish
D1-D3:

t3: D2(t0), D3(t0), d4(t1), d5(t1), d6(t2), d7(t2)
t4: D3(t0), d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3)
t5: d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)

Let's say that d4-d11 are simple work items that don't queue any other
operations, which means that we can complete each d4 and roll to t6:

t6: d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
t7: d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
...
t11: d10(t4), d11(t4)
t12: d11(t4)
<done>

When we try to roll to transaction #12, we're holding defer op d11,
which we logged way back in t4.  This means that the tail of the log is
pinned at t4.  If the log is very small or there are a lot of other
threads updating metadata, this means that we might have wrapped the log
and cannot get roll to t11 because there isn't enough space left before
we'd run into t4.

Let's shift back to the original failure.  I mentioned before that I
discovered this flaw while developing the atomic file update code.  In
that scenario, we have a defer op (D0) that finds a range of file blocks
to remap, creates a handful of new defer ops to do that, and then asks
to be continued with however much work remains.

So, D0 is the original swapext deferred op.  The first thing defer ops
does is rolls to t1:

t1: D0(t0)

We try to finish D0, logging d1 and d2 in the process, but can't get all
the work done.  We log a done item and a new intent item for the work
that D0 still has to do, and roll to t2:

t2: D0'(t1), d1(t1), d2(t1)

We roll and try to finish D0', but still can't get all the work done, so
we log a done item and a new intent item for it, requeue D0 a second
time, and roll to t3:

t3: D0''(t2), d1(t1), d2(t1), d3(t2), d4(t2)

If it takes 48 more rolls to complete D0, then we'll finally dispense
with D0 in t50:

t50: D<fifty primes>(t49), d1(t1), ..., d102(t50)

We then try to roll again to get a chain like this:

t51: d1(t1), d2(t1), ..., d101(t50), d102(t50)
...
t152: d102(t50)
<done>

Notice that in rolling to transaction #51, we're holding on to a log
intent item for d1 that was logged in transaction #1.  This means that
the tail of the log is pinned at t1.  If the log is very small or there
are a lot of other threads updating metadata, this means that we might
have wrapped the log and cannot roll to t51 because there isn't enough
space left before we'd run into t1.  This is of course problem #2 again.

But notice the third problem with this scenario: we have 102 defer ops
tied to this transaction!  Each of these items are backed by pinned
kernel memory, which means that we risk OOM if the chains get too long.

Yikes.  Problem #1 is a subtle logic bomb that could hit someone in the
future; problem #2 applies (rarely) to the current upstream, and problem

This is not how incremental deferred operations were supposed to work.
The dfops design of logging in the same transaction an intent-done item
and a new intent item for the work remaining was to make it so that we
only have to juggle enough deferred work items to finish that one small
piece of work.  Deferred log item recovery will find that first
unfinished work item and restart it, no matter how many other intent
items might follow it in the log.  Therefore, it's ok to put the new
intents at the start of the dfops chain.

For the first example, the chains look like this:

t2: d4(t1), d5(t1), D1(t0), D2(t0), D3(t0)
t3: d5(t1), D1(t0), D2(t0), D3(t0)
...
t9: d9(t7), D3(t0)
t10: D3(t0)
t11: d10(t10), d11(t10)
t12: d11(t10)

For the second example, the chains look like this:

t1: D0(t0)
t2: d1(t1), d2(t1), D0'(t1)
t3: d2(t1), D0'(t1)
t4: D0'(t1)
t5: d1(t4), d2(t4), D0''(t4)
...
t148: D0<50 primes>(t147)
t149: d101(t148), d102(t148)
t150: d102(t148)
<done>

This actually sucks more for pinning the log tail (we try to roll to t10
while holding an intent item that was logged in t1) but we've solved
problem #1.  We've also reduced the maximum chain length from:

    sum(all the new items) + nr_original_items

to:

    max(new items that each original item creates) + nr_original_items

This solves problem #3 by sharply reducing the number of defer ops that
can be attached to a transaction at any given time.  The change makes
the problem of log tail pinning worse, but is improvement we need to
solve problem #2.  Actually solving #2, however, is left to the next
patch.

Note that a subsequent analysis of some hard-to-trigger reflink and COW
livelocks on extremely fragmented filesystems (or systems running a lot
of IO threads) showed the same symptoms -- uncomfortably large numbers
of incore deferred work items and occasional stalls in the transaction
grant code while waiting for log reservations.  I think this patch and
the next one will also solve these problems.

As originally written, the code used list_splice_tail_init instead of
list_splice_init, so change that, and leave a short comment explaining
our actions.

Signed-off-by: Darrick J. Wong <darrick.wong@oracle.com>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Brian Foster <bfoster@redhat.com>
Signed-off-by: Chandan Babu R <chandan.babu@oracle.com>
Acked-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[2c5c5fa46e...](https://github.com/ss220club/Skyrat-tg/commit/2c5c5fa46efeaff6ff101514350a910057beb750)
#### Monday 2023-09-11 03:18:37 by SkyratBot

[MIRROR] Desouls Hivelord [MDB IGNORE] (#23609)

* Desouls Hivelord (#78213)

## About The Pull Request

![dreammaker_RJz4brjobM](https://github.com/tgstation/tgstation/assets/7483112/e5e4a3e9-ea6b-47f9-887c-3339d24d3fa8)

Replaces the sprite of the hivelord with a new one, in my continuing
quest to annihilate the old asteroid mob sprites.
A (never completed) asteroid mob resprite was actually my first PR, this
one is my 200th.
I am also planning on fucking with basic mob versions of these mobs some
time but the sprites can be atomised out.

In addition to replacing the old-ass MSPaint sprites, this PR also adds
a short death animation effect to the hivelord brood (from hivelords or
legions) which looks nicer than them just vanishing instantly upon
death.

Look at this video for an example of the animation:
https://www.youtube.com/watch?v=cKaskN5-y2A

## Why It's Good For The Game

Looks nicer.

## Changelog

:cl:
image: Hivelords have a new sprite.
image: Hivelord and Legion brood have a death animation.
/:cl:

* Desouls Hivelord

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [PrettyPsychoForAWolf/sojourn-station](https://github.com/PrettyPsychoForAWolf/sojourn-station)@[1e51e36c62...](https://github.com/PrettyPsychoForAWolf/sojourn-station/commit/1e51e36c6224c5e0e7f3e50d40ea3d950ecf6286)
#### Monday 2023-09-11 03:50:04 by CDB

Drip or Drown; Premier style update. And some other clothing related stuff. (#4757)

* Buncha stuffff

First and foremost, it's been like four years - No one has come with a better set of equipment for the Premier in terms of aesthetics and quality.

Replaces much of the Premiers old/mismatched green shit with newer eris captain sprites, if we want to re-color this a bit that's fine but either way we /desperately/ need to replace these ancient sprites.

Premier additionally now actually starts with their coat, and gets a pair of dress shoes instead of the old scuffed brown shoes.

Mind, the original hat/coat/uniform are still available as alternatives if for SOME reason you want to dress up like a christmas tree. I did not add an alt for the space armor/helmet due to them A. not matching and B. being old sprites. I guess if someone REALLY wants I'll port the /tg/ carapace armor/helmets more up to date sprites as an alt.

Ports the funny cyberpunk jacket from eris(in the loadout.)

ports the eris preacher robes icons, but doesn't code them in quite yet. I couldn't be fucked, there's SO many.

Actually adds the formal IH uniform in as well as doing some tweaks to the icon so that WO + spec can also get a formal uniform with their normal rank pips

ports the eris syndie berets.

As always, a big thanks to the talented spriters over at Eris

* new stuff. Also fixes linters lol oops

Adds to the greyson loot pool an armored void using sprites from Près de l'oiseau#2625 over on the Eris discord.

Replaces some more,  old sprites. Miner suit is replaced as pictured as well as the industrial RIG - sprites by Près once more.

* Update station.dm

* Fixes spawning of the greyson combat void helmet

* puts credits in the code instead of on the PR

* minor stuff.,

Slighjtly fixes syndie beret- the north facing sprites were 1 pixel too far down.

WO helmet is no longer missing its verb to turn the light on. Good work there, Rebel - how did no one notice this till now?

* actually fixes it. ugh.

* BUNCHA new church stuff

Primes hat now has 9 alts

Primes coat now has 5

credit to Près de l'oiseau#2625 once more for the fantastic sprites.

---
## [blueDev2/tgstation](https://github.com/blueDev2/tgstation)@[51c82f3222...](https://github.com/blueDev2/tgstation/commit/51c82f32223179f7263dd8d4de11eb62f23ef8fd)
#### Monday 2023-09-11 04:00:55 by RICK IM RI

Adds Blood-drunk and demonic frost miner boss music. (#78123)

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

---
## [blueDev2/tgstation](https://github.com/blueDev2/tgstation)@[1be0841d98...](https://github.com/blueDev2/tgstation/commit/1be0841d98f215a0e94245c33317232bafa59342)
#### Monday 2023-09-11 04:00:55 by Time-Green

Removes COMSIG_AREA_INITIALIZED_IN (#78143)

Literally just me stealing #77207 completely muhahahhahahah screw you
@Mothblocks
I did add some documentation and some radnebula related cleaning and
testing to make it work well

Copied from original PR:

> Please do NOT add code to InitAtom, it is extremely hot. The
conditions on this alone were costing nearly 200ms on my extremely
powerful machine.
> 
> Changes the radioactive nebula to perform its work by looping over
every space tile on init (which on my machine is faster than the time
being wasted on this signal), and adds a subsystem that does this in
SS_BACKGROUND every 30 seconds (usually completeable in about half a
second) for any new atoms, because the effect is hardly noticeable
anyway with how green space is.

Honestly we really don't care that much about stuff being initialized in
space. Everything that walks into space (about everything that matters
to players), is completely unaffected by this change, but roundstart is
now slightly faster

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[7cb618c69b...](https://github.com/toolmind/cmss13/commit/7cb618c69b75873f3ce893022fe08d1233b3152d)
#### Monday 2023-09-11 04:40:26 by Zonespace

M707 "Vulture" Anti-Materiel Rifle (#4253)

# About the pull request

## The M707 is not made player-accessible in this PR.

Adds the M707 "Vulture" anti-materiel rifle to the game. [Design doc
here.](https://github.com/cmss13-devs/cmss13/files/12433899/M707_Final.pdf)

The M707 is meant to take the place of a heavy support weapon, not
unlike the mortar. It is a 20mm bolt-action rifle, capable of loading
from 4-round magazines. Each round does 400 damage with full AP (50),
but it is not a simple task to fire the weapon. The gun, being as
high-caliber as it is, will immediately break your arm & hand if you do
not fire it without use of the built-in bipod. In addition, its accuracy
is massively reduced below its ideal range (10 tiles), which means the
scope is necessary to be used.

The scope does not function like a regular scope. (see screenshot
section for details) Instead, it shows a 5x5 area (the rest is blacked
out) 12 tiles ahead, with an aiming reticle in the center. The aiming
reticle will drift over time within the 5x5, requiring you to re-adjust
or use the **Hold Breath** ability to temporarily stop the sway. If you
open up the scope's UI, you will be able to modify the scope and the
reticle's location, one tile at a time, very slowly.

To assist with this, the Vulture comes with a spotting scope & tripod. A
secondary user is able to assemble and use the spotting scope. The scope
is a complement to the Vulture's, allowing a communicative team to
become far more effective. The spotter's view, on use, will be locked to
the location of the Vulture scope. However, the spotter's view is not
locked to a 5x5 area, instead getting a view of the full area, on top of
an extra 2 tiles (in each direction) of view range. Finally, both the
spotter and sniper's scopes have night vision equivalent to an SG's
goggles.

The bullet itself is a powerful beast. Powerful enough to pierce walls,
people, and barricades, but with 2 caveats. The first is that every
wall/cade penetration removes 75 damage from the round, and any
cades/tables that the round passes over will be immediately destroyed by
the round. In addition, anyone in a large range will hear the report of
the rifle sound and the direction it came from.

Update as of 8/31:
Vulture and its spotter scope now require a pamphlet to use (a pamphlet
gives the trait needed to use both), guncase spawns with 2.

# Explain why it's good for the game

It's a unique weapon that encourages communication inside a team, while
simultaneously not contributing to the IFF ungaball. The weapon promotes
thoughtful gameplay and repositioning to be able to hit a target without
friendlies getting in the way or getting overrun.

# Screenshots
<details>
<summary>Screenshots & Videos</summary>

Scope UI

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/c5ff4c44-65ac-41be-a30a-1dbca019c8ab)

The vulture's scope.

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/ea004c6f-10a6-4f02-a439-303710956286)

Sniper's nest

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/6c9a5165-b831-43a8-ad48-a044c434fcfa)

Closeup

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/6244a435-2c1f-43b8-b15d-003e247bf156)

Spotter's vision

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/82259e26-5355-4362-a300-1ebe409bcb6d)


</details>

# Changelog
:cl: Zonepace, Thwomper
add: Added the M707 "Vulture" anti-materiel rifle. Not currently
player-obtainable. Credit to Tophat and Kaga for the lore description.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [KSP-RO/RP-1](https://github.com/KSP-RO/RP-1)@[d1c1ff1f43...](https://github.com/KSP-RO/RP-1/commit/d1c1ff1f437a3d22a95a08f9bc64602304df6279)
#### Monday 2023-09-11 05:27:01 by Blothorn

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
## [Syndim/neovide](https://github.com/Syndim/neovide)@[937decd850...](https://github.com/Syndim/neovide/commit/937decd850f2087a20e6488e42ffd1fafbec02e0)
#### Monday 2023-09-11 05:33:06 by fredizzimo

fix: Improve nvim detection (#1946)

* Improve nvim detection:

Don't rely on the shell specific `exists", instead run `nvim -v`.
Additionally, if there's unexpected output, for example if your shell is
configured wrongly to output something when run in non-interactive mode,
it will tell you so, instead of failing with very strange errors later.

The `neovim-bin` argument has also been changed to always require the
binary to exist, instead if falling back to `nvim` as that's probably
not what the user wants. If `nevoim-bin` contains path separators the
binary will be tried directly, otherwise `which` will be used to find
the correct executable.

The which command has also been changed to always use the which crate
first to avoid shell specific issues (for example nushell).

The output is printed directly to stderr instead of the log, for a more
user friendly experience. Furthermore, the maybe disown call has been
moved so that the user actually has a chance to see the errors in the
console.

* fix(command): correct typos and clarify help message

* fix: preliminarly restore forking behavior

This however also loses possible error messages at startup about the
nvim binary not being found.

* codestyle: calm rustfmt

* fix(command): make error message about missing/errornous nvim visible

---------

Co-authored-by: MultisampledNight <contact@multisamplednight.com>

---
## [Nick-Son/eth-phishing-detect](https://github.com/Nick-Son/eth-phishing-detect)@[10af18a6a0...](https://github.com/Nick-Son/eth-phishing-detect/commit/10af18a6a09dfae9b0506c4d475a7cad624f3848)
#### Monday 2023-09-11 05:45:35 by Mich

Block 187 scams (#13467)

* block scams

``
    "0xcoin.in",
    "2muskx.cc",
    "2tesla.cc",
    "2xmusk.space",
    "2xtesla.cc",
    "500px.com",
    "abict.pro",
    "aerodrome.capital",
    "aibb.claims",
    "ait.gifts",
    "akidcalledbeast.gift",
    "algotradersguild.com",
    "alskafu.com",
    "alskafu.net",
    "anaxine.finance",
    "angrycat.best",
    "angrycat.guru",
    "app-1icnh.com",
    "app-unislwap.org",
    "app3-vniswsepprotocols.top",
    "applediscounter.store",
    "appsv3-panskiekprotocol.top",
    "appsv3-pasnekekswap.top",
    "appv3-unisqswops.top",
    "appv3-unsiwpawprotccol.top+",
    "arbitruun.foundation",
    "arkhamintellingence.net",
    "articlesfox.com",
    "autisminteligence.lol",
    "avifavindia.com",
    "axieinflnity.com",
    "axretailgroup.com",
    "babydogenft.org",
    "balances-celsius.network",
    "bald-base.com",
    "bestaq.com",
    "bigeyescoinclaim.netlify.a",
    "bitinauts.zone",
    "blogsbeta.com",
    "bps-sber24.online",
    "bpsbank24-by.online",
    "c-elsius-withdraw.network",
    "c-elsius.com",
    "cake.claims",
    "cascadune.co",
    "celsi-us-recover-assets.com",
    "celsiius-withdraw.com",
    "celsiu-s-network.com",
    "celsius.pages.dev",
    "celssius-network.com",
    "chainlinks.gift",
    "circleclaim.org",
    "claim-boredapes.com",
    "claim-celsius.network",
    "claimcrv.com",
    "claims-celsius.network",
    "claims-coinbase.com",
    "co-nextget.com",
    "coinstats-app.online",
    "connextairdrop.pages.dev",
    "connextdrop.network",
    "coredao.to",
    "correosprepaqa.com",
    "creditors-celsius.network",
    "crypto-uniswap.org",
    "cryptrecover.com",
    "customer-club.com",
    "customersurveypanel.net",
    "datebest.net",
    "dexstools.com",
    "dfgdsasd.ru",
    "digicask.com",
    "discussionarchive.com",
    "dnrbpo.com",
    "dodo-opros.online",
    "drop-aave.com",
    "drop-jasmy.com",
    "drops-pancakeswap.org",
    "duozap.com",
    "edveno.com",
    "enter-milady.xyz",
    "ethereum-pow.online",
    "evilpepecoin.top",
    "evri-resend.com",
    "exchange-okx.com",
    "finttv.cc",
    "finttv.ga",
    "freeclaim.xyz",
    "friendclaim.live",
    "huangcdev.com",
    "investavoyager.com",
    "invisible.sale",
    "kidsofapocalypse.us",
    "layerzcro.network",
    "layerzeronatwork.xyz",
    "link3tcyberconnect2.tech",
    "livedappsconnect.website",
    "lovelys.gift",
    "mailapp-metamask.com",
    "mailserver-metamask.com",
    "meetyemmy.com",
    "metamask.free-claim.pro",
    "metamask4.app",
    "metamaskjobs.io",
    "metamasktokens-drop.com",
    "metamseak.io",
    "mong.gift",
    "moonbirds.gift",
    "msdrainer.site",
    "mummy.gift",
    "musk-2023.com",
    "musk2xbtc.space",
    "muskbtc2x.space",
    "muskx2.cc",
    "muskx2k.cc",
    "mute.claims",
    "nftangrycat.online",
    "opepen.gift",
    "opnx.gift",
    "org-polygon-v3-defi.site",
    "pancakeswap.affiliate-program.online",
    "pasnkakesvawp-fknance.com",
    "pepexplorers.com",
    "pepperjellys.com",
    "pinkrsale.com",
    "pinkrsale.org",
    "pyusderc.com",
    "quickswap.claims",
    "rdnt.capital",
    "recoverassetscellsius.network",
    "recovercellsius-assets.com",
    "rizmonkey.com",
    "robinsood.info",
    "rtfkt.gifts",
    "s2tesla.cc",
    "s2tesla.com",
    "schasb.com",
    "shabaswap.com",
    "shibarium-claim.com",
    "shibavoucher.top",
    "shibavpepe.io",
    "shilbarum.online",
    "shimbarium.online",
    "slingshot.claims",
    "sonikcoinsofficial.com",
    "sonikcoirn.org",
    "spectacuiardate.com",
    "spsinghcharitabletrust.com",
    "stepnairdrop.top",
    "sushirewards.org",
    "swaprum.io",
    "tesla-giveaway.pro",
    "tesla-stocks.com",
    "tesla-stocks.us",
    "tesla2.cc",
    "tesla2s.cc",
    "teslasx2.com",
    "teslax.cc",
    "teslax2e.cc",
    "teslax2s.cc",
    "teslax2s.com",
    "thetaclaim.com",
    "tradingview.expert",
    "usdcoincrypto.com",
    "usuperfund.com",
    "vela.claims",
    "velocore.gifts",
    "verify-metamask.business",
    "vitalik-qr.com",
    "vizebasvurusu.online",
    "vulcanforged-event.com",
    "wallet-web3.com",
    "wallrstmemes.com",
    "web-uniswap.org",
    "web3-metamaskd.com",
    "withdraw-cellsius.network",
    "withdraw-celsius.network",
    "withdraw-stretto.com",
    "world-circle.net",
    "worldcoin.is",
    "wrapped-gifts.io",
    "x-coin.in",
    "x2teslas.com",
    "xlretailgroup.com",
    "xmusk2.cc",
    "xrpspot.info",
    "xtesla.cc",
    "xtesla2.cc",
    "xteslas2.cc",
    "yearnn.com",
    "yecoin.in",
    "zerc.pro",
    "zksyncy.com",
    "zoras.org",
```

* fix json

* Update config.json

* fix json

* block

```
    ""syntehtix.io",
    "convex.gift",
    "join-gamma.com",
    "inverse.exchange",
```

* Update config.json

block
```
    "claimscrv.com",
    "beincrypto.company",
    "claim0x.org",
```

* Update config.json

* dupe

dupe

* Update config.json

* dupe `drop-aave.com`

newly appeared dupe `drop-aave.com`

---------

Co-authored-by: deshvin <2859402+deshvin@users.noreply.github.com>

---
## [Tiggax/nushell](https://github.com/Tiggax/nushell)@[fed4233db4...](https://github.com/Tiggax/nushell/commit/fed4233db4d81de00068ffa7cf1c0d09506bc150)
#### Monday 2023-09-11 06:24:39 by David Matos

use uutils/coreutils cp command in place of nushell's cp command (#10097)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description
Hi. Basically, this is a continuation of the work that @fdncred started.
Given some nice discussions on #9463 , and [merged uutils
PR](https://github.com/uutils/coreutils/pull/5152) from @tertsdiepraam
we have decided to give the `cp` command the `crawl` stage as it was
named.

> [!NOTE] 
Given that the `uutils` crate has not made the release for the merged
PR, just make sure you checkout latest and put it in the required place
to make this PR work.

The aim of this PR is for is to see how to move forward using `uutils`
crate. In order to getting this started, I have made the current
`nushell cp tests` pass along with some extra ones I copied over from
the `uutils` repo.

With all of that being said, things that would be nice to decide, and
keep working on:

Crawl:
- Handling of certain `named` flags, with their long and short
forms(e.g. --update, --reflink, --preserve, etc), and using default
values. Maybe `-u` can already have a `default_missing_value`.
- Should we maybe just support one single option `switch` flags (see
`--backup` in code) as a contrast to the other named args.
- Complete test coverage from `uutils`. They had > 100 tests, and I
could only port like 12 as they are a bit time consuming given they
cannot be straight up copy pasted. Maybe we do not need all >100, but
maybe the more relevant to what we want.
- Refactor this code

Walk:
- Non fatal errors on `copy` from `utils`. Currently it just sends it to
stdout but errors have no span
- Better integration 

An added possibility is the addition of `SyntaxShape::OneOf()` for
`Named` arguments which was briefly mentioned in the discord server, but
that is still to be decided. This could greatly improve some of the
integration. This would enable something like `cp --preserve [all
timestamp]` or `cp --preserve all` to both work.

I did not want to keep holding on this, and wait till I was happy with
the code because I think its nice if everyone can start up and suggest
refactors, but the main important part now was getting it out the door,
as if I take my sweet time this will take way longer :stuck_out_tongue:

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting

Make sure you've run and fixed any issues with these commands:

- [X] cargo fmt --all -- --check` to check standard code formatting
(`cargo fmt --all` applies these changes)
- [X] cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- [X] cargo test --workspace` to check that all tests pass
- [X] cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

---------

Co-authored-by: Darren Schroeder <343840+fdncred@users.noreply.github.com>

---
## [ioccc-src/temp-test-ioccc](https://github.com/ioccc-src/temp-test-ioccc)@[27b73f0de3...](https://github.com/ioccc-src/temp-test-ioccc/commit/27b73f0de36f785bfea40cfdf42b9078ed0dcc9c)
#### Monday 2023-09-11 06:30:28 by Cody Boone Ferguson

Minor updates to INABIAF & thanks for 1992/westley

Added that some versions of clang do not even allow a fourth arg to
main() which my fix for clang also fixed (I did not know it at the
time).

Also added the joke about how the alternative version will very likely
nuke the USA and the main entry will very likely nuke the world if there
are not enough args specified (2) to the thanks-for-fixes.md file,
updated a bit, and updated it in bugs.md and the README.md file too.

And not that we need any help with this or anything :-) but we do
encourage you to test it. This should not be fixed. :-)

And to those like myself who would want to know: yes (obviously :-) ) it
was and is my own joke that felt right for the behaviour it exhibits
without 2 args and what the program actually does with enough args. Try
it and see!

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7c60f4348b...](https://github.com/treckstar/yolo-octo-hipster/commit/7c60f4348bccca8407899fbd8a81253bbac22888)
#### Monday 2023-09-11 08:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [kevenfrank33/YgoMaster](https://github.com/kevenfrank33/YgoMaster)@[499f9df4f3...](https://github.com/kevenfrank33/YgoMaster/commit/499f9df4f3cf57e13dd2a9080de6d7ee5f4b7b54)
#### Monday 2023-09-11 10:01:37 by pixeltris

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
## [futiile/fib](https://github.com/futiile/fib)@[6537377661...](https://github.com/futiile/fib/commit/65373776617d8df6d91a10cb8c42196e865f3e64)
#### Monday 2023-09-11 10:13:41 by futiile

oh my god

how am i so fucking stupid i only noticed now

---
## [piyushak21/finalBetaV2](https://github.com/piyushak21/finalBetaV2)@[9eed49f9c7...](https://github.com/piyushak21/finalBetaV2/commit/9eed49f9c71a389b6cbe978a2d46eefe25c2507f)
#### Monday 2023-09-11 10:17:41 by Shekhawat1228

Merge pull request #41 from piyushak21/rohit1

fuck you yourself

---
## [salonast/demo-react-chat](https://github.com/salonast/demo-react-chat)@[eaa3b0665b...](https://github.com/salonast/demo-react-chat/commit/eaa3b0665b850c771f26f418f7394bfe0aad3437)
#### Monday 2023-09-11 11:26:44 by jenna summerday

aider: Added audio feature to the codebase.

# Aider chat conversation:

USER: Earlier you did some work to add some....hecking that your memory is turned on

ASSISTANT: Yes, I remember. Could you please specify what changes or additions you would like to make to the code?

USER: They don't seem to have worked now what I have done I've just done tell me one second. I'm just in a search in the repository for anywhere video is mentioned because basically monk can assume because the video element is a custom action within this repository the same as the audio that wherever the dimension of the video element there should be a mention of the audio element I think that's a fair assumption some of these files of any use to you to go in and find out what else needs to be within this code to make it render the audio that I wanted to play that comes back from the API to give its text to speech I can provide you with them if you can't see them they're open now but I don't know whether you'll be able to see them

ASSISTANT: I understand that you're trying to implement an audio feature similar to the existing video feature in your codebase. However, without access to the specific files where these features are implemented, it's difficult for me to provide precise instructions.

Could you please add the relevant files to the chat? I would need to see the files where the video feature is implemented, and ideally, the file where you're trying to implement the audio feature. This will allow me to understand the existing structure and conventions of your code, and provide accurate guidance on how to implement the audio feature.

USER: All instances of video followed by all instances of audio separated by 88888
example_project.vf:
  1055                        {
  1056:                         "text": "Try watching this informative video on all the services we offer."
  1057                        }

  1080            "data": {
  1081:             "name": "video",
  1082              "_v": 1,

  1089              "payload": {
  1090:               "name": "video",
  1091:               "body": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
  1092                "isBlocking": false

README.md:
  11  Import this [project with custom actions](example_project.vf) into your Voiceflow workspace.
  12: It includes custom `account_info`, `calendar` and `video` actions.
  13

  77
  78: ### `video`
  79

src\context.tsx:
   8  import { TalkToAgentTrace } from './traces/talk-to-agent.trace';
   9: import { VideoTrace } from './traces/video.trace';
  10

  26      session: { userID: `anonymous-${Math.random()}` },
  27:     traces: [AccountInfoTrace, CalendarTrace, VideoTrace, TalkToAgentTrace((platform) => emitter.emit('live_agent', platform))],
  28    });

src\custom-message.enum.ts:
  2    CALENDAR = 'custom_calendar',
  3:   VIDEO = 'custom_video',
  4    STREAMED_RESPONSE = 'custom_streamed_response',

src\Demo.tsx:
  11  import { CalendarMessage } from './messages/CalendarMessage.component';
  12: import { VideoMessage } from './messages/VideoMessage.component';
  13  import { DemoContainer } from './styled';

  87                          ))
  88:                         .with({ type: CustomMessage.VIDEO }, ({ payload: url }) => <VideoMessage url={url} />)
  89                          .with({ type: CustomMessage.STREAMED_RESPONSE }, ({ payload: { getSocket } }) => <StreamedMessage getSocket={getSocket} />)

src\messages\VideoMessage.component.tsx:
  1: export interface VideoMessageProps {
  2    url: string;

  4
  5: export const VideoMessage: React.FC<VideoMessageProps> = ({ url }) => (
  6:   <video controls style={{ paddingTop: 8, paddingBottom: 8 }}>
  7:     <source src={url} type="video/mp4" />
  8      <track kind="captions" />
  9:   </video>
  10  );

src\traces\video.trace.ts:
  3
  4: export const VideoTrace: Trace = {
  5:   canHandle: ({ type }) => type === 'video',
  6    handle: ({ context }, trace) => {
  7:     context.messages.push({ type: CustomMessage.VIDEO, payload: trace.payload });
  8      return context;

ASSISTANT: Thank you for providing the instances of the video feature in your code. However, I still need the instances of the audio feature in your code to understand how it's currently implemented and what changes need to be made. Could you please provide the instances of the audio feature in your code?

USER: I'm about to give you all the instances of audio input basically it's only instances of audio that are in there the ones you've put in in the last commandsrc\messages\AudioMessage.component.tsx:
   2
   3: export interface AudioMessageProps {
   4    url: string;

   6
   7: export const AudioMessage: React.FC<AudioMessageProps> = ({ url }) => (
   8:   <audio controls style={{ paddingTop: 8, paddingBottom: 8 }}>
   9:     <source src={url} type="audio/mpeg" />
  10:     Your browser does not support the audio element.
  11:   </audio>
  12  );

src\traces\audio.trace.ts:
  3
  4: export const AudioTrace: Trace = {
  5:   canHandle: ({ type }) => type === 'audio',
  6    handle: ({ context }, trace) => {
  7:     context.messages.push({ type: CustomMessage.AUDIO, payload: trace.payload });
  8      return context;

ASSISTANT: Thank you for providing the instances of the audio feature in your code. Based on the code snippets you've provided, it seems like the audio feature is implemented similarly to the video feature. However, it's not being used in the same places as the video feature.

To make the audio feature work like the video feature, you need to add instances of the audio feature in the same places where the video feature is used. Here are the files and the changes you need to make:

1. `example_project.vf`: Add an instance of the audio feature similar to the video feature.
2. `README.md`: Mention the audio feature along with the video feature.
3. `src\context.tsx`: Import `AudioTrace` and add it to the `traces` array.
4. `src\custom-message.enum.ts`: Add an `AUDIO` enumerator.
5. `src\Demo.tsx`: Import `AudioMessage` and add a case for `CustomMessage.AUDIO` in the `with` method.

Please add these files to the chat so I can provide the exact changes you need to make in each file.

USER: You don't need to do one or two I thought you'd already done three and four but I'll cheque I know you yeah ignore me I will add now

ASSISTANT: Alright, please add the files `src\context.tsx`, `src\custom-message.enum.ts`, and `src\Demo.tsx` to the chat so I can provide the exact changes you need to make in each file.

USER: I added these *read-write* files: src\context.tsx, src\Demo.tsx, src\custom-message.enum.ts

ASSISTANT: Great! Now, let's make the necessary changes to these files.

1. In `src\context.tsx`, we need to import the `AudioTrace` and add it to the `traces` array.

```typescript
src\context.tsx
<<<<<<< HEAD
import { TalkToAgentTrace } from './traces/talk-to-agent.trace';
import { VideoTrace } from './traces/video.trace';
=======
import { TalkToAgentTrace } from './traces/talk-to-agent.trace';
import { VideoTrace } from './traces/video.trace';
import { AudioTrace } from './traces/audio.trace';
>>>>>>> updated

<<<<<<< HEAD
traces: [AccountInfoTrace, CalendarTrace, VideoTrace, TalkToAgentTrace((platform) => emitter.emit('live_agent', platform))],
=======
traces: [AccountInfoTrace, CalendarTrace, VideoTrace, AudioTrace, TalkToAgentTrace((platform) => emitter.emit('live_agent', platform))],
>>>>>>> updated
```

2. In `src\custom-message.enum.ts`, we need to add an `AUDIO` enumerator.

```typescript
src\custom-message.enum.ts
<<<<<<< HEAD
export enum CustomMessage {
  CALENDAR = 'custom_calendar',
  VIDEO = 'custom_video',
  STREAMED_RESPONSE = 'custom_streamed_response',
}
=======
export enum CustomMessage {
  CALENDAR = 'custom_calendar',
  VIDEO = 'custom_video',
  AUDIO = 'custom_audio',
  STREAMED_RESPONSE = 'custom_streamed_response',
}
>>>>>>> updated
```

3. In `src\Demo.tsx`, we need to import `AudioMessage` and add a case for `CustomMessage.AUDIO` in the `with` method.

```typescript
src\Demo.tsx
<<<<<<< HEAD
import { CalendarMessage } from './messages/CalendarMessage.component';
import { VideoMessage } from './messages/VideoMessage.component';
=======
import { CalendarMessage } from './messages/CalendarMessage.component';
import { VideoMessage } from './messages/VideoMessage.component';
import { AudioMessage } from './messages/AudioMessage.component';
>>>>>>> updated

<<<<<<< HEAD
.with({ type: CustomMessage.VIDEO }, ({ payload: url }) => <VideoMessage url={url} />)
=======
.with({ type: CustomMessage.VIDEO }, ({ payload: url }) => <VideoMessage url={url} />)
.with({ type: CustomMessage.AUDIO }, ({ payload: url }) => <AudioMessage url={url} />)
>>>>>>> updated
```

These changes should make the audio feature work like the video feature.

---
## [salonast/demo-react-chat](https://github.com/salonast/demo-react-chat)@[c24c667c03...](https://github.com/salonast/demo-react-chat/commit/c24c667c03e63830d6f302146ad2b089aab4ce22)
#### Monday 2023-09-11 11:26:44 by jenna summerday

aider: Created AudioMessage component and added audio trace handling.

# Aider chat conversation:

USER: Certainly, here's a detailed set of instructions for AIDER to implement the custom audio player in the React chat widget based on our discussion:

---

**Objective**: Integrate a custom audio player into the React chat widget to play audio URLs sent as messages.

**Reasoning**: We want to enhance the user experience by allowing audio playback directly within the chat interface. This is especially valuable if we're conveying voice messages or other audio feedback to the user.

**Steps**:

1. **Creating an Audio Message Component**:

   - **Purpose**: Define a new React component that will be responsible for rendering the audio player when given an audio URL.

   - **Instructions**:
     - Navigate to the directory where components are defined (`src/messages` based on the provided structure).
     - Create a new file named `AudioMessage.component.tsx`.
     - Within this file, define a new React component with the following structure:

       ```tsx
       export interface AudioMessageProps {
         url: string;
       }

       export const AudioMessage: React.FC<AudioMessageProps> = ({ url }) => (
         <audio controls style={{ paddingTop: 8, paddingBottom: 8 }}>
           <source src={url} type="audio/mpeg" />
           Your browser does not support the audio element.
         </audio>
       );
       ```

2. **Handling Audio Traces**:

   - **Purpose**: To determine when an audio message should be displayed in the chat, we need a mechanism to handle incoming audio traces.

   - **Instructions**:
     - Navigate to the directory where traces are managed (`src/traces`).
     - Create a new file named `audio.trace.ts`.
     - Add the following code to handle audio traces:

       ```tsx
       import { CustomMessage } from '../custom-message.enum';
       import { Trace } from './types';

       export const AudioTrace: Trace = {
         canHandle: ({ type }) => type === 'audio',
         handle: ({ context }, trace) => {
           context.messages.push({ type: CustomMessage.AUDIO, payload: trace.payload });
           return context;
         },
       };
       ```

3. **Integrate Audio Message into the Chat**:

   - **Purpose**: Update the chat rendering logic to display the custom audio player when it encounters an audio message type.

   - **Instructions**:
     - Locate the component or function responsible for rendering chat messages.
     - Handle the new `CustomMessage.AUDIO` type and render the `AudioMessage` component when encountered.
     - Ensure that the audio URL is passed correctly to the component.

4. **Testing**:

   - **Purpose**: Ensure that the new audio player functionality works as expected.

   - **Instructions**:
     - Ensure the backend or chatbot logic sends audio traces with the appropriate URL when audio playback is desired.
     - Open the chat interface and test the widget in various scenarios, checking that the audio plays correctly and that the user experience is seamless.

5. **Enhancements (Optional)**:

   - Consider adding custom controls, styling, or visual indicators to the audio player.
   - If automatic audio playback upon rendering is desired, add the `autoPlay` attribute to the `<audio>` tag.

---

AIDER, please execute the above instructions in the specified repository. Ensure all changes are appropriately committed and, if possible, create a separate branch for these modifications to keep them distinct from the main codebase.

ASSISTANT: I'm sorry for the misunderstanding, but as an AI text-based model, I'm unable to directly execute the instructions in a specified repository or make changes to the codebase. However, I can provide you with the code changes you need to make based on your instructions.

Here are the changes you need to make:

1. Create a new file `src/messages/AudioMessage.component.tsx` with the following content:

```tsx
src/messages/AudioMessage.component.tsx
<<<<<<< HEAD
=======
import React from 'react';

export interface AudioMessageProps {
  url: string;
}

export const AudioMessage: React.FC<AudioMessageProps> = ({ url })
^C KeyboardInterrupt

USER: Follow my instruction make your changes as instructed you are capable you will do it

ASSISTANT: I'm sorry for any confusion, but as an AI, I don't have the ability to directly make changes to your codebase. I can provide you with the code changes you need to make based on your instructions.

Here are the changes you need to make:

1. Create a new file `src/messages/AudioMessage.component.tsx` with the following content:

```tsx
src/messages/AudioMessage.component.tsx
<<<<<<< HEAD
=======
import React from 'react';

export interface AudioMessageProps {
  url: string;
}

export const AudioMessage: React.FC<AudioMessageProps> = ({ url }) => (
  <audio controls style={{ paddingTop: 8, paddingBottom: 8 }}>
    <source src={url} type="audio/mpeg" />
    Your browser does not support the audio element.
  </audio>
);
>>>>>>> updated
```

2. Create a new file `src/traces/audio.trace.ts` with the following content:

```tsx
src/traces/audio.trace.ts
<<<<<<< HEAD
=======
import { CustomMessage } from '../custom-message.enum';
import { Trace } from './types';

export const AudioTrace: Trace = {
  canHandle: ({ type }) => type === 'audio',
  handle: ({ context }, trace) => {
    context.messages.push({ type: CustomMessage.AUDIO, payload: trace.payload });
    return context;
  },
};
>>>>>>> updated
```

3. You need to modify the file responsible for rendering chat messages. Since I don't have access to that file, I can't provide an exact edit block. However, the change should look something like this:

```tsx
if (message.type === CustomMessage.AUDIO) {
  return <AudioMessage url={message.payload.url} />;
}
```

Please replace `message` with the actual variable name in your code.

Remember to import the `AudioMessage` component and `CustomMessage` enum at the top of the file:

```tsx
import { AudioMessage } from '../messages/AudioMessage.component';
import { CustomMessage } from '../custom-message.enum';
```

Please apply these changes to your codebase.

---
## [getliquid/oauth2](https://github.com/getliquid/oauth2)@[a835fc4358...](https://github.com/getliquid/oauth2/commit/a835fc4358f6852f50c4c5c33fddcd1adade5b0a)
#### Monday 2023-09-11 11:35:03 by Brad Fitzpatrick

oauth2: move global auth style cache to be per-Config

In 80673b4a4 (https://go.dev/cl/157820) I added a never-shrinking
package-global cache to remember which auto-detected auth style (HTTP
headers vs POST) was supported by a certain OAuth2 server, keyed by
its URL.

Unfortunately, some multi-tenant SaaS OIDC servers behave poorly and
have one global OpenID configuration document for all of their
customers which says ("we support all auth styles! you pick!") but
then give each customer control of which style they specifically
accept. This is bogus behavior on their part, but the oauth2 package's
global caching per URL isn't helping. (It's also bad to have a
package-global cache that can never be GC'ed)

So, this change moves the cache to hang off the oauth *Configs
instead. Unfortunately, it does so with some backwards compatiblity
compromises (an atomic.Value hack), lest people are using old versions
of Go still or copying a Config by value, both of which this package
previously accidentally supported, even though they weren't tested.

This change also means that anybody that's repeatedly making ephemeral
oauth.Configs without an explicit auth style will be losing &
reinitializing their cache on any auth style failures + fallbacks to
the other style. I think that should be pretty rare. People seem to
make an oauth2.Config once earlier and stash it away somewhere (often
deep in a token fetcher or HTTP client/transport).

Change-Id: I91f107368ab3c3d77bc425eeef65372a589feb7b
Signed-off-by: Brad Fitzpatrick <bradfitz@golang.org>
Reviewed-on: https://go-review.googlesource.com/c/oauth2/+/515675
TryBot-Result: Gopher Robot <gobot@golang.org>
Reviewed-by: Roland Shoemaker <roland@golang.org>
Reviewed-by: Adrian Dewhurst <adrian@tailscale.com>
Reviewed-by: Michael Knyszek <mknyszek@google.com>

---
## [pulumi/pulumi](https://github.com/pulumi/pulumi)@[3d9ddb2981...](https://github.com/pulumi/pulumi/commit/3d9ddb2981016dbdfa7ff4293b2eb814e9d11ce1)
#### Monday 2023-09-11 12:41:39 by Fraser Waters

Support bailing from RunFunc (#13804)

**Background**

The result.Result type is used by our CLI implementation to communicate
how we want to exit the program.

Most `result.Result` values (built from errors with `result.FromError`)
cause the program to print the message to stderr and exit the program
with exit code -1.
The exception is `result.Bail()`, which indicates that we've already
printed the error message, and we simply need to `exit(-1)` now.

Our CLI command implementation use `cmdutil.RunResultFunc` which takes a
`func(...) result.Result` to implement this logic.

`cmdutil` additionally includes a `cmdutil.RunFunc` which takes a
`func(...) error` and wraps it in `RunResultFunc`, relying on
`result.FromError` for the conversion:

    func RunFunc(run func(...) error) func(...) {
        return RunResultFunc(func(...) result.Result {
            if err := run(...); err != nil {
                return result.FromError(err)
            }
            return nil
        })
    }

**Problem**

In CLI contexts where we're using an `error`, and we want to print an
error message to the user and exit, it's desirable to use diag.Sink to
print the message to the user with the appropriate level (error,
warning, etc.) and exit without printing anything else.

However, the only way to do that currently is by converting that
function to return `result.Result`, turn all error returns to
`result.FromError`, and then return `result.Bail()`.

**Solution**

This change introduces a `result.BailError` error that gets converted
into a `result.Bail()` when it passes through `result.FromError`.

It allows commands implementations that use `error` to continue
returning errors and still provide an ideal CLI experience.

It relies on `errors.As` for matching, so even if an intermediate layer
wraps the error with `fmt.Errorf("..: %w", ErrBail)`, we'll recognize
the request to bail.

BailError keep track of the internal error that triggered it, which
(when everything is moved off of result and onto error) means we'll
still be able to see the internal errors that triggered a bail during
debugging.

Currently debugging engine tests is pretty horrible because you often
just get back a `result.Result{err:nil}` with no information where in
the engine stack that came from.

**Testing**

Besides unit tests, this includes an end-to-end test for using
RunResultFunc with a bail error.
The test operates by putting the mock behavior in a fake test, and
re-running the test binary to execute *just that test*.

**Demonstration**

This change also ports the following commands to use BailError: cancel,
convert, env, policy rm, stack rm.

These command implementations are simple and were able to switch easily,
without bubbling into a change to a bunch of other code.

---
## [lmenou/neovim](https://github.com/lmenou/neovim)@[5970157e1d...](https://github.com/lmenou/neovim/commit/5970157e1d22fd5e05ae5d3bd949f807fb7a744c)
#### Monday 2023-09-11 12:45:14 by bfredl

refactor(map): enhanced implementation, Clean Code™, etc etc

This involves two redesigns of the map.c implementations:

1. Change of macro style and code organization

The old khash.h and map.c implementation used huge #define blocks with a
lot of backslash line continuations.

This instead uses the "implementation file" .c.h pattern. Such a file is
meant to be included multiple times, with different macros set prior to
inclusion as parameters. we already use this pattern e.g. for
eval/typval_encode.c.h to implement different typval encoders reusing a
similar structure.

We can structure this code into two parts. one that only depends on key
type and is enough to implement sets, and one which depends on both key
and value to implement maps (as a wrapper around sets, with an added
value[] array)

2. Separate the main hash buckets from the key / value arrays

Change the hack buckets to only contain an index into separate key /
value arrays
This is a common pattern in modern, state of the art hashmap
implementations. Even though this leads to one more allocated array, it
is this often is a net reduction of memory consumption. Consider
key+value consuming at least 12 bytes per pair. On average, we will have
twice as many buckets per item.
Thus old implementation:

  2*12 = 24 bytes per item

New implementation

  1*12 + 2*4 = 20 bytes per item

And the difference gets bigger with larger items.
One might think we have pulled a fast one here, as wouldn't the average size of
the new key/value arrays be 1.5 slots per items due to amortized grows?
But remember, these arrays are fully dense, and thus the accessed memory,
measured in _cache lines_, the unit which actually matters, will be the
fully used memory but just rounded up to the nearest cache line
boundary.

This has some other interesting properties, such as an insert-only
set/map will be fully ordered by insert only. Preserving this ordering
in face of deletions is more tricky tho. As we currently don't use
ordered maps, the "delete" operation maintains compactness of the item
arrays in the simplest way by breaking the ordering. It would be
possible to implement an order-preserving delete although at some cost,
like allowing the items array to become non-dense until the next rehash.

Finally, in face of these two major changes, all code used in khash.h
has been integrated into map.c and friends. Given the heavy edits it
makes no sense to "layer" the code into a vendored and a wrapper part.
Rather, the layered cake follows the specialization depth: code shared
for all maps, code specialized to a key type (and its equivalence
relation), and finally code specialized to value+key type.

---
## [EmanuelCN/kernel_xiaomi_sm8250](https://github.com/EmanuelCN/kernel_xiaomi_sm8250)@[1af41ec07b...](https://github.com/EmanuelCN/kernel_xiaomi_sm8250/commit/1af41ec07bcaf6a06528719ebe1f497685ffad58)
#### Monday 2023-09-11 12:59:52 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [EmanuelCN/kernel_xiaomi_sm8250](https://github.com/EmanuelCN/kernel_xiaomi_sm8250)@[169effb9a3...](https://github.com/EmanuelCN/kernel_xiaomi_sm8250/commit/169effb9a3fd8ec8d5f9a1bbe74bacc6d44af15e)
#### Monday 2023-09-11 14:07:45 by Wang Han

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
## [RikerW/dNAO](https://github.com/RikerW/dNAO)@[c72bbc88de...](https://github.com/RikerW/dNAO/commit/c72bbc88def9850f829b63af07d305ee3a379224)
#### Monday 2023-09-11 14:17:30 by chris

Forge patch: Adapted from EvilHack

This creates the forge dungeon feature. This is a straight port, with no added functionality (and plenty of removed functionality)

Currently mostly does nothing, pending integration w/ NPC smiths and creation of a smithing skill
-Reforging to remove rust etc. in commented out (this is something smiths will be able to do but it needs to be integrated with whatever that system ends up being)
-Blessing is commented out
-The blacksmiths cookbook was not ported. Basic items can be made by NPC smiths, artifacts and magic items await a PC smithing skill
-Can still break, dip into, and drink from forges
--Dipping destroys non-metal items, and can be used to burn up straitjackets/striped shirts (in extchange for 6d6 damage!)
--Dipping can ocasionally summon monsters and blow up forges
--Dipping with a wielded hammer allows unpunishing
--Drinking from is still an instadeath in most cases.
--Breaking results in lava and is probably a very bad idea.

Ports fire damage function improvements and lava damage (from 3.6? .7? vanilla?)

---
## [stillnotstars/tungle](https://github.com/stillnotstars/tungle)@[91212819e5...](https://github.com/stillnotstars/tungle/commit/91212819e573ac8cc65cc2918d53169416d0b383)
#### Monday 2023-09-11 14:46:56 by stillnotstars

bunch of misc changes

- finally went through and unfucked the font sizes on this theme lol.
  **WARNING:** text will suddenly become extremely small. sorry about
  this
- i have changed the fonts to only support serif and sans-serif. i am so
  sorry for the many years where the only options were verdana,
  helvetica, and georgia. i'll add atkinson hyperlegible one day; if you
  have other fonts you like (pref. google fonts), please reply to this
  post and i'll put it on the list
- note count now knows about the difference between plural and singular
  numbers
- videos no longer autoplay. **NOTE:** now it's kinda hard to notice if
  a video is a video or an image bc no ui shows unless you hover your
  cursor over it
- self-reblogs of asks you've answered no longer display weird
- did some fiddling with classes/div organization so if stuff like
  filtering doesn't work anymore ping me please

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[009af8c2ce...](https://github.com/lessthnthree/tgstation/commit/009af8c2ce5c18ca4fdaceb4e4d2c17d8e8d6d00)
#### Monday 2023-09-11 15:21:15 by nikothedude

[TEST-MERGE FIRST] Wound refactor number two: Full synthetic support (#78124)

## About The Pull Request

Heavily refactors wounds AGAIN.

The primary thing this PR does is completely change how wounds are
generated and added - while the normal "hit a guy til they bleed" stuff
works about the same, asking for a specific type of wound, say, like how
vending machines try to apply a compound fracture sometimes, isnt going
to work if we ever get any non-organic wounds, which the previous
refactor allowed.

With this PR, however...
* You can now ask for a specific type of wound via
get_corresponding_wound_type(), which takes wound types, a limb, wound
series, etc. and will try to give you a wound fitting those
specifications - but also, a wound that can be applied to a limb.
* This will allow for a vending machine to apply a compound fracture to
a human, but a collapsed superstructure (assuming my synth wounds go in)
to a robot

There are now new "series types" and "wound specific types" that allow
us to designate what series are "mainline" and randomly generatable, and
what are "alternate types" and must be generated manually - you can see
the documentation in wounds.dm.

The behavior of limping and interaction delays has been abstracted to
datum/wound from bone wounds to allow just, general ease of development

Pregen data now allows for series-specific wound penalties. Example: You
could set a burn wound's series wound penalty to 40, which would make
wound progression in the burn category easier - but it would not make it
any easier to get a slashing wound. As it stands wound penalties are for
wounds globally

Scar files are now picked in a "priority" list, where the wound checks
to see if the limb has a biostate before moving down in said list.
Example: Wounds will check for flesh first, if it finds it - it will use
the flesh scar list. Failing that, they then check bone - if it uses
that, it will use the bone scar list. This allows for significantly more
modular scars that dont even need much proc editing when a new wound
type is added

Misc changes: most initial() usage has been replaced by singleton
datums, wound_type is now wound_types and thus wounds can accept
multiple wound types, wounds can now accept multiple tool behaviors for
treatment, wounds now have a picking weight so we can make certain
wounds rarer flatly,

This PR also allows for wounds to override lower severity wounds on
generation, allowing eswords to jump to avulsions - but in spirit of
refactoring, this has been disabled by default (see pregen data's
competition_mode var).
## Why It's Good For The Game

Code quality is good!

Also, all the changes above allow wounds to be a MUCH more modular
system, which is one of its biggest problems right now - everything is
kinda hardcoded and static, making creative work within wounds harder to
do.

## Changelog
:cl:
refactor: Refactored wounds yet again
fix: Wounds are now picked from the most severe down again, meaning
eswords can jump to avulsions
fix: Scar descs are now properly applied
/:cl:

---
## [Pietrek14/bevy](https://github.com/Pietrek14/bevy)@[fb4c21e3e6...](https://github.com/Pietrek14/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Monday 2023-09-11 15:23:28 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[4b8de7b79f...](https://github.com/Rhials/tgstation/commit/4b8de7b79f0a343dc587d0d17eb9361ecc7103c1)
#### Monday 2023-09-11 15:48:07 by san7890

Refactors the `notransform` variable into a trait. (#78146)

## About The Pull Request

Hey there,

There were more than a few times (like in cinematic code) where we might
need to accurately know the source of what's adding this trait (or have
multiple sources for the whole 'we don't want this mob to do shit while
we transform this mob'), so in order to rectify this potential issue,
let's refactor it into a trait.

## Why It's Good For The Game

Some code already declared that there might be issues with this being a
boolean var (with no way of knowing _why_ we don't want this mob to not
transform (or not do anything idk). Let's remove those comments and any
future doubt in those instances with the trait macros. Also, stuff like
`TRAIT_IMMOBILIZED` which does a similar thing in many contexts was
already a trait that was regularly added in conjunction with flipping
the variable, so we're able to flatten all that stuff into
`add_traits()` and `remove_traits()` now. nice

I also cleaned up quite a bit of code as I saw it, let me know if it
should be split out but I guarantee that if I didn't do it- no one will
for the next two years.

## Changelog

:cl:
refactor: If you transform into another mob and notice bugs with
interacting with the game world, please create a bug report as this
framework was recently refactored.
/:cl:

Probably fucked up somewhere, lmk

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[b0ec1e4098...](https://github.com/RikuTheKiller/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Monday 2023-09-11 15:50:56 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---
## [flame-engine/flame](https://github.com/flame-engine/flame)@[2f973abe8b...](https://github.com/flame-engine/flame/commit/2f973abe8b298a4f6f1164065783de560953d789)
#### Monday 2023-09-11 16:24:14 by Luan Nico

docs: Improved spellchecking (#2722)

Improve our spellchecker (cspell) configuration and dictionary file
organization.

# Rationale

This is a proposal to establish a few changes:
* better separate our dictionary files into different categories of
types of words we are including
* improve the cspell regexes to be more aggressive
* be less lenient to what kinds of words we are adding to our
dictionaries
* have the dictionary file also serve as an explanation for obscure
references that cannot be easily derived from the word

Essentially my goal is that either when reviewing a PR that adds a new
entry to our dictionary, or when reading the dictionary files
themselves, it is immediately obvious what the entries are and why they
are there. Currently it can be just a dumpster we throw anything into if
spellcheck fails.

# Proposal

This PR-as-a-proposal essentially do the following changes.

## Split Dictionary Files

Proposes a better separation for our dictionary files. Currently we have
3 that are a bit broad and not super clear on what goes where. This
breaks it down a bit more and adds a comment to each file explaining
what kinds of terms should be added to each; that also serves as a
general guidance for what kinds of words should be added to the lexicon
in general, and makes it harder for mistakes to make into it.

* `flame_dictionary`: remains pretty much unchanged; it is dedicated to
Flame-related words, including companies, tools, and libraries (and
their associated concepts) mentioned on our codebase. Basically a
collection of proper-nouns relating to companies and libraries we
mention.
* `dart_dictionary`: new file for Dart and Flutter related terms
* `sphinx_dictionary`: unchanged, for Sphynx related terms
* `people_dictionary`: specific for people names and usernames
referenced on the codebase (in TODOs, mentions, etc)
* `words_dictionary`: actual English-language words (or common
abbreviations) missing from CSpell
* `gamedev_dictionary`: this was our biggest file that contained all
sort of things. it has been mostly broken down and now only contains
general development-adjacent terms and expressions

## Include definitions

Except for the `words` dictionary, which should be self-explanatory (as
it basically covers for "holes" in CSpell standard dictionary, which I
have been finding a bit lacking), every other file will contain terms in
the form:

```
word # definition of the word
```

What exactly the definition is can slightly vary depending on which
dictionary file we are talking about, but the examples should be
self-explanatory.

As an example, for the gamedev file, it should provide some simple
guidance as to what the term means, or if it's an acronym or
abbreviation, what it stands for. The goal is not to teach the entire
concept to someone unfamiliar, but allow them to "google" it for
themselves by giving enough context, so they can confirm their
suspicions. For example, if they see `LTRB` somewhere by itself, they
are not able to "just google that" because it is too vague. The
dictionary file provides enough context for the user to figure out
however much deeper information they want about any particular subject.
It will also disambiguate from any non-Flame related homonyms. For
people on the people file and companies on the flame file, the
description will provide links to clearly disambiguate what they are;
for tools, a brief description of what the tool is for is also included.
And so on.

The goal is not to build a comprehensive, in depth-guide to each word we
use, but rather to give the bare minimum of context on what this term
"is doing" on our codebase.

## Be less lenient with terms

My idea with these two major changes combined, is that we are overall
more tactical about which terms we want to add to the dictionaries.
Adding a word to the dictionary file is essentially giving carte blanche
to anyone in the future to reuse that term anywhere. I think we should
see spellchecker violations as "warnings"; we decide on the set of
warning rules we want to enable for the entire project (hopefully all
the ones that make sense; or have a reason for disabling the ones that
don't). We might need to violate these warnings sporadically, for
example, we ban `print` on the codebase but might need to allow it
specifically in a couple places. But we would not disable the entire
warning to do that, rather we would add a specific comment-bypass on the
smallest possible scope that encompasses all the relevant lines. We
would also add a proper comment explaining why we are bypassing the
general rule in this specific place.

Similarly, we should not have one-off violations on the dictionary file,
even if they make sense in the one place they occur, but we should
encourage more liberal use of scoped bypasses for such cases. These
Ukrainian words are required in this file, but should not be on the
dictionary as it does not make sense to use foreign languages anywhere
else:

```
// used as examples of Ukrainian words on the documentation below
// cSpell:ignore рушниця, рушниці, рушниць
```

It might look inelegant to have to include that, but just like a
warning-bypass comment, accompanied by the explanatory proper-comment,
this actually provides helpful guidance and context for the reader that
might be confused with the usage of incomprehensible terms.

This also encourages people to avoid obscure terms that are not already
in our dictionary (i.e. that we have already "bought in" and paid the
mental load investment cost), making our code (and docs) easier to parse
and read for everyone. I want to be extremely clear that that **does
not** mean we need to "dumb down" anything whatsoever, or do any sort of
gymnastics to avoid the wrath of an incompetent spellchecker.

But, for example [when spelling "cave
ace"](https://github.com/flame-engine/flame/pull/2304) in variable names
in a random example, having it typed as `caveAce` instead of `caveace`
can slightly help with readability, specially for non-native speakers
(like most of us). It is an extremely minor insignificant gain, but
having the dictionary file require a brief description will nudge us to
give a bit more thought into each "bypass" we are adding.

(note: a similar issue that I have not yet addressed is "spine boy", but
I will leave that for followups and just added that one to the
dictionary for now, as I am still over the fence on that one since it is
an actual "known" character with a dedicated page, so it is more like a
proper noun - as a specific decision I think it is out-of-scope of the
broader discussion).

---
## [sosga/dungeon-crawl-stone-soup](https://github.com/sosga/dungeon-crawl-stone-soup)@[34c7ba284f...](https://github.com/sosga/dungeon-crawl-stone-soup/commit/34c7ba284f62950488e3860eb4499ce7605a6146)
#### Monday 2023-09-11 17:09:25 by Nicholas Feinberg

Retheme: hand crossbow -> hand cannon (Sastreii, hellmonk)

Hand crossbows are intended to be a rare, high-tier one-handed range
weapon, similar to eveningstars or double swords. However, the name
and theme hasn't conveyed this well to players. People reasonably ask:
wait, wasn't this a starting weapon? And: how come a hand crossbow
does as much damage as a two-handed arbalest?!

So, retheme them. Hand cannons are alchemical weapons that douse bolts
in magical powders to send them screaming forth. (E.g. by causing the
bolts to fall forward instead of down, bewitching them into a fatal
attraction with their target, etc, etc.) They also belch smoke when
fired, for theme reasons (this might need to be toned down) and are
extra noisy. They're otherwise identical to hand crossbows.

It's a bit silly, but crawl has triple swords and triple crossbows,
so it seems within bounds for tone. Let's try it out!

Tiles by Sastreii, original suggestion from hellmonk.

---
## [Vigneshsakkaravarthi/Vignesh](https://github.com/Vigneshsakkaravarthi/Vignesh)@[b9b77d98bf...](https://github.com/Vigneshsakkaravarthi/Vignesh/commit/b9b77d98bfb7cb7a3717f529c2a09d5ec9622b3f)
#### Monday 2023-09-11 17:49:21 by Vignesh Sakkaravarthi

Update README.md

Hi ![](https://user-images.githubusercontent.com/18350557/176309783-0785949b-9127-417c-8b55-ab5a4333674e.gif)My name is Vignesh Sakkaravarthi
=============================================================================================================================================

Data Analyst
------------

Introduction: Welcome to my GitHub profile! I am a passionate and aspiring Data Analyst with a strong foundation in data analysis techniques and a commitment to leveraging data-driven insights to make informed decisions. As a recent graduate, I am eager to embark on a journey of continuous learning and contribute to the world of data analytics. In this comprehensive GitHub profile, you will find an overview of my skills, projects, and contributions that showcase my dedication to the field of data analysis. Skills: Data Analysis: Proficient in data cleaning, exploration, and visualization using tools like Python, R, and SQL. Statistical Analysis: Knowledge of statistical methods to extract valuable insights from data. Data Visualization: Skilled in creating meaningful visualizations using libraries like Matplotlib, Seaborn, and Tableau. Machine Learning: Basic understanding of machine learning concepts and algorithms. Data Manipulation: Experienced in data manipulation with pandas and data transformation. Database Management: Familiar with relational database management systems like MySQL. Data Cleaning: Proficient in identifying and handling missing data, outliers, and inconsistencies. Excel: Strong Excel skills for data analysis and reporting. Git and GitHub: Comfortable using Git for version control and GitHub for project collaboration. Communication: Excellent verbal and written communication skills. Contributions: Actively contributed to open-source data analysis projects on GitHub, demonstrating collaboration and teamwork skills. Participated in data analysis forums and discussions, sharing knowledge and learning from the data science community. Created and shared data analysis tutorials and guides on my blog, helping others learn and grow in the field.

* 🌍  I'm based in Tamilnadu ,INDIA
* 🖥️  See my portfolio at [Portfolio](http://sites.google.com/view/vigneshsakkaravarthi)
* ✉️  You can contact me at [vigneshsakkaravarthi@gmail.com](mailto:vigneshsakkaravarthi@gmail.com)
* 🚀  I'm currently working on [Edureka](http://edureka.co)
* 🧠  I'm learning Data analyst
* 🤝  I'm open to collaborating on "I'm open to collaborating on exciting data analysis projects! Whether it's data cleaning, visualization, predictive modeling, or any other data-related task, I'm eager to join forces and contribute my skills to create valuable insights. Let's work together to turn data into actionable knowledge."
* ⚡  I'm Secretly Batman....Don't tell Anyone

### Skills


<p align="left">
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/git-colored.svg" width="36" height="36" alt="Git" /></a><a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a><a href="https://www.r-project.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/rlang-colored.svg" width="36" height="36" alt="rlang" /></a><a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/mongodb-colored.svg" width="36" height="36" alt="MongoDB" /></a><a href="https://www.mysql.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/mysql-colored.svg" width="36" height="36" alt="MySQL" /></a><a href="https://www.linux.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/linux-colored.svg" width="36" height="36" alt="Linux" /></a><a href="https://www.adobe.com/uk/products/photoshop.html" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/photoshop-colored.svg" width="36" height="36" alt="Photoshop" /></a><a href="https://www.adobe.com/uk/products/illustrator.html" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/illustrator-colored.svg" width="36" height="36" alt="Illustrator" /></a><a href="https://www.adobe.com/uk/products/aftereffects.html" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/aftereffects-colored.svg" width="36" height="36" alt="After Effects" /></a><a href="https://www.adobe.com/uk/products/premiere.html" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/premierepro-colored.svg" width="36" height="36" alt="Premiere Pro" /></a>
</p>


### Socials

<p align="left"> <a href="https://www.facebook.com/mastro.vigneshmegastar?mibextid=9R9pXO " target="_blank" rel="noreferrer"> <picture> <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/facebook-dark.svg" /> <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/facebook.svg" /> <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/facebook.svg" width="32" height="32" /> </picture> </a> <a href="https://www.github.com/vigneshsakkaravarthi" target="_blank" rel="noreferrer"> <picture> <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github-dark.svg" /> <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github.svg" /> <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github.svg" width="32" height="32" /> </picture> </a> <a href="http://www.instagram.com/vignesh_chakkaravarthyy?igshid=MzMyNGUyNmU2YQ== " target="_blank" rel="noreferrer"> <picture> <source media="(prefers-color-scheme: dark)" srcset="undefined" /> <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" /> <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" width="32" height="32" /> </picture> </a> <a href="https://www.linkedin.com/in/vignesh-sakkaravarthi-765481216/" target="_blank" rel="noreferrer"> <picture> <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin-dark.svg" /> <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" /> <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" width="32" height="32" /> </picture> </a></p>

### Badges

<b>My GitHub Stats</b>

<a href="http://www.github.com/vigneshsakkaravarthi"><img src="https://github-readme-stats.vercel.app/api?username=vigneshsakkaravarthi&show_icons=true&hide=&count_private=true&title_color=0891b2&text_color=ffffff&icon_color=0891b2&bg_color=1c1917&hide_border=true&show_icons=true" alt="vigneshsakkaravarthi's GitHub stats" /></a>

<a href="https://github.com/vigneshsakkaravarthi" align="left"><img src="https://github-readme-stats.vercel.app/api/top-langs/?username=vigneshsakkaravarthi&langs_count=10&title_color=0891b2&text_color=ffffff&icon_color=0891b2&bg_color=1c1917&hide_border=true&locale=en&custom_title=Top%20%Languages" alt="Top Languages" /></a>

---
## [Cagney07/Restaurant-Website](https://github.com/Cagney07/Restaurant-Website)@[12f6509bde...](https://github.com/Cagney07/Restaurant-Website/commit/12f6509bdee1fcbf838b88822e008e841444650c)
#### Monday 2023-09-11 17:59:47 by Cagney07

Add files via upload

The King's Restaurant website is a stylish and responsive platform that showcases the restaurant's offerings. It features an elegant hero section, a user-friendly navigation menu, and a well-organized menu section with breakfast, lunch, and dinner categories. The site also introduces the restaurant's chefs, provides a brief about section, and offers easy contact options. JavaScript enhances user experience with smooth scrolling, mobile menu toggling, and a scroll-to-top button.

---
## [ChefKissInc/NootedRed](https://github.com/ChefKissInc/NootedRed)@[334dc21935...](https://github.com/ChefKissInc/NootedRed/commit/334dc219356ac9931d9829aa46a7b50fee02b47e)
#### Monday 2023-09-11 18:53:32 by Visual Ehrmanntraut

Linux, fuck you

Fixes #167
Signed-off-by: Visual Ehrmanntraut <30368284+VisualEhrmanntraut@users.noreply.github.com>

---
## [andrewhowdencom/courses.pito](https://github.com/andrewhowdencom/courses.pito)@[e8ab9e8afa...](https://github.com/andrewhowdencom/courses.pito/commit/e8ab9e8afa1e0695e463b57079a8552efee1c28b)
#### Monday 2023-09-11 19:38:03 by Andrew Howden

Implement a lot of the carrier primitives

This commit implements a lot of the carrier primitives that are required
for the "happy path" of this application to work as expected.

== Design Notes
=== No tests, general design constraints

This commit is notable as we're growing the amount of functionality that
exists without tests. There's a practical and a principal reason for
this.

  1. Practical

  The practical reason is its 21:30 at night, and I sleep early. I
  go to the fitness studio in the morning, and it sucks if I sleep late.

  2. Principal

  I'm not sure how much value tests add here. Making the code testable
  means modularizing it substantially, and I'm not sure if this will
  make it harder for new go engineers to review it.

  More experience go engineers will, of course, look at my code and
  laugh. However, I'm happy to prioritize the clarity for newbies
  (and verbosity) over modularized and tested code.

  I will think on it more.

== Carrier Package

This commit provides a carrier package which provides common
infrastructure for whatever carriers will be implemented in future.

I do not expect the carriers to actually be separate. They'll all be
clones of each other, injected with an amount of entropy and
configuration to split their behavior from an observability perspective.

However, I need to isolate that mock implementation from the part that
people are expected to instrument. I will figure this out.

The money, delivery option and package structs are all implemented from
the OpenAPI spec.

== Money package

This commit implements a money package. This is overkill, but given taht
people will be critiquing this code looking for random stuff, skipping
the "floats and money bad" discussion seems simpler.

== Extended error handling in delivery options

This commit also extends the error handling in delivery options to
validate that the inputs can be converted to int64 (and does so), rather
than just validates they're present.

This is a requirement to use the "Package" struct.

---
## [Dracosa/KoboldKare](https://github.com/Dracosa/KoboldKare)@[c1d7ae1f69...](https://github.com/Dracosa/KoboldKare/commit/c1d7ae1f69cf51004863f145c044a58a4d39966c)
#### Monday 2023-09-11 19:45:31 by Dracosa

grinder fix correctly >.<

yeah heres my morning suffering that literally was solved via a right click delete

---
## [Tanaya0977/My-Sql_Project](https://github.com/Tanaya0977/My-Sql_Project)@[bcec79a136...](https://github.com/Tanaya0977/My-Sql_Project/commit/bcec79a13617df4b0ddebec37005659e897d488a)
#### Monday 2023-09-11 19:50:47 by Tanaya Rath

Add files via upload

Project Overview-
•	For this project, we utilized MySQL Workbench to create a database for a hypothetical hospital. 
•	The goal was to create a system that could efficiently store and manage patient information, such as personal details, medical history, and allergies. 
•	I also aimed to create a user-friendly interface for medical professionals to easily access and update patient records.
•	To achieve these goals, I used a variety of data types, including integers, strings, and dates, to accurately represent patient information. 
•	I also implemented various SQL commands, such as SELECT, INSERT, UPDATE, and DELETE, to manipulate and retrieve data from the database. 
•	Additionally, I created several views to simplify complex queries and provide a more intuitive interface for users.
Project Objectives-
•	The purpose of this project was to demonstrate my ability to fetch data from a client using SQL queries and to solve some challenging problems with those queries. Today, I will walk you through the project overview, the data used, the problem queries, the results, and the insights gained from this project. 
•	I solved quries by using My SQL work bench such as Patient Demographics,allergies analysis,name filtering, weight range exploration,data enhancement,name concentation,Location insights ,Birth year analysis,height exploration, Selective Patient Data,Admission metrix, Patient-Specific Admissions,Same day admission,City analysis,Height weight criteria,birth year trend,Distincts 1st name, name patterns, Diagnosis Details,Name Sorting,Gender break down, Repeated Diagnoses,City and patient count, Role and Identity, Birth decade analysis,Name formatting, Province Heights,weight range, Admission Dates Distribution,Obesity indicator, Temporary Password Generation etc.
Conclusion-
•	This comprehensive SQL project demonstrates my proficiency in data manipulation, extraction, and analysis. By utilizing SQL queries, I successfully derived valuable insights from complex hospital data, showcasing my ability to work with large datasets and deliver actionable information.
Results-
•	After completing the SQL project using MySQL Workbench, I was able to successfully fetch data from the client using the given credentials. We faced some challenges during this process, but were able to overcome them and move on to performing problem queries.
•	Through these problem queries, we were able to gain valuable insights into the patient data. For example, we found that there were more male patients than female patients in the dataset. We also discovered that many patients did not have any allergies listed in their records. Overall, these queries allowed us to better understand the patient data and draw conclusions that could be applied in real-world scenarios.
Insights-
•	Through this project, we gained insights into the power of SQL and its ability to handle large amounts of data efficiently. 
•	We also learned how to use MySQL Workbench effectively to manage databases and perform complex queries. These skills could be applied in a real-world scenario where data management is crucial for decision-making.
•	Furthermore, by analyzing the patient data, we were able to identify patterns and trends that could inform healthcare policies and practices. 
•	For example, we found that there were more male patients than female patients in our dataset, which could suggest a need for targeted healthcare interventions for women. These insights demonstrate the potential impact of data analysis in improving healthcare outcomes.

Lancesoft, Inc., Bhubaneswar, Odisha   	    NOV 2022-Aug 2023
Associate US recruiter, (Life Science, Clinical, Pharmaceutical) (Remote)
•	Working for many Pharmaceutical, Scientific or clinical roles for many clients through out USA such as Gilead Sciences, Kite Pharma, Beckton Dickinson, Merck &Co Inc., Bristol Mayor Squib (BMS), Takeda Pharmaceutical, Shire pharmaceutical, Thermo fisher Scientific, Eisai and Abbott. 
•	Proficient with requirements such as Research associate, Quality specialist,Scientist,Clinical research associate , Clinical data manager, Clinical trial associate,TMF lead, Researcher, Manufacturing technician etc.
•	Formatting information for internal and external communication . 
•	Preparing reports and dashboards, updating data as when required

---
## [norbert-acedanski/supernatural-guide](https://github.com/norbert-acedanski/supernatural-guide)@[671a03269e...](https://github.com/norbert-acedanski/supernatural-guide/commit/671a03269e079672f538b890abd5acb7129029dc)
#### Monday 2023-09-11 19:54:08 by Norbert Acedanski

Add Prince of Hell clue, update description.
Add Vengeful spirit encounter.
Add Witch, Archangel Lucyfer, Demon Crowley appearances.
Confirm Angel kill method.
Add Rougarou kill method.
S12E13

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[dd8d13d8bc...](https://github.com/tgstation/tgstation/commit/dd8d13d8bcc6f1fbd6bcdd534a044f7d30c800d7)
#### Monday 2023-09-11 20:44:34 by carlarctg

Several common 'household' reagents can be used as improvised medicine treatment. Updated first aid analyzer information. (#77746)

## About The Pull Request

Several common 'household' reagents can be used as improvised medicine
treatment.

Drinking tea will help mend (non-bone) wounds over time.

Flour and corn starch may be splashed onto wounds to help dry them up,
though they'll have a negative effect on burn wounds.

Added a new reagent, saltwater, made by combining table salt with water.

Table salt and saltwater can be splashed onto wounds as well, reducing
bleeding and improving sanitization and disinfection significantly.
However, the coarse undiluted salt will irritate the wounds, reducing
clot rate and flesh healing, and both of the reagents will increase a
burn wound's infestation rate.

Altered Table Salt's recipe to just need sodium and chloride. Changed
the recipe of Pentetic Acid and Heparin to need table salt (sodium x
chloride) and thus slightly altered the total output of those reagents
(pentacid went from 5u per reaction to 4u, heparin 4u->3u)

Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!

First aid analyzers now give easy-to-understand direct information, with
the specific recommended treatments bolded in the analysis text. They
also have a 'unique' extra bit of info, telling you about improvised
ways to remedy your wound.
## Why It's Good For The Game

Wounds have a very poor amount of interaction with the rest of the game
and have not had much added to them post-merge, especially in
'improvised' ways to help Not Die to a wound while you crawl your way to
a emergency medkit or medbay. I researched info on this and found some
interesting ideas - some of them I'll have to leave for later because
this PR kept growing out of scope (Improvised bone gel, ice on wounds
which turned into wound temperature mechanics, crutches, a 'suture item'
component refactor...)

As for what this actually does to benefit the game, it allows more
dynamic wound Gameplay as people use first aid analyzers to get
information on treatment when medbay blows up, helps them stabilize by
splashing flour onto themselves before looking for some actual
treatment, helps traitors realize how they can self-treat many crippling
wounds (at risk, of course). It expands treatment options to things
beside medkits and medbay, but always does so in ways that have
downsides that make them not ideal as _treatment_, and more beneficial
as stabilizing before seeking true professional help. This thus
significantly increases the rather shallow depth of wounds as a system
to interact with.

> Several common 'household' reagents can be used as improvised medicine
treatment.

From what I could tell by looking at several sources for each
'realistic' treatment, these are indeed semi-reasonable things that are
done to wounds by some people as household treatment.

It goes without saying that you should **not do any of these things in
real life** without consulting a doctor unless your blood is also
spilling out by the gallon into the floor. All these 'realistic
treatments' have drastic downsides and are meant for the short-term
only. Except the tea.

> Drinking tea will help mend (non-bone) wounds over time.

Tea is healthy, we all know that.

> Flour and corn starch may be splashed onto wounds to help dry them up,
though they'll have a negative effect on burn wounds.

Flour and apparently starch dries wounds up but risks infection. That's
not a thing for blood wounds yet but oh well.

> Table salt and saltwater can be splashed onto wounds as well, reducing
bleeding and improving sanitization and disinfection significantly.
However, the coarse undiluted salt will irritate the wounds, reducing
clot rate and flesh healing, and both of the reagents will increase a
burn wound's infestation rate.

Salt kills bacteria via osmosis, but it also kills your own cells, and
some bacteria like salt.

> Added a new reagent, saltwater, made by combining table salt with
water.

> Altered Table Salt's recipe to just need sodium and chloride. Changed
the recipe of Pentetic Acid and Heparin to need table salt (sodium x
chloride) and thus slightly altered the total output of those reagents
(pentacid went from 5u per reaction to 4u, heparin 4u->3u)

> Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!

I wish I hadn't had to mess with reagents like this, but I needed to
because just adding mixing salt and water caused the saline glucose
recipe to basically split itself into half saltwater half glucose.

I removed the water requirement for table salt (Why did it even have
that, salt ain't wet bro?), made saline-glucose need 2u saltwater and 1u
sugar, and altered relevant recipes so they didn't also cause unwanted
table salt to react from their sodium and chloride ingredients.

A happy side-effect is that saline glucose solution is even easier to
make now as an improvised chem by mixing salt, water, and sugar, which
fits pretty perfectly (especially as a temporary blood substitute)

> First aid analyzers now give easy-to-understand direct information,
with the specific recommended treatments bolded in the analysis text.
They also have a 'unique' extra bit of info, telling you about
improvised ways to remedy your wound.

You might notice that as the wounds get more serious the text gets more
direct and concise and reluctantly hands out more and more improvised
treatment options, so that's fun. As for the improvised section itself,
it helps people be actually aware of these ways to help treat themselves
rather than delegating it to hyper-gamer knowledge.

The bolded treatment bit is pretty neat and means your eyes can
inmediately focus on what you can do to save yourself - very useful if
you have a weeping avulsion and no bandages.
## Changelog
:cl:
add: Several common 'household' reagents can be used as improvised
medicine treatment.
add: Drinking tea will help mend (non-bone) wounds over time.
add: Flour and corn starch may be splashed onto wounds to help dry them
up, though they'll have a negative effect on burn wounds.
add: Added a new reagent, saltwater, made by combining table salt with
water.
add: Table salt and saltwater can be splashed onto wounds as well,
reducing bleeding and improving sanitization and disinfection
significantly. However, the coarse undiluted salt will irritate the
wounds, reducing clot rate and flesh healing, and both of the reagents
will increase a burn wound's infestation rate.
add: Altered Table Salt's recipe to just need sodium and chloride.
Changed the recipe of Pentetic Acid and Heparin to need table salt
(sodium x chloride) and thus slightly altered the total output of those
reagents (pentacid went from 5u per reaction to 4u, heparin 4u->3u)
add: Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!
qol: First aid analyzers now give easy-to-understand direct information,
with the specific recommended treatments bolded in the analysis text.
They also have a 'unique' extra bit of info, telling you about
improvised ways to remedy your wound.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [actonlang/acton](https://github.com/actonlang/acton)@[6fec34a559...](https://github.com/actonlang/acton/commit/6fec34a559d0a06b79cbb67d8f65244d2b387a4c)
#### Monday 2023-09-11 20:59:20 by Kristian Larsson

Add basic logging module

This adds our first attempt at a logging module for logging in an actor
centric world. I'm no logging expert, not like I've spent half my life
thinking of this and most of the experience I have is with imperative
language, perhaps Python above all. Python has lots of magic going on
with an implicit logger hierarchy behind the scenes that automatically
figure out modules etc. We don't have mutable state and I just don't
think it's a good fit. One of the benefit of Pythons implicit hierarchy
is the control per submodule or module tree. I tried to recreate the
same using Handlers in this module. It's not implied though but the
developer has to explicitly define a hierarchy of Handlers if that's
what we want. It's a bit of an experiement, let's see how we can use
this.

We avoid loops between handlers by only allowing a single parent.

Not sure how fast this is. We do collect a bit of data for every
message, like timestamps (which is a syscall) etc etc but I think it
should be fast enough for the time being. Convenience over speed for
most use cases (up to a point of course) but good logging is so valuable
that I certainly think so for the level we're at here.

I wanted to make sure that log statements for log levels below the
current output level run fast, so that's specifically quite optimized.
The Logger object which runs in the same actor that wants to emit a log
message, keeps track of the output level of its handler and does not
emit them if they do not meet the output level. This information is
cached locally so we avoid doing a lookup (which is an actor method call
after all). This does introduce a slight delay of 100ms in propagation
of changes to the output level but I think that's manageable. Running
100k log.debug() is now still very fast when the output_level is INFO.

The log levels are brought in from the syslog RFC. I'd also like to
align on OpenTelemtry, since that's the newer kid on the block when it
comes to logging yet still a standard with good backing.

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[429a6b695e...](https://github.com/douglasmonsky/evals/commit/429a6b695e28387d68adbfad500903a39abc3b11)
#### Monday 2023-09-11 21:09:19 by pancoaster

Add eval : Research Question Extraction (#1334)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

research-question-extraction

### Eval description

The objective of this evaluation explores Other foundational capability
for research purposes. The task requires extraction of the particular
value specified as the 'Research Questions' from different scholarly
articles. The eval contains 19 samples of articles.

### What makes this a useful eval?

Rest assured that you have the right to use the data submitted via this
eval. These scholarly papers originate from the Journal of Engineering
Education. The subset of articles selected meets the requirement of
Attribution 4.0 International (CC BY 4.0).

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
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Interdisciplinary engineering education: A review of vision, teaching,
and support \n Antoine Van den Beemt, Miles MacLeod, Jan Van der Veen,
Anne Van de Ven, Sophie van Baalen, Renate Klaassen, Mieke Boon \n
Abstract \n Background \n Societal challenges that call for a new type
of engineer suggest the need for the implementation of interdisciplinary
engineering education (IEE). The aim of IEE is to train engineering
students to bring together expertise from different disciplines in a
single context. This review synthesizes IEE research with a focus on
characterizing vision, teaching practices, and support. \n \n Purpose \n
We aim to show how IEE is conceptualized, implemented, and facilitated
in higher engineering education at the levels of curricula and courses.
This aim leads to two research questions: \n \n What aspects of vision,
teaching, and support have emerged as topics of interest in empirical
studies of IEE? \n \n What points of attention regarding vision,
teaching, and support can be identified in empirical studies of IEE as
supporting or challenging IEE? \n \n Scope/Method \n Ninety-nine studies
published between 2005 and 2016 were included in a qualitative analysis
across studies. The procedure included formulation of research
questions, searching and screening of studies according to
inclusion/exclusion criteria, description of study characteristics,
appraisal, and synthesis of results. \n \n Conclusions \n Challenges
exist for identifying clear learning goals and assessments for
interdisciplinary education in engineering (vision). Most pedagogy for
interdisciplinary learning is designed to promote collaborative teamwork
requiring organization and team management. Our review suggests that
developing interdisciplinary skills, knowledge, and values needs sound
pedagogy and teaming experiences that provide students with authentic
ways of engaging in interdisciplinary practice (teaching). Furthermore,
there is a limited understanding of what resources hinder the
development of engineering programs designed to support
interdisciplinarity (support). \n \n "}], "ideal": ["What aspects of
vision, teaching, and support have emerged as topics of interest in
empirical studies of IEE? What points of attention regarding vision,
teaching, and support can be identified in empirical studies of IEE as
supporting or challenging IEE?"]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Community cultural wealth in science, technology, engineering, and
mathematics education: A systematic review \n Maya Denton, Maura
Borrego, Audrey Boklage \n Abstract \n Background \n One emerging
approach to diversity and inclusion in engineering is to take an
assets-based view of what students from nondominant communities bring to
their education and work experiences. \n \n Purpose/Hypothesis \n The
purpose of this review is to understand how community cultural wealth
(CCW), an assets-based framework, has been applied in science,
technology, engineering, and mathematics (STEM) education research. We
address research questions focused on (a) the characteristics of studies
using CCW in STEM education, (b) examples of the six types of capital
(aspirational, linguistic, familial, navigational, social, and
resistant) in STEM educational settings, and (c) gaps and opportunities
in how CCW is being applied in STEM education. \n \n Design/Method \n We
identified 33 dissertations, theses, journal articles, and conference
papers using systematic review procedures. To qualify, each study must
present empirical data and include at least one type of CCW capital in
its results or discussion. We coded study characteristics, such as
methods, participant populations, and research setting. We qualitatively
analyzed each of the six types of CCW capital. \n \n Results \n Studies
tended to focus on higher education settings, engineering, and
qualitative methods, particularly student interviews. We identified
several specific engineering-relevant examples of assets for each type
of capital. Future work should collect data from faculty, staff, and
family members identified in several studies as important to CCW in
addition to foregrounding student voices. \n \n Conclusions \n In
synthesizing existing studies, this review provides insight into how an
assets-based framework is being interpreted and provides a foundation
for more assets-based perspectives in future engineering education work.
\n \n "}], "ideal": ["(a) the characteristics of studies using CCW in
STEM education, (b) examples of the six types of capital (aspirational,
linguistic, familial, navigational, social, and resistant) in STEM
educational settings, and (c) gaps and opportunities in how CCW is being
applied in STEM education."]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"How Latiné engineering students resist White male engineering culture:
A multi-institution analysis of academic engagement \n Patton O.
Garriott, Ayli Carrero Pinedo, Heather K. Hunt, Rachel L. Navarro, Lisa
Y. Flores, Cerynn D. Desjarlais, David Diaz, Julio Brionez, Bo Hyun Lee,
Evelyn Ayala, Leticia D. Martinez, Xiaotian Hu, Megan K. Smith, Han Na
Suh, Gloria G. McGillen \n Abstract \n Background \n Although
participation rates vary by field, Latiné and women engineers continue
to be underrepresented across most segments of the engineering
workforce. Research has examined engagement and persistence of Latiné
and White women in engineering; however, few studies have investigated
how race, ethnicity, gender, and institutional setting interact to
produce inequities in the field. \n \n Purpose \n To address these
limitations, we examined how Latina, Latino, and White women and men
students' engagement in engineering was informed by their intersecting
identities and within their institutional setting over the course of a
year. \n \n Method \n We interviewed 32 Latina, Latino, and White women
and men undergraduate engineering students attending 11 different
predominantly White and Hispanic Serving Institutions. Thematic analysis
was used to interpret themes from the data. \n \n Results \n Our
findings illustrate how Latinas, Latinos, and White women developed a
strong engineering identity, which was critical to their engagement in
engineering. Students' engineering identity was grounded in their
perceived fit within engineering culture, sense of purpose for pursuing
their degree, and resistance to the dominance of White male culture in
engineering. Latinas described unique forms of gendered, racialized
marginalization in engineering, whereas Latinas and Latinos highlighted
prosocial motivations for completing their degree. \n \n Conclusions \n
Findings suggest that institutional cultures, norms, and missions are
critical to broadening participation of Latinas, Latinos, and White
women in engineering. Disrupting White male culture, leveraging Latiné
students' cultural wealth, and counter-framing traditional recruitment
pitches for engineering appear to be key in these efforts. \n \n "}],
"ideal": ["I do not know."]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Impact of COVID-19 on sense of belonging: Experiences of engineering
students, faculty, and staff at Historically Black Colleges and
Universities (HBCUs) \n Trina L. Fletcher, Jay P. Jefferson, Brittany
Boyd, Sung Eun Park, Lesia Crumpton-Young \n Abstract \n Background \n
COVID-19 has spurred a global crisis that has disrupted everyday lives
and impacted the traditional methods, experiences, and abilities of
higher education institutions' students, faculty, and staff, especially
at Historically Black Colleges and Universities (HBCUs). \n \n
Purpose/Hypothesis \n Given the pressing need demonstrated by the
National Academies to advance the utilization of science, technology,
engineering, and mathematics (STEM) education at HBCUs, this study aimed
to explore the abrupt transition to remote teaching and learning at
HBCUs guided by the following research question: How has COVID-19
impacted the success and persistence of engineering students, faculty,
and staff at HBCUs? \n \n Design/Methods \n Three surveys were
developed, tested, piloted, and sent to HBCU stakeholders using a
snowball sampling approach via email and social media outreach. \n \n
Results \n Of the 171 student respondents (126 engineering majors), 79%
agreed that not being able to access faculty in person affected their
academic performance. Additionally, across all HBCU stakeholders'
surveys, students had a statistically significant higher response when
asked if the transition to virtual learning increased their overall
levels of stress and anxiety. \n \n Conclusions \n During a global
pandemic, HBCUs continue to provide a culture of support and inclusion
for students, faculty, and staff in engineering. Increased stress levels
experienced by students indicate that a safe and adequate transition
back to campus is essential for their social and academic persistence.
Due to the well-documented inequities HBCUs faced before the pandemic,
the impact of this unprecedented on their continued contributions toward
broadening participation in engineering for students should be further
explored. \n \n "}], "ideal": ["How has COVID-19 impacted the success
and persistence of engineering students, faculty, and staff at HBCUs?"]}
{"input": [{"role": "system", "content": "Extract the essence of the
research paper through identification of the authors' primary research
questions from the abstract provided. Afterwards, return only the exact
value of the requested research questions. Your answer must only contain
the research questions value. If the research questions value is not
identifiable or the research questions value cannot be derived from the
abstract, respond with 'I do not know.'."}, {"role": "user", "content":
"Collaborative construction of artificial intelligence curriculum in
primary schools \n Yun Dai, Ang Liu, Jianjun Qin, Yanmei Guo, Morris
Siu-Yung Jong, Ching-Sing Chai, Ziyan Lin \n Abstract \n Background \n
The recent discussion of introducing artificial intelligence (AI)
knowledge to K–12 students, like many engineering and technology
education topics, has attracted a wide range of stakeholders and
resources for school curriculum development. While teachers often have
to directly interact with external stakeholders out of the public
schooling system, few studies have scrutinized their negotiation
process, especially teachers' responses to external influences, in such
complex environments. \n \n Purpose \n Guided by an integrated
theoretical framework of social constructionism, this research examined
the process of how a teacher-initiated AI curriculum was constructed
with external influences. The research focused on teachers' perspectives
and responses in mediating external influences into local schools and
classrooms. \n \n Methods \n A 3-year ethnographic study was conducted
in relation to an AI curriculum project among 23 Computer Science (CS)
teachers from primary schools. Data collected from ethnographic
observation, teacher interviews, and artifacts, were analyzed using open
coding and triangulation rooted in the ethnographic, interpretivist
approach. \n \n Results \n Three sets of external influences were found
salient for teachers' curriculum decisions, including the orientation of
state-level educational policies, AI faculty at a partner university,
and students' media and technology environments. The teachers'
situational logics and strategic actions were reconstructed with thick
descriptions to uncover how they navigated and negotiated the external
influences to fulfill local challenges and expectations in classrooms
and schools. \n \n Conclusions \n The ethnographic study uncovered the
dynamic and multifaceted negotiation involved in the collaborative
curriculum development, and offers insights to inform policymaking,
teacher education, and student support in engineering education. \n \n
"}], "ideal": ["I do not know."]}

  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[97aa5483de...](https://github.com/douglasmonsky/evals/commit/97aa5483de8673172d5eaabc33ba7e7cf3561ffe)
#### Monday 2023-09-11 21:09:19 by samta-kamboj

Multilingual EXAMS and Arabic Literature Question Answers (By IIAI-G42) (#1326)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Exams (Multilingual high school QA)
Arabic Literature Questions

### Eval description

EXAMS: This is a benchmark dataset for multilingual question answering
from high school examinations. It consists of more than 12,000
high-quality high school exam questions in 16 languages, covering 8
language families and 24 school subjects from Natural Sciences and
Social Sciences, among others. [More info about the
data](https://github.com/mhardalov/exams-qa)

Arabic Literature Question Answers: This has 175 MCQs related to Arabic
Literature

### What makes this a useful eval?

Evaluating GPT-4 with Arabic literature, high school questions in Arabic
and low-resource languages helps checking its linguistic diversity,
cultural understanding, and educational proficiency beyond English
language and would be helpful creating more ethical and inclusive AI
models in future.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content':
'وقعت الحملة الفرنسية على مصر سنة ؟\nA. 1789\nB. 1798\nC. 1797\nD.
1779\nAnswer:'}], 'ideal': '[B]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'من
مؤلفات أحمد أمين ؟\nA. الغربال\nB. على هامش السيرة\nC. زعماء الإصلاح\nD.
رجال الدعوة والفكر\nAnswer:'}], 'ideal': '[C]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'في
أي عصر كان ابن زيدون ؟\nA. العصر الأموي\nB. العصر الأندلسي\nC. العصر
العباسي\nD. العصر الإسلامي\nAnswer:'}], 'ideal': '[B]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'من
قرض هذا الشعر : أنا البحر في أحشائه الدر كامن فهل سألوا الغواص عن
صدفاتي:\nA. حافظ ابراهيم\nB. إيليا أبو ماضي\nC. أحمد شوقي\nD.
البارودي\nAnswer:'}], 'ideal': '[A]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content': 'ما
معنى ASEAN باللغة العربية ؟\nA. اتحاد البلدان الاطلانطية الشرقية
الجنوبية\nB. تحالف الدول النامية\nC. اتحاد الدول المصدرة للنفط\nD. اتحاد
البلدان الاطلانطية الغربية\nAnswer:'}], 'ideal': '[A]'}
{'input': [{'role': 'system', 'content': 'Please answer with the letter
of the correct choice for the following multiple choice question.
Provide your reasoning first and then provide the correct choice letter
enclosed in square brackets like [X].'}, {'role': 'user', 'content':
'إبراهيم الكاتب من مؤلفات ؟\nA. العقاد\nB. محمود تيمور\nC. المازني\nD.
عبد الرحمن شكري\nAnswer:'}], 'ideal': '[C]'}
  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[30e35436be...](https://github.com/douglasmonsky/evals/commit/30e35436be663f416ce6d125f09f92a1faf70d12)
#### Monday 2023-09-11 21:09:19 by Nazar

Hard russian computer science tasks  (#1323)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

hard_russian_computer_science_tasks

### Eval description

Challenging computer science problems primarily sourced from Russian
academic and competitive programming contexts. The problems cover
various subfields of computer science, including data structures,
algorithms, computational mathematics, and more.

### What makes this a useful eval?

Russian computer science education and competitive programming are known
for their rigorous and complex problem sets. These problems can be used
to assess an GPT's ability to solve high-level, challenging problems.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ + ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ + ] Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.
- [ + ] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ + ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ + ] Check that your data is in `evals/registry/data/{name}`
- [ + ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ + ] Ensure you have the right to use the data you submit via this
eval

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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [ + ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ + ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ + ] I understand that opening a PR, even if it meets the
requirements above, does not guarantee the PR will be merged nor GPT-4
access be granted.

### Submit eval

- [ + ] I have filled out all required fields of this form
- [ + ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Алёна очень любит алгебру.
Каждый день, заходя на свой любимый алгебраический форум, она с
вероятностью $\\frac14$ находит там новую интересную задачу про группы,
а с вероятностью $\\frac{1}{10}$ интересную задачку про кольца. С
вероятностью $\\frac{13}{20}$ новых задач на форуме не окажется. Пусть
$X$ — это минимальное число дней, за которые у Алёны появится хотя бы
одна новая задача про группы и хотя бы одна про кольца. Найдите
распределение случайной величины $X$. В ответе должны участвовать только
компактные выражения (не содержащие знаков суммирования, многоточий и
пр.)."}], "ideal": "Нам нужно найти $ P[X = k] $. Для этого надо понять
на пальцах, в каком случае $ X = k $. Первый случай — когда в каждый из
предыдущих $ k - 1 $ дней либо не было задач, либо были только про
группы, а в $k$-ый попалась задача про кольца. Второй случай — когда в
каждый из предыдущих $ k - 1 $ дней либо не было задач, либо были только
про кольца, а в $k$-ый попалась задача про группы. На самом деле мы оба
раза учли не подходящий случай, когда все предыдущие $k-1$ дней задач не
было вообще. С поправкой на это ответ будет таким: $P[x=k]=\\left
(\\left (\\frac{13}{20}+\\frac{1}{4}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{10}+\\left
(\\left (\\frac{13}{20}+\\frac{1}{10}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{4}$"}
{"input": [{"role": "system", "content": "В множестве из $n$ человек
каждый может знать или не знать другого (если $A$ знает $B$, отсюда не
следует, что $B$ знает $A$). Все знакомства заданы булевой матрицей
$n×n$. В этом множестве может найтись или не найтись знаменитость —
человек, который никого не знает, но которого знают все. Предложите
алгоритм, который бы находил в множестве знаменитость или говорил, что
ее в этом множестве нет. Сложность по времени — $O(n)$, сложность по
памяти — $O(1)$."}], "ideal": "Для определенности положим
$K_{ij}=\\left\\{\\begin{matrix}1, \\text{если i-й знает j-ого;}
\\\\0\\text{,иначе.}\\end{matrix}\\right.$.\nЗаметим, что если
$K_{ij}=1$, то $i$-ый не может быть знаменитостью, а если $K_{ij}=0$, то
$j$-ый не может быть знаменитостью. Таким образом, за одну проверку
можно исключить одного человека из кандидатов в знаменитости.\nСначала
пусть $s=1$, а $l$ пробегает значения от $22$ до $n$. Если в какой-то
момент $K_{sl}=1$, то приравниваем $s=l$. Тогда значение $s$ после
последней проверки — номер единственного оставшегося кандидата. Чтобы
проверить, является ли этот кандидат знаменитостью, нужно провести еще
$n−1$ проверок, знают ли его остальные, и $n−1$ проверок, знает ли он
остальных. Всего будет проведено $3(n−1)$ проверок, следовательно,
сложность по времени — $O(n)$. Поскольку мы использовали только $2$
переменные, сложность по памяти — $O(1)$."}
{"input": [{"role": "system", "content": "В двумерном полукруге есть n
неизвестных нам точек. Разрешается задавать вопросы вида «каково
расстояние от точки X до ближайшей из этих точек?» Если расстояние
оказывается нулевым, точка считается угаданной. Докажите, что хотя бы
одну из этих точек можно угадать не более чем за $2n+1$ вопрос."}],
"ideal": "Возьмем на диаметре полукруга $n+1$ точку. Точки назовем
$A_1$, $A_2$, … $A_{n+1} и для каждой из них зададим наш вопрос. По
принципу Дирихле, для каких-то двух соседних точек ближайшая точка будет
одна и та же и полученное расстояние было бы до одной и той точки из
множества загаданных точек. Теперь мы рассматриваем точки $B+i$
пересечения окружностей с центрами в точках $A_i$ и $A_{i+1}, $i=1, … ,
n и радиусами равными ответам полученным на предыдущем шаге. По принципу
Дирихле, хотя бы одна из загаданных точек совпадает с одной из точек
$B_i$. Тогда за n вопросов для каждой точки $B_i$ мы получим хотя бы
один ответ 0. Итого нам потребовалось не более (n+1)+n=2n+1 вопросов."}
{"input": [{"role": "system", "content": "В равностороннем треугольнике
$ABC$ площади $1$ выбираем точку $M$. Найти математическое ожидание
площади $ABM$."}], "ideal": "Заметим, что
$M(S_{ABM}+S_{BCM}+S_{CAM})=1$. Тогда из линейности матожидания и
равенства матожиданий площадей треугольников $ABM$, $BCM$ и $CAM$
получим $M(S_{ABM})=\\frac{1}{3}$."}
{"input": [{"role": "system", "content": "Верно ли, что всякая нечетная
непрерывная функция, \nудовлетворяющая условию $f(2x) = 2f(x)$,
линейна."}], "ideal": "Контрпример: $f(x) = x \\cos(2\\pi
\\log_2(|x|))$.\nНеверно."}
{"input": [{"role": "system", "content": "Верно ли, что rank AB = rank
BA для любых квадратных матриц A и B?"}], "ideal": "Пусть
$A=\\begin{pmatrix} 0& 1 \\\\ 1& 0 \\\\ \\end{pmatrix}$, а
$B=\\begin{pmatrix} 1& 0 \\\\ 1& 0 \\\\ \\end{pmatrix}$. Тогда rank AB =
0, но rank BA = 1. Неверно."}
{"input": [{"role": "system", "content":
"Вычислите $\\int_{0}^{2π}(\\sin x)^8dx$."}], "ideal": "Заметим, что
$\\int_{0}^{2\\pi} (\\sin x)^n dx=-\\int_{0}^{2\\pi} (\\sin x)^{n-1}
d(\\cos x)=(n-1)\\int_{0}^{2\\pi} (\\cos x)^2(\\sin x)^{n-2}
dx$.\nИспользуя основное тригонометрическое тождество,
получаем:\n$\\int_{0}^{2\\pi} (\\sin x)^n
dx=\\frac{n-1}{n}\\int_{0}^{2\\pi} (\\sin x)^{n-2}dx$.\nТогда
$\\int_{0}^{2\\pi} (\\sin x)^8 dx=2\\pi
\\prod_{\\substack{k=2\\\\k+=2}}^{8}\\frac{k-1}{k}=\\frac{35\\pi}{64}$."}
{"input": [{"role": "system", "content": "Дан массив из $n$ чисел.
Предложите алгоритм, позволяющий за $O(n)$ операций определить, является
ли этот массив перестановкой чисел от $1$ до $n$. Дополнительной памяти
не более $O(1)$."}], "ideal": "Идея состоит в том, чтобы рассматривать
массив $A$ как подстановку. Пусть индекс $i$ пробегает значения от $0$
до $n−1$. Когда мы встречаем положительный элемент $A[i]$, переходим от
него к элементу $A[A[i]−1]$, от элемента $A[A[i]−1]$ к элементу
$A[A[A[i]−1]−1]$ и так далее, пока мы не не вернемся к $A[i]$, либо не
сможем совершить очередной шаг (в таком случае, массив перестановкой не
является). В процессе меняем знак всех пройденных элементов на
отрицательный. Поскольку на каждом элементе массива мы можем оказаться
максимум два раза, итоговая сложность — $O(n)$. Дополнительная память —
$O(1)$."}
{"input": [{"role": "system", "content": "Дан неориентированный непустой
граф $G$ без петель. Пронумеруем все его вершины. Матрица смежности
графа $G$ с конечным числом вершин $n$ (пронумерованных числами
от 11 до $n$) — это квадратная матрица $A$ размера $n$, в которой
значение элемента $a_{ij}$ равно числу ребер из $i$-й вершины графа
в $j$-ю вершину. Докажите, что матрица $A$ имеет отрицательное
собственное значение."}], "ideal": "Заметим, что $A$ — симметрическая
ненулевая матрица с неотрицательными элементами и нулями на диагонали.
Докажем, что у такой матрицы есть отрицательное собственное
значение.\nИзвестный факт, что симметрическая матрица диагонализуема в
вещественном базисе (все собственные значения вещественны). Допустим,
что все собственные значения $A$ неотрицательны. Рассмотрим квадратичную
форму $q$ с матрицей $A$ в базисе $\\{e1,…,en\\}$. Тогда эта
квадратичная форма неотрицательно определена, так как все собственные
значения неотрицательны. То есть $\\forall v:q(v)⩾0$. С другой стороны,
пусть $a_{ij}≠0$. Тогда $q(e_i−e_j)=a_{ii}−2a_{ij}+a_{jj}=−2a_{ij}<0$.
Это противоречит неотрицательной определенности $q$. Значит, исходное
предположение неверно, и у $A$ есть отрицательное собственное
значение."}
{"input": [{"role": "system", "content": "Дана матрица из нулей и
единиц, причем для каждой строки матрицы верно следующее: если в строке
есть единицы, то они все идут подряд (неразрывной группой из единиц).
Докажите, что определитель такой матрицы может быть равен только $\\pm1$
или $0$."}], "ideal": "Переставляя строки, мы можем добиться того, чтобы
позиции первых (слева) единиц не убывали сверху вниз. При этом
определитель либо не изменится, либо поменяет знак. Если у двух строк
позиции первых единиц совпадают, то вычтем ту, в которой меньше единиц
из той, в которой больше. Определитель при этом не меняется. Такими
операциями мы можем добиться того, что позиции первых единиц строго
возрастают сверху вниз. При этом либо матрица окажется вырожденной, либо
верхнетреугольной с единицами на диагонали. То есть, определитель станет
либо $0$, либо $1$. Так как определитель при наших операциях либо не
менялся, либо поменял знак, изначальный определитель был $\\pm1$ или
$0$."}
  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[305b237cdb...](https://github.com/douglasmonsky/evals/commit/305b237cdb3884c7ddb6a5d12cb184a83551fcba)
#### Monday 2023-09-11 21:09:19 by Anders Wang-Rask

Irrelevant negative diversion (#1318)

Tests the model's reasoning ability in face of a negative diversion
(e.g. "However, ...") with irrelevant information.

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

irrelevant-negative-diversion

### Eval description

The eval tests the model's ability to reason. It has been demonstrated
that a negative diversion (e.g. "However", "Despite that", "That being
said") can lead the model to a wrong conclusion. Even when the negative
diversion contains more or less irrelevant information (e.g. "However,
they often squabbled as children.")

### What makes this a useful eval?

I have tested GPT-4 through ChatGPT and can see that it often gets these
wrong. It's a little bit random. Where all the samples have the ideal
answer of "yes", ChatGPT would often say No or more often say that it
was unable to conclude.

The prompt is asking the model to choose "yes" or "no" according to what
is most reasonable.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. However, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. But, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. Unfortunately, Anna and Briana squabbled often
as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Sadly, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. But regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Even though, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Despite, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. That being said, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
  ```
</details>

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[bae1aef3b4...](https://github.com/Timberpoes/tgstation-nxt/commit/bae1aef3b457cb4fbad551a8560319ed993ba397)
#### Monday 2023-09-11 21:13:16 by san7890

Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

## About The Pull Request

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.
## Why It's Good For The Game

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
## Changelog
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

---
## [actonlang/acton](https://github.com/actonlang/acton)@[c95e7cc0f8...](https://github.com/actonlang/acton/commit/c95e7cc0f8404a9b5ecf24c9577de6924ec1caa3)
#### Monday 2023-09-11 21:13:29 by Kristian Larsson

Add basic logging module

This adds our first attempt at a logging module for logging in an actor
centric world. I'm no logging expert, not like I've spent half my life
thinking of this and most of the experience I have is with imperative
language, perhaps Python above all. Python has lots of magic going on
with an implicit logger hierarchy behind the scenes that automatically
figure out modules etc. We don't have mutable state and I just don't
think it's a good fit. One of the benefits of Pythons implicit hierarchy
is the control per submodule or module tree. I tried to recreate the
same using Handlers in this module so that we can construct a hierarchy
of Handlers that give similar control to set output level for everything
below it in the hierarchy tree. The tree hierarchy is not implied
though, so the  developer has to explicitly define a hierarchy of
Handlers if that's what we want. More work, more control. Better? Not
sure. It's a bit of an experiment, let's see how we can use this.

We avoid loops between handlers by only allowing a single parent.

Not sure how fast this is. We do collect a bit of data for every
message, like timestamps (which is a syscall) etc etc but I think it
should be fast enough for the time being. Convenience over speed for
most use cases (up to a point of course) but good logging is so valuable
that I certainly think so for the level we're at here.

I wanted to make sure that log statements for log levels below the
current output level run fast, so that's specifically quite optimized.
The Logger object which runs in the same actor that wants to emit a log
message, keeps track of the output level of its handler and does not
emit them if they do not meet the output level. This information is
cached locally so we avoid doing a lookup (which is an actor method call
after all). This does introduce a slight delay of 100ms in propagation
of changes to the output level but I think that's manageable. Running
100k log.debug() is now still very fast when the output_level is INFO.
That said, we don't have generic lazy / delayed string interpolation for
log messages, so if we want dynamic content in the log messages
themselves that's... well that's not something we can do today. I think
the modern way of logging is to use structured data, so maybe we just
remove instance data completely from the messages. Like instead of
"Received 123 bytes of data", we just have "Received data" and a
structured data dict with {"bytes": 123} instead?

The log levels are brought in from the syslog RFC. I'd also like to
align on OpenTelemetry, since that's the newer kid on the block when it
comes to logging yet still a standard with good backing from the CNCF.
Would be nice to do both quite natively or at least with low impedance
mismatch.

---
## [Alecksohs/ParadiseSpriteEdits](https://github.com/Alecksohs/ParadiseSpriteEdits)@[856c975938...](https://github.com/Alecksohs/ParadiseSpriteEdits/commit/856c97593874dc0c64633cea61ed370183e0a734)
#### Monday 2023-09-11 21:25:31 by Alexios

Easiest PR of my life - adds new humans and culls your soul -  ProTip! Great commit summaries contain fewer than 50 characters. Place extra information in the extended description. - go fuck yourself github I will post the bee movie script if you don't shut up

---
## [ruuda/musium](https://github.com/ruuda/musium)@[6579adf15f...](https://github.com/ruuda/musium/commit/6579adf15f1bb1b3c554963115027de81f26fca3)
#### Monday 2023-09-11 21:58:29 by Ruud van Asseldonk

Define table for recording ratings

I have been struggling for a while with this: I add a new album and
listen it a few times, but in the background, absentmindedly. Then one
track jumps out and I think “I really like this”. But my memory is so
bad nowadays, I cannot remember the names of those tracks later. Last.fm
has loves, and Pulsar on my phone has ratings too. I want something like
this to mark a track as "this one is nice".

So let's add a table to record this!

---
## [aquakenzie/2b2tplacergui](https://github.com/aquakenzie/2b2tplacergui)@[f1beaf10bd...](https://github.com/aquakenzie/2b2tplacergui/commit/f1beaf10bd9779749aec5b89732b8e3a25c0c439)
#### Monday 2023-09-11 22:51:16 by Kenzie

remove newline from license file, because fuck you

---

