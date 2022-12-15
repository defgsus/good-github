## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-14](docs/good-messages/2022/2022-12-14.md)


2,049,777 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,049,777 were push events containing 3,093,568 commit messages that amount to 261,068,671 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [xiaoleGun/Home](https://github.com/xiaoleGun/Home)@[ba91e1ad05...](https://github.com/xiaoleGun/Home/commit/ba91e1ad05dfa5cda3e659d9ad02a1d95102a4c2)
#### Wednesday 2022-12-14 00:10:27 by xiaoleGun

Fuck your mother's militaristic Japan

 *  The Nanking Massacre, commonly known as
    the Rape of Nanking, was an infamous war
    crime committed by the Japanese military
    in Nanjing (Nanking), then the capital of
    the Republic of China, after it fell to the
    Imperial Japanese Army on December 13, 1937.
    The duration of the massacre is not clearly
    defined, although the violence lasted well
    into the next six weeks, until early February 1938.
    Japanese officials lied about civilian death figures and
    still refuse to reveal them properly today.
    During the occupation of Nanking, the Japanese army
    committed numerous atrocities, such as rape, looting,
    arson and the execution of prisoners of war and civilians.
    The executions began under the pretext of eliminating Chinese
    soldiers disguised as civilians, and a large number of innocent
    men were intentionally misidentified as enemy combatants and executed
    as the massacre gathered momentum. A large number of women
    and children were also killed, as rape and murder became more widespread.
    The Japanese side has not recognized the Nanjing Massacre!!!

 *  南京大虐殺は、1937年12月13日に日本帝国軍の手に渡った後、日本軍が当時の中華民国の首都
    南京（南京）で犯した悪名高い戦争犯罪である。大虐殺の継続期間は明確に定義されていないが、
    暴力は1938年2月初めまで6週間続いた。日本の役人は民間人の死亡数を偽って、今も公開を拒
    否している。南京占領中、日本軍は強姦、強盗、放火、捕虜と民間人の処刑など多くの暴行を犯
    した。処刑は民間人を装った中国兵の撲滅を口実に始まった。大量の罪のない男が故意に敵戦闘員
    と誤認され、大虐殺が激化する中で処刑された。レイプや殺人が一般的になるにつれ、多くの女性
    や子供も殺害された。
    日本側は、いまだ南京大虐殺を認めていない!!!

Signed-off-by: xiaoleGun <1592501605@qq.com>

---
## [TJatPBnJ/tgstation](https://github.com/TJatPBnJ/tgstation)@[5da871e271...](https://github.com/TJatPBnJ/tgstation/commit/5da871e2719fb7aac04fb1ec4c85ea7a09a83b36)
#### Wednesday 2022-12-14 00:14:16 by RikuTheKiller

Made geysers easier to find (#71608)

## About The Pull Request

This PR raises the geyser spawn rate from 0.1 to 0.15 and increases the
weight of wittel geysers to 10 which is the same as every other special
geyser. (previously 6)

Wittel shouldn't be any less difficult to find than other geysers as all
of the special geysers are equally powerful. Hyper-plasmium oxide can be
used to make extremely powerful explosives that can go beyond maxcaps
and hollow water + protozine can create an infinite amount of strange
reagent.

I've subjected myself to going out of my way to visit lavaland/icemoon
several times to get wittel and each time finding a single geyser takes
about 5 minutes of my time. This, coupled with the fact you really don't
have a lot of time to be wasting on looking for the geysers results in
an unfun experience.

I understand geysers are sort of a necessary evil, however, they
shouldn't be THIS difficult to find. Out of the 10 or so geysers I've
found, only 1 has had wittel in it and it was next to a whelp portal
which ended both me and my miner escort.

I've also hunted the entirety of lavaland with no luck. (Horrendous
experience.)

I've dedicated entire rounds to this, by the way.
## Why It's Good For The Game

If you go out of your way to waste ages hunting for geysers, there
should at least be a reward. That is, in the same round, not after 3 or
more rounds as even megafauna gear isn't gatekept THAT hard.

You shouldn't have to waste this much of a miner's time (who is also
going for megafauna gear) to get something that is arguably less
powerful than what they get for less effort. Megafauna gear is also
available every round and is attained via predictable methods.

This PR will also likely make geyser scanning a more comparable method
of point gain to just mining.

Oh and not to mention that penthrite is available almost roundstart via
luxpens. (It's a wittel chem.)
## Changelog
:cl:
balance: Geysers now spawn more often, especially wittel geysers.
/:cl:

---
## [TJatPBnJ/tgstation](https://github.com/TJatPBnJ/tgstation)@[2425531eb2...](https://github.com/TJatPBnJ/tgstation/commit/2425531eb2dab84fb27ed864e4c52470bfff6918)
#### Wednesday 2022-12-14 00:14:16 by John Willard

Removes tablets (not PDAs) entirely. (#71507)

## About The Pull Request

**Comes with an UpdatePaths!**

Removes the tablet subtype, PDAs now replaces them entirely.

Nukie and Silicon tablets are now subtypes of the PDA instead, while
contractor ones were removed entirely as they didn't do anything and
were unused (though it wouldn't be hard to re-add).

Nukie PDAs are now the only type of PDA that uses modular_tablets.dmi,
which is just larger icons of modular_pda. Each application requires an
icon state in both of these, for 2 different sizes, which makes it
annoying to make new applications, especially if it can also run on
computers/laptops.

### Icons

Because Silicon tablets are now a subtype of PDA, they use PDA icons
instead of tablet ones. Luckily for us, they already exist in code.

![image](https://user-images.githubusercontent.com/53777086/203876575-56eb1593-774c-47c6-8e7d-491a7805f28c.png)

AI's don't use a tablet icon though, so they aren't affected.

## Why It's Good For The Game

There's very little difference between tablets and PDAs, PDAs overshadow
them in every single way, so at this point I don't see why we should
have both of these, and if you compare the two in usefulness and actual
in-game use by players, it's a no-brainer than the item all players get
roundstart and comes with a messenger should be the one we go with.

Also as said in the about section, when making an app you would need to
make icon states for the program running for all hardware it can run on,
which is Computer, Laptop, PDA, and Tablet.

Laptop is just a smaller computer icon
PDA is just a smaller tablet icon

However, you can't simply shrink the size of the icon, instead you have
to completely resprite the same app icon FOUR TIMES for it to not
bluescreen on all these different devices.

<details>
<summary>
Here's examples of it
</summary>
Computer (NOTE: *They share the same icon file as regular computers*)
<img
src="https://user-images.githubusercontent.com/53777086/203876801-486a8054-489a-4983-bdad-a2599b4dc379.png"/>
Laptop
<img
src="https://user-images.githubusercontent.com/53777086/203876333-58e5d135-f4c6-4a02-8948-1df771e294a4.png"/>
Tablet
<img
src="https://user-images.githubusercontent.com/53777086/203876352-816c7fb1-c681-40b9-99e0-052f49632c7f.png"/>
PDA
<img
src="https://user-images.githubusercontent.com/53777086/203876358-1cf7253d-3c6a-456a-8133-ebf7f0351637.png"/>
</details>

If we wish to help in simplifying this, we should remove tablet icons
entirely, which means 1 less icon to worry about. To do this, we'd need
to resprite nukie PDAs, however I am very much not a spriter and never
tried GAGS, so I'll leave it to someone else to do.

## Changelog

:cl:
del: Tablets are now removed, PDAs are now the base 'tablet'. Silicon
and nukie tablets are now PDAs.
/:cl:

---
## [Cryleve/sojourn-station](https://github.com/Cryleve/sojourn-station)@[2747557916...](https://github.com/Cryleve/sojourn-station/commit/2747557916f2db8c94c80995c12a8516d7dbd351)
#### Wednesday 2022-12-14 00:43:04 by DimmaDunk

Drip megapack 100% real not fake 1 commit church buff speedmerge (#3188)

* Drip megapack 100% real not fake 1 commit church buff speedmerge

- Adds Justice, Pandemonica, Malina, Zdrada and Modeus alt styles for charming outfit
- Adds a black suit jacket with adjustable styles for the charming outfit
- Adds charming waistcoat for Malina/Cerberus drip
- Ports the Tojo Pants and Tojo Jacket from the mad dog of Shimano himself
- Ports black and red overcoat styles (Joker, Morningstar)
- New sprites for Prospector/Foreman lockers, Salvager lockers changed in appearance to rusty old ones for fluff
- Adds New Testament Knight Hardsuit RIG module for the church's New Testament Armaments Disk, a Divisor/Numerical joint effort in producing a combat-ready hardsuit. A pre-loaded version with flash, shield, jetpack and storage modules spawns on the Prime's office's altar. Same stats as the Combat Hardsuit.

* Adds Knight RIG module sprite

Solving merge conflicts.

* Catifies your SCAFs

SCAF helmet and Blackshield SCAF helmet given alternate styles with cat ears for that Halo drip.

---
## [nuke-ops/Nostra-13](https://github.com/nuke-ops/Nostra-13)@[8eec99b320...](https://github.com/nuke-ops/Nostra-13/commit/8eec99b3206e917bd711987a80422168de53f83d)
#### Wednesday 2022-12-14 00:48:01 by LemonInTheDark

Caches GetJobName. Fuck you (#274)

* Caches GetJobName. Fuck you

This code made me deeply upset, WHY IS IT RECURSIVE WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY

* Centcom handling, properly this time

* Empties out real_job_name

* Sets real_job_name up in the right place

* Moves real_job_name to SSjob, uses modularTM

* Yeet

* Removes old code, swaps over to the SSjob list

* dme changes

* indents... comments

Co-authored-by: SandPoot <enric_gabirel@hotmail.com>

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[44008f485d...](https://github.com/TrashDoxx/TG/commit/44008f485d6d72537935cfa8a3a5b6140eece744)
#### Wednesday 2022-12-14 01:03:25 by Jacquerel

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
## [Higgin/Skyrat-tg](https://github.com/Higgin/Skyrat-tg)@[460ab7adf5...](https://github.com/Higgin/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Wednesday 2022-12-14 01:37:34 by SkyratBot

[MIRROR] JPS Optimization (Light Botcode) [MDB IGNORE] (#17669)

* JPS Optimization (Light Botcode) (#70623)

## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@ Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog

:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* JPS Optimization (Light Botcode)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[e766444468...](https://github.com/MidoriWroth/tgstation/commit/e766444468445f084d3714b515003d3f40bbce69)
#### Wednesday 2022-12-14 03:14:19 by LemonInTheDark

Changes our map_format to SIDE_MAP (#70162)


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

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Pat070028/app-dev](https://github.com/Pat070028/app-dev)@[8ce6cf92de...](https://github.com/Pat070028/app-dev/commit/8ce6cf92deded790d4e5031ed91a15d7a6e41c76)
#### Wednesday 2022-12-14 03:49:28 by Pat070028

Update README.md

info about titanic movie - It stars Kate Winslet and Leonardo DiCaprio. The two play characters who are of different social classes. They fall in love after meeting aboard the ship, but it was not good for a rich girl to fall in love with a poor boy in 1912.
info about spiderman movie - After being bitten by a genetically-modified spider, a shy teenager gains spider-like abilities that he uses to fight injustice as a masked superhero and face a vengeful enemy.
info about end game movie - After half of all life is snapped away by Thanos, the Avengers are left scattered and divided. Now with a way to reverse the damage, the Avengers and their allies must assemble once more and learn to put differences aside in order to work together and set things right.

---
## [CRITAWAKETS/coSINE19](https://github.com/CRITAWAKETS/coSINE19)@[54b475eb0b...](https://github.com/CRITAWAKETS/coSINE19/commit/54b475eb0b3ff9913f6ec5de25243c899edcde7a)
#### Wednesday 2022-12-14 04:26:01 by Andromeda

removes annoying shit

sorry, i hate punpun and the portals

---
## [4hands44/cmss13](https://github.com/4hands44/cmss13)@[eb4886c115...](https://github.com/4hands44/cmss13/commit/eb4886c115a0965a347783b87eb3415f098c2c1f)
#### Wednesday 2022-12-14 04:27:11 by carlarctg

Spitter Rework (#1541)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Design doc:

https://hackmd.io/@waltuh/Sy0A1SnEo
Slightly inaccurate as my brainworms enticed me to change and add mini
features.

Approved by Walter, ignorepproved by Gevonius and Satanbatros


https://cdn.discordapp.com/attachments/280051925154660363/1041475609165045770/image.png

Changes:
- Spit doesn't spatter by default, instead it's now a faster, weak
7-tile* projectile that deals 20 damage with a faster spit cooldown.
Fully accurate at 6 tiles, inaccurate at 7 tiles but can sometimes hit.
- Frenzy replaced with 'charge spit'. Halved speed buff, added +5 armor
buff, the next spit will deal 10 more damage and coat humans in acid but
have only 5* tiles of range.
- Acid spray halves damage every time someone walks on it. However, its
damage is spread over legs and feet, and if someone who is spattered
with acid is hit by it, their acid spatter will be strengthened, dealing
more damage, lasting longer, and needing two rolls to clear up. Also,
the bonus damage didn't actually work, now it does.

* Projectile range code is SHIIIT and breaks on diagonals so the range
variable is increased.

Also, queen acid spit spatters and has 1 second less extra cooldown
because find and replace caused it and I didn't think it was a change
worth removing. It's neat, maybe they'll actually use it now.

Added support for balloonchat colors. (Even TG doesn't have this, we're
awesome now!)

Renamed vision_distance parameter to max_distance so it's similar to
visible_message

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

As stated in the hackmd, spitter is very ineffective without using the
oversight-exploit infinite acid spray spam, and its combo (acid spatter
into spray) does not actually help, as the stun stops the human from
getting further hit by the spray and the bonus damage does not actually
apply thanks to shitcode. This PR makes it so that the combo is indeed
more effective than making humans walk into the spray.

Again as stated, spitter suffers from a strange issue where it's
actually not good at harassing from range despite that being its
purpose, since it has a low range. By letting it be long ranged by
default and choose to go short range, it adds a lot of depth and
versatility and lets it actually harass marines.

As always they can just. Shoot it to make it go away. 

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
refactor: Added support for balloonchat colors. (Even TG doesn't have
this, we're awesome now!)
add: Spitter rework!
add: Spit is now full screen range but weaker.
add: Frenzy is renamed and causes spit to inflict spatter coating.
add: Acid spray's damage is halved every time it hits a human, but if it
hits someone coated in acid it will enhance it, making it more dangerous
and need two rolls to shake off.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [4hands44/cmss13](https://github.com/4hands44/cmss13)@[146d4a3fa8...](https://github.com/4hands44/cmss13/commit/146d4a3fa87a25a16e7246c32d85b6b57614adc5)
#### Wednesday 2022-12-14 04:27:11 by carlarctg

Cloaked belltower alpha increased from 10 (scout) to 35. (#1768)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Var change.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

You may think this is a 'ided' change, that I got owned by a bell tower
and opened this PR. But believe me, it's the exact other way around.

I play engineer often, especially on New Varadero, and every time I pick
the cloaked bell. It is hilariously busted, but that's not actually the
point here. The reason I'm making this PR is because it is genuinely
_impossible_ to find the belltower if it's fully cloaked. If you don't
memorize the placement you quite literally HAVE to right click over
every single tile in the region because the alpha value is SO low it is
just not feasible to detect. I'm saying this as an engineer, it's too
damn much, it takes me half a minute to find my tower and pack it up
again. Worse, sometimes people take it or a xeno slashes it while I'm
being defibbed and I can't tell if I just can't find it or what.

The difference between scout's cloak and the belltower's cloak is that
scout has a large one color silhouette and is constantly moving, and can
additionally be detected through walls by xenos, though again, not the
reason for this. The belltower has a small, thin silhouette that has
lots of gaps in its sprite, making it very hard to locate by hand.

That this will weaken the belltower against xenos is no surprise, but I
don't think that's a problem. As I said, the belltower is busted. I say
this as someone who uses it more than has it used against them. 6
seconds of superslow in a 4x4/5x5 range!

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
balance: Increased alpha (reduced camo) of the camo belltower from 10 to
35. This is mainly meant for engineers to be able to see their tower to
pick it up, but the inevitable balance changes aren't unintended.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [mattdway/CreateWithVR](https://github.com/mattdway/CreateWithVR)@[72fd1329b6...](https://github.com/mattdway/CreateWithVR/commit/72fd1329b62c4955b451af49eaa3704182d04c23)
#### Wednesday 2022-12-14 06:07:24 by mattdway

12-13-22 v2.5.2

12-13-22 v2.5.2
12-13-22 Commit
I was able to work out a many of the remaining issues with my physics hands tonight.

Being able to spam select things is now gone by changing Select Action Trigger on the XR Interactable from State to State Selected on the "LeftHand Controller With Physics" and the "RightHand Controller With Physics" controller game objects.

Not only can't you spam the select button to select something over and over again, this also prevents being able to pick up multiple objects with the same hand and it also prevents being able to grab an interactable with a single grab point with both hands at once, which also eliminates the obnoxious haptic and sound feedback that would happen when grabbing an object with a single grab point with both hands at once. Now, the behavior is that it simply switches hands.

I also turned off physics hands on the opposite hand in one instance by adding some additional Interactable Events for "Select Entered" and "Select Exited" on the XR Interactable on the "LeftHand Controller With Physics" and the "RiightHand Controller With Physics" controller game objects.

Each controller object now has the following:

Select Entered
LeftHandPhysics Hand.ToggleVisiibility
LeftHandPhysics HandPhysics.DisableHandCollider
RightHandPhysics HandPhysics.DisableCollider

Select Exited
LeftHandPhysics   Hand.ToggleVisiibility
LeftHandPhysics   HandPhysics.EnableHandColliderDelay with a time duration of 0.5
RightHandPhysics  HandPhysics.EnableHandColliderDelay with a time duration of 0.5

This means whenever something is picked up in the right hand, the right hand disappears and both the right hand colliders are disabled as are the left hand colliders. When something is dropped from the right hand the right hand reappears and both the right hand colliders and left hand colliders are re-enabled again after a wait duration of 0.5ms.

The same is true when something is picked up in the left hand.

The only instance where this isn't true is when you pick something up in the right hand and then switch to the left hand. It appears in this instance the "Selected Exit" executes and the collider for the opposite hand turns back on but this switching of an object in hands for whatever reason doesn't register as a "Select Entered", which means that opposite hand collider isn't turned off again.

If the object is dropped completely and picked back up this triggers Select Entered. I'm not entirely sure why but I haven't found many instances where having the opposite hand physics turned off when holding something is much of a problem. Sometimes you can bump it with a hand and it'll move slightly but even with large objects like the painting, that doesn't cause any severe physics issues, it simply nudges the object slightly. So maybe I'll even allow physics in the opposite hand to remain when picking up an object and only have it disabled for the hand holding the item. We'll see.

I re-enabled distance grab for both hands. At one point I had turned this off on the left hand and I don't remember why. It wasn't a problem that I recall and being able to pick up objects with either hands is helpful. Especially when picking up two items (such as the bottle and the lid) from a table where getting close enough to the object to direct pick up is difficult.

I thought there was a collision issue with distance grab to where I would distance grab an object and it would hit my hand and fly in an odd direction before grabbing. I went ahead and set the same "Select Entered" and "Select Exited" as with the XR Direct Interaction to disable collisions when using the rays.

Select Entered
LeftHandPhysics Hand.ToggleVisiibility
LeftHandPhysics HandPhysics.DisableHandCollider
RightHandPhysics HandPhysics.DisableCollider

Select Exited
LeftHandPhysics   Hand.ToggleVisiibility
LeftHandPhysics   HandPhysics.EnableHandColliderDelay with a time duration of 0.5
RightHandPhysics  HandPhysics.EnableHandColliderDelay with a time duration of 0.5

While I'll keep those Interactor Events enabled what I found in play testing is that this wasn't a problem with the collisions but with the thumbstick press to toggle the ray. It's very easy to let go too soon, thus breaking the distance grab before it completes. Pressing down on the thumbstick is an alternative technique that in some ways works better for distance grabbing. However, pressing on the thumbstick can also accidently engage the snap turning and/or continuous movement when unintended. So distance grabbing with either continuous movement or snap turning can be persnickety and takes some practice and patience on the part of the user. There is maybe a better way to do this to avoid conflicts and to have less work or annoyance on the part of the player. I'll have to research this more and/or pay more attention to how this works in commercial games.

I tried to duplicate the wall glitch by the fireplace but was unable to. I'm not entirely sure what the sequence of events were that allowed this glitch to happen, at this point in time. I'm checking with the student who found this glitch to see how I can reproduce it.

All in all things are working pretty well with the hands and they seem less glitchy than before with these changes made.

I also turned off the Direct Interactor for the ghost hands. Those hands now animate but are not capable of directly picking anything up.

I have tried (using ChatGPT to spitball ideas) to troubleshoot and add 90 degree hand rotation on the physics hands so that these start rotated with the palms facing in. So far any start rotation I add to these interferes with the constant rotation being applied and this causes the hand assets (target per the C# code) to shake. There is most likely a coding solution to this but I haven't found it yet. I'll come back to this one again later.

While it is possible to sometimes get into weird situations where the physics hands will get stuck on something, with collisions with most every object, including walls, floors, interactables, non-interactables, furniture, etc. this is somewhat rare. While I am confident those glitches can occur, I don't know if I can code around every instance of that happening and I don't currently have a known repeatable method of making the physics hands get stuck on something, which would be an instance where I could then further troubleshoot and fix those issues.

I also, at some point, want to add hand-poses for different objects to these hands instead of making the hand disappear.
@mattdway
mattdway committed on Dec 13

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[09407db227...](https://github.com/treckstar/yolo-octo-hipster/commit/09407db227522cbb25b14b58029d80acae172917)
#### Wednesday 2022-12-14 06:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [rkimera94/CancerDB](https://github.com/rkimera94/CancerDB)@[c720c97576...](https://github.com/rkimera94/CancerDB/commit/c720c97576dd34eb97d257c49b0c9876091f37f8)
#### Wednesday 2022-12-14 08:03:17 by Breck Yunits

Fuck you @NSAGov fuck you @CIA. (though if you let me keep my crypto keys we'll call it a truce)

---
## [Nanrech/library](https://github.com/Nanrech/library)@[e527a7d034...](https://github.com/Nanrech/library/commit/e527a7d034f93781d2739a380a1c87c089fdf572)
#### Wednesday 2022-12-14 08:40:20 by EdVraz

feat(channel): Add new overwrite helper methods (#1173)

* fix: edge case

* refactor: move import

* guys I don't recommend coding when you're sick

* do stuff

* omg what the fuck did i code yesterday

* fix: simplify code

* feat: add another helper method

* Update channel.py

---
## [Imaginos16/tgstation](https://github.com/Imaginos16/tgstation)@[fccd833526...](https://github.com/Imaginos16/tgstation/commit/fccd833526364b131ce440b4ab0e65022103927c)
#### Wednesday 2022-12-14 08:42:03 by GoldenAlpharex

Fishing Odds Code Improvements and Rescue Hooks (#71415)

## About The Pull Request
I wanted to try and implement an easier way for people to fish out
corpses from chasms, as I heard many tales of people trying to fish
others out of chasms and it taking over one IRL hour, with some cases
where it would take over two hours. Obviously, that's not really
interesting gameplay, and it doesn't really give people an incentive to
fish, it just turns it into an annoyance that people won't want to do
for fun. Now, we don't want that, do we?

As such, I've created the rescue hook, a special fishing hook that can
only be used in chasms (as that's currently the only place you can find
people into), which will only be able to fish out duds, skeleton
corpses, any mob that's fallen into a chasm and hasn't been rescued yet,
or rarely, a hostile monster lurking below. It has, at the time of
writing this, a weight of 5 (50 without bait, lower with bait) for duds
and a weight of 30 for chasm detritus, which themselves have a 50%
chance to be a random skeleton corpse, or a lobstrosity, and the
remaining 50% chance of fishing out a mob that's fallen into a chasm.
I'm open to tweaking these values if we think it's too easy or too hard,
but it's still a rather expensive item, so I'd consider it quite fine
the way it is myself, as it's still not risk-free.

It's currently only obtainable through buying it from cargo in the
goodies section, at a default price of 600 credits (making it
SIGNIFICANTLY more expensive than the rest of the fishing content, and
making it something that assistants will have to put some elbow grease
into if they want to be able to afford it).

As it stands currently, it can't be used to recover the fallen's
belongings that weren't on their person (i.e., their crusher if they
were holding it in hands), ~*but* I'm down to make that easier to fish
out using, for instance, the magnet hook, while also making it
incompatible with fishing out bodies, which would make it a nice way to
recover those lost items without spending over an hour fishing for them,
if that's something that maintainers would want.~ Maintainers did want
it, and as such...

The Magnetic hook is now the go-to hook to retrieve objects from chasms!
Not only does it inherently do a much better job at fishing out
non-fishes, it also has a lesser chance of retrieving random junk from
chasms, and an even lower chance of fishing out lobstrosities!

I also improved the code for the fishing weights calculation so that the
hooks and the rods can have an effect on the odds of certain types of
rewards more easily, with the option of offloading a more of what's
currently being calculated on `fishing_challenge` over on the rods or
even the hooks themselves.

I finished by fixing a handful of capitalization and punctuation issues
in various fishing items, as that bugged me when I was testing my
changes.

## Why It's Good For The Game
Corpses being recoverable from chasms was a great idea, however making
it so people would have to sink a major portion of their shift for a
chance at recovering a corpse doesn't create a particularly interesting
gameplay loop. However, being able to spend your hard-earned funds in
order to streamline that process without really being able to use that
to cheese other mechanics sounds like a great deal to me.

## Changelog

:cl: GoldenAlpharex
add: Added a Rescue Hook, that will allow the fishing rod it's attached
onto to become a lot more proficient at recovering corpses from chasms,
at the expense of making it unusable for more traditional fishing. It
isn't entirely lobstrosity-proof, however...
balance: The magnetic hook can no longer fish out corpses from chasms,
but will fish out items much more efficiently than any other hooks,
while also being much less attractive to lobstrosities. Some still fall
for it regardless, however.
spellcheck: Fixed the capitalization and punctuation in the description
of multiple fishing accessories.
code: Improved the code for fishing weights, to allow for different
hooks to have some more noticeable results on the weights without having
to add to an already massive proc.
/:cl:

---
## [Imaginos16/tgstation](https://github.com/Imaginos16/tgstation)@[7d04edb6e2...](https://github.com/Imaginos16/tgstation/commit/7d04edb6e2927330906a7af89664b7a5ab3aa48c)
#### Wednesday 2022-12-14 08:42:03 by Profakos

Mail sorting helper, and disposals fixes (#70861)

## About The Pull Request


![image](https://user-images.githubusercontent.com/2676196/198695007-53db1b70-845f-46a9-b98a-e146bb53951b.png)

This PR adds a mail sorting map helper, which during Late Initialization
will apply a sorting location index to the mail sorting disposals pipe
under them. I have replaced the varedits with all mail sorters with the
appropriate map helpers. I have thoroughly tested this, making sure
packages arrived to every location, where possible.

I have also fixed a few issues with the disposals network:

**Tramstation**

- One of the random maintenance segments had a place with no disposal
pipes. This has been fixed
- A sorter was looking for chapel and library packages, but it actually
meant to look for engineering packages
- There was no dormitory mail sorter, I have added one

**Metastation**

- There was no dormitory mail sorter, I have added one

**Icebox**

- There is no experimentor lab in icebox, but there is an
"experimentation" lab, which is good enough, so I have added it as a
location

**Deltastation**

- There was no dormitory mail sorter, I have added one
- Virology was not connected to the disposals network. However, on every
other map, it has a one way connection. I have hooked it up just like
that, so virology mail will arrive safely, and virology trash will go
into space as usual.

**Kilostation**

- Genetics packages were rerouted to the psychologist office

Unsolved issue on kilostation: there is no experimentor on this station,
and there is no space for a disposals in the circuits lab, so sadly, if
you send a package to this destination, it will come back to the mail
sorting office.

**Future improvements**

The TAGGERLOCATIONS list, which is used to retrieve the labels of the
various tags, is frankly unorganizable, and hard to expand. I have
delayed fixing this for a future PR.

I kinda wish to remove the sortType variable, as it is no longer
necessary to have it around with these helpers, but sadly, this would
ruin downstream maps, so I have no plans for this at the moment.

## Why It's Good For The Game

While mapping, having to constantly compare a comment in flavor_misc.dm
to figure out what to varedit a disposal mail sorter to is rather
annoying. These map helpers, similar to the access helpers, will help
with this issue.

Its also good if mail actually arrives.

## Changelog


:cl:
qol: added a mail sorting map helper, to allow mappers to create
disposal networks faster
fix: fixes several non working disposal mail targets that never received
their packages
/:cl:

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[ed63e8ec80...](https://github.com/Offroaders123/NBTify/commit/ed63e8ec80f20605497aa7cda349aa0fd516e75b)
#### Wednesday 2022-12-14 09:02:02 by Offroaders123

Source Maps + Side Effects

Did some looking into packaging, bundling, minifying, those sort of things. Gonna try out adding source maps, as it will look nice in DevTools for error positions, and it makes it nice to easily see the actual source for the code right in the browser too, with all of it's TypeScript goodness!

In addition to that exploration, found a super cool site called Bundlephobia, and it gives some super neat stats about NPM packages. After seeing how big some of the other libraries are, namely Prismarine NBT, having a bit extra in size for source maps shouldn't be too crazy. You get a nice developer experience out of it too!
https://bundlephobia.com/

One of their metrics mentioned whether the package is side-effect-free, which means if the package does anything to any code outside of it's own area. An example of that would be a polyfill or something, I think. Since bundlers don't know if there are side effects for a package or not, they assume there are, just to be safe and not break anything. After looking into it more, looks like there's a commonly-followed (not standard in terms of the `package.json`) property called `sideEffects`, and bundlers like Webpack will decide if it can perform tree-shaking on your code, if this property is set to `false`. Since NBTify doesn't have any side effects, I can set it to false too! Now it can enable tree-shaking for NBTify wherever someone may need it. I honestly haven't looked into bundlers yet, but I get the idea behind that, and it's definitely something I want to try working towards from the start! Modules are awesome!
https://sgom.es/posts/2020-06-15-everything-you-never-wanted-to-know-about-side-effects/

Looking into how nbt-ts implemented some of their bundling and packaging, I also noticed that they provide both an ESM and CJS export, which is neat. I kind of want to do that, but I also just want to go all in on ESM too. I don't want to prevent other people from using the library, but I think full-ESM is just too nice not to strive for. It works everywhere now, so I think it's good to try and work towards using it wherever you can! I wish it worked cross-browser in Service Workers, that's one of the last things I'm waiting for on that!

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[00d3780c38...](https://github.com/Huffie56/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Wednesday 2022-12-14 09:39:47 by carlarctg

PDT/L Buff (#1757)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

PDT/L kits now fold into cardboard.

Added many spare PDT/L kits and batteries to req. (Marines dropped them
off at req once they realized they were shitty milsurp knockoffs)

Made minibatteries tiny.

Added boldwarning span macro.

Improved locator tube sprites: Now has a pop-out battery slot at the top
that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.

Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Fixed a bug in which a string referenced a null var.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

When I saw the PDT/L kit, I was very interested. It seemed like a great
way to encourage teamwork and buddying up with some fun lore flavor on
the side. However, trying it out, it really feels bare-bones. I get it's
supposed to be 'crappy' because Boots magazine subscriber items suck and
so do the lives of every private on the corps, but the way that's
implemented really ruins the extremely cool concept that is being able
to locate your fellow buddies across the battlefield, so you don't need
to continually say HEY WHERE ARE YOU over comms in the many times you'll
get split up.

Thus I've heavily buffed them around the board, which you may think is
going way too far, and to an extent, you're _right._ It's intentional.
This is a really cool item that actively encourages teamwork and that's
why I would rather swing the buff hammer too hard than give it a paltry
buff and some qol that ultimately nobody cares about. It's the same as
the spotter kit. It's nuts, but needs teamwork to actually be useful.
And this should be encouraged.

If it is still deemed too strong, there are things we can do to
laterally nerf it without closing the PR outright. Making the tube not
work if the bracelet holder's dead, having it needs comms to work come
to mind, but there are surely others.

> Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

The intention here is to let marines actually resupply their kits once
they run dry, and if they're proactive, maybe grab some and bring them
to FOB with them. Despite the description, the cells cannot easily be
recharged as power cell chargers are different from rechargers, they are
effectively Bay12 legacy that is VERY hard to come across.

'What if someone carries like 5 of them in their bag? That'd completely
nullify the power drain part.'

The stinger here is 'in the bag'. There are not enough reasons to carry
bags and satchels in this game right now as the sheer amount of storage
for goods marines have make them a one-man-army with two primaries. If a
marine forgoes a shotgun that might save them from a 1-pounce capping
runner for 5 spare LT batteries, a default medkit, and two flare boxes,
they are well within their rights to do so.

> Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)

This lets req drop them off at FOB if they eventually figure out they
can drop unvended surplus there. If this somehow happens, marines who
never even glanced at the kit in loadout or prep will notice it exists
and maybe, just maybe, use them!

> Made minibatteries tiny.

You may think this contradicts my earlier point about sacrificing
storage value, but _actually_ think about it. All webbing types, armor
slots, pouches, belts, even the helmet, all share the common attribute
of not caring about item size. If it's small or medum it still takes 1
out of the 3 slots in medium armor. Any storage item that isn't a
satchel, effectively. Every spare battery taken directly in the average
marine's inventory is one slot less for 5 shotgun shells, one magazine,
one unga juice flask, binoculars. What this means in the end is simply
that marines may carry one to two spare batteries in their helmet (I
think) at the cost of Drip which few marines will trade for, and satchel
marines don't have to sacrifice a lot of space for the spare battery.
Plus, it makes sense, why wouldn't a small AA rechargeable battery be
tiny.

> Improved locator tube sprites: Now has a pop-out battery slot at the
top that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

This looks so sick!

> Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Adding sounds to items should be standarized, I think. There are so many
cool sounds in the sound/machines folder that go unused. Personally i
felt like these small stupid sounds added a LOT to the atmosphere of
this tiny locator tube and bracelet. Alien Isolation is known for its
sounds, we should strive to emulate that.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
add: Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.
qol: PDT/L kits now fold into cardboard.
add: Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)
balance: Made minibatteries tiny.
refactor: Added boldwarning span macro.
imageadd: Improved locator tube sprites: Now has a pop-out battery slot
at the top that shows up if emptied. The main green stripe is now a
battery indicator with appropiately-faded-out yellow warning and
blinking red danger sprites. The small notch at the bottom is now a
bracelet indicator that turns off without a battery and blinks red if
the bracelet was somehow destroyed.
qol: The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.
soundadd: Added a ton of sounds to interactions with the PDT/L kit.
Beeps on scanning, buzzes on errors, clicks on handling.
fix: Fixed a bug in which a string referenced a null var.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[ce39f048bf...](https://github.com/Huffie56/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Wednesday 2022-12-14 09:39:47 by carlarctg

Buffed, resprited, enhanced Oppressor. (#1732)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

**Resprited Oppressor! Pics here:**


![image](https://user-images.githubusercontent.com/53100513/204121775-9f4acd11-d818-46e8-81d3-c38bdfdabf5c.png)

Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Oppressor can hook over the M2C and M56D again.

Oppressor can hook over ledges. (UNIMPLEMENTED)

Tail stab's main ability usage is moved to a different proc for future
custom tail stabs.

Redesigned Tail Stab for Oppressor. Tail seize now utilizes a projectile
and beams to fire a 3-tile reaching tail hook, that pulls in AND DOES
NOT STUN marines. (It slows them for 0.5 seconds)

![Screenshot_20221127-032533~2](https://user-images.githubusercontent.com/53100513/204122365-e1ee57f7-1b9d-443e-a45c-dceec07a88d3.png)

Oppressor's abduct has had its effect strings changed to imply coiling
and uncoiling of the tail. Captured targets will now have a beam of the
Oppressor's tail attached to them (Purely visual) until they reach the
Praetorian, alongside an overlay of the vice grip on their legs.

Added a proc, .ammo/on_bullet_generation(), for the ammo datum to apply
effects to the generated bullet/projectile.

Added the bound_beam variable to projectiles. Could be used in the
future for things like harpoon guns, lasers, etc.

Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

Videos tomorrow.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Animated telegraphs looked really cool, but (I presume) were removed
because BYOND sometimes freezes or starts animations midway through when
short lived animated objects show up, for some reason. I effectively
made it so these are irrelevant by slapping on the border - The animated
effects are just a bonus and will not impact visibility, and in fact
enhance it.

> Oppressor can hook over the M2C and M56D again.

Everyone I've talked to agrees that there really is no reason for these
weapons to protect from abduction. The player can just.. move out of the
way, or even rest if they're in a crowded spot. It's also very
frustrating to see it get in the way of *other* abducts that bonk into
it. The player is going immobile in range of a xenomorph that punishes
immobility.

> Oppressor can hook over ledges. (UNIMPLEMENTED)

Couldn't replicate this issue for some reason... So uh. I dunno.

> Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)

Geeves approved.

This looks so fucking awesome. The slow is barely a thing, so I wouldn't
fret about slow creep. The reaching hook does no damage, only pulls
targets closer. This isn't necessarily super strong, but it's mega cool
and fits with Oppressor's theme of dislocation. I also changed the
windup from 1s to 0.5s so it can be utilized during combat, but this
could be reverted if it's too strong somehow.

> Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

This looked stinky on the tail seize.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Carlarc, Mikola Wei

imageadd: Resprited Oppressor, sprites made by Mikola Wei.
imageadd: Re-added animated telegraphs for Abduction. They've been
tweaked to always have the default border - that way, the weird way
byond handles short-lived animated objects doesn't make the telegraph
absurdly small. It can always be easily seen.
balance: Oppressor can hook over the M2C and M56D again.
refactor: Tail stab's main ability usage is moved to a different proc
for future custom tail stabs.
add: Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)
imageadd: Oppressor's abduct has had its effect strings changed to imply
coiling and uncoiling of the tail. Captured targets will now have a beam
of the Oppressor's tail attached to them (Purely visual) until they
reach the Praetorian, alongside an overlay of the vice grip on their
legs.
refactor: Added a proc, .ammo/on_bullet_generation(), for the ammo datum
to apply effects to the generated bullet/projectile.
refactor: Added the bound_beam variable to projectiles. Could be used in
the future for things like harpoon guns, lasers, etc.
fix: Fixed non-damaging projectiles causing a blood spurt. (It was
checking flags && FLAG instead of flag & flag, remember to use
CHECK_BITFIELD folks!)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

Co-authored-by: harryob <me@harryob.live>

---
## [allanlewis/djoser](https://github.com/allanlewis/djoser)@[4ebdc10add...](https://github.com/allanlewis/djoser/commit/4ebdc10add211cb238002fcc79a7cf8409d99825)
#### Wednesday 2022-12-14 10:04:29 by github

Fix for Friendly tips when Missing SOCIAL_AUTH_ALLOWED_REDIRECT_URIS

i forget add SOCIAL_AUTH_ALLOWED_REDIRECT_URIS to my config

it return 400 error, i don't know why ,  i pay more time find the issues

so  i add Friendly tips

-- sorry  , my english is not well

and thank you all

---
## [SciCrunch/sparc-curation](https://github.com/SciCrunch/sparc-curation)@[30441cbf29...](https://github.com/SciCrunch/sparc-curation/commit/30441cbf297fe9193b13f7c2a5ac3bbd5512999c)
#### Wednesday 2022-12-14 10:08:28 by Tom Gillespie

sparcur.simple.utils.fetch_paths_parallel switch to Async/deferred

You know that crazy stochastic file size mismatch error? We have it
cornered now. Nearly have the full root cause found as well, but not
quite, there are still some weird things going on.

For example, if I am using multiprocessing to retrieve different
files, then shouldn't nothing be shared and shouldn't it be impossible
for the url for one file to be returned from a requests session.get
that specified the other? I kind of want to check that the request url
matches across a single call to session.get because this is so insane.

In short, the reason why a mismatched file size occures is becuase a
call to BlacckfynnRemote.get_file_url -> utils.ApiWrapper.get_file_url
can seeminly at random return a url pointing to the wrong file!?! On
examination you will notice that that url returned points to THE WRONG
FILE, but also usually a file was also requested close in time to the
one that got the wrong url.

Looking over the logs again, it is clear to me now that the issue is
not that there is a race condition in any of the joblib code, because
it is not that we are somehow reading the results of session.get
twice.  The reason we know this is that rest of the long url with the
X-Amazon fields is different (eternal screaming).

Switching to Async/deferred avoids the issue, probably by going more
slowly, and by not sending a multiple requests during the same
microsecond, which if I had to bet would be why these things get
confused on the remote side.

I am going to test with this configuration to see whether we encounter
similar or other issues.

The issue was found when I noticed that the mismatched actual size of
a subjects.xlsx file was the exact size of the samples.xlsx file.
Which is the kind of utterly terrifying thing that you hope to never
see because it means that something has gone Mickensly wrong.

---
## [hfiref0x/UACME](https://github.com/hfiref0x/UACME)@[c65f9215c1...](https://github.com/hfiref0x/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Wednesday 2022-12-14 10:22:19 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [avar/git](https://github.com/avar/git)@[f1c903debd...](https://github.com/avar/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Wednesday 2022-12-14 12:04:29 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [mauriciozuardi/seedsigner](https://github.com/mauriciozuardi/seedsigner)@[d2a657f2d4...](https://github.com/mauriciozuardi/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Wednesday 2022-12-14 12:10:36 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [yuryzablotski/yuzaR-Blog](https://github.com/yuryzablotski/yuzaR-Blog)@[0e2122af7d...](https://github.com/yuryzablotski/yuzaR-Blog/commit/0e2122af7da4238743281d2d5102c2e703d3cb60)
#### Wednesday 2022-12-14 12:15:19 by yuryzablotski

new post fix: stupidely, I needed to add two last Rmd scripts to QR post, because for whatever reasen, it needed them in there ... starts to get annoying actually, that it does not just fucking work!

---
## [Dallinger/Dallinger](https://github.com/Dallinger/Dallinger)@[73e39d94a7...](https://github.com/Dallinger/Dallinger/commit/73e39d94a7ba96a17438f3c5b149a36408838d66)
#### Wednesday 2022-12-14 13:08:09 by Peter Harrison

Misc Docker quality of life improvements (#4616)

# Major

- Disabled the behavior where the built image name is written to config.txt. This behavior was inconsistent with the other Dallinger deployment patterns, because it meant that if you deployed once, changed code in experiment.py, then redeployed, then the experiment would launch in the former version unless you remembered to delete the image name from config.txt.
- Heroku deployments were failing because the default `heroku_python_version` had been discontinued by Heroku. We have experienced similar problems in the past and have always had to update Dallinger. Now we have changed the behaviour such that, if `heroku_python_version` is not specified in the experiment config, then it will use the default Python runtime currently in use by Heroku.

# Minor

- Propagate more information from deployment-related functions (e.g. dashboard credentials) so that they can be used by wrapper functions.
- Print more information (e.g. dashboard credentials) in deployment-related functions.
- Better debugging logs for docker-ssh deployments.
- Move deployment info logs from `deployment-info_{experiment_id}.txt` to `deploy_logs/*` to avoid clutter.
- Move default `dallinger_develop_directory` to `/tmp/dallinger_develop` because the original location was not writable by default on Docker.
- Minor bugfixes in docker-ssh deployment/export.
- Rename config variable `docker_ssh_volumes` -> `docker_volumes` because it's relevant also when we're doing docker locally. 
- Some minor renaming of internal variables for consistency.

---
## [HanceGalvez/app-dev](https://github.com/HanceGalvez/app-dev)@[806a3bf03f...](https://github.com/HanceGalvez/app-dev/commit/806a3bf03f4bbd76a8013a3edb1dd99858892400)
#### Wednesday 2022-12-14 13:30:33 by HanceGalvez

Update README.md

1. Click:
Michael Newman (Adam Sandler) seems to have it all but his wife, Donna (Kate Beckinsale), is increasingly frustrated by the amount of time he has to spend at work. Michael cannot find time to be at home until he meets an eccentric inventor (Christopher Walken) who gives him a universal remote that controls time. At first he happily skips the boring times until he realizes the remote is in control of his life and he learns to cherish all the precious moments with his family.

2. Avatar:
Avatar is an American media franchise created by James Cameron, which consists of a planned series of epic science fiction films produced by Lightstorm Entertainment and distributed by 20th Century Studios, as well as associated computer games and theme park rides.

3. Toy Story
Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.

4. Just Go With It
His heart recently broken, plastic surgeon Danny Maccabee (Adam Sandler) pretends to be married so he can enjoy future dates with no strings attached. His web of lies works, but when he meets Palmer (Brooklyn Decker) -- the gal of his dreams -- she resists involvement. Instead of coming clean, Danny enlists Katherine (Jennifer Aniston), his assistant, to pose as his soon-to-be-ex-wife. Instead of solving Danny's problems, the lies create more trouble.

5. Crazy, Stupid, Love
Cal Weaver (Steve Carell) is living the American dream. He has a good job, a beautiful house, great children and a beautiful wife, named Emily (Julianne Moore). Cal's seemingly perfect life unravels, however, when he learns that Emily has been unfaithful and wants a divorce. Over 40 and suddenly single, Cal is adrift in the fickle world of dating. Enter, Jacob Palmer (Ryan Gosling), a self-styled player who takes Cal under his wing and teaches him how to be a hit with the ladies.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[8aac90bcbb...](https://github.com/odoo-dev/odoo/commit/8aac90bcbbaf4152d9c43e3af2a6d47f38da1095)
#### Wednesday 2022-12-14 13:34:04 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104521

X-original-commit: 1636ba5ed2f8a284bef0930313a85cc3dc7cf072
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [sr229/garrysmod-chatsounds](https://github.com/sr229/garrysmod-chatsounds)@[6fe16b8cb4...](https://github.com/sr229/garrysmod-chatsounds/commit/6fe16b8cb459afbad868151c473986cc739346af)
#### Wednesday 2022-12-14 13:52:12 by Ayane

My name is Walter Hartwell White.

I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead, murdered by my brother-in-law Hank Schrader. Hank has been building a Virtual Youtuber empire for over a year now and using me as his recruiter. Shortly after my 50th birthday, Hank came to me with a rather, shocking proposition. He asked that I use my Live2D knowledge to recruit talents, which he would then hire using his connections in the Japanese utaite world. Connections that he made through his career with Niconico. I was... astounded, I... I always thought that Hank was a very moral man and I was... thrown, confused, but I was also particularly vulnerable at the time, something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me on a ride along, and showed me just how much money even a small indie channel could make. And I was weak. I didn't want my family to go into financial ruin so I agreed. Every day, I think back at that moment with regret. I quickly realized that I was in way over my head, and Hank had a partner, a man named Motoaki Yagoo Tanigo, a businessman. Hank essentially sold me into servitude to this man, and when I tried to quit, Yagoo threatened my family. I didn't know where to turn. Eventually, Hank and Yagoo had a falling out. From what I can gather, Hank was always pushing for a greater share of the business, to which Yagoo flatly refused to give him, and things escalated. Yagoo was able to arrange, uh I guess I guess you call it a hit on my brother-in-law, and failed, but Hank was seriously injured, and I wound up paying his medical bills which amounted to a little over 77,000. Upon recovery, Hank was bent on revenge, working with a man named Riku Tazumi , he plotted to kill Yagoo, and did so. In fact, the bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen in the ranks to become the head of the Cover Corp, and about that time, to keep me in line, he took my children from me. For 3 months he kept them. My wife, who up until that point, had no idea of my vtubing activities, was horrified to learn what I had done, why Hank had taken our children. We were scared. I was in Hell, I hated myself for what I had brought upon my family. Recently, I tried once again to quit, to end this nightmare, and in response, he gave me this. I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. I... All I could think to do was to make this video in hope that the world will finally see this man, for what he really is.

Signed-off-by: GitHub <noreply@github.com>

---
## [sunset-wasteland/sunset-wasteland](https://github.com/sunset-wasteland/sunset-wasteland)@[f7f7ae2cfc...](https://github.com/sunset-wasteland/sunset-wasteland/commit/f7f7ae2cfc1c91d2df5bfdbd7895e7ab2c6eb4d3)
#### Wednesday 2022-12-14 14:12:58 by Colovorat

Fixes cable merging, changes merging code just a little bit (#60997)

Makes stack code support merging two different stacks with the same mats, but different mats_per_unit numbers by implementing averages.

It's in an attempt to support the stupid efficiency shit that protolathes do. It's not great, but it ought to work alright for now. Kinda a bandaid
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [kyanch/NetHack](https://github.com/kyanch/NetHack)@[b2fe51490d...](https://github.com/kyanch/NetHack/commit/b2fe51490dac43cac70ec29c6958467b0fa9bdd4)
#### Wednesday 2022-12-14 14:48:14 by PatR

tty-style role selection for curses

Move the tty role/race/&c selection from wintty.c to role.c and remove
its references to BASE_WINDOW.  Have curses call the same routine now
so that the player has the option to choose role, race, gender, and
alignment in any order and to confirm or override random settings
prior to starting play.  Also if you went through "who are you?" then
final confirmation includes an extra menu choice to rename the hero.

It still has the quirk of sometimes remembering some of the previous
aspects when you re-pick a new value for some aspect which already
been selected.

The menus pop up on top of the copyright screen and that looks a bit
strange.  I don't think core code has any way to erase that base
window without erasing the entire screen so to fix the strangeness
the window ports would need to do that before calling the selection
routine.  I didn't do that because the very first prompt, "Shall I
pick ... for you? [ynaq]" shows up in that window rather than in a
popup over it, and having it be all by itself on an otherwise blank
screen seemed to be even stranger.

X11 and Qt both have more sophisticated selection routines so I
haven't tried to switch either of them to use this.  They both use a
fancy role-selection-specific menu with all the aspects present at
once so this wouldn't fit without more work than I care to tackle.

---
## [peff/git](https://github.com/peff/git)@[237b689b36...](https://github.com/peff/git/commit/237b689b366957f7236081dd80f76dae95ade57e)
#### Wednesday 2022-12-14 16:29:16 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [LukasNickel/aoc_2022](https://github.com/LukasNickel/aoc_2022)@[41ec0e37e3...](https://github.com/LukasNickel/aoc_2022/commit/41ec0e37e315239a867c3007ea2e01de3879e67e)
#### Wednesday 2022-12-14 16:46:34 by Lukas Nickel

Solution day 14

- Pretty awful, lots of magic numbers and some hacks for part 2

---
## [NASA-AMMOS/AIT-Core](https://github.com/NASA-AMMOS/AIT-Core)@[6c329174a5...](https://github.com/NASA-AMMOS/AIT-Core/commit/6c329174a598cf152e07b75670a3c87cc153b1c8)
#### Wednesday 2022-12-14 16:56:26 by Michael Joyce

Update tox with multiple python versions for testing

Update tox with test envs for Python 3.7 - 3.10. Skipped 3.11 due to
some issues getting the tests and the like to cooperate. Likely doable
with a bit of effort but didn't want perfect to be the enemy of good.

Semi-recent Poetry broke the way we were integrating with tox. The tests
have been updated in line with the recommendation on Poetry's website.
The development dependencies plugin we were using no longer works since
it relied on some private APIs that have since changed. It seems like
there isn't a great solution for this problem at the moment; Some of the
alternatives are also having trouble with the new version of Poetry.
Hopefully tox will support parsing pyproject.toml directly soon and do
away with all these hacks.

It is recommended that people run tox inside of `poetry shell` without
any other virtual environment open. I ran into a number of annoyances
with tox not being able to find the correct python versions and the like
when doing it other ways. The documentation has been updated to reflect
this. While I was in there I tried to make the development tools section
a bit clearer in general.

Minor updates throughout the repo are either from the linting checks
actually being run on the code or small fixes necessary to make the
linter happy. Shame on whomever has been skipping them :), and shame on
me for not fixing the broken CI yet.

The python version specified in pyproject.toml has been opened up to
support anything from Python 3.7 - 3.10. I've also unpinned gevent
(since it seemed necessary to get 3.9 to cooperate to do some oddities
with cffi on ARM). Dependencies have been relocked. Tox suite is all
passing for me currently. That includes tests running on all the
supported Python versions. We'll need more thorough testing here but
hopefully this is a step in the correct direction.

I've also included .python-version with a list of the python versions
I'm using in `pyenv`. Others should be able to use this to make sure
we'll all testing against the same versions. Not sure how correct it is
to include that but figured it wouldn't hurt for now.

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[68ba844196...](https://github.com/Huffie56/cmss13/commit/68ba84419624366956ae5f9bde67f1e33287301a)
#### Wednesday 2022-12-14 17:27:31 by RenaRenaRe

Cross-ciphering fix (#1879)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes the cross-ciphering property so it actually works instead of
producing a never ending stream of runtime errors and a broken larva
that never develops. I'm deliberately being vague about what it does
because I think it's supposed to be a secret, the wiki tells you to
"find out in game!", but you can just read the code since it isn't
complicated.
This is my first time using github so sorry if I've fucked something up.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Things should function the way they're supposed to.
Cross-ciphering is an extremely hard to get property that I'm not sure
if anyone has ever actually made in game, now on the incredibly rare
occasion that somebody actually makes it it should work correctly.
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
fix: Cross-ciphering now works correctly
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [NextWork123/n0kernel-nextkernel](https://github.com/NextWork123/n0kernel-nextkernel)@[bb1a0cb35e...](https://github.com/NextWork123/n0kernel-nextkernel/commit/bb1a0cb35e9a977888f3eb3bc183e79594bdac58)
#### Wednesday 2022-12-14 17:49:51 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [Programming-Person321/Hack-Club-Project](https://github.com/Programming-Person321/Hack-Club-Project)@[afbd500d87...](https://github.com/Programming-Person321/Hack-Club-Project/commit/afbd500d870d563840aa0bb8230de46af44706d9)
#### Wednesday 2022-12-14 18:25:30 by Ggacegi

Create Enlightenment

Pepsiman[a] is an action video game developed and published by KID for the PlayStation. It was released in Japan on March 4, 1999, and is based on the eponymous Japanese superhero mascot for the American carbonated soft drink Pepsi. It focuses the player on avoiding obstacles by running, dashing, and jumping, while Pepsiman automatically runs forward through each of the game's stages.

The game was made on a low budget, prompting the decision to make videos in-between stages that show a man drinking Pepsi, as they were cheap to produce. The game also features 3D cutscenes, for which the future visual novel writer Kotaro Uchikoshi created 3D models. While an American publisher did look into acquiring the rights to publish the game in the United States, it remained a Japan-exclusive game.

Reviewers frequently compared Pepsiman to other games, including Crash Bandicoot, and commented on its simplicity and its price, which was thought to be low. A writer for Complex included it on a list of company-branded games that "didn't suck", commenting that it is not a bad game as long as the player can tolerate the large amount of advertisement in it. According to Uchikoshi, the game did not sell well.

Contents
1	Gameplay
2	Background and development
3	Reception
4	Notes
5	References
6	External links
Gameplay[edit]

Gameplay of Pepsiman. Here, he is jumping on an intersection in an attempt to avoid a moving car.
Pepsiman is an action game[2] that consists of four stages, each divided into smaller segments,[3] and each involving the superhero Pepsiman saving a person who is dehydrated, such as a military man in the middle of a desert, by giving him a can of Pepsi.[4] The first three stages are based on real locations, San Francisco, New York City and Texas. The last one takes place in Pepsi City.[5] The game is played from a third-person perspective, with Pepsiman automatically running forward through the stages,[4] sometimes running through homes and other buildings.[3] The player takes control of Pepsiman himself, aiming to dodge obstacles, such as cars, construction cranes, and people,[4] as well as Pepsi-branded obstacles, including a Pepsi truck.[6] The player does this by using four different moves: running, dashing, jumping, and super-jumping.[3] The player gains points by collecting Pepsi cans.[6]

In some stages, Pepsiman's head becomes stuck inside a steel drum, which inverts the controls, and in some, he rides on a skateboard, which requires to player to avoid all obstacles. Throughout each stage is a number of checkpoints; if Pepsiman gets hit by obstacles too many times, the player is required to restart from the latest checkpoint. Each stage ends with Pepsiman being chased by an object,[4] such as a giant Pepsi can.[6] In between stages, the player is shown videos of an American man (played by Mike Butters) drinking Pepsi and eating chips and pizza as he watches Pepsiman.[4]

Background and development[edit]
Pepsiman is based on Pepsi's mascot of the same name, which was created for Pepsi's Japanese branch.[4] The character, whose fictional backstory says he used to be a scientist who transformed into a superhero after coming into contact with "Holy Pepsi",[7] was featured in Japanese Pepsi commercials[4] and in the Japanese version of the video game Fighting Vipers; he became popular in Japan,[8] spawning related characters such as Lemon Pepsiman and Pepsiwoman,[7] and Pepsi decided to promote the character with a video game.[4]

The game was developed by the Japanese video game developer KID. It was made on a low budget, which led to the decision to make the low-cost video scenes of actor Mike Butters drinking Pepsi.[9][10] The game also uses 3D event scenes, which were modeled by Kotaro Uchikoshi, who would later be a scenario writer for visual novels at KID. This was Uchikoshi's first job; he had been hired to plan video game adaptations of board games, but ended up being part of the development of Pepsiman instead, which was already in progress when he joined KID in 1998.[9] The game was released in Japan by KID for the PlayStation on March 4, 1999;[2] while an American publisher was looking into acquiring the rights to publish the game in the United States,[8] it remained Japan-exclusive. Despite this, the game is entirely in English, not Japanese (although with Japanese subtitles for dialogue).[4] According to Uchikoshi, the game did not sell well.[9]

In 2019, the game was featured in an episode of James Rolfe's comedy web series Angry Video Game Nerd, in which Butters reprised his role from the game's cutscenes.[11] The soundtrack for the game received a vinyl release in 2020 by the European label Chipped Records.[12]

Reception[edit]
Reception
Review scores
Publication	Score
Famitsu	25/40[2]
GameFan	90/100[13]
Joypad	2/10[14]
Gamers' Republic	B−[15]
Planet Playstation	88/100[16]
Writers for Famitsu called the game "super-simple", comparing it to Metro-Cross and Paperboy, and calling it a simplified version of Crash Bandicoot.[2] Others have made similar comments. A reviewer for IGN also compared it to Crash Bandicoot, described the gameplay as "simplistic [and] route memorization-based", and said that the thing the game would be remembered for was its "extremely bizarre premise". They still felt that the game was not bad, and that it was worth the price, which they noted was low.[3] James Mielke at GameSpot called the game a "nifty little distraction", and said that the gameplay was similar to the "old-school gaming dynamics of yesteryear". He commented on the low price, but said that it was difficult to find imports of it.[8] Gamers' Republic magazine rated the game a B−.[15] Gamers' Republic later listed the game in their 1999 Video Game Buyers Guide and Y2K Preview as one of the best games to import from Japan that year.[17]

In 2011, Allistair Pinsof at Destructoid reviewed the game, calling it a mix between Paperboy and Muscle March in terms of the complexity and pace, and compared the gameplay to Crash Bandicoot. He found it to be "such a gloriously twisted, charming spectacle" that it would be difficult not to like it; he said that the main reason to play the game is "the sheer lunacy" of it, saying that the game is "obsessed" with America, and portrays Americans as "unhygienic hillbillies" in a manner that makes it unclear if it is a self-aware parody or not. He concluded that the game is funny, but not great, and that the ridiculous premise and its large amount of small details make the game "charmingly brain-dead".[4] In 2013, Justin Amirkhani at Complex included the game in a list of company-branded video games that "didn't suck", saying that while the game's graphics had not aged well, it was mechanically very similar to Temple Run, which Amirkhani called his favorite iOS game. He concluded that Pepsiman is not a bad game for people with quick reflexes, as long as they can stand the high amount of advertising within the game; he claimed that Pepsiman was the advergame with the largest amount of "logos-per-second".[6]

In 2015, Retro Gamer magazine listed it as number 18 on their list of "The 20 Greatest PlayStation Games You've Never Played".[18

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[ebc0227176...](https://github.com/Jacquerel/orbstation/commit/ebc0227176b5213f379eefc3f5c6aa7be2d09c0a)
#### Wednesday 2022-12-14 18:34:36 by Tastyfish

Makes dog a basic mob [MDB IGNORE] (#70799)


About The Pull Request

    Made a basic version of the pet base called /mob/living/basic/pet. It's significantly more stripped down from the old simple_animal one, because its half collar stuff and...

    Made the collar slot a component that you could theoretically remove from a pet to disable the behavior, or add to any other living mob as long as you set up the icon states for the collar (or not, the visuals are optional).
        The corgi's collar strippable slot is now generally the pet collar slot, and in theory could be used for other pet stripping screens.

    I also gutted the extra access card code from /mob/living/basic/pet as it's only being used by corgis. Having a physical ID is now just inherent to corgis, as they're the only ones that could equip it anyway.

    Ported the make_babies() function from simple_animals to a new subtree and associated behavior, called /datum/ai_planning_subtree/make_babies that uses blackboards to know the animal-specific info.
        Note that it's marginally improved, as the female walks to the male first instead of bluespace reproduction.

    Tweaked and improved the dog AI to work as a basic mob, including making /datum/idle_behavior/idle_dog fully functional.

    Made a /datum/ai_planning_subtree/random_speech/dog that pulls the dynamic speech and emotes to support dog fashion.

I've tested base collars across multiple pet types.

For dogs, I've tested general behavior, fetching, reproduction, dog fashion, and deadchat_plays, covering all the oddities I'm aware of.

image
Why It's Good For The Game

Very big mob converted to a basic mob.
Changelog

cl
fix: Lisa no longer uses bluespace when interacting with Ian.
refactor: A large portion of dog code was re-written; please report any strange bugs.
/cl

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[a30fb1438a...](https://github.com/cockroachdb/cockroach/commit/a30fb1438a6f1f99ebf2a27695e89d4b4e51cf8f)
#### Wednesday 2022-12-14 20:03:20 by craig[bot]

Merge #93153 #93325 #93354 #93545 #93557 #93563 #93618

93153: rttanalysis: don't count leasing the database desc r=andreimatei a=andreimatei

A bunch of rtt-analysis tests were counting a request for leasing the database descriptor. This is not interesting. This patch makes the test framework lease it first through a "USE" statement.

The number of KV requests required for leasing is currently mis-counted. We count 1, but in reality it's 4. A different patch will correct the miscounting that, at which point that would be too significant for the tests.

Release note: None
Epic: None

93325: multitenant: retain range splits after TRUNCATE for secondary tenants r=knz a=ecwall

Fixes #69499
Fixes #82944

Existing split points are preserved after a TRUNCATE statement is executed by a secondary tenant.

Release note: None

93354: tracing: disallow children of sterile span with different Tracer r=andreimatei a=andreimatei

Before this patch, creating a "child" of a sterile span with a different Tracer than the one used to create the sterile span was tolerated - on the argument that sterile spans don't actually get children (the would-be child span is created as a root), so the arguments for not allowing a children to be created with different tracers don't apply. At the same time, creating a child of a noop span with a different Tracer than the noop span's Tracer was documented to not be allowed. In practice, it was, because the code was confused [1].

This patch disallows creating children of sterile spans with a different tracer, for consistency with all the other spans. The patch also makes it a panic for the children of noop spans to be created with a different Tracer.

This is all meant as a cleanup / code simplification.

[1] WithParent(sp) meant to treat sterile spans differently than noop spans but it was using sp.IsSterile(), which returns true for both. As such, it was unintentionally returning an empty parent option. startSpanGeneric() meant to check the tracer of parent noop spans, but it was failing to actually do so because it was going through the opts.Parent.empty().

Release note: None
Epic: None

93545: sql: make SHOW RANGES FOR TABLE include all indexes r=ajwerner a=knz

Informs #80906.
Fixes #93546.
Fixes #82995.

Release note (backward-incompatible change): `SHOW RANGES FOR TABLE`
now includes rows for all indexes that support the table. Prior to
this change, `SHOW RANGES FOR TABLE foo` was an alias for `SHOW RANGES
FOR INDEX foo@primary`. This was causing confusion, as it would miss
data for secondary indexes. It is still possible to filter to just the
primary index using `SHOW RANGES FOR INDEX foo@primary`.

The statement output now also includes the index name.

93557: syntheticprivilegecache: scan all privileges at startup  r=ajwerner a=ajwerner

#### syntheticprivilegecache: move caching logic out of sql
This is a pure refactor to move the logic for caching synthetic privileges
from the sql package. This will make it easier to add features later.

#### syntheticprivilegecache: scan all privileges at startup 


Fixes https://github.com/cockroachdb/cockroach/issues/93182

This commit attempts to alleviate the pain caused by synthetic virtual table
privileges introduced in 22.2. We need to fetch privileges for virtual tables
to determine whether the user has access. This is done lazily. However, when a
user attempts to read a virtual table like pg_class or run SHOW TABLES it will
force the privileges to be determined for each virtual table (of which there
are 290 at the time of writing). This sequential process can be somewhat slow
in a single region cluster and will be very slow in an MR cluster.

This patch attempts to somewhat alleviate this pain by scanning the table
eagerly during server startup.

Release note (performance improvement): In 22.2 we introduced privileges on
virtual tables (system catalogs like pg_catalog, information_schema, and
crdb_internal). A problem with this new feature is that we now must fetch those
privileges into a cache before we can use those tables or determine their
visibility in other system catalogs. This process used to occur on-demand, when
the privilege was needed. Now we'll fetch these privileges eagerly during
startup to mitigate the latency when accessing pg_catalog right after the
server boots up.

93563: pgwire: handle decoding Geometry/Geography in binary r=rafiss a=otan

Resolves #81066
Resolves #93352

Release note (bug fix): Previously, CockroachDB would error when receiving Geometry/Geography using binary parameters. This is now resolved.

93618: cli,cliccl: move some mt commands to cliccl r=ajwerner a=ajwerner

Part of #91714

Epic: none

Release note: None

Co-authored-by: Andrei Matei <andreimatei1@gmail.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>
Co-authored-by: Andrew Werner <awerner32@gmail.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>

---
## [AntonLTG/bolibompacs](https://github.com/AntonLTG/bolibompacs)@[9b783ac124...](https://github.com/AntonLTG/bolibompacs/commit/9b783ac124e0fd81c06c7931e0ac6a62a17018b3)
#### Wednesday 2022-12-14 20:13:18 by JesusHolyBalls

!important; Yeeeah jump function and advanced movement, gravity is screwed for character

.grounded is bs, need so much information and the troubleshooting is insanly annoying.

1. need to have the character dimmensions, to use raycasts.(raycats gives a true or false value after detecting if an object is a certain distance from a certain point.) Done

2.right now falling at constant speed which needs to be fixed, it is possible to kinda bhop tho. NOT DONE

3.To fix speed we need to calculate theoretical max speed and replace current speed with "max speed" Done

4. Apperantly fbx files is packed so needed to unpack to make the eyes and ears move with the head and then repack it. Done

5.At this time we cant walk upwards on smal height differences, just end up launching the character upwards (the more speed the higher). NEED HOTFIX

6. To import scripts and characters is a hell, you need to rebind all scripts to (in our case) the different body parts to make them move, I should've named the bone structure parts better for easier navigation and easier distrubution, will be hard for others collaborators to understand.

took about 5 hours to rewrite the movement script and add a working jump function with a "check if grounded"

total programming time is about 8hours now and another 20 hours 3D moddeling (includes getting familiar with the programs).

---
## [cursorweb/JavaAOC](https://github.com/cursorweb/JavaAOC)@[daf9f95558...](https://github.com/cursorweb/JavaAOC/commit/daf9f955583ed785f586f73d193aa65531ebb72a)
#### Wednesday 2022-12-14 20:20:05 by Junhao "Jerry" Zhang

part 1

oh my god i'm literally pissing myself right now oh my god oh my god oh my god did i seriously just do this in java what the heck java sucks

---
## [Gamer025/tgstation](https://github.com/Gamer025/tgstation)@[03bc97ade5...](https://github.com/Gamer025/tgstation/commit/03bc97ade5a76f156229b946e38816ced97a0e30)
#### Wednesday 2022-12-14 20:40:25 by necromanceranne

Nukies Update 6: Interdyne is here for you! Medical Supplies and Atropine! (#71067)

## About The Pull Request

Quite a few changes overall to the nuclear operatives tactical medkit.
The kit is more of a full suite of equipment for performing field
medical duties as a nukie.

- I've split the medkits between two kinds. Basic and premium. Medical
bundle has the premium kit.
- Basic contains additional amounts of basic c2 chem patches, some spare
atropine autoinjectors, sutures and regen mesh, and some basic medical
equipment for tending wounds. 4 TC (as it was before). That's it.
- The premium kit is a far more useful full suite of advanced medical
equipment, MODsuit modules, medical supplies and cybernetic implants,
including the combat hypospray and the combat defib. 15 TC.

**In the premium kit, there is:**
- It has a box of beakers with powerful healing chems. Omnizine,
salicylic acid, oxandrolone, pentetic acid, atropine, salbutamol and
rezadone.
- The combat injector is empty, so you can load it as necessary.
- There are advanced sutures and regenerative mesh packs. They don't
work through spacesuits, but are invaluable for wound repair. Especially
burns.
- There is a surgery arm toolset so you can do field operations without
lugging tools.
- There is a surgery processor module that comes preloaded with advanced
surgeries, a threadripper module, and the combat defib module. The
module works entirely like a combat defib, but you don't need to lose
your belt slot to use it.
- The surgeries are revival, the upgrade surgeries (like vein
threading), brainwashing (did you know they didn't get access to
brainwashing, I think this is a shame) and the better tend wounds
option.
- The nightvision medical hud doubles as a pair of science goggles.

**Atropine changes:**
- Atropine now stops bomb implants from autoexploding. This does **NOT**
stop you from manually detonating the bomb. (This is possible even when
you're dead and haven't left your body)
- As a result, nukies get atropine medipens so that they can potentially
stop themselves detonating prematurely, or stop their allies detonating
prematurely. They have a little pamphlet to help explain how their
microbomb works.

## Why It's Good For The Game

Straight up: The medkit is ass.

The meds in the injector sucks, just getting c2 meds in patches is kind
of insulting for something granted to you from an uplink item (and also
you get those for free with your ~~xbox~~ infiltrator medical room so
lol), and operatives just got the kit for one reason and one reason
only. That combat defib as a _weapon_.

Fuck that. So the kits now much better as a way to both support yourself
AND your team through providing a range of improvements you can provide
the squad, while also not undermining the reason why people may have
wanted the kit (that defib). I would really like to see more nukies
attempt to support one another in combat, and a medic operative is a
role that needs love to make that a reality.

**Edit here**: I reintroduced a low end kit with more c2 medical
supplies _if you want them_. I can see how someone might pinch all of
the medical supplies like a cunt, so maybe we should have a failsafe for
that.

A huge culprit of the lack of value of support meds was usually that
ops...explode when they die. If a medic can pop atropine into an op
before they die, they might be able to save them, or an op could pop
themselves with atropine prematurely to maybe stave off death.

## Changelog
:cl:
balance: Splits the nuclear operative combat medical kit into two
versions: basic and premium.
balance: Basic contains additional amounts of basic c2 chem patches,
some spare atropine autoinjectors, sutures and regen mesh, and some
basic medical equipment for tending wounds. 4 TC (as it was before).
balance: The premium kit is a far more useful full suite of advanced
medical equipment, MODsuit modules, medical supplies and cybernetic
implants, including the combat hypospray and the combat defib. 15 TC.
balance: Atropine stops bomb implants from automatically detonating on
death. You can still manually activate your bomb implant (even when you
are dead).
balance: Operatives start with an atropine pen to stop themselves and
their allies from detonating so they can hopefully be saved by a medical
operative.
add: There is a pamphlet to explain this in the nuclear operative's
survival box.
add: I'm not telling you to read the pamphlet, but you should probably
read the pamphlet.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[af9d63ce15...](https://github.com/treckstar/yolo-octo-hipster/commit/af9d63ce15cff654a1210fa8f94008bc24dcdd94)
#### Wednesday 2022-12-14 21:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [JohnH-Github/YouTooltip](https://github.com/JohnH-Github/YouTooltip)@[34ed711d55...](https://github.com/JohnH-Github/YouTooltip/commit/34ed711d559926b84901407cf3f7c90ac109ca76)
#### Wednesday 2022-12-14 22:10:22 by John H

Fix newly added links sometimes skipped.

Holy mother of God this was frustrating to figure out. For some odd reason, the top of the MutationObserver callback (above the changes.forEach() loop) is executed on EVERY change, which caused newValidLinksBucket to reset. The fix is simple, but the hours lost was not.

---
## [wojsmol/hestiacp](https://github.com/wojsmol/hestiacp)@[365dab5670...](https://github.com/wojsmol/hestiacp/commit/365dab5670f6d1a862858be01638072eeb2ec1db)
#### Wednesday 2022-12-14 22:10:50 by divinity76

Use secure RNG to generate passwords (#2726)

* use secure rng to generate passwords

quoting MDN:
>Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead

My rng is kinda shitty, i know there is some fast way to cut down higher digits to get a digit in range without introducing bias, but i also know that other people have introduced bias by trying to do that on an initially secure rng and getting it wrong (iirc it's discussed here? https://www.youtube.com/watch?v=LDPMpc-ENqY - been years since i saw the talk, but i know Lavavej discussed it in one of his presentations, i think it was that one)  , but anyway this is fast enough, and secure.

* shorter name

* randomString2 / centralize js string generation

* missed 2

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[7f1e80ca3d...](https://github.com/cmss13-devs/cmss13/commit/7f1e80ca3dd4800f54b5ff4dc3663dd1f804c28c)
#### Wednesday 2022-12-14 23:32:26 by carlarctg

MIDIs are now either 'Meme' or 'Atmospheric', players can toggle each option (#1939)

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

Updated savefile number from 19 to 20. Meme and atmospheric preferences
are enabled by default.

Admin sounds now need a selection between 'Meme' or 'Atmospheric' type.
Ideally, this would let players decide if they want to listen to hijack
or first drop songs without needing to listen to GOOD HITS or whatnot.

I am uncertain about the savefile bit of code. I don't fully understand
it.

As stated I don't care about GBP, so if the tags are teechnicallly
incorrect go ahead and change them or whatever.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.

As it says. Lots of people hate the memes and just want to listen to the
cool atmosphere. This is of course dependant on staff selecting the
right option, which is sometimes up to opinion, but I fully trust staff
will be able to handle this subjective affair correctly.

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
refactor: Updated savefile number from 18 to 19. Meme and atmospheric
preferences are enabled by default.
admin: Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [Jolly-66/Skyrat-tg](https://github.com/Jolly-66/Skyrat-tg)@[81ca11b95a...](https://github.com/Jolly-66/Skyrat-tg/commit/81ca11b95a59d5cf0eb0a066454b2903f4859503)
#### Wednesday 2022-12-14 23:41:38 by SkyratBot

[MIRROR] Basic Mob Carp: Retaliate Element [MDB IGNORE] (#18030)

* Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

* Basic Mob Carp: Retaliate Element

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: tastyfish <crazychris32@gmail.com>

---

