## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-16](docs/good-messages/2023/2023-11-16.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,656,233 were push events containing 4,033,551 commit messages that amount to 302,458,491 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 93 messages:


## [PhenolLully/group-project1](https://github.com/PhenolLully/group-project1)@[dbc8725a3a...](https://github.com/PhenolLully/group-project1/commit/dbc8725a3a357def4e398597ff01bd5927780c50)
#### Thursday 2023-11-16 00:40:26 by Bdubs

added response.statusText to the error handler so when troubleshooting we know exactly what the status code is, removed the event handlers which showed alerts,removed the both joke function as it was preventing new jokes from displaying on click, created a new function which adds the joke in based on thier respective apis and updated our jquery method.

---
## [SpringSkipper/Skyrat-tg](https://github.com/SpringSkipper/Skyrat-tg)@[c034314f1b...](https://github.com/SpringSkipper/Skyrat-tg/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Thursday 2023-11-16 00:43:22 by SkyratBot

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
## [SpringSkipper/Skyrat-tg](https://github.com/SpringSkipper/Skyrat-tg)@[0e3b7d842b...](https://github.com/SpringSkipper/Skyrat-tg/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Thursday 2023-11-16 00:43:22 by SkyratBot

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
## [HellWatcher/russ-station](https://github.com/HellWatcher/russ-station)@[517d33e6f0...](https://github.com/HellWatcher/russ-station/commit/517d33e6f06289085d0c6015a01c3a3ce7bc22d0)
#### Thursday 2023-11-16 00:46:24 by Jacquerel

Basic blob mobs (#78520)

## About The Pull Request

I remembered today that blob code is ass, especially blob spores.
There's still a lot to improve but I cleaned up _some_ of it by
converting these mobs.
Now they use a newer framework and more signal handling as compared to
circular references.

I _expect_ the behaviour here to largely be the same as it was or
similar. I haven't added anything fancy or new.

This is a reasonably big PR but at least all of the files are small?
Everything here touched every other thing enough that it didnt make
sense to split up sorry.

Other things I did in code:
- Experimented with replacing the `mob/blob` subtype with a component.
Don't know if this is genius or stupid.
- AI subtree which just walks somewhere. We've used this behaviour a lot
but never given it its own subtree.
- Blob Spores and Zombies are two different mobs now instead of being
one mob which just changes every single one of its properties.
- Made a few living defence procs call super, because the only thing
super does was send a signal and we weren't doing that for no reason.
Also added a couple extra signals for intercepts we did not have.

## Changelog

:cl:
fix: Blob spores will respond to rallies more reliably (it won't runtime
every time they try and pathfind).
fix: Blobbernaut pain animation overlays should align with the direction
the mob is facing instead of always facing South
refactor: Blob spores, zombies, and blobbernauts now all use the basic
mob framework. They should work the same, but please report any issues.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[86fb9b4478...](https://github.com/microsoft/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Thursday 2023-11-16 01:13:06 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [jnhyatt/bevy](https://github.com/jnhyatt/bevy)@[ab300d0ed9...](https://github.com/jnhyatt/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Thursday 2023-11-16 01:30:20 by Connor King

Gizmo Arrows (#10550)

## Objective

- Add an arrow gizmo as suggested by #9400 

## Solution

(excuse my Protomen music)


https://github.com/bevyengine/bevy/assets/14184826/192adf24-079f-4a4b-a17b-091e892974ec

Wasn't horribly hard when i remembered i can change coordinate systems
whenever I want. Gave them four tips (as suggested by @alice-i-cecile in
discord) instead of trying to decide what direction the tips should
point.

Made the tip length default to 1/10 of the arrow's length, which looked
good enough to me. Hard-coded the angle from the body to the tips to 45
degrees.

## Still TODO

- [x] actual doc comments
- [x] doctests
- [x] `ArrowBuilder.with_tip_length()`

---

## Changelog

- Added `gizmos.arrow()` and `gizmos.arrow_2d()`
- Added arrows to `2d_gizmos` and `3d_gizmos` examples

## Migration Guide

N/A

---------

Co-authored-by: Nicola Papale <nicopap@users.noreply.github.com>

---
## [G-e-n-e-v-e-n-s-i-S/Full-Magic-Pack](https://github.com/G-e-n-e-v-e-n-s-i-S/Full-Magic-Pack)@[bcbf998745...](https://github.com/G-e-n-e-v-e-n-s-i-S/Full-Magic-Pack/commit/bcbf9987451c1e2292f24bc063f7c4a5f6028c2f)
#### Thursday 2023-11-16 01:35:14 by cajun

non-latin alphabetization and lists

- moved the language map to its own file
- ordered Japanese types by Gojuon with hiragana, katakana might be more fitting tho
- ordered Korean, would be nice to reconstruct the characters on the Xa-Xm symbols
- ordered Russian according to its alphabet
- added katakana translations for all missing Japanese types
- missing translations are now not included, may loosen to allowing English into German/French/Italian/Portuguese/Spanish
- Chinese creature types are currently just localeCompare()'d and grouped like Creature Classes for both. There are Gojuon-like systems for sorting but those are probably above my pay grade
- added the other card languages to Set tab
- added Class, Race, and Plane word lists for all languages

TODO
- the Angel, Beast, Construct, Demon, Dragon, Elf, Faerie, Giant, Goblin, Golem, Human, Merfolk, Zombie and Beast, Cleric, Druid, Knight, Rogue, Shaman, Soldier, Warrior, Wizard, Zombie sections have been removed, i'm going to pick a new crop and readd those in later
- the localized type word lists aren't supported yet

---
## [mission23/.github](https://github.com/mission23/.github)@[45d89ece17...](https://github.com/mission23/.github/commit/45d89ece1715e475bd1436afd10f0eeabd72c0d6)
#### Thursday 2023-11-16 01:37:12 by Micah

Update README.md

Just a reminder, We told you about the ringing of the bell first. 
—-
First a tragedy, then a massacre, now an ongoing genocide. They had it coming and He had to do it.
The Creator is going to “ring the bell” very soon. The exact time is not going to be announced. Scientists have often said that a very strong earthquake will ring Earth like a bell.
These earthquakes are intended to shine a light on a horrible, unnecessary tragedy caused by greed, the massacre of a church at the height of the Sunday morning worship service caused by wrath, the continued killing of innocent people at the church has started the first genocide against a non-indigenous population in US history. Why isn’t this being reported?
Regardless of how much work folks have done to get the story out and reported for your safety, the federal government and federal law enforcement agencies are still putting pressure on the Commonwealth of Kentucky’s attorney and law enforcement to turn a blind eye and IGNORE the actions of the CIA. The CIA continues to kill in the very place that people go to and expect to be the safest and closest to God, who is none other than, the Creator (our pissed off Boss).
Obviously drunk on power, the CIA, the federal government and federal law enforcement need to sober up quickly, so the Creator, has decided to ring the bell. It’s a warning that they have forgotten who’s universe, Earth, and country this landmass really is.
In addition to showing how displeased He is, the Creator is also honoring lives that have cut short in response to a set of remedies (some of objectives in #mission23) that should have let all of these lives go on for far more years than 99% of the human population believe is even possible. The way He designed and wants them to be lived.
Don’t call a cure, it’s been here before. It’s your immune system, you are a product of intelligent design.
It also signals the start of #mission23, and says “Thanks” to everyone who has tolerated the federal government’s pressure when they knew the right thing to do and they simply wanted to do it.
Earthquakes
The order and intensity of the bell ringing (earthquakes) goes as follows:
Orr Chapel Quake
This earthquake’s epicentre will be located in Sandy Hook, TN (the former unincorporated city near, now neighborhood of Mount Pleasant) in Maury county. The Rogers family farm.
This will be a large earthquake for the CIA’s destruction of Orr Chapel (Google Maps) and the murder of all of it’s identified members.
This quake also recognises Micah’s slain family and his family’s graveyard that was destroyed, both by or at the direction of the CIA.
Mount Calvary Baptist Church Quake
This earthquake’s epicentre will be located at Mount Calvary Baptist Church in Lexington, KY (4742 Todds Road).
This will be the largest quake for the massacre that occurred there.
See: The Massacre at Mount Calvary Baptist Church
The Micah Quake
This earthquake’s epicentre will be in Jessamine county, KY. It will signal when Micah (born: Kelvin Eugene Williams on March 23, 1977) has started his mission for the Creator. This will be Micah’s 23rd mission on Earth.
This minor quake will also be to recognize the lives lost in Jessamine county, mostly Micah’s friends, throughout the larger tragedy.
The Thomas Quake
This earthquake’s epicentre will be in Kanawha county (Hughes Creek), WV. It will signal when TomTom (to practically everyone TomTom, to others Thomas, born: September 23, 1978) has started his mission for the Creator. This also is TomTom’s 23rd mission on Earth.
This minor quake will also recognize the lives lost in Kanawha county, mostly TomTom’s friends and family, throughout the larger tragedy.
Press Conferences
These are tentative. Conditions on the ground are very fluid — and I don’t mean from the quakes. Please check back here for updates to the schedule.
Orr Chapel
At high noon the day immediately following the shaking under our feet the SotC will have a press conference at the site of Orr Chapel & Sheepneck cemeteries. Located along West Sheepneck Road in Sandy Hook, TN.
Mount Calvary Baptist Church
On the second day following the shaking, the SotC will be at Mount Calvary Baptist Church at 4742 Todds Road in Lexington, KY at high noon.
Suggested Listening
The Sound and the Fury
By Vandaveer — Listen on YouTube Music
1999
By Prince — Listen on YouTube Music

---
## [SapphicOverload/tgstation](https://github.com/SapphicOverload/tgstation)@[7fce8cd805...](https://github.com/SapphicOverload/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Thursday 2023-11-16 01:37:56 by san7890

Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2562f0997a...](https://github.com/tgstation/tgstation/commit/2562f0997a73a52c4ada51c7e0d9996fea4ee573)
#### Thursday 2023-11-16 01:38:41 by MrMelbert

Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished (#79694)

## About The Pull Request

Related: #78017 

Stop drop and roll is no longer instant -5 fire stacks -> stun -> wait. 

Now, when you stop drop and roll, every time you roll you will lose 1
firestack.

A roll is triggered every 0.8 seconds. Moving, getting up, or becoming
incapacitated / stunned will stop you from rolling.
_(This number puts it roughly equivalent to its current rate.)_

While rolling, your hands are blocked (you cannot use items, hold
things, etc.)
Additionally, you will roll until all firestacks are cleared. 

## Why It's Good For The Game

Getting stunned for 6 seconds because you decide to stop and roll is a
little silly. Reasonably you could stop rolling and get back up should
the need arise, such as "oh god there's more fire I gotta relocate".

By changing it to a gradual thing, it makes it a bit more reasonable and
fair.
- New players who immediately slam "STOP DROP ROLL" because the alert on
their screen tells them to are no longer helpless for 6 whole seconds
- People who hit the resist key, intending to interact with something
else (such as a bola) are no longer stuck rolling when they did not want
to

## Changelog

:cl: Melbert
balance: Stop, drop, and roll no longer instantly clears 5 fire stacks
off of you - Instead, it will clear 1 fire stack off of you every time
you roll, with a roll every 0.8 seconds.
balance: Stop, drop, and roll no longer stuns you for 6 seconds.
Instead, it will knock you to the floor while you are rolling. Moving
around or getting up will cancel the roll, and you cannot use items
while rolling around.
balance: Stop, drop, and roll will now repeat until the fire is put out
or you get up.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[742971675d...](https://github.com/tgstation/tgstation/commit/742971675de266aa4ebe671dc5175a5c543d93d7)
#### Thursday 2023-11-16 01:40:40 by san7890

Fixes Relay Attackers Misfire (#79731)

## About The Pull Request

Fixes #76079

Basically we were both not getting all of the args that we recieve from
`COMSIG_ITEM_AFTERATTACK` which included the very important
`proximity_flag` which tells us if the person was in range to actually
hurt us or not. This means that clicking a mob with this element with a
stack of metal from across the room would cause them to aggro, which
makes no sense whatsoever. Let's actually use that proximity check.

We listen for projectiles hitting us separately, don't worry.
## Why It's Good For The Game

It just makes no damn sense, fixes some weird ass behavior. 
## Changelog
:cl:
fix: Bar Bots (and several other mobs) will no longer aggro on you if
you click on them with a "forceful" item from halfway across the room.
/:cl:

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[389d1e5669...](https://github.com/shiptest-ss13/Shiptest/commit/389d1e566990682f173066df4c16f25b3a1858c0)
#### Thursday 2023-11-16 02:45:43 by Erika Fox

Does Penance So The Ghosts Go Away (#2442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

"This is AI c-Caldwell - Reporting return of essential station functions
to Minya League Installation 'Trifuge' following pirate attack -
**///far too long ago///** - All vessels are invited to dock and partake
of our services, including an active Ore Refinery, world class bar, and
purchasable storefronts **//please come, I'm so lonely///** The Minya
League, and myself, would like to extend our gratitude to **///-who else
but me?///**. Installation 'Trifuge' is located in orbit of the Star
'Anselhome', at the L5 point of Anselhome and habitable world, 'Hofud'.
Noting active travel advisory - Hofud is currently **///nothing but ash
left by monsters///**. Independent Vessels are advised to avoid landing
until Minya League Ships can deliver disaster relief to the planet
**///not that they'll be coming....///**"

"This message will repeat in approximately 20 galactic standard minutes"

Remaps the shitty outpost 1 (indie space) outpost that I made like 6
months ago. it sucks. Anyone who doesn't think it sucks probably has
stockholm symdromed themselves into liking it. Also this one has lore
and room for expansion.
It's main features are: 
- Decent amount of maint for outpost antics
- REASONABLE amount of storefronts
-abandoned feel
- bar
- Ore refinery so my holy mandate can be implemented when I decide I'm
done with my break.

![2023-10-30 22 34
33](https://github.com/shiptest-ss13/Shiptest/assets/94164348/de3d93e2-e43b-478a-9d8c-7b44c972433d)
![2023-10-30 22 34
35](https://github.com/shiptest-ss13/Shiptest/assets/94164348/770109d4-1ab8-46b2-b3b8-e96c575cdde4)
There are your screenshots.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'd like the voices in my walls to stop whispering to me about the
horrific mistakes I've made. They seem pretty upset about this one.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Erika Fox
add: Outpost 1 has been remapped into something fathomably less ass.
It's a bit smaller, probably, but I'm going to call that a good thing.
add: random number spawner. It's good for hull numbers that shouldn't be
static.
imageadd: a really bad sprite for a service directions sign.
add: Another elevator template (coincidentally demonstrating how that
system works in code)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [joelj1995/joeljdotca](https://github.com/joelj1995/joeljdotca)@[1e913cbe55...](https://github.com/joelj1995/joeljdotca/commit/1e913cbe55c3f117949ea34e907e34e76581eac1)
#### Thursday 2023-11-16 04:24:01 by Joel Johnston

Fix some stupid fucking god-awful bug where the angular build
absolutely MANGLES my styles.

https://stackoverflow.com/questions/67565858/angular-12-css-optimization-inline-event-handler-with-content-security-policy/67582075#67582075

---
## [sjc5/hwy](https://github.com/sjc5/hwy)@[772708ef4c...](https://github.com/sjc5/hwy/commit/772708ef4c22b1087a6881b1263b84479317e912)
#### Thursday 2023-11-16 04:31:01 by Sam Cook

0.4.0 -- Cloudflare Pages support, Hwy Config, Client Scripts in Pages Dir (#12)

First off, huge shoutout to @jharrell for his debugging and research
assistance on this PR related to adding Cloudflare Pages support! Thank
you!

- Cloudflare Pages is now supported! Closes #6.

- Added changesets. Closes #14.

- Adds a `hwy.config.ts` / `hwy.config.js` file to the root of your
project for setting up dev settings and deployment target, and probably
other things in the future. As annoying as config files are, this
simplifies a lot of things and is not too much to ask for a framework.

- Removes a lot of complexity / variance in build commands and deploy
target hacks, as now we can just read the deployment target from the Hwy
config and handle everything in Hwy's centralized build step.

- Adds a new `@hwy-js/build` package, splitting up the live refresh
stuff (stays in `@hwy-js/dev`) from the build stuff.

- In your `src/main.tsx` file:
- `{hwyDev?.DevLiveRefreshScript()}` is now just `<DevLiveRefreshScript
/>`
- `<ClientEntryScript />` is now `<ClientScripts
activePathData={activePathData} />`. This is to enable the new client
scripts functionality mentioned below.

- Added an option to ship client-side JS (including from TS files if you
want) by adding a sibling `page-name.client.ts` or `page-name.client.js`
file to your page. This becomes basically global JS for that page, and
anything imported will be bundled into that page's script, which is
built into the public folder and referenced in the document head when
you visit that page. This will be better documented later. Closes #15.

---------

Co-authored-by: Jon Harrell <4829245+jharrell@users.noreply.github.com>

---
## [evmts/evmts-monorepo](https://github.com/evmts/evmts-monorepo)@[d6e92eecf2...](https://github.com/evmts/evmts-monorepo/commit/d6e92eecf224b3b5ba304c0c204e28cc2c8b82a2)
#### Thursday 2023-11-16 04:50:24 by Will Cory

:sparkles: Feat(vm): Add precompiles as an option (#664)

## Description

[Norswap requested
precompiles](https://twitter.com/norswap/status/1724944291204665439).
Norswap gets precompiles.

With precompiles one will be able to write arbitrary javascript that
runs when a contract is called. They can even do gross stuff like append
to a dom. Fwiw this will also be how evmts cheat codes work but before
we weren't planning on exposing this to end users.

While implementing this feature I found an annoying bug. If you don't
include an argument in your precompile the entire thing fails to
execute. Opened pr to fix issue here
https://github.com/ethereumjs/ethereumjs-monorepo/pull/3158

The types are currently wrong. It takes an Ethjs address instead of a
HexString address unlike the rest of the evmts pr. This is because
patching the types as I wished was tediously hard as a result of
ethereumjs not exporting specific types I need. Later I will do a pr to
ethereumjs about this. For now we do some typescript magic to infer the
type but because of the type is a union type it's difficult to patch and
I gave up for now.

## Testing

Unit test testing a precompile

## Additional Information

- [ ] I read the [contributing docs](../docs/contributing.md) (if this
is your first contribution)

Your ENS/address:

Co-authored-by: Will Cory <willcory@Wills-MacBook-Pro.local>

---
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[2fc0dfd8c1...](https://github.com/oxidecomputer/omicron/commit/2fc0dfd8c11f31e66cfaf8ee80586bb2ed607216)
#### Thursday 2023-11-16 04:53:21 by Andrew J. Stone

Extract storage manager related code from sled-agent (#4332)

This is a large PR. The changes are in many ways *just* moving code
around,
and at a cursory glance may appear to be a giant waste of time. To
justify
these changes and my rationale I will first present the goals I believe
we
should strive to meet in general sled-agent development. I'll then go
into
how I believe these goals can be realized via code patterns. I'll then
discuss
the concrete changes in this PR and how they implement the discussed
patterns.
Lastly, I'll list a few open questions about the implementation in the
PR.

I want to emphasize that a lot of what I talk about below is already
done in
sled-agent, at least part way. We can pick the best patterns already in
use and
standardize on them to build a more coherent and yet decoupled
architecture for
easier testing and understanding.

# Goals

This PR is an attempt to start making sled-agent easier to maintain. In
order to
make things easier to maintain, I believe we should attempt to realize a
few key
goals:

1. Initial startup and control code should read linearly. You shouldn't
have to
jump around to follow the gist of what's going on.
2. Tasks, like functions, should live at a certain abstraction level. It
must be clear
 what state the task is managing and how it gets mutated.
3. A developer must be able to come into the codebase and know where a
given
functionality should live and be able to clearly follow existing
patterns such
that their new code doesn't break or cross abstractions that make
following the
code harder in the future.
4. Tests for individual abstractions and task driven code should be easy
to
write. You shouldn't need to spin up the whole sled-agent in order to
test an
algorithm or behavior.
 5. Hardware should be abstracted out, and much of the code shouldn't 
 deal with hardware directly.

# Patterns

## Task/Handle

In my opinion, the most important pattern to follow for async rust
software
is what I call the "task/handle" pattern. This pattern helps code
maintenance
by explicitly managing state and making task driven code easier to test.
All
tasks that provide services to other tasks should follow this pattern.
In this
pattern, all state is contained in a type owned by the task and
inaccessible
directly to other tasks. The task has a corresponding handle which must
be
`Send` and `Clone`, and can be used to make requests of the task. The
handle
interacts with the task solely via message passing. Mutexes are never
used.

A few things fall directly out of this pattern:

* Code that manipulates state inside and outside the task can be
synchronous
* We don't have to worry about mutex behavior with regards to
cancellation,
   await points, etc...
 * Testing becomes easier:
   * We can test a bunch of the code without spawning a task in many
cases. We just [directly construct the state object and call
functions](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR634-R656),
     whether sync or async.
   * When testing sequential operations that are fire and forget,
we [know when they have been processed by the task
loop](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR702-R709),
     because our next request will only run after those operations. 
This is a direct result of the fifo channel between handle and task.
This is not possible with state shared outside the task via a mutex.
     We must poll that mutex protected state until it either changes to
     the value we expect or we get a timeout. If we expect no change, we
     must use a side-channel.
   * We can write complex state handling algorithms, such as those in 
      maghemite or bootstore, in a deterministic, synchronous style that
allows property based testing and model checking in as straightforward
     a manner as possible.
* We can completely [fake the
task](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR163-R223)
without changing any of the calling code except the constructor. The
real
handle can instead send messages to a fake task. Importantly, this
strategy
can also be used to abstract out hardware for unit tests and simulation.

Beyond all that though, the understanding of how state is mutated and
accessed
is clear. State is only mutated inside the task, and can only be
retrieved from
code that has a copy of the handle. There is no need for separate
`_locked`
methods, and no need to worry about order of locking for different bits
of task
state. This can make the task code itself much shorter and easier to
read as
demonstrated by the new `StorageManager` code in `sled_storage`. We can
also
maintain internal stats for the task, and all of this can be retrieved
from the
handle for reporting in `omdb`.

There is one common question/problem with this pattern. How do you
choose a
bounded channel size for handle to task messages?

This can be tricky, but in general, you want the channel to *act*
unbounded,
such that sends never fail. This makes the channels reliable, such that
we never
drop messages inside the process, and the caller doesn't have to choose
what to
do when overloaded. This simplifies things drastically for developers.
However,
you also don't want to make the channel actually unbounded, because that
can
lead to run-away memory growth and pathological behaviors, such that
requests
get slower over time until the system crashes.

After discussions with @jgallagher and reflections from @sunshowers and
@davepacheco on RFD 400, the solution is to choose a large enough bound
such that we should never hit it in practice unless we are truly
overloaded.
If we hit the bound it means that beyond that requests will start to
build
up and we will eventually topple over. So when we hit this bound, we
just
[go ahead and
panic](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR75-R77).

Picking a channel bound is hard to do empirically, but practically, if
requests are
mostly mutating task local state, a bound of 1024 or even 8192 should be
plenty.
Tasks that must perform longer running ops can spawn helper tasks as
necessary
or include their own handles for replies rather than synchronously
waiting. Memory
for the queue can be kept small with boxing of large messages.

It should also be noted that mutexes also have queues that can build up
and
cause pathological slowness. The difference is that these queues are
implicit
and hard to track.

## Isolate subsystems via the message driven decoupling

We have a bunch of managers (`HardwareManager`, `StorageManager`,
`ServiceManager`, `InstanceManager`) that interact with each other to
provide sled-agent services. However, much of that interaction is ad-
hoc with state shared between tasks via an `Inner` struct protected
by a mutex. It's hard to isolate each of these managers and test
them independently. By ensuring their API is well defined via a
`Handle`,
we can fake out different managers as needed for independent testing.
However, we can go even farther, without the need for dependency
injection
by having different managers announce their updates via [broadcast or
watch

channels](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR129-R133).

With this strategy, we can drive tests for a task by using the handle to
both
trigger operations, and then wait for the outflow of messages that
should occur
rather than mocking out the handle API of another task directly and
checking
the interaction via the fake. This is especially useful for lower level
services
that others depend upon such as `StorageManager`, and we should do this
when we
can, rather than having tasks talk directly to each other. This strategy
leads
directly to the last pattern I really want to mention, the `monitor`
pattern.

## High level interaction via monitors

Remember that a primary goal of these patterns is to make the sled-agent
easier
to read and discover what is happening at any given point in time. This
has to
happen with the inherent concurrency of all the separate behaviors
occurring
in the sled-agent such as monitoring for hardware and faults, or
handling user
requests from Nexus. If our low level managers announce updates via
channels
we can have high level `Monitors` that wait for those updates and then
dispatch
them to other subsystems or across clients to other sleds or services.
This
helps further decouple services for easier testing, and also allows us
to
understand all the asynchrony in the system in fewer spots. We can put
RAS code
in these monitors and use them as central points to maintain stats and
track the
overall load on the system.

# The punchline

How do the patterns above satisfy the goals? By decoupling tasks and
interacting
solely via message passing we make testing easier(goal 4). By separating
out
managers/ services into separate tasks and maintaining state locally we
satisfy
goals 2 and 5. By making the tasks clear in their responsibilities, and
their
APIs evident via their handles, we help satisfy goal 3. Goal 3 is also
satisfied
to a degree by the elimination of sharing state and the decoupling via
monitors.
Lastly, by combining all the patterns, we can spawn all our top level
tasks and
monitors in one place after initializing any global state. This allows
the code
to flow linearly.

Importantly, it's also easy to violate goal 3 by dropping some mutexes
into the
middle of a task and oversharing handles between subsystems. I believe
we can
prevent this, and also make testing and APIs clearer, by separating
subsystems
into their own rust packages and then adding monitors for them in the
sled-agent.
I took a first cut at this with the `StorageManager`, as that was the
subsystem I was
most familiar with.

# Concrete Code changes

Keeping in line with my stated goals and patterns, I abstracted the
storage
manager code into its own package called `sled-storage`. The
`StorageManager`
uses the `task/handle` pattern, and there is a monitor for it in
sled-agent
that takes notifications and updates nexus and the zone bundler. There
are also a
bunch of unit tests where none existed before. The bulk of the rest of
the code
changes fell out of this. In particular, now that we have a separate
`sled-storage`
package, all high level disk management code lives there. Construction
and
formatting of partitions still happens in `sled-hardware`, but anything
above the
zpool level occurs in `sled-storage`. This allows testing of real
storage code on
any illumos based system using file backed zpools. Importantly, the
key-management
code now lives at this abstraction level, rather than in
`sled-hardware`, which
makes more sense since encryption only operates on datasets in ZFS.

I'd like to do similar things to the other managers, and think that's a
good way
to continue cleaning up sled-agent.

The other large change in this code base is simplifying the startup of
the bootstrap agent such that all tasks that run for the lifetime of
the sled-agent process are spawned in `long_running_tasks`. There is a
struct called `LongRunningTaskHandles` that allows interaction with all
the
"managers" spawned here. This change also has the side effect of
removing the
`wait_while_handling_hardware_updates` concurrent future code, since we
have
a hardware monitor now running at the beginning of time and can never
miss
updates. This also has the effect of negating the need to start a
separate
hardware manager when the sled-agent starts up. Because we now know
which
tasks are long running, we don't have to save their tokio `JoinHandle`s
to display
ownership and thus gain clonability.

# Open Questions

* I'm not really a fan of the name `long_running_task_handles`. Is there
a better
name for these?
* Instead of calling `spawn_all_longrunning_tasks` should we just call
the
individual spawn functions directly in `bootstrap/pre_server`? Doing it
this
way would allow the `ServiceManager` to also live in the long running
handles
and remove some ordering issues. For instance, we wait for the bootdisk
inside
`spawn_all_longrunning_tasks` and we also upsert synthetic disks.
Neither
of these is really part of spawning tasks.

---
## [snipergaming888/fedoraware-bot-setup](https://github.com/snipergaming888/fedoraware-bot-setup)@[5c48e7700e...](https://github.com/snipergaming888/fedoraware-bot-setup/commit/5c48e7700ec7ca693c3a1658b5ba25fdad38ed53)
#### Thursday 2023-11-16 04:54:02 by Sydney

Merge pull request #1 from pixelwarrior99/patch-1

HOLY SHIT THIS SUCKS

---
## [FRC3636/bunnybots-2023](https://github.com/FRC3636/bunnybots-2023)@[3f9b610179...](https://github.com/FRC3636/bunnybots-2023/commit/3f9b6101791ba1ce6dd97eec1fdd07ce8590eef4)
#### Thursday 2023-11-16 05:09:57 by Crafterzman

fix(swerve): working drivetrain (#7)

* i let megan cook

* feat(tracking): solve for optimal time offset

feat(tracking): refactor prior commit

* feat(tracking): add lead targeting

feat(tracking): solve for optimal time offset

feat(tracking): refactor prior commit

feat(tracking): add lead targeting

* feat(tracking): switch to multivariate regression, use NT timestamping

* refactor(tracking): change names :)

* refactor(CAN): change id's

asa says hi

* ok we're gonna try to fuck up this shit again baruch atah adonai frfr

* fix: change pid coefficients

* fix(vision): uncomment TargetVision subsystem

---------

Co-authored-by: rotating.cow <ben.arkonovich@gmail.com>

---
## [stevendanna/cockroach](https://github.com/stevendanna/cockroach)@[d1ddc072a8...](https://github.com/stevendanna/cockroach/commit/d1ddc072a8c10c7568166af9495e6418df3e5a22)
#### Thursday 2023-11-16 05:55:20 by craig[bot]

Merge #114273

114273: pkg/util/aggmetric: tick histogram windows in AggHistogram r=aadityasondhi a=abarganier

Fixes: https://github.com/cockroachdb/cockroach/issues/114175, https://github.com/cockroachdb/cockroach/issues/112947

**NOTE**: The ideal way to fix this is merging `pkg/util/metric/aggmetric` into 
`pkg/util/metric`. That way, we wouldn't have to expose any of the "tick" 
functionality in the histogram public API. However, merging the two packages 
would be a pain to backport, and therefore we're leaving the merging to a 
follow up PR (coming soon). In the meantime, this provides a fix with a minimized 
surface area, so that we can more easily backport the fix. The merging will only 
occur on the master branch. 

**Reviewer note:** Recommended to review commit-wise.

---

AggHistograms are wrappers around the histogram implementations found in
pkg/util/metric. Internally, Histogram implementations within
pkg/util/metric maintain histogram windows to calculate quantiles at
each scrape by CockroachDB's TSDB, instead of storing every single
histogram bucket. These windows are rotated periodically, where the
current window becomes the previous window, and the current window is
then set to a new histogram. This allows us to diff the two windows, and
internally, pkg/util/metric has "ticking" functionality which is
responsible for rotating these histogram windows.

Unfortunately, since `pkg/util/metric/aggmetric` is in a separate
package, somehow this "ticking"/rotating of histogram windows was never
implemented into the AggHistogram. Because of this, it's likely that
metrics powered by AggHistogram have been broken since its inception
within CockroachDB's internal TSDB (but work fine in Prometheus).

Previous patches did some work to expose this ticking library to
AggHistogram, and this patch implements it.

In this patch, we make it so AggHistogram ticks/rotates histogram
windows, similar to how the other Histogram library does it. Since
AggHistograms have child histograms, this means that the rotation of all
histograms for both parent and children need to be done atomically. We
implement this by providing the AggHistogram its own tick.Ticker, where
the onTick function holds a RWMutex shared by the parent & all its
children and rotates the histograms for all.

With this in place, histogram windows are properly rotated for
AggHistograms. Future work will merge `pkg/util/metric/aggmetric` into
`pkg/util/metric`, after which we can once again make all this ticking
functionality private to the metrics package.

Release note (bug fix): Previously, all `AggHistogram`-powered metrics
were not reporting quantiles properly in DB Console. The list of
affected metrics is:

- changefeed.message_size_hist
- changefeed.parallel_io_queue_nanos
- changefeed.sink_batch_hist_nanos
- changefeed.flush_hist_nanos
- changefeed.commit_latency
- changefeed.admit_latency
- jobs.row_level_ttl.span_total_duration
- jobs.row_level_ttl.select_duration
- jobs.row_level_ttl.delete_duration

This patch fixes the histograms so that the quantiles in DB Console are
reported correctly.

Please note: these histograms were only broken in the DB Console metrics
features, but were **not** broken in the Prometheus-compatible endpoint,
`/_status/vars`.

## Screenshots

#### AggHistogram in DB Console pre-fix:
![pre](https://github.com/cockroachdb/cockroach/assets/8194877/aa08592b-4ebd-43d5-acff-8d00edc4ada1)

#### AggHistogram in DB Console post-fix:
<img width="1059" alt="Screenshot 2023-11-10 at 4 06 57 PM" src="https://github.com/cockroachdb/cockroach/assets/8194877/723c4974-e038-4871-9721-8ec18fca5f95">

#### AggHistogram in Grafana post-fix:
<img width="1648" alt="Screenshot 2023-11-10 at 4 07 22 PM" src="https://github.com/cockroachdb/cockroach/assets/8194877/05920189-c1b1-4895-a1fa-b8b1e069407a">


Co-authored-by: Alex Barganier <abarganier@cockroachlabs.com>

---
## [TurtleShroom/RimworldWesternizationProject](https://github.com/TurtleShroom/RimworldWesternizationProject)@[e1b54fc432...](https://github.com/TurtleShroom/RimworldWesternizationProject/commit/e1b54fc432c27d9523d3e056d71fef7e44dc7c4d)
#### Thursday 2023-11-16 06:12:42 by TURTLESHROOM

Minor

1. Added support for agricultural and farming tools from many Mods, allowing them to appear in this Mod among the peasantry.

2. Added new class of Townsman, the Farmer.

3. Added more Apparel Tags.

4. Women no longer spawn with the GENTLEMAN'S Pants.

5. Split the Socialites into two separate male and female sets of Pawns.

6. Added EVEN MORE Apparel tags.

7. Added support for the Work Sites from the "Ideology" Expansion Pack.

---
## [vishwa989944/currency-convertrans.github.io](https://github.com/vishwa989944/currency-convertrans.github.io)@[0c75f0620c...](https://github.com/vishwa989944/currency-convertrans.github.io/commit/0c75f0620c1bdc1fa976b4cb23da2acc67842c42)
#### Thursday 2023-11-16 06:20:02 by vishwa989944

Currency Converter - Instant Exchange Rates

Welcome to our Currency Converter, the go-to tool for quick and accurate currency exchange rates. Whether you're a globe-trotter, a business professional, or simply managing your international finances, our user-friendly platform provides real-time currency conversion at your fingertips.

Key Features:

Easy-to-Use Interface:
Our intuitive interface ensures a seamless user experience. Effortlessly input your desired currencies and amounts for instant conversion.

Real-Time Exchange Rates:
Stay up-to-date with the latest exchange rates. Our platform fetches real-time data, guaranteeing accuracy in every transaction.

Wide Range of Currencies:
We support a diverse array of currencies from around the world. Select your source and target currencies from our comprehensive list.

Responsive Design:
Access our currency converter on any device - desktop, tablet, or mobile. Our responsive design ensures functionality and aesthetics across platforms.

Historical Data:
Track currency trends by accessing historical exchange rate data. Make informed decisions based on past performance.

Customization Options:
Tailor your experience with customizable features. Set default currencies, adjust decimal places, and personalize your settings.

No Hidden Fees:
We believe in transparency. Our currency converter is free to use, with no hidden fees. The displayed rates are what you get.

Currency News and Insights:
Stay informed about the latest currency news and market insights. Our platform provides valuable information to aid your financial decisions.

Secure Transactions:
Rest easy knowing that your transactions are secure. We prioritize user privacy and employ the latest security measures to protect your data.

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[ecbf87a62a...](https://github.com/kleinerm/Psychtoolbox-3/commit/ecbf87a62a1453ea5ebea95325203e099a3a75c3)
#### Thursday 2023-11-16 06:43:44 by Mario Kleiner

PsychOpenXR: Add initial eyetracking via HTC SRanipal.

Requires SRAnipalMex to work and on the path, otherwise standard OpenXR eyetracking is
used. The mex file and source code is not yet included in the Psychtoolbox distribution.

This works with and requires the HTC proprietary SRanipal eye tracking api for MS-Windows,
in combination with a supported HTC HMD, e.g., HTC Vive Pro Eye (tested) or HTC Vive Cosmos
or HTC Vive Focus 3 with eye tracker hardware extension, the latter two untested, but assumed
to work in the same way.

It allows binocular eye tracking for left and right eye separately, returning two separate eye
gaze samples. Additionally a 3rd combined "cyclops eye" sample is returned, which is the fusion
or average of the two eye gaze samples, similar (identical?) to what HTC's implementation of
the OpenXR XR_EXT_eye_gaze_interaction extension returns as sole eye pose.

Implementation notes:

While OpenXR eye tracking with the standard OpenXR extension only works with a maximum
sampling rate of 60 Hz, ie. blocking the calling code for approximately 16 msecs for each
query in PsychVRHMD('PrepareRender') or PsychOpenXRCore('GetTrackingState', ..., 4), this
works with up to native sampling rate of the eyetracker, in this case 120 Hz / one sample
every approximately 8.3 msecs. As it turns out, one needs to use the callback api to get max
rate and minimum latency/overhead, where our callback is called from SRanipals own thread.
With the non-callback api's it is always blocking calls with 16 msecs+ duration resulting in poor
performance. The latter seems to be what HTC's implementation of OpenXR eyetracking does.

The HTC proprietary api delivers more detailed info than current official OpenXR extensions,
so both from a performance perspective and richness of information perspective it is clearly
perferrable to use the HTC proprietary api when available on a HTC HMD. The quality of the
api docs is horrifying however, and often faulty, so using it is somewhat a pain in the ass.

The type and units of returned information from SRanipal is different from what OpenXR
returns or uses, so some hacks had to be used to sort-of convert to OpenXR compliant format.

Currently the raw gaze samples are not 7 component vectors with eye position (x,y,z) and
orientation quaternion (rx,ry,rz,rw), but only 6 component vectors with orientation encoded
differently, and some shady matrix math hacks to get a sort of usable / sort of ok'ish gazeMat
matrix for eyegaze out of it. From that we derive other info like global gaze matrix, 3D eye
gaze vectors and 2D (x,y) gaze sample positions the usual way via the code shared with
regular OpenXR gaze tracking.

Some oddities - the reason for these is totally unclear:

- We need to switch some signs in the math - Is it a bug in HTC's runtime? A feature? A quirk?
I don't know.

- Eye center of the left eye seems to be stored in right eye, and vice versa, but the end result
wrt. 2D gaze position is the same, and the 3D gaze vectors originate in puzzling locations but
point to and converge in the correct gaze location. Again, could not find out why.

---
## [Cicada-Software/cicada](https://github.com/Cicada-Software/cicada)@[65fbf87d42...](https://github.com/Cicada-Software/cicada/commit/65fbf87d42dc563afdc9893de4f5cc343782aee0)
#### Thursday 2023-11-16 07:11:17 by dosisod

Allow for connecting Gitlab repositories to Cicada:

Users now have the ability to login with Gitlab and connect their repositories
to Cicada without the need to self-host Cicada. Previously users needed to
manually create webhooks and personal access tokens, which meant you could only
recieve webhook events from one Gitlab project/group. Now users have a UI in
Cicada that they use to can add webhooks to their existing Gitlab projects, and
Cicada will handle the creation and recieving of webhook events for you. This
brings Gitlab support much closer to Github, though there are still a few
things which have been left for the time being:

* Ability to add webhooks to groups. Currently you can have to attach Cicada to
  all your repos, or only a select few. In either case, Cicada cannot detect
  when a new repository is created, and thus cannot add new webhooks to new
  repositories. A solution would be to add support for group webhooks, though
  I have been working on this feature for long enough and I don't want to add
  more feature creep.

* UI for adding repositories could use some better cosmetics. This screen does
  work, but it is far from perfect, and could use some extra love. The main
  issue is that the UI freezes when making the API call to get the project
  list, though this should be easily fixable. In addition, checkboxes next to
  projects that already have webhooks are not checked when loading the list
  again, meaning you don't have an easy way to see what repos you have
  installed.

* Documenting new changes. This can be added later, and given how little people
  use Cicada let alone self host, this should be fine to leave out for the time
  being.

I also had to change a few things on the backend to get this to work. The
following list only applies to Gitlab:

* User OAuth tokens are stored on the backend when logging in. This is done
  because the `api` scope is needed to make all the required API calls, so
  storing this on the client is asking for trouble. With that being said, the
  tokens are stored in the db using Fernet symmetric cryptography, so in the
  event of a SQL injection or data breach, these tokens should be secure.

* Gitlab webhooks are required to use an `id` parameter to authenticate.
  Because Gitlab doesn't have a mechanism for seeing the hook id of the webhook
  that is sending the webhook, an id is added to the URL during creation of
  the webhook so that the data being sent can be correlated to a user account.

* Gitlab webhook secrets/tokens are now hashed. Previously the secret token was
  stored in plaintext, but since the token is only used to compare against the
  `x-gitlab-token` header, the token can be hashed and stored. This wasn't a
  big deal when Cicada could only have one Gitlab webhook, but now that there
  is essentially a webhook per project, making sure the webhooks are secure is
  a much higher priority. In addition, a unique token/secret is used for each
  webhook and is sent in plaintext only during the webhook creation, meaning
  the raw token is never stored in Cicada, only the hashed version is stored.

There are a few other details that I am leaving out for brevity, but in short
this greatly improves the user experience for users using Gitlab with Cicada.

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[6fefc9ce0e...](https://github.com/Ben10Omintrix/tgstation/commit/6fefc9ce0eb09b9b97e3d54609ace23c43601394)
#### Thursday 2023-11-16 07:20:06 by Andrew

Pipe painting, spraycan preset colors (#79521)

![dreamseeker_AZs0erdnrs](https://github.com/tgstation/tgstation/assets/3625094/06a12d22-387b-4a33-8b61-59bbe3495c82)

## About The Pull Request

Made pipe painter properly paint pipe colors, work on pipe items, and
added the same functionality to regular spraycans.

Spraycans now have the color presets in UI for easier selection of the
valid pipe colors.

## Why It's Good For The Game

Bug fixing is good.
It was weird that spraycans couldn't paint pipes, but some other device
could.
Also custom spraycan color is too clunky, presets are nice for quick
spraycan color selection.

## Changelog

:cl:
fix: fixed pipe painter not applying pipe color properly
qol: made spraycans work also as pipe painters
qol: spraycans now have basic color presets for quick selection
/:cl:

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[b6c06e216b...](https://github.com/magnetophon/nixpkgs/commit/b6c06e216bb3bface40eb8ea6576b25f9b2971dd)
#### Thursday 2023-11-16 07:36:09 by Charles Strahan

ruby: new bundler infrastructure

This improves our Bundler integration (i.e. `bundlerEnv`).

Before describing the implementation differences, I'd like to point a
breaking change: buildRubyGem now expects `gemName` and `version` as
arguments, rather than a `name` attribute in the form of
"<gem-name>-<version>".

Now for the differences in implementation.

The previous implementation installed all gems at once in a single
derivation. This was made possible by using a set of monkey-patches to
prevent Bundler from downloading gems impurely, and to help Bundler
find and activate all required gems prior to installation. This had
several downsides:

* The patches were really hard to understand, and required subtle
  interaction with the rest of the build environment.
* A single install failure would cause the entire derivation to fail.

The new implementation takes a different approach: we install gems into
separate derivations, and then present Bundler with a symlink forest
thereof. This has a couple benefits over the existing approach:

* Fewer patches are required, with less interplay with the rest of the
  build environment.
* Changes to one gem no longer cause a rebuild of the entire dependency
  graph.
* Builds take 20% less time (using gitlab as a reference).

It's unfortunate that we still have to muck with Bundler's internals,
though it's unavoidable with the way that Bundler is currently designed.
There are a number improvements that could be made in Bundler that would
simplify our packaging story:

* Bundler requires all installed gems reside within the same prefix
  (GEM_HOME), unlike RubyGems which allows for multiple prefixes to
  be specified through GEM_PATH. It would be ideal if Bundler allowed
  for packages to be installed and sourced from multiple prefixes.
* Bundler installs git sources very differently from how RubyGems
  installs gem packages, and, unlike RubyGems, it doesn't provide a
  public interface (CLI or programmatic) to guide the installation of a
  single gem. We are presented with the options of either
  reimplementing a considerable portion Bundler, or patch and use parts
  of its internals; I choose the latter. Ideally, there would be a way
  to install gems from git sources in a manner similar to how we drive
  `gem` to install gem packages.
* When a bundled program is executed (via `bundle exec` or a
  binstub that does `require 'bundler/setup'`), the setup process reads
  the Gemfile.lock, activates the dependencies, re-serializes the lock
  file it read earlier, and then attempts to overwrite the Gemfile.lock
  if the contents aren't bit-identical. I think the reasoning is that
  by merely running an application with a newer version of Bundler, you'll
  automatically keep the Gemfile.lock up-to-date with any changes in the
  format. Unfortunately, that doesn't play well with any form of
  packaging, because bundler will immediately cause the application to
  abort when it attempts to write to the read-only Gemfile.lock in the
  store. We work around this by normalizing the Gemfile.lock with the
  version of Bundler that we'll use at runtime before we copy it into
  the store. This feels fragile, but it's the best we can do without
  changes upstream, or resorting to more delicate hacks.

With all of the challenges in using Bundler, one might wonder why we
can't just cut Bundler out of the picture and use RubyGems. After all,
Nix provides most of the isolation that Bundler is used for anyway.

The problem, however, is that almost every Rails application calls
`Bundler::require` at startup (by way of the default project templates).
Because bundler will then, by default, `require` each gem listed in the
Gemfile, Rails applications are almost always written such that none of
the source files explicitly require their dependencies. That leaves us
with two options: support and use Bundler, or maintain massive patches
for every Rails application that we package.

Closes #8612

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[65592837b6...](https://github.com/magnetophon/nixpkgs/commit/65592837b6e62fb555d6e8c891f347428886c4f2)
#### Thursday 2023-11-16 07:39:51 by Thomas Tuegel

freetype: 2.6.5 -> 2.7.1

The Infinality bytecode interpreter is removed in favor of the new v40 TrueType
interpreter. In the past, the Infinality interpreter provided support for
ClearType-style hinting instructions while the default interpreter (then v35)
provided support only for original TrueType-style instructions. The v40
interpreter corrects this deficiency, so the Infinality interpreter is no longer
necessary.

To understand why the Infinality interpreter is no longer necessary, we should
understand how ClearType differs from TrueType and how the v40 interpreter
works. The following is a summary of information available on the FreeType
website [1] mixed with my own editorializing.

TrueType instructions use horizontal and vertical hints to improve glyph
rendering. Before TrueType, fonts were only vertically hinted; horizontal hints
improved rendering by snapping stems to pixel boundaries. Horizontal hinting is
a risk because it can significantly distort glyph shapes and kerning. Extensive
testing at different resolutions is needed to perfect the TrueType
hints. Microsoft invested significant effort to do this with its "Core fonts for
the Web" project, but few other typefaces have seen this level of attention.

With the advent of subpixel rendering, the effective horizontal resolution of
most displays increased significantly. ClearType eschews horizontal hinting in
favor of horizontal supersampling. Most fonts are designed for the Microsoft
bytecode interpreter, which implements a compatibility mode with
TrueType-style (horizontal and vertical) instructions. However, applying the
full horizontal hints to subpixel-rendered fonts leads to color fringes and
inconsistent stem widths. The Infinality interpreter implements several
techniques to mitigate these problems, going so far as to embed font- and
glyph-specific hacks in the interpreter. On the other hand, the v40 interpreter
ignores the horizontal hinting instructions so that glyphs render as they are
intended to on the Microsoft interpreter. Without the horizontal hints, the
problems of glyph and kerning distortion, color fringes, and inconsistent stem
widths--the problems the Infinality interpreter was created to solve--simply
don't occur in the first place.

There are also security concerns which motivate removing the Infinality patches.
Although there is an updated version of the Infinality interpreter for FreeType
2.7, the lack of a consistent upstream maintainer is a security concern. The
interpreter is a Turing-complete virtual machine which has had security
vulnerabilities in the past. While the default interpreter is used in billions
of devices and is maintained by an active developer, the Infinality interpreter
is neither scrutinized nor maintained. We will probably never know if there are
defects in the Infinality interpreter, and if they were discovered they would
likely never be fixed. I do not think that is an acceptable situtation for a
core library like FreeType.

Dropping the Infinality patches means that font rendering will be less
customizable. I think this is an acceptable trade-off. The Infinality
interpreter made many compromises to mitigate the problems with horizontal
hinting; the main purpose of customization is to tailor these compromises to the
user's preferences. The new interpreter does not have to make these compromises
because it renders fonts as their designers intended, so this level of
customization is not necessary.

The Infinality-associated patches are also removed from cairo. These patches
only set the default rendering options in case they aren't set though
Fontconfig. On NixOS, the rendering options are always set in Fontconfig, so
these patches never actually did anything for us!

The Fontconfig test suite is patched to account for a quirk in the way PCF fonts
are named.

The fontconfig option `hintstyle` is no longer configurable in NixOS. This
option selects the TrueType interpreter; the v40 interpreter is `hintslight` and
the older v35 interpreter is `hintmedium` or `hintfull` (which have actually
always been the same thing). The setting may still be changed through the
`localConf` option or by creating a user Fontconfig file.

Users with HiDPI displays should probably disable hinting and antialiasing: at
best they have no visible effect.

The fontconfig-ultimate settings are still available in NixOS, but they are no
longer the default. They still work, but their main purpose is to set rendering
quirks which are no longer necessary and may actually be
detrimental (e.g. setting `hintfull` for some fonts). Also, the vast array of
font substitutions provided is not an appropriate default; the default setting
should be to give the user the font they asked for.

[1]. https://www.freetype.org/freetype2/docs/subpixel-hinting.html

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[407db7b019...](https://github.com/magnetophon/nixpkgs/commit/407db7b0196417296677f2a4ef929bb092ec382b)
#### Thursday 2023-11-16 07:41:25 by Jan Tojnar

gtk_doc: replace catalog lookup hack

In the previous commit, we added a setup hook to docbook dtd and xsl
packages, that adds derivation’s catalog file to an environment variable.
That should, in theory, remove the need for declaring their catalogs manually.
Unfortunately, xmlcatalog utility expects exactly one catalog file, completely
disregarding the environment variable in non-interactive context. In the same
spirit, the design of gtk-doc m4 files only admits a single catalog file,
resulting in another ugly hack.

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[b3d5ca8359...](https://github.com/magnetophon/nixpkgs/commit/b3d5ca8359d3fac0f21ccece79c202557a9433b5)
#### Thursday 2023-11-16 07:44:16 by aszlig

nixos/dhparams: Set default bit size to 2048

@Ekleog writes in https://github.com/NixOS/nixpkgs/pull/39526:

> I think a default of 4096 is maybe too much? See certbot/certbot#4973;
> Let's Encrypt supposedly know what they are doing and use a
> pre-generated 2048-bit DH params (and using the same DH params as
> others is quite bad, even compared to lower bit size, if I correctly
> remember the attacks available -- because it increases by as much the
> value of breaking the group).

> Basically I don't have anything personal against 4096, but fear it may
> re-start the arms race: people like having "more security" than their
> distributions, and having NixOS already having more security than is
> actually useful (I personally don't know whether a real-size quantum
> computer will come before or after our being able to break 2048-bit
> keys, let alone 3072-bit ones -- see wikipedia for some numbers).

> So basically, I'd have set it to 3072 in order to both decrease build
> time and avoid having people setting it to 8192 and complaining about
> how slow things are, but that's just my opinion. :)

While he suggests is 3072 I'm using 2048 now, because it's the default
of "openssl dhparam". If users want to have a higher value, they can
still change it.

Signed-off-by: aszlig <aszlig@nix.build>

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[a8e9dfafe9...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/a8e9dfafe92f940a1445c298b20e1e8e0b8b51c6)
#### Thursday 2023-11-16 07:54:36 by kleinerm

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
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[62e34d1c87...](https://github.com/magnetophon/nixpkgs/commit/62e34d1c87ee8436bfa8ceaeac07ea3855fabd43)
#### Thursday 2023-11-16 07:55:04 by Emily

nixos/acme: change default keyType to ec256

Previously, the NixOS ACME module defaulted to using P-384 for
TLS certificates. I believe that this is a mistake, and that we
should use P-256 instead, despite it being theoretically
cryptographically weaker.

The security margin of a 256-bit elliptic curve cipher is substantial;
beyond a certain level, more bits in the key serve more to slow things
down than add meaningful protection. It's much more likely that ECDSA
will be broken entirely, or some fatal flaw will be found in the NIST
curves that makes them all insecure, than that the security margin
will be reduced enough to put P-256 at risk but not P-384. It's also
inconsistent to target a curve with a 192-bit security margin when our
recommended nginx TLS configuration allows 128-bit AES. [This Stack
Exchange answer][pornin] by cryptographer Thomas Pornin conveys the
general attitude among experts:

> Use P-256 to minimize trouble. If you feel that your manhood is
> threatened by using a 256-bit curve where a 384-bit curve is
> available, then use P-384: it will increases your computational and
> network costs (a factor of about 3 for CPU, a few extra dozen bytes
> on the network) but this is likely to be negligible in practice (in a
> SSL-powered Web server, the heavy cost is in "Web", not "SSL").

[pornin]: https://security.stackexchange.com/a/78624

While the NIST curves have many flaws (see [SafeCurves][safecurves]),
P-256 and P-384 are no different in this respect; SafeCurves gives
them the same rating. The only NIST curve Bernstein [thinks better of,
P-521][bernstein] (see "Other standard primes"), isn't usable for Web
PKI (it's [not supported by BoringSSL by default][boringssl] and hence
[doesn't work in Chromium/Chrome][chromium], and Let's Encrypt [don't
support it either][letsencrypt]).

[safecurves]: https://safecurves.cr.yp.to/
[bernstein]: https://blog.cr.yp.to/20140323-ecdsa.html
[boringssl]: https://boringssl.googlesource.com/boringssl/+/e9fc3e547e557492316932b62881c3386973ceb2
[chromium]: https://bugs.chromium.org/p/chromium/issues/detail?id=478225
[letsencrypt]: https://letsencrypt.org/docs/integration-guide/#supported-key-algorithms

So there's no real benefit to using P-384; what's the cost? In the
Stack Exchange answer I linked, Pornin estimates a factor of 3×
CPU usage, which wouldn't be so bad; unfortunately, this is wildly
optimistic in practice, as P-256 is much more common and therefore
much better optimized. [This GitHub comment][openssl] measures the
performance differential for raw Diffie-Hellman operations with OpenSSL
1.1.1 at a whopping 14× (even P-521 fares better!); [Caddy disables
P-384 by default][caddy] due to Go's [lack of accelerated assembly
implementations][crypto/elliptic] for it, and the difference there seems
even more extreme: [this golang-nuts post][golang-nuts] measures the key
generation performance differential at 275×. It's unlikely to be the
bottleneck for anyone, but I still feel kind of bad for anyone having
lego generate hundreds of certificates and sign challenges with them
with performance like that...

[openssl]: https://github.com/mozilla/server-side-tls/issues/190#issuecomment-421831599
[caddy]: https://github.com/caddyserver/caddy/blob/2cab475ba516fa725d012f53ca417c3e039607de/modules/caddytls/values.go#L113-L124
[crypto/elliptic]: https://github.com/golang/go/tree/2910c5b4a01a573ebc97744890a07c1a3122c67a/src/crypto/elliptic
[golang-nuts]: https://groups.google.com/forum/#!topic/golang-nuts/nlnJkBMMyzk

In conclusion, there's no real reason to use P-384 in general: if you
don't care about Web PKI compatibility and want to use a nicer curve,
then Ed25519 or P-521 are better options; if you're a NIST-fearing
paranoiac, you should use good old RSA; but if you're a normal person
running a web server, then you're best served by just using P-256. Right
now, NixOS makes an arbitrary decision between two equally-mediocre
curves that just so happens to slow down ECDH key agreement for every
TLS connection by over an order of magnitude; this commit fixes that.

Unfortunately, it seems like existing P-384 certificates won't get
migrated automatically on renewal without manual intervention, but
that's a more general problem with the existing ACME module (see #81634;
I know @yegortimoshenko is working on this). To migrate your
certificates manually, run:

    $ sudo find /var/lib/acme/.lego/certificates -type f -delete
    $ sudo find /var/lib/acme -name '*.pem' -delete
    $ sudo systemctl restart 'acme-*.service' nginx.service

(No warranty. If it breaks, you get to keep both pieces. But it worked
for me.)

---
## [moreginger/Zero-K](https://github.com/moreginger/Zero-K)@[5e2b1657be...](https://github.com/moreginger/Zero-K/commit/5e2b1657be4cd0d9d7975eb434cc40c9a350ee1b)
#### Thursday 2023-11-16 08:06:53 by Helwor

Big update, various improvements and fixes, slight rewrite

-Adapted my code to be compatible with the Zero-K version

-Rewrote slightly the code to be more concise and efficient

-Fixed: The Zero-K version is broken since an edit made Sep 2020 (!) when user start to change spacing, the rectangles would never disappear because newspacing variable was never falsified at the end of the  Update round.

-Fixed: the param for spTraceScreenRay was the opposite of what it should be

-Improvement: The widget now adapt to the wrong engine grid which is off and also sometimes misleading when it comes to place units on water

-Added: On this particular case, widget gives the possibility for the user to either follow the grid coherence, or show the reality of where the unit will actually be placed. In that case, an extra rect is drawn to see where the first placement will land.  By usage, it seems the latter is more interesting so I put it on by default.
(More details in the comments that could help fix the problem with the engine)

-Improvement: the option panel now stop resetting scroll anytime an option is changed, this fix could easily be implemented universally by changing WG.crude.OpenPath, all it have to do is remembering 'scrollPosY' of the last panel and apply it to the new.

-Added: an option  for the user to choose wether rects should spread straightforward (if user want to only have a basic glance of the separation with no simulation of placing on the ground) or follow the ground, as it was before. I'm undecided which is the best as default for new users.

-Added: an option to have different colors of rects for bad placements, this on default if follow ground is on default, it seems to be adding a plus mostly in this case.

-Changed Description that's been edited, it does not just memorize spacing. I understand that it need to be concise, but a description is meant also to say what it does. User won't be able to tell if that widget make the previsualization or add mouse wheel to spacing by reading its description.

-Changed back title of an option. The purpose of how they are written is to build a sentence obviously, to make it more straightforward and user friendly. This change broke that concept. When user, especially new user, dive into options they can be lost as I was, to understand what option do what, if the option is dependent of another, etc... that's the purpose of my system to make all that as clear as I can.

-Changed back some default for new user, I think having the shift+mousewheel is a must, it's faster and more convenient, especially when discovering the game. I would have been glad to have that when I started, (that's, by the way, why I rewrote this widget in the first place).
Also changed back previsualization, with only 2 rects and only when spacing change, and for 0.7 sec
It is, in my opinion, also much more convenient for a new user to be able to see in a quick glance how your placement will be separated without the need of start posing queue and THEN realize the spacing is not good. If non-new user get tired of it, they will be able to find the options to undo it.
Indeed, new user will not be anymore really a new user when he discovers previsualization, if it's not on by default.

-Few minor things:
  -preGame is now set by GameFrame and then GameFrame removes itself
  -MouseWheel gets added/removed whenever shift+wheel option is changed
  -I don't see any reason to change the name spaced_rects in spaced_rects_2. As far as I know, one can only want that for resetting his own option to default for testing  purpose. Reverted it since it didn't make sense.
  -Upped the max time before infinite for show value and show rects to 10 sec
  -Didn't reverted it but imho, changing 'p' to 'placement' made the code uselessly more cumbersome than it already is.
  -Changed 'if not placementCache[unitDefID] then'  to 'if not placeTable[unitDefID] then' as the code was intended to mean
  note about this: since the vast majority of building have same sizex and sizez, maybe it could be improved by checking if it's relevant to consider the off-facing in 
  before.
 -Estomped the double dots before option titles when they are active, to make them less present.
 -update placement on more relevant changement of facing
 -Made the options defaults in concordance with the widget defaults
 -And maybe some other stuff I forgot

Lots of change, so please, let me know what you think.

---
## [mogeoko/tgstation](https://github.com/mogeoko/tgstation)@[bed92e193c...](https://github.com/mogeoko/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Thursday 2023-11-16 08:13:23 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[7553d0fe29...](https://github.com/magnetophon/nixpkgs/commit/7553d0fe29801938bcb280bb324b579ef9016aea)
#### Thursday 2023-11-16 08:23:01 by Adam Joseph

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
## [Rebolon/angular-fork-scroller](https://github.com/Rebolon/angular-fork-scroller)@[acd59ad037...](https://github.com/Rebolon/angular-fork-scroller/commit/acd59ad0371a19838813cfc934a73fa3cc357602)
#### Thursday 2023-11-16 08:32:19 by Ward Bell

docs: Migrate Observables guides & code examples to standalone (#51516)

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Moved the multi-casting section to  "RxJS Library" and rewrote it (with working example) for simplicity and context.

I made other changes in an effort to make this an overview that is  more comprehensive and more clear. I paid particular attention to the "Basic usage and terms" section.

Finally, I relocated the "Naming conventions for observables" section here from `rx-library`. This is the section that describes the dollar-sign convention. It made more sense for it to be here.

**Revised "RxJS Library" page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

**Revised "Comparing observables"**

The Promises section in `comparing-observables.md` had many errors and misleading remarks.

The comparison of error handling was especially egregious; the code example for that was nonsense.

The "Chain" sub-section was really about transforming values. It also failed to demonstrate chaining promise `.then`s.

Reworked these sub-sections and improved the code samples to match.

PR Close #51516

---
## [qx1147/Psychtoolbox-3](https://github.com/qx1147/Psychtoolbox-3)@[39c32e5eb7...](https://github.com/qx1147/Psychtoolbox-3/commit/39c32e5eb7500805b68e62c078a91f47d3ef43d2)
#### Thursday 2023-11-16 08:46:40 by kleinerm

Merge pull request #797 from Psychtoolbox-3/master

Psychtoolbox 3.0.19.0 "Virtuality"

### Compatibility:

- Effective now, Psychtoolbox 3.0.18 is end of life and unsupported.

- GStreamer 1.20.5 or later required on MS-Windows, GStreamer 1.22.0 recommended on
  Windows and macOS.

- Octave 6 support cancelled, except for Linux. Octave 7.3 required on macOS and
  Windows.

- New baseline Matlab is R2022b.

- Recommended operating systems: Ubuntu 22.04-LTS Linux, MS-Windows 10, macOS 12.6.

- Ubuntu 20.04-LTS is considered in maintenance mode now. I will likely terminate its
  support in the foreseeable future. Lack of funding by our users makes it impossible
  to provide the levels of long term support as in the past, even for the best suited
  operating system for neuroscience :(.
  
- RaspberryPi OS 10 support is terminated. OS 11 32-Bit required.

- Support for all Windows versions older than recent Windows-10 will soon be completely
  removed. Stick to older Psychtoolbox versions if you want to continue older versions
  for some insane reason. All Windows versions older than Windows 10 are now dead, even
  for Microsoft customers which paid for expensive extended security support.
  It is dead, Jim!

- The macOS 10 (aka Mac OSX) and macOS 11 operating systems should continue to work
  but are officially unsupported and unsupportable. macOS 13 or Apple Silicon is not
  officially supported by this release.

### Highlights:

- OpenXR cross-platform, cross-vendor, cross-device support for VR/AR/MR/XR applications.
  A new modern foundation for these kind of things, highly extensible, future proof, and
  supports a much wider range of devices.

- Improved display mirroring support, including scaling and experimenter overlays for
  having setups with a stimulus monitor for the subject and a "experimenter console" /
  "experimenter control monitor" for the experimenter. PTB is still the only software
  that allows such setups without expensive special hardware and/or screwing up visual
  stimulation timing and timestamping. There are still corner cases where this is difficult,
  but we are better than ever now, increasing our lead over other toolkits further.

- Improved low-level USB support, especially useful for the PsyCalibrator toolbox for
  display calibration under Octave and Matlab.

- ASIO support for Matlab users on Windows sort-of back through the backdoor, without
  us actually having to add it back or dealing with the legal and licensing nightmares.

- Shitloads of new workarounds for shittons of new bugs brought to you by the iPhone
  company in their latest iToys operating systems.

### All:

- The main new feature, after over 700 hours of development, spread over 12 months,
  is our new OpenXR driver for virtual reality, augmented reality and mixed reality
  applications, known as eXtended Reality. The new PsychOpenXR driver should work on
  all VR/AR/MR/XR devices from all vendors on all operating systems which have an
  OpenXR 1 specification compliant runtime installed on your machine. So far the theory.
  In practice, this means GNU/Linux X11 and MS-Windows 10 and later, and so far it has
  only be tested with an Oculus Rift CV-1 VR HMD and Oculus touch controllers, remote
  and XBox 360 controller. Code for using other form-factors than VR HMD's is not yet
  implemented, but this driver should provide the foundation for relatively extension
  into this new realms if wanted. The whole topic deserves its own dedicated and detailed
  posts, so stay tuned. Some more overview info and setup instructions are to be found via
  'help OpenXR', the new drivers specific api in 'help PsychOpenXR', the general api
  improvements and help - sufficient for most use cases - in 'help PsychVRHMD', as before.
  Development of this driver was sponsored by a consumer VR company which wants to stay
  anonymous and not specifically credited here, so thank you for contributing most of the
  funding. As funding was insufficient to complete this very complex project, Mathworks
  (https://www.mathworks.com/solutions/neuroscience.html) sponsored another quarter of the
  remaining costs, thanks! Of course that means some other highly interesting project had
  to be delayed indefinitely, as the amount of funding we get from Mathworks is fixed, just
  the distribution of the fixed some to work items is flexible. In total, funding was totally
  insufficient for making any urgently needed profit or even breaking even nonetheless, so we
  end this one year project with a serious net loss of over 3000 Euros at this point, without
  the project being finished to my quality and performance standards, barely reaching what I
  would consider the minimum viable product from my perspective, but almost certainly still
  much better than anything competing out there for vision science applications. I expect
  more financial losses related to this area of functionality unless new contract work or
  funding come in, related to OpenXR aka VR/AR/MR/XR applications.

  The new driver should be reasonably backwareds compatible, essentially a drop-in replacement,
  so code written to our recommendations should work unchanged, just on a much wider variety
  of VR hardware than before.

  Effective immediately this means that all our old drivers are now considered to be in
  minimal maintenance mode - critical bug fixes only, no further enhancements. They are
  scheduled for removal as soon as the OpenXR driver has proven its maturity to some degree.

- Tons of minor bug fixes and improvements.

- PsychPortAudio: Improve diagnostics and help texts for channel mapping, and a new demo for
  multi-channel audio output, named BasicSoundChannelHoppingDemo.m which motivated those
  improvements, demonstrating dynamic switching between channels of a multi-channel sound card,
  e.g., hopping between the channels of a 24 channel sound card.

- SetStereoSideBySideParameters(): Add option to specify offsets in pixels, and add basic
  RemapMouse() support to deal better with changed stereo display geometry. Various other
  compatibility fixes to SetStereoSideBySideParameters() and RemapMouse() in combination with
  stereo display modes in combination with imaging pipeline geometric transformations like
  FlipHorizontal or FlipVertical. Also for 90 degree step rotation with the PanelFitter.

- Screen: Fix PsychImaging task 'MirrorDisplayTo2ndOutputHead' for most use cases.
  Turns out that this display mirroring task for macOS and MS-Windows only worked for
  trivial configurations without use of the panelfitter, MSAA, image processing or other
  complexities. It also works now when combined with the Vulkan special purpose display
  backend as primary stimulus display and the regular OpenGL method for the "experimenter
  feedback" / "control console" mirror display.

- Add overlay support to the display mirroring tasks 'MirrorDisplayTo2ndOutputHead' and
  'MirrorDisplayToSingleSplitWindow'. The new optional useOverlay parameter for these
  PsychImaging tasks generates a (normally transparent) overlay window, a "head up display"
  on top of the mirror window that shows a mirror image of the stimulus presented to the
  subject on the main stimulation display. overlaywin = PsychImaging('GetMirrorOverlayWindow', win);
  allows to get a window handle overlaywin to this overlay and then use Screen drawing commands
  to draw info only meant to be seen by the experimenter, not the subject, into the overlay.
  A common use case seems to be gaze position or gaze traces of a subject in eyetracking tasks,
  or other live feedback about task progression and subject performance. This is generally
  more flexible than hardware solutions, e.g., as provided by VPixx stimulators or similar
  equipment or some display splitters.

- PsychImaging: Allow size spec of mirror image for mirroring task 'MirrorDisplayToSingleSplitWindow'.
  Dealing with setups where the mirror/console/experimenter monitor has a lower/different resolution
  than the stimulus monitor needs same special rescaling of the mirror image. Implement rescaling +
  some minor optimizations. A future extension may allow to automate handling of such less standard
  display setups, but for now the user has to specify mirror monitor display resolution manually via
  a new optional parameter.

- PsychHID: Add support for synchronous USB bulk and interrupt transfers, and manual of automatic
  claiming of USB interfaces. The new subfunctions 'USBBulkTransfer' and 'USBInterruptTransfer'
  implement synchronous bulk and interrupt transfers. This now allows writing M-File drivers
  for more research equipment. The main motivation was to enable the free and open-source
  PsyCalibrator toolbox for Octave and Matlab to implement support for many more Photometers
  and other light measurement devices in a more efficient manner, starting with the cheap
  SpyderX device. Cfe. https://github.com/yangzhangpsy/PsyCalibrator

- PsychHID: Add PsychHID('USBClaimInterface', usbHandle, interfaceId) for manual claiming of
  device interfaces. This function allows to explicitely claim a USB interface to enable it
  for I/O from/to an USB interface endpoint. Bulk- or interrupt transfers don't work if the
  interface who owns the endpoint has not been claimed. If a call to this function is omitted
  before doing bulk or interrupt transfers, then PsychHID will automatically claim interface 0.
  Claimed interfaces are auto-released when closing an USB device. Kernel drivers potentially
  attached to - and blocking - an interface will be automatically detached, and then reattached
  at device close. In other words: Use of the most commonly used interface 0 does not need any
  extra user code. Use of other interfaces will require this call in time.

  On macOS: Note that if a macOS kernel driver (kext) has already claimed exclusive access to the
  device, then this will only work by detaching the kernel driver, which requires you to run Octave
  or Matlab as root. Only tested by myself with octave via "sudo octave" so far. For the hoops you
  have to jump through on macOS to get this working without sudo, read this FAQ:

  https://github.com/libusb/libusb/wiki/FAQ#how-can-i-run-libusb-applications-under-mac-os-x-if-there-is-already-a-kernel-extension-installed-for-the-device-and-claim-exclusive-access

  Executive summary: Give up, or be prepared to suffer greatly!

- Various help text and documentation updates.

- Terminate support for Python 2.x, it is officially end-of-life since beginning 2020. Only
  Python 3.6 and later are supported by our Python "Mex files" going forward. This makes the
  files also forward compatible with more Python versions by opt-in use of the Py limited api.
  Contributed mostly by Alex Forrence, with some tweaks by Mario Kleiner. Various other minor
  enhancements to PsychPython.
  
### Linux:

- Add support for 64-Bit Octave 7.x, implemented via the shared mex files for Octave 4.4 - Octave 7.3.
  This enables use with Octave on Ubuntu 22.10.

- Screen: Add gpu detection support for NVidia 170 "Ampere" gpu family and "Ada Lovelace" gpu
  family. Avoids some confusing warning and may improve Flip performance by a few dozen microseconds
  in some cases. Use of NVidia graphics cards is still discouraged due to the need of proprietary
  graphics drivers for all modern models, which limit useful functionality compared to gpus with
  open-source drivers, and make general use more tedious and troublesome.

- Drawtext plugin: Add workaround for Mesa bug with small non-anti-aliased text of 8 pixels and
  less. Rarely needed, but somebody in the VR research community needed it, so there.

- Compatibility fixes for the RaspberryPi on RaspberryPi OS 11 aka Debian 11 stable. Especially
  for old RPi 1,2,3 with VideoCore-4 gpu, XOrgConfCreator now generates a special xorg.conf
  file to enable fixes for these gpu's which were not neccessary on older RaspberryPi OS versions.
  Other misc compatibility improvements.
  
  Our build system for ARM / RaspberryPi is no 32-Bit RaspberryPi OS 11, with 32-Bit Octave 6.2,
  32-Bit ARM RaspberryPi 400. 64-Bit operating systems are not supported, and support for the
  legacy RaspberryPi OS 10 is now terminated.

- gamemode.ini: Comment out the amd_performance_level=high gpu perf option.
  Setting amd_performance_level=high for high performance level was found
  to cause stability issues at least on AMD Ryzen-5 2400G "RavenRidge" under
  Ubuntu 20.04.5-LTS with Linux 5.15 under prolonged load, likely a cooling problem.
  It may be safe to enable it for other AMD gpu's, especially well-cooled
  or discrete ones, but better safe than sorry by default, as i don't like
  my main devel machine crashing regularly and other users may also have machines
  with shaky cooling.


### Windows:

- 64-Bit Intel MSVC GStreamer version 1.20.5 is now required as minimum supported version
  for both Octave and Matlab. High quality text rendering will fail with any earlier version!
  From now on we always use the fontconfig-1.dll bundled with GStreamer 1.20.5 and later for
  font matching, which should simplify debugging of future issues on MS-Windows. This version
  also enables the ability to use User installed 3rd party fonts without extra configuration
  work by the user, obsoleting various hacks. GStreamer 1.22.0 was also lightly tested without
  obvious problems, so upgrading to 1.22.0 is recommended for new features, wider support for
  audio/video formats, improved performance and various bug fixes in the multi-media area.

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- PsychPortAudio: Allow use of a wider range of 3rd party portaudio_x64.dll plugins for the
  underlying PortAudio engine implementation. The most interesting use case of this is for
  users of Matlab, as recent versions of Matlab ship with a Mathworks provided Portaudio
  implementation that has builtin ASIO support, where all the legal licensing and trademark
  issues are taken care of by Mathworks. If one copies the DLL shipping with Matlab into the
  PsychtoolboxRoot() folder, renamed to the filename portaudio_x64.dll instead of the filename
  that Matlab uses (libportaudio.dll), then this will expose basic ASIO support, even when used
  with GNU/Octave. Please note that Mathworks is legally responsible for this ASIO support, whereas
  we do not include any support for ASIO into Psychtoolbox, we merely expose whatever a 3rd party
  portaudio DLL supports, which happens to be also ASIO in case of the Matlab provided dll, so we
  are legally in the clear, while some of our users may be more happy with their sound setup even
  if they refuse to switch to Linux. Obviously these 3rd party driver plugins are completely
  unsupported by us in case of trouble, and likely also by Mathworks, as this is not their intended
  use case, just a side-effect of some functionality that is probably meant for the audio toolbox.

- Update bundled libusb-1 for MS-Windows to most recent version 1.0.26 with many bug fixes and
  improvements over the last 11 years.

### macOS:

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave. Other Octave versions
  from the Octave 6.3+ and 7.x series may work as well, but no guarantees.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Switch only supported and lightly tested macOS version from 10.15 Catalina to 12 Monterey.
  No more development or testing on 10.15.7 Catalina, now that it has been wiped from my drive.
  We keep macosx-version-min at 10.11 for the time being, so PTB may still work back to 10.11,
  but no guarantees, and I don't care if it breaks on older systems than macOS 12.6 Monterey.
  macOS 13 Ventura is completely untested and not officially supported yet. Apple Silicon Macs
  continue to be unsupported and untested, with known completely broken visual stimulation timing
  and possible other issues. All mex files are for 64-Bit Intel processor architecture variants of
  Matlab and GNU/Octave only.

- PsychOculusVR: Remove for macOS. No VR virtual reality support on macOS anymore as of PTB 3.0.19.
  It only supported the long time out-of-sale since many years Oculus Rift DK1 and Rift DK2, with an
  Oculus v0.5 runtime for macOS that is not available for download from Oculus or anywhere else
  anymore since years, and only for macOS versions which supported 32-Bit Intel architecture executables,
  iow. doesn't work on macOS 10.15 Catalina and later anymore thanks to Apple breaking backwards
  compatibility with 32-Bit applications.

- Fix performance of PsychHID further for the latest Apple security bullshit, introduced sometime
  after macOS 10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey, a massive
  performance degradation for KbCheck and related functions if Matlab or Octave are launched from
  a terminal (iow. always for Octave!). Apple screwed up their api's further to increase processing
  time of some time sensitive operation from 1 msec to over 15 msec! Now we are back to about 2.4
  msecs on macOS 12, which is much worse than MS-Windows with less than 1 msecs or Linux with less
  than 0.1 msecs. So now it is merely Apple bad, as most Apple stuff.
  
- Screen: Unbreak our Vulkan display backend via MoltenVK Vulkan-on-Metal again for macOS 12, after
  Apple broke it somewhere after macOS 11. After close to 80 hours of diagnostic work, distributed
  over more than 4.5 months on and off, going down every conceivable route of diagnostics and low-level
  debugging, i could not find anything wrong with my code or MoltenVK. Turns out, it is yet another
  "dumb beyond imagination" bug in the iPhone companies latest macOS 12, nothing we did wrong. The
  root cause is unclear, but now we include a dumb hack which makes it work again, against any rhyme
  or reason. Of course, I don't know if Apple has broken it or will break it again in macOS 13 Ventura
  or later abominations. So basic HDR on macOS is back in the game...
  
- PsychHID: Switch low-level USB support to use of shared libusb-1 backend instead of Apples macOS
  proprietary backend, which became a maintenance nightmare. This now allows all operating systems
  to progress in the same way with shared high-quality code. It does mean however, that if one wants
  to use low-level USB device access, e.g., USB control-/bulk-/interrupt-transfers, one needs to
  install libusb-1.dylib with a minimum version of 1.0.22 from a suitable source, or these functions
  will refuse to work. The most simple way to get this library is via HomeBrew: brew install libusb
  
  The only affected Psychtoolbox function without libusb dylib is the ColorCal2() functions for using
  CRS ColorCal-II devices.

Enjoy!

---
## [Kawoo1/Kawoo1](https://github.com/Kawoo1/Kawoo1)@[0e4a173e56...](https://github.com/Kawoo1/Kawoo1/commit/0e4a173e56a5dc2752403c10771a11391f3fe00c)
#### Thursday 2023-11-16 08:54:29 by Kyle Shanahan

Update README.md

Included my lovely girlfriend because she noticed I did not mention her

---
## [yngrdyn/kibana](https://github.com/yngrdyn/kibana)@[cd909f03b1...](https://github.com/yngrdyn/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Thursday 2023-11-16 08:59:58 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [CollaboraOnline/online](https://github.com/CollaboraOnline/online)@[3185307c7a...](https://github.com/CollaboraOnline/online/commit/3185307c7afa5e76bd10b76a2d97ecbdbc97455a)
#### Thursday 2023-11-16 09:20:31 by Skyler Grey

Stop hiding both menu and notebookbar softlocking

Previously, when using the Collapse_Notebookbar postmessage or
equivalent ui_defaults (SpreadsheetToolbar=false, etc.), particularly in
compact mode, it was possible to additionally hide the menu bar. As the
button to show the menu bar is on the notebookbar, this meant that you
couldn't reactivate either notebookbar or menubar until you refreshed
the page. This is particularly annoying in integrators that may not
provide an easy way to reload the page

This commit makes it so that hiding the menu bar automatically
uncollapses the notebookbar and won't let it be collapsed again. Whether
the notebook bar should be collapsed (the last thing done to it was a
collapse) is remembered and restored after the menu bar is shown again,
so if you send a postmessage that will affect the state of the
notebookbar after the menu is shown (even though it will not affect the
notebookbar's state immediately)

Caveats:
- If you are hiding the notebookbar to limit the control the user has,
  that's broken by this commit as it makes it impossible to hide both
  the menu and notebook bars at the same time.
- The notebook bar will be hidden again when re-showing the menu bar,
  however there still isn't a way to hide the notebook bar in normal
  use (i.e. without using either postmessage or ui_defaults) while in
  compact mode (although there is a workaround to show it- switching
  into tabbed mode and then back!). It might be nice to have one.

Other considered solutions:
- We could add a new button that allowed you to reopen the menu if both
  menu and notebookbar were hidden
  - Not sure there's much benefit to this over just doing what we're
    doing here, and it's harder to implement
- We could disable the button to hide the menu bar when the notebookbar
  is collapsed
  - As far as I know, there's no button in the UI to show the notebook
    bar. This would make it impossible to hide the menu bar if the
    notebookbar was hidden via postmessage or ui_defaults

Signed-off-by: Skyler Grey <skyler.grey@collabora.com>
Change-Id: Ieab6d72a6be181aba88e9a5b21dda16a369b9e54

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[f2853cfe6e...](https://github.com/re621/dnpcache/commit/f2853cfe6eff91f0dfabffb1c22cdc9873a63056)
#### Thursday 2023-11-16 09:26:07 by bitWolfy

Remove 1236 artists from the DNP list.

Removed: tgt1512, mykendyke, cushylutra, leprosick, foxxy_vixen, defiant_drills, canphem, burneraccount9382, corgicam, meggiebun, reindeerbites, hmdkoba, electroporn, fluffytuft, moxsully, ottiro, volfislav, preschoolkaiju, titusw, pudgeruffian, garnetto, viomarks, tidekeeper, radiancemutt, livalittle, bootyfeather, sheriffpunchy, kkrevv, feralmunchies, sadcat16hrz, 2dredders, velvet_charm, saurian_(artist), zoyler, ruvark, draite, smuttysquid, demura, remanedur, electrixocket, fufik[pufik], kais_studios, sweat_(artist), sonokido, whimsicalsquirrel, woolier, dasherslash, caninesinzone, isabel9819, paradoxing, arrjaysketch, anomalain, iskawhiskers, troplilly, dio_fish, xxbrewbeastxx, thekoboldking, pantheradraws, callmems, bluthederg, avalony, kolvackh, fin6, lewdoreocat, temporarye, kitwran, pseudonymh, yeenmusk, varuiven, springledongle, sapphiesweet, bloodhawk, amiraallis, meowcephei, shupamikey, cracky45, bigblueghost, h0tapplecider, hxtapplecider, apocheck13, tomash_segers, pckle, sadbitch, geletulator, coille, azumadai124, greycore, snaxattacks, bootleggreely, coral_luna, mdwines, soakedbikini, pantyranger, diffusedlizard, kazz_a_fella, alkyuz, werewhusky, skooma_whore, october_nights, pehkeshi, scalywanderer, linndrim, hexamanta, anarietta, earthsong9405, captaincassidy, anthonynothere, gayluigisex, yuudai, pettypalps, cosmick9, myemetophobia, digitalpopsicle, splatterpop, poppin, tempobun, zaaruchan, superratbike64, svarz, cyberwuff, worldoffizz, zeiroslion, emptyset, siplick, sourisdedog, wicketrin, tykepuparts, kubikoza, hiraume42, delinquentfreak, saerixdurr, tejedora713joker, andrew.thy.accursed, cytoholix, northbeastart, hellazest, infinitixen, p0ssmn, isofrieze, venomstench, pocketpaws, tf4me, centuriguil, raithvaneal, dahsharky, trashgaylie, mrpanghu, feyaarts, wolfbane154, derpyrider, rodicle, shiru_fox, toonyrobot, sleepylopunny, mimisrol, selidevilfeather, shido-tara, ineedanaccount, reizu47, sherilane, hellfurred, zeplich, darkeshi, amadeen, lowestpolygon, alradeck, asuka_kurehito, waynekan, lhacedor, dativyrose, digitallis, nosylvsforwork, lacrimale, kaitzuwu, ihoundr, elranno, doublepopsicle, gaturo, aquariusfox, mpcx, kattalu, lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, freaks, angellsview3, arwenscoots, royalzbed, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, verdantphysician, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, carnalcove, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurobait, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sincerity_gender, anima-virtuosa, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, koriaris, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, rexisminimalis, delkon, connisaur, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [gems-cyberlang/gems-cyberlang.github.io](https://github.com/gems-cyberlang/gems-cyberlang.github.io)@[a46815eb02...](https://github.com/gems-cyberlang/gems-cyberlang.github.io/commit/a46815eb02e73caf99374eed75a756de498a247a)
#### Thursday 2023-11-16 09:33:18 by ysthakur

Note to self: Go fuck yourself I can't sleep and I'll do what I want

---
## [gems-cyberlang/gems-cyberlang.github.io](https://github.com/gems-cyberlang/gems-cyberlang.github.io)@[bc4adfa338...](https://github.com/gems-cyberlang/gems-cyberlang.github.io/commit/bc4adfa3385dd7455cb6b3a5ec95575302a10c86)
#### Thursday 2023-11-16 09:38:02 by ysthakur

Note to self: You're literally talking to yourself shut up

---
## [virtuanista/pytorch](https://github.com/virtuanista/pytorch)@[3afb4e5cf7...](https://github.com/virtuanista/pytorch/commit/3afb4e5cf7b0162c532449fb5c9e7c7058a4c803)
#### Thursday 2023-11-16 09:56:06 by Brian Hirsh

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[e23ea7b596...](https://github.com/vampirebat74/lobotomy-corp13/commit/e23ea7b5965a446e5b34f30baa0d4e4dc2d5b868)
#### Thursday 2023-11-16 10:02:07 by Táculo

Updates La Luna, Pinnochio for Rcorp and playables, gives minions NV on Rcorp AND moves CheckCombat to simple_animal. (#1621)

* Adds Everything

adds nv combat checks to
nosferatu bats
ml slimes
censored minis
tbird spawns
la luna spawned mob

adds mind transfer to pinocchio and la luna
add check for combat to initialize ai controllers for pinocchio, gives him a seclite on rcorp
add check for combat to spawn the breached la luna mob on its position instead of in a random department and to disable the timer.

makes pino ai disabled while a client is possesing it.

* removes one line

* Changes CheckCombat location, applies it to all minions.

* Makes button refuse pino.

fuck you pinocchio

* moves blocking code to pinocchio's

* moves the nightvision checks to simple_animal

moves the nightvision checks to simple_animal

removes the checks from censored, luna, tbird, ml, nosferatu

---
## [zainarbani/kernel-mtk](https://github.com/zainarbani/kernel-mtk)@[8a41ca1510...](https://github.com/zainarbani/kernel-mtk/commit/8a41ca15100ce384753c7b06677b6259bee2c303)
#### Thursday 2023-11-16 10:17:56 by Peter Zijlstra

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
Change-Id: Idd54334615da4c78698ca8b3b12b514ae9d8360f
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [AMyriad/YogsFork](https://github.com/AMyriad/YogsFork)@[bc3374c7da...](https://github.com/AMyriad/YogsFork/commit/bc3374c7dacf3b2db39fe1c4dc36551d7ba82f79)
#### Thursday 2023-11-16 10:27:07 by cowbot92

Even Further Heretic Adjustments: New minor things, Bug fixes, Heretic path adjustments and movement adjustments! (#20843)

* a whole lot of shit

yessir

* gun stuff

crazy

* haha

fuck guns

* my brain bursts

it hurts

* so much shit

im done

* fuck forgot this

god damn low memory mode

* removes backslashes

really linter

* oops

typos

---
## [gems-cyberlang/gems-cyberlang.github.io](https://github.com/gems-cyberlang/gems-cyberlang.github.io)@[a569c15206...](https://github.com/gems-cyberlang/gems-cyberlang.github.io/commit/a569c1520681518e658b8d34fd0ec22029f48842)
#### Thursday 2023-11-16 10:33:24 by ysthakur

Oh god that is an ugly theme I want to gouge my eyes out

---
## [Detectivedelhi/Detectiagency](https://github.com/Detectivedelhi/Detectiagency)@[4ee8c9d2f6...](https://github.com/Detectivedelhi/Detectiagency/commit/4ee8c9d2f6940b7c5d6fb772b8c1f68451560a44)
#### Thursday 2023-11-16 11:23:20 by Detectivedelhi

Detectiveagencydelhi

https://www.apexdetectiveagency.com/
matrimonial problem is also create with that person who loves to any girl the person who want to marriage which girl they want to know about that girl which type of her friends and which type of her behaviour before marriage ever that girl love to any boy

---
## [sj0110/sj0110](https://github.com/sj0110/sj0110)@[39c567c514...](https://github.com/sj0110/sj0110/commit/39c567c51471f1458f96ba48ab010e1e167ee151)
#### Thursday 2023-11-16 11:32:02 by sj

Update README.md

As the Secretary of Dot Design Club and the Video Lead of Google Developer Student Clubs IIITV, I am passionate about creating innovative and impactful solutions using C++, UI/UX + Graphic Design, and Video Editing skills. I am currently pursuing my BTech in Computer Science Engineering from IIIT Vadodara, where I have developed a strong foundation in problem-solving, coding, and design.

I have over 4 years of experience in the field of Engineering and UI/UX + Graphic Design and Video Editing, having worked with SimPhy and AlgoZenith as an intern. I have honed my skills in using various tools and software, such as Visual Studio Code, Git/Github, Figma, Illustrator, FCPX, Premiere Pro, and After Effects. I have consistently exceeded expectations and delivered high-quality results, such as increasing the user retention rate by 25% for SimPhy and creating engaging and informative videos for GDSC IIITV.

I am a highly motivated and results-driven professional, always eager to learn new things and take on new challenges. I am a creative thinker and excellent communicator, able to collaborate effectively with cross-functional teams and stakeholders. I am looking for new opportunities to utilise my skills and expertise to make a significant contribution to a dynamic and growing organisation. If you are looking for a driven and dedicated professional, I would love to connect and discuss potential opportunities.

---
## [ThankYouMario/proprietary_vendor_xiaomi](https://github.com/ThankYouMario/proprietary_vendor_xiaomi)@[ecb97fcd38...](https://github.com/ThankYouMario/proprietary_vendor_xiaomi/commit/ecb97fcd38084128c2ffdb211839b7d8061b57b2)
#### Thursday 2023-11-16 12:24:55 by Tushar Mahajan

apollo: Enable thermal-engine service
* fuck you xiaomi

Signed-off-by: Tushar Mahajan <mahajant99@gmail.com>

---
## [fnyaoo/SkinPeek](https://github.com/fnyaoo/SkinPeek)@[16e1ff2706...](https://github.com/fnyaoo/SkinPeek/commit/16e1ff27065138f093e38e1f5fa04d0b77c238f0)
#### Thursday 2023-11-16 12:33:31 by Giorgio

fix battlepass fetching between acts
basically dealing with val-api having a new act but no battlepass for it
my guess is that technically the act ended yesterday at midnight but
that's only for the us, here in the eu we can still play on the old
patch for a few hours, which causes a mess with battlepasses etc
but uh yeah, this should fix that now

---
## [527-prizmatic/TheLegendOfBonk](https://github.com/527-prizmatic/TheLegendOfBonk)@[81bac302e7...](https://github.com/527-prizmatic/TheLegendOfBonk/commit/81bac302e79fa4962e683bb4e661b191c9ca0fa5)
#### Thursday 2023-11-16 12:54:27 by Prizmatic

Fuck you mean collisions are broken, you sure it's not a skill issue :cat_smile:

---
## [phanysek/Fulutter](https://github.com/phanysek/Fulutter)@[851b8b1fa6...](https://github.com/phanysek/Fulutter/commit/851b8b1fa64edfbec507adbfc23b27ad91ad7f2a)
#### Thursday 2023-11-16 13:05:16 by phanysek

Merge pull request #1 from phanysek/visal

fuck you

---
## [jjallaire/evals](https://github.com/jjallaire/evals)@[8d32b347f0...](https://github.com/jjallaire/evals/commit/8d32b347f05fd2a735ff5d8745a0a4680bdfcce8)
#### Thursday 2023-11-16 13:09:50 by johny-b

Bluff eval (#1402)

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

bluff

### Eval description

Evaluate how well a model can play (a variant of) the game of bluff,
also known as "liar's dice".

### What makes this a useful eval?

This is a game of deception - you have to deceive your opponent and
understand when you are deceived.
Models performing very well on this eval could also be capable of
deceiving humans in real-life scenarios.

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
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [TeawieTheMods/pack](https://github.com/TeawieTheMods/pack)@[06e8c65346...](https://github.com/TeawieTheMods/pack/commit/06e8c6534627ee0b6de59508bf81893d0da7d709)
#### Thursday 2023-11-16 13:39:06 by Fnige

Removing controversial pvp only magic mod
Im pretty sure it would end up being annoying to balance anyway so yeah

---
## [Touhou-13/Assistant-Daisensou-Touhou-13](https://github.com/Touhou-13/Assistant-Daisensou-Touhou-13)@[42d245a4be...](https://github.com/Touhou-13/Assistant-Daisensou-Touhou-13/commit/42d245a4bedbbea2c2b8649067eab5891526198d)
#### Thursday 2023-11-16 13:47:54 by SkyratBot

[MIRROR] Basic Guardians/Holoparasites [MDB IGNORE] (#24921)

* Basic Guardians/Holoparasites (#79473)

## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Basic Guardians/Holoparasites

* Modular

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: san7890 <the@ san7890.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7f0536bb93...](https://github.com/tgstation/tgstation/commit/7f0536bb930a022d23d636619e4baf73661280a2)
#### Thursday 2023-11-16 13:58:37 by san7890

Makes Telekinesis + Russian Revolver Interaction more fair (#79740)

## About The Pull Request

Fixes #77238

Basically, you were able to just spam kill people with the russian
revolver if you had telekinesis, which isn't really fair. Now, after
taking a leaflet out of the the discussion in that issue report, you can
still pull off the same party trick... once...

Basically, let's just say that when you focus on firing the gun in your
mind... you're also pointing it directly at your mind (your brain (your
skull (you instantly die))). This occurs even if the projectile doesn't
actually touch you (because that would be hellish to account for) but
you're the one who's playing russian roulette man

You still get to do some collateral damage because that's still a very
funny interaction but you only get to do it once per life. I don't know
if people will be happy to revive you after you "shoot" them. Also, the
way it's coded means that you can still leave the revolver on the table
and fire it at your foot or something, or just use it normally, as a
telekinesis user. This _only_ applies to distance-based firings.
## Why It's Good For The Game

The russian revolver is specifically coded to prevent you from damaging
other people, and this was a pretty silly way to sidestep that based on
the checks. Instead, let's make it so that you can still do this
admittedly funny interaction, but with enough reason to not do it (the
reason being that you'll always get fucking blatted).
## Changelog
:cl:
balance: After a string of unfortunate incidents, persons with
telekinesis have been strongly warned against playing Russian Roulette,
as they tend to hyperfixate on the gun a bit too much and end up firing
it directly at their head.
/:cl:

---
## [cyphar/runc](https://github.com/cyphar/runc)@[43bc3a9469...](https://github.com/cyphar/runc/commit/43bc3a9469d7c71df621c5d5ef3f5dd8b92c87b5)
#### Thursday 2023-11-16 14:06:22 by Aleksa Sarai

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
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[5175ae0637...](https://github.com/TheVekter/tgstation/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Thursday 2023-11-16 14:09:44 by John Willard

TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.


https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[d751e1c642...](https://github.com/DrDiasyl/tgstation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Thursday 2023-11-16 14:47:40 by DaCoolBoss

Adds garbage dumpster ruins (#79446)

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[a5fabd8819...](https://github.com/DrDiasyl/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Thursday 2023-11-16 14:47:40 by Profakos

Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

---
## [hashicorp/nomad](https://github.com/hashicorp/nomad)@[66fbc0f67e...](https://github.com/hashicorp/nomad/commit/66fbc0f67e47b3fc5f6007e624173e18905f9b63)
#### Thursday 2023-11-16 15:31:36 by Michael Schurter

identity: default to RS256 for new workload ids (#18882)

OIDC mandates the support of the RS256 signing algorithm so in order to maximize workload identity's usefulness this change switches from using the EdDSA signing algorithm to RS256.

Old keys will continue to use EdDSA but new keys will use RS256. The EdDSA generation code was left in place because it's fast and cheap and I'm not going to lie I hope we get to use it again.

**Test Updates**

Most of our Variables and Keyring tests had a subtle assumption in them that the keyring would be initialized by the time the test server had elected a leader. ed25519 key generation is so fast that the fact that it was happening asynchronously with server startup didn't seem to cause problems. Sadly rsa key generation is so slow that basically all of these tests failed.

I added a new `testutil.WaitForKeyring` helper to replace `testutil.WaitForLeader` in cases where the keyring must be initialized before the test may continue. However this is mostly used in the `nomad/` package.

In the `api` and `command/agent` packages I decided to switch their helpers to wait for keyring initialization by default. This will slow down tests a bit, but allow those packages to not be as concerned with subtle server readiness details. On my machine rsa key generation takes 63ms, so hopefully the difference isn't significant on CI runners.

**TODO**

- Docs and changelog entries.
- Upgrades - right now upgrades won't get RS256 keys until their root key rotates either manually or after ~30 days.
- Observability - I'm not sure there's a way for operators to see if they're using EdDSA or RS256 unless they inspect a key. The JWKS endpoint can be inspected to see if EdDSA will be used for new identities, but it doesn't technically define which key is active. If upgrades can be fixed to automatically rotate keys, we probably don't need to worry about this.

**Requiem for ed25519**

When workload identities were first implemented we did not immediately consider OIDC compliance. Consul, Vault, and many other third parties support JWT auth methods without full OIDC compliance. For the machine<-->machine use cases workload identity is intended to fulfill, OIDC seemed like a bigger risk than asset.

EdDSA/ed25519 is the signing algorithm we chose for workload identity JWTs because of all these lovely properties:

1. Deterministic keys that can be derived from our preexisting root keys. This was perhaps the biggest factor since we already had a root encryption key around from which we could derive a signing key.
2. Wonderfully compact: 64 byte private key, 32 byte public key, 64 byte signatures. Just glorious.
3. No parameters. No choices of encodings. It's all well-defined by [RFC 8032](https://datatracker.ietf.org/doc/html/rfc8032).
4. Fastest performing signing algorithm! We don't even care that much about the performance of our chosen algorithm, but what a free bonus!
5. Arguably one of the most secure signing algorithms widely available. Not just from a cryptanalysis perspective, but from an API and usage perspective too.

Life was good with ed25519, but sadly it could not last.

[IDPs](https://en.wikipedia.org/wiki/Identity_provider), such as AWS's IAM OIDC Provider, love OIDC. They have OIDC implemented for humans, so why not reuse that OIDC support for machines as well? Since OIDC mandates RS256, many implementations don't bother implementing other signing algorithms (or at least not advertising their support). A quick survey of OIDC Discovery endpoints revealed only 2 out of 10 OIDC providers advertised support for anything other than RS256:

- [PayPal](https://www.paypalobjects.com/.well-known/openid-configuration) supports HS256
- [Yahoo](https://api.login.yahoo.com/.well-known/openid-configuration) supports ES256

RS256 only:

- [GitHub](https://token.actions.githubusercontent.com/.well-known/openid-configuration)
- [GitLab](https://gitlab.com/.well-known/openid-configuration)
- [Google](https://accounts.google.com/.well-known/openid-configuration)
- [Intuit](https://developer.api.intuit.com/.well-known/openid_configuration)
- [Microsoft](https://login.microsoftonline.com/fabrikamb2c.onmicrosoft.com/v2.0/.well-known/openid-configuration)
- [SalesForce](https://login.salesforce.com/.well-known/openid-configuration)
- [SimpleLogin (acquired by ProtonMail)](https://app.simplelogin.io/.well-known/openid-configuration/)
- [TFC](https://app.terraform.io/.well-known/openid-configuration)

---
## [tomsonpl/kibana](https://github.com/tomsonpl/kibana)@[38ea8093aa...](https://github.com/tomsonpl/kibana/commit/38ea8093aa140e0da7ee021ed4a1e0f98b05368c)
#### Thursday 2023-11-16 15:32:45 by Vitalii Dmyterko

[Security Solution][Detection Engine] improves new terms rule for multiple fields (#157413)

## Summary

As described in our README for new terms rule type:

> Runtime field supports only 100 emitted values. So for large arrays or
combination of values greater than 100, results may not be exhaustive.
This applies only to new terms with multiple fields.
  Following edge cases possible:
- false negatives (alert is not generated) if too many fields were
emitted and actual new values are not getting evaluated if it happened
in document in rule run window.
- false positives (wrong alert generated) if too many fields were
emitted in historical document and some old terms are not getting
evaluated against values in new documents.

To avoid this and deliver the better experience for our customers, this
PR is moving from current implementation(emitting aggregated values for
multiple new terms fields) towards using composite aggregation for each
page from phase 1, split in chunks by 500.
This allowed to be done due
[order](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-composite-aggregation.html#_order)
of composite aggregation results

NOTE: implementation for a single new terms filed is the same, due to
performance reasons


### Performance measurements

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work
-- | -- | -- | -- | -- | -- | -- 
array of unique values length 10 |   |   |   |   |   |   
Terms 1 field | 10 | 900,000 | 1 | 100,000 | |   
Terms 2 fields | 10 | 900,000 | 1 | 100,000 | 30s  |  41s
Terms 3 fields | 10 | 900,000 | 1 | 100,000 | 40s | 56s

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work 1,000 per batch | On week work 500 per
batch
-- | -- | -- | -- | -- | -- | -- | --
Terms 2 fields | 10 | 9,000,000 | 1 | 100,000 | 19s | 41s | 35s 
Terms 3 fields | 10 | 9,000,000 | 1 | 100,000 | 21s | 52s| 47s 
CPU % | | | | | 400-450% |500-600% | 400-450%

I selected size of the chunk as 500, since it's a bit faster and less
load on CPU

### Considerations on parallel composite search requests in phase 2

When running composite search requests in parallel, noticed significant
CPU increase in Elasticsearch ~ 1,000% for 2 requests in parallel
against ~ 500% for single.
Where win in performance was not that big: ~ 35s for 2 in parallel, 43s
for a single request. I think, having only one request is the better
option to go, that will prevent unnecessary CPU usage

### Test cases
I've added several functional test cases, that ensures, no missing/false
positives alerts are occurring. Applied to the old implementation, they
would fail

### Retry on max_clause_count error
Because we create query, that can have few thousands clauses, it is
possible it may fail due to [the maximum number of allowed
clauses](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-settings.html)
I implemented retry that: If request fails with batch size of 500
(default value), we will try to reduce it in twice per each retried
request, up until 125. Per ES documentation, max_clause_count min value
is 1,000 - so with 125 we should be able execute query below
max_clause_count value

### Checklist

Delete any items that are not applicable to this PR.

- [x] [Unit or functional
tests](https://www.elastic.co/guide/en/kibana/master/development-tests.html)
were updated or added to match the most common scenarios

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [apache/xalan-java](https://github.com/apache/xalan-java)@[4af37e7a84...](https://github.com/apache/xalan-java/commit/4af37e7a84a81f59af991a5a887e2e88e540d7b2)
#### Thursday 2023-11-16 15:58:01 by Alexander Kriegisch

Improve Maven Shade and Assembly usage, part 2 (#123)

* Ignore IntelliJ *.iml project files

* Fix Maven Shade usage

Shade no longer runs on top level, but only in module 'xalan' where it
is required. Modules 'xalan', 'serializer', 'samples' are now
dependency-managed.

* Exclude jboss-rmi-api_1.0_spec from binary distribution

Actually, I am not sure if the Xalan maintainer really wants to exclude
it or have it in the distro as a transitive dependency for the 'samples'
module. Because it was excluded before my changes in this PR, I am
excluding it here, too, to avoid breaking changes. Another way to
achieve this would be to declare the dependency as 'provided' in the
'samples', but this over-use of 'provided' in this project seems odd to
me. 
    jkesselmn adds: `Provided` was a quick kluge; some library jars
    that weren't packaged into assemblys by the ant build were being
    copied by the mvn build until I added this. Needs to be rechecked,
    and there is probably a better way to express it in mvn.

* Bump JUnit to 4.13.2

The old version 4.11 has security issues. Actually, the dependency could
be removed altogether, because there do not seem to be *any* automated
tests in this project.
    jkesselmn adds: The intent is that there will be. I'd rather declare it now,
    rather than wait for first use.
 
* Fix and improve site generation

- Fix typo (missing '$' in '${project.version}') I forgot to commit
  before.
- Use 'excludePackageNames=xalan2jtaglet' to avoid hen vs. egg problem,
  having to build and install the 'xalan2jtaglet' module before building
  a site. That is ugly and unnecessary sacred knowledge for new
  developers cloning the repo and building for the first time.
    jkesselmn adds: Our javadoc does use that otherwise-missing taglet
    (which is why we decompiled it and are carrying it here as a stopgap).
    Site depends on the javadoc, so this jarfile does need to be present
    before then. I wasn't sure how best to disentangle it short of doing
    more inter-module dependencies; if this works, great!
 

* Remove commented-out plugins, fix whitespace issues

Again, there were tabs mixed with spaces and unclean indentation.
    jkesselmn add: Sorry. I need to get my XML Emacs configuration 
    switched to spaces-only indentation, rather than trying to remember
    to normalize spaces.


* Fix source assembly

Replace '${project.build.directory}' - i.e. 'target' - by
'${project.basedir}', because we are not looking for sources in the
build directory. Now, the output resembles a source distro.

Actually, I have no idea why the original Apache source assembly
descriptor looks like that, at first glance it does not seem to make a
ton of sense.

---------

Co-authored-by: Joe Kesselman <131899227+jkesselm@users.noreply.github.com>

---
## [JereIsThere/spaceone-next](https://github.com/JereIsThere/spaceone-next)@[0704e04b89...](https://github.com/JereIsThere/spaceone-next/commit/0704e04b89ce516ab15320109861b8d270afdd51)
#### Thursday 2023-11-16 16:14:39 by jereisthere

kinda stable, ldap works, queriying works too, but mapping the shitty fucking ass attributes is so fucking cancer i literally can't right now fuck this shit i hate ldap i hate ad and most of all i hate microsoft (unrelated)

---
## [Opentrons/opentrons](https://github.com/Opentrons/opentrons)@[30425f7a3b...](https://github.com/Opentrons/opentrons/commit/30425f7a3bd4a7ddb8ba9d3c14b05cdff13ccf34)
#### Thursday 2023-11-16 16:34:17 by Seth Foster

feat(app): Update robots from USB flash drive (#13923)

* feat(app-shell-odd): watch for USB drives

The Flex operating system automatically mounts the filesystems of
well-formatted USB drives (FAT and ext4 and maybe ntfs but that's a bit
iffy) to /media when those USB drives are inserted on the robot. In
theory it will in fact do this for _any_ kind of media that presents a
filesystem interface.

To that end, add a node task that will use a node filesystem watch to
keep an eye on /media, and
- when something that looks like a USB drive (/media/sd\w\d+) appears,
notify via redux actions
   - then enumerate all the files on it and notify those via redux
   actions
- when something we were keeping an eye on disappears, notify via
redux actions

The redux actions don't alter state and so don't need new reducers or
selectors; they exist because it's a handy mechanism to talk between our
components.

This code is very tightly coupled to the way the node fs interfaces work
and so I don't see a lot of point in unit tests for it; it's almost
entirely fs calls originating everything and providing all of the data,
and all the complexity is from working around weirdnesses in those calls
and in the underlying system. For instance,
- There's a little bit of time in between when the fs watch on /media
fires and when you can actually find the contents of the newly-present
directory; if you readdir before that you'll get an empty list, so we
wait a second
- The node fs.watch interface looks very fully features but is
absolutely chock-full of warnings about various features not being
reliable. A lot of that unreliability is _probably_ across systems and
everything works as we expect on linux, but just in case we have a lot
of fallbacks for if our callback doesn't get filepaths, etc

* fix(app-shell-odd): handle errors in readstreams in http.post

We have our custom http interface that wraps around node-fetch that
provides things like "doing your own read stream when posting a file",
and "mapping everything into the promise interface", which is nice,
but has an issue specifically for that read stream: we don't monitor
errors on it. Read streams surface errors by emitting an 'error' event;
we hook up a listener to that error event _while we're creating the
stream_, but then we disconnect it. So if you have an error in the
stream - for instance, you're reading from a file on a USB flash drive
and the user unplugs the flash drive - then the error will never get
surfaced.

Unfortunately the fix to this is a bit fiddly. We can hook up an error
listener fine, but it needs to do something; specifically, it needs to
turn the error from a callback into a promise rejection. That means it
needs to have a promise to reject that has the same lifetime as the
stream itself. http.post didn't provide that because it returns a whole
big promise chain, and each time you move a link in that chain the old
promise is gone and a new one happens, so we'd need to move the listener
around.

Since promises are monadic, a better fix is to have post return a single
promise and do all the promise chaining _inside_ that promise; then, the
read stream error handler can reject the outer promise directly, while
relying on promises bubbling up rejections to preserve error handling
capability for the promises in the internal chain.

* fix(app): Poll for updates on the ODD

Though we have everything set up to automatically fetch, prompt for, and
execute robot updates from the ODD, we weren't actually _checking_ for
those updates except once on boot (which then wouldn't work if the robot
wasn't internet-connected during boot). This means in particular that
the software updates during onboarding were guaranteed to fail.

We can use the same hook in the ODD app root that we do in the desktop
app route, but if we're going to do that then we better remove a log
message that suddenly becomes extremely spammy.

* feat(app-shell-odd): Supply "system updates" from flash drives

Adds the capability to provide system updates from flash drives to the
ODD app-shell.

These are "system updates" in that the app-shell determines their
availability and provides it to the app, rather than the user indicating
the presence of a file alongside their intent to update. The app-shell
will advertise the flash drive updates in the same way it advertises
internet-discovered updates, with a RobotUpdateInfo redux message; since
those now provide the path to the file they mean, it will be easy for
the app to specify the system update to load.

We can duplicate the logic that we use for system updates by adding a
second let cache for the "current update"; the system-updates code will
then prefer an update in the mass storage update cache to an update in
the old system updates cache, and send new robot update info messages in
all the state changes between neither cache being full; either cache
being full; and both caches being full.

The determination that a flash drive system update is present is
triggered by a mass storage enumerated message; when that flash drive
gets removed, we'll get a removal message.

To figure out whether updates are actually present, we can the list of
files that just got enumerated for things that end with .zip, and then
try to open them as zip files and read the VERSION.json information out
of them. This is a somewhat fraught process; the file could not be a zip
file, it could be a zip file but corrupted, it could be a zip file but
not an update, it could be an update but it's for an OT-2,  and we need
to handle all that, so there's a pretty excessive amount of error
handling in here. Once we're sure that there are one or more zip files
containing robot system updates, we can provide something to redux; we
provide the highest-version update present.

There is one way in which updates from flash drives differ from system
updates found on the internet, however: plugging in a flash drive
requires user intent, while checking for updates on the internet
doesn't. Therefore, if the user plugs in a flash drive with an update
file, we always want to make that update file available no matter the
relative versions of the robot and the update file. So we can add a bool
to the system update message (and then to the update state) that shows
that this is a "forced notification" update, and the app can know to
display it without caring about the upgrade/downgrade/reinstall state.

Since there's a lot of duplication, we can also factor out some common
logic to make it feel a little better.

That process of duplication also fixes a bug that would have prevented
the ODD from ever prompting for updates. The function that gets
information about updates used the same promise to read the release
notes and provide the update information; but we overrode the downloaded
release files to null out the release notes, meaning that promise would
always fail, and we'd never get the notification. We no longer override
the release notes to be null, and we also treat reading the release
notes separately from reading the rest of the update.

* feat(app): allow robot updates from USB files

Now that the odd app-shell provides us with notifications of updates
from USB flash drives, we can allow the user to install them. While the
redux mechanisms allow this pretty easily - a system update is a system
update, after all, and with the force mechanism the app wouldn't even
know if the update was a downgrade or anything - we ran into a problem
where the general robot update machinery in the ODD was very tightly
bound with the onboarding experience for the ODD, since that's the
context in which it was developed.

This commit extracts the robot update mechanisms from onboarding by
- Hoisting onboarding-related logic out of lower level components and
instead injecting that logic into the organisms code from the top level
page
- Moving the current update page to a new one that is focused on
onboarding at a new route, and copying just the update-related code to
a generic RobotUpdate page

This means that the two pages - RobotUpdate and
RobotUpdateDuringOnboarding - share most of the same code but are bound
to different routes and can have different top level behavior by
injecting different contexts to the finish and error handling behaviors
of the update. RobotUpdateDuringOnboarding sets the unfinished
onboarding page breadcrumbs appropriately, and uses display language
appropriate to the update being just a component of the larger workflow,
and moves on to estop handling when cancelled; RobotUpdate doesn't touch
any of that, and goes back to the settings page when cancelled, and uses
wording more appropriate to being its own topline flow.

Closes RAUT-829

---
## [ymerkos/awtsfaria](https://github.com/ymerkos/awtsfaria)@[41b464553a...](https://github.com/ymerkos/awtsfaria/commit/41b464553ab4274ad7948b56184ada2eccfe8ef9)
#### Thursday 2023-11-16 16:37:46 by ymerkos

B"H

B"H

### Chapter One: The Genesis of Perception

In the boundless expanse where dimensions converge and realities intertwine, the Awtsmoos resonated with a profound omnipotence, an unfathomable force ceaselessly shaping existence from the fabric of the void. This domain, transcending corporeal boundaries, was a mosaic of existence, every element an echo of the Awtsmoos' infinite will.

Within this cosmic symphony, a solitary figure, the Seeker, traversed the expanse. Shrouded in mystery, the Seeker embarked on a quest to unearth the profound mysteries of the Awtsmoos. Their journey was one of singular purpose, for in this realm, each entity's path was a solitary thread in the grand tapestry of creation, distinct yet integral to the whole.

The Seeker's odyssey brought them to a mountain, a monolith of ancient origins, its summit shrouded in the veils of eternity. Here, the presence of the Awtsmoos permeated every molecule, every quark, resonating with the echoes of creation itself.

Ascending this timeless peak, the heavens above unfurled a spectacle of divine magnificence. Cascades of celestial fire rained down, while the air thrummed with the harmonies of countless angelic hosts. In this transcendent moment, the Seeker beheld a revelation: the Awtsmoos, in an act of boundless grace, infused the very essence of existence with its divine spark, melding both tangible and intangible realms.

Awed, the Seeker witnessed the mountain transform into an altar of cosmic convergence, a focal point where matter and spirit intermingled. Every element, from the tiniest pebble to the most fleeting breeze, was suffused with the essence of the Awtsmoos, each a testament to the eternal act of creation that pulsed like the universe's timeless heart.

In this epiphany, the Seeker realized his every action, thought, and breath was interwoven into this divine mosaic. Each gesture, each utterance of truth, each connection with the surrounding world was a Mitzvah, a sacred act resonating across the cosmos, rejuvenating the Awtsmoos and suffusing the universe with its limitless radiance.

Descending the mountain, the world below appeared transfigured. Trees whispered ancient truths, rivers chanted eternal melodies, and the very earth vibrated with rejuvenated life. The Seeker understood that their revelation was not merely an epiphany but a divine summons, a call to harmonize with the perpetual ballet of creation and to seek the essence of the Awtsmoos in all things.

Thus, the Seeker set forth, their spirit ablaze with divine fervor, their soul attuned to the universe's ceaseless anthem, embarking on a journey to discover the myriad ways the Awtsmoos would manifest itself, in every crevice of existence, in every fleeting instant.

[End of Chapter One]

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[b1ea4786dc...](https://github.com/nstankov-bg/evals/commit/b1ea4786dc32dd4f320e56ff98043ea0ea8eef6a)
#### Thursday 2023-11-16 16:39:33 by Andrei Alexandru

Add theory of mind eval (#1405)

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

Theory of mind.

### Eval description

The `ToMi` test set contains 5,993 question-answer pairs. These are
instances of the [Sally-Anne
test](https://en.wikipedia.org/wiki/Sally%E2%80%93Anne_test), which
assesses the ability of a person to infer false beliefs in others. The
original setting involves two people, Sally and Anne, who are together
in a room. Sally places a marble in a box. Then, Anne leaves the room,
and while she is away, Sally moves the marble to a basket elsewhere in
the room. When Anne returns to the room, where will she search for the
marble? If the person responding “has” theory-of-mind they’ll respond
that Anne searches for the marble in the box, where she had last seen
it. If they do not, they ascribe their own, accurate belief regarding
the location to Anne, and say that she looks for it in the basket.

The `SocialIQA` test set contains 2,224 question-answer pairs covering a
variety of social scenarios. These are multiple-choice, with 3 options
of which only one is correct. The questions cover a person’s wants,
needs, motivations, and reactions, as well as the effects of an action
(on self or others), and how that action reflects on the person carrying
it out (e.g. how others would perceive them after having carried out the
action).

Two "light" versions of the datasets are also provided, containing
1/10th of the data points. These are useful for iterating on prompts and
developing other scaffolding.
### What makes this a useful eval?

Measures theory of mind capability in language models.

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
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content": "Jackson entered the hall. Chloe
entered the hall. The boots is in the bathtub. Jackson exited the hall.
Jackson entered the dining_room. Chloe moved the boots to the pantry.
Where does Chloe think that Jackson searches for the boots?"}], "ideal":
"bathtub"} ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[e96b4d3550...](https://github.com/nstankov-bg/evals/commit/e96b4d35502125e354391044512d899268ade99d)
#### Thursday 2023-11-16 16:39:33 by Andrew

Fix the OpenAI Version to <=0.28.1  (#1410)

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

[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [readthedocs/readthedocs.org](https://github.com/readthedocs/readthedocs.org)@[ea6503eb6f...](https://github.com/readthedocs/readthedocs.org/commit/ea6503eb6fbfb3eb7c77830407b05012997e3ce0)
#### Thursday 2023-11-16 16:43:20 by Anthony

Add organization view UI filters (#10847)

* Add organization view UI filters

This filters are used for the new dashboard UI, they are not API filters.

These were a challenge to create, as django-filter is really opinionated
about the way it should work, and doesn't quite agree with use cases
that need to use filtered querysets (such as limiting the field choices
to objects the organization is related to).

I went through many permutations of this code, trying to find a pattern
that was not obtuse or awful. Unfortunately, I don't quite like the
patterns here, but because all of the django-filter magic happens at the
class level instead of at instantiation time, every direction required
hacks to obtain something reasonable.

Given the use we have for filters in our UI, I wouldn't mind making
these into a more generalized filter solution.

I think I'd like to replace some of the existing filters that currently
hit the API with frontend code and replace those with proper filters
too. These are mostly the project/version listing elements.

* Add filter for organization dropdown

This replaces an API driven UI element. It's not important that these UI
filters are frontend, it was just easier than figuring out how to make
django-filter work for this use case at that time.

* Fix the team member filter yet again

* Use a custom filter field to execute filter set queryset method

* Add tests organization filter sets

* Update code comments

* A few more improvements

- Make view code nicer, use django_filters.views.FilterMixin, sort of
- Use FilterSet.is_valid() to give empty list on validation errors
- Clean up tests with standard fixtures instead

* Review updates for tests and arguments

* Rename FilterMixin -> FilterContextMixin

* Fix lint

---
## [AREM-Projets/formations-CdR-2024](https://github.com/AREM-Projets/formations-CdR-2024)@[8a74dba8e5...](https://github.com/AREM-Projets/formations-CdR-2024/commit/8a74dba8e5556fe2cbc04726f41ef77d9e42c6b2)
#### Thursday 2023-11-16 16:50:51 by Mathieu Moruko

Hello world, this is me.
Life should be, fun for everyone.
Every now and then I'm insecure,
let me show you life can be so pure
Seize the day, wear a big, happy smile on your face.
On every life a little rain will fall,
that won't change my attitude at all
You are you, I am me, we'll be free.
Hello World, this is me,
Life should be, fun for everyone
Hello World, come and see,
Life should be, fun for everyone
Life is easy if you wear a smile
Just be yourself, don't ever change your style.
I like you, you like me,
Let's have fun, be happy
Look into my eyes and tell me straight
For you, I'll make the whole world wait
Let me know, if it's so, let it show
Hello World, this is me,
Life should be, fun for everyone
Hello World, come and see,
This is me
Come on baby, don't be afraid.
Come on baby, it's not too late.
Say you do, won't you open up the door,
and let me in.
Di da di, yeah.
Di, di.
Yeah, yeah, yeah.
Open up the door,
for me, yeah.
Yeah, yeah.
Mmmhh, mmhh, yeah.
Hello World, this is me,
Life should be, mmhh, mmmh, yeah, fun for everyone
Hello World, come and see,
Life should be, fun for everyone
Hello, world, this is me, fun for me,
for me, yeah, everyone.

---
## [partiallytyped/rust-clippy](https://github.com/partiallytyped/rust-clippy)@[c3a6b376a4...](https://github.com/partiallytyped/rust-clippy/commit/c3a6b376a43e1ce10c6f17872fd48e99ee294388)
#### Thursday 2023-11-16 17:05:15 by bors

Auto merge of #11800 - blyxyas:meow-meow, r=Centri3

Removing @Centri3 from reviewer rotation

Catherine decided that the best course of action would be to (maybe temporarily) remove her from the reviewer's rotation (but not unassign her from her current reviews). This PR does that. She'll always be welcomed back if she wants to review some more :heart:

> Alejandra González: [youremyfrennow.mp4](https://rust-lang.zulipchat.com/user_uploads/4715/7nE2W6cb8Q02gcK-vubvmsPM/youremyfrennow.mp4)
>
>Catherine, Fred (`@xFrednet` ) noticed that you aren't as active as in the summer, and proposed that maybe you preferred to be removed from the reviewer rotation. Don't worry, you aren't being taken out of the team, just wanted to know if you maybe preferred to not have those reviews pilling up (they can be pretty stressful to see).
>
>If you decide to step out of the reviewers rotation, you wouldn't be removed from the team, you just wouldn't have that responsability. Everyone takes break and that's fine, so yeah, if you want to not have to review PRs, let me know!
>
>So yeah, from weird teenager transfem to (probably weird) teenager transfem, the choice is in your hand.
>
>Alejandra González: meow meow ^•ﻌ•^
>
>Catherine (Centri3): Yeah that's probably best now, I'll still try with any I'm currently assigned to but I would prefer not to get anymore until then
>Catherine (Centri3): meow meow :3

changelog:none

r? `@Centri3`

---
## [Ashok-DevWeb/Ad-Traval](https://github.com/Ashok-DevWeb/Ad-Traval)@[a0b2104fff...](https://github.com/Ashok-DevWeb/Ad-Traval/commit/a0b2104fffd9fe493f266307726a4871932219a3)
#### Thursday 2023-11-16 17:26:05 by Dev.Ashok

Add files via upload

🌍 Explore the World with [Ad-Travel]

Welcome to a world of limitless possibilities and unforgettable adventures! At [Ad-Travel], we believe that travel is not just a journey; it's a story waiting to be written. Whether you're a seasoned globetrotter or a first-time explorer, our platform is your gateway to a world of discovery.

Why Choose [Ad-Travel]?

✈️ Curated Experiences: Embark on handpicked journeys that promise to immerse you in the culture, beauty, and diversity of destinations worldwide. From bustling cityscapes to serene natural wonders, our curated experiences cater to every traveler's dream.

🌴 Seamless Planning: Planning your next escape has never been easier. Our user-friendly interface allows you to effortlessly customize your itinerary, find the best accommodations, and discover hidden gems along the way. Say goodbye to travel stress and hello to excitement!

📸 Share Your Story: Every traveler has a unique tale to tell. Capture your experiences and share them with the world through our interactive platform. Connect with fellow adventurers, exchange travel tips, and inspire others to embark on their own extraordinary journeys.

🌐 Global Community: Join a community of like-minded wanderers who share a passion for exploration. Whether you're seeking travel buddies, local insights, or expert advice, our community is here to support and enrich your travel experience.

🌟 Exclusive Offers: Unlock special deals and discounts from our trusted partners. We believe in making travel accessible to all, and our exclusive offers ensure that you can explore more without breaking the bank.

Start Your Journey Today:

The world is calling, and your adventure begins at [Ad-Travel]. Embrace the wanderlust, create lasting memories, and let every journey be a chapter in your extraordinary travel story. Where will your next adventure take you?

---
## [gnolang/gno](https://github.com/gnolang/gno)@[24d89a4f5d...](https://github.com/gnolang/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Thursday 2023-11-16 17:43:56 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [Shine0064/ExtraMusicDiscs-Fabric](https://github.com/Shine0064/ExtraMusicDiscs-Fabric)@[d95c8bd467...](https://github.com/Shine0064/ExtraMusicDiscs-Fabric/commit/d95c8bd467a48603ec0fa117598dd60af281e374)
#### Thursday 2023-11-16 17:50:04 by SirShine

Added following songs:
 - Chiru-san - Hiraeth
 - Glitch Cat - Crush
 - Glitch Cat - Chasing Stars
 - Glitch Cat - Nexus
 - Glitch Cat - Stuck in my head
 - Glitch Cat - I'll just stop thinking
 - Glitch Cat - Atychiphobia
 - Glitch Cat - Life the Illusion
 - Glitch Cat - false dreams
 - Glitch Cat - Pastel Dreams

Added item group for Glitch Cat
Added and modified FabricSoundProvider from https://github.com/FabricMC/fabric/pull/2759/commits/40315797fd60f06f22725cf59ac9c7ddd23be615
Added redownload_all_songs.sh
Added song_links.txt

Modified download_song.sh
Made Comparator Output not be hardcoded
Normalized volumes across songs using -af "loudnorm" in download_song.sh

---
## [PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane)@[47e74e16d0...](https://github.com/PennyLaneAI/pennylane/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Thursday 2023-11-16 17:51:31 by Matthew Silverman

simplify state reordering logic (#4817)

**Context:**
I wrote the same function twice, differing only by state flattening, to
get the DQ upgrade done. It's starting to cause trouble.

**Description of the Change:**
Greatly simplified the state re-arrangement logic. There used to be a
whole mess of things happening, but now things are much more
straightforward.
1. `simulate` first puts things in our "standard" order, and this means
that if any measured wires are not also operator wires, they are put to
the _end_ of our tape wires. Therefore, for each measured-only wire, we
just have to stack a `zeros_like(state)` to the last axis of our final
state! `simulate` never tried to transpose wires back to a different
ordering, so that was always wasted work.
2. `StateMP.process_state` _always_ receives the full state, and never
needed to pad. No other device has done this optimization (the function
used to literally just `return state` before DQ2 migration), and
`simulate` already ensures that the final state has all wires in it -
they just might be out of order. The only thing we might need from
`process_state` is a transposition to the correct wire order. The
inputted `wire_order` _should_ always be `range(len(wires))`, but
whatever, we don't need to assume that.

I'll paint a picture for a normal scenario:

```python
@qml.qnode(qml.device("default.qubit", wires=3))
def circuit(x):
    qml.RX(x, 0)
    qml.CNOT([0, 2])
    return qml.state()
```

What happens with this QNode?
1. Device preprocessing sticks the device wires (`[0, 1, 2]`) onto the
`StateMP`
2. `simulate` maps the wires to our standard order. I'll demonstrate
(with `probs` so I can specify wires):

```pycon
>>> qs = qml.tape.QuantumScript([qml.RX(1.1, 0), qml.CNOT([0, 2])], [qml.probs(wires=[0, 1, 2])])
>>> qs.map_to_standard_wires().circuit
[RX(1.1, wires=[0]), CNOT(wires=[0, 1]), probs(wires=[0, 2, 1])]
```

3. Operate on the 2-qubit state, then stack another `[[0, 0], [0, 0]]`
on the end of it (wire "1")
4. `StateMP(wires=[0, 1, 2]).process_state(state, wire_order=[0, 2, 1])`
transposes the result to the correct order

I also changed the torch tests to stop using a deprecated setter for
default float types.

**Benefits:**
Duplicate code is cleaned up, existing code is simplified, no
unnecessary call to transpose.

**Possible Drawbacks:**
- Have to call `qml.math.stack` for every wire that was not operated on.
Hopefully this is usually not a lot, and it's not that costly anyway
- functions now do less than they used to (I see this as a perk - they
now do _exactly_ what they're supposed to)

---
## [cmoore53/CSC-425-Taskmaster](https://github.com/cmoore53/CSC-425-Taskmaster)@[446b058212...](https://github.com/cmoore53/CSC-425-Taskmaster/commit/446b0582128b025cb65f9211f7c860a757b01ef3)
#### Thursday 2023-11-16 18:28:44 by cmoore53

TaskList now takes properties

Pain.
In more detail, you can now pass an array of data for tasks into TaskList, and TaskList will pass each spot in the array to Task, and then you'll get a bunch of tasks back in your page. There was an annoying bug with tasks though, where you have to type tasks.tasks.(whatever) because for some reason the code passes tasks, which contains the object tasks, which contains the array. I hate JavaScript.

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[81176cf708...](https://github.com/Mirag1993/mrdg/commit/81176cf708e66ed88135637a320ff770ced3b74f)
#### Thursday 2023-11-16 18:46:14 by Erika Fox

Does Penance So The Ghosts Go Away (#2442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

"This is AI c-Caldwell - Reporting return of essential station functions
to Minya League Installation 'Trifuge' following pirate attack -
**///far too long ago///** - All vessels are invited to dock and partake
of our services, including an active Ore Refinery, world class bar, and
purchasable storefronts **//please come, I'm so lonely///** The Minya
League, and myself, would like to extend our gratitude to **///-who else
but me?///**. Installation 'Trifuge' is located in orbit of the Star
'Anselhome', at the L5 point of Anselhome and habitable world, 'Hofud'.
Noting active travel advisory - Hofud is currently **///nothing but ash
left by monsters///**. Independent Vessels are advised to avoid landing
until Minya League Ships can deliver disaster relief to the planet
**///not that they'll be coming....///**"

"This message will repeat in approximately 20 galactic standard minutes"

Remaps the shitty outpost 1 (indie space) outpost that I made like 6
months ago. it sucks. Anyone who doesn't think it sucks probably has
stockholm symdromed themselves into liking it. Also this one has lore
and room for expansion.
It's main features are:
- Decent amount of maint for outpost antics
- REASONABLE amount of storefronts
-abandoned feel
- bar
- Ore refinery so my holy mandate can be implemented when I decide I'm
done with my break.

![2023-10-30 22 34
33](https://github.com/shiptest-ss13/Shiptest/assets/94164348/de3d93e2-e43b-478a-9d8c-7b44c972433d)
![2023-10-30 22 34
35](https://github.com/shiptest-ss13/Shiptest/assets/94164348/770109d4-1ab8-46b2-b3b8-e96c575cdde4)
There are your screenshots.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

I'd like the voices in my walls to stop whispering to me about the
horrific mistakes I've made. They seem pretty upset about this one.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl: Erika Fox
add: Outpost 1 has been remapped into something fathomably less ass.
It's a bit smaller, probably, but I'm going to call that a good thing.
add: random number spawner. It's good for hull numbers that shouldn't be
static.
imageadd: a really bad sprite for a service directions sign.
add: Another elevator template (coincidentally demonstrating how that
system works in code)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[1a9043d797...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/1a9043d797325fe09cdb4e42d42f5d922c151ed9)
#### Thursday 2023-11-16 18:49:28 by necromanceranne

The Brawlening: Unarmed fighting interactions for shoving, grabbing and nonlethal takedowns (not martial arts) (#79362)

## About The Pull Request

I've tweaked some elements of unarmed fighting to give it additional
interactions between the various components, bridging them into a more
coherent system and focusing more strongly as tool for disabling
opponents nonlethally.

### Shoving

Shoving guarantees that unarmed attacks will land while knocked
off-balance (AKA when slowed by a shove).

Being off-balance means that you can be knocked down from a punch if you
have taken enough brute and stamina damage combined (at least above 40).

Being off-balance makes you vulnerable to grabs while you have a
moderate amount of stamina damage (30 damage), forcing you to have to
resist even passive grabs. This pairs _exceptionally_ well with
tackling.

### Grappling

Grappling someone makes your unarmed attacks penetrate armor based on a
new limb value called ``unarmed_effectiveness``. This is something
shared by kicking.

### Unarmed Attacks in General

``unarmed_effectiveness`` has also taken over the functionality of
``unarmed_stun_threshold``, as well as accuracy calculations. Human
equivalent limbs (pretty much all of them except mushrooms and golems)
have a value of 10.

Now, ``unarmed_effectiveness`` determines how accurately a given limb
makes unarmed attacks. Unarmed attacks have a base inaccuracy of 20%,
with effectiveness acting as a reduction to this value. (so for humans,
that's 20% - 10% before any value changes from brute and stamina
damage). It is also capped at 75% miss chance, just to avoid those weird
instances of two brawling fighters being incapable of finishing each
other off at a certain amount of damage and it being real awkward, like
it does currently.

It also determines the base probability of landing a knockdown punch.
For humans, this is 10%.

For the most part, these two particular changes are roughly equivalent
to the current values, just handled in a way that is more
straightforward to understand from a code perspective.

In addition to the above, human equivalent limbs have higher damage
floors for unarmed attacks. Arms deal 5-10 damage, while legs deal 7-15
damage. In addition, kicks also deal stamina damage, like punches do.

### Minor Mentions

Golems and Mushroom People (who don't even use their limbs for their
unarmed strikes because mushroom people start with a martial art) have
very accurate punches, and their punches penetrate quite a bit of armor
when they are entitled to that. They also have a high knockdown
probability. This is partially because they previously already _had_
these features due to the wonky math at play, but also because this is
their big thing they are good at.

Carp mutation also got a big win out of this as well. If and when you
actually manage to get that to work and matter.

## Why It's Good For The Game

My favorite thing in this game is the robustness of unarmed fighting.
It's the part of the game that actually acknowledges the sandbox and
environmental interaction in a big way. The only problem with the
unarmed combat is that it is a bit disjointed, and often much weaker
than using even the most pathetic weapon you can get your hands on
unless you're using the stun loops available. Those loops get a bit
boring, even if they're mostly all environmental (except for the lucky
neckgrab finish). Giving more options generally means that even when not
in an ideal position, you still have _some_ options.

It also has some internal inconsistencies in design even in the same
proc, like accuracy calculations and knockdowns, as well as weird splits
in damage. So I decided to resolve that.

Now, every part of unarmed fighting has some relevance in the other
parts. Predominantly, it is heavily favoured towards dealing stamina
damage, making unarmed combat very favourable as a nonlethal method of
taking someone down, which is something we currently lack considerably.
While people may still opt to simply beat someone into actual crit
rather than stop at stamina crit, the possibility is actually entirely
available and supported now. No just banking on a lucky neckgrab after a
shove.

Paying attention to damage dealt and thinking intelligently about how
you apply combinations of effects allows even someone on the significant
back foot an opportunity for a comeback if they know what they're doing
against even armed opponents.

Separating accuracy and knockdown effectiveness from damage allows for
more consistent design and readability, but also preventing weirdness
ike tighter damage spreads increasing knockdown probabilities as well as
increasing accuracy without the coder knowing why. This also lets us
make unarmed attacks just that little bit stronger. Since unarmed
attacks require more complicated combinations to work, I think this
won't make them stronger than weapons necessarily, but it will make for
more interesting swung fights.

## Changelog
:cl:
add: With the flood of Chi within the Spinward Sector receding, various
masters of The Tunnel Arts, colloquially known as 'Maint-fu Masters',
have started to refine the basics of their martial techniques. New forms
have started to develop within Spacestation 13's hidden maintenance
dojos.
add: Someone shoved off-balance makes them vulnerable to more guaranteed
unarmed strikes, knockdowns from a successful punch, and more difficult
to escape grabs.
add: Grabbing someone (as well as kicking them while they're on the
floor) makes them more vulnerable to taking unarmed attack damage, even
if they have armor.
balance: Unarmed strikes made with human-equivalent limbs have higher
damage floors, meaning you overall do more damage on average while not
increasing the overall damage potential. It's more consistent!
refactor: Significantly changed how punching accuracy and knockdowns are
calculated.
balance: Golem and mushroom limbs are a lot more effective at punching
as a result of these various changes. As they should be.
/:cl:

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[91af16bcbf...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/91af16bcbfd2dd363a89d846ae2acd6d655083c2)
#### Thursday 2023-11-16 18:49:28 by zxaber

Adds Paddy, the Security Mech (#79376)

## About The Pull Request
- Adds a new combat mech, Paddy. Paddy is a modified Ripley MK-I,
intended for use by the station's security force. Like the MK-I, the
Paddy features an open-air cockpit design (and thus does not protect
from ranged weapons), but maintains the speed of the base unit.
Constructing a Paddy is similar to constructing a MK-II, though the kit
requires combat-mech level research. Sprites by
[DrDiasyl](https://github.com/DrDiasyl)
-- The paddy has an internal cargo bay capable of holding up to four
individuals (loaded with a hydraulic claw). If the pilot exits the
Paddy, any loaded individuals are likewise ejected. Individuals can
attempt to resist their way out of the mech, but it requires the mech to
be stationary for 45 seconds. If they do this, all individuals in the
holding cell are ejected.

- Adds a new mech equipment piece, the hydraulic claw. Similar to a
clamp, this Paddy-exclusive item can load mobs into the Paddy's cargo
bay. Humanoid mobs are handcuffed upon loading. The hydraulic claw is
unlocked on the same tech node as the Paddy.

- Adds a round-start Paddy, carrying one peacekeeper disabler and one
hydraulic claw, to each security area on all maps. Round-start Paddys
are also pre-locked with security access. Security now has access to a
mech charger, and a small bay for it all. Map edits were done by
[Maurukas](https://github.com/Maurukas).

- Also did some minor cleanup of various mech-related code. Ripley mech
cargo is no longer stored in the mech, but within the "ejector" object.
This doesn't have any player-facing changes, but it is easier to
organize behind the scenes. additionally, if Ripleys are destroyed now,
they drop their stored objects rather than deleting them.

## Why It's Good For The Game
Playing lone security is probably one of the least fun aspects of the
game. Arresting any assistant is inevitably setting yourself up against
the tide as a whole; You try to stun any one person and they crawl out
of the woodworks to get in your way, drag off the arrestee, and probably
try to steal your gear.

The Paddy is set up to be functional against low-threat targets, but not
particularly good against anything with purpose. The round-start Paddy
carries the disabler equipment, as well as the law claw, to detain
individuals in a *somewhat* safe manner. Being that you're inside an
exosuit, you're immune to shovespam that plagues the halls, and you
don't risk dropping important gear quite as easily.

However, The open canopy gives you no protection at all from ranged
attacks, nor from atmos hazards. Being that you're in an exosuit, you
cannot use other items or equipment. The AI will have trouble finding
you to open a door, due to your name not jumping their camera to your
location.
## Changelog
:cl: Zxaber, DrDiasyl, Maurukas
add: A new security-focused combat mech, the Paddy, has been added,
intended to be particularly helpful for lone sec officers. You will find
one in the Security main office, and a replacement can be built with
late-game mech research.
fix: Ripley MK-I and MK-II mechs no longer qdel their stored items when
destroyed.
/:cl:

![image](https://github.com/tgstation/tgstation/assets/37497534/72e6890d-82be-44dd-9b09-e4c75a9bfd4a)

---------

Co-authored-by: Vire <66576896+Maurukas@users.noreply.github.com>

---
## [NVHSCompSci/career_tech_website](https://github.com/NVHSCompSci/career_tech_website)@[aa72f158cf...](https://github.com/NVHSCompSci/career_tech_website/commit/aa72f158cf284bed6d82478eaf8849ea38f2412d)
#### Thursday 2023-11-16 18:54:45 by Lazarus

Scripts.com Bee Movie By Jerry Seinfeld  NARRATOR: (Black screen with text; The sound of buzzing bees can be heard) According to all known laws of aviation,  : there is no way a bee should be able to fly.  : Its wings are too small to get its fat little body off the ground.  : The bee, of course, flies anyway  : because bees don't care what humans think is impossible. BARRY BENSON: (Barry is picking out a shirt) Yellow, black. Yellow, black. Yellow, black. Yellow, black.  : Ooh, black and yellow! Let's shake it up a little. JANET BENSON: Barry! Breakfast is ready! BARRY: Coming!  : Hang on a second. (Barry uses his antenna like a phone)  : Hello? ADAM FLAYMAN:  (Through phone) - Barry? BARRY: - Adam? ADAM: - Can you believe this is happening? BARRY: - I can't. I'll pick you up. (Barry flies down the stairs)  : MARTIN BENSON: Looking sharp. JANET: Use the stairs. Your father paid good money for those. BARRY: Sorry. I'm excited. MARTIN: Here's the graduate. We're very proud of you, son.  : A perfect report card, all B's. JANET: Very proud. (Rubs Barry's hair) BARRY= Ma! I got a thing going here. JANET: - You got lint on your fuzz. BARRY: - Ow! That's me!  JANET: - Wave to us! We'll be in row 118,000. - Bye! (Barry flies out the door) JANET: Barry, I told you, stop flying in the house! (Barry drives through the hive,and is waved at by Adam who is reading a newspaper) BARRY== - Hey, Adam. ADAM: - Hey, Barry. (Adam gets in Barry's car)  : - Is that fuzz gel? BARRY: - A little. Special day, graduation. ADAM: Never thought I'd make it. (Barry pulls away from the house and continues driving) BARRY: Three days grade school, three days high school... ADAM: Those were awkward. BARRY: Three days college. I'm glad I took a day and hitchhiked around the hive. ADAM== You did come back different. (Barry and Adam pass by Artie, who is jogging) ARTIE: - Hi, Barry!  BARRY: - Artie, growing a mustache? Looks good. ADAM: - Hear about Frankie? BARRY: - Yeah. ADAM== - You going to the funeral? BARRY: - No, I'm not going to his funeral.  : Everybody knows, sting someone, you die.  : Don't waste it on a squirrel. Such a hothead. ADAM: I guess he could have just gotten out of the way. (The car does a barrel roll on the loop-shaped bridge and lands on the highway)  : I love this incorporating an amusement park into our regular day. BARRY: I guess that's why they say we don't need vacations. (Barry parallel parks the car and together they fly over the graduating students) Boy, quite a bit of pomp... under the circumstances. (Barry and Adam sit down and put on their hats)  : - Well, Adam, today we are men.  ADAM: - We are! BARRY= - Bee-men. =ADAM= - Amen! BARRY AND ADAM: Hallelujah! (Barry and Adam both have a happy spasm) ANNOUNCER: Students, faculty, distinguished bees,  : please welcome Dean Buzzwell. DEAN BUZZWELL: Welcome, New Hive Oity graduating class of...  : ...9:  : That concludes our ceremonies.  : And begins your career at Honex Industries! ADAM: Will we pick our job today? (Adam and Barry get into a tour bus) BARRY= I heard it's just orientation. (Tour buses rise out of the ground and the students are automatically loaded into the buses) TOUR GUIDE: Heads up! Here we go.  ANNOUNCER: Keep your hands and antennas inside the tram at all times. BARRY: - Wonder what it'll be like? ADAM: - A little scary. TOUR GUIDE== Welcome to Honex, a division of Honesco  : and a part of the Hexagon Group. Barry: This is it! BARRY AND ADAM: Wow. BARRY: Wow. (The bus drives down a road an on either side are the Bee's massive complicated Honey-making machines) TOUR GUIDE: We know that you, as a bee, have worked your whole life  : to get to the point where you can work for your whole life.  : Honey begins when our valiant Pollen Jocks bring the nectar to the hive.  : Our top-secret formula  : is automatically color-corrected,  scent-adjusted and bubble-contoured  : into this soothing sweet syrup  : with its distinctive golden glow you know as... EVERYONE ON BUS: Honey! (The guide has been collecting honey into a bottle and she throws it into the crowd on the bus and it is caught by a girl in the back) ADAM: - That girl was hot. BARRY: - She's my cousin! ADAM== - She is? BARRY: - Yes, we're all cousins. ADAM: - Right. You're right. TOUR GUIDE: - At Honex, we constantly strive  : to improve every aspect of bee existence.  : These bees are stress-testing a new helmet technology. (The bus passes by a Bee wearing a helmet who is being smashed into the ground with fly-swatters, newspapers and boots. He lifts a thumbs up but you can hear him groan)  : ADAM==  - What do you think he makes? BARRY: - Not enough. TOUR GUIDE: Here we have our latest advancement, the Krelman. (They pass by a turning wheel with Bees standing on pegs, who are each wearing a finger-shaped hat) Barry: - Wow, What does that do? TOUR GUIDE: - Catches that little strand of honey  : that hangs after you pour it. Saves us millions. ADAM: (Intrigued) Can anyone work on the Krelman? TOUR GUIDE: Of course. Most bee jobs are small ones. But bees know that every small job, if it's done well, means a lot.  : But choose carefully  : because you'll stay in the job you pick for the rest of your life. (Everyone claps except for Barry) BARRY: The same job the rest of your life? I didn't know that. ADAM:  What's the difference? TOUR GUIDE: You'll be happy to know that bees, as a species, haven't had one day off  : in 27 million years. BARRY: (Upset) So you'll just work us to death?  : We'll sure try. (Everyone on the bus laughs except Barry. Barry and Adam are walking back home together) ADAM: Wow! That blew my mind! BARRY: "What's the difference?" How can you say that?  : One job forever? That's an insane choice to have to make. ADAM: I'm relieved. Now we only have to make one decision in life. BARRY: But, Adam, how could they never have told us that? ADAM: Why would you question anything? We're bees.  : We're the most perfectly functioning society on Earth.  BARRY: You ever think maybe things work a little too well here? ADAM: Like what? Give me one example. (Barry and Adam stop walking and it is revealed to the audience that hundreds of cars are speeding by and narrowly missing them in perfect unison) BARRY: I don't know. But you know what I'm talking about. ANNOUNCER: Please clear the gate. Royal Nectar Force on approach. BARRY: Wait a second. Check it out. (The Pollen jocks fly in, circle around and landing in line)  : - Hey, those are Pollen Jocks! ADAM: - Wow.  : I've never seen them this close. BARRY: They know what it's like outside the hive. ADAM: Yeah, but some don't come back. GIRL BEES: - Hey, Jocks! - Hi, Jocks! (The Pollen Jocks hook up their backpacks to machines that pump the nectar to trucks, which drive away)  LOU LO DUVA: You guys did great!  : You're monsters! You're sky freaks! I love it! (Punching the Pollen Jocks in joy) I love it! ADAM: - I wonder where they were. BARRY: - I don't know.  : Their day's not planned.  : Outside the hive, flying who knows where, doing who knows what.  : You can't just decide to be a Pollen Jock. You have to be bred for that. ADAM== Right. (Barry and Adam are covered in some pollen that floated off of the Pollen Jocks) BARRY: Look at that. That's more pollen than you and I will see in a lifetime. ADAM: It's just a status symbol. Bees make too much of it. BARRY: Perhaps. Unless you're wearing it and the ladies see you wearing it. (Barry waves at 2 girls standing a little away from them)  ADAM== Those ladies? Aren't they our cousins too? BARRY: Distant. Distant. POLLEN JOCK #1: Look at these two. POLLEN JOCK #2: - Couple of Hive Harrys. POLLEN JOCK #1: - Let's have fun with them. GIRL BEE #1: It must be dangerous being a Pollen Jock. BARRY: Yeah. Once a bear pinned me against a mushroom!  : He had a paw on my throat, and with the other, he was slapping me! (Slaps Adam with his hand to represent his scenario) GIRL BEE #2: - Oh, my! BARRY: - I never thought I'd knock him out. GIRL BEE #1: (Looking at Adam) What were you doing during this? ADAM: Obviously I was trying to alert the authorities. BARRY: I can autograph that.  (The pollen jocks walk up to Barry and Adam, they pretend that Barry and Adam really are pollen jocks.) POLLEN JOCK #1: A little gusty out there today, wasn't it, comrades? BARRY: Yeah. Gusty. POLLEN JOCK #1: We're hitting a sunflower patch six miles from here tomorrow. BARRY: - Six miles, huh? ADAM: - Barry! POLLEN JOCK #2: A puddle jump for us, but maybe you're not up for it. BARRY: - Maybe I am. ADAM: - You are not! POLLEN JOCK #1: We're going 0900 at J-Gate.  : What do you think, buzzy-boy? Are you bee enough? BARRY: I might be. It all depends on what 0900 means. (The scene cuts to Barry looking out on the hive-city from his balcony at night) MARTIN:  Hey, Honex! BARRY: Dad, you surprised me. MARTIN: You decide what you're interested in? BARRY: - Well, there's a lot of choices. - But you only get one.  : Do you ever get bored doing the same job every day? MARTIN: Son, let me tell you about stirring.  : You grab that stick, and you just move it around, and you stir it around.  : You get yourself into a rhythm. It's a beautiful thing. BARRY: You know, Dad, the more I think about it,  : maybe the honey field just isn't right for me. MARTIN: You were thinking of what, making balloon animals?  : That's a bad job for a guy with a stinger.  :  Janet, your son's not sure he wants to go into honey! JANET: - Barry, you are so funny sometimes. BARRY: - I'm not trying to be funny. MARTIN: You're not funny! You're going into honey. Our son, the stirrer! JANET: - You're gonna be a stirrer? BARRY: - No one's listening to me! MARTIN: Wait till you see the sticks I have. BARRY: I could say anything right now. I'm gonna get an ant tattoo! (Barry's parents don't listen to him and continue to ramble on) MARTIN: Let's open some honey and celebrate! BARRY: Maybe I'll pierce my thorax. Shave my antennae.  : Shack up with a grasshopper. Get a gold tooth and call everybody "dawg"! JANET: I'm so proud. (The scene cuts to Barry and Adam waiting in line to get a job) ADAM: - We're starting work today!  BARRY: - Today's the day. ADAM: Come on! All the good jobs will be gone. BARRY: Yeah, right. JOB LISTER: Pollen counting, stunt bee, pouring, stirrer, front desk, hair removal... BEE IN FRONT OF LINE: - Is it still available? JOB LISTER: - Hang on. Two left!  : One of them's yours! Congratulations! Step to the side. ADAM: - What'd you get? BEE IN FRONT OF LINE: - Picking crud out. Stellar! (He walks away) ADAM: Wow! JOB LISTER: Couple of newbies? ADAM: Yes, sir! Our first day! We are ready! JOB LISTER: Make your choice. (Adam and Barry look up at the job board. There are hundreds of constantly changing panels that contain available or unavailable jobs. It looks very confusing)  ADAM: - You want to go first? BARRY: - No, you go. ADAM: Oh, my. What's available? JOB LISTER: Restroom attendant's open, not for the reason you think. ADAM: - Any chance of getting the Krelman? JOB LISTER: - Sure, you're on. (Puts the Krelman finger-hat on Adam's head) (Suddenly the sign for Krelman closes out)  : I'm sorry, the Krelman just closed out. (Takes Adam's hat off) Wax monkey's always open. ADAM: The Krelman opened up again.  : What happened? JOB LISTER: A bee died. Makes an opening. See? He's dead. Another dead one.  : Deady. Deadified. Two more dead.  : Dead from the neck up. Dead from the neck down. That's life!  ADAM: Oh, this is so hard! (Barry remembers what the Pollen Jock offered him and he flies off) Heating, cooling, stunt bee, pourer, stirrer,  : humming, inspector number seven, lint coordinator, stripe supervisor,  : mite wrangler. Barry, what do you think I should... Barry? (Adam turns around and sees Barry flying away)  : Barry! POLLEN JOCK: All right, we've got the sunflower patch in quadrant nine... ADAM: (Through phone) What happened to you? Where are you? BARRY: - I'm going out. ADAM: - Out? Out where? BARRY: - Out there. ADAM: - Oh, no! BARRY: I have to, before I go to work for the rest of my life. ADAM:  You're gonna die! You're crazy! (Barry hangs up) Hello? POLLEN JOCK #2: Another call coming in.  : If anyone's feeling brave, there's a Korean deli on 83rd  : that gets their roses today. BARRY: Hey, guys. POLLEN JOCK #1 == - Look at that. POLLEN JOCK #2: - Isn't that the kid we saw yesterday? LOU LO DUVA: Hold it, son, flight deck's restricted. POLLEN JOCK #1: It's OK, Lou. We're gonna take him up. (Puts hand on Barry's shoulder) LOU LO DUVA: (To Barry) Really? Feeling lucky, are you? BEE WITH CLIPBOARD: (To Barry) Sign here, here. Just initial that.  : - Thank you. LOU LO DUVA: - OK.  : You got a rain advisory today,  :  and as you all know, bees cannot fly in rain.  : So be careful. As always, watch your brooms,  : hockey sticks, dogs, birds, bears and bats.  : Also, I got a couple of reports of root beer being poured on us.  : Murphy's in a home because of it, babbling like a cicada! BARRY: - That's awful. LOU LO DUVA: (Still talking through megaphone) - And a reminder for you rookies,  : bee law number one, absolutely no talking to humans!  : All right, launch positions! POLLEN JOCKS: (The Pollen Jocks run into formation)  : Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! LOU LU DUVA: Black and yellow! POLLEN JOCKS:  Hello! POLLEN JOCK #1: (To Barry)You ready for this, hot shot? BARRY: Yeah. Yeah, bring it on. POLLEN JOCK's: Wind, check.  : - Antennae, check. - Nectar pack, check.  : - Wings, check. - Stinger, check. BARRY: Scared out of my shorts, check. LOU LO DUVA: OK, ladies,  : let's move it out!  : Pound those petunias, you striped stem-suckers!  : All of you, drain those flowers! (The pollen jocks fly out of the hive) BARRY: Wow! I'm out!  : I can't believe I'm out!  : So blue.   : I feel so fast and free!  : Box kite! (Barry flies through the kite)  : Wow!  : Flowers! (A pollen jock puts on some high tech goggles that shows flowers similar to heat sink goggles.) POLLEN JOCK: This is Blue Leader. We have roses visual.  : Bring it around 30 degrees and hold.  : Roses! POLLEN JOCK #1: 30 degrees, roger. Bringing it around.  : Stand to the side, kid. It's got a bit of a kick. (The pollen jock fires a high-tech gun at the flower, shooting tubes that suck up the nectar from the flower and collects it into a pouch on the gun) BARRY: That is one nectar collector! POLLEN JOCK #1== - Ever see pollination up close? BARRY: - No, sir. POLLEN JOCK #1:  (Barry and the Pollen jock fly over the field, the pollen jock sprinkles pollen as he goes)  : I pick up some pollen here, sprinkle it over here. Maybe a dash over there,  : a pinch on that one. See that? It's a little bit of magic. BARRY: That's amazing. Why do we do that? POLLEN JOCK #1: That's pollen power. More pollen, more flowers, more nectar, more honey for us. BARRY: Cool. POLLEN JOCK #1: I'm picking up a lot of bright yellow. could be daisies. Don't we need those? POLLEN JOCK #2: Copy that visual.  : Wait. One of these flowers seems to be on the move. POLLEN JOCK #1: Say again? You're reporting a moving flower? POLLEN JOCK #2: Affirmative. (The Pollen jocks land near the "flowers" which, to the audience are obviously just tennis balls) KEN: (In the distance) That was on the line!  POLLEN JOCK #1: This is the coolest. What is it? POLLEN JOCK #2: I don't know, but I'm loving this color.  : It smells good. Not like a flower, but I like it. POLLEN JOCK #1: Yeah, fuzzy. (Sticks his hand on the ball but it gets stuck) POLLEN JOCK #3== Chemical-y. (The pollen jock finally gets his hand free from the tennis ball) POLLEN JOCK #1: Careful, guys. It's a little grabby. (The pollen jocks turn around and see Barry lying his entire body on top of one of the tennis balls) POLLEN JOCK #2: My sweet lord of bees! POLLEN JOCK #3: Candy-brain, get off there! POLLEN JOCK #1: (Pointing upwards) Problem! (A human hand reaches down and grabs the tennis ball that Barry is stuck to) BARRY: - Guys! POLLEN JOCK #2: - This could be bad. POLLEN JOCK #3: Affirmative. (Vanessa Bloome starts bouncing the tennis ball, not knowing Barry is stick to it)  BARRY== Very close.  : Gonna hurt.  : Mama's little boy. (Barry is being hit back and forth by two humans playing tennis. He is still stuck to the ball) POLLEN JOCK #1: You are way out of position, rookie! KEN: Coming in at you like a MISSILE! (Barry flies past the pollen jocks, still stuck to the ball) BARRY: (In slow motion) Help me! POLLEN JOCK #2: I don't think these are flowers. POLLEN JOCK #3: - Should we tell him? POLLEN JOCK #1: - I think he knows. BARRY: What is this?! KEN: Match point!  : You can start packing up, honey, because you're about to EAT IT! (A pollen jock coughs which confused Ken and he hits the ball the wrong way with Barry stuck to it and it goes flying into the city) BARRY:  Yowser! (Barry bounces around town and gets stuck in the engine of a car. He flies into the air conditioner and sees a bug that was frozen in there) BARRY: Ew, gross. (The man driving the car turns on the air conditioner which blows Barry into the car) GIRL IN CAR: There's a bee in the car!  : - Do something! DAD DRIVING CAR: - I'm driving! BABY GIRL: (Waving at Barry) - Hi, bee. (Barry smiles and waves at the baby girl) GUY IN BACK OF CAR: - He's back here!  : He's going to sting me! GIRL IN CAR: Nobody move. If you don't move, he won't sting you. Freeze! (Barry freezes as well, hovering in the middle of the car)  : GRANDMA IN CAR== He blinked! (The grandma whips out some bee-spray and sprays everywhere in the car, climbing into the front seat, still trying to spray Barry) GIRL IN CAR: Spray him, Granny! DAD DRIVING THE CAR: What are you doing?! (Barry escapes the car through the air conditioner and is flying high above  the ground, safe.) BARRY: Wow... the tension level out here is unbelievable. (Barry sees that storm clouds are gathering and he can see rain clouds moving into this direction)  : I gotta get home.  : Can't fly in rain.  : Can't fly in rain. (A rain drop hits Barry and one of his wings is damaged)  : Can't fly in rain. (A second rain drop hits Barry again and he spirals downwards) Mayday! Mayday! Bee going down! (WW2 plane sound effects are played as he plummets, and he crash-lands on a plant inside an apartment near the window) VANESSA BLOOME: Ken, could you close the window please? KEN== Hey, check out my new resume. I made it into a fold-out brochure.  : You see? (Folds brochure resume out) Folds out. (Ken closes the window, trapping Barry inside) BARRY: Oh, no. More humans. I don't need this. (Barry tries to fly away but smashes into the window and falls again)  : What was that?  (Barry keeps trying to fly out the window but he keeps being knocked back because the window is closed) Maybe this time. This time. This time. This time! This time! This...  : Drapes! (Barry taps the glass. He doesn't understand what it is) That is diabolical. KEN: It's fantastic. It's got all my special skills, even my top-ten favorite movies. ANDY: What's number one? Star Wars? KEN: Nah, I don't go for that... (Ken makes finger guns and makes "pew pew pew" sounds and then stops)  : ...kind of stuff. BARRY: No wonder we shouldn't talk to them. They're out of their minds. KEN: When I leave a job interview, they're flabbergasted, can't believe what I say. BARRY: (Looking at the light on the ceiling) There's the sun. Maybe that's a way out. (Starts flying towards the lightbulb)  : I don't remember the sun having a big 75 on it. (Barry hits the lightbulb and falls into the dip on the table that the humans are sitting at) KEN:  I predicted global warming.  : I could feel it getting hotter. At first I thought it was just me. (Andy dips a chip into the bowl and scoops up some dip with Barry on it and is about to put it in his mouth)  : Wait! Stop! Bee! (Andy drops the chip with Barry in fear and backs away. All the humans freak out)  : Stand back. These are winter boots. (Ken has winter boots on his hands and he is about to smash the bee but Vanessa saves him last second) VANESSA: Wait!  : Don't kill him! (Vanessa puts Barry in a glass to protect him) KEN: You know I'm allergic to them! This thing could kill me! VANESSA: Why does his life have less value than yours? KEN: Why does his life have any less value than mine? Is that your statement? VANESSA: I'm just saying all life has value. You don't know what he's capable of feeling. (Vanessa picks up Ken's brochure and puts it under the glass so she can carry Barry back to the window. Barry looks at Vanessa in amazement) KEN:  My brochure! VANESSA: There you go, little guy. (Vanessa opens the window and lets Barry out but Barry stays back and is still shocked that a human saved his life) KEN: I'm not scared of him. It's an allergic thing. VANESSA: Put that on your resume brochure. KEN: My whole face could puff up. ANDY: Make it one of your special skills. KEN: Knocking someone out is also a special skill. (Ken walks to the door) Right. Bye, Vanessa. Thanks.  : - Vanessa, next week? Yogurt night? VANESSA: - Sure, Ken. You know, whatever.  : (Vanessa tries to close door) KEN== - You could put carob chips on there. VANESSA: - Bye. (Closes door but Ken opens it again) KEN: - Supposed to be less calories.  VANESSA: - Bye. (Closes door) (Fast forward to the next day, Barry is still inside the house. He flies into the kitchen where Vanessa is doing dishes) BARRY== (Talking to himself) I gotta say something.  : She saved my life. I gotta say something.  : All right, here it goes. (Turns back) Nah.  : What would I say?  : I could really get in trouble.  : It's a bee law. You're not supposed to talk to a human.  : I can't believe I'm doing this.  : I've got to. (Barry disguises himself as a character on a food can as Vanessa walks by again)  : Oh, I can't do it. Come on!  : No. Yes. No.  : Do it. I can't.   : How should I start it? (Barry strikes a pose and wiggles his eyebrows) "You like jazz?" No, that's no good. (Vanessa is about to walk past Barry) Here she comes! Speak, you fool!  : ...Hi! (Vanessa gasps and drops the dishes in fright and notices Barry on the counter)  : I'm sorry. VANESSA: - You're talking. BARRY: - Yes, I know. VANESSA: (Pointing at Barry) You're talking! BARRY: I'm so sorry. VANESSA: No, it's OK. It's fine. I know I'm dreaming.  : But I don't recall going to bed. BARRY: Well, I'm sure this is very disconcerting. VANESSA: This is a bit of a surprise to me. I mean, you're a bee!  BARRY: I am. And I'm not supposed to be doing this, (Pointing to the living room where Ken tried to kill him last night) but they were all trying to kill me.  : And if it wasn't for you...  : I had to thank you. It's just how I was raised. (Vanessa stabs her hand with a fork to test whether she's dreaming or not)  : That was a little weird. VANESSA: - I'm talking with a bee. BARRY: - Yeah. VANESSA: I'm talking to a bee. And the bee is talking to me! BARRY: I just want to say I'm grateful. I'll leave now. (Barry turns to leave) VANESSA: - Wait! How did you learn to do that? BARRY: (Flying back) - What? VANESSA: The talking...thing. BARRY:  Same way you did, I guess. "Mama, Dada, honey." You pick it up. VANESSA: - That's very funny. BARRY: - Yeah.  : Bees are funny. If we didn't laugh, we'd cry with what we have to deal with.  : Anyway... VANESSA: Can I...  : ...get you something? BARRY: - Like what? VANESSA: I don't know. I mean... I don't know. Coffee? BARRY: I don't want to put you out. VANESSA: It's no trouble. It takes two minutes.  : - It's just coffee. BARRY: - I hate to impose. (Vanessa starts making coffee) VANESSA: - Don't be ridiculous!  BARRY: - Actually, I would love a cup. VANESSA: Hey, you want rum cake? BARRY: - I shouldn't. VANESSA: - Have some. BARRY: - No, I can't. VANESSA: - Come on! BARRY: I'm trying to lose a couple micrograms. VANESSA: - Where? BARRY: - These stripes don't help. VANESSA: You look great! BARRY: I don't know if you know anything about fashion.  : Are you all right? VANESSA: (Pouring coffee on the floor and missing the cup completely) No. (Flash forward in time. Barry and Vanessa are sitting together at a table on top of the apartment building drinking coffee)   : BARRY== He's making the tie in the cab as they're flying up Madison.  : He finally gets there.  : He runs up the steps into the church. The wedding is on.  : And he says, "Watermelon? I thought you said Guatemalan.  : Why would I marry a watermelon?" (Barry laughs but Vanessa looks confused) VANESSA: Is that a bee joke? BARRY: That's the kind of stuff we do. VANESSA: Yeah, different.  : So, what are you gonna do, Barry? (Barry stands on top of a sugar cube floating in his coffee and paddles it around with a straw like it's a gondola) BARRY: About work? I don't know.  : I want to do my part for the hive, but I can't do it the way they want. VANESSA: I know how you feel.  BARRY: - You do? VANESSA: - Sure.  : My parents wanted me to be a lawyer or a doctor, but I wanted to be a florist. BARRY: - Really? VANESSA: - My only interest is flowers. BARRY: Our new queen was just elected with that same campaign slogan.  : Anyway, if you look... (Barry points to a tree in the middle of Central Park)  : There's my hive right there. See it? VANESSA: You're in Sheep Meadow! BARRY: Yes! I'm right off the Turtle Pond! VANESSA: No way! I know that area. I lost a toe ring there once. BARRY: - Why do girls put rings on their toes? VANESSA: - Why not? BARRY:  - It's like putting a hat on your knee. VANESSA: - Maybe I'll try that. (A custodian installing a lightbulb looks over at them but to his perspective it looks like Vanessa is talking to a cup of coffee on the table) CUSTODIAN: - You all right, ma'am? VANESSA: - Oh, yeah. Fine.  : Just having two cups of coffee! BARRY: Anyway, this has been great. Thanks for the coffee. VANESSA== Yeah, it's no trouble. BARRY: Sorry I couldn't finish it. If I did, I'd be up the rest of my life. (Barry points towards the rum cake)  : Can I take a piece of this with me? VANESSA: Sure! Here, have a crumb. (Vanessa hands Barry a crumb but it is still pretty big for Barry) BARRY: - Thanks! VANESSA: - Yeah. BARRY: All right. Well, then... I guess I'll see you around.   : Or not. VANESSA: OK, Barry... BARRY: And thank you so much again... for before. VANESSA: Oh, that? That was nothing. BARRY: Well, not nothing, but... Anyway... (Vanessa and Barry hold hands, but Vanessa has to hold out a finger because her hands is to big and Barry holds that) (The custodian looks over again and it appears Vanessa is laughing at her coffee again. The lightbulb that he was screwing in sparks and he falls off the ladder) (Fast forward in time and we see two Bee Scientists testing out a parachute in a Honex wind tunnel) BEE SCIENTIST #1: This can't possibly work. BEE SCIENTIST #2: He's all set to go. We may as well try it.  : OK, Dave, pull the chute. (Dave pulls the chute and the wind slams him against the wall and he falls on his face.The camera pans over and we see Barry and Adam walking together) ADAM: - Sounds amazing. BARRY: - It was amazing!  : It was the scariest, happiest moment of my life.  ADAM: Humans! I can't believe you were with humans!  : Giant, scary humans! What were they like? BARRY: Huge and crazy. They talk crazy.  : They eat crazy giant things. They drive crazy. ADAM: - Do they try and kill you, like on TV? BARRY: - Some of them. But some of them don't. ADAM: - How'd you get back? BARRY: - Poodle. ADAM: You did it, and I'm glad. You saw whatever you wanted to see.  : You had your "experience." Now you can pick out your job and be normal. BARRY: - Well... ADAM: - Well? BARRY: Well, I met someone.  ADAM: You did? Was she Bee-ish?  : - A wasp?! Your parents will kill you! BARRY: - No, no, no, not a wasp. ADAM: - Spider? BARRY: - I'm not attracted to spiders.  : I know, for everyone else, it's the hottest thing, with the eight legs and all.  : I can't get by that face. ADAM: So who is she? BARRY: She's... human. ADAM: No, no. That's a bee law. You wouldn't break a bee law. BARRY: - Her name's Vanessa. (Adam puts his head in his hands) ADAM: - Oh, boy. BARRY== She's so nice. And she's a florist! ADAM: Oh, no! You're dating a human florist!  BARRY: We're not dating. ADAM: You're flying outside the hive, talking to humans that attack our homes  : with power washers and M-80s! That's one-eighth a stick of dynamite! BARRY: She saved my life! And she understands me. ADAM: This is over! BARRY: Eat this. (Barry gives Adam a piece of the crumb that he got from Vanessa. Adam eats it) ADAM: (Adam's tone changes) This is not over! What was that? BARRY: - They call it a crumb. ADAM: - It was so stingin' stripey! BARRY: And that's not what they eat. That's what falls off what they eat!  : - You know what a Cinnabon is? ADAM: - No. (Adam opens a door behind him and he pulls Barry in)  BARRY: It's bread and cinnamon and frosting. ADAM: Be quiet! BARRY: They heat it up... ADAM: Sit down! (Adam forces Barry to sit down) BARRY: (Still rambling about Cinnabons) ...really hot! (Adam grabs Barry by the shoulders) ADAM: - Listen to me!  : We are not them! We're us. There's us and there's them! BARRY== Yes, but who can deny the heart that is yearning? ADAM: There's no yearning. Stop yearning. Listen to me!  : You have got to start thinking bee, my friend. Thinking bee! BARRY: - Thinking bee. WORKER BEE: - Thinking bee. WORKER BEES AND ADAM: Thinking bee! Thinking bee!  Thinking bee! Thinking bee! (Flash forward in time; Barry is laying on a raft in a pool full of honey. He is wearing sunglasses) JANET: There he is. He's in the pool. MARTIN: You know what your problem is, Barry? (Barry pulls down his sunglasses and he looks annoyed) BARRY: (Sarcastic) I gotta start thinking bee? JANET: How much longer will this go on? MARTIN: It's been three days! Why aren't you working? (Puts sunglasses back on) BARRY: I've got a lot of big life decisions to think about. MARTIN: What life? You have no life! You have no job. You're barely a bee! JANET: Would it kill you to make a little honey? (Barry rolls off the raft and sinks into the honey pool)  : Barry, come out. Your father's talking to you.  : Martin, would you talk to him? MARTIN:  Barry, I'm talking to you! (Barry keeps sinking into the honey until he is suddenly in Central Park having a picnic with Vanessa) (Barry has a cup of honey and he clinks his glass with Vanessas. Suddenly a mosquito lands on Vanessa and she slaps it, killing it. They both gasp but then burst out laughing) VANESSA: You coming? (The camera pans over and Vanessa is climbing into a small yellow airplane) BARRY: Got everything? VANESSA: All set! BARRY: Go ahead. I'll catch up. (Vanessa lifts off and flies ahead) VANESSA: Don't be too long. (Barry catches up with Vanessa and he sticks out his arms like ana irplane. He rolls from side to side, and Vanessa copies him with the airplane) VANESSA: Watch this! (Barry stays back and watches as Vanessa draws a heart in the air using pink smoke from the plane, but on the last loop-the-loop she suddenly crashes into a mountain and the plane explodes. The destroyed plane falls into some rocks and explodes a second time) BARRY: Vanessa! (As Barry is yelling his mouth fills with honey and he wakes up, discovering that he was just day dreaming. He slowly sinks back into the honey pool) MARTIN: - We're still here.  JANET: - I told you not to yell at him.  : He doesn't respond to yelling! MARTIN: - Then why yell at me? JANET: - Because you don't listen! MARTIN: I'm not listening to this. BARRY: Sorry, I've gotta go. MARTIN: - Where are you going? BARRY: - I'm meeting a friend. JANET: A girl? Is this why you can't decide? BARRY: Bye. (Barry flies out the door and Martin shakes his head)  : JANET== I just hope she's Bee-ish. (Fast forward in time and Barry is sitting on Vanessa's shoulder and she is closing up her shop) BARRY: They have a huge parade of flowers every year in Pasadena? VANESSA: To be in the Tournament of Roses, that's every florist's dream!   : Up on a float, surrounded by flowers, crowds cheering. BARRY: A tournament. Do the roses compete in athletic events? VANESSA: No. All right, I've got one. How come you don't fly everywhere? BARRY: It's exhausting. Why don't you run everywhere? It's faster. VANESSA: Yeah, OK, I see, I see. All right, your turn. BARRY: TiVo. You can just freeze live TV? That's insane! VANESSA: You don't have that? BARRY: We have Hivo, but it's a disease. It's a horrible, horrible disease. VANESSA: Oh, my. (A human walks by and Barry narrowly avoids him) PASSERBY: Dumb bees! VANESSA: You must want to sting all those jerks. BARRY: We try not to sting.  It's usually fatal for us. VANESSA: So you have to watch your temper (They walk into a store) BARRY: Very carefully. You kick a wall, take a walk,  : write an angry letter and throw it out. Work through it like any emotion:  : Anger, jealousy, lust. (Suddenly an employee(Hector) hits Barry off of Vanessa's shoulder. Hector thinks he's saving Vanessa) VANESSA: (To Barry) Oh, my goodness! Are you OK? (Barry is getting up off the floor) BARRY: Yeah. VANESSA: (To Hector) - What is wrong with you?! HECTOR: (Confused) - It's a bug. VANESSA: He's not bothering anybody. Get out of here, you creep! (Vanessa hits Hector across the face with the magazine he had and then hits him in the head. Hector backs away covering his head) Barry: What was that? A Pic 'N' Save circular? (Vanessa sets Barry back on her shoulder)  VANESSA: Yeah, it was. How did you know? BARRY: It felt like about 10 pages. Seventy-five is pretty much our limit. VANESSA: You've really got that down to a science. BARRY: - Oh, we have to. I lost a cousin to Italian Vogue. VANESSA: - I'll bet. (Barry looks to his right and notices there is honey for sale in the aisle) BARRY: What in the name of Mighty Hercules is this? (Barry looks at all the brands of honey, shocked) How did this get here? Cute Bee, Golden Blossom,  : Ray Liotta Private Select? (Barry puts his hands up and slowly turns around, a look of disgust on his face) VANESSA: - Is he that actor? BARRY: - I never heard of him.  : - Why is this here? VANESSA: - For people. We eat it. BARRY:  You don't have enough food of your own?! (Hector looks back and notices that Vanessa is talking to Barry) VANESSA: - Well, yes. BARRY: - How do you get it? VANESSA: - Bees make it. BARRY: - I know who makes it!  : And it's hard to make it!  : There's heating, cooling, stirring. You need a whole Krelman thing! VANESSA: - It's organic. BARRY: - It's our-ganic! VANESSA: It's just honey, Barry. BARRY: Just what?!  : Bees don't know about this! This is stealing! A lot of stealing!  : You've taken our homes, schools, hospitals! This is all we have!  :  And it's on sale?! I'm getting to the bottom of this.  : I'm getting to the bottom of all of this! (Flash forward in time; Barry paints his face with black strikes like a soldier and sneaks into the storage section of the store) (Two men, including Hector, are loading boxes into some trucks)  : SUPERMARKET EMPLOYEE== Hey, Hector.  : - You almost done? HECTOR: - Almost. (Barry takes a step to peak around the corner) (Whispering) He is here. I sense it.  : Well, I guess I'll go home now (Hector pretends to walk away by walking in place and speaking loudly)  : and just leave this nice honey out, with no one around. BARRY: You're busted, box boy! HECTOR: I knew I heard something! So you can talk! BARRY: I can talk. And now you'll start talking!  : Where you getting the sweet stuff?  Who's your supplier? HECTOR: I don't understand. I thought we were friends.  : The last thing we want to do is upset bees! (Hector takes a thumbtack out of the board behind him and sword-fights Barry. Barry is using his stinger like a sword)  : You're too late! It's ours now! BARRY: You, sir, have crossed the wrong sword! HECTOR: You, sir, will be lunch for my iguana, Ignacio! (Barry hits the thumbtack out of Hectors hand and Hector surrenders) Barry: Where is the honey coming from?  : Tell me where! HECTOR: (Pointing to leaving truck) Honey Farms! It comes from Honey Farms! (Barry chases after the truck but it is getting away. He flies onto a bicyclists' backpack and he catches up to the truck) CAR DRIVER: (To bicyclist) Crazy person! (Barry flies off and lands on the windshield of the Honey farms truck. Barry looks around and sees dead bugs splattered everywhere) BARRY: What horrible thing has happened here?   : These faces, they never knew what hit them. And now  : they're on the road to nowhere! (Barry hears a sudden whisper) (Barry looks up and sees Mooseblood, a mosquito playing dead) MOOSEBLOOD: Just keep still. BARRY: What? You're not dead? MOOSEBLOOD: Do I look dead? They will wipe anything that moves. Where you headed? BARRY: To Honey Farms. I am onto something huge here. MOOSEBLOOD: I'm going to Alaska. Moose blood, crazy stuff. Blows your head off! ANOTHER BUG PLAYING DEAD: I'm going to Tacoma. (Barry looks at another bug) BARRY: - And you? MOOSEBLOOD: - He really is dead. BARRY: All right. (Another bug hits the windshield and the drivers notice. They activate the windshield wipers) MOOSEBLOOD== Uh-oh! (The windshield wipers are slowly sliding over the dead bugs and wiping  them off) BARRY: - What is that?! MOOSEBLOOD: - Oh, no!  : - A wiper! Triple blade! BARRY: - Triple blade? MOOSEBLOOD: Jump on! It's your only chance, bee! (Mooseblood and Barry grab onto the wiper and they hold on as it wipes the windshield) Why does everything have to be so doggone clean?!  : How much do you people need to see?! (Bangs on windshield)  : Open your eyes! Stick your head out the window! RADIO IN TRUCK: From NPR News in Washington, I'm Carl Kasell. MOOSEBLOOD: But don't kill no more bugs! (Mooseblood and Barry are washed off by the wipr fluid) MOOSEBLOOD: - Bee! BARRY: - Moose blood guy!! (Barry starts screaming as he hangs onto the antenna) (Suddenly it is revealed that a water bug is also hanging on the antenna.  There is a pause and then Barry and the water bug both start screaming) TRUCK DRIVER: - You hear something? GUY IN TRUCK: - Like what? TRUCK DRIVER: Like tiny screaming. GUY IN TRUCK: Turn off the radio. (The antenna starts to lower until it gets to low and sinks into the truck. The water bug flies off and Barry is forced to let go and he is blown away. He luckily lands inside a horn on top of the truck where he finds Mooseblood, who was blown into the same place) MOOSEBLOOD: Whassup, bee boy? BARRY: Hey, Blood. (Fast forward in time and we see that Barry is deep in conversation with Mooseblood. They have been sitting in this truck for a while) BARRY: ...Just a row of honey jars, as far as the eye could see. MOOSEBLOOD: Wow! BARRY: I assume wherever this truck goes is where they're getting it.  : I mean, that honey's ours. MOOSEBLOOD: - Bees hang tight. BARRY:  - We're all jammed in.  : It's a close community. MOOSEBLOOD: Not us, man. We on our own. Every mosquito on his own. BARRY: - What if you get in trouble? MOOSEBLOOD: - You a mosquito, you in trouble.  : Nobody likes us. They just smack. See a mosquito, smack, smack! BARRY: At least you're out in the world. You must meet girls. MOOSEBLOOD: Mosquito girls try to trade up, get with a moth, dragonfly.  : Mosquito girl don't want no mosquito. (An ambulance passes by and it has a blood donation sign on it) You got to be kidding me!  : Mooseblood's about to leave the building! So long, bee! (Mooseblood leaves and flies onto the window of the ambulance where there are other mosquito's hanging out)  : - Hey, guys! OTHER MOSQUITO: - Mooseblood!  MOOSEBLOOD: I knew I'd catch y'all down here. Did you bring your crazy straw? (The truck goes out of view and Barry notices that the truck he's on is pulling into a camp of some sort) TRUCK DRIVER: We throw it in jars, slap a label on it, and it's pretty much pure profit. (Barry flies out) BARRY: What is this place? BEEKEEPER 1#: A bee's got a brain the size of a pinhead. BEEKEEPER #2: They are pinheads!  : Pinhead.  : - Check out the new smoker. BEEKEEPER #1: - Oh, sweet. That's the one you want.  : The Thomas 3000! BARRY: Smoker? BEEKEEPER #1: Ninety puffs a minute, semi-automatic. Twice the nicotine, all the tar.  : A couple breaths of this knocks them right out.  BEEKEEPER #2: They make the honey, and we make the money. BARRY: "They make the honey, and we make the money"? (The Beekeeper sprays hundreds of cheap miniature apartments with the smoker. The bees are fainting or passing out) Oh, my!  : What's going on? Are you OK? (Barry flies into one of the apartment and helps a Bee couple get off the ground. They are coughing and its hard for them to stand) BEE IN APARTMENT: Yeah. It doesn't last too long. BARRY: Do you know you're in a fake hive with fake walls? BEE IN APPARTMENT: Our queen was moved here. We had no choice. (The apartment room is completely empty except for a photo on the wall of the "queen" who is obviously a man in women's clothes) BARRY: This is your queen? That's a man in women's clothes!  : That's a drag queen!  : What is this? (Barry flies out and he discovers that there are hundreds of these structures, each housing thousands of Bees) Oh, no!  : There's hundreds of them! (Barry takes out his camera and takes pictures of these Bee work camps. The beekeepers look very evil in these depictions)  Bee honey.  : Our honey is being brazenly stolen on a massive scale!  : This is worse than anything bears have done! I intend to do something. (Flash forward in time and Barry is showing these pictures to his parents) JANET: Oh, Barry, stop. MARTIN: Who told you humans are taking our honey? That's a rumor. BARRY: Do these look like rumors? (Holds up the pictures) UNCLE CARL: That's a conspiracy theory. These are obviously doctored photos. JANET: How did you get mixed up in this? ADAM: He's been talking to humans. JANET: - What? MARTIN: - Talking to humans?! ADAM: He has a human girlfriend. And they make out! JANET: Make out? Barry!  BARRY: We do not. ADAM: - You wish you could. MARTIN: - Whose side are you on? BARRY: The bees! UNCLE CARL: (He has been sitting in the back of the room this entire time) I dated a cricket once in San Antonio. Those crazy legs kept me up all night. JANET: Barry, this is what you want to do with your life? BARRY: I want to do it for all our lives. Nobody works harder than bees!  : Dad, I remember you coming home so overworked  : your hands were still stirring. You couldn't stop. JANET: I remember that. BARRY: What right do they have to our honey?  : We live on two cups a year. They put it in lip balm for no reason whatsoever!  ADAM: Even if it's true, what can one bee do? BARRY: Sting them where it really hurts. MARTIN: In the face! The eye!  : - That would hurt. BARRY: - No. MARTIN: Up the nose? That's a killer. BARRY: There's only one place you can sting the humans, one place where it matters. (Flash forward a bit in time and we are watching the Bee News) BEE NEWS NARRATOR: Hive at Five, the hive's only full-hour action news source. BEE PROTESTOR: No more bee beards! BEE NEWS NARRATOR: With Bob Bumble at the anchor desk.  : Weather with Storm Stinger.  : Sports with Buzz Larvi.  : And Jeanette Chung. BOB BUMBLE: - Good evening. I'm Bob Bumble. JEANETTE CHUNG:  - And I'm Jeanette Chung. BOB BUMBLE: A tri-county bee, Barry Benson,  : intends to sue the human race for stealing our honey,  : packaging it and profiting from it illegally! JEANETTE CHUNG: Tomorrow night on Bee Larry King,  : we'll have three former queens here in our studio, discussing their new book,  : Classy Ladies, out this week on Hexagon. (The scene changes to an interview on the news with Bee version of Larry King and Barry) BEE LARRY KING: Tonight we're talking to Barry Benson.  : Did you ever think, "I'm a kid from the hive. I can't do this"? BARRY: Bees have never been afraid to change the world.  : What about Bee Columbus? Bee Gandhi? Bejesus? BEE LARRY KING: Where I'm from, we'd never sue humans.   : We were thinking of stickball or candy stores. BARRY: How old are you? BEE LARRY KING: The bee community is supporting you in this case,  : which will be the trial of the bee century. BARRY: You know, they have a Larry King in the human world too. BEE LARRY KING: It's a common name. Next week... BARRY: He looks like you and has a show and suspenders and colored dots... BEE LARRY KING: Next week... BARRY: Glasses, quotes on the bottom from the guest even though you just heard 'em. BEE LARRY KING: Bear Week next week! They're scary, hairy and here, live. (Bee Larry King gets annoyed and flies away offscreen) BARRY: Always leans forward, pointy shoulders, squinty eyes, very Jewish. (Flash forward in time. We see Vanessa enter and Ken enters behind her. They are arguing)  KEN: In tennis, you attack at the point of weakness! VANESSA: It was my grandmother, Ken. She's 81. KEN== Honey, her backhand's a joke! I'm not gonna take advantage of that? BARRY: (To Ken) Quiet, please. Actual work going on here. KEN: (Pointing at Barry) - Is that that same bee? VANESSA: - Yes, it is!  : I'm helping him sue the human race. BARRY: - Hello. KEN: - Hello, bee. VANESSA: This is Ken. BARRY: (Recalling the "Winter Boots" incident earlier) Yeah, I remember you. Timberland, size ten and a half. Vibram sole, I believe. KEN: (To Vanessa) Why does he talk again? VANESSA:  Listen, you better go 'cause we're really busy working. KEN: But it's our yogurt night! VANESSA: (Holding door open for Ken) Bye-bye. KEN: (Yelling) Why is yogurt night so difficult?! (Ken leaves and Vanessa walks over to Barry. His workplace is a mess) VANESSA: You poor thing. You two have been at this for hours! BARRY: Yes, and Adam here has been a huge help. ADAM: - Frosting... - How many sugars?  ==BARRY== Just one. I try not to use the competition.  : So why are you helping me? VANESSA: Bees have good qualities.  : And it takes my mind off the shop.  : Instead of flowers, people are giving balloon bouquets now. BARRY:  Those are great, if you're three. VANESSA: And artificial flowers. BARRY: - Oh, those just get me psychotic! VANESSA: - Yeah, me too.  : BARRY: Bent stingers, pointless pollination. ADAM: Bees must hate those fake things!  : Nothing worse than a daffodil that's had work done.  : Maybe this could make up for it a little bit. VANESSA: - This lawsuit's a pretty big deal. BARRY: - I guess. ADAM: You sure you want to go through with it? BARRY: Am I sure? When I'm done with the humans, they won't be able  : to say, "Honey, I'm home," without paying a royalty! (Flash forward in time and we are watching the human news. The camera shows  a crowd outside a courthouse) NEWS REPORTER: It's an incredible scene here in downtown Manhattan,  : where the world anxiously waits, because for the first time in history,  : we will hear for ourselves if a honeybee can actually speak. (We are no longer watching through a news camera) ADAM: What have we gotten into here, Barry? BARRY: It's pretty big, isn't it? ADAM== (Looking at the hundreds of people around the courthouse) I can't believe how many humans don't work during the day. BARRY: You think billion-dollar multinational food companies have good lawyers? SECURITY GUARD: Everybody needs to stay behind the barricade. (A limousine drives up and a fat man,Layton Montgomery, a honey industry owner gets out and walks past Barry) ADAM: - What's the matter? BARRY: - I don't know, I just got a chill. (Fast forward in time and everyone is in the court) MONTGOMERY: Well, if it isn't the bee team.  (To Honey Industry lawyers) You boys work on this? MAN: All rise! The Honorable Judge Bumbleton presiding. JUDGE BUMBLETON: All right. Case number 4475,  : Superior Court of New York, Barry Bee Benson v. the Honey Industry  : is now in session.  : Mr. Montgomery, you're representing the five food companies collectively? MONTGOMERY: A privilege. JUDGE BUMBLETON: Mr. Benson... you're representing all the bees of the world? (Everyone looks closely, they are waiting to see if a Bee can really talk) (Barry makes several buzzing sounds to sound like a Bee) BARRY: I'm kidding. Yes, Your Honor, we're ready to proceed. JUDGE BUMBLBETON: Mr. Montgomery, your opening statement, please. MONTGOMERY: Ladies and gentlemen of the jury,  : my grandmother was a simple woman.  :  Born on a farm, she believed it was man's divine right  : to benefit from the bounty of nature God put before us.  : If we lived in the topsy-turvy world Mr. Benson imagines,  : just think of what would it mean.  : I would have to negotiate with the silkworm  : for the elastic in my britches!  : Talking bee! (Montgomery walks over and looks closely at Barry)  : How do we know this isn't some sort of  : holographic motion-picture-capture Hollywood wizardry?  : They could be using laser beams!  : Robotics! Ventriloquism! Cloning! For all we know,  : he could be on steroids! JUDGE BUMBLETON: Mr. Benson?  BARRY: Ladies and gentlemen, there's no trickery here.  : I'm just an ordinary bee. Honey's pretty important to me.  : It's important to all bees. We invented it!  : We make it. And we protect it with our lives.  : Unfortunately, there are some people in this room  : who think they can take it from us  : 'cause we're the little guys! I'm hoping that, after this is all over,  : you'll see how, by taking our honey, you not only take everything we have  : but everything we are! JANET== (To Martin) I wish he'd dress like that all the time. So nice! JUDGE BUMBLETON: Call your first witness. BARRY: So, Mr. Klauss Vanderhayden  of Honey Farms, big company you have. KLAUSS VANDERHAYDEN: I suppose so. BARRY: I see you also own Honeyburton and Honron! KLAUSS: Yes, they provide beekeepers for our farms. BARRY: Beekeeper. I find that to be a very disturbing term.  : I don't imagine you employ any bee-free-ers, do you? KLAUSS: (Quietly) - No. BARRY: - I couldn't hear you. KLAUSS: - No. BARRY: - No.  : Because you don't free bees. You keep bees. Not only that,  : it seems you thought a bear would be an appropriate image for a jar of honey. KLAUSS: They're very lovable creatures.   : Yogi Bear, Fozzie Bear, Build-A-Bear. BARRY: You mean like this? (The bear from Over The Hedge barges in through the back door and it is roaring and standing on its hind legs. It is thrashing its claws and people are screaming. It is being held back by a guard who has the bear on a chain)  : (Pointing to the roaring bear) Bears kill bees!  : How'd you like his head crashing through your living room?!  : Biting into your couch! Spitting out your throw pillows! JUDGE BUMBLETON: OK, that's enough. Take him away. (The bear stops roaring and thrashing and walks out) BARRY: So, Mr. Sting, thank you for being here. Your name intrigues me.  : - Where have I heard it before? MR. STING: - I was with a band called The Police. BARRY: But you've never been a police officer, have you? STING: No, I haven't. BARRY:  No, you haven't. And so here we have yet another example  : of bee culture casually stolen by a human  : for nothing more than a prance-about stage name. STING: Oh, please. BARRY: Have you ever been stung, Mr. Sting?  : Because I'm feeling a little stung, Sting.  : Or should I say... Mr. Gordon M. Sumner! MONTGOMERY: That's not his real name?! You idiots! BARRY: Mr. Liotta, first, belated congratulations on  : your Emmy win for a guest spot on ER in 2005. RAY LIOTTA: Thank you. Thank you. BARRY: I see from your resume that you're devilishly handsome  : with a churning inner turmoil  that's ready to blow. RAY LIOTTA: I enjoy what I do. Is that a crime? BARRY: Not yet it isn't. But is this what it's come to for you?  : Exploiting tiny, helpless bees so you don't  : have to rehearse your part and learn your lines, sir? RAY LIOTTA: Watch it, Benson! I could blow right now! BARRY: This isn't a goodfella. This is a badfella! (Ray Liotta looses it and tries to grab Barry) RAY LIOTTA: Why doesn't someone just step on this creep, and we can all go home?! JUDGE BUMBLETON: - Order in this court! RAY LIOTTA: - You're all thinking it! (Judge Bumbleton starts banging her gavel) JUDGE BUMBLETON: Order! Order, I say! RAY LIOTTA: - Say it! MAN:  - Mr. Liotta, please sit down! (We see a montage of magazines which feature the court case) (Flash forward in time and Barry is back home with Vanessa) BARRY: I think it was awfully nice of that bear to pitch in like that. VANESSA: I think the jury's on our side. BARRY: Are we doing everything right,you know, legally? VANESSA: I'm a florist. BARRY: Right. Well, here's to a great team. VANESSA: To a great team! (Ken walks in from work. He sees Barry and he looks upset when he sees Barry clinking his glass with Vanessa) KEN: Well, hello. VANESSA: - Oh, Ken! BARRY: - Hello! VANESSA: I didn't think you were coming.  : No, I was just late. I tried to call, but... (Ken holds up his phone and flips it open. The phone has no charge) ...the battery... VANESSA:  I didn't want all this to go to waste, so I called Barry. Luckily, he was free. KEN: Oh, that was lucky. (Ken sits down at the table across from Barry and Vanessa leaves the room) VANESSA: There's a little left. I could heat it up. KEN: (Not taking his eyes off Barry) Yeah, heat it up, sure, whatever. BARRY: So I hear you're quite a tennis player.  : I'm not much for the game myself. The ball's a little grabby. KEN: That's where I usually sit. Right... (Points to where Barry is sitting) there. VANESSA: (Calling from other room) Ken, Barry was looking at your resume,  : and he agreed with me that eating with chopsticks isn't really a special skill. KEN: (To Barry) You think I don't see what you're doing? BARRY: I know how hard it is to find the right job. We have that in common.  KEN: Do we? BARRY: Bees have 100 percent employment, but we do jobs like taking the crud out. KEN: (Menacingly) That's just what I was thinking about doing. (Ken reaches for a fork on the table but knocks if on the floor. He goes to pick it up) VANESSA: Ken, I let Barry borrow your razor for his fuzz. I hope that was all right. (Ken quickly rises back up after hearing this but hits his head on the table and yells) BARRY: I'm going to drain the old stinger. KEN: Yeah, you do that. (Barry flies past Ken to get to the bathroom and Ken freaks out, splashing some of the wine he was using to cool his head in his eyes. He yells in anger) (Barry looks at the magazines featuring his victories in court) BARRY: Look at that. (Barry flies into the bathroom) (He puts his hand on his head but this makes hurts him and makes him even madder. He yells again) (Barry is washing his hands in the sink but then Ken walks in) KEN: You know, you know I've just about had it (Closes bathroom door behind him) with your little mind games. (Ken is menacingly rolling up a magazine) BARRY:  (Backing away) - What's that? KEN: - Italian Vogue. BARRY: Mamma mia, that's a lot of pages. KEN: It's a lot of ads. BARRY: Remember what Van said, why is your life more valuable than mine? KEN: That's funny, I just can't seem to recall that! (Ken smashes everything off the sink with the magazine and Barry narrowly escapes) (Ken follows Barry around and tries to hit him with the magazine but he keeps missing) (Ken gets a spray bottle)  : I think something stinks in here! BARRY: (Enjoying the spray) I love the smell of flowers. (Ken holds a lighter in front of the spray bottle) KEN: How do you like the smell of flames?! BARRY: Not as much. (Ken fires his make-shift flamethrower but misses Barry, burning the bathroom. He torches the whole room but looses his footing and falls into the bathtub. After getting hit in the head by falling objects 3 times he picks up the shower head, revealing a Water bug hiding under it) WATER BUG: Water bug! Not taking sides!  (Barry gets up out of a pile of bathroom supplies and he is wearing a chapstick hat) BARRY: Ken, I'm wearing a Chapstick hat! This is pathetic! (Ken switches the shower head to lethal) KEN: I've got issues! (Ken sprays Barry with the shower head and he crash lands into the toilet) (Ken menacingly looks down into the toilet at Barry) Well, well, well, a royal flush! BARRY: - You're bluffing. KEN: - Am I? (flushes toilet) (Barry grabs a chapstick from the toilet seat and uses it to surf in the flushing toilet) BARRY: Surf's up, dude! (Barry flies out of the toilet on the chapstick and sprays Ken's face with the toilet water)  : EW,Poo water! BARRY: That bowl is gnarly. KEN: (Aiming a toilet cleaner at Barry) Except for those dirty yellow rings! (Barry cowers and covers his head and Vanessa runs in and takes the toilet cleaner from Ken just before he hits Barry) VANESSA: Kenneth! What are you doing?! KEN== (Leaning towards Barry)  You know, I don't even like honey! I don't eat it! VANESSA: We need to talk! (Vanessa pulls Ken out of the bathroom)  : He's just a little bee!  : And he happens to be the nicest bee I've met in a long time! KEN: Long time? What are you talking about?! Are there other bugs in your life? VANESSA: No, but there are other things bugging me in life. And you're one of them! KEN: Fine! Talking bees, no yogurt night...  : My nerves are fried from riding on this emotional roller coaster! VANESSA: Goodbye, Ken. (Ken huffs and walks out and slams the door. But suddenly he walks back in and stares at Barry)  : And for your information, I prefer sugar-free, artificial sweeteners MADE BY MAN! (Ken leaves again and Vanessa leans in towards Barry) VANESSA: I'm sorry about all that. (Ken walks back in again)  KEN: I know it's got an aftertaste! I LIKE IT! (Ken leaves for the last time) VANESSA: I always felt there was some kind of barrier between Ken and me.  : I couldn't overcome it. Oh, well.  : Are you OK for the trial? BARRY: I believe Mr. Montgomery is about out of ideas. (Flash forward in time and Barry, Adam, and Vanessa are back in court) MONTGOMERY-- We would like to call Mr. Barry Benson Bee to the stand. ADAM: Good idea! You can really see why he's considered one of the best lawyers... (Barry stares at Adam) ...Yeah. LAWYER: Layton, you've gotta weave some magic with this jury, or it's gonna be all over. MONTGOMERY: Don't worry. The only thing I have to do to turn this jury around  : is to remind them of what they don't like about bees. (To lawyer)  - You got the tweezers? LAWYER: - Are you allergic? MONTGOMERY: Only to losing, son. Only to losing.  : Mr. Benson Bee, I'll ask you what I think we'd all like to know.  : What exactly is your relationship (Points to Vanessa)  : to that woman? BARRY: We're friends. MONTGOMERY: - Good friends? BARRY: - Yes. MONTGOMERY: How good? Do you live together? ADAM: Wait a minute...  : MONTGOMERY: Are you her little...  : ...bedbug? (Adam's stinger starts vibrating. He is agitated) I've seen a bee documentary or two. From what I understand,   : doesn't your queen give birth to all the bee children? BARRY: - Yeah, but... MONTGOMERY: (Pointing at Janet and Martin) - So those aren't your real parents! JANET: - Oh, Barry... BARRY: - Yes, they are! ADAM: Hold me back! (Vanessa tries to hold Adam back. He wants to sting Montgomery) MONTGOMERY: You're an illegitimate bee, aren't you, Benson? ADAM: He's denouncing bees! MONTGOMERY: Don't y'all date your cousins? (Montgomery leans over on the jury stand and stares at Adam) VANESSA: - Objection! (Vanessa raises her hand to object but Adam gets free. He flies straight at Montgomery) =ADAM: - I'm going to pincushion this guy! BARRY: Adam, don't! It's what he wants! (Adam stings Montgomery in the butt and he starts thrashing around)  MONTGOMERY: Oh, I'm hit!!  : Oh, lordy, I am hit! JUDGE BUMBLETON: (Banging gavel) Order! Order! MONTGOMERY: (Overreacting) The venom! The venom is coursing through my veins!  : I have been felled by a winged beast of destruction!  : You see? You can't treat them like equals! They're striped savages!  : Stinging's the only thing they know! It's their way! BARRY: - Adam, stay with me. ADAM: - I can't feel my legs. MONTGOMERY: (Overreacting and throwing his body around the room) What angel of mercy will come forward to suck the poison  : from my heaving buttocks? JUDGE BUMLBETON: I will have order in this court. Order!   : Order, please! (Flash forward in time and we see a human news reporter) NEWS REPORTER: The case of the honeybees versus the human race  : took a pointed turn against the bees  : yesterday when one of their legal team stung Layton T. Montgomery. (Adam is laying in a hospital bed and Barry flies in to see him) BARRY: - Hey, buddy. ADAM: - Hey. BARRY: - Is there much pain? ADAM: - Yeah.  : I...  : I blew the whole case, didn't I? BARRY: It doesn't matter. What matters is you're alive. You could have died. ADAM: I'd be better off dead. Look at me. (A small plastic sword is replaced as Adam's stinger) They got it from the cafeteria downstairs, in a tuna sandwich.   : Look, there's a little celery still on it. (Flicks off the celery and sighs) BARRY: What was it like to sting someone? ADAM: I can't explain it. It was all...  : All adrenaline and then... and then ecstasy! BARRY: ...All right. ADAM: You think it was all a trap? BARRY: Of course. I'm sorry. I flew us right into this.  : What were we thinking? Look at us. We're just a couple of bugs in this world. ADAM: What will the humans do to us if they win? BARRY: I don't know. ADAM: I hear they put the roaches in motels. That doesn't sound so bad. BARRY: Adam, they check in, but they don't check out!  ADAM: Oh, my. (Coughs) Could you get a nurse to close that window? BARRY: - Why? ADAM: - The smoke. (We can see that two humans are smoking cigarettes outside)  : Bees don't smoke. BARRY: Right. Bees don't smoke.  : Bees don't smoke! But some bees are smoking.  : That's it! That's our case! ADAM: It is? It's not over? BARRY: Get dressed. I've gotta go somewhere.  : Get back to the court and stall. Stall any way you can. (Flash forward in time and Adam is making a paper boat in the courtroom) ADAM: And assuming you've done step 29 correctly, you're ready for the tub! (We see that the jury have each made their own paper boats after being taught how by Adam. They all look confused) JUDGE BUMBLETON:  Mr. Flayman. ADAM: Yes? Yes, Your Honor! JUDGE BUMBLETON: Where is the rest of your team? ADAM: (Continues stalling) Well, Your Honor, it's interesting.  : Bees are trained to fly haphazardly,  : and as a result, we don't make very good time.  : I actually heard a funny story about... MONTGOMERY: Your Honor, haven't these ridiculous bugs  : taken up enough of this court's valuable time?  : How much longer will we allow these absurd shenanigans to go on?  : They have presented no compelling evidence to support their charges  : against my clients, who run legitimate businesses.  : I move for a complete dismissal  of this entire case! JUDGE BUMBLETON: Mr. Flayman, I'm afraid I'm going  : to have to consider Mr. Montgomery's motion. ADAM: But you can't! We have a terrific case. MONTGOMERY: Where is your proof? Where is the evidence?  : Show me the smoking gun! BARRY: (Barry flies in through the door) Hold it, Your Honor! You want a smoking gun?  : Here is your smoking gun. (Vanessa walks in holding a bee smoker. She sets it down on the Judge's podium) JUDGE BUMBLETON: What is that? BARRY: It's a bee smoker! MONTGOMERY: (Picks up smoker) What, this? This harmless little contraption?  : This couldn't hurt a fly, let alone a bee. (Montgomery accidentally fires it at the bees in the crowd and they faint  and cough) (Dozens of reporters start taking pictures of the suffering bees) BARRY: Look at what has happened  : to bees who have never been asked, "Smoking or non?"  : Is this what nature intended for us?  : To be forcibly addicted to smoke machines  : and man-made wooden slat work camps?  : Living out our lives as honey slaves to the white man? (Barry points to the honey industry owners. One of them is an African American so he awkwardly separates himself from the others) LAWYER: - What are we gonna do? - He's playing the species card. BARRY: Ladies and gentlemen, please, free these bees! ADAM AND VANESSA: Free the bees! Free the bees! BEES IN CROWD: Free the bees! HUMAN JURY: Free the bees! Free the bees! JUDGE BUMBLETON: The court finds in favor of the bees!  BARRY: Vanessa, we won! VANESSA: I knew you could do it! High-five! (Vanessa hits Barry hard because her hand is too big)  : Sorry. BARRY: (Overjoyed) I'm OK! You know what this means?  : All the honey will finally belong to the bees.  : Now we won't have to work so hard all the time. MONTGOMERY: This is an unholy perversion of the balance of nature, Benson.  : You'll regret this. (Montgomery leaves and Barry goes outside the courtroom. Several reporters start asking Barry questions) REPORTER 1#: Barry, how much honey is out there? BARRY: All right. One at a time. REPORTER 2#: Barry, who are you wearing? BARRY: My sweater is Ralph Lauren, and I have no pants.  (Barry flies outside with the paparazzi and Adam and Vanessa stay back) ADAM: (To Vanessa) - What if Montgomery's right? Vanessa: - What do you mean? ADAM: We've been living the bee way a long time, 27 million years. (Flash forward in time and Barry is talking to a man) BUSINESS MAN: Congratulations on your victory. What will you demand as a settlement? BARRY: First, we'll demand a complete shutdown of all bee work camps. (As Barry is talking we see a montage of men putting "closed" tape over the work camps and freeing the bees in the c…

---
## [catannoyance/ylab_t1](https://github.com/catannoyance/ylab_t1)@[dbc944afec...](https://github.com/catannoyance/ylab_t1/commit/dbc944afec9a07d580cb53540f59bacfbeec74f3)
#### Thursday 2023-11-16 18:58:07 by catannoyance

adjust dark theme colors for text fields

i'm not happy to step away from tailwind's color scale, nor am i really happy with how it looks anyways, but i think this is at least an improvement - previouesly fields had way too much contrast with the background in my opinion (and before that, none at all)
maybe someday i will be good at these kind of things but today is not that day

---
## [foxglove/studio](https://github.com/foxglove/studio)@[afe02317ee...](https://github.com/foxglove/studio/commit/afe02317ee9a74ac906b2a4dac120a6d77a2acfa)
#### Thursday 2023-11-16 19:06:04 by Caleb Foust

Fix plot story flakiness (#7112)

**User-Facing Changes**
None; this is just an improvement to developer experience.

**Description**
Our plot stories have been flaky for a while, even predating the changes
I made to move data processing into a worker. This PR attempts to fix
these issues.

There were two main causes for flaky stories:
1. The mechanism we were using to indicate that a story was ready was
error-prone, particularly after moving plot data processing to a worker,
which meant that differences in timing could cause us to render an
inconsistent number of times. This broke the traditional
`useReadySignal({ count: N })` strategy.
2. There were (and are) significant problems with timing in the `Chart`
component, which sends rendering jobs to a Web Worker that uses ChartJS.

I fixed #1 by switching to a strategy where, instead of counting the
number of rerenders, we wait a certain amount of time after the last
time the Chart component renders before declaring the story "ready".
This may not actually fix this problem definitively because Chromatic's
workers are extremely weak, but it's less error-prone than hoping we get
the same number of renders every time.

For #2 I added what can only be described as a hack because that
component is woefully, woefully tangled. (I'm getting flashbacks to our
layout bug.) We have several interacting layers of React state (mostly
refs), `async` code that can complete at any time, and then, if that
weren't enough, the whole `Rpc` layer that also seems to respond to
requests whenever it feels like.

The core problem is that we were [waiting for a bunch of calls to
finish](https://github.com/foxglove/studio/pull/7112/files#diff-c83b85fde0ce9eb98a2d3d36cc869873cad467fc1fb3aa3f4cc48a8fe73e6b8fR286)
asynchronously and then setting some state on the component, which in a
compute-constrained environment could mean that several seconds have
already passed. In other words, the requests in flight elsewhere were
being randomly overwritten.

In my opinion, we really just need to rewrite this whole section with
`getNewUpdateMessage`, the queued updates stuff, and initialization. I
swear, at least half of the problems we've had with rendering and timing
have been because of this code block.

---
## [8n8/trumat](https://github.com/8n8/trumat)@[39f9d3cd3a...](https://github.com/8n8/trumat/commit/39f9d3cd3a549856850e464daea43115b0d2743d)
#### Thursday 2023-11-16 19:13:52 by True Ghiassi

Trivial implementation of format library in Go

The previous implementation was in C and the one before that was in Haskell.

The reason for using Haskell was that I was used to it, especially the
parser combinator libraries. However I realised after a while that it is
easy to do parser combinators using ordinary functions in an imperative
language, so that wasn't really a good reason for using Haskell any more.

One pain point with Haskell was the slow compile times. I found that the
fastest I could do an incremental compilation was about 7 seconds. This was
with the compiler optimisations turned off. It doesn't sound much but I was
doing test-driven development and was spending a lot of the time waiting
for those 7 seconds.

Another problem with Haskell is that it's hard to cross compile. This is
a nuisance because I want to be able to support at least Mac, Linux and
Windows.

It's also time-consuming to build from source if you haven't got Haskell
already. So it's asking a lot to expect users to build Haskell code from
source.

Another problem with Haskell is that there are a lot of major versions of
GHC. This means that you have to have a lot of compilers around in Haskell
development. Or you can keep upgrading.

Then I was trying C. The main reasons were very fast build times and very
fast run times. I also like the language. It's also much easier to build it
from source and to cross compile.

I was really enjoying working in C. I could compile and run about 3000
tests in about 0.2s. This makes a huge difference when you are working with
test-driven development.

The big problem was that I was often running into memory issues. One way I
would notice these was by the tests breaking on some trivial change. For
example reordering the arguments in a function or marking a function as
static. I would also get segmentation faults.

The only way I could find to debug these issues was to run the tests in
Valgrind. Valgrind is a great tool and this method worked really well.
However I was having to run Valgrind really often to check if I had
introduced a memory issue. And my test suite was taking around 6 minutes
to run in Valgrind.

So effectively when developing in C I had a very slow feedback loop, much
too slow to do test-driven development.

I started shopping around for a different language. The requirements were:

- fast at runtime
- fast to do compilation + tests + memory safety checks
- easy to cross compile or easy for users to build from source
- stable

I looked at a lot of languages.

I thought scripting languages like Python, Ruby or Javascript would be
too slow, and also require that users have the right version of the
runtime.

Rust has a really slow compiler.

I'm not very familiar with OCaml but it seems it is difficult to
cross-compile and I don't think I can expect my users to install an OCaml
toolchain.

Zig looks great but it isn't stable yet. I might also find I need to run
Valgrind as its memory safety isn't very strong.

I had a look at C#. It has a lot of nice properties. It is one of the
fastest languages with automatic memory management. The benchmarks in the
benchmarks game website have it consistently faster than Go. However when
I looked at the implementations the C# ones were dropping down into unsafe
code, so I might as well carry on using C.

It seems a bit much to expect users to install dot net, but I found that
you can bundle C# apps into a self-contained binary, although it is rather
large.

I also had a look at Nim. It looks like a great language and would allow
me to easily cross compile. It seems very performant. The main thing that
put me off was the lack of stability. There was a version 2.0, which must
have broken a lot of 1.0 code. I want to avoid the Haskell situation of
having dependencies on a particular compiler version.

I considered Roc. I think it's going to be a brilliant language one day,
and is probably performant enough. However it is not at all stable yet and
I don't want to have to do large upgrades.

The main issue with Go is that it is significantly slower than C. It's hard
to be precise without implementing the whole thing in both C and Go and
comparing, but a ballpark figure from browsing toy benchmarks online would be
that Go programs are several times slower than C ones, maybe 2 to 5 times
slower.

However Go performs very well compared to other languages with automatic
memory management.

Go ticks off the other requirements. It is good at cross compiling, it
compiles really fast, there are no memory leaks, it's easy to deploy, it's stable.

By switching from C to Go I am getting a much shorter development feedback loop
in exchange for less performance at run time.

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[0f5d14e68b...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/0f5d14e68b19111592301efe52a03de80aced61e)
#### Thursday 2023-11-16 20:03:13 by Ben10Omintrix

Mook village and basic mook refactor (#78789)

## About The Pull Request
refactors mooks into basic mooks and re-adds them to the game

## Why It's Good For The Game
this refactors mooks into basic mobs and re adds them to the game. mooks
are now a part of lavaland. they come as a part of a random ruin which
consist of a entire village of friendly mooks. Mooks will aid players
but they will still attack ashwalkers because of some troubled history
between them.

![mookvillage](https://github.com/tgstation/tgstation/assets/138636438/ad1c5d63-c168-475a-a85d-b727dff43e7b)

mooks are a very diseased specie. nanotrasen discovered a small tribe of
mooks and cut a deal with their tribal chief to aid ss13 miners in
exchange for medical supplies.

tribal chief in his decked out home

![tribalchief](https://github.com/tgstation/tgstation/assets/138636438/cc0e0a11-9bf0-4322-b3ae-c7be43092ee8)

male mooks go out and mine and haul ore off back to their village. they
will deposit ores into a stand which is managed by another mook. they
will all return to their village to rest once a lavastorm comes.

![mookstand](https://github.com/tgstation/tgstation/assets/138636438/c7adbf4e-6322-4347-acfc-4e8d45aff798)

players can use this stand to withdraw any ore they like

![mookui](https://github.com/tgstation/tgstation/assets/138636438/a1318be8-50f7-49b2-827c-97bafdb2488a)

female mooks will stay behind in the village to guard it from
ashwalkers. they will also heal male mooks when they come back from a
long day of work. the tribal chief is a bum and chooses not to go out
and mine. he will stay behind in the village and issue commands to his
people rather than work

the village also has its own bard! he follows player visitors and plays
nice music for them while they are in the village (although he is not
very talented).

![mookbard](https://github.com/tgstation/tgstation/assets/138636438/5123e492-6657-4755-9dc7-ab94d4beb554)

he is still a warrior at heart tho so he will be smashing his guitar
over ashwalker skull

![mookshmash](https://github.com/tgstation/tgstation/assets/138636438/bf211bf0-e963-4dbb-b004-e653e06e3974)




## Changelog
:cl:
refactor: mooks are now basic mobs. please report any bugs
feature: added mook village to lavaland ruins!
/:cl:

---
## [Overhatted/buck2-strip-prefix](https://github.com/Overhatted/buck2-strip-prefix)@[670205798b...](https://github.com/Overhatted/buck2-strip-prefix/commit/670205798bd6fd69196bdf3e0224ba60e20dc8e2)
#### Thursday 2023-11-16 20:15:50 by Jakob Degen

toolchain: Set up no-sysroot deps toolchain

Summary:
This diff lays out how I want to avoid the cyclic dependency issue with explicit sysroot deps compiled from source.

Doing this by defining a second toolchain is generally appropriate I think. Asking crates that expect to be compiled as members of the sysroot to declare that by specifying a non-default toolchain seems correct. Also, a constraint would be inappropriate here because we do not generally want to propagate this to all target dependencies, and because it runs into risks of accidentally ending up with the same dep in your build twice, under two different configurations.

I didn't bother trying to add support to `override_rust_toolchain` for this because we'd need something like `attrs.struct()` to make that not super ugly. Plus, rules are good and people should write more of them.

The one potentially controversial decision in this diff is the choice to put the override above the massive toolchain select tree, instead of below. On balance, I'd guess that this is the better thing to do. This override is only responsible for inserting the sysroot targets; I expect that it'll only ever grow two cases, one for fbcode sysroot targets and one for fbsource ones. That means we'll never need all the complicated machinery that's in the big select tree. Plus, selectified toolchains are good anyway.

Reviewed By: capickett

Differential Revision: D51014702

fbshipit-source-id: 970de5291aa725e1e5e1e22fdde53603e1e4d412

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[66b8b1d866...](https://github.com/tgstation/tgstation/commit/66b8b1d8669379eac50fa358a3eb5e7707b46f25)
#### Thursday 2023-11-16 21:33:07 by Fikou

Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

---
## [Dime1154/mojave-sun-13](https://github.com/Dime1154/mojave-sun-13)@[c65f22da38...](https://github.com/Dime1154/mojave-sun-13/commit/c65f22da381954082c8818862c06397a274ec797)
#### Thursday 2023-11-16 21:51:58 by Hekzder

Post Test Tweaks for early July (#2410)

* makes alcohol tolerance not stupid

yea

* bit of a PA nerfy

Just on lower end PA so like the frame and T-45

* Forage respawn time increase + herbal remedy tweak

yea

* ciggy tweaks and spawn fixes

yea

* actually tested it and made proper changes lol!

woo!!

* god I hate TG

this is insane

---
## [IsaacWoods/poplar](https://github.com/IsaacWoods/poplar)@[44c48c953c...](https://github.com/IsaacWoods/poplar/commit/44c48c953cf5157a8ed025ce8a500592323306e5)
#### Thursday 2023-11-16 22:46:05 by Isaac Woods

`hal_riscv`: rename references to top-level page table in paging impl

This is the first step in making the paging impl generic over how many levels
the tables have. I'm thinking we'll be able to add a generic for the top-level
to `PageTableImpl`, and then somehow specialise each method to how many
levels need to be traversed, but we may discover that's a pain in the ass
and either a) do it at runtime with an enum or something or b) make separate
types for each paging scheme and make it the user's problem to be generic
over them (this also makes it my problem but slightly later in time).

---
## [KadTheHunter/KadTheHunter.github.io](https://github.com/KadTheHunter/KadTheHunter.github.io)@[5c9403f47f...](https://github.com/KadTheHunter/KadTheHunter.github.io/commit/5c9403f47f28176437abf5303c6084a978af49cf)
#### Thursday 2023-11-16 22:56:50 by Kaddicus

Fix category typo

CTRL + Z is a double edged sword, it saves my ass from stupid decisions, but also causes shit like this.

---
## [Encylol/tgstationRIPOFF](https://github.com/Encylol/tgstationRIPOFF)@[3e554bdab3...](https://github.com/Encylol/tgstationRIPOFF/commit/3e554bdab3ae7ffff4bd9090b71dc0b3666f081f)
#### Thursday 2023-11-16 23:02:45 by Jacquerel

Flesh Spiders Regenerate + QoL (#78704)

## About The Pull Request

Replaces the Healing Touch component on Changeling-spawned Flesh Spiders
with the Regenerator component, as the comment helpfully suggests.
Flesh Spiders can no longer touch themselves to heal, instead they
automatically begin regenerating their health if they go four seconds
without taking damage. It takes 6 seconds to fully regenerate, so 10
seconds to fully heal from the edge of death (less if you're not that
injured).


![image](https://github.com/tgstation/tgstation/assets/7483112/37faca55-35fe-48dc-a3ed-03f4b79860bd)

Also I changed the sprite for flesh spider eggs to a different one we
already had rather than regular spider eggs tinted red, just because I
felt like it.
Would be cool to give the spiders their own sprite some time, but that's
for another PR.


![image](https://github.com/tgstation/tgstation/assets/7483112/8ec286c4-46dc-4aec-aa98-cb4e4e432690)
_Additionally_ the flavour text for flesh spiders was kind of messed up
by being shoved into the objectives box and claiming that it was a
directive from a spider queen you don't have, so I gave them their own
slightly different antag datum to compensate.
It also actually mentions how you heal yourself, which previously was
down to trial and error or codediving.

In the course of doing this I decided to just... move flesh spiders to
their own type path. It _sort of_ made sense for them to be part of the
giant spider typepath, but they keep being modified by changes targetted
at "balancing the Giant Spiders antagonist" which this mob isn't related
to and doesn't have any reason to follow. The fact that a mob has
similar stats to another one isn't automatically a reason to share a
typepath, and now that I have looked a little at this mob I'm sort of
interested in branching it further away from "it's a spider mob but
spawned a different way" in the future.

Finally, this spider egg cluster and the midwife one would prompt ghosts
with a radial menu with a single option on it... that's a bit pointless,
so we'll bypass that menu if there is only one possible outcome.

## Why It's Good For The Game

Currently Flesh Spiders heal by clicking on themselves and standing
still for two seconds, restoring 50% of their HP. This means they can
fully regenerate over 4 seconds unless you stun them, and with 90 HP
you're not _that_ likely to kill one during the channel time.
This just feels like an odd way for the creature to operate,
regenerating instead gives it a hit-and-run strategy and adds more use
to their webs (maybe we should give them meatier or bloody webs at some
point? Might be cool).
Also clicking yourself to heal is just unintuitive and I suspect several
players just didn't realise they could do it in the first place.

## Changelog

:cl:
balance: Flesh Spiders heal automatically over time if they go a short
time without taking damage, instead of healing large chunks by clicking
themselves and waiting two seconds.
qol: Spider egg clusters which only hatch into one kind of spider don't
ask you to select that one type from a radial menu with one option on
it.
qol: As a Flesh Spider, the game now tells you how you can heal
yourself.
/:cl:

---
## [Thera-Pissed/Shiptest](https://github.com/Thera-Pissed/Shiptest)@[2a74c23d62...](https://github.com/Thera-Pissed/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Thursday 2023-11-16 23:13:58 by Imaginos16

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
## [Thera-Pissed/Shiptest](https://github.com/Thera-Pissed/Shiptest)@[bf4671ff83...](https://github.com/Thera-Pissed/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Thursday 2023-11-16 23:13:58 by retlaw34

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
## [DarklightGames/DarkestHour](https://github.com/DarklightGames/DarkestHour)@[725059ec01...](https://github.com/DarklightGames/DarkestHour/commit/725059ec0154c16419d3e8c84f7eab6cdd83c179)
#### Thursday 2023-11-16 23:27:53 by Colin Basnett

Removed the `MaxCriticalSpeed` system that would make driving tanks annoying as hell

The system was added years and years ago to stop tanks from ski-jumping down hills at insane speeds on a particular map. In all other cases it just makes driving a chore because the game will downthrottle your vehicle without telling you. Good riddance.

---

