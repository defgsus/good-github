## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-29](docs/good-messages/2023/2023-08-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,260,200 were push events containing 3,466,072 commit messages that amount to 271,680,128 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [StollD/linux-fedora](https://github.com/StollD/linux-fedora)@[8b9c1cc041...](https://github.com/StollD/linux-fedora/commit/8b9c1cc0418a43196477083e7082568e7a4c9418)
#### Tuesday 2023-08-29 00:02:12 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [KikoWen0/NebulaStation](https://github.com/KikoWen0/NebulaStation)@[74198373da...](https://github.com/KikoWen0/NebulaStation/commit/74198373dada9f9d9e7c01e0337ba8ef04447583)
#### Tuesday 2023-08-29 00:21:57 by GuillaumePrata

Fixes vents having "infinite" pressure caps. (#77686)

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

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[d1afd66508...](https://github.com/Hatterhat/tgstation/commit/d1afd66508ed3474ca6179d54294742bef531419)
#### Tuesday 2023-08-29 00:22:24 by san7890

The Curse Of The Slot Machine - Now Clone-less (#77841)

## About The Pull Request

Hey there,

I think it's commonly held that clone damage sucks and is overused. One
of the last places where it was in slot machine code as a type of
"immutable" damage that would cause you to die if you didn't leave and
get medical attention. It had a lot of silliness and I'm not sure if a
lot of it was meant to work the way it was, but here we are.

So, what's the changes?

* The Cursed Slot Machine will give you a status effect that will
"curse" you with repeated damage. After five curses, you get gibbed
(similar to the old behavior of the machine). Each curse has it's own
change to the status effect, with a lot of depth included. Let me know
if the fluff messages about the status effect change sucks, I think it's
neat though.
* A person with the curse will smoke. I wanted this to look a bit more
"steamy" or grey, but I think it's a decent way of communicating that
shit is fucked up with that dude.
* You also get a branded wound after your first failure at the slot
machine. Ouchers. Should get it looked at by a doctor.
* We also throw a nice screen alert and all of that jazz.
* I also cleaned up all of the code relating to the slot machine
(including a stupid double and), and did some tinkering with the status
effects framework to get the desired effect I wanted. I hope you enjoy
it as much as I did making it. We use cooldowns and stuff between slot
machine pulls.
* If _anyone_ wins on the slot machine, all curses/brands are lifted.
Lucky jackpot!
* A lot of the stuff in this code has a lot of vars that might not be
modified codewise in case admins still want to jank with this for
events.
## Why It's Good For The Game

Clone damage stinks, and I don't really like it as a way to subvert the
whole "oh you can't use legion cores to get your way". It's a cursed
slot machine, and it should do long term damage so that even if you
expend all of the resources on the station, it might all be for naught.
It's a horrible price to pay in your search for that d20. I think the
negative side effects are pretty OK as far as balance, earlier
iterations of this concept had you die _way_ too fast.

All in all, it's just way more of an interesting interaction than "you
take damage and then go to medbay and then come back in the hopes of
gambling a d20".
## Changelog
:cl:
add: The Lavaland Cursed Slot Machine of Greed suddenly seems a lot more
sinister...
refactor: Instead of taking clone damage from the cursed slot machine,
you now get a status effect with a number of curses associated with it.
There's some interesting florid language associated with the status
effect as a nicety until your eventual gibbing from chasing that prize.
/:cl:

I remain undecided if I should keep the curse limit uncapped (but have
the damages increase rapidly after the 5-curse threshold), so I left it
as the `gib()` from the old code. Let me know your thoughts, but I
really don't like the thought that getting the fabled d20 is easy.

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[71d75632d3...](https://github.com/TaleStation/TaleStation/commit/71d75632d3c845101470805edda98102b04ef674)
#### Tuesday 2023-08-29 00:26:45 by TaleStationBot

[MIRROR] [MDB IGNORE] Light eater is now indestructible (#7503)

Original PR: https://github.com/tgstation/tgstation/pull/77903
-----
## About The Pull Request

This means a nightmare going into an emagged recycler will no longer be
fucked by their lack of a light eater.
Oh yeah, also moved the ACID_PROOF flag to the correct bitflag.
## Why It's Good For The Game

Bugfix good, you're not supposed to be able to delete an external limb
generated by an internal one, such as implants and such. Pretty sure
reimplanting the heart would make the light eater reappear, too, but
that's night impossible to get done as a nightmare.
## Changelog
:cl:
fix: Light eaters can no longer be eaten by their higher-grade brothers,
the trash eaters. (recyclers)
/:cl:

---------

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[b34be330be...](https://github.com/TaleStation/TaleStation/commit/b34be330be1eec9a9deb284bb79d5a30f516b371)
#### Tuesday 2023-08-29 00:28:34 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes vents having "infinite" pressure caps. (#7516)

Original PR: https://github.com/tgstation/tgstation/pull/77686
-----

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
## Changelog
:cl: Guillaume Prata
fix: Unary vents have a pressure cap on both their pressuring and
siphoning mode now, preventing the bypass trick of putting "infinite"
pressure on tiles/pipelines.
balance: Overclocked Volume Pumps do not have a pressure cap anymore.
/:cl:

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [Lufferly/tgstation](https://github.com/Lufferly/tgstation)@[0dd3e66aef...](https://github.com/Lufferly/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Tuesday 2023-08-29 00:55:13 by Vekter

Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [GySgtMurphy/Citadel-Station-13-RP](https://github.com/GySgtMurphy/Citadel-Station-13-RP)@[7d600bf36a...](https://github.com/GySgtMurphy/Citadel-Station-13-RP/commit/7d600bf36a691d4be27e852eed0106a1564d7aee)
#### Tuesday 2023-08-29 01:22:29 by TheObserver-sys

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
## [holub/mame](https://github.com/holub/mame)@[dbb0909cba...](https://github.com/holub/mame/commit/dbb0909cbab3f2094088a42687894e0e6053986b)
#### Tuesday 2023-08-29 01:23:24 by wilbertpol

msx1_flop.xml: Added 105 working items, and replaced one item. (#11511)

* Replaced Konami Game Collection 3: Shooting Series (Japan) with a better dump. [file-hunter]

New working software list items (msx1_flop.xml)
-------------------------------
10 Programas Serie Oro (Spain) [file-hunter]
20 Programas Serie Oro (Spain) [file-hunter]
747 400b Flight Simulator (Europe, cracked) [file-hunter]
Alfabet en Deelsom (Netherlands) [file-hunter]
Alien Panic (Spain) [file-hunter]
Andon (Japan, hacked) [file-hunter]
Duad-MSX (Japan) [file-hunter]
Engels + Procenten (Netherlands) [file-hunter]
Fracta (Brazil) [file-hunter]
Graphos III (Brazil) [file-hunter]
Gruta de Maquine (Brazil)
The Iron Gauntz (Japan, prototype) [file-hunter]
Konami Game Collection 1: Action Series (Japan, alt) [file-hunter]
Konami Game Collection 4: Sports Series 2 (Japan, alt) [file-hunter]
Lettergrijper + Geld (Netherlands) [file-hunter]
Manuscript (United Kingdom) [file-hunter]
MSX Compilation 5 (Netherlands) [file-hunter]
MSX PageMaker DeLuxe (Brazil) [file-hunter]
Music Creator (Netherlands) [file-hunter]
Professional Data Retrieve (Brazil) [file-hunter]
Professional Paint (Brazil) [file-hunter]
Professional Publisher (Brazil, cracked) [file-hunter]
Rekenen tot 20 + Optellen en aftrekken tot 100 + Taalbedrijf (Netherlands) [file-hunter]
SF Zone 1999 (Japan) [file-hunter]
Simulador Profesional de Tenis (Spain) [file-hunter]
Super Procole (Japan) [file-hunter]
Super Procole 2 (Japan) [file-hunter]
Super Procole 3 (Japan) [file-hunter]
Supersellers 1 (Netherlands) [file-hunter]
Twin Hammer (Korea) [file-hunter]
The Wood (Spain) [file-hunter]
Woordmaker en Cijferend Vermenigvuldigen (Netherlands) [file-hunter]
Word Plus (Brazil) [file-hunter]
Wordstore+ (Netherlands) [file-hunter]
Zen (United Kingdom) [file-hunter]
3D Maze [Chalky]
666 - Uma Aventura Macabra [file-hunter]
8192 Story Tower [NAGI-P SOFT]
Baruko [file-hunter]
Blinky's Scary School [file-hunter]
Bounce Mania [MSXdev]
Burner Burst [file-hunter]
Buster Mystery [file-hunter]
City (Japan) [file-hunter]
Defence (v1.3) [MSXdev]
Galaxy Zone [aburi6800]
Ghosts'n Goblins (v1.1.0) [file-hunter]
Hibernated 1 - This Place is Death [file-hunter]
Hibernated 1 - Eight Feet Under [file-hunter]
JUMPER [NAGI-P SOFT]
Kame Graphics [file-hunter]
Kill Mice [MSXdev]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
Las Aventuras de Rudolphine Rur (Spanish, xmessage) [Dwalin]
Last War [NAGI-P SOFT]
Last War II [NAGI-P SOFT]
Logic (Russia) [file-hunter]
Mars [NAGI-P SOFT]
Mars II [NAGI-P SOFT]
May The Force Be With You [Cobinee]
Maze Chase [JLTurSan]
Micro Rocketz [MSXdev]
Mood Land [file-hunter]
Muhonmourn 3 (v1.1) [MSXdev]
Muhonmourn 3 (v1.1, with Ninja Tap support) [file-hunter]
Muhonmourn 3 (v1.0) [file-hunter]
Nibbles [file-hunter]
Oceano [file-hunter]
Paint-it (rev2) [file-hunter]
Paint-it (rev1) [file-hunter]
Paint-it [file-hunter]
Palhada City (Brazil) [file-hunter]
Penguin Catcher (v1.1) [MSXdev]
Penguin Catcher (v1.0) [file-hunter]
Pyramid Quest [Crappysoft]
Raftoid [PlattySoft]
Roger Dice (Spain) [oniric-factor]
Search for Mum (Netherlands) [file-hunter]
Sim City [file-hunter]
Storm Rescue [Concurso MSX-BASIC]
Stripgirl [file-hunter]
SubCommander (v1.02) [MSXdev]
SubCommander (older) [file-hunter]
Super Adventure [file-hunter]
The Tower of Gold [MSXdev]
UZIX (v1.0.0) [UZIX]
Wash Man (v2.8) [MSXdev]
Wash Man (v1.9) [file-hunter]
Wash Man (v1.5) [file-hunter]
Wash Man (v1.3) [file-hunter]
Wash Man (v1.2) [file-hunter]
Wash Man (v1.1) [file-hunter]
Wash Man (v1.0) [file-hunter]
Wired Shooting [Cobinee]
MSXMAS Demo [file-hunter]
Xadrama [file-hunter]
Xarchon [file-hunter]
XOR [Chalky]
XOR (older) [file-hunter]
Yellow Submarin [file-hunter]
Yobai [file-hunter]
Zero Gravity [file-hunter]
The zoBITRONics Inc [Hannu Töyrylä]
Zone TNT [MSXdev]
La Abadia del Crimen (Spain, alt) [file-hunter]

---
## [bushrat011899/bevy](https://github.com/bushrat011899/bevy)@[44f677a38a...](https://github.com/bushrat011899/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Tuesday 2023-08-29 01:28:17 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [DamrongGuoy/drake](https://github.com/DamrongGuoy/drake)@[f90899e13f...](https://github.com/DamrongGuoy/drake/commit/f90899e13fd6b703ac5c7da3d1b7c0584a793769)
#### Tuesday 2023-08-29 02:28:27 by Jeremy Nimmer

[geometry] Add Meshcat::GetRealtimeRate (#19700)

Tidy up recent Meshcat changes:
- Add missing pydrake bindings.
- Strongly prefer testing the public API (eschew test-friendship hacks).
  We want to guard against regressions in the end-user experience;
  using private API goes against that goal.
- Fix indentation, typos, and eschew abbreviation.

---
## [Trilbyspaceclone/lobotomy-corp13](https://github.com/Trilbyspaceclone/lobotomy-corp13)@[171b1478f9...](https://github.com/Trilbyspaceclone/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Tuesday 2023-08-29 02:36:50 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [Offroaders123/Region-Types](https://github.com/Offroaders123/Region-Types)@[8524c9bb54...](https://github.com/Offroaders123/Region-Types/commit/8524c9bb5431bd173425cc294ee55df1ba5b8d10)
#### Tuesday 2023-08-29 02:38:37 by Offroaders123

No-Enums

Ok, I'll give them that! Enums are definitely really nice to use. They have some drawbacks in my opinion when using them at the type-level though, so I'm gonna go back to my `{} as const` enum-ish union type method.

Funny timing to see @MichiganTypeScript post a new video about this, after having been discussing this recently in the @Minecraft-Manipulator group.

https://www.youtube.com/watch?v=XTXPKbPcvl4 (New enums video)
https://www.youtube.com/watch?v=0fTdCSH_QEU (I think this was the original inspiration for my use of the `{} as const` method.)

This might be a backwards step in relation to #2, but I can come back to that later once the types are more established as a whole. It's still a thing to think about, consider, and brainstorm for though! I definitely want to have that kind of thing be possible.

---
## [thecsw/thecsw.github.io](https://github.com/thecsw/thecsw.github.io)@[1ef0e25713...](https://github.com/thecsw/thecsw.github.io/commit/1ef0e25713133f35a7373df916c921854ac87c3f)
#### Tuesday 2023-08-29 02:51:49 by Ubuntu

[ASTRIE] Added a new fortune: ** 186; 12023 H.E.

Okay, asking somebody how long they believed in Santa Claus is so stupid, you can't even consider the topic suitable for idle conversation. But if you still wanna know how long I believed in some old fat guy who wears a funky red suit, I can tell you this: I've never believed in him, ever. The Santa that showed up at my kindergarten Christmas festival, I knew he was fake. And I never saw mommy kissing Santa or anything. But I have to say, that even as a little kid, I knew better than to believe in some old man that only worked one day a year. Now, having said that, it wasn't until I got older that I realized that aliens, time travelers, ghosts, monsters, espers, the evil syndicates and the anime/manga/fantasy flick heroes that fight said evil syndicates, were also fake. Okay, I guess I always knew those things were bogus, I just didn't wanna admit it. All I ever wanted was for an alien, time traveler, ghost, monster, esper, evil syndicate, or the hero that fought them to just appear and say "Hey". Unfortunately, reality is a hard road indeed. Yep, you gotta admit, the laws of physics definitely puts a damper on things. I even stopped watching those TV shows about aliens and ghosts and stuff. Aliens, time travelers, espers; of course they don't exist, but a little part of me wishes that they did. I guess I've grown up and realized I can think about those things and still accept reality. But by the time I got out of junior high, I pretty much outgrew that kind of stuff and I guess I got used to the idea of living in an ordinary world. Just like that, I was in high school...that's when I met her.

— Kyon, /The Melancholy of Haruhi Suzumiya/

---
## [Koshenko/tgstation](https://github.com/Koshenko/tgstation)@[1e27ce031b...](https://github.com/Koshenko/tgstation/commit/1e27ce031ba94161c64edcc87e5f3aaad778d3fe)
#### Tuesday 2023-08-29 02:56:16 by carlarctg

Syndicate Duffelbag Rerework (#77060)

## About The Pull Request

Syndicate duffelbags can fit 2 extra bulky items, down from three.

Reduced syndicate duffelbag's unzipped slowdown from '1' to '0.3', and
set its zipping-up sped to 0.5, same as unzipping.

Added the following items to the Syndicate Duffelbag bulky exception
list: Greentext, mech removal tool, gibtonite, skub, golem shells, mech
ammo. Roughly sorted the list by item category.

Fixed the syndie surgery duffelbag having more items than it can hold by
removing the redundant surgical drill (Upgraded cauteries can turn into
one anyways)

Any storage item with a can_hold description can be examined twice to
see what it can hold now.

## Why It's Good For The Game

> Syndicate duffelbags can fit 2 extra bulky items, down from three.

> Reduced syndicate duffelbag's unzipped slowdown from '1' to '0.3', and
set its zipping-up sped to 0.5, same as unzipping.

For most intents and purposes, it seems the syndicate duffelbag has gone
from 'bland upgrade to backpack', to 'useless'. This is especially made
apparent because it isn't exactly shown to the player that these
duffelbags can carry bulky items (I didn't even know about it until I
was making this PR!)

The extra bulky item hold concept is great, but I have my issues with
the item as-is that I seek to fix with this PR. There are TONS of issues
with being unable to access your bag quickly, which is twice as relevant
when your bag is an incredibly conspicious traitor item. Sure, you can
have it in your hand, but then why even have it in the first place?

That's why I want to reduce the slowdown significantly. '1' slowdowns
are thrown around the whole game like they're reasonable (galoshes,
water back-tanks, biosuits) - they aren't. '1' slowdown is CRIPPLING. It
makes you frustratingly slow and effectively destroys any combat
maneuvering you can do. This is very relevant for a traitorious item.

The zip speed helps one use the duffelbag as a storage item dynamically,
letting the item be an actual trade-off rather than mostly a downside.
Gives you a reason to use it rather than just buying a smuggler satchel
for more storage.

Of course these are some hefty buffs, so I lowered the bulky storage to
make up for it. I can bring it back up to 3 if wanted.

> Added the following items to the Syndicate Duffelbag bulky exception
list: Greentext, mech removal tool, gibtonite, skub, golem shells, mech
ammo. Roughly sorted the list by item category.

Some traitorious items that felt like they should be allowed in.
Honestly, I think this shouldn't even be an exception hold except for
blacklisting clearly bonkers things like backpacks, but whatevs.

> Any storage item with a can_hold description can be examined twice to
see what it can hold now.

Generalization is awesome. Hardcoding is cringe!

## Changelog

:cl:
balance: Syndicate duffelbags can fit 2 extra bulky items, down from
three.
balance: Reduced syndicate duffelbag's unzipped slowdown from '1' to
'0.3', and set its zipping-up sped to 0.5, same as unzipping.
add: Added the following items to the Syndicate Duffelbag bulky
exception list: Greentext, mech removal tool, gibtonite, skub, golem
shells, mech ammo. Roughly sorted the list by item category.
fix: Fixed the syndie surgery duffelbag having more items than it can
hold by removing the redundant surgical drill (Upgraded cauteries can
turn into one anyways)
qol: Any storage item with a can_hold description can be examined twice
to see what it can hold now.
fix: The parent crayon's name is 'crayon' to prevent any weirdness with
things that show the parent type's name.
/:cl:

---
## [Koshenko/tgstation](https://github.com/Koshenko/tgstation)@[d875610098...](https://github.com/Koshenko/tgstation/commit/d875610098a1259a5112d4a0e5afc0b7bd32ff6d)
#### Tuesday 2023-08-29 02:56:16 by Rhials

[NO GBP] Fixes clown car + deer collision  (#77076)

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

---
## [JohnFulpWillard/Yogstation](https://github.com/JohnFulpWillard/Yogstation)@[9db2f06363...](https://github.com/JohnFulpWillard/Yogstation/commit/9db2f06363bc325a0e8eadfdf7266e55def4d7c1)
#### Tuesday 2023-08-29 02:59:20 by Scrambledeggs

Fuck you *Ungreens your Peacekeepers* (#20053)

* Sprites Part 1: I hate transparency

* Sprites Part 2: Electric Booogaloo

* lack of transparency fixed

* More sprite fixes

* Tacmask and sprites

* Tacprod inactive and nocell sprites

* Tacprod Animation Part 1: Bugs galore

* Tacprod Animation Part 2: Tacmask revengance

* white beret

---
## [nik1097/langchain](https://github.com/nik1097/langchain)@[d57d08fd01...](https://github.com/nik1097/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Tuesday 2023-08-29 03:55:07 by nikhilkjha

Initial commit for comprehend moderator (#9665)

This PR implements a custom chain that wraps Amazon Comprehend API
calls. The custom chain is aimed to be used with LLM chains to provide
moderation capability that let’s you detect and redact PII, Toxic and
Intent content in the LLM prompt, or the LLM response. The
implementation accepts a configuration object to control what checks
will be performed on a LLM prompt and can be used in a variety of setups
using the LangChain expression language to not only detect the
configured info in chains, but also other constructs such as a
retriever.
The included sample notebook goes over the different configuration
options and how to use it with other chains.

###  Usage sample
```python
from langchain_experimental.comprehend_moderation import BaseModerationActions, BaseModerationFilters

moderation_config = { 
        "filters":[ 
                BaseModerationFilters.PII, 
                BaseModerationFilters.TOXICITY,
                BaseModerationFilters.INTENT
        ],
        "pii":{ 
                "action": BaseModerationActions.ALLOW, 
                "threshold":0.5, 
                "labels":["SSN"],
                "mask_character": "X"
        },
        "toxicity":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        },
        "intent":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        }
}

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

response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})

print(response['output'])


```
### Output
```
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii validation...
Found PII content..stopping..
The prompt contains PII entities and cannot be processed
```

---------

Co-authored-by: Piyush Jain <piyushjain@duck.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Bagatur <baskaryan@gmail.com>

---
## [j-sherrick/integra-tech](https://github.com/j-sherrick/integra-tech)@[d0f9a9407c...](https://github.com/j-sherrick/integra-tech/commit/d0f9a9407cec304a538341120df4a74ae94029d0)
#### Tuesday 2023-08-29 05:05:49 by Jason Sherrick

is trying to fix this ignorecase bug (fuck you Windows)

---
## [Taniya62/Power-Bi](https://github.com/Taniya62/Power-Bi)@[853abb3265...](https://github.com/Taniya62/Power-Bi/commit/853abb3265372330c627b5c6cf3be737689c7c71)
#### Tuesday 2023-08-29 05:59:40 by Taniya Das

Add files via upload

Hey 👋 I'm thrilled to share that I've been diving deep into Power BI and recently crafted a powerful dashboard using DAX queries. 📈🔍

In a world flooded with data, transforming raw numbers into actionable insights is a game-changer. With the magic of DAX (Data Analysis Expressions), I've harnessed the true potential of Power BI to deliver a dynamic dashboard that unveils trends, patterns, and invaluable information.

🔥 What's Hot about the Dashboard:
1. **Interactive Visuals**: The dashboard isn't just a bunch of static graphs. It's a living, breathing tool that responds to your clicks and queries, letting you explore the data from multiple angles.
2. **Data-driven Decisions**: By using DAX queries, I've created calculated columns and measures that distill complex data into easy-to-understand metrics. This helps in making informed decisions faster than ever.
3. **User-friendly Interface**: I've put extra effort into designing an intuitive interface. Navigating through the dashboard is as smooth as slicing a cake!

I'm passionate about data-driven decision-making, and this dashboard is a testament to that passion. If you're interested in seeing how insights can be brought to life through data visualization and DAX wizardry, I'd be delighted to share a sneak peek with you.

---
## [Dokati/Predictions](https://github.com/Dokati/Predictions)@[8124493170...](https://github.com/Dokati/Predictions/commit/81244931703c82bb60fe729de0b15dfce4399136)
#### Tuesday 2023-08-29 07:11:13 by Dor katirachi

Merge pull request #2 from patrisiakaplun/patrisiaka

Fuck you Dor

---
## [venkateshmungi/venkateshmungi](https://github.com/venkateshmungi/venkateshmungi)@[fb26ef3c29...](https://github.com/venkateshmungi/venkateshmungi/commit/fb26ef3c291465e20541c68ebed692430942b1ca)
#### Tuesday 2023-08-29 07:16:20 by venkatesh_mungi

Update README.md

Data Scientist with two years of broad-based experience in building data-intensive applications, overcoming complex architectural, and scalability issues in diverse industries. Proficient in predictive modeling, data processing, Natural Language Processing, data mining algorithms, as well as scripting language, Python. Capable of creating, developing, testing, and deploying highly adaptive diverse services to translate business and functional qualifications into substantial deliverables.

Junior Data Scientist
SocialTek AI ML Business solutions Pvt Ltd, Hyderabad.				          Sep 2021 – Present

•	Collected and processed data from diverse sources, ensuring data quality and consistency. 
•	Employed effective data cleaning techniques, performed feature engineering, and conducted exploratory data analysis to prepare data for predictive modelling and natural language processing (NLP) tasks.
•	Developed and implemented machine learning models using programming languages such as Python and leveraged libraries including Scikit-learn, NLTK, TensorFlow, Keras and PyTorch. Applied these models to derive insights and make data-driven decisions.
•	Develop action plans to mitigate risks in decision making while increasing profitability by leveraging data science.
•	Conducted experiments to assess model performance and iteratively enhanced accuracy through techniques like hyperparameter tuning and ensembling. Ensured that models met specified requirements and were optimized for superior performance.
•	Collaborated closely with cross-functional teams, including product managers, software engineers, and data analysts. Effectively communicated and understood business requirements, contributing to the development of innovative solutions that met client needs.

---
## [malikayan827/Machine-Learning-and-Datasciences-using-python](https://github.com/malikayan827/Machine-Learning-and-Datasciences-using-python)@[70f9a59fd5...](https://github.com/malikayan827/Machine-Learning-and-Datasciences-using-python/commit/70f9a59fd567d62a4f11e64a7c78551a59dc55d4)
#### Tuesday 2023-08-29 07:34:51 by Muhammad Ayan

Emotion Detector  App

The Emotion Detection Web Application is a Python-based project that leverages IBM Watson's Natural Language Processing (NLP) capabilities to analyze and predict emotions from text input provided by users. The application provides a user-friendly interface where users can enter text statements, and the system uses the Watson NLP library to determine the emotions associated with the input. The project involves the creation of a Flask-based web application that serves as an interface to interact with the Watson NLP service.

Key Features:

Emotion Analysis: The core functionality of the application is to analyze the emotions expressed in the text input. The application uses the Emotion Predict function of the Watson NLP library to provide insights into emotions like anger, disgust, fear, joy, and sadness.

User-Friendly Interface: The project includes a user interface that allows users to input text statements. The application then processes the input and displays the emotions detected, along with the dominant emotion.

Error Handling: The application incorporates error handling to manage blank entries. If a user submits an empty input, the system provides an error message indicating that the text input is invalid and prompts the user to try again.

Display of Results: The application displays the detected emotions along with their respective scores and identifies the dominant emotion. The results are presented in a user-friendly format, enhancing user understanding.

Web Deployment: The project utilizes the Flask framework to create a web server that hosts the emotion detection application. The application is deployed locally on localhost:5000, enabling users to access and use the tool through a web browser.

Static Code Analysis: The project ensures code quality by conducting static code analysis using tools like PyLint. This helps maintain clean and well-structured code.

Testing: The application is thoroughly tested for various input scenarios, including both valid and blank inputs, to ensure that the error handling and emotion detection functionalities work as intended.

The Emotion Detection Web Application showcases the integration of IBM Watson's NLP capabilities with a user-friendly web interface. The project's key focus on error handling, result presentation, and code quality makes it a practical tool for anyone interested in exploring the emotions expressed in text. Whether for personal use or as a starting point for more advanced emotion analysis applications, this project provides valuable insights into the realm of natural language processing and sentiment analysis.

---
## [kirillzyusko/react-native-keyboard-controller](https://github.com/kirillzyusko/react-native-keyboard-controller)@[84f94eb639...](https://github.com/kirillzyusko/react-native-keyboard-controller/commit/84f94eb6393e930b9debe75d2a763c523e02d130)
#### Tuesday 2023-08-29 08:19:50 by Kirill Zyusko

refactor: react on tag changes (#216)

## 📜 Description

Improved `KeyboardAwareScrollView` example - now it react on `TextInput`
focus changes 🙂

## 💡 Motivation and Context

I highlighted key changes below:

### Interpolation depends on previous keyboard size

Before it was a fixed number (0). But since the size of the keyboard can
be different per different `TextInput` types - we have to interpolate
value from previous keyboard size to the new one. Otherwise the
animation when keyboard changes its size looks slightly ugly (will have
a jump in beginning).

Just as an example let's imagine, that the keyboard is changing size
from `200` to `300` and you need to scroll from `100` to `200`. The
current scroll position is `100` and you interpolate as before from 0 to
300. In this case, when keyboard size grows from 200 to 300 first
scrollTo will scroll to ~160. So 60% of the smooth transition will be
missed 😔

If we interpolate from `previousKeyboardSize`, then we will interpolate
from `200` to `300` (as expected) and we'll have a smooth transition for
all distance.

### Assure `TextInput` is not overlapped by `Keyboard` in `onEnd`
handler

Sometimes `onMove` handler can be missed. It happens in two cases:
- on iOS when TextInput was changed - keyboard transition is instant and
`onMove` will not be triggered;
- on Android when TextInput was changed and keyboard size wasn't
changed.

To handle these cases I've decided to run `scrollTo` in `onEnd` handler.
For plain transition it will not have any effect, because scroll
position already will be as the desired one.

However for cases above it'll handle TextInput focus changes and will
assure, that the `TextInput` is always above the Keyboard 🙂

### Back transition

To assure smooth back transition I've introduced
`scrollBeforeKeyboardMovement` (updated whenever `TextInput` becomes a
focus). Later this variable is used in interpolation, when keyboard
hides.

Also I do a layout substitution in `onEnd` handler:

```tsx
const prevLayout = layout.value;
layout.value = measureByTag(e.target);
// ...
layout.value = prevLayout;
```

This is needed because we need to remember "initial layout" (before
keyboard movement) in order to perform beautiful back transition.

> I'm more than sure, that this implementation is not perfect and still
has some bugs (it is still not clear how to handle a case, when you
scroll TextInput off-screen (under keyboard or under header - which back
transition do we need to apply in this case?)). But it resolves some of
the problems that were reported and shows how to use new API of the
library. So in order to unlock a release process I'm leaving this
implementation as is - maybe later I'll come up with more sophisticated
approach which will handle even more cases, but for now as an example
it's good to go.

## 📢 Changelog

### JS
- added documentation for `KeyboardAwareScrollView` describing the flow
of execution;
- removed combination of `useWorkletCallback` + direct `worklet`
directive;
- interpolate transition based
- run additional `scrollTo` in `onEnd` handler to assure that there will
be no overlap with `TextInput` and `Keyboard` - handles a case when
focus changed, but keyboard size was not changed;
- removed `console.log` that were used for debugging 🙂 

## 🤔 How Has This Been Tested?

Tested manually on:
- iPhone 14 Pro;
- Pixel 7 Pro;

## 📸 Screenshots (if appropriate):

|Before|After|
|------|-----|
|<video
src="https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/f9e41c28-0082-4dad-8495-57e48ee97c74">|<video
src="https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/c43d85ce-0cdb-4bc6-b269-895e3e094ad8">|

## 📝 Checklist

- [x] CI successfully passed

---
## [pulumi/pulumi](https://github.com/pulumi/pulumi)@[3d9ddb2981...](https://github.com/pulumi/pulumi/commit/3d9ddb2981016dbdfa7ff4293b2eb814e9d11ce1)
#### Tuesday 2023-08-29 08:21:13 by Fraser Waters

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
## [Spookuni/tgstation](https://github.com/Spookuni/tgstation)@[72174845f5...](https://github.com/Spookuni/tgstation/commit/72174845f5b417bf0cbd3f4a8fc66835b052acf8)
#### Tuesday 2023-08-29 08:47:37 by Jacquerel

Basic Watchers & Basilisks (#77630)

## About The Pull Request

This one is a double feature because Watchers and Basilisks share the
same typepath. You might see a couple more of those.
As is tradition I decided to fuck with them rather than just port them.
Here's what's up.

**Basilisks**

![image](https://github.com/tgstation/tgstation/assets/7483112/9e4b0115-65dd-4df7-b62a-21c7be8549bf)

![image](https://github.com/tgstation/tgstation/assets/7483112/59162e68-7d73-4659-9531-5078ff751228)

- Have a new soulless sprite which looks less like a living blue hedge.
- Walk at you and shoot you while you are not in range (just like
before).
- Become supercharged if they become "heated" by lava, lasers, or
temperature weapons. This was a feature they also previously had but
they would never encounter lava, so now it also works if you use the
wrong gun on them.
- Lose their supercharge if you cool them down.
- Otherwise pretty normal mobs.

**Watchers**

https://www.youtube.com/watch?v=kOq_Bf78k5A
Here's a traditional video of me intentionally getting hit by mechanics
(trust me its definitely on purpose)

- They glow emmissively a little bit so you can see them from further
away.
- Their eyes light up about 0.5 seconds before they are able to shoot at
you.
- No longer melee attack, instead try to stay out of melee.
- Will occasionally put you into "Overwatch", meaning they will shoot
you rapidly if you move or act while they're staring at you for a brief
time period (after which you become immune for 12 seconds, and during
which other watchers will play fair and stop shooting at you).
- If they start taking damage they will also start using their "Gaze"
attack, look away or suffer some kind of negative effect!
- - Normal watcher gaze flashes and confuses you.
- - Magmawing watcher gaze obviously burns (and briefly stuns) you.
- - Icewing watcher gaze freezes you and throws you backwards.
- Magnetically attract and eat diamonds. They also used to do this, but
just if they happened to coincidentally walk past some.

**Other accompanying changes**

All basic mobs will now adopt the "stop gliding" trait if they get
slowed down too much.
I moved behaviour for "fire a projectile from this atom" into a helper
proc because I was using it in three places and I will probably use it
in more places. There are probably other places in the existing code
which could be using this.
I think I made the basic mob melee attack forecast default a little more
forgiving, they were fucking me up too much and I am the playtester.

## Why It's Good For The Game

Another one off the list.
New tricks for old dogs.
Framework for making mobs with ranged attacks "fairer" (you can see when
they are ready to shoot you).
More (hopefully) versatile AI behaviours which we will reuse later (I
hope I'm not duplicating one someone already made).
If our players "enjoy" them enough we can give more mobs "don't look at
me" mechanics.
Removes some soul sprites.

## Changelog

:cl:
refactor: Basilisks and Watchers now use the basic mob framework. Please
bug report any unusual behaviour.
sprite: Basilisks have new sprites.
add: Basilisks will go into a frenzy if heated by energy weapons or
temperature beams as well as by lava.
add: Watcher eyes will be illuminated briefly when they are ready to
fire at you.
add: Watchers can now briefly put you into "Overwatch" and penalise you
for moving while they can see you.
add: Wounded watchers will occasionally punish players who look at them.
balance: Unusual watcher variants are more likely to appear.
/:cl:

---
## [IamWAITINGforYOUsanju/CosmoMC](https://github.com/IamWAITINGforYOUsanju/CosmoMC)@[abe7bfa2b3...](https://github.com/IamWAITINGforYOUsanju/CosmoMC/commit/abe7bfa2b357ec0c0129af16ab923b11516905fe)
#### Tuesday 2023-08-29 09:01:15 by IamWAITINGforYOUsanju

Create You're all I want in this life. Can we please talk? 

Please understand

---
## [2002jai/ComprehensiveFeatureSelectionTests](https://github.com/2002jai/ComprehensiveFeatureSelectionTests)@[09239e2be3...](https://github.com/2002jai/ComprehensiveFeatureSelectionTests/commit/09239e2be33c42c48f38509fd68345b421693ddd)
#### Tuesday 2023-08-29 10:09:28 by jai chauhan

ComprehensiveFeatureSelectionTests

Dive into the world of comprehensive feature selection techniques with our GitHub repository, "ComprehensiveFeatureSelectionTests." This repository serves as a valuable resource for both beginners and experienced practitioners in the field of machine learning and data analysis. Feature selection is a critical step in building effective and efficient models, and our repository covers a wide array of topics to provide a holistic understanding of this process.

Inside this repository, you'll find implementations of various feature selection methods, including filter, wrapper, embedded, and hybrid approaches. We offer hands-on examples and experiments that showcase the practical application of these techniques on diverse datasets. Whether you're working with text, image, time series, or other types of data, we provide domain-specific considerations to tailor your feature selection strategies.

Visualization is key to understanding feature importance and selection outcomes. We offer a variety of visualization tools, such as plots and graphs, to help you gain insights into your feature selection results. Additionally, we address the challenges of high-dimensional data and provide insights into managing the curse of dimensionality.

For those interested in automation, our repository explores automated feature selection methods and their integration into machine learning pipelines. Our collection of real-world datasets is an invaluable asset for testing and fine-tuning your feature selection techniques. Tutorials and Jupyter notebooks provide step-by-step guidance, empowering you to implement these methods effectively.

Contributors are welcomed to expand the repository by adding new techniques, experiments, and improvements. By maintaining best practices and offering clear guidelines, we aim to foster a collaborative environment that advances the field of feature selection. Unlock the potential of your machine learning models with "ComprehensiveFeatureSelectionTests." Start exploring and contributing today!

---
## [hoxyq/react](https://github.com/hoxyq/react)@[ac1a16c67e...](https://github.com/hoxyq/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Tuesday 2023-08-29 10:11:00 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [qiracy/FMHYedit](https://github.com/qiracy/FMHYedit)@[5fa2298307...](https://github.com/qiracy/FMHYedit/commit/5fa22983079c6223d8b8118449677a7b44f269c7)
#### Tuesday 2023-08-29 10:34:15 by Q

Update STORAGE.md

First things first, added descriptions for a bunch of unique stuff. It's much better to actually leave descriptions whenever possible so if people are looking for, let's say, a terminal typing test, they can find it simply by searching and won't have to go through 10 links before they get to it.

Simply putting almost every link next to lessons is messy at best and misleading at worst since some of those links aren't typing lessons, they're exclusively typing tests or ways to practice typing.

Also, there were 2 instances of klavaro, the site link and the sourceforge link. You can get to the sourceforge download link from the site and it's much easier to navigate the site since it has translations for a bunch of languages, so I left the site link. I also divided klavaro, typefast, and typingstudy from regular typing lessons because those are the only ones that have multilingual options, and I think they're worth separating for the sake of people having an easier time finding a non-english exclusive typing lessons/tests.

Typelit.io is very unique in the sense that it's the only site where you can practice typing by retyping books. It doesn't really fit under lessons since there's no lessons, it's just an interesting way to practice.

Colemak is unique because while it is a pretty bare-bones typing test, it does offer alternative keyboard options (colemak, dvorak, tarmak, workman etc.) as well as a custom keyboard layout, so I think it's worth mentioning that in the description so folks who use non QWERTY based keyboards can have an easier time finding the typing test they need. It also really doesn't fit next to lessons since, again, it has no lessons.

Generally even just leaving monkeytype without a description implies it's a site for typing lessons, which it is not. It's a site for customizable typing tests, which can assist in improving typing skill, but it isn't an actual lesson or a tutorial by any means.

10fastfingers is pretty much the only site with active typing competitions, so it's worth separating from regular lesson sites. Again, makes it way easier for users to find what they need and saves them the time of clicking through shitton of links for a niche they need.

Now onto the removed stuff:

* [Typing Finger Positions](https://i.ibb.co/L8VY6xR/Finger-position-on-a-keyboard.png) - it's just an image. The exact same image you'd find on pretty much any typing lesson or even typing test site, except those also come with the additional features of actually being useful since you're doing something and they generally show you what keys you're pressing as well. I really doubt anybody would spare more than a few seconds looking at this image, let alone just have it left in a tab and looking back on it whenever they try to type to remind themselves of the finger positioning. For people who wanna learn typing, there's plenty of actually interactive lessons which beat just staring at an image. And even if someone needs this, it's one search away. It's on just about every typing related site. Just save this for the FreeImagesHeckYeah wiki.

* [Dance Mat Typing](https://www.bbc.co.uk/bitesize/topics/zf2f9j6/articles/z3c6tfr) - Nobody above the age of 8 has any real use for this. There's plenty of other lessons you can more easily navigate and that don't come with an obnoxious animation and music.

* [RapidTyping](https://rapidtyping.com/) - it was last updated 2 years ago, most likely a dead project, has nothing the other sites/apps don't already offer and is pretty bloat since it's 50MB. There's really no good explanation for why software this simplistic would be 50MB unless it's just badly coded or has a bunch of useless shit. The UI itself is not really pleasant either.

* [kbs](https://kbs.im/) - bare-bones typing test. The only kind of special thing about it is you can change keyboard colors. That's about it. But even that is pretty much useless since you're not going to be looking at the image of a keyboard during the typing test, you're going to be looking at the words which are above it. The project was also last updated almost 2 years ago, so it's really unlikely it'll have any new features.

Last thing, I've renamed Typing Lessons to Typing Lessons / Tests since there's really both of those in this category and some sites don't have lessons at all, so I thought the category name just being Typing Lessons was kind of misleading. Typing games also generally fit more into the typing tests niche.

---
## [beetlejuicetr/PsychonautStation](https://github.com/beetlejuicetr/PsychonautStation)@[69827604c4...](https://github.com/beetlejuicetr/PsychonautStation/commit/69827604c46952dd4393db8617cd494ade17bea2)
#### Tuesday 2023-08-29 10:53:38 by Watermelon914

Improves the RPG loot wizard event. (#77218)

## About The Pull Request
As the title says. Adds a bunch more stat changes to various different
items and a somewhat simple way of modifying them whilst minimizing
side-effects as much as possible.
Added a new negative curse of polymorph suffix that can randomly
polymorph you once you pick up the item.
Curse of hunger items won't start on items that are not on a turf.
Curse of polymorph will only activate when equipped.

Bodyparts, two-handed melees, bags, guns and grenades, to name a few,
have a bunch of type-specific stat changes depending on their quality.

Some items won't gain fantasy suffixes during the RPG loot event, like
stacks, chairs and paper, to make gamifying the stats a bit harder.
I'm sure there'll still be other ways to game the event, but it's not
that big of a deal since these are the easiest ways to game it.
High level items also have a cool unusual effect aura

## Why It's Good For The Game
Makes the RPG item event cooler. Right now, it's a bit lame since
everything only gains force value and wound bonus on attack. This makes
the statistic increases more type-based and make it interesting to use

It's okay for some items to be powerful since this is a wizard event and
a very impactful one too. By making the curse of hunger items not spawn
on people, it'll also make it a less painful event too.

## Changelog
:cl:
add: Expanded the RPG loot wizard event by giving various different
items their own statistic boost.
/:cl:

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [libbpf/bpftool](https://github.com/libbpf/bpftool)@[911adbfc89...](https://github.com/libbpf/bpftool/commit/911adbfc89e7fd80e576bcf4578ec4da5b74a87a)
#### Tuesday 2023-08-29 11:34:15 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Thanks also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Acked-by: Jakub Kicinski <kuba@kernel.org>
Link: https://lore.kernel.org/r/20230719140858.13224-3-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [libbpf/bpftool](https://github.com/libbpf/bpftool)@[e0e6b3aaa9...](https://github.com/libbpf/bpftool/commit/e0e6b3aaa9cff3103de7c7e0d778a875d897c556)
#### Tuesday 2023-08-29 11:34:15 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Thanks also to Andrii Nakryiko for early API discussions wrt Meta's BPF prog
management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Link: https://lore.kernel.org/r/20230719140858.13224-2-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [xDec0de/uSleep](https://github.com/xDec0de/uSleep)@[7ac263475a...](https://github.com/xDec0de/uSleep/commit/7ac263475a58acc599ecaa81e82f6ee96ecadd9c)
#### Tuesday 2023-08-29 12:51:05 by xDec0de_

Update SleepErrorEvent message path's

Let's keep the same format for all messages, shall we? On a side note, yeah, I enjoy adding random comments to commit descriptions, makes the whole coding process more enjoyable and less painful, who is gonna read this on such a small commit anyway? If you do, please let me know, I'd die from laughter.

---
## [rza4ev/Webscrappingandmodeling](https://github.com/rza4ev/Webscrappingandmodeling)@[1f215485d2...](https://github.com/rza4ev/Webscrappingandmodeling/commit/1f215485d2f14e5ea7a0fd3984ebd8f4ede4723d)
#### Tuesday 2023-08-29 13:14:41 by rza4ev

Add files via upload

Webscraping, Data Modeling, and Random Forest Regression" GitHub Repository Description:

Welcome to the "Webscraping, Data Modeling, and Random Forest Regression" repository! 🌐🔍📈

This repository serves as a comprehensive resource for projects and code examples focusing on web scraping, data preprocessing, and the application of the Random Forest Regression model. Whether you're a data enthusiast, researcher, or developer, this repository offers a wealth of knowledge on extracting, transforming, analyzing data from the web, and using advanced modeling techniques.

📚 Projects and Code Samples:
Discover a wide array of projects and code samples that cover the entire data science pipeline. From extracting structured data using web scraping tools like BeautifulSoup and Scrapy to cleaning, preprocessing, and transforming data, this repository provides practical insights into the data journey.

🕸️ Web Scraping Techniques:
Learn the art of web scraping – how to extract relevant information from websites efficiently and automate data collection. Explore techniques to navigate websites, parse HTML, and gather valuable datasets for analysis and modeling.

📈 Random Forest Regression:
Dive deep into the world of predictive modeling using Random Forest Regression. Witness the power of ensemble learning as you build robust models that handle non-linearity and capture complex relationships in data. Leverage the benefits of decision trees and ensemble techniques to predict outcomes accurately.

🌟 Why Explore This Repository:

Master the art of web scraping for data acquisition from diverse online sources.
Develop strong data preprocessing skills to clean, structure, and enhance your datasets.
Explore practical applications of the Random Forest Regression model for predictive analytics.
Collaborate with a community of learners, practitioners, and enthusiasts passionate about data science.
Whether you're a beginner seeking a foundational understanding or an experienced data scientist looking to expand your toolkit, "Webscraping, Data Modeling, and Random Forest Regression" is your guide to mastering data extraction, manipulation, and advanced modeling techniques.

Feel free to contribute, share your insights, and embark on an exciting journey of turning raw web data into actionable predictions!

Join us in unlocking the potential of data and making meaningful strides in the world of web scraping and predictive modeling. 🌐🔍📊🌲🚀

---
## [codecov/codecov-api](https://github.com/codecov/codecov-api)@[e2c6b1c425...](https://github.com/codecov/codecov-api/commit/e2c6b1c425cac66f0d422bd5692c7aae4cc46b61)
#### Tuesday 2023-08-29 13:20:46 by Giovanni M Guidini

fix: lru_cache issues + meta info missing  (#72)

Context: https://github.com/codecov/engineering-team/issues/119

So the real issue with the meta info is fixed in codecov/shared#22.
spoiler: reusing the report details cached values and _changing_ them is not a good idea.

However in the process of debuging that @matt-codecov pointed out that we were not using lru_cache correctly.
Check this very well made video: https://www.youtube.com/watch?v=sVjtp6tGo0g

So the present changes upgrade shared so we fix the meta info stuff AND address the cache issue.
There are further complications with the caching situation, which explain why I decided to add the cached value in the
`obj` instead of `self`. The thing is that there's only 1 instance of `ArchiveField` shared among ALL instances of
the model class (for example, all `ReportDetail` instances). This kinda makes sense because we only create an instance
of `ArchiveField` in the declaration of the `ReportDetail` class.

Because of that if the cache is in the `self` of `ArchiveField` different instances of `ReportDetails` will have dirty cached value of other `ReportDetails` instances and we get wrong values. To fix that I envision 3 possibilities:
1. Putting the cached value in the `ReportDetails` instance directly (the `obj`), and checking for the presence of that value.
If it's there it's guaranteed that we put it there, and we can update it on writes, so that we can always use it. Because it is
for each `ReportDetails` instance we always get the correct value, and it's cleared when the instance is killed and garbage collected.

2. Storing an entire table of cached values in the `self` (`ArchiveField`) and using the appropriate cache value when possible. The problem here is that we need to manage the cache ourselves (which is not that hard, honestly) and probably set a max value. Then we will populate the cache and over time evict old values. The 2nd problem is that the values themselves might be too big to hold in memory (which can be fixed by setting a very small value in the cache size). There's a fine line there, but it's more work than option 1 anyway.

3. We move the getting and parsing of the value to outside `ArchiveField` (so it's a normal function) and use `lru_cache` in that function. Because the `rehydrate` function takes a reference to `obj` I don't think we should pass that, so the issue here is that we can't cache the rehydrated value, and would have to rehydrate every time (which currently is not expensive at all in any model)

This is an instance cache, so it shouldn't need to be cleaned for the duration of the instance's life
(because it is updates on the SET)

closes codecov/engineering-team#119

---
## [mjg/git](https://github.com/mjg/git)@[8f23432b38...](https://github.com/mjg/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Tuesday 2023-08-29 13:51:46 by Johannes Schindelin

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
## [WeizhuoZhang-intel/benchmark](https://github.com/WeizhuoZhang-intel/benchmark)@[745644f391...](https://github.com/WeizhuoZhang-intel/benchmark/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Tuesday 2023-08-29 15:05:09 by Mark Saroufim

FIX SAM for bfloat16 (#1764)

Summary:
Ok this was kinda annoying

Basically the SAM codebase had a few places where it hardcodes `torch.float32` such that even if you convert the model to `torch.bfloat16` a few parts of the model won't be and will have type mismatch errors - this fixes the problem cpuhrsch desertfire - idk enough about floats and why there isn't some type promotion rule for bfloat16

I wonder whether we should add tests for multiple dtypes in torchbench to make checking for this kind of issue more robust especially now that bfloat16 seems to be the default for dynamo xuzhao9

## Logs

```
FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
E
======================================================================
ERROR: test_sam_eval_cuda (__main__.TestBenchmark)
----------------------------------------------------------------------
components._impl.workers.subprocess_rpc.ChildTraceException: Traceback (most recent call last):
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 482, in _run_block
    exec(  # noqa: P204
  File "<subprocess-worker>", line 2, in <module>
  File "/home/ubuntu/benchmark/torchbenchmark/util/model.py", line 280, in invoke
    out = self.eval()
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/__init__.py", line 65, in eval
    masks, scores, logits = predictor.predict(
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/predictor.py", line 164, in predict
    low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
TypeError: Got unsupported ScalarType BFloat16

    working_dir: /tmp/tmpg5de41du
    stdout:
        [2023-07-13] 01:57:38.499061: TIMER_SUBPROCESS_BEGIN_EXEC
        [2023-07-13] 01:57:39.002078: TIMER_SUBPROCESS_FAILED
        [2023-07-13] 01:57:39.002141: TIMER_SUBPROCESS_FINISHED
        [2023-07-13] 01:57:39.002153: TIMER_SUBPROCESS_BEGIN_READ

    stderr:

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/ubuntu/benchmark/test.py", line 104, in eval_fn
    task.invoke()
  File "/home/ubuntu/benchmark/torchbenchmark/__init__.py", line 402, in invoke
    self.worker.run("""
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 155, in run
    self._run(snippet)
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 320, in _run
    subprocess_rpc.SerializedException.raise_from(
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 458, in raise_from
    raise e from ChildTraceException(traceback_str)
TypeError: Got unsupported ScalarType BFloat16

----------------------------------------------------------------------
Ran 1 test in 7.814s

FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
.
----------------------------------------------------------------------
Ran 1 test in 8.315s

OK
```

Pull Request resolved: https://github.com/pytorch/benchmark/pull/1764

Reviewed By: drisspg, cpuhrsch

Differential Revision: D47441873

Pulled By: msaroufim

fbshipit-source-id: a60880fd7c0826cfd469ace39d76894469ca0e5e

---
## [powerhome/playbook](https://github.com/powerhome/playbook)@[205619a0e9...](https://github.com/powerhome/playbook/commit/205619a0e9ce327306acf84735c13ea4ed356c7b)
#### Tuesday 2023-08-29 15:20:45 by Gavin Huang

[PLAY-972] dateTime Bug Fixes (#2716)

**What does this PR do?**
- Corrects incorrect weekdays by removing the `getUTC` functions
- In the DB, for example, the date was August 15, 2023 01:30:00. The
`toWeekday` function formatted the date from UTC to Local Time, but
`getUTCDay()` went back to grab the UTC date. This issue was evident
with late-day appointments. Therefore, we should not be using any
`getUTC` functions.
- Corrects two bugs Jason found within`fromNow()`:
  - Remove period from "years ago"
- Fix miscalculation of "milliseconds in a month" - this was causing any
past date with a timestamp of "x months ago" to have a random number
- Updates `toLocaleString()` to use `en-US`
- Hayden R. reported he was receiving `undefined NaN`. Upon
investigation, certain locales (like en-GB [Great Britain]), can't use
functions like `getMonth()` so it was returning `undefined NaN`. We
default to `en-US` because internationalization and formatting does not
matter since Playbook formats dates in a specific way.

**Screenshots**

**Before**

![Before](https://github.com/powerhome/playbook/assets/47684670/07303adf-f2eb-4d7b-a0ba-ad82cf7f945c)

**After**

![After](https://github.com/powerhome/playbook/assets/47684670/8696283f-d4b4-4ab3-9302-c9651af672cd)

**How to test?** Steps to confirm the desired behavior:
1. The weekday problem was experienced in the [Sales
Books](https://nitro.powerhrg.com/sales/reps/11115/sales_books?rep_filter%5Bdate%5D%5Byear%5D=2023&rep_filter%5Bdate%5D%5Bmonth%5D=8).
In Miguel Picart's (or any RC), select their "Books" tab, select "All
Appointments", find any place that has 2+ appointments the same day -
they should be correct.
2. For Hayden's bug, impersonate Hayden and in his user profile ensure
that the address is showing as his European address. Go to a Runway
ticket and check the reviewers, he should not see `undefined NaN`. We
should also ensure that Hayden can see a date after the release.

#### Checklist:
- [X] **LABELS** Add a label: `enhancement`, `bug`, `improvement`, `new
kit`, `deprecated`, or `breaking`. See [Changelog &
Labels](https://github.com/powerhome/playbook/wiki/Changelog-&-Labels)
for details.
- [X] **DEPLOY** I have added the `milano` label to show I'm ready for a
review.
- [ ] **TESTS** I have added test coverage to my code.

---------

Co-authored-by: Nida Ghuman <nidaqg@gmail.com>

---
## [pixeltris/YgoMaster](https://github.com/pixeltris/YgoMaster)@[499f9df4f3...](https://github.com/pixeltris/YgoMaster/commit/499f9df4f3cf57e13dd2a9080de6d7ee5f4b7b54)
#### Tuesday 2023-08-29 15:26:59 by pixeltris

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
## [entrez/NetHack](https://github.com/entrez/NetHack)@[38cda5ad52...](https://github.com/entrez/NetHack/commit/38cda5ad52f47a810c44171e9081d0275401c516)
#### Tuesday 2023-08-29 15:49:38 by Michael Meyer

Adjust seenres on visible gear removal

If a monster sees you remove some piece of gear that grants a
resistance, it will remove that resistance from its list of remembered
resistances and be willing to try attacking you with that adtyp again.
This avoids the situation where you put on a ring of cold, get hit with
one cold attack, and then can remove it because all the monsters nearby
will permanently remember you as being cold resistant (but even after
this change a wily hero could still step into a niche and do it without
any monsters seeing, so trick them into thinking she's still cold
resistant...).  The hero could still be resistant if there were multiple
sources to begin with, of course, but the monsters will test it and
learn that again if necessary.

It's a little weird that the monsters can recognize the intrinsic
granted by the item being removed, but they display knowledge of
unidentified (by the hero) objects in many other circumstances too, so I
hope it's forgivable in the pursuit of having them act more cleverly
about resuming previously-resisted attacks like this.  Another approach
that avoids the gear recognition, blanking seenres on any gear change,
can result in odd situations like orcs treating their own cloaks as
potential sources of many different resistances, which also seems silly.

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[dc6ddd821b...](https://github.com/FernandoJ8/tgstation/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Tuesday 2023-08-29 16:03:12 by Cheshify

North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

---
## [benoit-pierre/koreader](https://github.com/benoit-pierre/koreader)@[4acf131071...](https://github.com/benoit-pierre/koreader/commit/4acf131071c704863d0d66f78f1b2314df9c3164)
#### Tuesday 2023-08-29 16:33:56 by NiLuJe

ReaderActivityIndicator: Oh god, my eyes, they buuuuurn.

Make this a real boy, with a transient lipc handle.
And get rid of the insane 1s sleep on affected ReaderView paints,
because ouchy.

This is completely deprecated anyway, so this is entirely pointless,
and mainly to prevent implementation details from creeping into
reader.lua.

---
## [ryanvolz/rtl-sdr](https://github.com/ryanvolz/rtl-sdr)@[ade7842328...](https://github.com/ryanvolz/rtl-sdr/commit/ade78423283a03938c1325f1baf42ac277480678)
#### Tuesday 2023-08-29 17:05:10 by Ryan Volz

Add commits since 0.6.0 through 2023/08/21

change version to 0.6git

Signed-off-by: Steve Markgraf <steve@steve-m.de>

lib: Add workaround for Linux usbfs mmap() bug

The Linux Kernel has a bug on ARM/ARM64 systems where the USB CMA
memory is incorrectly mapped to userspace, breaking zerocopy.

When the Kernel allocates the memory, it clears it with memset().
If the mapping worked correctly, we should have zeroed out buffers,
if it doesn't, we get random Kernel memory. We now check for this,
and fall back to buffers in userspace if that's the case.

Signed-off-by: Steve Markgraf <steve@steve-m.de>

contrib/jenkins.sh: run "make maintainer-clean"

Related: OS#3047
Signed-off-by: Oliver Smith <osmith@sysmocom.de>
Signed-off-by: Steve Markgraf <steve@steve-m.de>

lib: fix memory leak in rtlsdr_open()

Thanks to Vincent Perrier for reporting the bug.

lib: disable usbfs zero-copy support by default

Although we added a detection mechanism for the presence of the Kernel
bug earlier, reading from the incorrectly mapped memory might cause a
bus error on some ARM systems.

With the overall performance benefit being rather minimal for the
data rates of rtl-sdr, disable zero-copy by default.

rtl_eeprom: fix warnings

Account for \0 string terminator when calling strncpy().

Fixes the following GCC 9 warning:
warning: ‘__builtin_strncpy’ specified
bound 256 equals destination size

Fix building librtlsdr on OpenBSD

Gets rid of librt, which doesn't exist on OpenBSD. The version of
librtlsdr in the OpenBSD ports tree is extremely old (~2013), so this
should help some users.

Tested against tag 0.6.0, but it should apply just fine to HEAD.

lib: Add GPIO version of the bias tee configuration API

rtl_biast allows for non-default GPIO pins to be used.
Add an API call which allows for that.

rtl_biast: Add rtl_biast

This is an import of the rtl_biast command line tool from the
rtlsdrblog github repository.  It's easier to include it here than
try to package up the separate application because they both
wish to install dynamic libraries.

allow building librtlsdr as CMake subproject

Replace CMAKE_SOURCE_DIR by PROJECT_SOURCE_DIR in main CMakeLists.txt
to fix CMake errors when building librtlsdr as a subproject.

Fixed issues compiling on Windows with MSVC, CMake and NMake (#61)

When trying to build a simple program which uses librtlsdr
as a subproject on Windows, CMake reported several problems
which were solved by:
- Added complete name of libusb in FindLibUSB module.
- Replaced CMAKE_SOURCE_DIR to PROJECT_SOURCE_DIR in src/CMakeLists.txt.
- Replaced header file <afxres.h> in src/rtlsdr.rc.in (only present when windows MFC is
  installed) by <windows.h> which defines the same constants.

set CMake policy CMP0075 if it exists

Otherwise newer versions of CMake are throwing a warning.

lib: enable better UHF reception (>862MHz) for FC0013

Improve librtlsdr.pc file

librtlsdr.pc should declare -lusb-1.0 in Libs.private section
to exclude usb library from dynamic linking.
References to libusb headers are not needed in Cflags, since these
headers are not used by external rtlsdr API, but this is optional.
https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=784912

CMake: support for libusb on GNU/Hurd

Debian builds on hurd-i386 with a variant of libusb.

rtl_fm/rtl_power: Improve scanning range parsing

Use udev uaccess rules

rtl_tcp: Add IPv6 support

I've prepared this patch in response to Debian bug #870804
https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=870804

It passes the text from the -a and -p options through
getaddrinfo() and uses the first result that has a valid
socket with a successful bind.

While not a complete bind to all possible valid names, it
does appear to address the use case of the bug submitter
without completely changing the program flow.

rtl_tcp: Initialize listensocket

Older versions of GCC will complain that it can be used
uninitialized - which is not the case, but it breaks our Jenkins
build as we build with -Werror.

Modernize CMake

New minimum version is CMake 3.7.2.

This patch has been rebased to incorporate changes that happened
since the creation of the original patch.

Original Author: A. Maitland Bottoms  <bottoms@debian.org>, 07 Sep 2018

Update Debian packaging information

Add missing rtlsdrConfig.cmake

This file was missing in commit
849f8efca42b659bf7e8fe17156ee0aa67b47233.

Fix for CMake < 3.12.0

As several current LTS distributions currently ship with CMake
< 3.12.0, add a work-around for CMake Issue 16967.

Otherwise we get:
CMake Error at
/usr/share/cmake-3.7/Modules/CheckCXXSourceCompiles.cmake:64 (try_compile):
   Unknown extension ".cxx" for file

     /tmp/rtl-sdr/build/CMakeFiles/CMakeTmp/src.cxx

   try_compile() works only for enabled languages.  Currently these are:

     C

debian: fix source/format from quilt to native

We certainly don't use quilt, as we build packages using
git-buildpackage.

This is what likely causes build failures on our osmocom nightly
builds stating

gbp:error: Non-native package 'rtl-sdr' has invalid version '0.5.4.32.3d7c'

If the package now is 'native', the errors should be gone.

tuner_r82xx: fix short-write in r82xx_read

In r82xx_read, there is a 1-byte I2C write followed by the I2C read.  If
this I2C write fails, r82xx_read correctly bails out but may return 0.
Callers that check whether (rc < 0) will assume that the buffer was written
when it has not been, e.g. in r82xx_set_tv_standard where

	priv->fil_cal_code = data[4] & 0x0f;

consumes a garbage value for data[4].

This change resolves that issue by copying the error path from r82xx_write.

Add rtl_biast as install target

Thanks to https://github.com/erikarn for pointing this out.

cmake: populate pkgconfig file with prefix

Previously the prefix and related paths were not set.

fix windows build

We really should not have pkgconfig as a build requirement on windows.

rtl_tcp: Extracted some constants out of printf strings

The help output contained constants that should print values
based on code constants and not be hardcoded into the print strings.

rtl_tcp: put new DEFAULT_* constants in defines

Fix failures with some GCC versions:
  /usr/src/packages/BUILD/src/rtl_tcp.c:90:24: error: initializer element is not constant
   static int llbuf_num = DEFAULT_MAX_NUM_BUFFERS;

Fixes: 641c22 ("rtl_tcp: Extracted some constants out of printf strings")
Change-Id: Ia9e18d4c22d957f561dcdaf2657bb6d201374375

rtl_fm: add a new option to select 2nd direct sampling mode

Fix minGW build

MinGW-w64 ships all Windows SDK headers as lowercase, which prevents
cross-compiling this code from Linux.

lib: force wait state after cancel of usb transfer

..and before handling usb events

This avoids an occasional crash when closing the device on Windows.
Also see https://github.com/libusb/libusb/issues/1043.

lib: Stop applying workaround for libusb < 1.0.9

Librtlsdr has a workaround for libusb versions that lack
libusb_handle_events_timeout_completed, which was added in version 1.0.9
(released 2012-04-02). The workaround is always applied unless the
HAVE_LIBUSB_HANDLE_EVENTS_TIMEOUT_COMPLETED macro is set, but the cmake
code that sets this macro was removed in
849f8efca42b659bf7e8fe17156ee0aa67b47233. As a result, the workaround is
now always applied. This results in an extra 1-second delay whenever a
GNU Radio flowgraph containing an RTL-SDR block is stopped, which makes
operations like switching between demodulators in Gqrx annoyingly slow.

To solve this problem, I've simply removed the workaround, as it should
no longer be needed.

I wonder if perhaps the workaround recently applied in
2659e2df31e592d74d6dd264a4f5ce242c6369c8 might stem from the same bug.

Fix signal handler from getting stuck in an endless loop

The signal handler for SIGINT/TERM/QUIT and, importantly, SIGPIPE tries
to write an informational message to stderr. When however stderr is
redirected to a closed pipe, this will cause (another) SIGPIPE, and in
turn the signal handler will get called again, and again and again.

Since we intend to exit rtl_fm anyways, we can just ignore this signal.

add rtl-sdr blog v4 support

---
## [openai/evals](https://github.com/openai/evals)@[97aa5483de...](https://github.com/openai/evals/commit/97aa5483de8673172d5eaabc33ba7e7cf3561ffe)
#### Tuesday 2023-08-29 17:10:07 by samta-kamboj

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
## [openai/evals](https://github.com/openai/evals)@[429a6b695e...](https://github.com/openai/evals/commit/429a6b695e28387d68adbfad500903a39abc3b11)
#### Tuesday 2023-08-29 17:10:22 by pancoaster

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
## [Segrain/cmss13](https://github.com/Segrain/cmss13)@[f3fc60ed65...](https://github.com/Segrain/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Tuesday 2023-08-29 17:20:50 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[b033e1ed6a...](https://github.com/spockye/Shiptest/commit/b033e1ed6a1e7f87edc73a75a96bcf6536e39aba)
#### Tuesday 2023-08-29 17:48:05 by Sun-Soaked

Update_Appearance Port (#2170)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
[(original pr)](https://github.com/tgstation/tgstation/pull/55468)
After nine years in development we hope it was worth the wait

I ported this specifically for the signals I'll need for world icons.
However, it had a lot of other useful stuff, so I ended up just grabbing
(almost) the entire pr.
I tried to grab as few of the superfluous code rewrites as possible to
make reviewing a bit easier, but I couldn't help grab stuff like the APC
icon code rewrite(the original code was a war crime).

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

- ports the wrapper proc `update_appearance` for icons, descs, and
names, adds `update_desc` and `update_name` subprocs to handle those.
Things. without just stuffing them into update_icons like some kind of
psychopath

- ports a bunch of signal hooks useful for changing names, descriptions,
and icons. I needed these for world_icons which is where this wild ride
all started

- ports some `base_icon_state` implementation. Stuff like spear code
makes slightly less duplicates(and more sense) now which is nice.
We could definitely implement it more I think but that's a future me
problem

- 500 files of immersive vsc-mass-editing action to implement
`update_appearance()`(sorry in advance, but not as sorry as I was when
manually copy-pasting the custom ones for like 3 straight days)

-"consig" and "comisg" have been taken out behind the codebase and shot.
Not 'technically' a bug it just made my head hurt

-My first pr with 0 player facing changes (confetti)
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: TemporalOroboros, Memed Hams
code: ports update_appearance, update_name, and update_desc from tg, as
well as associated signals
code: a bit of base_icon_state implementation. Can you believe it's been
sitting in our code almost unused for like 3 years
code: cleans up some code formatting, mainly around custom icons and
overlays
code: fixes the typos in COMSIG_STORAGE_EXITED and
COMSIG_STORAGE_ENTERED
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [giorgi-o/SkinPeek](https://github.com/giorgi-o/SkinPeek)@[16e1ff2706...](https://github.com/giorgi-o/SkinPeek/commit/16e1ff27065138f093e38e1f5fa04d0b77c238f0)
#### Tuesday 2023-08-29 18:06:55 by Giorgio

fix battlepass fetching between acts
basically dealing with val-api having a new act but no battlepass for it
my guess is that technically the act ended yesterday at midnight but
that's only for the us, here in the eu we can still play on the old
patch for a few hours, which causes a mess with battlepasses etc
but uh yeah, this should fix that now

---
## [thisismy-github/pyplayer](https://github.com/thisismy-github/pyplayer)@[3d84e7072d...](https://github.com/thisismy-github/pyplayer/commit/3d84e7072d8268f70015849f1c3e053c081457cf)
#### Tuesday 2023-08-29 19:17:48 by thisismy-github

Improved geometry saving/restoring consistency

First, the "toggle maximize" action not saving geometry has been fixed
through brute force, using two new properties:
`self.invert_next_move_event` and `self.invert_next_resize_event`.
This is to circumvent horrible, awful, no good Qt behavior that causes
the window's state to be inverted during the ensuing move/resize event
when manually calling `self.showMaximized()`.

Next, saving/restoring window geometry in general has been improved
and is about as good as it'll get (not including refactoring the code).
I finally learned about `QWidget.saveGeometry()` and
`QWidget.restoreGeometry()`, only to find that they too have many edge
cases that cause geometry to be lost, necessitating the use of all the
aforementioned and already existing garbage. Hopefully in the future
we can get rid of all the other stuff entirely. In the mean time, the
`pos` and `size` settings have been replaced by `geometry`, an
indecipherable hex-encoded string. This is somewhat unfortunate,
but necessary. I think. Whatever, man. I wish this stuff just worked.

Additionally, `self.ignore_next_fullscreen_move_event` has been added to
allow moving the window while fullscreen to immediately force the user
out of fullscreen.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d2a9834b32...](https://github.com/TaleStation/TaleStation/commit/d2a9834b3241f3a1848eede1739b1f23e2f718c2)
#### Tuesday 2023-08-29 19:29:38 by TaleStationBot

[MIRROR] [MDB IGNORE] [no gbp] Adds missing chat feedback to watcher abilities (#7417)

Original PR: https://github.com/tgstation/tgstation/pull/77700
-----
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

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Sm680-Development/kernel_motorola_sm6225](https://github.com/Sm680-Development/kernel_motorola_sm6225)@[febdcf373b...](https://github.com/Sm680-Development/kernel_motorola_sm6225/commit/febdcf373b1584efebc10df0542ba06516311ec5)
#### Tuesday 2023-08-29 20:33:03 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Sm680-Development/kernel_motorola_sm6225](https://github.com/Sm680-Development/kernel_motorola_sm6225)@[4c7d0ec1eb...](https://github.com/Sm680-Development/kernel_motorola_sm6225/commit/4c7d0ec1eba070f96d5ef894fa1d7d8f73f7a5d1)
#### Tuesday 2023-08-29 20:34:53 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[4155eecdac...](https://github.com/silicons/Citadel-Station-13-RP/commit/4155eecdacd658fd0509f41e3bf8a7c48b13102c)
#### Tuesday 2023-08-29 21:34:02 by silicons

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
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[69d6d9d4e1...](https://github.com/silicons/Citadel-Station-13-RP/commit/69d6d9d4e1d72089acb1754bace58625d27c6571)
#### Tuesday 2023-08-29 21:34:02 by CharlesWedge

Let Slip the Dogs of War (#5905)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## The Machines Rise
With the recent sector wide hack rogue synthetics have become a problem
in the sector. What's worse now corrupted fabricators are even building
more combat designs! With an increasingly dangerous galaxy, it seems
that mercenaries will not be the only threat brave explorers and
security teams may face today. All security forces are advised to stay
on the lookout for the latest threat to the galaxy, and those not
equipped to take them on are advised, stay well out range!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
As we want to move away for humanoid threats for simple mobs, I feel it
necessary to shore up killer machines as more advanced type of enemy to
take the place of humans in terms of 'dangerous opponents'. The current
selection of machines mobs tend to be more niche in function (we can't
exactly use the nanite horror as common enemies). Also there is a bigger
maint drone now because the smaller ones weren't bad enough, least these
ones are easier to hit.

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
add: 4 New Hostile Drones, Three Dogs (including one sniper), and a
Maint Drone.
add: New News article elaborating on recent events.
tweak: drones are now part of the same faction as hivebots. This means
evil bots will now cooperate (Hivebots are being updated next).
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: BlueWildrose <57083662+BlueWildrose@users.noreply.github.com>

---
## [get-convex/ai-town](https://github.com/get-convex/ai-town)@[021e3902b9...](https://github.com/get-convex/ai-town/commit/021e3902b9a770bf10b1803a91297f26ed06814a)
#### Tuesday 2023-08-29 21:35:31 by Lee Danilek

private action to change identity (#8)

some of the NPC identities make them hard to talk to. e.g. Alice has trouble responding to questions, so if i ask "what kind of shampoo do you like" she responds "ah the mysteries of hair care! let the universe guide your decisions".

we can add an internal action that can be called from the dashboard function runner to override an agent's identity. then anyone who clones the repo and spins up their own town can modify the NPC identities without having to clear memories and stuff.

Alice is more fun to talk to when her prompt is "Alice knows about everything, including science and computers and politics and history and biology. She loves talking about everything, always injecting fun facts and eager to teach interesting tidbits about the world."

---
## [bakour1/shoppay-ecommerce](https://github.com/bakour1/shoppay-ecommerce)@[f7fa7f1c44...](https://github.com/bakour1/shoppay-ecommerce/commit/f7fa7f1c44074f2c840a3365108d28e9af46b2f5)
#### Tuesday 2023-08-29 23:34:55 by bakour1

35. Sign up 4 Send email 1

So after using the activation token, the risk is to actually create the URL so we can go in sequence

and we call this URL.

We're going to have back six because we need to have first of all, it's going to be our, you know,

our website, which is going to be, for example, HTTP localhost, 3000.

So maybe we can go back, write it to the dot in V here and we have this next URL you can use.

That's what I prefer to have something that is called always the base URL because this will change when

you host your application.

The PCR will change for your application and it's not going to be local host 3000.

It could be like WW dot shop, a dot com or something like that.

So I'm just going to take this URL.

Also, we need to restart the server.

Okay.

And then go back to our code.

So this is the first thing.

So we're going to go to process dot E and V, and this is basic.

So that's the first thing.

Then we're going to go forward slash, which is going to be something like activate account or activate

and then forward slash.

We need to have the activation token right here like that.

This way and we can actually just resend the URL so you can see that here.

So if I go back, let me just see if it's runs.

Okay, so the server is running.

We can go back here and then let me try something like that and then send and this waits a little bit.

And I hope there is no problem right here.

Let me just make sure.

So open the console.

Okay.

Just been waiting to connect to the database.

Okay.

And we get this.

So that's the URL we sent to the email.

So the email is going to be like that.

He clicks in that you are.

So that means he's going to go to our websites and then to the activity page and we're going to have

this long activation token that we're just going to extract from that URL and get the user ID and then

make the email verified in the database from here.

If you go back, we're going to make, as I told you, the email verified from NULL to true.

And now if this is true, that means the user is activated.

So it's a pretty simple idea to make.

So the second the second thing is, which would be to have some sort of way to send the emails because

now we have the data ready, but we need the tool to send this and that's when it's going to use the

Gmail API from the Google Cloud console.

And also we're going to use node mail and some stuff.

So I've done this like before in my other course and some people say that after like two days or something,

the method stops working or like you can send email until you refresh and do the method again.

And I've been aware of that and I've looked into it and the problem was simply from the Express server.

So if you follow this with me, you're using next year's, I promise you it will never happen to you.

It doesn't even get revoked or nothing.

Like I created this, this application like five months ago and is still working till now.

So I promise you, if you follow me carefully and everything I do the same is not going to be a problem

at all.

It will always work no matter what.

And that's a pretty, pretty good thing because sending emails is a little bit complicated, you know?

So let's go back.

So the first thing is you've got to go to Google Cloud Console and you open the console.

I open that, so I'm here.

So if you are this is the first time here we show you log login and then you're going to it's going

to have some button to create a new project.

If you if you have another project before you can click right here and then click in your projects,

make sure in the Google Cloud console and right here is called this, for example, Shop or something

like that.

Okay, This is just for testing purposes.

I'm going to click Create and let's wait a little bit as it's still creating.

Okay.

You see right here this some process six times.

So you just got to be patient with it a little bit.

So it's been created.

I'm going to click select projects.

I know minutes.

So what you can do is simply click on the minority on the navigation.

You're going to have this API and services and then you're going to go to the oath consent screen and

you're going to click right here and then you're going to get redirected to this page.

So let me close this.

So right here, make sure you use Excel so it can be available for all users and then click create.

And then right here you need an app name.

So for me, I'm just going to call it both.

And then the support image should be the email that you use.

And I'm just having this for testing purposes.

You can have a logo for your application and then some some information for your application or like

your websites as you want.

So right here, everything as it is for the email address, just have the same one and then save and

continue.

And it's a lot of written right here.

So this is for scoops.

You really don't have to do anything right here.

Just save and continue.

And then for chase users, this is very important.

You need to add the email that you will send from.

So I'm just going to add it and then add like that.

Let me add.

Okay.

So it's been added right here in the table and then save and continue.

Kelly Sweet.

This is the summary.

Everything is right.

Then you can click back to Dashboard.

Dashboard was actually you can just go to credentials from here.

Just go to credentials from here.

Clicking here.

Okay?

Please, let's make this faster.

And right here, we're going to go to create credentials, and we're going to go to the oath.

Client ID.

And let's click on that and then we're going to define the application type, which is going to be a

web application, then the name of it, make sure to use the same name for you.

Have everything organized for us or like so you don't have any mix up.

So for the authorized JavaScript login, we need to add the local host 3000.

But if it's hosted, it should be the URL of your websites.

That's it.

So http make sure everything is right.

That's very important.

And then if you click again, you need to.

Okay, so it's been added automatically and then the otherwise redirects you.

Or else you need something like this, which is this URL that I'm going to leave for you, which is

this one.

So developers dot google dot com for slash playground and you're going to see why because we're going

to use the Gmail API, which is available right here for us from Google developers so that everything

seems fine.

Let me remove this from here and then I'm just going to click create.

And as we click Create, we get our first client's key and the secret key.

So these two are very important.

You can download them as JSON.

I'm just going to copy the first one, then go back to our application, go back to the DOT EMV and.

Okay, So we can have it.

Maybe.

So maybe right here.

And you can call this, for example, mailing service.

And I say we're going to do the same.

So it's going to be mailing service, mailing service, client ID, and we can also have the second

one, which is going to be client secrets.

So for the ID, that's the ID, don't use this because just I'm going to delete that later.

So make sure you use your own and go back again, get the secrets, go back and just paste it.

It sets also right here like that and you need to reset the server to you.

Really?

You don't really need that to do.

You really don't need to do that.

Sorry.

I don't know what's happened to my tank.

So then simply we're going to go back to the oath to playground and this is simply going to go to settings

here on the right and then make sure to click on use your own or credentials like this.

And then here we're going to need the client ID and the client secrets, which is simply what we have.

So the secret is already like copied so we can copy that and paste it.

Also, we need the client ID.

This is very important.

If you don't do this, it's going to keep refreshing the data and the ID and the secret is always going

to be changing.

Not the client's ID, but the client secrets.

Make sure to do that and click close.

Make sure that it's already registered there.

And then here we just simply got to go https four four slash and then mail dot google dot com and then

you're going to click authorize APIs to use the mail Google API.

So click on it and let's switch.

Okay.

So now we need to log in with the same, you know, the one that we had in the test user.

Make sure to log in with that and you click on and then we're going to click, continue to make sure

it's accepted, then continue to give the access.

Okay.

And simply everything is been done and we get the authorization code.

So right here we're just simply going to click exchange authorization for tokens like that.

And we get that.

So and we're going to get this refreshed token.

Sorry.

Let's go back right here to the second sip.

So the refresh token is all we need.

Don't worry.

This is this this message has expired.

Don't worry about it.

It's not going to create any problems, I promise you, because we're going to always going to get the

new token.

So just take this refresh token for now and just go back right here and then let me copy just the text.

That's what I need.

Client refresh.

Token, something like that, and paste that their mail in their mail in service client's refresh token

and go back.

Right.

And this is all actually what we need for now we have the dots are there and now actually we can go

we're going to go back to code and we actually change a few things.

So first thing that we need to do is actually just open the console and click right here and we need

to go here and add and then we're going to use Google APIs because we're going to use the node mailer.

But the node mailer is already been installed before.

If you don't if you don't have it, like if you go back to the package JSON, if you don't have rotate

the node mailer, make sure to install it, which I believe we installed it when we install next.

But if you don't make sure to install it and we tell this installs, let me go back right here and also

you have to refresh.

Okay, maybe, maybe not.

Now let's wait.

Okay.

Let's wait until it's installs.

---

