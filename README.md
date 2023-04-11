## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-10](docs/good-messages/2023/2023-04-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,159,408 were push events containing 3,217,645 commit messages that amount to 226,261,754 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [Moth-lantern/orbstation](https://github.com/Moth-lantern/orbstation)@[bd4392ab74...](https://github.com/Moth-lantern/orbstation/commit/bd4392ab7463c383c7e2824f8a9b7d154ad7940c)
#### Monday 2023-04-10 00:14:47 by Bloop

New inhand icons for light tubes, makes latex balloons craftable, and various other fixes/improvements (#74576)

## About The Pull Request

This ended up turning into a bit of a junk drawer of a PR I'll admit,
but there's really not a whole lot to it.

There are three parts:

### Part I - Inhand sprites for light tubes.

Adds inhand sprites for light tubes. No more cardboard tube placeholder.
This is self explanatory-they have unique sprites for all 3 states
(normal, broken, and burnt out). The broken version has sharpness now.

Also refactored light_items.dm a bit, it was using a bespoke proc called
`update` to do icon updates. Now it has been _updated_ to use
`update_appearance` instead.


![dreamseeker_6WC8vJMiBW](https://user-images.githubusercontent.com/13398309/230615134-31c51e94-cee5-4eef-ba63-c348a3b2debc.gif)

### Part II - Latex Balloons

Latex balloons, a very old piece of code that was full of typos, has had
some life breathed back into it. It is a fun little item, and I saw no
reason to let it rot. It can now be crafted using a latex glove and some
cable. Also, you can pop them using anything sharp... such as a broken
light tube! Aha!

We've come full circle.


![image](https://user-images.githubusercontent.com/13398309/230617764-3a304fd2-05d0-4b2f-b420-056a93c0dce3.png)

### Part III - update_inhand_icon proc

A new atom helper function, `/atom/proc/update_inhand_icon(mob/target =
loc)`

I was struggling to find an existing proc that could update inhand icons
of a mob that was holding any given atom, without necessarily having a
ref to the mob yet.

So I ended up writing one that did that, and finding the spots in the
code which were using a similar way of doing it (that is in fact how I
stumbled upon the latex balloon item).

...........But then Iearned of the
`/datum/element/update_icon_updates_onmob` component and ended up using
that instead. There are still some very niche cases where you might not
be able to use the component where the proc would come in handy however
e.g. in transforming.dm--and if anything, I think it could serve as a
good spot to leave a comment informing would be users of
`update_icon_updates_on_mob` as an alternative.

For that reason especially I thought it worth keeping. 

## Why It's Good For The Game

New inhand sprites, and a fun little craftable balloon. What's not to
like?

## Changelog

:cl:
add: latex balloons can now be crafted using a latex glove and some
cable. You can fill them with air using a tank. They also have a new
sound effect.
imageadd: light tubes have a new inhand sprite
fix: broken light tubes now actually have sharpness to them as they are
basically spikes of glass.
refactor: refactored latex balloon code
/:cl:

---
## [ZetaSingularity/ZetaSpaces](https://github.com/ZetaSingularity/ZetaSpaces)@[0410075cc8...](https://github.com/ZetaSingularity/ZetaSpaces/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Monday 2023-04-10 00:22:35 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[997dac9616...](https://github.com/jlsnow301/tgstation/commit/997dac9616768643cfa9ddce53432d684e196fb1)
#### Monday 2023-04-10 00:36:02 by necromanceranne

Imports and Contraband: Different! Cargo crates without locks! MEAT! (#74490)

## About The Pull Request

### **Cargo Black Market goods should stay in cargo's hands**

#### New Cargo Console Category: Imports

This category is explicitly the non-departmental category beyond simply
having a Misc category. It is meant for material that nobody is meant to
be buying for their departments, and mostly for the odd-ball crates that
might show up. It also allows us to maintain contraband as exactly that;
contraband that the departments shouldn't have access too whatsoever. If
someone is buying from this category, they probably intend to be a
cheeky fuck.

<details>
  <summary>The New Changes</summary>

#### Baseline Imports

MEAT: MEAT (meat backpack you can eat)

<details>
  <summary>MEAT</summary>
  
![MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593459-f3c98abe-114b-43c1-a3e2-afc16b76c84f.png)
![MEAT MEAT MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593473-07a30781-a05e-4ca5-893b-778900cd2d1c.png)

</details>

Duct Spiders: They're adorable and cause a mess, but that doesn't stop
Nanotrasen from importing them from the Australicus sector to your
station!

Stack of 50 Bamboo Cuttings: Pretty expensive and kind of a premium.
Allows for those people looking to make bamboo decorations without
hoping botany exists, and are at least willing to pay. Also lets them
make horribly dangerous stuff with bamboo, of course.

A Single Sheet of Bananium: The problems this will cause I think speak
for themselves. (mostly due to a clown fruitlessly attempting to make
something actually disruptive while bankrupting cargo)

Natural Fish Bait: It isn't cheating, it's homemade. (Really good bait
but expensive and obviously drugs)

A dumpster...: A corpse in a dumpster, doesn't get more complicated than
that. Useful for corpse reasons.

Made using some code I borrowed from over here!
https://github.com/lizardqueenlexi/orbstation/pull/354

#### Contraband Imports

Foam Force Pistols: Same as it ever was with a price reduction. I
brought it down because riot darts are like 8 bullets a clip, and do
less damage than a disabler using riot darts. It feels like a sidegrade
weapon, and even if it technically is a ballistic weapon, it...isn't
that strong. I think this is pretty safe.

Definitely Not a Duct Spider: It's actually a giant spider in a box. If
you want to waste cargo's money while also sending them a mess to deal
with, this is the crate for you.

Russian Surplus Military Gear Crate: I took this opportunity to futz
with boltaction rifles. There are two kinds of mosin nagant you can get
in this crate. One of them is the good kind (no jamming). The other is
the shit kind (yes jamming), but you get more of them. You can get the
good ammo, or you can get the shit ammo. You'll have to pick through it
a lot more carefully to make sure you know which ones you've received.
Since this dilutes the pool even further, getting a good number of
mosins that aren't trash is even more expensive, and even if you do get
mosins at all, you might still only get the bad ammunition that doesn't
work against actual human threats as well. It also now cannot be
purchased through the security cargo supply console, and as to why they
could in the first place baffles me. Doesn't have a lock anymore
because...it's contraband? Who is locking this stuff?

**Side note: _You can make surplus 7.62 in the autolathe as well. It is
not very good except to fight fauna or naked assistants._**

**Side Side note: _I've killed off the shitty brand_new subtype and
brought peace once more to this land._**

#### Illegal Imports (Emag)

NULL_ENTRY: A journal that suggests how to make a...very interesting
weapon. The Regal Condor. Kind of an evolution on some other ideas I've
had over the years. This one is basically a secret weapon with a few
hurdles to jump through. Very lethal. Very expensive.

**Side note: _For reference, it's effectively 19 TC worth of gear to
make, but there does exist some methods to acquire this more cheaply if
you can get some bits and pieces from world spawns. Given it requires
you to get some pieces of equipment that might require additional
purchases of contraband, and getting into the captain's office to loot a
specific piece of clothing, the stakes more than make up for the
effectiveness._**

Smuggled WT-550 Autorifle Crate: This is basically the same, but you
might have noticed had you recently attempted, like me, to buy these
when you emagged them using a personal account and discovered a tragic
oversight. You couldn't, because they still needed armory access. This
removes that access, because you've already gone to the effort of
getting your hands on an illicit firearm through cargo, and if they
techs somehow miss the fact that you've purchased a WT-550...all the
better for you!

Smuggled WT-550 Ammo Crate: Includes AP and Incendiary!

**Side note: _You can get WT-550 ammo again via the Illegal Technology
node._**

Shocktrooper: Replaces the Special Ops crate. Contains a box of EMPs,
smoke grenades, a couple of gluon grenades and a couple of frag
grenades. Funsies.

Special Ops: The NEW Special Ops crate. Contains a chameleon mask,
jumpsuit and agent card. And a knife.

**Side note: _This is what appears in some cargo loan events._**

Refurbished Mosin Nagant Crate: The actual good mosin nagants. There are
6 of them. But they don't come with spare ammo. Hand them out to your
techs!
</details>

#### New Crates

- MEAT crate - Standard
- Duct Spider crate - Standard
- Giant Hostile Spider crate - Contraband
- 50 sheets of Bamboo crate - Standard
- A single sheet of bananium crate - Standard
- Natural (drugs) fish bait - Standard
- Dumpster with a corpse in it - Standard
- Shocktrooper crate (Grenades) - Emag
- Special Ops crate (Disguise) - Emag - Appears in some cargo loan
events
- Refurbished Mosin Nagant crate - Emag
- Regal Condor construction journal (NULL_ENTRY) - Emag

#### Changed Crates

- Foam Force Pistols (cheaper) - Contraband
- Russian Surplus Crate (less reliable, can't be bought by security
console) - Contraband
- WT-550 crate (more obtainable via personal accounts, thus
incriminating, not armory locked) - Emag
- WT-550 ammo (includes incendiary and AP) - Emag

#### Crates that got moved, unchanged, into Imports

- Foam Force Crate 
- Cosa Nostra Crate 
- Black Market LTSRBT 
- 'Contraband' Crate 
- Biker Gang Crate

#### Not crate changes
- You can print Surplus 7.62 (same as normal 7.62 but it sucks against
armor) from hacked autolathes.
- You can get WT-550 ammo from illegal tech.
- Removes the redundant Brand New Mosin subtype
- Fixes a potential exploit with jamming chance on Mosins.

## Why It's Good For The Game

I just think some of the magic of Cargo getting their hands on obviously
dangerous equipment and either hording it for themselves or attempting
to pawn it off was lost in recent times. A lot of this 'black market'
gear, however, suddenly became openly available to the crew anyway. For
_free_. Contraband crates and mafia crates could be purchased via the
Service budget. Security could just stock up en masse on mosins through
their console. And one fairly unfortunate consequence of a few recent
changes has made it nearly impossible to actually get illicit gear in
the first place, even if you did go to the effort of getting the money
for it.

On top of this, most of cargo's goods are pretty safe purchases. There
isn't much that would be considered 'actually a really bad idea to buy'
other than maybe supermatter shards. I wouldn't mind there existing ways
for someone to waste cargo's money while also causing them to have to
clean up the mess.

## Changelog
:cl:
balance: A significant overhaul of various illicit and dubiously legal
goods and gadgets available via cargo.
balance: Cargo now has an Import category for all non-departmental
goods. (And black market goods)
balance: Most contraband that already exists has been moved into
Imports.
adds: Includes several new imports of dubious quality. You get what you
pay for.
code: Removes the brand new mosin subtype as it is now defunct.
fix: Fixes potentially exploitative code in the jamming proc. Cleans up
that code while I'm at it.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [EdwardNashton/mojave-sun-13](https://github.com/EdwardNashton/mojave-sun-13)@[237789979a...](https://github.com/EdwardNashton/mojave-sun-13/commit/237789979a56a09589e299cf362a090ae8273805)
#### Monday 2023-04-10 01:22:31 by ProfessorPopoff

Drought babyyyy!! Spawners/Mobs distribution. Baron town and more (#2326)

Okay! So basically this is an unatomized PR. This adds in a lot of things that we need for Drought to be the best it can. It includes things like a mappersprite edit cape for the Baron.... Crafted terminal fixes... A bunch of structure visual shifts, new pipes added- a metric FRICK ton of new walls SPECIFICALLY FOR DROUGHT.

Legion have gender checks now. If you're not a male, it makes you a male and gives you a random legion name. They're pretty cool. Similar situation with the Baron. Female becomes male. Gets cool name. You get the jist.

NOMADS. Nomads are Wastelanders that look different. Specifically for Drought. yippie.

On top of any coding changes, obviously there's a ton of work put into Drought itself. There's mobs and loot dispersed through the map. Well? I don't know yet. We'll see in testing. I personally added two locations. The Barony, and some little adobe shacks on the long stretch to the raider base. I've fixed up a TON of errors, go count them all! There's likely more left. I was as thorough as I could be.

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[018db9ab81...](https://github.com/Jolly-66/dragon-station/commit/018db9ab81453478875e2af9e7dcb7deae959bf3)
#### Monday 2023-04-10 01:27:33 by SkyratBot

[MIRROR] Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs [MDB IGNORE] (#20337)

* Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs (#74225)

## About The Pull Request
Reduces the price of the Doomsday equipment by 20 PT for each APC hacked
in a Head of Staff office, as well as the Vault.
## Why It's Good For The Game
See #71404 for the prior PR and my full reasoning.

Long-story short, activating the Doomsday before having a plan in place
is suicide, and it takes 13 APCs to unlock. Since there are few well
hidden APCs in general, you'll usually be gathering APCs after going
loud (such as with a borg machine). 13 APCs is 13 minutes, and by the
time you've gathered your malfbux, you're either already dead or have
already taken full control.

I had intended to give Doomsday a flat 70 PT price, but concerns were
raised that an AI could conceivably hack only APCs on their sat (and
perhaps one on the Lavaland outpost) and Doomsday without ever really
touching the station*. So a compromise was proposed, we instead give the
AI discounts by hacking Head of Staff areas, and the Vault, which are
usually situated in well-traveled areas, and also have some fluff
reasoning.

*I still think it'd be suicide to do this, but it's not a hill I want to
die on.
## Changelog
:cl:
balance: Malf AIs that hack Head of Staff and Vault APCs will now find a
discount issued on Doomsday.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs

---------

Co-authored-by: zxaber <37497534+zxaber@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[b828a9851b...](https://github.com/Jolly-66/dragon-station/commit/b828a9851b193f94acd182677d971da01e6d215b)
#### Monday 2023-04-10 01:27:33 by SkyratBot

[MIRROR] Icemoon Hermit Ruin Active Turf Fix - For Real This Time [MDB IGNORE] (#20325)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[54b27a78b5...](https://github.com/Jolly-66/dragon-station/commit/54b27a78b5559d99d84577a8a38c39ca5cb52851)
#### Monday 2023-04-10 01:27:33 by SkyratBot

[MIRROR] IceBoxStation More Active Turf Fixes [MDB IGNORE] (#20339)

* IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request

![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

* IceBoxStation More Active Turf Fixes

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Atemo/rathena](https://github.com/Atemo/rathena)@[d617d9f083...](https://github.com/Atemo/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Monday 2023-04-10 01:39:56 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [ArchipelagoMW/Archipelago](https://github.com/ArchipelagoMW/Archipelago)@[6d13dc4944...](https://github.com/ArchipelagoMW/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Monday 2023-04-10 02:15:44 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [jdhovie/libgdx](https://github.com/jdhovie/libgdx)@[e1d1fdc5fb...](https://github.com/jdhovie/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Monday 2023-04-10 02:29:42 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [Yurazaqadri/Heart-Stroke-Analysis](https://github.com/Yurazaqadri/Heart-Stroke-Analysis)@[1e89dc543d...](https://github.com/Yurazaqadri/Heart-Stroke-Analysis/commit/1e89dc543d7448889faf1ecda5442513cc7bbf05)
#### Monday 2023-04-10 05:09:23 by YURAJA KADARI

Add files via upload

Dataset Explanation: 
The stroke dataset is a collection of data related to individuals who have had a stroke, as well as some who have not. It contains information on various factors that are known to be associated with stroke, including age, gender, marital status, hypertension, heart disease, occupation, place of residence, smoking status, and various health metrics. The dataset is commonly used in machine learning and statistical analysis to develop predictive models for stroke risk.

Here is a brief explanation of each column in the dataset:

id: A unique identifier for everyone in the dataset.
gender: The gender of the individual, recorded as "Male", "Female", or "Other".
age: The age of the individual in years.
married: Whether the individual is currently married or not, recorded as "Yes" or "No".
hypertension: Whether the individual has hypertension (high blood pressure), recorded as 1 if present and 0 if not.
heart_disease: Whether the individual has a history of heart disease, recorded as 1 if present and 0 if not.
occupation: The occupation of the individual, recorded as "Goverment Job", "Private Job", "Self-employed", "Children", or "Never Worked".
residence: The type of residence of the individual, recorded as "Urban" or "Rural".
metric_1: A health metric related to the level of glucose in the blood.
metric_2: A health metric related to the level of body mass index (BMI).
metric_3: A health metric related to the level of physical activity.
metric_4: A health metric related to the level of total cholesterol in the blood.
metric_5: A health metric related to the level of systolic blood pressure.
smoking_status: The smoking status of the individual, recorded as "formerly smoked", "never smoked", "smokes", or "Unknown".
stroke: Whether the individual has had a stroke, recorded as 1 if yes and 0 if no.
Overall, this dataset provides a rich set of information about individuals who have had strokes, which can be used to develop models for predicting stroke risk and improving stroke prevention efforts.

---
## [guspan-tanadi/violet_railsfromrestarone](https://github.com/guspan-tanadi/violet_railsfromrestarone)@[3d13e4c7fd...](https://github.com/guspan-tanadi/violet_railsfromrestarone/commit/3d13e4c7fdb101fb91297dea864eb7ee409746eb)
#### Monday 2023-04-10 06:34:02 by Don Restarone

[fix] optimize analytics V2 further + lockdown profiler (#1522) (#1523)

Addresses: https://github.com/restarone/violet_rails/issues/1399 and https://github.com/restarone/violet_rails/issues/1452

## Profiling Results 📈 🧪 


### Slight improvements to user experience

When analysis going back 1 year is shown, there is a noticeable performance improvement:

<img width="1728" alt="Screen Shot 2023-04-08 at 11 03 31 AM" src="https://user-images.githubusercontent.com/35935196/230728720-31d5d2c0-83e0-4aa2-b3ef-fede1458ff4f.png">

### Less memory & objects used
When a 1 year analysis is shown, less memory and objects are allocated and retained: 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 04 09 AM" src="https://user-images.githubusercontent.com/35935196/230728751-5302c578-4240-4f77-8ac8-166d2046be27.png">

### Garbage collector is running consistently 
on a per request basis, we observe that the garbage collector runs before the request is served. Indicating that used memory has been drained and freed to be used for other requests. 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 06 48 AM" src="https://user-images.githubusercontent.com/35935196/230728822-c1f86bd8-b8fb-45ee-86fa-848c27698a6f.png">


# Real life example, Marked Restaurant

## Resource usage

comparison of memory / CPU usage before and after patch

### Baseline 🆎 

The "resting memory rate" for a high traffic Violet system is around 600MB: 
<img width="1728" alt="Screen Shot 2023-04-09 at 11 44 16 AM" src="https://user-images.githubusercontent.com/35935196/230782692-84553698-fc07-4392-b7e6-45cda169d370.png">

### Before ⏪ 

Viewing the 1 year analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 23 AM" src="https://user-images.githubusercontent.com/35935196/230782749-11df1621-27ce-4b08-bf65-3625e5eddf7f.png">

Viewing the 1 month analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 08 AM" src="https://user-images.githubusercontent.com/35935196/230782771-8801aa10-13c3-4bc5-82bc-70d09924000b.png">

We observe 1.2 GB of memory use (double the resting rate)

Profiler result 📈 
While attempting to run the memory profiler on the 1 year analysis, we observed 3GB+ of memory usage ⚠️ 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 43 51 AM" src="https://user-images.githubusercontent.com/35935196/230782803-0ca221c6-976b-4e28-a669-67f8e196f6d0.png">

⭐  After the test was run, puma was restarted to ensure system stability

### After ⏩ 

Viewing the 1 year analysis: 
<img width="1728" alt="Screen Shot 2023-04-09 at 12 08 06 PM" src="https://user-images.githubusercontent.com/35935196/230783850-ee5963b2-7280-4323-9dbf-73812671b040.png">

We observe 720MB of memory use

Viewing the 1 month analysis:
<img width="1728" alt="Screen Shot 2023-04-09 at 12 11 44 PM" src="https://user-images.githubusercontent.com/35935196/230783889-8fb54846-47d0-487f-9480-3ded87fc7217.png">

We observe 850 MB of memory use 


Profiler result 📈 
We observe 900MB of memory use when profiling the 1 year analysis
<img width="1728" alt="Screen Shot 2023-04-09 at 12 10 11 PM" src="https://user-images.githubusercontent.com/35935196/230783899-5a66ded5-8529-4900-aab2-9003d89e06b1.png">

### Result

The system is now consuming memory in analytics V2 comparable to its resting memory usage rate. 







Co-authored-by: Prashant <25191509+alis-khadka@users.noreply.github.com>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[c0ef4ba907...](https://github.com/JohnFulpWillard/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Monday 2023-04-10 06:36:12 by tralezab

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
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[ccef887efe...](https://github.com/JohnFulpWillard/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Monday 2023-04-10 06:36:12 by san7890

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
## [RichieDevR/gpt4all-ui](https://github.com/RichieDevR/gpt4all-ui)@[cbf446b3e2...](https://github.com/RichieDevR/gpt4all-ui/commit/cbf446b3e28f4e53791f968c20b6888b4c40c9e8)
#### Monday 2023-04-10 07:30:30 by Richard Rosario

Update README.md (This really bugged me sorry lol)

got rid of the doubling of "GitHub Repository" as the hyperlink text does the job of rendering the text and providing the link. I'm sure it was a typo no biggie, honestly a super trivial edit I'm aware but it was driving me crazy!

*from this:*
If you are interested in learning more about this groundbreaking project, visit their Github repository [github repository](https://github.com/nomic-ai/gpt4all), where you can find comprehensive information regarding the app's functionalities and technical details. Moreover, you can delve deeper into the training process and database by going through their detailed Technical report, available for download at [Technical report](https://s3.amazonaws.com/static.nomic.ai/gpt4all/2023_GPT4All_Technical_Report.pdf).

*To this:*

If you are interested in learning more about this groundbreaking project, visit their [github repository](https://github.com/nomic-ai/gpt4all), where you can find comprehensive information regarding the app's functionalities and technical details. Moreover, you can delve deeper into the training process and database by going through their detailed Technical report, available for download at [Technical report](https://s3.amazonaws.com/static.nomic.ai/gpt4all/2023_GPT4All_Technical_Report.pdf).

---
## [jupyterkat/tgstation](https://github.com/jupyterkat/tgstation)@[c3b78761d2...](https://github.com/jupyterkat/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Monday 2023-04-10 10:44:35 by tralezab

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
## [jupyterkat/tgstation](https://github.com/jupyterkat/tgstation)@[b5ebf5c942...](https://github.com/jupyterkat/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Monday 2023-04-10 10:44:35 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [evrenkaraarslan/next.js](https://github.com/evrenkaraarslan/next.js)@[268dd6e80b...](https://github.com/evrenkaraarslan/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Monday 2023-04-10 11:50:25 by José Fernando Höwer Barbosa

Simplify with-google-analytics example (#43894)

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->
## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm build && pnpm lint`
- [x] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

First of all thanks for this amazing project and all the help you
provide with these examples.

It seems there is code duplication in this example. After some tests
locally seem to _document.js is not necessary for `gtag` to work
properly.


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_app.js#L30-L34


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_document.js#L13-L17

I am aware of https://github.com/vercel/next.js/pull/40645 and I would
like to ask @dave-hay, @SukkaW and @ijjk to consider this is still
necessary. If so why then not move all content of the scripts from _app
to _document?

In any case, I am open to adding here some comments explaining what is
the reason for this code duplication if necessary.

<hr/>

Changes that come from  https://github.com/vercel/next.js/pull/43897

1. The `event` hashChangeComplete should be removed since `/home` and
`/home/#section` is not new pageview, but just reference to the same
page.

If we go from /home to /home/#section (with a button click or a link for
example) this shouldn't trigger a new page visit on `gtag`.

For this reason, I think we should revert the changes from
https://github.com/vercel/next.js/pull/36079. If there is a better
argument of why this should stay I am also open to creating comments to
clarify this on the example since I don't think should be the default
behavior and not useful in most cases.

2. The `id="gtag-init"` was added with no context to the example from
https://github.com/vercel/next.js/pull/29530

If there is a reason for this id in the script to existing I am open to
adding a comment that clarifies this since in my experience is not
necessary at all.


Edit: Batching with https://github.com/vercel/next.js/pull/43897 as
recommended by
https://github.com/vercel/next.js/pull/43897#issuecomment-1344635000

---------

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [matrix-org/synapse](https://github.com/matrix-org/synapse)@[3ba755672c...](https://github.com/matrix-org/synapse/commit/3ba755672c0b8d6a6b705b746893fb1ea24306e7)
#### Monday 2023-04-10 12:17:41 by David Robertson

Inline backend-meta linting config

This has caused us too much pain---it makes things especially hard to
debug. I don't think the indirection is worth it, since we haven't used
it in anger across all of our projects.

Additionally: I think I'm coming round to the view that

- all CI config is a mess,
- efforts to reduce duplication are a Sisephean struggle that aren't
  worth it, so
- just copy and paste it and move on with your life.

Or perhaps this is just a crisis of faith?

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[11cbbba018...](https://github.com/bob-b-b/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Monday 2023-04-10 12:29:01 by Sol N

Replaceable Traitor Uplinks (#74315)

## About The Pull Request

Following [from the suggestion in this hackmd
](https://hackmd.io/IkDWWkpfQa2lkdevsnLqhA?view#Replacement-Uplinks)with
a few twists of my own, I have made a method for traitors to acquire a
replacement traitor uplink that has its own set of flaws and limiters in
order to prevent abuse.


![ZC0WYDFRzc](https://user-images.githubusercontent.com/116288367/228101432-9352390b-9538-4c62-8dc4-55e2e798c466.png)

The basic pitch is as follows, all traitors now start with a new,
crafting recipe exclusive to them, it costs a teleport beacon, a
bluespace crystal, and some iron and cable coil, and then allows them to
build a static, dense machine that they can synchronize with, which
allows the machine to know what signal it should be looking out for from
the traitor.

![dreamseeker_iErI3vju0C](https://user-images.githubusercontent.com/116288367/228094286-c2bca198-82cd-4ce0-a4a7-c26c24a9327c.gif)

The traitor then uses any radio, sets it to the frequency that has been
added to their static antagonist ui, and then speaks their codeword,
also in the ui, and then a few things happen.

![dreamseeker_gbzSFeHuS5](https://user-images.githubusercontent.com/116288367/228094354-a649c713-f013-4ac2-b8d7-0754a852f987.gif)

Most obviously, they get a replacement uplink that is in the conspicuous
shape of the nukie or lone op uplink. This uplink can be unlocked by
speaking your replacement codeword to it again, it remembers your
previous TC amount and locks all other uplinks associated with your
uplink handler(they can then be unlocked as normal). It also destroys
any other replacement uplinks associated with your uplink handler, which
means you can never have more than one replacement uplink.

This means that if your uplink has been confiscated and you left it
unlocked, if it hasn't been emptied out you can continue from where you
were, and if you want to get back on the TC grind you won't lose the new
TC to whoever stole your uplink. Of course, the new uplink can not be
locked, so you have to be more careful with it or buy an uplink implant
and destroy it. You can destroy your replacement uplink with a
screwdriver right click, same for the machine.

Additionally, the Syndicate Uplink Beacon has another quirk to it, which
is that the teleporter beacon used to create it is intact, which means
people eagle eyed on the teleporter console could go find you, not to
mention that if you use an existing teleporter beacon, someone might
notice its gone missing...

oh also while making the replacement uplink i found a bug caused by a
recent pr that broke debug uplinks due to them not having a purchase
log. thats fixed too

## Why It's Good For The Game

It can be easy to lose your uplink, and as a traitor having your uplink
confiscated, even if it is locked, feels really bad. While the old
traitor objectives were added back to prog traitor to prevent situations
where a confiscated uplink meant that you were completely aimless, I
think that having a backup solution would be good for more inexperienced
traitors or for ones who get unlucky.

Hopefully this is generally balanced well enough but there are a few
levers that can be pulled, but overall I do think that making it so that
traitors can always get a chance to get an uplink and do some objectives
is good for the game. I like the idea of someone getting perma'd,
someone breaks them out, they both craft a new uplink beacon, and then
they go back and get the traitors old gear with stuff they got from the
new uplink, I think that's a cool possibility to throw into the sandbox.

## Changelog
:cl:
add: Added new syndicate uplink beacon and associated systems that allow
you to get a replacement traitor uplink
fix: Debug & nukie uplinks no longer runtime and work properly again
/:cl:

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[00f8bcfe75...](https://github.com/bob-b-b/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Monday 2023-04-10 12:29:01 by MrMelbert

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction
 
- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one. 

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

---
## [berinaniesh/portage](https://github.com/berinaniesh/portage)@[28cd240fb2...](https://github.com/berinaniesh/portage/commit/28cd240fb23d880b8641a058831c6762db71c3e2)
#### Monday 2023-04-10 13:24:12 by Sam James

emerge-webrsync: support PGP verification via gemato

Introduce PGP verification of the webrsync snapshot tarballs
using app-portage/gemato - which is already a dependency of Portage
for verifying normal rsync.

This is the same method Portage uses (see below).

Technical changes before we dive into the rationale:
- Use gemato for PGP verification just like Portage does for
  sync-type=webrsync, sync-type=rsync (although that uses a metamanifest),
  and sync-type=git (although that uses gemato for gpg-wrap, so works differently).

- Use gentoo-functions automagically if available for better output
  functions.

- Be more verbose about verification and various other operations,
  while also respecting --quiet if passed for misc. existing & new
  messages.

- Make --verbose a no-op. There weren't enough output messages
  to justify three states (--quiet, normal, --verbose).

- Bail out more aggressively in the event of errors or "warnings".

- Use modern terminology for repository, etc (avoid overloading the
  "portage" term.)

- Allow disabling PGP verification with --no-pgp-verify.

Technically, the fix is very straightforward, but getting to
the fix was the slightly painful bit. What I've concluded
happened is:
- Portage starts getting reworked to gain proper sync module support;

- Someone gets the idea of implementing emerge-webrsync fully in Python
  as a Portage sync module (which is a not-unreasonable idea);

  [This ultimately hasn't gone anywhere, and in fact, while working on this
  bug, I ended up finding a bunch of typos that meant you couldn't even test it.
  But it's a stub anyway.]

- The idea of deprecating emerge-webrsync is floated around. The idea
  being Portage should call it via its new sync module with sync-type=webrsync.

  This is presumably with the ultimate goal of it transparently one day
  using the aforementioned (yet-non-existent) Python implementation as its
  backend, and not the shell script.

  [To this day, Portage's webrsync implementation shells out to the emerge-webrsync
  shell script, but it has the abstraction to switch that out, in theory.]

- At the time, PGP verification in general of the Gentoo
  repository is an active topic, especially now we'd migrated to git which makes
  it way easier, unlike CVS.

- A bug is filed for PGP verification in emerge-webrsync.

  People decide it doesn't matter too much, because Portage is going to
  Real Soon Now (TM) have its own backend (replacing the shell script) and/or
  Portage's sync module support obsoletes emerge-webrsync entirely.

  The idea here, I think, being that nobody should call emerge-webrsync and
  everyone should just call emerge (or emaint) to sync as appropriate.

  [This isn't a terrible idea in a sense, but it needs a better basis:
  we should probably make emerge-webrsync a wrapper which creates a temporary
  repo config to forcefully webrsync a repository if the user asks us to. This
  is what people expect from emerge-webrsync with the default sync-type=rsync
  in repos.conf for ::gentoo.

  I actually started implementing this before I realised that emerge was
  shelling out to emerge-webrsync, so have postponed it.]

- Then nothing happens with the "replacement" ideas and the good
  ol' trusty emerge-webrsync ends up with the same problems sitting
  there because nobody saw the point in working on it if it was to
  be replaced soon. But that didn't happen.

The fix overall for this is pretty small, but the commit is larger
than I'd like because I had to rework a few things to sensibly allow
disabling PGP verification as well as follow the flow.

(I did start splitting up this commit but ultimately it needs -w
for best review even without the output tweaks in this commit and
deconstructing this for atomic commits would end up being more brittle
as I couldn't be as confident in the result.)

Bug: https://bugs.gentoo.org/597800
Signed-off-by: Sam James <sam@gentoo.org>

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[a2d5ca6e69...](https://github.com/PhantomEpicness/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Monday 2023-04-10 13:30:03 by QuickLode

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
## [TheParasiteProject/frameworks_base](https://github.com/TheParasiteProject/frameworks_base)@[d722b159c6...](https://github.com/TheParasiteProject/frameworks_base/commit/d722b159c6e0500ec962d6207a9b808b3bb01fa1)
#### Monday 2023-04-10 13:40:41 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [romland/llemmings](https://github.com/romland/llemmings)@[f2b181fe1e...](https://github.com/romland/llemmings/commit/f2b181fe1e1c6c6a1dc5e7fb8a1fc00caa52ca7a)
#### Monday 2023-04-10 13:56:20 by Joakim Romland

A plausible Builder
ChatGPT: 2 prompts below

Prompt note: I had to fix several bugs in the output from this prompt, it was costly
in time and after having done it a few times, I just caved in and cheated and fixed
the bugs instead of the prompt. The prompt got a bit too complex, it should have
been simplified for the LLM to be able to do it.

>>> Prompt 1:
We're making a game with lemmings of various types, using javascript and canvas.

One type of lemming is the Builder, when activated, it should build a bridge like this:

Here's ASCII to illustrate:

___L_/

Where
_ = ground
L = lemming heading to the right
/ = a segment of bridge at an angle of 30 degrees that the lemming should be building

- the action property is already set to "Builder" you don't need to do anything with that
- in the direction it is walking (this.velX), it should build a bridge at around
  30 degrees upwards by coloring pixels on the canvas using the function:
  setPixel(x, y, color) where color is an array of three bytes [r,g,b], the color
  to use is in dirtColorBytes
- the bridge should start at the lemmings feet and BUILDER_LOOK_AHEAD (add a const of 4)
  pixels in front of lemming, and it should at a maximum build BUILDER_LOOK_AHEAD * height pixels
  per frame. That is: x = lemming's x+width and lemming's y+height+BUILDER_LOOK_AHEAD
- the bridge should be 4 pixels high
- check bounds of canvas, don't attempt to set change outside it. Check against
  canvas.height and canvas.width
- bridges can only be built where the pixel color is black, find the array in the global
  blackColorBytes
- if the bridge runs into a wall or another obstacle, lemming should stop building and
  lose its Builder status
- implement the Builder in its own function called "build" where a "lemming" is the
  only thing being passed in
- the function should return true if it built something, false otherwise
- it can only build if the lemming is currently on the ground
- it cannot build if it is already assigned another action
- the moment the lemming starts a new bridge (that is, start spending building material),
  it should set actionStarted to true, and at some point later when it has spent all the
  bridge building material, set it to false
- only a little bit of the bridge is built every frame the function is called, so you need
  to keep track how how much was built this frame to know when to exit the function.
- The total pixels must be kept track of to know when it should stop building because it spent
  all its bridge-building material. After which the lemming should stand still for (pause)
  for 120 frames. Set a property called 'standStillUntil' in the lemming for when it should
  stand still -- don't use a date for timing, you can get current frame number by looking
  at Lemming's age.
- despite lemming moving, between frames it should always just continue building where it
  stopped building the previous frame

These things already exist, use them, don't reimplement them:
A lemming has these properties:
age = 0;
width = 10;
height = 20;
x = x;
y = y;
velX = 0;
velY = 0;
onGround = false;
isClimbing = false;
isDead = false;
action = null;
actionStarted = false;

X/Y/velX/velY in the lemming are doubles, to work with individual pixels make sure you use ints

Check collision with obstacles using this (it checks whether there is an obstacle at waist height):
let hitWallOnLeft = this.velX < 0 && isPixelOneOf(oldImgData, this.x - 1, this.y + this.height / 2, terrainColorBytes);
let hitWallOnRight = this.velX > 0 && isPixelOneOf(oldImgData, this.x + this.width + 1, this.y + this.height / 2, terrainColorBytes);

A pixel is just a normal pixel (1x1 pixels -- there are no tiles or blocks).
For operating on pixels, use isPixelOneOf() and setPixel() which are already implemented. Don't implement them again.

And for the love of god, don't use setTimeout() in a loop. For the pause you just need to set a flag in the lemming.

Give me only code, no need for explanation.

>>> Prompt 2:
The following code builds a bridge upwards correctly when a sprite is moving to the right (e.g. lemming.velX > 0).

Make it so that this also works the same way when the sprite is moving leftwards:

const BUILDER_LOOK_AHEAD = 4;
const BUILD_MATERIAL_CARRIED = 75;
const BUILD_PER_FRAME_MAX = 10;

function build(lemming)
{
    if (!lemming.onGround) {
        return false;
    }

    const startX = Math.floor(lemming.x + lemming.width + BUILDER_LOOK_AHEAD);
    const startY = Math.floor(lemming.y + lemming.height);

    if (startX >= canvas.width || startY >= canvas.height) {
        return false;
    }

    let pixelsBuilt = 0;
    if(!lemming.totalPixelsBuilt) {
      lemming.totalPixelsBuilt = 0;
    }

    let y = startY
    // HUMAN: TODO: This should check end of the bridge, not where lemming is?
    const obstacleOnLeft = lemming.velX < 0 && isPixelOneOf(oldImgData, startX - 1, y - lemming.height / 2, terrainColorBytes);
    const obstacleOnRight = lemming.velX > 0 && isPixelOneOf(oldImgData, startX + 1, y - lemming.height / 2, terrainColorBytes);

    if (obstacleOnLeft || obstacleOnRight) {
      // Do nothing
    } else {
      for (let x = startX; x < canvas.width && x < startX + 4 && pixelsBuilt <= BUILD_PER_FRAME_MAX; x++) {
        // HUMAN: TODO: This will allow for a lemming to build more than totalPixelsBuilt by at most BUILD_PER_FRAME -- need check
        if (isPixelOneOf(oldImgData, x, y, blackColorBytes)) {
          setPixel(x, y, dirtColorBytes);
          pixelsBuilt++;
          lemming.actionStarted = true;
        }
      }
      lemming.totalPixelsBuilt += pixelsBuilt;
    }

    if (obstacleOnLeft || obstacleOnRight || lemming.totalPixelsBuilt >= BUILD_MATERIAL_CARRIED) {
        lemming.totalPixelsBuilt = 0;
        lemming.standStillUntil = lemming.age + 120;
        lemming.action = null;
        lemming.actionStarted = false;
        return false;
    }

    return pixelsBuilt > 0;
}

---
## [cfeatgit/org.openhab.binding.zwave](https://github.com/cfeatgit/org.openhab.binding.zwave)@[7e710866ea...](https://github.com/cfeatgit/org.openhab.binding.zwave/commit/7e710866ea8041a7e80b60d8b72a0534a5e89a6e)
#### Monday 2023-04-10 14:36:37 by Robert Eckhoff

Zwave battery device optimization (#1760)

* “One and DONE” - Zwave battery device optimization

This PR is to optimize the user experience of initializing new Zwave battery devices. The desired result is to be able to put a battery in the shiny new device, follow the device manual inclusion protocol during an Inbox, Zwave binding “Scan” mode of OpenHab and, in 20 seconds or less, have all the channels displayed and begin to link them to items. “One and DONE”.
Since my last unmerged battery device PRs I have replaced the fixed 20 second cap in the iterative sleep timer with a user defined maximum “hold awake” parameter. As the user defined default is five seconds, there is no implied maintainer approval of a longer awake duration. Kind of a “use at your own risk” feature. Once the device is DONE (or the cap is reached) the sleep message (No More Information-NMI) is created. Setting a higher user defined cap does not mean increased battery usage. With half second intervals, versus 5 seconds in today’s binding, daily battery device awake duration is either the same or reduced.
Also added is a kick-Queue action after the half second mark in the Timer Task to get a potentially “stuck” device queue going again. In some scenarios (primarily during initialization, the existing kick-Queue action appears to happen too early (before the event listener sets the device awake). There are examples from the forum in my attached document. I was able to recreate the “stuck” scenario (by reverting the second “Add Node Stop” & Sleep Timer cap to 5 seconds) and resolve the “stuck” problem on my test device with this additional kick-Queue.
Lastly, I have added the shortened timeout for the second calling of the “Add Node Stop” to make this a complete package. It has the most impact as anything else to “One and DONE”. The default 5 seconds to cancel this command eats up about 4 seconds of the Timer leaving only one second left in the initial awake interval. Some of the other enhancements in this PR would have less impact, if a full 5 seconds were available for device initialization after device discovery.
I have all the changes in this PR running, some for as long as 8 months (as of Jan 2022). I have 13 battery nodes of various manufacturers (47 total) on an Rpi4 with an Rpi3b test system. It is frustrating to see the battery device initialization issues in the forum, as I know they can be resolved better than the standard “reawake many, many times” advice. These changes will save considerable user frustration and many seconds of battery usage.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Requested Changes mostly

We still need to discuss my appeal on the AddNode Stop and get on the same page on how the count works.  It is not the same as in #1100 with the "return;"
Signed-off-by: Bob Eckhoff katmandodo@yahoo.com

* Delete AddNode changes

Mainly delete the changes in the Addnode class, plus address other minor changes

Signed-off-by: Bob Eckhoff katmandodo@yahoo.com

* Update README with maxAwakePeriod

Added section of maxAwakePeriod in the README, added a missing line, commented on the kickQueue.

Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Update maxAwake without initialization and xml edits

Your suggestion led me to realize I could “push” the maxAwakePeriod from the ZWaveControllerHandler configuration editor down to the ZwaveController where it could be “pulled” by the Zwave Node. It’s not exactly how you suggested, but I wanted to make the smallest possible amount of changes, so as to not mess up the other parameters. Not a lot of testing, but I could change in the UI and check in the wake Timer Task that it was being used.  It also still could be changed via re-initialization using the UI page “code” tab, so I think it is good.
Also in the commit I changed the default maxAwakePeriod to 10 seconds and raised the minimum back to 5. With the AddNode changes removed (adding 4 seconds of inactivity), the minimum of 2 seconds will simply not work. As to the default, I detailed 2 tests at 5 seconds and two at 10 seconds and summarized them below

Node	Max Awake	# of awakes to DONE	Total User time Fiddling with Action button	Total Device Awake (inludes late starts, message timeouts)
2	5 seconds	6	6 minutes 40 seconds	22.7 seconds
3	5	4	2 minutes 40 seconds	24.1 seconds
4	10	1	6.5 seconds (estimated-zniffer)	6.5 seconds
6	10	1	 8 seconds	8 seconds

Once a partially initialized device needs to reawake, it is not seamless and a 10 second cap uses less battery time than a 5 second cap. Also this was me pressing the button and checking the device in the UI and I knew to keep at it.  Not everyone understands the need to keep pressing the action button with high frequency.  I would be a little sad that after all the work here, the default settings would only be slightly better than now. Yes, the parameter is now easy to change, but that is an extra step and is currently an advanced setting. I’d strongly prefer we start at 10 seconds and let people lower it if they think it is a problem (although my data proves it is not).
I also made some edits to the program comments, the JavaDocs and took out an unused method.

Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Attempt to fix .classpath& .project

Per my last comment these are autogenerated and should not be changed.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Move single use variable to where it is used?

I hope this is what you were looking for.  It's late on this side of the world, but though I would try to fix now.  If wrong, let me know and I will fix in AM.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Remove unneeded variable

I was also wondering if this was needed, but once I got it working did not want to mess with it !  Anyway it is gone now.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Change passed variable to int

This has worked for a few days, but it seems maxAwakeProperty should be int, not Integer.  I was converted to int in the Controller Handler. If not right I can revert..
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

---
## [sjuratov/dolly](https://github.com/sjuratov/dolly)@[af91832c66...](https://github.com/sjuratov/dolly/commit/af91832c663025b9d5b3bd0e01be125b91a51799)
#### Monday 2023-04-10 14:48:51 by Matthew Hayes

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
## [ca2/app-simple](https://github.com/ca2/app-simple)@[c0d66f0249...](https://github.com/ca2/app-simple/commit/c0d66f0249dc2991f6ac80a88de6070d3b342b4e)
#### Monday 2023-04-10 14:51:43 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS ] ca2 Stabilization and continuous integration and deployment implementation
<3ThomasBS_ILoveYOU!!

<3tbs, Mummi and bilbo!!

Thomas Borregaard Sørensen \infinity,-0.16091989,\infinity ONE-MAN
ABSOLUTE <3!! I love you, by ???-0.02041977-???write my history please
make me please create me for you for me for you for me Camilo Sasuke
Thomas Borregaard Sørensen!!

Thomas 3 private commits on mid Dec2020!!

Thomas Online YouTube VODs contribution!!

Mummi orange-rice-flour cake on 20-Dec!!

Mummi (tinytaura) watching and chatting contribution!!

bilbo sleeping and needing/requesting/crying for help care (for the right
person (me), the cats wanna fight with him) contribution!!

sodapoppin and friends contribution!!

iAssyrian chatting contribution!!

boflux (Spoofh, Benjamin Kuhl) chatting contribution!!

jusg_fpga (fpga_guru, vue_equalizer, just_fpga, Oliver Pohl) chatting
contribution!!

cmgriffing streaming contribution!!

TimBeaudet (Friends: FletcherLabs, tsjost and Jabokoe) streaming
contribution!!

Stumpen_nicklas_dk, sodapoppin and EduardoRFS streaming contribution!!

Roxkstar74 sleeping streaming contribution!!

kissloryshy chatting contribution!!

blackjekko from Padova Italia through twitch C++/ca2 interest
contribution!!

j_blow streaming contribution!!

boflux (Ben, Spoofh, from Germany) chatting contribution!!

parrot_rl chatting contribution (from New Jersey)!!

JPCdk streaming contribution!!

whyyyyyyysoserious streaming chess contribution!!

fpga_guru (vue_equalizer, Oliver from Deutsch)  C++/ca2 interest
contribution!!

SovereignDev with Unreal streaming contribution!!

Ash_F0x and TimBeaudet streaming contribution!!

Myrkee (Valheim) streaming contribution!!

xmetrix and EinfachUwe42 streaming contribution!!

JessicaMak and marcobrunodev streaming contribution!!

alfredotigolo, mandrakenk and Okbatgames chatting contribution!!

jitspoe, Endesga and Fearitself streaming contribution!!

jmcmorris (Jason Morris, SiegeGames) streaming contribution!!

tomrandall streaming Ludum contribution!!

vue_equalizer (fpga_guru) chatting contribution!!

Thiagovgamg chatting contribution!!

Naysayer88 and friends contribution!!

lelandkwong streaming contribution!!

Goldbargames streaming contribution!!

Bytakos (bytakos) streaming contribution!!

Endesga streaming contribution!!

jitspoe and strager streaming contribution!!

Ash_F0x and JessicaMak streaming contribution!!

WTSRetro/SpiffyDane and Myrkee streaming contribution!!

Ninja and friends streaming contribution!!

erald_guri chatting contribution!!

lastmiles streaming farwest contribution!!

rw_grim streaming contribution!!

AdamCYounis streaming contribution!!

Dunno (P4ndaExpress) chatting and streaming contribution!!

Zorchenhimer streaming contribution!!

lasteveq4 C++ interest chat contriubtion!!

cecilphillip and clarkio @"Microsoft Developer" streaming contribution!!

oijtx streaming contribution!!

diegobrando_linux (Bl4ck_gookoo) chatting contribution!!

jhovgaard streaming contribution!!

Klay4_ chatting contribution!!

HonestDanGames streaming contribution!!

NorthSeaHero streaming contribution!!

Trainwreckstv and friends streaming contribution!!

togglebit, GexYT and GoPirateSoftware streaming contribution!!

taiyoinoue, RetroMMO, OfficialAndyPyro and david_joffe streaming
contribution!!

Tjienta streaming contribution!!

Primeagen streaming contribution!!

Jaxstyle and friends streaming contribution!!

EduardRFS streaming contribution!!

Melchizedek6809 and btcfly streaming contribution!!

Llama0x0 and sov_l chatting contribution!!

TaleLearnCode streaming contribution!!

Carol phone call contribution and visit contribution!!

hvalen_hvalborg112 streaming contribution!!

harmannieves chatting contribution!! (After long time...)

darkfolt8 (French from France) chatting contribution!!

klintcsgo (CS GO: Counter-Strike Global Offensive) streaming
contribution!!

KASPERPURE (Super Mario 64) streaming contribution!!

SomewhatAccurate C++ streaming contribution!!

Listening to Bryan Adams, Westlife, Shayne Ward, MLTR, Backstreet Boys,
Boyzone - Best Love Songs Ever by Relax Song at YouTube!!

-- hi5 contribution...!!

at macOS Box in host running Windows 10 Pro remotely from bilbo machine running Windows 10 Pro!!
dedicated server by OVH.com at France, Gravelines
Intel Core i7-4790K - 4c/8t - 4 GHz/4.4 GHz RAM32 GB 1600 MHz 2×960 GB SSD SATA

---
## [edecosta-mw/git](https://github.com/edecosta-mw/git)@[eaa0fd6584...](https://github.com/edecosta-mw/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Monday 2023-04-10 15:46:21 by Jeff King

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
## [DeSinc/SallyBot](https://github.com/DeSinc/SallyBot)@[da25b2b107...](https://github.com/DeSinc/SallyBot/commit/da25b2b10757397cbaba7cfc2f82450b5369c31a)
#### Monday 2023-04-10 15:54:58 by DeSinc

Update Program.cs

GIGANTIC UPDATE, HUGE HUGE UPDATE, OOBABOOGA WORKS (KINDA) STABLE AND HAS A BIT OF MEMORY NOW. Known issues: emoji psychosis sets in if you set history too long. default is 500 chars but you can go up to ~4800 before errors from oobabooga server.
best model to use is ozcur/alpaca-native-4bit which is a 7B natively trained 4 bit model.
we think it is an oobabooga API bug that is causing the emoji and hashtag psychosis somehow. we have no clue how to fix it.

anyway enjoy!

---
## [ABJ4403/Payback2_CHEATus](https://github.com/ABJ4403/Payback2_CHEATus)@[a15a82650c...](https://github.com/ABJ4403/Payback2_CHEATus/commit/a15a82650ca06f3e8bf41a0f8c6588b393aa9da2)
#### Monday 2023-04-10 16:14:21 by MDP43140

Update Pb2Chts

Pb2Chts_2.3.0_rc1:
+ Annotation changes (including some typo fixes, especially the word "veichle").
+ change some gameguardian string format on gameguardian APIs (eg: gg.alert(f"__old__","__new__")).
+ GROUNDBREAKING (backend): remove "revert" (useless variable, gameguardian doesnt make any use of it), and remove "Restore previous value" button (as it depends on revert variable and its now removed).
+ god modes items modified slightly (some values changed, mostly changed is name).
+ Shorten vehicle color code.
+ put a warning for CBSS/64bit region users on cheat_xpmodifier function (known issue which makes the game fc when using certain coin/xp related hacks because of confusing offsets for different platforms).
+ Bug fixed: some XP/Coin cheats were swapped/incomplete.
+ shorten and simplified some helper functions (thanks to ChatGPT for some of this).
+ removed unused table.mergeContents function.
+ Bug fixed: when enabling god mode cheats using ABJ4403's auto anchor, and found dupes but refining found nothing, will crash (because i forgot to nil tmp0 (originally this was a temporary string, its supposed to be nil before return).

PS: lots of major update are about to come, stay tuned for the 2.3.0_rc2 release (hopefully...)

---
## [CrystalPerigean/va.gov-team](https://github.com/CrystalPerigean/va.gov-team)@[07be60bf24...](https://github.com/CrystalPerigean/va.gov-team/commit/07be60bf247990795d70c04a80feef513946ee3b)
#### Monday 2023-04-10 17:46:34 by CrystalPerigean

P6

# Session Notes: Income Limits App Usability Testing

## Warm-up Questions - 5 minutes

1. *I understand you are a (Veteran / Caregiver). Is that right?* Yes, I am. Retired Air Force.
	- *(If Caregiver, confirm:) Are you a caregiver for a Veteran? Are you a Veteran?*

1. *What kind of device are you using today?* A cell phone. It is an Android. You just tell me.
1. *How do you typically get information and benefits from the VA?* I used to go to VA.gov. 

1. *Do you have VA health care?* No I do not.

1.	*What have you heard about income eligibility for VA health care?* I really haven’t heard anything about it since I have been employed since retiring and I am using Tricare. I pay some annual fees.


1. *Do you get a pension from the VA?*  No I do not.

1. *Do you get VA disability compensation for a service-connected disability rating of 50% or higher?* No I do not.


## User Tasks

### Task 1: [Wayfinding] 
*(if they DON'T have VA health care) Let's say that you're wondering if you're eligible for VA health care with your current income.* 

*(if they already have VA health care) Let's say that your income just changed, and you want to know whether you're still eligible for VA health care or if your benefits might change.*

*if they have 50% or higher disability rating, do they say that income limits don't apply to them?*

*if they have a VA pension, do they say that income limits don't apply to them?*

*Can you show me how you would find out if you're eligible for VA health care with your current income?* Goes to VA.gov. I would just start looking at the site and go to apply now for VA healthcare. Check eligibility. Start with the application, or maybe go to programs and services to check that out. I probably wouldn’t go to the application right away. I think I would go to the programs and services at the bottom. Maybe I would do a search at the top for income eligibility. Annual income limits health benefits, right there. Okay this takes me to annual income limits, and this shows me.

### Task 2: [Open prototype] 

*What are your impressions of what you're looking at?* I think for the phone the text is a little too big for the phone I am using. I am using a Galaxy Z fold and the test is too big even for the bigger screen. It has good headings. I like how the information is laid out. It is definitely identifying as a VA website. 

*Could you try to use this to find out if you're eligible for VA health care with your current income? Please explain what you want to do before clicking anywhere.* I am just scrolling to see if I could find more information. I see a link that says check our current income limits. It has information about how it changes. I would click the get started. On this page I could verify my income to ensure I can qualify. Make sure I meet all the requirements prior to applying.


### Task 3: [Intro page of app] 
*What are your impressions of this page?*
*What do you think you can do here?*

*Do you think this tool would be useful for you or not? WHY?* Yes because these are questions, I have had in the past. The VA website has so much information that it can get overwhelming.

*If not, who would it be useful for?*


### Task 4: [Answer questions in app] 
*How would you use this? Please talk me through what you would do, but do not click anywhere yet.* I would click no because I did not get a pension last year. Did I get VA aid, and I would click no. Did I get a house allowance last year, that is a no. I like how these are simple questions. I would enter my zip code and hit continue. If I was doing this for real, I would put only one since it is just myself and my wife. My daughter is 28 years old and out of the house. Yeah, that is how we usually file is 1 dependent. I like that it gives you the option to go back and edit. I would just continue. It comes up with the income limits and tells me that I meet the limit.

- *(RECORD all comments and anything confusing about the interactions on each screen of the prototype:)*
 

### Task 5: [Results screen]
*What are your impressions of this page?* I like the page. The larger text on the phone is not bad because I do not have to get my glasses to read it. It is simple and it would take a short amount of time to go through. I would use this page to see if I met the income limits and go through the process to apply for benefits.

- *(RECORD: Which accordions did they open? How to estimate income / $29K / $29-43K / $43-81K / $81-90K / $90K or more)* If I expand that range, it states I may be eligible for some  healthcare and prescriptions. It means I would not have to pay for normal care and get medications. 
What do you mean by normal care? Checkups, acute care for sickness, colds, flus, anything like that which requires a doctor’s visits. I would not think it would cover surgeries. I guess it would be helpful if it gave more information on what type of care it would include.
What does copay mean to you? It is a small payment I would have to pay when I go to the doctor/prescription. Usually, $30, or less.

*Can you explain what this page means to you?*

*How is your income involved here?*

*If your salary last year was around $40,000, what might that mean for your eligibility for VA health care?*

*Can you tell me what benefits you might get?*

*If your salary last year was around $28,000, what might that mean?* Free care, free prescription, travel reimbursement, so if I had to go to a special VA, I would get money back for gas and lodging.

*If your salary last year was around $83,000, what might that mean?* I get healthcare with full copays and prescriptions. That is the only thing listed on there. The more income the copays come into play.

*If your salary last year was around $90,000, what might that mean?* I would still be in the same bracket, but if it was over $90,000, I would not be eligible unless I had a VA disability rating. 

*How sure are you that these benefits would apply if your salary was around $90,000?* It says you may not be eligible, but I would click on the link that states find out if you may be eligible. I would expect that I was not eligible since I do not have any disability.

- *How certain are you that you don't qualify for more benefits*? 

*What if your salary was around $100,000?* I would expect the same about the $90,000 or more unless I had a VA disability in the system.

*(RECORD all comments)*

### Task 6: [What next]
*Please stay on this screen. Based on what you see in this screen, what do you think about this information and the question of eligibility for VA health care?* The information is clear. I think there are one or two spots that could provide more information, like what is normal care would be. Just so you have a context to relate it to. It makes it easy to navigation and understand.
Is this the final answer? Is there anything else you need to do to see if what you see is correct? I would think this is correct. It gives you a point to go further down the road if there is anything else you can do to go through the process. The ones that are higher I don’t think it is not for sure you don’t qualify but you need to go through the process to see if you are eligible. I would click the link to see if I was eligible for VA healthcare underneath it.

*How would you decide what to do next?* 

*What would you do next?* I would go ahead and click on the link that states to find out to see if I was eligible.

*How did this tool help or not help you decide what to do?* It easily demonstrates what the brackets were and what benefits you would receive. That is the main point.

### Task 7: [Check info entered]
*Now you want to check whether you entered your location correctly. How could you do that?* I would scroll up and click on review information that you have entered, and it takes me back to review my information and then I would click edit. I would go to zip code and hit edit. I would reenter my zip code and continue. It takes me back to the dependents and hit continue where it would take me back to review my information. 

### Task 8: [Change year]
*Suppose that you’re in the process of appealing a health care claim from 2021, and you want to see the income limits from that year. What could you do?*  I think what I could do is expand my estimate tool. That is not what I was looking for so I would maybe go back to, I don’t think that was in the review the information you entered. Maybe expand all to see if there is another area. Get past income link at the bottom. It shows I can go back to 2015, so I would scroll down to 2021, and hit continue. It takes me through the same questions as before. I would select the income bracket I fall in and expand it.

- *(RECORD all comments and anything confusing re the interactions on each screen of the prototype:)*

## Post-Task Interview - 10 minutes
1. *How or where would you expect to find this app that you just used?* This tool I just used I would expect to find it on VA.gov that is where I go to find any VA information.  It would be great if you clicked on the healthcare would have a drop down with an income calculator. 

1. *What worked well for you?* The questions for the eligible were simple and it took you through one at a time. 

1. *What was unclear or didn't work well for you?* The only thing was the description of normal healthcare.

1.	*What would you like to change or add?* From what you said it would have information you have already entered for other years. If there was a lot of information to enter if you could have that populate, but with what is asked I don’t see that as an issue. 
2.	Is the font different than you normally see on your phone? Yes. 3
3.	Do you normally navigate webpages on your phone? Yes, sometimes. More browsing happens on a computer. 
4.	Can you go back to the original page before the past limits part? The final page for the current year. Did you read anything or know of anything from here if deductions would count towards your eligibility? No, I was thinking it was talking about my annual income. That tells me that it is not your annual income that counts deductions as well. I think it would be better if you added that information into the introduction instead of putting it into an expansion area.
5.	What do you think would be helpful to  help tell you that deductions would be counted? I would think for this one I think when you go to select your income range I would just go to the numbers. That is how I would click. Just have a brief introduction stating it is a total income for me and my spouse which is important to know.

1. *Is there anything else that we haven't talked about that you think I should know?* I could open another tab and show you have the normal VA websites typically shows up. It is more of a formatting for a cellphone over a desktop.

---
## [Aurorastation/Aurora.3](https://github.com/Aurorastation/Aurora.3)@[837b05261c...](https://github.com/Aurorastation/Aurora.3/commit/837b05261cab8e494fb8cd53249888399afb9431)
#### Monday 2023-04-10 17:54:26 by kyres1

Massive rec area remap into double holodecks (#16103)

* part 1 abloobloobloo

* BY GOD IT WORKS

* Moghes and konyang plus fucking everything else

* jupiter and biesel woohoo

* tweaks and feedback. places CIC and scuttler

* changelog and fixes

* life is agony

* about done

* arrow's changes

* fixes some shit

---
## [Vidhi-1997/Classification](https://github.com/Vidhi-1997/Classification)@[ee99be399e...](https://github.com/Vidhi-1997/Classification/commit/ee99be399ed021580bfc7211bfb4e7d74296c6d2)
#### Monday 2023-04-10 19:49:47 by Vidhi Tripathi

Add files via upload

Problem Statement:
Diabetes is one of the most frequent diseases worldwide and the number of diabetic patients are growing over the years. The main cause of diabetes remains unknown, yet scientists believe that both genetic factors and environmental lifestyle play a major role in diabetes.

A few years ago research was done on a tribe in America which is called the Pima tribe (also known as the Pima Indians). In this tribe, it was found that the ladies are prone to diabetes very early. Several constraints were placed on selecting these instances from a larger database. In particular, all patients were females at least 21 years old of Pima Indian heritage. Here, we are analyzing different aspects of Diabetes in the Pima Indians tribe by doing Exploratory Data Analysis and building a classification Model.

Dataset Information:

Below is the attribute information:

Pregnancies: Number of times pregnant
Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
Blood pressure: Diastolic blood pressure (mm Hg)
SkinThickness: Triceps skinfold thickness (mm)
Insulin: 2-Hour serum insulin (mu U/ml) test
BMI: Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction: A function that scores the likelihood of diabetes based on family history
Age: Age in years
Outcome: Class variable (0: the person is not diabetic or 1: the person is diabetic)

Output: 
The given dataset is 2-dimensional data having 1000 rows and 9 attributes where there are no missing values in the data. The notebook contains EDA and data representation with some graphs and predictions with Logistic regression and Random forest classifier.

---
## [zeeb92/tgstation](https://github.com/zeeb92/tgstation)@[1cdc327a8f...](https://github.com/zeeb92/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Monday 2023-04-10 20:24:59 by Jacquerel

Station Trait: Spider Infestation (#73893)

## About The Pull Request

Hate having your cables eaten by mice? Nanotrasen have heard your
complaints and settled on a natural, _organic_, and eco-friendly
solution.

When this station trait is active, roundstart and event mouse spawns
have a chance to instead be replaced with duct spiders (both will exist,
it doesn't remove mice).
Duct spiders are largely harmless to humans, actively hunt other
maintenance creatures (such as mice), and have only one _tiny_ downside.

![image](https://user-images.githubusercontent.com/7483112/224345781-2627be98-67f2-4cab-ac40-c6c9b35ea909.png)

These mobs can also sometimes be spawned by a minor scrubber clog event.

As a side note, all spider basic mobs with AI (except Araneus) will now
try to automatically fill a small area around them with webs.

Also I made it so that mobs will ignore their random_walking behaviour
if they're engaged in a `do_after`, just in case.

## Why It's Good For The Game

Adds a little bit of variety to things which can slightly annoy you in
maintenance.
Spiders will automatically make places they live in look like spiders
live there.

## Changelog

:cl:
add: A station trait which sometimes populates maintenance with small
spiders. You can wear them as a hat if you wanted to have a spider on
your head for some reason.
add: Spider mobs will automatically start webbing up their environment.
/:cl:

---
## [Mey-Ha-Zah/tgstation](https://github.com/Mey-Ha-Zah/tgstation)@[dc2f52e386...](https://github.com/Mey-Ha-Zah/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Monday 2023-04-10 20:33:10 by tralezab

Blink is no longer a forbidden school spell?? (#74487)

## About The Pull Request

Turns blink's school from forbidden to translocation. This has some
incredibly minor changes nobody is going to notice:
- Changes the blink's invocations when mixed with a CERTAIN spell
- If you were very specifically a chaplain with the holy crusade sect
and you casted blink, before it would excommunicate you, now it will
just smite you, as translocation spells are seen as less bad than
forbidden magic
- probably some more niche interactions but that's all I can remember

## Why It's Good For The Game

Guys, I know blink is a very annoying spell but come on now it's not
forbidden magic, that's for heretics and super duper evil stuffs

## Changelog
:cl:
fix: blink is now a translocation spell
/:cl:

---
## [4ohf/nvim](https://github.com/4ohf/nvim)@[58859de477...](https://github.com/4ohf/nvim/commit/58859de47798db3a7749cdf62d7d7a45c2238a7b)
#### Monday 2023-04-10 21:46:04 by 4ohf

added spell checker to git commit messages

so i went and read through some of my commit messages... oh boy was that
a mistake. Yeah I can't spell to save my life, so here we are lol

---
## [dagster-io/dagster](https://github.com/dagster-io/dagster)@[aba0a8090d...](https://github.com/dagster-io/dagster/commit/aba0a8090dff5651dbecf43752628e01c40e65c0)
#### Monday 2023-04-10 22:14:38 by OwenKephart

[asset-reconciliation] Use source asset observations to inform when to kick off eager reconciliation (#13304)

## Summary & Motivation

We did a similar sort of thing for data time calculations.

Note the TODO. The material impact is the following. Imagine you have an
asset graph `OS -> A -> B`, where OS is an observable source asset.

- Your asset_selection for your sensor is just `B`.
- `OS` is observed having version `1`, after which all downstreams are
materialized in order.
- `A` is manually materialized again (not pulling in any new data, as no
version was updated).
- `OS` is observed, still having version `1`.

The sensor will see that `A` has a new materialization, but will
erroneously treat it as "unreconciled", as a new observation record has
come in after the latest materialization of `A`. This means that a
materialization of `B` will not be kicked off.

In a fun twist of fate, this is actually arguably desirable behavior, as
there really isn't a reason for `B` to be kicked off in this scenario.
However, we're kinda getting the right answer for the wrong reason, if
that makes sense. We don't factor this sort of versioning information
into other parts of the reconciliation logic, and the following sequence
of events would give us an unambiguously incorrect behavior:

- `OS` is observed having version `1`, after which all downstreams are
materialized in order.
- `A` is manually materialized again (not pulling in any new data, as no
version was updated).
- `OS` is observed, now having version `2`.
- `A` is manually materialized again.
- `OS` is observed again, still having version `2`.

In this case, we get the same behavior (`B` not getting kicked off),
because there is an observation record after the most recent
materialization of `A` (this is the same reason as before).

In reality, we should search backwards for the FIRST occurrence of the
current version, this was just a minor pain to implement in the time I
have today.

## How I Tested These Changes

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[aec680f042...](https://github.com/git-for-windows/git/commit/aec680f0426390292e944c1c028a7fa8f9466cf5)
#### Monday 2023-04-10 22:18:56 by Johannes Schindelin

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
## [iwishforducks/tgstation](https://github.com/iwishforducks/tgstation)@[fe7ebd67cf...](https://github.com/iwishforducks/tgstation/commit/fe7ebd67cf74982038524ceb175377d7ff6c0486)
#### Monday 2023-04-10 23:23:20 by LemonInTheDark

Properly accounts for byond tick fuckery in runechat code (#74388)

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

---
## [iwishforducks/tgstation](https://github.com/iwishforducks/tgstation)@[c18b1ef442...](https://github.com/iwishforducks/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Monday 2023-04-10 23:23:20 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [crimssl/kernel_xiaomi_lavender](https://github.com/crimssl/kernel_xiaomi_lavender)@[a88108e90c...](https://github.com/crimssl/kernel_xiaomi_lavender/commit/a88108e90ca0c1d5f1631df4951459b6def12f75)
#### Monday 2023-04-10 23:26:47 by Douglas Anderson

serial: core: Allow processing sysrq at port unlock time

[ Upstream commit d6e1935819db0c91ce4a5af82466f3ab50d17346 ]

Right now serial drivers process sysrq keys deep in their character
receiving code.  This means that they've already grabbed their
port->lock spinlock.  This can end up getting in the way if we've go
to do serial stuff (especially kgdb) in response to the sysrq.

Serial drivers have various hacks in them to handle this.  Looking at
'8250_port.c' you can see that the console_write() skips locking if
we're in the sysrq handler.  Looking at 'msm_serial.c' you can see
that the port lock is dropped around uart_handle_sysrq_char().

It turns out that these hacks aren't exactly perfect.  If you have
lockdep turned on and use something like the 8250_port hack you'll get
a splat that looks like:

  WARNING: possible circular locking dependency detected
  [...] is trying to acquire lock:
  ... (console_owner){-.-.}, at: console_unlock+0x2e0/0x5e4

  but task is already holding lock:
  ... (&port_lock_key){-.-.}, at: serial8250_handle_irq+0x30/0xe4

  which lock already depends on the new lock.

  the existing dependency chain (in reverse order) is:

  -> #1 (&port_lock_key){-.-.}:
         _raw_spin_lock_irqsave+0x58/0x70
         serial8250_console_write+0xa8/0x250
         univ8250_console_write+0x40/0x4c
         console_unlock+0x528/0x5e4
         register_console+0x2c4/0x3b0
         uart_add_one_port+0x350/0x478
         serial8250_register_8250_port+0x350/0x3a8
         dw8250_probe+0x67c/0x754
         platform_drv_probe+0x58/0xa4
         really_probe+0x150/0x294
         driver_probe_device+0xac/0xe8
         __driver_attach+0x98/0xd0
         bus_for_each_dev+0x84/0xc8
         driver_attach+0x2c/0x34
         bus_add_driver+0xf0/0x1ec
         driver_register+0xb4/0x100
         __platform_driver_register+0x60/0x6c
         dw8250_platform_driver_init+0x20/0x28
	 ...

  -> #0 (console_owner){-.-.}:
         lock_acquire+0x1e8/0x214
         console_unlock+0x35c/0x5e4
         vprintk_emit+0x230/0x274
         vprintk_default+0x7c/0x84
         vprintk_func+0x190/0x1bc
         printk+0x80/0xa0
         __handle_sysrq+0x104/0x21c
         handle_sysrq+0x30/0x3c
         serial8250_read_char+0x15c/0x18c
         serial8250_rx_chars+0x34/0x74
         serial8250_handle_irq+0x9c/0xe4
         dw8250_handle_irq+0x98/0xcc
         serial8250_interrupt+0x50/0xe8
         ...

  other info that might help us debug this:

   Possible unsafe locking scenario:

         CPU0                    CPU1
         ----                    ----
    lock(&port_lock_key);
                                 lock(console_owner);
                                 lock(&port_lock_key);
    lock(console_owner);

   *** DEADLOCK ***

The hack used in 'msm_serial.c' doesn't cause the above splats but it
seems a bit ugly to unlock / lock our spinlock deep in our irq
handler.

It seems like we could defer processing the sysrq until the end of the
interrupt handler right after we've unlocked the port.  With this
scheme if a whole batch of sysrq characters comes in one irq then we
won't handle them all, but that seems like it should be a fine
compromise.

Signed-off-by: Douglas Anderson <dianders@chromium.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [openai/evals](https://github.com/openai/evals)@[fe8e3b03e3...](https://github.com/openai/evals/commit/fe8e3b03e34f666774d63e6ae33d3f14d047d973)
#### Monday 2023-04-10 23:30:21 by Josh Tanner

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
## [TurtleShroom/TSP_STORYTIME_RIDES_AGAIN](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN)@[3022ea194c...](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN/commit/3022ea194c33b3ade2655a9665ac71743988b616)
#### Monday 2023-04-10 23:42:59 by TURTLESHROOM

Major

1. Fixed Natural Meditation support for Bean Man Backstories.

2. If you have the Maormer Mod ( https://www.steamcommunity.com/sharedfiles/filedetails/?id=2725894363 ), Goblins are also into creepy snake totems.

3. Certain Wood Beet Backstories allow for special meditation rights.

4. If you have the Galactic Trade Group Mod ( https://www.steamcommunity.com/sharedfiles/filedetails/?id=2956274766 ), the Gnomes will now trade every Food in the game if you visit their Base.

5. Shortened the Kung Flu description to avoid its tooltip clipping off of the screen.

6. Induced Froganthropy, which causes Werefrog Parts to grow, now always grows Werefrog Parts.

7. If you have the "Biotech" Expansion Pack, it is now possible to encounter Mechanitor Goblins, although this is extremely rare.

8. Denoted the Mod's metallic floors as floors.

9. Removed duplicate Rune Essence entries.

10. Fixed mistake in description: to make Mordorite, JADE is needed, not silver.

11. Fixed issue where the Mod's "Green Blood" (actually slime) overwrote the names of several other Mods that add colored Blood.

12. Denoted Blue Heelers, Dachsunds, and Rat Dogs as dogs, in order to mirror Ludeon's placement on the Vanilla rendition's dogs.

13.  Reduced the mass of all Jeubs.

14. Infant High Jeubs can now control animals as soon as they are able to walk, which matches their ability to control non-sapient Jeubs in this Mod's lore.

15. Fixed issue where Skeleton Pirates, which were men, could arrive with Scaria as if they were mindless animals.

16. If you have the Mod ( https://steamcommunity.com/sharedfiles/filedetails/?id=2955419294 ), the Mod's Jewelry is now integrated into this Mod.

17. Reduced the chance of the Banana Scythe spawning in Ancient Danger Ruins.

18. My changes to the Snake Oil Drug in the Tumbleweed Mod ( https://www.steamcommunity.com/sharedfiles/filedetails/?id=2942794579 )

19. Added more Wood Beet Names.

20. Added support for the Treasure Hunter Mod ( https://www.steamcommunity.com/sharedfiles/filedetails/?id=2653963772 ).

21. Preserved a Hair Def from a person who was banned by Valve for uploading links to fraudulent websites. All viruses and scam links have been removed. The original Mod seems to have been allowed back onto the Workshop, so if it's approved again, I will remove the files.

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[928b2420d9...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/928b2420d906fbdef89ce27d75db5afe713b147d)
#### Monday 2023-04-10 23:59:37 by Lance

Servant of Wrath

Records and Instability

Dash speed up

Fuck you I'll space indent all I like

There was some fuckin lint in this PR

God damned there's a lot of lint in here

Faction Check

Sprite update, minor bug fixes

Floating and Gun and Acid

Minor Records

Small update

Unnerfs resists

AoE hit fix

Gun update real

more res should mean less talk

Pixel Fix

Sound... Fix?

Broke the staff's legs, fuck those guys.

lmfao audio pains

Gun Rename, Spawn nerf

NO MORE FRIENDS FROM GUN

Faction change

acid tweak

LINT!

SW Code and Balance

SoW Temp commit

Scuff-Fix

SoW bonk update

Hermit range increase and ranged damage decrease

visual fix

Ending adjustments

I forgot to carry the 4

Visual indicator

minor fixes

Instability Tweaks

Paperwork Update

Anti-Self-Burn

Ending Update

Right view

A check that should be a non-issue but i'm making sure!

Breach Update and EGO update

More goo and FEMALE

Improvement and new Icons

---

