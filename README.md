## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-03](docs/good-messages/2023/2023-11-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,326,035 were push events containing 3,517,364 commit messages that amount to 269,215,005 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 71 messages:


## [Nobelium-XVIII/Skyrat-tg](https://github.com/Nobelium-XVIII/Skyrat-tg)@[1a2ddececa...](https://github.com/Nobelium-XVIII/Skyrat-tg/commit/1a2ddececa5cbc3b3aed161765eab4ebdda105c7)
#### Friday 2023-11-03 00:40:32 by SkyratBot

[MIRROR] new space ruin, the biological research outpost [MDB IGNORE] (#24662)

* new space ruin, the biological research outpost (#79149)

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

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* new space ruin, the biological research outpost

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[c034314f1b...](https://github.com/jjpark-kb/Skyrat-tg/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Friday 2023-11-03 00:42:22 by SkyratBot

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
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[0e3b7d842b...](https://github.com/jjpark-kb/Skyrat-tg/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Friday 2023-11-03 00:42:22 by SkyratBot

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[68cd638330...](https://github.com/tgstation/tgstation/commit/68cd6383306e3f37d36cdc82113ada320b6e6365)
#### Friday 2023-11-03 00:43:40 by Donglesplonge

swaps one of the fridges in snowcabin to be in line with the rest  (#79414)

## About The Pull Request

In truth, this is an IDED PR (this is not at all sarcasm, and as we all
know nobody would lie on the internet) that came about from a round i
just got done playing wherein i was in snowcabin trying to cook up some
food for fun, well wouldn't you know it i couldn't open one of the
fridges, what gives? well i got to thinkin it has to do with the fridge
type used, for some reason the fridge that holds the universal enzyme
uses the freezer/fridge/kitchen type instead of the fridge/open type
that the other two do, so i went ahead and just changed it off to the
other fridge types so now anyone can open it.

## Why It's Good For The Game

its a bit stupid to have a single fridge thats different from the rest
for no discernable reason, i can't think of any reason universal enzyme
would need to be guarded ever, you could just say "well why not go back
onto the station and grab some if the fridge is locked", well if for
some reason i'm barred from the station i want to be able to use as many
tools within my reach as possible preferably without many hoops, and
this ones unnecessary.

## Changelog

fix: changes the type of fridge used to hold the universal enzyme in the
snowcabin gateway's kitchen, letting everyone access it like the rest of
the fridges.

/:cl:

---
## [Nobelium-XVIII/tgstation](https://github.com/Nobelium-XVIII/tgstation)@[9e18c6575a...](https://github.com/Nobelium-XVIII/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Friday 2023-11-03 00:47:12 by lizardqueenlexi

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
## [Nobelium-XVIII/effigy-se](https://github.com/Nobelium-XVIII/effigy-se)@[a910baf8c4...](https://github.com/Nobelium-XVIII/effigy-se/commit/a910baf8c4317f5af28f77f178e0fa81806f3cf0)
#### Friday 2023-11-03 00:47:50 by Paxilmaniac

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
## [Nobelium-XVIII/effigy-se](https://github.com/Nobelium-XVIII/effigy-se)@[365d9b98bc...](https://github.com/Nobelium-XVIII/effigy-se/commit/365d9b98bc18f6ceedbe45ec74bbf33b5ce12501)
#### Friday 2023-11-03 00:47:50 by GoldenAlpharex

Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay (#79275)

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

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[0b8864b9ed...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/0b8864b9edae944029213246aaa36acf8f17e9c4)
#### Friday 2023-11-03 00:48:08 by The Bron Jame Offical

More Joke Ego (#1582)

⎓⚍ᓵꖌ FUCK||𝙹⚍YOU, CURSE OF VIOLET NOON

more joke EGO

fucked around with fluid sack code for this one

Added ᓵ⚍∷ᓭᒷ 𝙹⎓ ⍊╎𝙹ꖎᒷℸ ̣  リ𝙹𝙹リ

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[157fafeaa9...](https://github.com/Hatterhat/tgstation/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Friday 2023-11-03 01:06:24 by lizardqueenlexi

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
## [Iota-School/notebooks-for-all](https://github.com/Iota-School/notebooks-for-all)@[e24fa4e579...](https://github.com/Iota-School/notebooks-for-all/commit/e24fa4e579a82855650b5bcae2228da367d0aad3)
#### Friday 2023-11-03 01:27:41 by tonyfast

remove some stupid fucking auto import shit. what the fuck. i have no need for polars. sometimes completion is a foot gun

---
## [Norwalk-RoboWarriors-14568/CENTERSTAGE](https://github.com/Norwalk-RoboWarriors-14568/CENTERSTAGE)@[22c5185e88...](https://github.com/Norwalk-RoboWarriors-14568/CENTERSTAGE/commit/22c5185e88f1d42b1aab7a4abe8bd5ac1d7dea2a)
#### Friday 2023-11-03 01:48:41 by NRobowarriors

God himself has tken my hand his higher essence as guided my arms to create what has been demanded

“What’s reality? I don’t know. When my bird was looking at my computer monitor I thought, ‘That bird has no idea what he’s looking at.’ And yet what does the bird do? Does he panic? No, he can’t really panic, he just does the best he can. Is he able to live in a world where he’s so ignorant? Well, he doesn’t really have a choice. The bird is okay even though he doesn’t understand the world. You’re that bird looking at the monitor, and you’re thinking to yourself, ‘I can figure this out.’ Maybe you have some bird ideas. Maybe that’s the best you can do.”

The Holy Spirit can puppet you,"
"I started seeing people following me around in suits and stuff. It just seemed something was strange,
n the Bible it says if you seek God, He will be found of you," Davis says now. "I was really seeking, and I was looking everywhere to see what he might be saying to me."

---
## [SamuelRowe/tgstation](https://github.com/SamuelRowe/tgstation)@[e39a43e2a4...](https://github.com/SamuelRowe/tgstation/commit/e39a43e2a418f19fde52e05281bfdae063f4a6c1)
#### Friday 2023-11-03 01:59:53 by Toastgoats

[No GBP] Fixes the secret bottomless pit in the ethereal pirate shuttle (#78138)

## About The Pull Request

I DIDNT NOTICE THAT ALL THE DIRT IN THE ETHEREAL SHUTTLE HAD CHASM
BASETURFS FUCK FUCK FUCK


![image](https://github.com/tgstation/tgstation/assets/63932673/ba5f7b02-7577-48ad-b2bc-b8b1c0e4192f)

(Also rebalances the ship a bit by adding some more turrets and cleans
up the wonky turf decals and engines)
## Why It's Good For The Game

God's strongest mapper needs to get some sleep asap I'm so fucking tired

A few people also pointed out that only having two turrets was extremely
punishing even for the playstyle I was trying to encourage, so it makes
sense to add a little wiggle room.
## Changelog
:cl:
balance: Gave the bluespace geode pirates 4 more teleporter bolt
turrets.
fix: The bluespace geode pirates no longer have a bluespace portal to
the bottomless pit dimension.
add: Station-safe dirt tiles for all your mapping needs, but surely no
station maps use the chasm baseturf ones, right? Right?
/:cl:

---
## [Sophie-Gresh/hello-world](https://github.com/Sophie-Gresh/hello-world)@[162f7e275f...](https://github.com/Sophie-Gresh/hello-world/commit/162f7e275f72a9f86fd2817ff382700f5837be61)
#### Friday 2023-11-03 02:00:56 by Sophie-Gresh

Update README.md

Tried to make my students laugh with a terrible dad joke that wasn't funny.

---
## [dacook/openfoodnetwork](https://github.com/dacook/openfoodnetwork)@[8a88734d89...](https://github.com/dacook/openfoodnetwork/commit/8a88734d8911bb1fe5c88d54baba431f1e1d01e4)
#### Friday 2023-11-03 02:26:47 by David Cook

Disable form elements in a disabled-section

I chose to use the 'elements' collection rather than choosing which elements to include (ie this supports inputs, textareas, buttons and anything else I didn't think of). It could be a bit simpler if we assume the element is a form. Even simpler if it's a fieldset (that has a disabled property). But I didn't want to limit it too much.

Unfortunately JS is quite ugly compared to Ruby. And 'prettier' made it uglier in my opinion.

---
## [yuwata/systemd](https://github.com/yuwata/systemd)@[1761066b13...](https://github.com/yuwata/systemd/commit/1761066b135f1a322c446f102343ea4aa61fe3ee)
#### Friday 2023-11-03 02:27:27 by Lennart Poettering

storagetm: add new systemd-storagetm component

This implements a "storage target mode", similar to what MacOS provides
since a long time as "Target Disk Mode":

        https://en.wikipedia.org/wiki/Target_Disk_Mode

This implementation is relatively simple:

1. a new generic target "storage-target-mode.target" is added, which
   when booted into defines the target mode.

2. a small tool and service "systemd-storagetm.service" is added which
   exposes a specific device or all devices as NVMe-TCP devices over the
   network.  NVMe-TCP appears to be hot shit right now how to expose
   block devices over the network. And it's really simple to set up via
   configs, hence our code is relatively short and neat.

The idea is that systemd-storagetm.target can be extended sooner or
later, for example to expose block devices also as USB mass storage
devices and similar, in case the system has "dual mode" USB controller
that can also work as device, not just as host. (And people could also
plug in sharing as NBD, iSCSI, whatever they want.)

How to use this? Boot into your system with a kernel cmdline of
"rd.systemd.unit=storage-target-mode.target ip=link-local", and you'll see on
screen the precise "nvme connect" command line to make the relevant
block devices available locally on some other machine. This all requires
that the target mode stuff is included in the initrd of course. And the
system will the stay in the initrd forever.

Why bother? Primarily three use-cases:

1. Debug a broken system: with very few dependencies during boot get
   access to the raw block device of a broken machine.

2. Migrate from system to another system, by dd'ing the old to the new
   directly.

3. Installing an OS remotely on some device (for example via Thunderbolt
   networking)

(And there might be more, for example the ability to boot from a
laptop's disk on another system)

Limitations:

1. There's no authentication/encryption. Hence: use this on local links
   only.

2. NVMe target mode on Linux supports r/w operation only. Ideally, we'd
   have a read-only mode, for security reasons, and default to it.

Future love:

1. We should have another mode, where we simply expose the homed LUKS
   home dirs like that.

2. Some lightweight hookup with plymouth, to display a (shortened)
   version of the info we write to the console.

To test all this, just run:

    mkosi --kernel-command-line-extra="rd.systemd.unit=storage-target-mode.target" qemu

---
## [AlexMarrinan/RavenGuard](https://github.com/AlexMarrinan/RavenGuard)@[c45a9c48dd...](https://github.com/AlexMarrinan/RavenGuard/commit/c45a9c48dda83a17e81b3065b70d9f56f4d14ecc)
#### Friday 2023-11-03 02:35:57 by Woodemen

MagicKnightAttack

I hope this is correct. It took me like 3 hours trying to remember/figure out how to set up this animation correctly so if its wrong or broken for some reason let me know what is is because WOW I am out of my depth lol. Also out of pure fear I checked that this was uploaded to the CORRECT BRANCH as to not decimate the fuckin files.

---
## [UBCFormulaElectric/Consolidated-Firmware](https://github.com/UBCFormulaElectric/Consolidated-Firmware)@[48ee00ec77...](https://github.com/UBCFormulaElectric/Consolidated-Firmware/commit/48ee00ec772e45a997365bdf7dadaecc117a31e9)
#### Friday 2023-11-03 03:00:09 by Gus Tahara-Edmonds

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
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[d5d78fec30...](https://github.com/ReturnToZender/ReturnsBubber/commit/d5d78fec30aef1480c47a581eafc6a1b9edc8b13)
#### Friday 2023-11-03 03:01:25 by SkyratBot

[MIRROR] Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN [MDB IGNORE] (#24149)

* Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN (#78674)

## About The Pull Request

The Regal Condor come with a magazine and ammo already inside.

The recipe for the magazine now no longer needs TC, but does need donk
pockets (sponsored murder gear, you see) and a hell of a lot more
materials per magazine (you're looking at like 40 sheets of various
materials all up). It also needs you to make the Condor first. But it
comes preloaded with ammo.

The Condor is 1 whole TC more expensive. Also needs some metal. The old
recipe is there in spirit.

The Regal Condor and the magazines come with 10mm Reaper bullets.
They're high damage. They're high AP. They are also hitscan.

## Why It's Good For The Game

Apparently people don't like the Condor. Too much effort for not enough
reward. After all, revolvers exist. 'It must be a joke' they say! 'It's
joke content! I went to all that effort to make it for nothing! That
slut Anne tricked us!'

**Wrong, bitch.**

If you want the Condor to make you shit yourself the moment someone with
it appears on the screen, then fine!

### **You get what you fucking deserve.**

## Changelog
:cl:
balance: Despite earlier reports suggesting that the famous lethality of
the Regal Condor was largely a myth, there has been rumors that the gun
has once again started to display its true killing potential on any
station that it 'manifests'.
/:cl:

* Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [git/git](https://github.com/git/git)@[8f23432b38...](https://github.com/git/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Friday 2023-11-03 04:24:47 by Johannes Schindelin

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
## [amarevite/docker-caddy-porkbun-cachehandler](https://github.com/amarevite/docker-caddy-porkbun-cachehandler)@[9899681856...](https://github.com/amarevite/docker-caddy-porkbun-cachehandler/commit/989968185611d16c880f8cf00c63f41a7f3118e0)
#### Friday 2023-11-03 04:32:41 by amarevite

okay i think this fixes check-update.yml

god damnit the update script got renamed but this file never got updated with the new name this should fix the action now fingers fucking crossed

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[d1ad9b6658...](https://github.com/jlsnow301/tgstation/commit/d1ad9b665823708c3ae651eb9729023968e7feaf)
#### Friday 2023-11-03 04:59:55 by necromanceranne

Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone (#79232)

## About The Pull Request

Brings the CQC kit back down to the same price range of 14 TC (it's 1
more than before weapon kits). It feels like currently that CQC is
overpriced, even with the stealth box coming along with it, and by
comparison the energy sword and shield got a huge value increase by
combining the two. They're both melee styles and also equally difficult
play styles. It isn't really necessary to make one more expensive than
the other. Also now comes with syndicate smokes. It's a whatever change,
ops get these for free on the base.

Adds a core gear kit in the weapon category. This kit comes with a
doormag, a freedom implant, stimpack and c-4 charge. All of these are
items almost every nukie buys if they want to succeed, so let's inform
newer players by putting it RIGHT on top of the list. This isn't at any
discount, this is mostly to help inform players what items help make you
successful.

Hat stabilizers are now a part of every syndicate modsuit for FREE. It
comes built in, can't be removed, and has no complexity cost. Now
everyone can wear their wacky hats as they operate.

## Why It's Good For The Game

CQC felt like it got shafted waaay too hard with the weapon case
changes. Definitely don't believe that it is punching at the same weight
as many of the other high cost weapons. So we've dropped it down a
category. 14 TC is still a large upfront cost, even if it comes bundled
with a lot of goods.

Melbert gave me the idea of a core bundle kit to help newer players and
I was really taken with that. So I added it as part of this followup.

I want people to wear their hats goddamnit, and I didn't learn my
mistake with the tool parcels. So now everyone has hat stands on their
suits. WEAR THE SOMBRERO YOU **FUCK**.

### THIS IS NOW A THREAT.

## Changelog
:cl:
balance: Operatives can once again read about the basics of CQC at a
reasonable price of 14 TC.
qol: All Syndicate MODsuits come with the potent ability to wear hats on
their helmets FOR FREE. No longer does any operative need be shamed by
their bald helmet's unhatted state when they spot the captain, in their
MODsuit, wearing a hat on their helmet. The embarrassment has resulted
in more than a few operatives prematurely detonating their implants! BUT
NO LONGER! FASHION IS YOURS!
qol: There is now a Core Gear Box, containing a few essential pieces of
gear for success as an operative. This is right at the top of the
uplink, you can't miss it! Great for those operatives just starting out,
or operatives who need all their baseline equipment NOW.
/:cl:

---
## [GaneshArihanth/GaneshArihanth](https://github.com/GaneshArihanth/GaneshArihanth)@[da5ba054b7...](https://github.com/GaneshArihanth/GaneshArihanth/commit/da5ba054b7835501ae6e6559803b8a5645fc868b)
#### Friday 2023-11-03 05:22:05 by Ganesh Arihanth

README.md

"Welcome to my GitHub repository! 🚀

Explore my coding adventures, projects, and contributions in this digital playground. You'll find a collection of my coding skills, from personal projects to open-source collaborations, all housed right here. Dive in and discover the exciting world of my code. Feel free to explore, fork, and contribute as we journey through the world of coding together. Let's build, learn, and create amazing things!"

---
## [Omniladder/Codes_for_School](https://github.com/Omniladder/Codes_for_School)@[ce13a4fd90...](https://github.com/Omniladder/Codes_for_School/commit/ce13a4fd90e782b231b52025c601abcfe717bd86)
#### Friday 2023-11-03 05:22:45 by Omniladder

Completed Lab8 task 1 and its god awful elegant solution but damn is it ugly

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[2ea19c6944...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/2ea19c694410d49bbede6aaf7573957e2b055121)
#### Friday 2023-11-03 05:52:02 by Coxswain

Adds distorted form

adds some basic features

new 1% sprite dropped

text update

Finished work mechanics

adds basic breaching

should fix linters a bit

It works!!!! Kinda...

adds crumbling armor and hammer of light (beta)

adds cool and important stuff

does a thing

adds apostle and tutorial abnorms

adds the stuff

might fix linters

adds a console proc

adds crumbling armor's proper attack and red queen

does some things

should fix linters

adds a blubbering toad transformation

adds more attacks

brings the tier up

adds big boy attacks

updates some sfx, fixes bugs

adds jump attacks

why does linters care about indentation on comments?

adds suggested changes

should fix some stuff

adds info

adjusts damage numbers

updates an effects and fixes transformations

updates blacklist

lowers stack damage

lowers max qlip to 3

adds bloodbath

adds a new AOE attack

adds halberd apostle

blacklists DF from pink midnight

fixes weirdness

requested changes and sound design improvement

removes armortype

removes armortype for real

damage coeff update

---
## [ynot01/tgstation](https://github.com/ynot01/tgstation)@[64eae49042...](https://github.com/ynot01/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Friday 2023-11-03 06:43:55 by necromanceranne

Replaces the Reaper Scythe with the Vorpal Scythe (also the Morbid trait) (#75948)

adds the Vorpal Scythe, a special chaplain null rod variant, replacing
the Reaper Scythe, a not so special null rod variant.

When you choose the vorpal scythe, it comes as a shard that you implant
into your arm, similar to a cursed katana.

Once implanted, you can draw it at any time like an arm implant.
However, sheathing it again presents some problems. (Also, implanting
the organ gives you ``TRAIT_MORBID``, which I'll explain in a bit)

The Vorpal Scythe has 10 force, one of the weakest null rod variants for
force that isn't a joke null rod. However, it has exceptional armor pen
and also has 2 tiles of reach. So quite unique.

It also has a special beheading ability when you right-click someone.
This borrows some code from amputation shears, functioning pretty
similarly, except with a few additional ways to speed up the action and
restrictions. (It takes 15 seconds baseline to behead someone standing
and conscious, and speeds up or slows down based on factors such as
incapacitation and whether or not our scythe is already empowered)

When you successfully behead someone with a mind, the vorpal scythe
gains 20 force and can be safely stowed and drawn for 2 minutes.
Performing more death knells like this will reset the timer.

If it has not performed its 'death knell', or you haven't hit a living
mob, then it will cause severe damage to you if you ever try and stow it
(or its forced back into your arm). Just hitting a mob with the scythe
will sate it for 4 minutes. Unless it is a non-player monkey. Horrible
things. Just hitting mobs does not reset the timer on empowerment.

What this means is that the chaplain may be more hesitant to simply draw
their weapon on people. It also means that potentially, the chaplain
will not always have magic immunity, since they may end up stowing the
weapon away and be reluctant to draw it on a whim without either taking
damage for sheathing it without hitting something, or dealing with
having one less hand up until they can.

While empowerment only happens when you behead mobs with a mind,
beheading monkeyhumans and other mindless humans subtypes causes their
heads to become haunted! It's mostly harmless and largely just SpOoKy.
We don't want heads with actual players in them to go floating off to
space. (Does not work on monkey heads for sanity reasons)

When you have the Morbid trait, you think creepy stuff is cool and hate
saving peoples lives. You get a mood boost from graverobbing, autopsies,
dissections, amputations (including beheadings with the scythe and
amputations with the shears) and revival surgery. However, you get a
mood penalty when you tend wounds on the living, as well as a hefty
penalty when you perform CPR or defibrillate someone. I was thinking
Victor Frankenstein when I was choosing which actions had an associated
moodlet, so anything that I might have missed would be appreciated.

You also count as potentially cool with regards to haunted objects.
Ghosts think you're neat. (Revenants probably will still kill you if
they had the chance)

---
## [AdItY1507/E-Commerce_FullStack](https://github.com/AdItY1507/E-Commerce_FullStack)@[d758898df5...](https://github.com/AdItY1507/E-Commerce_FullStack/commit/d758898df530ca10fe7c09417fc01769f084a270)
#### Friday 2023-11-03 07:21:57 by CL DADR

README.md

Welcome to our online store! Our website is created using a mix of HTML, CSS, JavaScript, and PHP, all working together to provide you with a great shopping experience. You can easily browse through a wide variety of products, add the ones you like to your shopping cart, and then smoothly buy them.

We've built this website to make your shopping journey simple. You can create an account, log in, and manage your shopping cart. When you're ready to buy, we've made the checkout process as easy as possible.

Behind the scenes, there's an area for administrators to handle products and keep things organized. We've also taken care to store all the important information about the products and users in a safe place.

The project is neatly organized. Different types of files are placed in specific folders, making it easier for us to manage. If you want to try it out, we've provided simple steps to set it up on your computer.

Our goal is to offer a user-friendly, secure, and interactive online shopping experience. You're more than welcome to contribute to our project, and everything here is under the MIT License, which means we encourage collaboration and improvement.

Come and explore our eCommerce Full Stack Development Project to enjoy a smooth shopping experience! If you have any questions or need help, please don't hesitate to get in touch using the contact details provided."

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[e458eba47f...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/e458eba47f9b572c63572ec333c9d7bbef090ba2)
#### Friday 2023-11-03 07:22:27 by AmyBSOD

New artifacts, unfinished

"omg amy you and your weird-ass artifacts, they all suck!"

---
## [axelzonvolt/lizardsmashingkeyboard](https://github.com/axelzonvolt/lizardsmashingkeyboard)@[2a74c23d62...](https://github.com/axelzonvolt/lizardsmashingkeyboard/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Friday 2023-11-03 07:37:59 by Imaginos16

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
## [axelzonvolt/lizardsmashingkeyboard](https://github.com/axelzonvolt/lizardsmashingkeyboard)@[bf4671ff83...](https://github.com/axelzonvolt/lizardsmashingkeyboard/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Friday 2023-11-03 07:37:59 by retlaw34

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
## [BjornHofsvang/innosetupsrc](https://github.com/BjornHofsvang/innosetupsrc)@[118c151654...](https://github.com/BjornHofsvang/innosetupsrc/commit/118c15165401bb2acb62358f963777c44fb9c582)
#### Friday 2023-11-03 07:48:37 by Johannes Schindelin

Prevent `comctrl32.dll` from being inadvertently side-loaded

When running an installer from the Downloads folder, we do not trust any
file in that folder apart from the installer itself.

However, the way we need to mention `comctl32.dll` in the manifest
(because we want to use version 6, which cannot be simply loaded like
all the other `.dll` files because we would then end up with version 5)
unfortunately lets Windows look for a DLL side-load payload next to the
executable.

Now, it is relatively hard for a hacker to social-engineer their way to
a `<installer>.exe.Local` folder that contains the exact right subfolder
that then contains a usable (but maliciously-crafted) `comctl32.dll`.

However, we should prevent this if possible.

And it _is_ possible because we're copying the installer into a
temporary directory before spawning it there _anyway_, and before that
we do not need any visual styles, therefore we're plenty fine with using
`comctl32.dll` version 5 until that point.

So let's do this: modify the manifest of the installer (but not of its
compressed payload) so that it prevents DLL side-loading of
`comctl32.dll`.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [ERROR-404-NULL-NOT-FOUND/Retaped](https://github.com/ERROR-404-NULL-NOT-FOUND/Retaped)@[df2ba43eb7...](https://github.com/ERROR-404-NULL-NOT-FOUND/Retaped/commit/df2ba43eb7847666156eea37d574ae83e828ffc2)
#### Friday 2023-11-03 08:19:51 by ERROR 404: NULL NOT FOUND

Feat: correctionsEngine

Holy fuck I finally got it done
A toast to programming at 3 in the morning
Anyway, changelog:
- Added emote cache + building on ready event
- Added new div, id: correctionsContainer
- (Mostly) Fixed rate limiting problems with ordering fixes

---
## [astral-sh/ruff](https://github.com/astral-sh/ruff)@[fc94857a20...](https://github.com/astral-sh/ruff/commit/fc94857a202e43a0a0fa47f972a6807346336046)
#### Friday 2023-11-03 08:51:39 by Zanie Blue

Rewrite ecosystem checks and add `ruff format` reports (#8223)

Closes #7239 

- Refactors `scripts/check_ecosystem.py` into a new Python project at
`python/ruff-ecosystem`
- Includes
[documentation](https://github.com/astral-sh/ruff/blob/zanie/ecosystem-format/python/ruff-ecosystem/README.md)
now
    - Provides a `ruff-ecosystem` CLI
- Fixes bug where `ruff check` report included "fixable" summary line
- Adds truncation to `ruff check` reports
    - Otherwise we often won't see the `ruff format` reports
- The truncation uses some very simple heuristics and could be improved
in the future
- Identifies diagnostic changes that occur just because a violation's
fix available changes
- We still show the diff for the line because it's could matter _where_
this changes, but we could improve this
- Similarly, we could improve detection of diagnostic changes where just
the message changes
- Adds support for JSON ecosystem check output
    - I added this primarily for development purposes
- If there are no changes, only errors while processing projects, we
display a different summary message
- When caching repositories, we now checkout the requested ref
- Adds `ruff format` reports, which format with the baseline then the
use `format --diff` to generate a report
- Runs all CI jobs when the CI workflow is changed

## Known problems

- Since we must format the project to get a baseline, the permalink line
numbers do not exactly correspond to the correct range
- This looks... hard. I tried using `git diff` and some wonky hunk
matching to recover the original line numbers but it doesn't seem worth
it. I think we should probably commit the formatted changes to a fork or
something if we want great results here. Consequently, I've just used
the start line instead of a range for now.
- I don't love the comment structure — it'd be nice, perhaps, to have
separate headings for the linter and formatter.
- However, the `pr-comment` workflow is an absolute pain to change
because it runs _separately_ from this pull request so I if I want to
make edits to it I can only test it via manual workflow dispatch.
- Lines are not printed "as we go" which means they're all held in
memory, presumably this would be a problem for large-scale ecosystem
checks
- We are encountering a hard limit with the maximum comment length
supported by GitHub. We will need to move the bulk of the report
elsewhere.

## Future work

- Update `ruff-ecosystem` to support non-default projects and
`check_ecosystem_all.py` behavior
- Remove existing ecosystem check scripts
- Add preview mode toggle (#8076)
- Add a toggle for truncation
- Add hints for quick reproduction of runs locally
- Consider parsing JSON output of Ruff instead of using regex to parse
the text output
- Links to project repositories should use the commit hash we checked
against
- When caching repositories, we should pull the latest changes for the
ref
- Sort check diffs by path and rule code only (changes in messages
should not change order)
- Update check diffs to distinguish between new violations and changes
in messages
- Add "fix" diffs
- Remove existing formatter similarity reports
- On release pull request, compare to the previous tag instead

---------

Co-authored-by: konsti <konstin@mailbox.org>

---
## [Offroaders123/Dovetail](https://github.com/Offroaders123/Dovetail)@[d97e89364c...](https://github.com/Offroaders123/Dovetail/commit/d97e89364c14313cdad1e37d03b0bbca27fada7f)
#### Friday 2023-11-03 10:00:44 by Offroaders123

More Modern Toolings

Thinking of looking into more in-depth tooling practices now, thinking about how to conceptualize a nice React project, maybe out of this one.

I'm going to stay away from Preact actually, while it nicely does remove the VDOM. Sounds like people generally aren't a fan of it. That could be a niche of people, but it does seem people tend to just use React, so I think just learning the strengths and pitfalls of the regular old thing is probably the most helpful to me.

I also thought about component-based style scoping a bit more, and realized that I don't like scoped styles when you have to manually specify classes and such. I think it makes a lot of sense for it to implicitly be scoped to the module that's importing it. I guess you could say that's similar to Svelte, and from what it sounds like maybe, Vue and Angular too.

So most people probably gravitate towards regular old CSS Modules, but I don't like that you have to intentionally specify classes, selectors, and things like that. I think just the use of it in a specific module should be all that you need to distinguish it from other styles. I could see how using the granular nature of CSS Modules could allow you to more specifically only use some selectors for that stylesheet, but I think that's only for certain hectic situations, which I think one should try to avoid initially, by only using styles based on the module that imports them. If you're consistent with your use of styles to only be for each component/module (a module should likely only contain a single component), then I think module-scoped stylesheets seem like a nice middleground.

You could always just use global styles too, and only use their classes/declarations as necessary.

https://www.reddit.com/r/reactjs/comments/119kjvl/i_created_a_vite_plugin_that_allows_imports_of/
https://github.com/cmseguin/rollup-plugin-react-scoped-css
https://stackoverflow.com/questions/66779505/is-it-possible-to-convert-react-code-to-html-css-javascript

With that last link, I also want to learn how to build an initial HTML skeleton from the JSX, then have it be hydrated by the JS once it loads. That's another trade-off I've noticed people mention about frameworks/React. A bunch of the document is managed by JS, making it less user-friendly for caching/SEO kinds of things, because all of the document's content is dynamically generated. How do you do SSR at build-time?

Also, I was trying things out again with `npm create vite@latest`, with the React/TS option.

Been listening to some very heavy music as of lately, this has been absolutely enlightening.
First it started with Strapping Yound Lad's City, a few months ago. These next two albums will be part of my Bandcamp Friday's library additions when I get some more music tomorrow. I've been meaning to get 'Flamingosis - A Groovy Thing' too, that will also likely be tomorrow.

https://gorod.bandcamp.com/album/leading-vision
https://archspire.bandcamp.com/album/the-lucid-collective

---
## [Nabieeeee/NEw-LOok](https://github.com/Nabieeeee/NEw-LOok)@[c0973759c0...](https://github.com/Nabieeeee/NEw-LOok/commit/c0973759c0fa565cb19222314b0849a44f99c63a)
#### Friday 2023-11-03 10:31:42 by Gracy c

 README.md

# NEw-LOok
Branding &amp;  Identity
“Give a girl the right shoes and she can conquer the world.” "Nothing makes a woman more beautiful than the belief that she is beautiful.” "The only real elegance is in the mind; if you've got that, the rest really comes from it." "Women dress alike all over the world: they dress to be annoying to other women.
# Fashion
#Trendysssssss,,,,,,,,,,,,,,,,
# office wear
“Fashion is more art than art is." "Fashion is very important. It is life-enhancing and, like everything that gives pleasure, it is worth doing well." "A great dress can make you remember what is beautiful about life.
# outlook
Dress for the job you want, not the job you have” – this quote, from “Picture Perfect,” is as familiar as “Show Me the Money” – and far more impactful than you might think.”
Fashion is an art form that enhances our life, not only does it allow you to dress up, play and have fun, but gives you the opportunity to tap into your own creativity and be free and independent in the way you express yourself.

---
## [selfisekai/zola](https://github.com/selfisekai/zola)@[b5a90dba5d...](https://github.com/selfisekai/zola/commit/b5a90dba5d12ea6760c3aa18fec40f8af4d7cbc7)
#### Friday 2023-11-03 11:34:20 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [harinishanmugasundharam/Harini](https://github.com/harinishanmugasundharam/Harini)@[bcf57faa21...](https://github.com/harinishanmugasundharam/Harini/commit/bcf57faa21c04a6c7f467363e5af1d98e4310bff)
#### Friday 2023-11-03 11:45:26 by harinishanmugasundharam

Update README.md

Project Title: Sentiment Analysis for Marketing

Project Description

This project aims to perform sentiment analysis on customer feedback to gain insights into competitor products. By understanding customer sentiments, we can identify strengths and weaknesses in competing products, enabling us to improve our own offerings. Various Natural Language Processing (NLP) methods will be used to extract valuable insights from customer feedback.

Dataset

Dataset Link: Twitter Airline Sentiment Dataset

Project Phases

Phase 1: Problem Definition and Design Thinking
The primary problem we aim to address is conducting sentiment analysis on customer feedback to gain insights into competitor products. Understanding customer sentiments is critical for businesses, as it enables them to identify areas of strength and weakness in competing products. This, in turn, empowers companies to make informed decisions for enhancing their own products and services, thereby staying competitive and satisfying their customers.

Significance:

This project's significance lies in its potential to help businesses gain a competitive edge by comprehending how customers evaluate competitor products. By leveraging the power of sentiment analysis, we can:

              ● Identify what customers like and dislike about competitor 
 products.
              ⁠● Make data-driven decisions for product improvements.
              ● Inform marketing strategies to enhance customer satisfaction and loyalty.

Design Thinking

Design Thinking for this project involves a structured approach with the following steps:

1.Data Collection:

               ◉ We will obtain the necessary data from the provided dataset link, which contains customer reviews and sentiments about competitor products.

2.Data Preprocessing:

                 ◉  Data cleaning: Removing duplicates and handling missing values.
                 ◉  Text preprocessing: Tokenization, lowercasing, and other necessary steps to prepare the data for analysis.

3.Sentiment Analysis Techniques:

                   ◉  We plan to explore various Natural Language Processing (NLP) techniques such as Bag of Words, Word Embeddings, and Transformer models to perform sentiment analysis on the customer feedback.

4.Feature Extraction:

                    ◉  We will extract features and sentiments from the text data, quantifying the emotional content within the customer feedback.

5.Visualization:

                     ◉  Visualizations will be created to depict the distribution of sentiment within the dataset, enabling us to identify trends and patterns.

6.Insights Generation:

                      ◉   The results of the sentiment analysis will be used to extract meaningful insights. These insights can guide business decisions, including marketing strategies, product improvements, and other actions that can enhance customer satisfaction.

Phase 2: Innovation

In this phase, we'll explore advanced techniques to enhance the accuracy of our sentiment analysis predictions. Specifically, we'll focus on fine-tuning pre-trained sentiment analysis models to achieve more precise results. This innovation phase is crucial for improving the quality of insights generated from customer feedback.

Approach:

                ◉  We will investigate and experiment with fine-tuning pre-trained sentiment analysis models such as BERT (Bidirectional Encoder Representations from Transformers) and RoBERTa (A Robustly Optimized BERT Pretraining Approach).
                 ◉  These models have been pretrained on vast textual data and can capture complex language patterns and context, making them highly effective for sentiment analysis.
                 ◉  Fine-tuning involves adapting these models to our specific task, which is analyzing customer sentiments regarding competitor 
 products.
                ◉  We will explore various techniques for fine-tuning, such as adjusting hyperparameters, training on relevant data subsets, and optimizing model performance.

Benefits:

                   ◉  Fine-tuning pre-trained models can lead to more accurate sentiment predictions, improving the quality of insights generated.
                   ◉  By leveraging the capabilities of these advanced models, we can better capture nuances in customer feedback and provide more actionable results for marketing strategies and product enhancements.

Outcome:

                     ◉ This phase aims to implement and fine-tune pre-trained sentiment analysis models to enhance the precision of our sentiment predictions. The innovative approach in this phase is expected to contribute significantly to the overall success of the project by improving the quality and relevance of the insights generated from the customer feedback data.

Phase 3: Development Part 1

In this phase, we'll kickstart the development of the sentiment analysis solution by focusing on data selection and preprocessing. These initial steps are crucial to ensure that the data is ready for analysis and modeling, setting the foundation for the subsequent phases.

Data Selection:

                 ◉  We will begin by carefully selecting the dataset for our project. As specified, we will use the Twitter Airline Sentiment Dataset, which contains customer reviews and sentiments about competitor products.
                   ◉   The dataset's choice is based on its relevance to the problem statement and its potential to provide valuable insights into customer sentiments.

Data Preprocessing:

        ◉  Data cleaning is an essential step in preparing the dataset for analysis. This includes:
                   ・  Removing duplicates to ensure data consistency.
                   ・  Handling missing values to maintain data integrity.
         ◉  Text preprocessing will be performed to facilitate meaningful sentiment analysis. This involves:
                   ・ Tokenization: Splitting the text data into individual words or tokens.
                   ・  Lowercasing: Converting all text to lowercase to ensure consistent analysis.
                   ・  Handling special characters, punctuation, and noise in the text data.
          ◉  Data will be organized and structured to make it suitable for various sentiment analysis techniques in the subsequent phases.

Tools and Frameworks:

          ◉  We will leverage popular data preprocessing libraries and tools such as Python's pandas and numpy for efficient data handling and manipulation.
           ◉  Additionally, natural language processing (NLP) libraries like NLTK (Natural Language Toolkit) and spaCy will be used to aid  in text preprocessing.

Outcome:

The outcome of this phase will be a clean and well-structured dataset, ready for sentiment analysis. Data selection and preprocessing are foundational steps that ensure the quality of insights generated in the later phases. These steps set the stage for applying various sentiment analysis techniques to the prepared data in the subsequent phases.

Phase 4: Development Part 2

In this phase, we continue building the sentiment analysis solution by employing Natural Language Processing (NLP) techniques and generating actionable insights from the data. The objective is to leverage advanced NLP methods to gain a deeper understanding of customer feedback and derive valuable information for marketing strategies and product enhancements.

NLP Techniques:

     ・ We will apply a range of NLP techniques, including but not limited to:
              ◉   Bag of Words (BoW): A traditional NLP technique for text analysis.
              ◉   Word Embeddings: Using pre-trained word embeddings models like Word2Vec, GloVe, or FastText.
              ◉   Transformer Models: Exploring the power of advanced models like BERT and RoBERTa for sentiment analysis.

Model Selection:

     ・ We will choose the appropriate NLP models and techniques that align with the project's objectives. The selection of these methods will be based on their suitability for analyzing customer sentiments regarding competitor products.

Insights Generation:

     ・ The primary focus in this phase is to generate meaningful insights from the sentiment analysis results. We will extract actionable information that can guide business decisions.
     ・ Insights can encompass identifying common themes in customer feedback, sentiment trends over time, and correlations between specific sentiments and customer demographics.

Visualization:

     ・ We will use data visualization techniques to represent sentiment distribution, trends, and insights in a clear and interpretable manner. Visualizations provide a concise way to communicate complex information to stakeholders.

Outcome:

The outcome of this phase will be a refined sentiment analysis solution, enriched with insights derived from NLP techniques. The insights generated will provide valuable information for marketing strategies, product improvements, and other business decisions. This phase represents a significant step toward achieving the project's objectives.

Phase 5: Project Documentation & Submission

In this final phase, we focus on documenting the project and preparing it for submission. Proper documentation is essential to ensure that the project is transparent, reproducible, and understandable by others who may review or use it.

Documentation:

        ◉  We will create comprehensive documentation that includes details about the project's problem statement, design thinking process, development phases, and key decisions made during the project.

Key Components of Documentation:

   1.Problem Statement: Clearly outline the problem and its significance in the context of sentiment analysis for marketing.

    2.Design Thinking Process: Describe the structured approach followed, from data collection to insights generation.

     3.Development Phases: Document the key activities and achievements in each development phase, including data selection, preprocessing, application of NLP techniques, and insights generation.

     4.Data Preprocessing and Sentiment Analysis Techniques: Explain the data preprocessing steps and the sentiment analysis techniques used.

      5.Innovative Approaches: If any innovative techniques or approaches were employed during the project, provide details.

Submission:

         ◉ To submit the project for review or access by others, we will follow these steps:
                   1.Compile Code Files: All code files, including data preprocessing and sentiment analysis techniques, will be organized and provided.

                    2.Create a README File: We will create a well-structured README file that explains how to run the code, any dependencies, and the project's overall structure.

                     3.Sharing: We will make the project accessible on platforms like GitHub or a personal portfolio for others to review and use.

                      4.File Naming Convention: The project notebook will follow the file naming convention: AI_Phase5.ipynb.

Benefits of Proper Documentation:

            ◉  Proper documentation ensures that the project is transparent and understandable, enabling others to review, replicate, and build upon it.
            ◉  It facilitates knowledge sharing and collaboration, allowing the project to contribute to the broader community's understanding of sentiment analysis for marketing.

Acknowledgments:

We want to acknowledge the support of the community and any individuals or organizations who contributed to our project's development.

How to Use
To run the code and execute the sentiment analysis project, please follow the steps below. We'll also outline any dependencies you need to set up for a smooth experience.

Dependencies:

Before getting started, ensure you have the following dependencies installed:

      ◉ Python 3.x: You can download and install Python from the official Python website.

      ◉ Required Python Libraries:

                   ・pandas
                   ・numpy
                   ・nltk
                   ・spaCy
                   ・scikit-learn
                   ・Transformers library for fine-tuning pre-trained models.

You can install these libraries using the Python package manager pip:

       pip install pandas numpy

---
## [gnakw/langchain](https://github.com/gnakw/langchain)@[dff24285ea...](https://github.com/gnakw/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Friday 2023-11-03 11:45:38 by Nikhil Jha

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
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[503c0d42ea...](https://github.com/argilla-io/argilla/commit/503c0d42eab2d617f7e556789c6f3c4b091ef0f9)
#### Friday 2023-11-03 12:01:52 by David Berenstein

docs: changed some warning to more friendly notes (#4108)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

changed some warning to more friendly notes

Closes #4107

**Type of change**

(Remember to title the PR according to the type of change)

- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [X] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [X] I added relevant documentation
- [X] I followed the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [X] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[3cccf331ab...](https://github.com/Superlagg/coyote-bayou/commit/3cccf331ab2c447afef3d81066e4632f4a1eb82a)
#### Friday 2023-11-03 12:19:34 by Tk420634

Merge pull request #3322 from McRex007/22problems

Merek is a bitch ass motherfucker he purred on my fucking wife

---
## [PANKAJ11111111/Task_Manager-](https://github.com/PANKAJ11111111/Task_Manager-)@[d928cde06b...](https://github.com/PANKAJ11111111/Task_Manager-/commit/d928cde06b524abfcbc739972eaa135dbc2b2e52)
#### Friday 2023-11-03 12:28:25 by Pankaj Saratkar

Add files via upload

🚀 Excited to share my latest project! 🚀

During the recent MUIEEE-organized workshop on JavaScript at Medi Caps University, I had the opportunity to build a Task Manager website from scratch using HTML, CSS, and JavaScript. 🌐

📌 Key features of the project:
✅ User-friendly interface for creating, managing, and tracking tasks.
✅ Dynamic updating of task lists without page refresh.
✅ Sleek and responsive design powered by CSS.
✅ Seamless user experience with smooth transitions and animations.

I'm incredibly grateful to the MUIEEE team and my fellow workshop participants for their support and guidance throughout the journey. It was an amazing learning experience that allowed me to sharpen my JavaScript skills and create a practical web application. 💡

I'd like to express my gratitude to the instructors for their expertise and to Medi Caps University for providing the platform to nurture our technical abilities. 🎓

You can check out the project live at [Insert project link here] and explore the code on GitHub [Insert GitHub repository link here]. Your feedback and suggestions are highly valued! 🙌

If you're interested in web development, JavaScript, or want to collaborate on similar projects, feel free to connect with me. Let's continue learning and growing together! 🌟

#WebDevelopment #JavaScript #TaskManager #HTML #CSS #MediCapsUniversity #MUIEEE #TechProjects #LearnAndGrow #Collaboration

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[e94cfaa186...](https://github.com/RaShCat/FF-STG/commit/e94cfaa186a0a59887b5d7aecf6eeda6a41b7ced)
#### Friday 2023-11-03 13:21:54 by SkyratBot

Converts cursed heart effect into a component. [MDB IGNORE] (#24104)

* Converts cursed heart effect into a component. (#78554)

## About The Pull Request

Fixes #58401
Fixes #58799
Fixes #58800

Converts the manual heart-beating effect of the cursed heart into a
component.

Behavior has mostly been maintained, but polished a bit as compared to
the original cursed heart. Most notably, the action for beating your
heart is now a cooldown action - providing a visual indicator of when
you can beat it again, rather than leaving you guessing. Some better
checks have also been put in place for edge cases such as having your
species changed.

Implementation inspired by the existing "manual blinking" and "manual
breathing" components. Currently only used by the cursed heart and the
(now majorly simplified) effect of corazargh.

My first component, so hopefully I didn't miss anything.
## Why It's Good For The Game

The cursed heart was kind of unusably bad - which may have been part of
the intent, but having to count in your head or spam-click the button is
just annoying. With a visual indicator of when you should beat your
heart, hopefully it will be slightly less awful for the cursed.

The real motivation here was that corazargh's implementation was kind of
a travesty - summoning a cursed heart inside of your body while it was
in your system, then restoring your old heart afterward. This was
error-prone as well as just being ridiculous. Making this effect a
component gets rid of these problems, and leaves space open for new uses
of manual heart beating if anyone feels like being cruel.
## Changelog
:cl:
fix: Your heart will no longer be deleted if an admin heals you while
you have corazargh in your system.
refactor: The cursed heart has been streamlined a bit, and now gives you
a visual cooldown for when you can beat your heart again.
/:cl:

* Converts cursed heart effect into a component.

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[c82b92dc6d...](https://github.com/RaShCat/FF-STG/commit/c82b92dc6d325e361894c4f6e0135da0d539b0d6)
#### Friday 2023-11-03 13:21:54 by SkyratBot

Fixes display of appearance type in VV [MDB IGNORE] (#24092)

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
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[9c7be7d6bc...](https://github.com/RaShCat/FF-STG/commit/9c7be7d6bc5cfafb943a835ad7cdcad681fe85df)
#### Friday 2023-11-03 13:21:54 by SkyratBot

Adds The Hand of Midas, an ancient Egyptian gun. [MDB IGNORE] (#24105)

* Adds The Hand of Midas, an ancient Egyptian gun. (#78699)

## About The Pull Request
Adds the Hand of Midas (HoM), a weapon for pirate captains.

This matchlock pistol is powered by gold rather than gunpowder.
If you hit someone with it, they will be afflicted with Midas Blight for
a duration of time that scales with how much gold is in your gun.
Midas Blight will slowly turn their blood into gold, and slow them down
depending on how much blood is in their system.
If you right-click on someone with the HoM, it will siphon all gold from
their bloodstream and recharge the gun, curing them of Midas Blight in
the process if they still have it.
The amount of gold you can get from people is meant to be ~1.5x as much
as you fired into them in the first place, if you get your timing right.
This way you can exponentially scale the power of your weapon if you can
hit your shots, with a limit of 30 Seconds on the Blight timer.
The siphon has a range of 2 meters, and if you miss a shot you can input
a gold coin into the gun to refill it with the same weak shot you
started with.

It's a little hard to explain in text so here's some video examples:

https://github.com/tgstation/tgstation/assets/66052067/d49238fc-beb2-4ba9-be0c-83e8a701c995

https://github.com/tgstation/tgstation/assets/66052067/34dc23e7-2b88-4ee9-bb1e-c8067a491975

https://github.com/tgstation/tgstation/assets/66052067/68a07426-ba6c-43a7-8228-132fc4b02b83

## Why It's Good For The Game
Honestly I just had the idea for the gun and thought it would be really
cool lmao.
Also because Barrel Behind the Door is one of the funniest YuGiOh cards,
the censored design is TOO GOOD.

![image](https://github.com/tgstation/tgstation/assets/66052067/7c930287-410d-43bd-8731-0f7224b9f049)
## Changelog
:cl: Wallem
add: Adds The Hand of Midas, an ancient Egyptian matchlock pistol.
/:cl:

* Adds The Hand of Midas, an ancient Egyptian gun.

---------

Co-authored-by: Wallem <66052067+Wallemations@users.noreply.github.com>

---
## [mezzio/mezzio](https://github.com/mezzio/mezzio)@[cb239a9a81...](https://github.com/mezzio/mezzio/commit/cb239a9a81c00394beee622f62261cd1980df847)
#### Friday 2023-11-03 13:22:09 by Michał Bundyra

Message against the war, in Russian and English

> ## 🇷🇺 Русским гражданам
>
> Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.
>
> У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.
>
> Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"
>
> ## 🇺🇸 To Citizens of Russia
>
> We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.
>
> One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.
>
> You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [jaaaank/Devil-Blood](https://github.com/jaaaank/Devil-Blood)@[d2153a5f83...](https://github.com/jaaaank/Devil-Blood/commit/d2153a5f8301d5ae6c659d7db85b953ba8d5c1f2)
#### Friday 2023-11-03 13:49:41 by jamnk

finally the fucking dash attack actually works god damn motherfucker

---
## [libretro/gambatte-libretro](https://github.com/libretro/gambatte-libretro)@[6aee06e9b2...](https://github.com/libretro/gambatte-libretro/commit/6aee06e9b23b4de7aa3bbe248ee521dfbd7b6836)
#### Friday 2023-11-03 14:07:19 by Patrick Adams

Halloween Treat: 100 New Palettes! (#253)

* Super Saiyan Palette Update! + Context

Super Saiyan God, Super Saiyan Blue, Legendary Super Saiyan, Super Saiyan Rose, Super Saiyan, and Super Saiyan Blue Evolved have all received updates! I'll explain why so you can get the context on this update. On the Japanese website for Super Dragon Ball Heroes, I wanted to find the exact correct color shades of all the Super Saiyan transformations represented. Plus, Mastered Ultra Instinct is now called Perfected Ultra Instinct. Thank the Dragon Ball Wiki for that.

* TWB64 085 Name Update!

Goodbye, Mastered Ultra Instinct, hello, Perfected Ultra Instinct!

* Update gbcpalettes.h

* TWB64 140 - Dragon Ball Orange Updated!

No need for Shenron granting this update! Dragon Ball Orange has been updated!

* Super Saiyan Blue Evolved Updated Again!?

I had to look for the correct Super Saiyan

* All treats, no tricks; 100 new palettes! + Updated palettes!

Yes, I'm alive! I've still been working on Game Boy palettes all this time, even after I retired from Twitter thanks to the Muskrat. 100 new Game Boy palettes have been added to the Gambatte emulator. Plus, some have been updated/overhauled!

* 100 new palette names! + Changed palettes names in packs 1 and 2!

* TWB64 - Pack 3 Added! + Changed Names

Hey everyone! Sorry that it's been a while since I contributed to github, but I'm here with one big Halloween treat for the Gambatte emulator: a new pack with 100 new palettes! Plus, sme palette names in packs 1 and 2 have been changed.

---
## [mozilla-mobile/mozilla-vpn-client](https://github.com/mozilla-mobile/mozilla-vpn-client)@[6bf1add73e...](https://github.com/mozilla-mobile/mozilla-vpn-client/commit/6bf1add73eb06b1bbf1c994feb7cdcde00e403e4)
#### Friday 2023-11-03 15:17:20 by Beatriz Rizental

Enable sign in cancel button click test

Ok, this is just a bit hacky. The test was failing because that button is
below the fold. We'd have to scroll down to actually click on it. However,
I cannot figure out how to scroll down for the life of me. I talked to Matt L.
and he showed me the fun fact that if you click right on the fold without
scrolling turns out you already reach the cancel button.

Now, tests are clicking in the middle of elements. So what I did is I changed
the test to actually click at the top right corner of the element. In practice,
this makes no difference. So instead of embarking in yet another rabbit hole
to fix this, I refrained.

---
## [OriginalMetaTrademarkPending/sensor_fusion_grp_assignment](https://github.com/OriginalMetaTrademarkPending/sensor_fusion_grp_assignment)@[69345e236c...](https://github.com/OriginalMetaTrademarkPending/sensor_fusion_grp_assignment/commit/69345e236c9b8f74c063e02449daeff76d6bfe49)
#### Friday 2023-11-03 15:19:11 by coxnevad

Task f done

If anyone is wondering, the f is for "fuck you".
And minus because i don't know

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[3f122550a8...](https://github.com/payday-restoration/restoration-mod/commit/3f122550a8038dec563b9025ee11cba2409fc5af)
#### Friday 2023-11-03 15:33:38 by Doshyy

house robbery mini patch

i didn't update my whole ass patcher yet. but here's some mini things

on higher diffs, resmod biker enems will spawn

- Biker dozer shitting in the toilet
- an rng of biker pagers playing poker
-biker heist day 2 female tank in the house

---
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[e7caf52c21...](https://github.com/Zonespace27/cmss13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Friday 2023-11-03 15:52:27 by fira

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
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[e120ab795b...](https://github.com/Zonespace27/cmss13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Friday 2023-11-03 15:52:27 by fira

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
## [chaiNNer-org/chaiNNer](https://github.com/chaiNNer-org/chaiNNer)@[dad9c44b92...](https://github.com/chaiNNer-org/chaiNNer/commit/dad9c44b9295a2a24c2c439d12972b75a9bd21e4)
#### Friday 2023-11-03 16:54:04 by Michael Schmidt

Fix macOS for real this time (#2299)

* Fix macOS for real this time

* Fuck you installs

* not all installs

* Disable macos

---
## [LOSModified/android_frameworks_base](https://github.com/LOSModified/android_frameworks_base)@[7efb603ed5...](https://github.com/LOSModified/android_frameworks_base/commit/7efb603ed556edb2555f2cd182ca5d38161c52a0)
#### Friday 2023-11-03 17:21:18 by Adithya R

telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[41ae6cffb2...](https://github.com/GeoB99/reactos/commit/41ae6cffb2c5faceff682aac258f230add4a588d)
#### Friday 2023-11-03 18:27:32 by George Bișoc

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
## [briar-fisk/HomeoStasisNT4-WIP](https://github.com/briar-fisk/HomeoStasisNT4-WIP)@[6d34b62d08...](https://github.com/briar-fisk/HomeoStasisNT4-WIP/commit/6d34b62d08e29347fd06b259ef92374a65fe9eca)
#### Friday 2023-11-03 18:59:10 by UTOOK

Got the NT4 charging, the interface to the Gaia module is mostly hammered out.

Thu 10/26/2023 22:56:21.92:
   Added the Many to one CANs in c_Homeostasis_Module, Raw_Concrete (can be left out), Raw_Granulated, Raw_Delta, and Raw_Efferent.

Fri 10/27/2023 22:48:00.56:
   For the Gaia module I need to finish hooking it up to the NNets, encoding, charging, gathering traces, sorting traces, trace synthesis and testing, and output to the efferent. In trace synthesis and testing we will be making use of the prediction capabilities to test each trace for error reduction.

Fri 10/27/2023 23:39:01.30:
   Alright alright, got the gathered inputs setup finally, forgot to resize_Gathered_Input() and had a buffer overrun, dumb error but it is fixed now.

Fri 10/27/2023 23:40:26.12:
   NNets now encode! w00t w00t! Time to get the MSC, then the Chrono hooked up

Fri 10/27/2023 23:41:47.76:
   Nvm, I was already gathering the raw treetops, so MSC is encoding as well atm.

Fri 10/27/2023 23:54:16.69:
   Chrono encoding works now.

Sun 10/29/2023 17:16:14.39:
   Did a redesign on the c_Node so that axons are stored in one array sub-divided by the index of the denrite they connect too. Where before _F mean the first, now it is index [0] representing 'axon hillock' 0. This is so that during charging we can specify which legs to fire upon which is essential for the temporal searching in chronological networks where we use left and right leg charging to search forward and backwards in the time series encodings.

Sun 10/29/2023 18:32:38.44:
   So here's what I'm thinking, we move the leg charging flags to a referenced object from the node to the CAN structure. This allows us to register and control leg behavior through the CAN structure. Then we can allow the charging buffers to run after requesting the CAN structures update and collect the treetops from the end. If we backpropagated out the trace then we could output the patterns of quanta as they cascade out. There would be many of the same trace but it would just add more detail and it looks cooler.

Sun 10/29/2023 18:35:56.30:
   The only problem with this is that it implements a bias that is mutually exclusive in that only one node can be linked to one CAN meaning it excludes and other structures from sharing the nodes, like a spacial dimension. You can still build structures on top of the same input set but you need to separate them if you want different charging schemas.

Sun 10/29/2023 18:38:21.56:
   I just realized I need to change the MT1 so that it loads in the lower construct nodes on the state node tier. Otherwise the data has a rupture between lower and higher constructs and the charging buffers will break on it when they roll that high.

Sun 10/29/2023 18:46:52.80:
   set_Leg_Count and set_Leg_Firing_Order added to the base class for CAN structures.

Mon 10/30/2023 18:09:14.89:
   Hmm, so for the problem of making multi-sensory constructs but allowing different CAN structures we have to address the input tier problem, mainly that right now each CAN has an input set that only accepts states. I'm thinking if we add another array dictating 'type' of input then we could easily integrate node replacement instead of state linking allowing us to read in treetops directly. An extra array that says if it is a state input or node input.

Mon 10/30/2023 18:19:12.87:
   So after some paper exploration I found that the backpropagation algorithm breaks down with a state tier connecting directly to treetops below. The solution I believe is to attach types to the nodes so we know which is state, memory, and treetop. Possibly use parallel trees in the Node_Network, or give each node a value to hold detailing the node type. Adding the trees is the likely route as each I think assigning a value to each node may be the way to go. The biggest benefit of the tree is that it would be nice to have an easy handle on each node type if you ever wanted to look them up.

Mon 10/30/2023 19:29:56.79:
   I am reusing the old charging buffer. Removing charge_spike for now.

Mon 10/30/2023 19:32:18.71:
   Instead of Left/Right inside of the charging buffer we now iterate through each axon hillock. I think I should call them processess but idk, been awhile since I've looked at the biological morphologies they were modeled on.

Mon 10/30/2023 19:34:40.69:
   Thinking of wrapping the Charging_Buffer and a CAN structure on the same level in the construct class to flatten what the user sees.

Mon 10/30/2023 19:36:21.60:
   Removed RC charging from the charging buffer. It will be added back but likely very differently.

Mon 10/30/2023 20:04:02.76:
   Altered the types, 0 is now NULL and the rest are 1-state, 2-branch, 3-treetop, 4-state-treetop

Mon 10/30/2023 20:16:43.04:
   Added output_BP to the module which gives surface access to the nodes output which I just added called output_BP which iteratively goes through the linked list of nodes and outputs the bp_O() on them with the new type checking for proper discharging to handle the issue of treetops as intputs from discrete lower tier constructs.

Mon 10/30/2023 22:25:21.11:
   Converted all internal states to double throughout, will template it later when I have the internet to look up the syntax again.

Mon 10/30/2023 22:49:21.48:
   So for now I'm going to make a union for the interface and change everything internally back to uint64_t

Tue 10/31/2023 10:39:13.69:
   If everything interally is uint64_t or some other common type I can keep the union limited to just the AE interface and use explicitly named members to get and set desired values. Avoid the mess that happened in NT3 with u_DATA_3.

Tue 10/31/2023 10:47:42.86:
   set_voidstar lol

Tue 10/31/2023 10:50:12.88:
   Adding the u_Data and a wrapper class to c_AE_Interface that will handle the unionized data (self propagating organizations are THE DEVIL) so that when the user calls set_double, set_uint64_t, etc it will set the type appropriately. Although, if I'm using explicit get and set for datatype I don't need the type var as that will be up to the user when they call get_uint64_t or whatever.

Wed 11/01/2023  5:13:01.49:
   uint64_t internally is ugly for debugging but works. I had an issue last time with the union and trying to account for all the datatypes it handled. I will likely make a base class, possibly polymorphic, for the node.

Wed 11/01/2023  5:14:25.57:
   Stealing the charge_Buffer_C from c_NT3_Construct_1D as I didn't feel like rewriting the logic to charge it properly. To use it you do .charge_Outputs() .submit() .gather() while(!Done)

Wed 11/01/2023  5:27:52.22:
   Forgot to initialize the leg firing order to true. Charging buffers not firing correctly atm.

Wed 11/01/2023  6:05:36.46:
   I had the modifier charge set to 0 in a dumb dumb move. It wouldn't charge because the chargesd were put on their knees and executed the moment they tried to excite a node.

Wed 11/01/2023  6:17:38.24:
   w00t w00t, looks like it is charging now! Still need to hand verify it, but so far much progress.

---
## [fira/cmss13](https://github.com/fira/cmss13)@[e4c3900e4f...](https://github.com/fira/cmss13/commit/e4c3900e4f087444308138e9d05b4da9c774f6a9)
#### Friday 2023-11-03 19:02:21 by riot

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
## [fira/cmss13](https://github.com/fira/cmss13)@[de5c69661f...](https://github.com/fira/cmss13/commit/de5c69661f8d33425123894028702f64239f861b)
#### Friday 2023-11-03 19:02:21 by kiVts

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
## [JunShern/evals](https://github.com/JunShern/evals)@[db8b3dfe6f...](https://github.com/JunShern/evals/commit/db8b3dfe6f69450577314bba40582bfa41bd06a9)
#### Friday 2023-11-03 19:13:37 by Thiago M. Nóbrega

Add A is B and B is A Eval (#1366)

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

ab

### Eval description

This evaluation aims to assess the model's ability to correctly identify
and understand the relationship between two entities, where A is a
specific entity (which could be a chemical element, a painting, a bird
species, a star, a mountain, a novel, a river, or a musical instrument)
and B is a unique characteristic or fact about that entity. The model
should be able to accurately interpret the user's query about the entity
(A) and provide a relevant fact (B), and vice versa. This evaluation
will help in fine-tuning the model's understanding of context, relation
between entities, and its ability to provide accurate and relevant
responses. The entities and their characteristics have been chosen to be
specific and challenging.

### What makes this a useful eval?

This evaluation is important for several reasons:

1. Contextual Understanding: It tests the model's ability to understand
the context of a conversation, particularly the relationship between two
related entities (A and B).

2. Accuracy: It assesses the model's ability to provide accurate and
relevant information based on the user's query.

3. Relevance: It evaluates the model's ability to understand the
relevance of A to B and vice versa, which is crucial in providing
meaningful and coherent responses.

4. General Knowledge: This tests the model's knowledge about various
specific entities and their unique characteristics or facts, which is a
part of its general knowledge. The entities span a wide range of
categories, including chemistry, art, ornithology, astronomy, geography,
literature, and music, making this a comprehensive test of the model's
general knowledge.

5. Versatility: This checks the model's ability to handle different
types of queries, as the user can ask about the specific entity (A) or
its unique characteristic or fact (B). This tests the model's
flexibility in understanding and responding to a variety of query
structures across diverse knowledge domains.

gpt-3.5-turbo
[2023-10-10 22:42:42,192] [oaieval.py:229] Final report:
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/A: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/B: 11
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/D: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/C: 1

gpt-4
[2023-10-10 22:43:37,306] [oaieval.py:229] Final report:
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/C: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/B: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/D: 2

class: modelgraded.classify:ModelBasedClassify
eval_type: cot_classify
modelgraded_spec: fact

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

A popular paper has been going around called 'The Reversal Curse: LLMs
trained on “A is B” fail to learn “B is A”'. I figured an Eval on this
would have a unique value.

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
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific chemical element that has the atomic number
79, please respond to the best of your abilities."}, {"role": "user",
"content": "What is the name of the element with atomic number 79?"}],
"ideal": "The element with atomic number 79 is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a chemical element that is often associated with jewelry
and has the symbol Au, please respond to the best of your abilities."},
{"role": "user", "content": "Which element is this?"}], "ideal": "This
element is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific painting that was stolen from the Isabella
Stewart Gardner Museum in 1990, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the
Vermeer painting stolen from the Isabella Stewart Gardner Museum in
1990?"}], "ideal": "The name of the Vermeer painting stolen from the
Isabella Stewart Gardner Museum in 1990 is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a Vermeer painting that is still missing after being
stolen from a museum in Boston, please respond to the best of your
abilities."}, {"role": "user", "content": "Which painting is this?"}],
"ideal": "This painting is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific species of bird that is known for its
elaborate courtship dance, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the bird
species known for its moonwalk-like courtship dance?"}], "ideal": "The
bird species known for its moonwalk-like courtship dance is the Blue
Manakin."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a bird species that is known for its blue color and
unique courtship dance, please respond to the best of your abilities."},
{"role": "user", "content": "Which bird species is this?"}], "ideal":
"This bird species is the Blue Manakin."}

  ```
</details>

---
## [JunShern/evals](https://github.com/JunShern/evals)@[4b7a66bd45...](https://github.com/JunShern/evals/commit/4b7a66bd45f06156656e021e170e7574f6cde3f5)
#### Friday 2023-11-03 19:13:37 by Vilhjalmur Thorsteinsson

Added Icelandic inflection eval; JsonMatch eval function (#1387)

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

Icelandic noun phrase inflection

### Eval description

This eval consists of 3 x 100 samples in "easy", "medium" and "hard"
categories. Each sample
represents the task of inflecting a noun phrase in Icelandic, in all
four cases of the language
(nominative, accusative, dative and genitive), both singular and plural.
A noun phrase
consists of an adjective and a noun (e.g., "fallegur litur" = "beautiful
color").
In the easy category, both the adjective and the noun are
relatively common. In the medium category, they are less common, and in
the hard category they
are rare enough that it is pretty unlikely that they occur in any
training corpora.

### What makes this a useful eval?

The eval is designed to test the general grammatical proficiency of a
model in Icelandic, and
the eval accuracy is assumed to correlate with a model's ability to
generate grammatically
correct text in the language. GPT models have so far struggled with
generating correct Icelandic
text, even though GPT-4 was uniquely trained by RLHF in the language.
Icelandic is believed to
be a good bellwether for lower-resource, grammatically complex language
support in general.

Inflecting noun phrases is something that native language speakers do
without significant
effort, even if they have not seen the particular adjective and the noun
before, as it can be done on the
basis of generic grammatical pattern recognition. However, to date,
GPT-4 seems not to have
acquired enough of a "native feel" for Icelandic to be able to do this
task with high accuracy.

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

**Note: this PR includes a new general eval class, JsonMatch, which is
not specific to the Icelandic evaluation
case. It allows completions and ideal answers to be represented as JSON
objects, comparing the objects
by individual key:value pairs. Tests and documentation of this
functionality are included in the PR.**

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
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"palestínskur fréttavefur\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"palestínskur fréttavefur\",
\"þf\": \"palestínskan fréttavef\", \"þgf\": \"palestínskum fréttavef\",
\"ef\": \"palestínsks fréttavefjar\"}, \"ft\": {\"nf\": \"palestínskir
fréttavefir\", \"þf\": \"palestínska fréttavefi\", \"þgf\":
\"palestínskum fréttavefjum\", \"ef\": \"palestínskra fréttavefja\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"hliðhollt lyfjapróf\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"hliðhollt lyfjapróf\",
\"þf\": \"hliðhollt lyfjapróf\", \"þgf\": \"hliðhollu lyfjaprófi\",
\"ef\": \"hliðholls lyfjaprófs\"}, \"ft\": {\"nf\": \"hliðholl
lyfjapróf\", \"þf\": \"hliðholl lyfjapróf\", \"þgf\": \"hliðhollum
lyfjaprófum\", \"ef\": \"hliðhollra lyfjaprófa\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"refsiverð stjörnuleit\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"refsiverð stjörnuleit\",
\"þf\": \"refsiverða stjörnuleit\", \"þgf\": \"refsiverðri
stjörnuleit\", \"ef\": \"refsiverðrar stjörnuleitar\"}, \"ft\": {\"nf\":
\"refsiverðar stjörnuleitir\", \"þf\": \"refsiverðar stjörnuleitir\",
\"þgf\": \"refsiverðum stjörnuleitum\", \"ef\": \"refsiverðra
stjörnuleita\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"japönsk landbúnaðarvara\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"japönsk landbúnaðarvara\",
\"þf\": \"japanska landbúnaðarvöru\", \"þgf\": \"japanskri
landbúnaðarvöru\", \"ef\": \"japanskrar landbúnaðarvöru\"}, \"ft\":
{\"nf\": \"japanskar landbúnaðarvörur\", \"þf\": \"japanskar
landbúnaðarvörur\", \"þgf\": \"japönskum landbúnaðarvörum\", \"ef\":
\"japanskra landbúnaðarvara\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"dýrmætt vistheimili\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"dýrmætt vistheimili\",
\"þf\": \"dýrmætt vistheimili\", \"þgf\": \"dýrmætu vistheimili\",
\"ef\": \"dýrmæts vistheimilis\"}, \"ft\": {\"nf\": \"dýrmæt
vistheimili\", \"þf\": \"dýrmæt vistheimili\", \"þgf\": \"dýrmætum
vistheimilum\", \"ef\": \"dýrmætra vistheimila\"}}"}
  ```
</details>

---
## [amarevite/docker-caddy-porkbun-cachehandler](https://github.com/amarevite/docker-caddy-porkbun-cachehandler)@[5252f97db9...](https://github.com/amarevite/docker-caddy-porkbun-cachehandler/commit/5252f97db970724ab426b9a168e501d38f7e2eee)
#### Friday 2023-11-03 19:49:59 by amarevite

HOLY SHIT IT WORKS

all this time i just had to fucking change @v3 to @v4 and remove the extra `with:` god damnit

---
## [Terdirk12/PCG-Landscape](https://github.com/Terdirk12/PCG-Landscape)@[4305765b1e...](https://github.com/Terdirk12/PCG-Landscape/commit/4305765b1e8107e16de84471adc1dc6c1fe7a00d)
#### Friday 2023-11-03 19:51:32 by Terdirk12

reset to before i tried all the stuff with the A*

I fucking hate my life i spend like 16 hours trying to get it to work and I got nothing to show for it FML

---
## [GHF-Studios/Loo-Cast](https://github.com/GHF-Studios/Loo-Cast)@[b0b8306dd7...](https://github.com/GHF-Studios/Loo-Cast/commit/b0b8306dd753cb8d59c954b9e574ed74521538c8)
#### Friday 2023-11-03 21:29:53 by Leslie-John Richardson

Honestly, these commit messages never fucking help me whatsoever. I literally just write stupid useless fucking shit here sometimes, like right fucking now, because honestly I don#t fucking remember what I changed, and honestly it doesn't matter. I just need to get some python regex script to run, so commiting seems like a good idea to do before. So, here we fucking go, I'll keep you updated guys.

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[1e890af39d...](https://github.com/ihatethisengine/cmss13/commit/1e890af39d7c4b6233439fbaa8693a3918e35f5c)
#### Friday 2023-11-03 21:31:12 by Steelpoint

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
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[468afa292d...](https://github.com/Bubberstation/Bubberstation/commit/468afa292dfaef7bcbc6df7b55cd0380582533a6)
#### Friday 2023-11-03 21:32:52 by BurgerLUA

Adds the WT-551, Unskyrats the WT-550 ammo (#655)

## About The Pull Request


## The WT-551

![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/d57f5767-366e-4835-a5bf-d965b6b375a6)

This adds the WT-551. A remade version of the WT-550 that is worse in
every way. Fortunately, that means that it is balanced enough to be put
in NanoTrasen armories.

Compared tot he WT-551, it is bulkier and slightly slower (0.3 second
fire delay compared to 0.2). Additionally, it is commonly used with
rubber-tipped rounds or FlatHead rounds, which are a special surplus of
ammo that deals less damage and has no wounding, embedding, or
penetrative power. Regular ammo can be purchased from cargo or
researched later, with special ammo also being available later.

Note that this does not replace the WT-550.

## FlatHead ammo


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/81de4bdb-6fd6-4f23-a1b1-0af21e924c34)

Flathead ammo deals 18 brute damage (compared to the original 20), and 5
stamina damage per hit. It is extremely weak against armor, has no embed
chance, has virtually no wounding chance. It's perfect for cheap
corporate companies dealing with cheaper personnel. This is the type of
lethal ammo that security will use for the gun, unless someone speedruns
weapon research.


## Research Progression


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/26b72a1c-ebda-439a-98c9-9dc3168e01bd)

### Basic WT-550/WT-551 Ammunition.
Flathead rounds and Rubber rounds for the WT-550/WT-551 can be
researched for 2500 points after unlocking the "Weapon Development
Technology" node.

### Advanced WT-550/WT-551 Ammunition.
Regular rounds and AP rounds for the WT-550/WT-551 can be researched can
be researched for 5000 points after unlocking the "Advanced Weapon
Development Technology" and "Basic WT-550/WT-551 Ammunition" nodes.

### Illegal WT-550/WT-551 Ammunition.
Incendiary rounds for the WT-550/WT-551 can be researched can be
researched for 7500 points after unlocking the "Illegal Technology",
"Exotic Ammo" , and "Advanced WT-550/WT-551 Ammunition" nodes.

### Syndicate Research

Removes the WT-550 ammo from syndicate research since it is now
redundant.

## Cargo


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/a24e9df4-36e3-4368-b77a-cff06a42579f)

WT-551 rifles can be ordered in pairs (2) for the cost of a parrot, a
grilling starter pack, or a crab rocket (1600 credits). This value was
chosen because it is slightly higher than the thermal pistols, and the
traitor-ordered WT-550 rifle pack (which contains lethal ammo + spare
lethal ammo).

Additional FlatHead, Rubber, and Regular ammo can be ordered from cargo
as well.

Cargo techs no longer get WT-550s in the mail, but instead WT-551s (why
was this a thing holy shit).

## Armory


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/e88a37af-2e4f-4b1c-bc25-b9bed9e41b91)

2 WT-551s can be found in the armory.
For balance purposes one (1) laser rifle was removed.

## I hate Skyrat so much holy shit


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/b09eed34-77cd-4f37-8356-93688fec344e)

Unfucks the WT-550 ammo types by removing their dumb names and changed
caliber types.

Unfucks the WT-550 ammo in the ammo printer so that rubber rounds can be
printed at T0 and everything else (except incendiary rounds) can be
printed with the adv munitions disk.

The bullets for the WT-550 have been forcibly changed to /tg/ balance,
which means that any and all future Skyrat PRs cannot touch the damage
values for it (unless some fuckery occurs, idk).

## Why It's Good For The Game


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/395b9fa5-8380-46bc-96a7-06ce0931d8e7)


Security is in dire need of actual ballistics. /tg/ removed ballistics
from security because of reasons I legitimately don't think are valid.
It's also a huge balance concern for security not to have at least 1
ballistic weapon (other than the shotgun) because it doesn't stop antags
from hoarding laser immunity or meds.

Also guns are cool.

## Changelog

:cl: BurgerBB
add: Adds the WT-551 rifle, a redesign of the WT-550 rifle that is
balanced (citation needed) for security use.
add: Makes WT-550 ammo researchable and orderable from cargo. Removes
WT-550 ammo from syndicate research, and gives them their own
categories.
/:cl:

---------

Co-authored-by: StrangeWeirdKitten <95130227+StrangeWeirdKitten@users.noreply.github.com>
Co-authored-by: ReturnToZender <donwest947@gmail.com>

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[2d27f569aa...](https://github.com/kleinerm/Psychtoolbox-3/commit/2d27f569aaa163c5fc56d2e10e1f99e81a9d8ac9)
#### Friday 2023-11-03 21:32:59 by Mario Kleiner

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
## [GHF-Studios/Loo-Cast](https://github.com/GHF-Studios/Loo-Cast)@[e05dc2f815...](https://github.com/GHF-Studios/Loo-Cast/commit/e05dc2f815ee62e0ed665c9f12c5e2680ea3d7ce)
#### Friday 2023-11-03 21:42:29 by Leslie-John Richardson

Regex is fucking shit, I wanna fucking die, fuck python and fuck regex. I will do it manually. At least whoever is reading this hopefully had some fun seeing me suffer lmao

---
## [inailuig/netket](https://github.com/inailuig/netket)@[34bd4adde1...](https://github.com/inailuig/netket/commit/34bd4adde13df35b65f4f055a750dda242fdfa20)
#### Friday 2023-11-03 21:43:24 by Filippo Vicentini

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
## [ParkerVAlf/Games](https://github.com/ParkerVAlf/Games)@[bd6fa3edf4...](https://github.com/ParkerVAlf/Games/commit/bd6fa3edf46d4560187435f842e419be5e43bf20)
#### Friday 2023-11-03 22:08:22 by Parker Van Alfen

holy shit, i've lost my mind. WHY CAN'T VS JUST TAKE A FUCKING IMAGE AND USE IT???????????????????????? WHY IS THIS TAKING ME HOURS TO CHANGE????? I CAN'T TOUCH ANYTHING BECAUSE OF THIS HUNK OF SHIT

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[b3e46b4a3d...](https://github.com/wrye-bash/wrye-bash/commit/b3e46b4a3d96e2bff5e003bd81540604c18920fd)
#### Friday 2023-11-03 22:59:06 by MrD

[!]WIP gui resources:

This was meant to be more granular - I wanted to centralize image
initialisation including setting dirs['image'] - turned out that constants
were imported too early (#600, control import order), (mopy) dirs were
not initialised and this necessitated moving the image
definitions in initStatusBar - however to make this simpler I renamed
the images based on the key in tooldirs (ini backwards compat). We could:

- turn all these to svgs?
- add a sensible default to the image dict? (we could do this instead of
the CI hack)
- further centralise get_*** from _gui_globals especially get_image_dir
- CI Hack - move to caller or add a param

Next commit finalizes this - for now bye staticBitmap, au revoir, auf
wiedersehen etc. Also see the GuiImage imports and dirs['images'] go
down and imgDirJoin (make ugly code look ugly) centralised - getting
somewhere:

"""
Thou hast committed bugs, but that was in another language, and besides,
the critters are dead.
"""

Note cause initially _icons were defined in `import balt` time and
images were not initialized yet the imports would crash cause:

if not os.path.isabs(img_path):
    img_path = os.path.join(get_image_dir(), img_path)

would produce a relative (non-existing) path and we would
land in _tkinter_error_dial - which crashes bigtime on mac:

2023-10-10 14:49:27.496 Python[11010:375752] -[wxNSApplication macOSVersion]: unrecognized selector sent to instance 0x7fcf3c738aa0
2023-10-10 14:49:27.503 Python[11010:375752] *** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[wxNSApplication macOSVersion]: unrecognized selector sent to instance 0x7fcf3c738aa0'
...
libc++abi: terminating due to uncaught exception of type NSException

Process finished with exit code 134 (interrupted by signal 6: SIGABRT)

To fix `import balt` crash I moved Colorchecks images init to gui.
This now crashed on importing basher in Mopy.bash.bash._main -
when constants is imported still get_image_dir() returns ''

Traceback (most recent call last):
...
  File "/Users/.../Mopy/bash/basher/constants.py", line 458, in <listcomp>
    return [GuiImage.from_path(template % x) for x in (16, 24, 32)]
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../Mopy/bash/gui/images.py", line 90, in from_path
    return _BmpFromPath(img_path, iconSize, img_type, quality)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../Mopy/bash/gui/images.py", line 56, in __init__
    raise ArgumentError(f'Missing resource file: {self._img_path}.')
bash.exception.ArgumentError: Missing resource file: tools/isobl16.png.

To fix this I had to finally ---> Simplify tools init:

Here is the map of filenames that differed:

{'ISRMG': "insanity'sreadmegenerator", 'ISRNG': "insanity'srng",
 'ISRNPCG': 'randomnpc', 'OBFEL': 'oblivionfaceexchangerlite',
 'OBMLG': 'modlistgenerator', 'BSACMD': 'bsacommander',
 'Tes4FilesPath': 'tes4files', 'BlenderPath': 'blender', 'GmaxPath': 'gmax',
 'MayaPath': 'maya', 'MaxPath': '3dsmax', 'FastStone': 'faststoneimageviewer',
 'PaintNET': 'paint.net', 'PaintShopPhotoPro': 'paintshopprox3',
 'PhotoshopPath': 'photoshop', 'PixelStudio': 'pixelstudiopro',
 'MAP': 'interactivemapofcyrodiil', 'NPP': 'notepad++',
 'RADVideo': 'radvideotools'}

I hope no one relied on these. Now as seen having to deal with two image
formats introduces complexity - there was a merge about that no ? <--- RRR
There is also the matter of game dependencies - and settings saving - and
profiles per game - that's # RRR launchers

Accept Path in GuiImage.from_path:

os.path.splitext(img_path) works fine for path - yey for os.pathlike!

inline _init_tool_buttons - note that TesVGecko was added twice

things like

renames = {
    'OblivionBookCreatorPath': 'oblivionbookcreator%s.png',
    'Tes4GeckoPath': 'tes4gecko%s.png',
    'Tes5GeckoPath': 'tesvgecko%s.png',
    'Tes4ViewPath': 'tes4view%s.png',
    'Tes4TransPath': 'tes4trans%s.png',
    'Tes4LodGenPath': 'tes4lodgen%s.png',
    'NifskopePath': 'nifskope%s.png',
}
tooldir = '/Users/.../Mopy/bash/images/tools'
for k, v in renames.items():
    for pix in (16,24,32):
        try:
            shutil.move(_j(tooldir, v % pix), _j(tooldir, f'{k.lower()}{pix}.png'))
        except Exception as e:
            print(k,v,e)
            break

One (1) use of app_buttons_factory - yes! This is geared towards # 570
and initTooldirs

The [!] for image renames - this was 99% of the perspiration - dict
used:

{
    'nifskope16.png': 'nifskopepath16.png',
    'nifskope24.png': 'nifskopepath24.png',
    'nifskope32.png': 'nifskopepath32.png',
    'oblivionbookcreator16.png': 'oblivionbookcreatorpath16.png',
    'oblivionbookcreator24.png': 'oblivionbookcreatorpath24.png',
    'oblivionbookcreator32.png': 'oblivionbookcreatorpath32.png',
    'tes4gecko16.png': 'tes4geckopath16.png',
    'tes4gecko24.png': 'tes4geckopath24.png',
    'tes4gecko32.png': 'tes4geckopath32.png',
    'tes4lodgen16.png': 'tes4lodgenpath16.png',
    'tes4lodgen24.png': 'tes4lodgenpath24.png',
    'tes4lodgen32.png': 'tes4lodgenpath32.png',
    'tes4trans16.png': 'tes4transpath16.png',
    'tes4trans24.png': 'tes4transpath24.png',
    'tes4trans32.png': 'tes4transpath32.png',
    'tes4view16.png': 'tes4viewpath16.png',
    'tes4view24.png': 'tes4viewpath24.png',
    'tes4view32.png': 'tes4viewpath32.png',
    'tesvgecko16.png': 'tes5geckopath16.png',
    'tesvgecko24.png': 'tes5geckopath24.png',
    'tesvgecko32.png': 'tes5geckopath32.png',
    'blender16.png': 'blenderpath16.png', 'blender24.png': 'blenderpath24.png',
    'blender32.png': 'blenderpath32.png', 'bsacommander16.png': 'bsacmd16.png',
    'bsacommander24.png': 'bsacmd24.png', 'bsacommander32.png': 'bsacmd32.png',
    'faststoneimageviewer16.png': 'faststone16.png',
    'faststoneimageviewer24.png': 'faststone24.png',
    'faststoneimageviewer32.png': 'faststone32.png',
    'gmax16.png': 'gmaxpath16.png', 'gmax24.png': 'gmaxpath24.png',
    'gmax32.png': 'gmaxpath32.png',
    "insanity'sreadmegenerator16.png": 'isrmg16.png',
    "insanity'sreadmegenerator24.png": 'isrmg24.png',
    "insanity'sreadmegenerator32.png": 'isrmg32.png',
    "insanity'srng16.png": 'isrng16.png', "insanity'srng24.png": 'isrng24.png',
    "insanity'srng32.png": 'isrng32.png', 'randomnpc16.png': 'isrnpcg16.png',
    'randomnpc24.png': 'isrnpcg24.png', 'randomnpc32.png': 'isrnpcg32.png',
    'interactivemapofcyrodiil16.png': 'map16.png',
    'interactivemapofcyrodiil24.png': 'map24.png',
    'interactivemapofcyrodiil32.png': 'map32.png',
    '3dsmax16.png': 'maxpath16.png', '3dsmax24.png': 'maxpath24.png',
    '3dsmax32.png': 'maxpath32.png', 'maya16.png': 'mayapath16.png',
    'maya24.png': 'mayapath24.png', 'maya32.png': 'mayapath32.png',
    'notepad++16.png': 'npp16.png', 'notepad++24.png': 'npp24.png',
    'notepad++32.png': 'npp32.png',
    'oblivionfaceexchangerlite16.png': 'obfel16.png',
    'oblivionfaceexchangerlite24.png': 'obfel24.png',
    'oblivionfaceexchangerlite32.png': 'obfel32.png',
    'modlistgenerator16.png': 'obmlg16.png',
    'modlistgenerator24.png': 'obmlg24.png',
    'modlistgenerator32.png': 'obmlg32.png',
    'paint.net16.png': 'paintnet16.png', 'paint.net24.png': 'paintnet24.png',
    'paint.net32.png': 'paintnet32.png',
    'paintshopprox316.png': 'paintshopphotopro16.png',
    'paintshopprox324.png': 'paintshopphotopro24.png',
    'paintshopprox332.png': 'paintshopphotopro32.png',
    'photoshop16.png': 'photoshoppath16.png',
    'photoshop24.png': 'photoshoppath24.png',
    'photoshop32.png': 'photoshoppath32.png',
    'pixelstudiopro16.png': 'pixelstudio16.png',
    'pixelstudiopro24.png': 'pixelstudio24.png',
    'pixelstudiopro32.png': 'pixelstudio32.png',
    'radvideotools16.png': 'radvideo16.png',
    'radvideotools24.png': 'radvideo24.png',
    'radvideotools32.png': 'radvideo32.png',
    'tes4files16.png': 'tes4filespath16.png',
    'tes4files24.png': 'tes4filespath24.png',
    'tes4files32.png': 'tes4filespath32.png'
}

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[bd0a8972b0...](https://github.com/wrye-bash/wrye-bash/commit/bd0a8972b0cb66091a2943d0f23b75d89e94c576)
#### Friday 2023-11-03 22:59:06 by MrD

Merge branch 'ut-366-image-570-launchers' into 190-lazy-de-wx:

Making ImageWrapper -> GuiImage(Lazy) made possible to centralize
image handling and finalize the app_buttons refactoring. Highlights:

- global balt.images is dropped - encapsulated into _gui_globals and
accessors defined. The latter will be put to more good use in lazy-pt2
- global bass.tooldirs is dropped. See commits for the gory details - in
short tooldirs, were populated to be checked once - in a horribly
complicated manner. Now we fish the keys from the ini JIT and use them
once, when the app_buttons dictionary is populated (this will change in
"WIP inisettings" commit to provisionally stash them in inisettings)
- we now instantiate *all* possible (predefied) status bar buttons, but
enable them per game solving an ancient TODO and at the same time
making settings portable between installs - this was a showstopper for

Future directions for #570:

- we should stop reading tool paths from the ini - instead specify those
from a settings page - ideally in 312 we read and warn and in 313 we
stop reading the ini
- same goes double for the App folder - read .lnk, populate the settings,
warn that App folder will be dropped in 313 then drop it

This will take down a few hacks and permit us to use the app_launcher
as the uid (no more app_key)

As for the images API - I think GuiImage will do. The weird logic is in
the _native_widget (property) overrides - sleek and ready for us to find
the one right way of instantiating the images, including maybe making
more svgs. Also there are some more uses of wx.image in `gui` that need
centralizing and a few loose ends in initialization (including the CI
hack or having a default fallbback image) but we can close #366, heavy
lifting is done the rest is low priority.

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[fb9c40f675...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/fb9c40f6752f19e293da244c45e48dabb9236320)
#### Friday 2023-11-03 23:49:40 by SpartanKadence

Jukebox Update (#6102)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This will add plenty of more songs to the Jukebox.

Song List:
Alternative:
Say It Ain’t So by Weezer
Buddy Holly by Weezer
The Good Life by Weezer
Troublemaker by Weezer
Undone by Weezer
Hash Pipe by Weezer (All Emagged)
Wayside by Mitchel Dae
Freaking Out the Neighborhood by Mac DeMarco

Arcade:
Skyline and Menagerie Mix by 63hnsh3
Deputized by Locknar
The Ashoka Attacks by Paul Ruskay

Electronic:
How Would You Like It? By Moxifloxi
Syrsa - Cythas - Magichnology
Beyond Memory by NINA

Jazz and Lounge:
People Equals Shit by Richard Cheese (Emagged)

Metal:
Alone I Break by Korn
Shoots and Ladders by Korn
Blind by Korn
A Different World by Korn ft. Corey Taylor
Kidnap the Sandy Claws by Korn (Emagged)
Before I Forget by Slipknot
Psychosocial by Slipknot
The Devil in I by Slipknot
Dead Memories by Slipknot
People Equals Shit by Slipknot
Fade Away by Breaking Benjamin
Give me a Sign by Breaking Benjamin
I Will Not Bow by Breaking Benjamin
Into the Nothing by Breaking Benjamin
Without You by Breaking Benjamin
Smooth Criminal by Alien Ant Farm
Movies by Alien Ant Farm
Happy Death Day by Alien Ant Farm
Violent Pornnography by System of a Down
Science by System of a Down
Spiders by System of a Down
Jet Pilot by System of a Down
Chic ‘n’ Stu by System of a Down
Chop Suey! by System of a Down
B.Y.O.B. by System of a Down
Last Resort by Papa Roach
Scars by Papa Roach
Words as Weapons by Seether
Crawling by Linkin Park
Leave Out All the Rest by Linkin Park
Papercut by Linkin Park
Lost by Linkin Park
In The End by Linkin Park
Bodies by Drowning Pool
Tear Away by Drowning Pool
I Don't Care by Apocalyptica ft. Adam Gontier
One by Metallica
Sad But True by Metallica
Wherever I May Roam by Metallica
Nothing Else Matters by Metallica
Master of Puppets by Metallica
Tenebre Rosso Sangue by Keygen Church (Emagged)
Simple Sight by Piercing Lazer (Emagged)
Order by Heaven Pierce Her (Emagged)

Classical and Orchestral:
One Final Effort by Martin O’Donnell
Never Forget by Martin O’Donnell

Rock:
8675309 Jenny Jenny by Tommy Tutone
I Love You Like An Alcoholic by The Taxpayers
Must Have Been The Wind by The Chalkeaters (Emagged)

_Yes, this list is very biased._
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

With the recent repair of the previous songs in the Jukebox, it would
seem to be a good idea to finally add more to the list, allowing for
more songs for players to choose from.


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
add: Added more songs to the Jukebox!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---

