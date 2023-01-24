## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-23](docs/good-messages/2023/2023-01-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,248,025 were push events containing 3,309,264 commit messages that amount to 245,400,287 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[de0a48b02e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/de0a48b02e65875833c6416fda28729677bc6245)
#### Monday 2023-01-23 00:03:28 by SkyratBot

[MIRROR] Unironically removes the atmos and black beret [MDB IGNORE] (#18747)

* Unironically removes the atmos and black beret (#72722)

## About The Pull Request

Removes atmos berets

## Why It's Good For The Game
Berets shouldn't be thrown into every job, it's milsim circlejerking
dressup shit that creeps out of our milsim containment jobs (security)
and into other innocent jobs. There is absolutely no reason for this job
to have a beret just straight up. Can we add unique hats to the game,
not the same one recolored every way to Sunday? That's my problem. We
don't have unique clothes, we have a billion types of beret when the
BASE BERET TYPE has `IS_PLAYER_COLORABLE_1` so ANYONE can color it. So
again, why do we have the atmos beret? To clog the wardrobe, a vending
machine added specifically because we couldn't stop clogging the
original locker atmos techs spawned in?

The black beret has the same problem: recolored item when you can get
the item of any color

## Changelog
:cl:
del: Atmospherics beret and black beret
/:cl:

* Unironically removes the atmos and black beret

* update modular

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [Mirino97/space-station-14](https://github.com/Mirino97/space-station-14)@[4492f8c50b...](https://github.com/Mirino97/space-station-14/commit/4492f8c50b64c9a5dcca76e4955e235d5d6bd61c)
#### Monday 2023-01-23 00:07:04 by Mirino97

Holy shit I got it working I'm so fucking close (to having the basic system implemented)

---
## [PrettyPsychoForAWolf/coyote-bayou](https://github.com/PrettyPsychoForAWolf/coyote-bayou)@[70042337db...](https://github.com/PrettyPsychoForAWolf/coyote-bayou/commit/70042337dbefb532ee9e1eb640edb00e9280c932)
#### Monday 2023-01-23 00:36:12 by A Psycho

Merge pull request #1483 from ARF-SS13/Fuck-you-github

Small mapfixes

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[25f4961156...](https://github.com/Paxilmaniac/Skyrat-tg/commit/25f4961156121121aa9b545cfc9f6014b89c2362)
#### Monday 2023-01-23 01:45:47 by SkyratBot

[MIRROR] Refactors memories to be less painful to add and apply, moves memory detail / text to memory subtypes. Adds some new memories to demonstrate.  [MDB IGNORE] (#18487)

* Refactors memories to be less painful to add and apply, moves memory detail / text to memory subtypes. Adds some new memories to demonstrate.  (#72110)

So, a huge issue with memories and - what I personally believe is the
reason why not many have been added since their inception is - they're
very annoying to add!

Normally, adding subtypes of stuff like traumas or hallucinations are as
easy as doing just that, adding a subtype.

But memories used this factory argument passing method combined with
holding all their strings in a JSON file which made it just frustrating
to add, debug, or just mess with.

It also made it much harder to organize new memories keep it clean for
stuff like downstreams.

So I refactored it. Memories are now handled on a subtype by subtype
basis, instead of all memories being a `/datum/memory`.

Any variety of arguments can be passed into memories like addcomponent
(KWARGS) so each subtype can have their own `new` parameters.

This makes it much much easier to add a new memory. All you need to do
is make your subtype and add it somewhere. Don't need to mess with jsons
or defines or anything.

To demonstrate this, I added a few memories. Some existing memories had
their story values tweak to compensate.

Makes it way simpler to add new memories. Maybe we'll get some more fun
ones now?

:cl: Melbert
add: Roundstart captains will now memorize the code to the spare ID
safe.
add: Traitors will now memorize the location and code to their uplink.
add: Heads of staff winning a revolution will now get a memory of their
success.
add: Heads of staff and head revolutionaries who lose their respective
sides of the revolution also get a memory of their failure.
add: Completing a ritual of knowledge as a heretic grants you a quality
memory.
add: Successfully defusing a bomb now grants you a cool memory. Failing
it will also grant you a memory, though you will likely not be alive to
see it.
add: Planting bombs now increase their memory quality depending on how
cool the bomb is.
refactor: Memories have been refactored to be much easier to add.
/:cl:

* Modular!

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [asmodium/wc3translations](https://github.com/asmodium/wc3translations)@[ab5813ca2b...](https://github.com/asmodium/wc3translations/commit/ab5813ca2beec88bd07598cd2d200a6bd58d24cc)
#### Monday 2023-01-23 01:47:08 by asmodium

Add files via upload

[Basics]
power/strength > STR
agility/dexterity > AGI
intelligence > INT
anything related to max hp > Max HP
anything related to max mp > Max MP
attack power/damage > Damage
attribute damage > affinity
cooldown reduction > CDR
critical/lifesteal for both at once > Omnicritical/Omnivampirism

[System]
Lucky draw [10 consecutive] > '|cffffff00Lucky Draw [10 Times]|r'

[Ilya]
Fast Heal > Full Heal
Wave Acceleration > Skip Wave
Buy Gold/Wood (large) > Exchange Gold/Wood (large)

[Monsters]
【Elite】Desert Scorpion Leader > 【Elite】Desert Arachnatid Leader
【Elite】Panda Jiuxian > 【Elite】Taoist Panda
【Elite】Holy Light Knight bright brador > 【Elite】God's Champion Righteous Brador
【Lord】Grand Magister Mysterious Force Nilas > 【Lord】Great Magister Nilas of the Force
【Lord】Shadow Assassin Cordana - Fallen Song > 【Lord】Phantom Assassin Cordana of Fallen Songs

[Items]
All basic shop items renamed and corrected, recipes to be fixed yet.
uplifiting gem > Hyperstone
Guardian of Shiva > Shiva's Guard
Satan's Evil Power > Satan's Crown
Demon Blade > Demonic Edge
iron tree branch > Ironwood Branch
Speed Gloves > Gloves of Haste
Amulet of Dodge > Amulet of Evasion
ball of energy > Energy Booster
Almighty Sphere > Sphere of Gods
vitality ball > Vitality Booster
essence ball > Spirit Booster
Spirit Stone > Soul Booster
Silver Scale Breastplate > Silver Breastplate
Fantasy magic sword "Flower of Fantasy" > Fantasy Magic Sword☆Flower of Fantasy
Nightmare materialized > True Nightmare
Silver Ice Snow > Freezing Silver Snow
Shard of a Star > Star Shard
Scythe of Death [Judgment] > 【Judgment】Death Scythe
Sword of the Night Sky > Night Sky Sword
Meteorite "Primary Flame" > 【Embryonic Flame】 Aestus Estus 
The Spear of Shining Last End > Armageddon Shining Spear
Magic Sword·Levatin > Magic Sword·Laevatein
Secret Stone > Arcane Stone
Desperate power > Power of Despair
Power of Nightmare > Nightmare Power
Power of Death > The Power of Death
Destruction Power > Power of Destruction
One of the Original > Original One
Doomsday power > The Power of Doom
Cattelan > Cattleya
Silver Leaf Chrysanthemum > Silverleaf Chrysanthemum
Evening Primrose
Evening Primrose 【Blooming】> 【Blooming】 Evening Primrose
Silverleaf【Blooming】 > 【Blooming】 Silverleaf Chrysanthemum
Cattelan【Blooming】 > 【Blooming】 Cattleya
Nine-character Kanesada > Nine-Faces Kanesada
Fantasy Magic Sword【Fantasy】>【Fantasy】Fantasy Magic Sword
Absolute Zero·Feilin > Absolute Zero·Feris
Cong Yuan/Cong Yuwan > Magic Sword·Cong Yuan
Acacia [Dream Language る Flower の Saint] > Acacia【Dream Language る Flower の Saint】
Inherit Armament—Falut [True Dragon Emperor] > Inheritance Armament - Falut【True Dragon Emperor】
Reaper of Souls > Soul Reaper
Space-Time Kunai > Flying Thunder God Kunai
Witch Soul > Soul of the Witch
Bougainvilea > Silverleaf Chrysantheum
Gemstone Holy Sword Shining > Shining Gem·Holy Sword
Meteor Gun Gungnir > Meteor Gungnir
Momentary Galaxy Crown > Momentary Galaxy River Crown
Dream Blade > Blade of Dreams
The overlord of the sky, Falut > Overlord of the Sky, Falut
Blessed Item > Proof of the Promise
Shard of Destiny > Destiny Shard
Fate Fragment > Destiny Shard
Poisonous Blade > Venomous Blade
God of Destruction > Destruction''s God Power
Radiance Rod > Bright Rod
Doomsday Awakening Vizia > Awakening of Doomsday·Vizia
Doomsday Awakening - Geotide > Awakening of Doomsday·Geotide
Mechanical God > Mechanicus
Silver Ice Dragonman Feilin > Ice Silver Dragonkin·Feris
Demon Blade Heart Crossing > Heartseeking Demonic Blade
World Tree > World Tree Branch
Black Dragon Power > Power of Black Dragon
Scythe of Death > Death Scythe
The Principle of the Ring 【Hope】 > 【Hope】The Law of Cycles
End Gatekeeper Sibine > Gatekeeper of End·Sibine
Tianyao Shield > Sky Shield
Queen of Manaria, Ann > Queen of Manaria·Ann
Sky Shield Recipe fixed
God''s Pronucleus > God''s Pro-Nucleus
The Domineering King, Falut > Overlord King of the Sky·Falut
Dimensional Witch Dorothy > Dimensional Witch·Dorothy
Exorcism Knife "Seven Nights" > Seven Nights·Exorcism Knife
Wings of Mediation Zoe > Wings of Mediation·Zoe

[Enchantment]

Fate Enchanting [Time and Space (Change)] > Fate Enchanting [Law of Time and Space]
Special enchantment【Noneness】> Special Enchantment【Void】
Inherit Armament——Dark Falut > Inheritance Armament - Dark Falut [True Dragon]
Special Enchantment [Dragon]

---
## [crcrpar/pytorch](https://github.com/crcrpar/pytorch)@[5c6f5439b7...](https://github.com/crcrpar/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Monday 2023-01-23 02:13:55 by Edward Z. Yang

Implement SymBool (#92149)

We have known for a while that we should in principle support SymBool as a separate concept from SymInt and SymFloat ( in particular, every distinct numeric type should get its own API). However, recent work with unbacked SymInts in, e.g., https://github.com/pytorch/pytorch/pull/90985 have made this a priority to implement. The essential problem is that our logic for computing the contiguity of tensors performs branches on the passed in input sizes, and this causes us to require guards when constructing tensors from unbacked SymInts. Morally, this should not be a big deal because, we only really care about the regular (non-channels-last) contiguity of the tensor, which should be guaranteed since most people aren't calling `empty_strided` on the tensor, however, because we store a bool (not a SymBool, prior to this PR it doesn't exist) on TensorImpl, we are forced to *immediately* compute these values, even if the value ends up not being used at all. In particular, even when a user allocates a contiguous tensor, we still must compute channels-last contiguity (as some contiguous tensors are also channels-last contiguous, but others are not.)

This PR implements SymBool, and makes TensorImpl use SymBool to store the contiguity information in ExtraMeta. There are a number of knock on effects, which I now discuss below.

* I introduce a new C++ type SymBool, analogous to SymInt and SymFloat. This type supports logical and, logical or and logical negation. I support the bitwise operations on this class (but not the conventional logic operators) to make it clear that logical operations on SymBool are NOT short-circuiting. I also, for now, do NOT support implicit conversion of SymBool to bool (creating a guard in this case). This does matter too much in practice, as in this PR I did not modify the equality operations (e.g., `==` on SymInt) to return SymBool, so all preexisting implicit guards did not need to be changed. I also introduced symbolic comparison functions `sym_eq`, etc. on SymInt to make it possible to create SymBool. The current implementation of comparison functions makes it unfortunately easy to accidentally introduce guards when you do not mean to (as both `s0 == s1` and `s0.sym_eq(s1)` are valid spellings of equality operation); in the short term, I intend to prevent excess guarding in this situation by unit testing; in the long term making the equality operators return SymBool is probably the correct fix.
* ~~I modify TensorImpl to store SymBool for the `is_contiguous` fields and friends on `ExtraMeta`. In practice, this essentially meant reverting most of the changes from https://github.com/pytorch/pytorch/pull/85936 . In particular, the fields on ExtraMeta are no longer strongly typed; at the time I was particularly concerned about the giant lambda I was using as the setter getting a desynchronized argument order, but now that I have individual setters for each field the only "big list" of boolean arguments is in the constructor of ExtraMeta, which seems like an acceptable risk. The semantics of TensorImpl are now that we guard only when you actually attempt to access the contiguity of the tensor via, e.g., `is_contiguous`. By in large, the contiguity calculation in the implementations now needs to be duplicated (as the boolean version can short circuit, but the SymBool version cannot); you should carefully review the duplicate new implementations. I typically use the `identity` template to disambiguate which version of the function I need, and rely on overloading to allow for implementation sharing. The changes to the `compute_` functions are particularly interesting; for most of the functions, I preserved their original non-symbolic implementation, and then introduce a new symbolic implementation that is branch-less (making use of our new SymBool operations). However, `compute_non_overlapping_and_dense` is special, see next bullet.~~ This appears to cause performance problems, so I am leaving this to an update PR.
* (Update: the Python side pieces for this are still in this PR, but they are not wired up until later PRs.) While the contiguity calculations are relatively easy to write in a branch-free way, `compute_non_overlapping_and_dense` is not: it involves a sort on the strides. While in principle we can still make it go through by using a data oblivious sorting network, this seems like too much complication for a field that is likely never used (because typically, it will be obvious that a tensor is non overlapping and dense, because the tensor is contiguous.) So we take a different approach: instead of trying to trace through the logic computation of non-overlapping and dense, we instead introduce a new opaque operator IsNonOverlappingAndDenseIndicator which represents all of the compute that would have been done here. This function returns an integer 0 if `is_non_overlapping_and_dense` would have returned `False`, and an integer 1 otherwise, for technical reasons (Sympy does not easily allow defining custom functions that return booleans). The function itself only knows how to evaluate itself if all of its arguments are integers; otherwise it is left unevaluated. This means we can always guard on it (as `size_hint` will always be able to evaluate through it), but otherwise its insides are left a black box. We typically do NOT expect this custom function to show up in actual boolean expressions, because we will typically shortcut it due to the tensor being contiguous. It's possible we should apply this treatment to all of the other `compute_` operations, more investigation necessary. As a technical note, because this operator takes a pair of a list of SymInts, we need to support converting `ArrayRef<SymNode>` to Python, and I also unpack the pair of lists into a single list because I don't know if Sympy operations can actually validly take lists of Sympy expressions as inputs. See for example `_make_node_sizes_strides`
* On the Python side, we also introduce a SymBool class, and update SymNode to track bool as a valid pytype. There is some subtlety here: bool is a subclass of int, so one has to be careful about `isinstance` checks (in fact, in most cases I replaced `isinstance(x, int)` with `type(x) is int` for expressly this reason.) Additionally, unlike, C++, I do NOT define bitwise inverse on SymBool, because it does not do the correct thing when run on booleans, e.g., `~True` is `-2`. (For that matter, they don't do the right thing in C++ either, but at least in principle the compiler can warn you about it with `-Wbool-operation`, and so the rule is simple in C++; only use logical operations if the types are statically known to be SymBool). Alas, logical negation is not overrideable, so we have to introduce `sym_not` which must be used in place of `not` whenever a SymBool can turn up. To avoid confusion with `__not__` which may imply that `operators.__not__` might be acceptable to use (it isn't), our magic method is called `__sym_not__`. The other bitwise operators `&` and `|` do the right thing with booleans and are acceptable to use.
* There is some annoyance working with booleans in Sympy. Unlike int and float, booleans live in their own algebra and they support less operations than regular numbers. In particular, `sympy.expand` does not work on them. To get around this, I introduce `safe_expand` which only calls expand on operations which are known to be expandable.

TODO: this PR appears to greatly regress performance of symbolic reasoning. In particular, `python test/functorch/test_aotdispatch.py -k max_pool2d` performs really poorly with these changes. Need to investigate.

Signed-off-by: Edward Z. Yang <ezyang@meta.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/92149
Approved by: https://github.com/albanD, https://github.com/Skylion007

---
## [DESUP2/Game-2d-Projects-source](https://github.com/DESUP2/Game-2d-Projects-source)@[037e0e984c...](https://github.com/DESUP2/Game-2d-Projects-source/commit/037e0e984c4d6c32e9ce7310d254b2871e873135)
#### Monday 2023-01-23 02:42:10 by SUPRADIP DEY

Add files via upload

Create your Character Animation Masterpiece
Creature is the Cutting-edge 2D Animation Software designed to add stunningly fluid animation to your digital content. Take advantage of Creature's Directable Automated Animation Engine and powerful workflow to produce amazingly complex animation in an incredibly easy and time-efficient manner. Creature is the ideal animation Tool for game developers, digital artists and web designers wanting to add that special animated magic to make your content come alive.

Creature is currently used in both Indie and Large-scale Animation/GameDev Production worldwide, including major studios like Ubisoft, NCSoft, Bianfeng and Playstudios.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[30147af9f8...](https://github.com/ARF-SS13/coyote-bayou/commit/30147af9f8b8147f3a3ee36c7b71a50e370b6b25)
#### Monday 2023-01-23 03:47:45 by Superlagg

Merge pull request #1485 from ARF-SS13/Fuck-you-github

Suckumb Fixes

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[e5d01832df...](https://github.com/ARF-SS13/coyote-bayou/commit/e5d01832dff42df21a0e5fbc57ae8e5810f15486)
#### Monday 2023-01-23 04:00:31 by Tk420634

Merge pull request #1488 from ARF-SS13/revert-1485-Fuck-you-github

Revert "Suckumb Fixes"

---
## [MostlyOperational18119/Mostly-Operational-Power-Play](https://github.com/MostlyOperational18119/Mostly-Operational-Power-Play)@[49625a3579...](https://github.com/MostlyOperational18119/Mostly-Operational-Power-Play/commit/49625a3579e11de0ef6bbd54ad44c6bb79a7c104)
#### Monday 2023-01-23 04:00:32 by TedArmenston

HOLY SHIT IT STACKED CONES. IT ACTUALLY DID IT (needs some fine tuning on the approach, and some obvious speed improvements, but god DAMN she's a beauty

---
## [Dantesousa/Nebula13-Reborn](https://github.com/Dantesousa/Nebula13-Reborn)@[a57b142c1a...](https://github.com/Dantesousa/Nebula13-Reborn/commit/a57b142c1a4949ded1dcde1157ccf789fb21aabd)
#### Monday 2023-01-23 04:02:00 by SkyratBot

[MIRROR] Basic mobs don't become dense upon death [MDB IGNORE] (#18679)

* Basic mobs don't become dense upon death (#72554)

## About The Pull Request

In #72260 what was previously a var became a flag, which was a sensible
change, however this inverted the default behaviour.
In virtually all cases we want dead mobs to _stop_ being dense, this
added a requirement for the flag to be present for that to happen and
then didn't add the flag to any mobs.

Rather than add this to every mob I inverted the function of the flag.
My reasoning here is that _simple_ mobs seemingly never required this
behaviour, basic mobs are probably going to need it rarely if ever, and
including it in `basic_mob_flags` by default seems messy and easy to
leave off when setting other flags (plus #72524 implies to me we want to
avoid adding more default values).

Setting this manually on each mob seems kind of silly as a requirement
going forward and I can't think of a way we'd unit test for people
forgetting.

For the same reason I did the same thing with the
`STOP_ACTING_WHILE_DEAD` flag I added to the AI controller in a recent
PR, the flag should denote unusual behaviour not the default.

## Why It's Good For The Game

It looks really odd when you're constantly shuffling places with dead
mobs, they're not supposed to do that.
It's tedious to add `STOP_ACTING_WHILE_DEAD` to every AI controller when
that should be an obvious default assumption.

## Changelog

:cl:
fix: Dead basic mobs are no longer "dense" objects and can be stepped
on.
/:cl:

* Basic mobs don't become dense upon death

* Removes a flag we didn't need anymore.

* Forgot to remove this one

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[674870ea46...](https://github.com/treckstar/yolo-octo-hipster/commit/674870ea464fd2c81395c7c03e092f5d258b5349)
#### Monday 2023-01-23 04:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Vancouver-KDD/ux-study](https://github.com/Vancouver-KDD/ux-study)@[00eea3ca73...](https://github.com/Vancouver-KDD/ux-study/commit/00eea3ca73bf48b06eefc60c060a5a6ffc15e556)
#### Monday 2023-01-23 08:20:53 by minj2

Update Defining-user-problems-MJLee.md

Have you ever considered how psychology influences your behavior and engagement with products in everyday life? 
I use hick's row day by day when I ask for the next day's lunch for my kid. I picked 2-3 choices and let her decide. When before, I asked all the options for the lunches that can be prepared, it took so long to decide and sometimes asked me what were the rest. I think the many options not only overwhelmed her but also harder to decide. After several try-outs, I picked 2-3 and she select 1 so quickly. We both happy with it.

---
## [galaxyholly/meteor_lite](https://github.com/galaxyholly/meteor_lite)@[d5dc346fd9...](https://github.com/galaxyholly/meteor_lite/commit/d5dc346fd902f70f177c26d5f6b80b86243300b5)
#### Monday 2023-01-23 08:56:41 by galaxyholly

Not sure if I changed much. I spent most of tonight's sessions reading up about pyside. I will say, the back end for weather data retrieval and display is working. It still needs error handling and cleanup, but it works! Now it's down to making the gui. I still have to plan out exactly how I want to design this app, what it's going to do, all its functions, etc... That's likely for tomorrow. I'm fairly excited though. I plan to make this a fully functional weather app and add support for an arduino weather station. Essentially, users can install a package on their arduino nano sense that collects weather data and stores it in the apps db. Then, once some data is collected the user will be able to see their data compared graphically to the NOAA data. If this project runs long enough they may be able to upload that data to a website and compare with a network of other weatherstations. Wild stuff. At this point I've got a strong base of knowledge for making all this work. I started with web development so I'm already ahead for making a django website. Anyway, lost in the clouds. Tomorrow I want to decide this apps style. I've been leaning towards an app that can start on PC startup and position itself as a toolbar. I'd like it to have a small loading screen to start with a cool graphic involving meteors. Then it shows highs and lows for each day of the week. It can also show the temps for the day. I'd like it to have optional alerts that pop up for certain conditions. I think including a color based system for highlighting certain temp ranges would be great. The idea is this is as lightweight or as involved as the user needs. (optionally, I could include more tools of sorts, but that's really just if I find this fun enough). Perhaps also animations on the weatherbar like a raining background for current temps and such. That would be sweet. Anyways, goodnight.

---
## [snipeTR/HIP](https://github.com/snipeTR/HIP)@[30350b936b...](https://github.com/snipeTR/HIP/commit/30350b936bff5c635c85d54edce19f429df103b7)
#### Monday 2023-01-23 09:02:37 by snipeTR

Create HIP_scientific_research.md

# HIP allocating unused processing power for scientific research.

- Author(s): snipeTR
- Start Date: 23.01.2023
- Category: technical
- Original HIP PR: <!-- leave this empty; maintainer will fill in ID of this pull request -->
- Tracking Issue: <!-- leave this empty; maintainer will create a discussion issue -->

# Summary

The incredible amount of total processing power created by changing hotspot tasks with HIP 55 will enable changes to be used for one/multiple projects that will benefit the world.
<!-- Read the content requests in all sections before starting to write any section. -->

# Motivation

With HIP 55, many HOTSPOT devices have turned into a type of hotspot called "light" hotspot, and the processing power used for block processing has become almost completely useless.

 Currently, thousands of devices with extremely powerful processors and Terabytes of memory are sitting idle on roofs and in houses. These devices are always open to electricity and internet access, and many have advanced cooling systems. Because they are not performing any block processing, they are wasting energy and running idle until the next ping. 

On average, each hotspot has the potential of 1Ghz single-core processing power, with the best case scenario being 1.4 ghz dual-core processing power and 1Gb - 8Gb of memory, all sitting idle in dusty plastic/metal boxes on rooftops and in corners of rooms. If you multiply these numbers by an average of 500,000 hotspots, it's not hard to see the incredible processing and memory power that is going to waste. 

To put this idle power to good use for the benefit of humanity, by using a completely scientific and civilian distributed system for computing mechanism for climate and nuclear research in the future, which could help humanity escape from the climate crisis and infectious diseases more quickly, is in my opinion, quite possible. This way, people living on this world could benefit from it and thank the helium community every day. 

If we think deeper, we can leave the choice of participating to personal selection and encourage the participation by rewarding them with helium award. But I think this is a different HIP topic.

# Stakeholders

- As a result of this HIP, I believe that all of humanity and all civilizations, including future generations, will be affected positively. I wanted to give an example of a "distributed system computing mechanism" that I mentioned above. There is an organization like this at https://boinc.berkeley.edu/ but a better computing organization may be found as a community. It would be good to make this decision together with the helium community. For example, after the necessary HIP for the limitations and operation of the mechanism is approved, a different HIP can be used to decide which distributed system computing organization/coordinator to work with.

- If as a result of this scientific computation, even at a very low level, electricity and bandwidth are consumed by the community, the following method can be used for the initial setup:
- - a Participation in the distributed computing system starts actively for everyone, and then a method is created for shutting it off.
     - a1- An award is given for the method and it is encouraged not to shut it off.
     - a2- No award is given for the method.
  - b- Participation in the distributed computing system starts inactively, and then a method is created for turning it on.
    - b1- An award is given for the method and it is encouraged to turn on the system.
    - b2- No award is given for the method.

# Detailed Explanation

**The scientific advancement that will result from this proposal is incredibly large compared to the individual cost of the energy spent. **

We can see how diseases like COVID have affected humanity. It is not incorrect to say that the way vaccines were developed so quickly for this disease was through distributed computing clusters, which we refer to as supercomputers. By repeating millions of simulations with thousands of possibilities in minutes, the ability to find optimal calculations and molecules has made it easier to find vaccines and prevent the pandemic from lasting for decades and saving millions of lives. This is just one example of a current and simple use case that I can give.

There can be various criteria for using this excess processing and memory power for scientific calculations and operations. For example, during transmission, these operations can be given a lower priority. This way, they do not affect the use of the helium network. And in this way, with the excess processing power, they can continue their calculations in a comfortable manner without affecting the necessary updates and system stability with a higher priority.

Another system control mechanism can be memory and processor/system temperature controls. For example, the amount of memory used can be the amount calculated as free by the system. And it can be changed dynamically. This way, the functionality of the helium network will not be affected. The situation where the operation is stopped based on the processor temperature can also be considered as a method that does not affect the functionality of helium and allows scientific calculations to continue and prevent possible hardware failures.

The algorithm is as follows:
- The helium hotspot software should be run at a lower CPU priority.
- If the amount of free memory is above a certain level, this amount of memory should be used.
- If the system temperature rises to 70 degrees or above, the scientific calculation should be stopped..

# Drawbacks

- There are two reasons not to do this requires inter-agency coordination (berkeley etc, vs helium)
- Difficulties in software development.

# Rationale and Alternatives

This is a unique proposal. 

There is no disadvantage to doing it, other than time and effort. 

However, if we don't do it, we will never know what contributions we can make to science. In the future, other than seeing news headlines like "the helium community found a definitive cure for cancer of xxxx", I can't see any disadvantage (:)).

# Unresolved Questions

For this hypothesis, a standard data set should be first requested from hardware manufacturers. 

##### The data should consist of:
1. Total units produced
2. Number online
3. Minimum RAM
4. Maximum RAM
5. Average free RAM
6. Minimum processor speed produced
7. Maximum processor speed produced
8. Number of processor cores
9. Disk size
10. Average free disk space
11. Average internet speed
12. Minimum processor temperature
13. Maximum processor temperature
14. Average ambient temperature

With these data, a security framework should be constructed. This security framework should be loaded onto systems with a separate update to obtain current data and calculate potential processing power. In other words, a kind of dummy calculation should be made and the effects of this calculation on the helium network should be monitored and adjustments made to optimize the security framework and not affect the helium network. After all, these devices perform operations that last only a tenth of a second every 10-15 times per hour. The rest of the time, they are idle.

Once this security framework system is successfully active, the necessary institutions will gladly develop and quickly write this software to make it applicable to systems. I am almost certain that they will provide the central servers themselves. No one will say no to such a scientific aid on this scale.

If this security layer test is successfully completed, it poses no security risk to helium because these hardware that uses linux embedded systems work in a separate user and permission, and even a software that runs under a container system like docker can never reach the software above and cannot steal information or stop their work. Special keys created specifically for helium, or similar things, must first be a major security vulnerability related to the institution in question, then take advantage of some vulnerabilities in the helium system, and then take advantage of the vulnerabilities of the devices. This possibility is reduced to zero.

The creation of the security framework is really important, but it is not a difficult task. It is a matter of collecting data and applying them to a simple algorithm. The algorithm that will be developed with the data obtained from the manufacturers will be able to analyze the data and report the results in a very short time.

# Deployment Impact

Describe how this design will be deployed and any potential impact it may have on
current users of this project.

- How will current users be impacted?
		Existing users will not be technically affected.

- How will existing documentation/knowlegebase need to be supported?
  Any content to change at <http://docs.helium.com> ?
		just a little information and a short article.

- Is this backwards compatible?
		yes
- Can this HIP be undone?
		yes


# Success Metrics

What metrics can be used to measure the success of this design?

		Despite no changes appearing in activities on the helium network, there is an incredible increase in the average processing power of the following website over 24 hours: https://boinc.berkeley.edu/computing.php

Are any new ETL reports needed to measure the success?

		yes, hardware statistics and a report showing the change in helium network activities may be required.

---
## [reddysujith/linux](https://github.com/reddysujith/linux)@[6a518afcc2...](https://github.com/reddysujith/linux/commit/6a518afcc2066732e6c5c24281ce017bbbd85506)
#### Monday 2023-01-23 09:15:58 by Linus Torvalds

Merge tag 'fs.acl.rework.v6.2' of git://git.kernel.org/pub/scm/linux/kernel/git/vfs/idmapping

Pull VFS acl updates from Christian Brauner:
 "This contains the work that builds a dedicated vfs posix acl api.

  The origins of this work trace back to v5.19 but it took quite a while
  to understand the various filesystem specific implementations in
  sufficient detail and also come up with an acceptable solution.

  As we discussed and seen multiple times the current state of how posix
  acls are handled isn't nice and comes with a lot of problems: The
  current way of handling posix acls via the generic xattr api is error
  prone, hard to maintain, and type unsafe for the vfs until we call
  into the filesystem's dedicated get and set inode operations.

  It is already the case that posix acls are special-cased to death all
  the way through the vfs. There are an uncounted number of hacks that
  operate on the uapi posix acl struct instead of the dedicated vfs
  struct posix_acl. And the vfs must be involved in order to interpret
  and fixup posix acls before storing them to the backing store, caching
  them, reporting them to userspace, or for permission checking.

  Currently a range of hacks and duct tape exist to make this work. As
  with most things this is really no ones fault it's just something that
  happened over time. But the code is hard to understand and difficult
  to maintain and one is constantly at risk of introducing bugs and
  regressions when having to touch it.

  Instead of continuing to hack posix acls through the xattr handlers
  this series builds a dedicated posix acl api solely around the get and
  set inode operations.

  Going forward, the vfs_get_acl(), vfs_remove_acl(), and vfs_set_acl()
  helpers must be used in order to interact with posix acls. They
  operate directly on the vfs internal struct posix_acl instead of
  abusing the uapi posix acl struct as we currently do. In the end this
  removes all of the hackiness, makes the codepaths easier to maintain,
  and gets us type safety.

  This series passes the LTP and xfstests suites without any
  regressions. For xfstests the following combinations were tested:
   - xfs
   - ext4
   - btrfs
   - overlayfs
   - overlayfs on top of idmapped mounts
   - orangefs
   - (limited) cifs

  There's more simplifications for posix acls that we can make in the
  future if the basic api has made it.

  A few implementation details:

   - The series makes sure to retain exactly the same security and
     integrity module permission checks. Especially for the integrity
     modules this api is a win because right now they convert the uapi
     posix acl struct passed to them via a void pointer into the vfs
     struct posix_acl format to perform permission checking on the mode.

     There's a new dedicated security hook for setting posix acls which
     passes the vfs struct posix_acl not a void pointer. Basing checking
     on the posix acl stored in the uapi format is really unreliable.
     The vfs currently hacks around directly in the uapi struct storing
     values that frankly the security and integrity modules can't
     correctly interpret as evidenced by bugs we reported and fixed in
     this area. It's not necessarily even their fault it's just that the
     format we provide to them is sub optimal.

   - Some filesystems like 9p and cifs need access to the dentry in
     order to get and set posix acls which is why they either only
     partially or not even at all implement get and set inode
     operations. For example, cifs allows setxattr() and getxattr()
     operations but doesn't allow permission checking based on posix
     acls because it can't implement a get acl inode operation.

     Thus, this patch series updates the set acl inode operation to take
     a dentry instead of an inode argument. However, for the get acl
     inode operation we can't do this as the old get acl method is
     called in e.g., generic_permission() and inode_permission(). These
     helpers in turn are called in various filesystem's permission inode
     operation. So passing a dentry argument to the old get acl inode
     operation would amount to passing a dentry to the permission inode
     operation which we shouldn't and probably can't do.

     So instead of extending the existing inode operation Christoph
     suggested to add a new one. He also requested to ensure that the
     get and set acl inode operation taking a dentry are consistently
     named. So for this version the old get acl operation is renamed to
     ->get_inode_acl() and a new ->get_acl() inode operation taking a
     dentry is added. With this we can give both 9p and cifs get and set
     acl inode operations and in turn remove their complex custom posix
     xattr handlers.

     In the future I hope to get rid of the inode method duplication but
     it isn't like we have never had this situation. Readdir is just one
     example. And frankly, the overall gain in type safety and the more
     pleasant api wise are simply too big of a benefit to not accept
     this duplication for a while.

   - We've done a full audit of every codepaths using variant of the
     current generic xattr api to get and set posix acls and
     surprisingly it isn't that many places. There's of course always a
     chance that we might have missed some and if so I'm sure we'll find
     them soon enough.

     The crucial codepaths to be converted are obviously stacking
     filesystems such as ecryptfs and overlayfs.

     For a list of all callers currently using generic xattr api helpers
     see [2] including comments whether they support posix acls or not.

   - The old vfs generic posix acl infrastructure doesn't obey the
     create and replace semantics promised on the setxattr(2) manpage.
     This patch series doesn't address this. It really is something we
     should revisit later though.

  The patches are roughly organized as follows:

   (1) Change existing set acl inode operation to take a dentry
       argument (Intended to be a non-functional change)

   (2) Rename existing get acl method (Intended to be a non-functional
       change)

   (3) Implement get and set acl inode operations for filesystems that
       couldn't implement one before because of the missing dentry.
       That's mostly 9p and cifs (Intended to be a non-functional
       change)

   (4) Build posix acl api, i.e., add vfs_get_acl(), vfs_remove_acl(),
       and vfs_set_acl() including security and integrity hooks
       (Intended to be a non-functional change)

   (5) Implement get and set acl inode operations for stacking
       filesystems (Intended to be a non-functional change)

   (6) Switch posix acl handling in stacking filesystems to new posix
       acl api now that all filesystems it can stack upon support it.

   (7) Switch vfs to new posix acl api (semantical change)

   (8) Remove all now unused helpers

   (9) Additional regression fixes reported after we merged this into
       linux-next

  Thanks to Seth for a lot of good discussion around this and
  encouragement and input from Christoph"

* tag 'fs.acl.rework.v6.2' of git://git.kernel.org/pub/scm/linux/kernel/git/vfs/idmapping: (36 commits)
  posix_acl: Fix the type of sentinel in get_acl
  orangefs: fix mode handling
  ovl: call posix_acl_release() after error checking
  evm: remove dead code in evm_inode_set_acl()
  cifs: check whether acl is valid early
  acl: make vfs_posix_acl_to_xattr() static
  acl: remove a slew of now unused helpers
  9p: use stub posix acl handlers
  cifs: use stub posix acl handlers
  ovl: use stub posix acl handlers
  ecryptfs: use stub posix acl handlers
  evm: remove evm_xattr_acl_change()
  xattr: use posix acl api
  ovl: use posix acl api
  ovl: implement set acl method
  ovl: implement get acl method
  ecryptfs: implement set acl method
  ecryptfs: implement get acl method
  ksmbd: use vfs_remove_acl()
  acl: add vfs_remove_acl()
  ...

---
## [TheAlternateDoctor/Saffron-REST](https://github.com/TheAlternateDoctor/Saffron-REST)@[db7146a26b...](https://github.com/TheAlternateDoctor/Saffron-REST/commit/db7146a26bbdf95d9c3d22a593498c1da2f5b22e)
#### Monday 2023-01-23 09:35:40 by Mathys Ballagny

fuck you *unjavascript your project*
fuck you *java your project*

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[92243b444b...](https://github.com/git-for-windows/git/commit/92243b444bdbcc278017b4947a3248e300daa416)
#### Monday 2023-01-23 10:01:39 by Johannes Schindelin

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
## [JosBarkman/LoudItIs](https://github.com/JosBarkman/LoudItIs)@[23ada83cc4...](https://github.com/JosBarkman/LoudItIs/commit/23ada83cc49b349e90d55fee623db4103ec0c34a)
#### Monday 2023-01-23 10:13:43 by Jozz

MUY IMPORTANTE

Oh, I remember drinking that jar of wine yesterday night!

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[91da50d2dc...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/91da50d2dcfe0713d9d6eb0aaebd011ceb1b3964)
#### Monday 2023-01-23 10:29:30 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[734196fbcd...](https://github.com/mrakgr/The-Spiral-Language/commit/734196fbcd8819e18757d5f8596e4737dcc24a8b)
#### Monday 2023-01-23 11:30:23 by Marko Grdinić

"10:10am. I am up. Let's see. Do I start applying or do I start working on ML with Z? Time to load it up.

No, emails at all. I start applying. I have no idea why I haven't gotten an answer by today, but it doesn't really matter. I need to find my own luck.

Let me add that game project back to my resume.

...You know what, let me get rid of the dark extension for Google Docs. It doesn't matter since I am writing in pageless mode with a gray background.

...For some reason the Manage Extensions is grayed out.

https://chrome.google.com/webstore/detail/google-docs-dark-mode/lgjhepbpjcmfmjlpkkdjlbgomamkgonb?hl=en

For some reason the inbuilt search sucks. But this has remove from chrome...

Ah, maybe it is a Chrome extension instead of a Docs one?

10:20am. This is ridiculous, where is that resume with the GVGAI port?

///

* GVGAI F# port
- Link: https://github.com/mrakgr/GVGAI-Fsharp
- Port of the Python library of the same name.
- A DSL for making simple games of the kind suitable for training RL agents.
- Tech used: F#, FParsec, XNA.

///

I found this in my journal. Let me put it back in.

10:25am. I added this back to my resume, as well put in 2 months of game programming. I also added 2 years of imperative programming to reflect my middle and high school experience.

10:30am. Now, I need to start applying for real.

10:35am. The stupid AngelList thing wants a company.

> Just getting started? You can also add relevant volunteer or project experiences

How do I do this?

Ah, I can just put in the stub. At the bottom it also says create a particular category.

10:55am. Ok, I've touched up my profile. I'll try applying to some senior positions like at AssemblyAI, but now my focus should just be to get an in regardless of the salary.

> What are some strategies you can use to scale a python rest application?*

The AssemlyAI application is asking me long winded questions like these. I really shouldn't be applying here. I thought the plan was to go for a startup?

11am. Forget it. It has a lot of questions up front just to apply which waste my time. Let me find some startups.

https://angel.co/jobs?job_listing_id=2528542

This thing pays 20-30k pounds. I guess I'll apply here too...no it does not support my location.

11:20am. I've applied to 13 places so far. Let me also put a message on the fsharp jobs twitter. Where was the link. I have it somewhere in my journal.

https://twitter.com/fsharpjobs?lang=en

Oh it is here.

> Ping me

How do I do that on twitter?

https://www.engadget.com/2010-11-11-twitter-adds-ping-functionality-to-user-pages.html

Ah, ping is an actual thing.

No wait, that can't be it.

///

A hobbyist with many years of experience in functional programming looking to turn pro. Looking for a remote only job. #fsharp preferred.

Resume: https://docs.google.com/document/d/1D6roVeWFWkwtSfSRr5ac3utd-qSvTtTgBMIbaQ0ZoTo/edit?usp=sharing

///

https://twitter.com/fsharpJobs/status/1579730683278536704

How do I ping this guy?

> Type the “@” symbol before the username(s) when addressing a particular account(s). Example: "I'm Tweeting on @Twitter!" Click or tap Tweet to post. Note: If your Tweet is a reply, the icon to post will say Reply.

11:50am. I posted a link to my resume.

12pm. I unpublished some of the old resumes that I've published in Docs. It seems that publishing a document is different from sharing it. Now that this has been done, I have only a single resume out there.

https://twitter.com/Ghostlike

Here is a link to my resume on top of my Twitter profile. Good. Now...

I think this is good.

12:05pm. I haven't really played all my cards, but there is no point in applying to 100 different places in a single day. I doubt I'll get accepts from most of these places as most of them are looking for seniors, but I only need one. And I'll get it at some point if I keep persevering.

Ah yes, Tessian. I remember now. I applied there before, and got an invite to do some HR problem, but I decided to skip it.

...Sigh, AngelList's search sucks. Do the words I am putting in mean anything at all to it?

12:15pm. Ah, whatever.

https://angel.co/company/tessian/jobs

I find it through google search...Ah, it is not a remote job I can apply to. It requires every candidate to be in the country. Skip then. I was just lingering in my mind.

Ok, good enough, good enough. Applied to a few more places while I was at it.

Let me just think, what do I have left?

'Hire me' threads on HN. Its own job postings. YCombinator jobs. The /twg/ thread on /g/. Usually people don't look for jobs there, but I could, I don't really care about being doxed.

12:25pm. Ok, I'll this run for two weeks, and if I get nothing from it, I'll apply to more places after that. It will take time to find a job either way so let's not rush it. The important thing is to keep a cool head and not get insecure. I should focus on my hobbies for the time being. The UPMEM backend I did was ideal practice for any coding interview questions.

It got rid of the rust. Now, let me do the chores and have breakfast here. After that I'll write more of Heaven's Key."

---
## [DannyBoy3642/tgstation](https://github.com/DannyBoy3642/tgstation)@[a9fda932e2...](https://github.com/DannyBoy3642/tgstation/commit/a9fda932e2a9d8cf20f5f74fdcbdbcca86d580e6)
#### Monday 2023-01-23 12:09:37 by Tim

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
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[66b7310039...](https://github.com/timothymtorres/tgstation/commit/66b7310039297843b01c5b14a9b59180909ab52c)
#### Monday 2023-01-23 12:37:10 by Rhials

STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

---
## [AthenaPrjk/kernel_xiaomi_mt6768](https://github.com/AthenaPrjk/kernel_xiaomi_mt6768)@[de286ae8e5...](https://github.com/AthenaPrjk/kernel_xiaomi_mt6768/commit/de286ae8e5c36738bfe0fa0524648fcc03c16f2d)
#### Monday 2023-01-23 12:50:40 by Peter Zijlstra

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

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[bf73344399...](https://github.com/Jacquerel/orbstation/commit/bf73344399f4b372c13d367cbbd8a40bec23916b)
#### Monday 2023-01-23 12:51:32 by Time-Green

[READY] DRAMATIC SHUTTLES!! You can now fly around the shuttle (#71906)

You can move around shuttles during transport now! Instead of them
teleporting you instantly into deepspace, you can move around somewhat
depending on your space-mobility and grip-strength.


![image](https://user-images.githubusercontent.com/7501474/206866132-3fae024c-a8a2-4f4a-b4b8-37c96a254498.png)

**Please watch the demonstration aswell, it should answer most
questions:**
https://www.youtube.com/watch?v=Os77qDOVSXE

Interactions:
- Being within armsreach of a wall or solid object means you 'cling',
where the shuttle pull is very weak and you can basically run around the
shutt;e (but dont fuck up or you're gone)
- Being in range of nothing gives you a very heavy pull, you can barely
resist if you have a decent jetpack
- Objects are instantly power-yeeted
- Being pulled or riding something excempts you from hyperspace pull
- Touching a space tile while being on hyperspace dumps you in
deepspace, you either go back to the shuttle or enjoy deepspace
- On shuttle hyperspace tiles are a lot less dangerous, and will instead
launch and freeze you instead of teleporting you into deepspace
- In-case it wasn't obvious, you can rest outside the shuttle as long as
something is blocking your path. I think it's funny but I might nerf it

:cl:
add: You can now fly around the shuttle during transit! Woohoo! You can
either cling to the side or grab a jetpack and try and keep up with the
shuttle! Carps can move around freely in hyperspace
qol: Increased shuttle hyperspace size from 8 tiles to 16
/:cl:

- [x] Find a way to detect when a shuttle arrives and do something with
the shit left in hyperspace

Things I will do in another PR: 
- Engines spit fire and hurt (almost finished but I want to keep this
small)
- Random shuttle events. You might run into dust meteors or migrating
carps OR A CHANGELING INFILTRATOR
- Hyperspace turfs on the shuttle pull you under the shuttle

### Why it's good for the game
It's so much more immersive than being instantly teleported into
deepspace. It gives you a chance to recover if you get spaced or for
daredevils to look cool

It's also just very cool idk

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[97db4ecca4...](https://github.com/Jacquerel/orbstation/commit/97db4ecca46ddac5b10f6bd7b2088fc2bd1f5aea)
#### Monday 2023-01-23 12:51:32 by Jeremiah

Adds the Cursed quirk  (#72317)

## About The Pull Request
Adds a silly negative quirk inspired by fallout's bloody mess.

Bad luck interactions for
- Microwaving
- Cigarette coupons
- Russian roulette
- Vending machines
- Ledges
- Slipping

All of which have a chance to kill you, which, by the way, causes you to
**delimb and explode**.

This changes the admin smite as well since it's all the omen component.
Giving permanent omens will mean the player will gib on death, which is
super probable given the insane base damage from bonking your head.
Permanent omen smites are basically dooming someone to die of natural
causes.

<details>
<summary>GIFs</summary>


![dreamseeker_ZE6hyRdYet](https://user-images.githubusercontent.com/42397676/209779120-f7d76862-91e2-4366-a49d-e93366d96faf.gif)

updated: Death no longer fully gibs (carbons)

![dreamseeker_8S8r6B6gMM](https://user-images.githubusercontent.com/42397676/209874302-2e24f581-ffda-42e7-9794-dbe0fff2ff5b.gif)

Panic at seeing bad omen coupons

![dreamseeker_tykHbePTSS](https://user-images.githubusercontent.com/42397676/209887936-5d7f5edf-6fa2-41c7-8503-37432b49c7c0.gif)


![3](https://user-images.githubusercontent.com/42397676/209885388-90523f2c-531a-4928-96b2-c902552cbbbc.png)
</details>

## Why It's Good For The Game
Adds a bit of physical comedy and difficulty for players that want it.
## Changelog
:cl:
add: Hope you saved for a rainy day: Added the 'Cursed' quirk which
causes excessive slippage and... other difficulties.
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Timberpoes <silent_insomnia_pp@hotmail.co.uk>
Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[acb96fee1d...](https://github.com/Jacquerel/orbstation/commit/acb96fee1d0f6605992280d751a7b9930e3a7211)
#### Monday 2023-01-23 12:51:32 by MrMelbert

Refactors memories to be less painful to add and apply, moves memory detail / text to memory subtypes. Adds some new memories to demonstrate.  (#72110)

## About The Pull Request

So, a huge issue with memories and - what I personally believe is the
reason why not many have been added since their inception is - they're
very annoying to add!

Normally, adding subtypes of stuff like traumas or hallucinations are as
easy as doing just that, adding a subtype.

But memories used this factory argument passing method combined with
holding all their strings in a JSON file which made it just frustrating
to add, debug, or just mess with.

It also made it much harder to organize new memories keep it clean for
stuff like downstreams.

So I refactored it. Memories are now handled on a subtype by subtype
basis, instead of all memories being a `/datum/memory`.

Any variety of arguments can be passed into memories like addcomponent
(KWARGS) so each subtype can have their own `new` parameters.

This makes it much much easier to add a new memory. All you need to do
is make your subtype and add it somewhere. Don't need to mess with jsons
or defines or anything.

To demonstrate this, I added a few memories. Some existing memories had
their story values tweak to compensate.

## Why It's Good For The Game

Makes it way simpler to add new memories. Maybe we'll get some more fun
ones now?

## Changelog

:cl: Melbert
add: Roundstart captains will now memorize the code to the spare ID
safe.
add: Traitors will now memorize the location and code to their uplink.
add: Heads of staff winning a revolution will now get a memory of their
success.
add: Heads of staff and head revolutionaries who lose their respective
sides of the revolution also get a memory of their failure.
add: Completing a ritual of knowledge as a heretic grants you a quality
memory.
add: Successfully defusing a bomb now grants you a cool memory. Failing
it will also grant you a memory, though you will likely not be alive to
see it.
add: Planting bombs now increase their memory quality depending on how
cool the bomb is.
refactor: Memories have been refactored to be much easier to add.
/:cl:

---
## [dscho/git](https://github.com/dscho/git)@[6c065f72b8...](https://github.com/dscho/git/commit/6c065f72b8d581eee53ab82e82da049ee492bf11)
#### Monday 2023-01-23 13:09:45 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Kush1Push1/myrat](https://github.com/Kush1Push1/myrat)@[2b9eba0fe0...](https://github.com/Kush1Push1/myrat/commit/2b9eba0fe06284c58a80303698784c7ccede75f4)
#### Monday 2023-01-23 14:36:37 by SkyratBot

[MIRROR] Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins [MDB IGNORE] (#18189)

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

* Sorting how did I miss it

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [Autisem/tgstation](https://github.com/Autisem/tgstation)@[5250b1fcc6...](https://github.com/Autisem/tgstation/commit/5250b1fcc6aca1aa6d6b0f9ec81ce6ad5fe2fa03)
#### Monday 2023-01-23 15:29:44 by san7890

Captain's Spare ID Safe Can Only Hold ID Cards (#72584)

## About The Pull Request

I've personally seen this strategy play out the exact same way on more
than one occasion in an higher frequency lately (I've never played as
either side, just witnessed it)- and it always just seems to be an abuse
of a skewed in-game mechanic. So, this PR makes it so that you can only
put IDs into the spare ID safe. Nothing else.
## Why It's Good For The Game

I think this balance change is needed because it really sort of ruins
what I like about nuclear operatives, having to run around and stay
fluid for whatever the nuclear operatives could have, not "HAHA WE WILL
PUT IT IN OUR (NEARLY) IMPENETRABLE SAFE THAT THEY WILL NEED TO USE A C4
DIRECTLY ON AND JUST END UP PLAYING BLOONS TOWER DEFENSE SIX AS WE AWAIT
THOSE RED FUCKS TO ARRIVE". I miss when it would be fun to inject it
into a monkey who could crawl around vents, put it in a disposals loop
around the station to keep the nukies on a wild goose chase, or just
holding your ground in the brig and retreating if they batter you down.
It's just a very OP location in a very OP place with lots of warranted
OP armor for it's intended use case, which is not really being followed
by putting the all-important disk in the safe.

It's just very strong overall due to how protected-from-damage the spare
ID safe is, and I don't really like the fact that this is emerging as a
new "meta gameplay" (even used when there aren't any nuclear
operatives), it just sullies the different variety of ways you can
defend yourself against nuclear operatives when there appears to be
**the clear choice**. I don't like that concept where you can have a
strategy so good that you _shouldn't_ do it.

Also, it's an _ID Safe_. Not a disk safe.
## Changelog
:cl:
balance: Due to materials costing a lot more than ever, Nanotrasen's
Spare ID Safe Supplier have cut down on the space inside of the ID Safe,
meaning you can only cram in things as thin as an ID Card.
/:cl:

---
## [plogs/asopposedtowhat.com](https://github.com/plogs/asopposedtowhat.com)@[5cca77412a...](https://github.com/plogs/asopposedtowhat.com/commit/5cca77412a8133950d9b852a823f3099238eb0a0)
#### Monday 2023-01-23 16:16:03 by Steve Isaacson

 - incremental checkin
   - content/posts/personal-pronoun-respect.md
     - Removed Thank you sir. Added compliance
--------------------------------------------------
24,26c24,26
< with someone else's worldview, like it or not and no discussion
< necessary, and then change what I say. "Thank you Sir, may I have
< another?"[^1]
---
> with someone else's worldview, like it or not, no discussion
> necessary, and then change what I say. So it's not really respect
> that's being asked for, it's compliance.
31,32c31,32
< personal pronouns. You'll get used to it. Why don't you just be
< _nice?_"
---
> personal pronouns. You'll get used to it. Why don't you just _be
> nice?_"
36,39c36
< Why don't you go fuck yourself?
<
<
< [^1]: History of the phrase "Thank you sir, may I have another" http://answers.google.com/answers/threadview?id=351627
---
> Why don't you just go _fuck yourself_?

---
## [LoopyTheSlayerFanGirl/animations-haha](https://github.com/LoopyTheSlayerFanGirl/animations-haha)@[6adbc48a84...](https://github.com/LoopyTheSlayerFanGirl/animations-haha/commit/6adbc48a84016ca753cfa31d074c0f78566a6a9b)
#### Monday 2023-01-23 16:28:06 by LoopyTheSlayerFanGirl

fuckoing girl man i love them so much

i love girl ahhhhhhhhh womeeeeen kiiiiisng

---
## [Zenitheevee/Skyrat-tg](https://github.com/Zenitheevee/Skyrat-tg)@[1737ab8598...](https://github.com/Zenitheevee/Skyrat-tg/commit/1737ab8598dc94f6c5d8a9f11d8b8bc5a75055d6)
#### Monday 2023-01-23 16:45:06 by SkyratBot

[MIRROR] Fixes parallax on >2 level maps going fucky with optimized multiz [MDB IGNORE] (#18298)

* Fixes parallax on >2 level maps going fucky with optimized multiz (#72169)

## About The Pull Request

We no longer always render parallax.
This was causing issues because we can't isolate the white of space from
the vaugely white of everything else.

So instead, if your parallax plane is out of view, we'll not only
disable it, but we'll disable the strand we send from the main plane TO
it.

Instead only blending against the bottom stack.

This does mean there's a possibility for fullwhite on z transition
borders (potentially fixable), or when hijacking the plane (also
fixable, but significantly more annoying).

This is enough to make large maps functional though, so I'm happy with
it

## Why It's Good For The Game

Allows for #71731 and other maps like it. Makes my code actually work

## Changelog
:cl:
fix: Using optimized multiz on > 2 z layer maps will no longer cause
fucko bungo
/:cl:

* Fixes parallax on >2 level maps going fucky with optimized multiz

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [qn895/kibana](https://github.com/qn895/kibana)@[afb09ccf8a...](https://github.com/qn895/kibana/commit/afb09ccf8a61d610e8e3d8beb2c80f413f1b33c5)
#### Monday 2023-01-23 17:13:59 by Spencer

Transpile packages on demand, validate all TS projects (#146212)

## Dearest Reviewers 👋 

I've been working on this branch with @mistic and @tylersmalley and
we're really confident in these changes. Additionally, this changes code
in nearly every package in the repo so we don't plan to wait for reviews
to get in before merging this. If you'd like to have a concern
addressed, please feel free to leave a review, but assuming that nobody
raises a blocker in the next 24 hours we plan to merge this EOD pacific
tomorrow, 12/22.

We'll be paying close attention to any issues this causes after merging
and work on getting those fixed ASAP. 🚀

---

The operations team is not confident that we'll have the time to achieve
what we originally set out to accomplish by moving to Bazel with the
time and resources we have available. We have also bought ourselves some
headroom with improvements to babel-register, optimizer caching, and
typescript project structure.

In order to make sure we deliver packages as quickly as possible (many
teams really want them), with a usable and familiar developer
experience, this PR removes Bazel for building packages in favor of
using the same JIT transpilation we use for plugins.

Additionally, packages now use `kbn_references` (again, just copying the
dx from plugins to packages).

Because of the complex relationships between packages/plugins and in
order to prepare ourselves for automatic dependency detection tools we
plan to use in the future, this PR also introduces a "TS Project Linter"
which will validate that every tsconfig.json file meets a few
requirements:

1. the chain of base config files extended by each config includes
`tsconfig.base.json` and not `tsconfig.json`
1. the `include` config is used, and not `files`
2. the `exclude` config includes `target/**/*`
3. the `outDir` compiler option is specified as `target/types`
1. none of these compiler options are specified: `declaration`,
`declarationMap`, `emitDeclarationOnly`, `skipLibCheck`, `target`,
`paths`

4. all references to other packages/plugins use their pkg id, ie:
	
	```js
    // valid
    {
      "kbn_references": ["@kbn/core"]
    }
    // not valid
    {
      "kbn_references": [{ "path": "../../../src/core/tsconfig.json" }]
    }
    ```

5. only packages/plugins which are imported somewhere in the ts code are
listed in `kbn_references`

This linter is not only validating all of the tsconfig.json files, but
it also will fix these config files to deal with just about any
violation that can be produced. Just run `node scripts/ts_project_linter
--fix` locally to apply these fixes, or let CI take care of
automatically fixing things and pushing the changes to your PR.

> **Example:** [`64e93e5`
(#146212)](https://github.com/elastic/kibana/pull/146212/commits/64e93e580679dd55f4fdf19bd01402bc478a1a75)
When I merged main into my PR it included a change which removed the
`@kbn/core-injected-metadata-browser` package. After resolving the
conflicts I missed a few tsconfig files which included references to the
now removed package. The TS Project Linter identified that these
references were removed from the code and pushed a change to the PR to
remove them from the tsconfig.json files.

## No bazel? Does that mean no packages??
Nope! We're still doing packages but we're pretty sure now that we won't
be using Bazel to accomplish the 'distributed caching' and 'change-based
tasks' portions of the packages project.

This PR actually makes packages much easier to work with and will be
followed up with the bundling benefits described by the original
packages RFC. Then we'll work on documentation and advocacy for using
packages for any and all new code.

We're pretty confident that implementing distributed caching and
change-based tasks will be necessary in the future, but because of
recent improvements in the repo we think we can live without them for
**at least** a year.

## Wait, there are still BUILD.bazel files in the repo
Yes, there are still three webpack bundles which are built by Bazel: the
`@kbn/ui-shared-deps-npm` DLL, `@kbn/ui-shared-deps-src` externals, and
the `@kbn/monaco` workers. These three webpack bundles are still created
during bootstrap and remotely cached using bazel. The next phase of this
project is to figure out how to get the package bundling features
described in the RFC with the current optimizer, and we expect these
bundles to go away then. Until then any package that is used in those
three bundles still needs to have a BUILD.bazel file so that they can be
referenced by the remaining webpack builds.

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [akshaykamath45/CP](https://github.com/akshaykamath45/CP)@[739e5c3d25...](https://github.com/akshaykamath45/CP/commit/739e5c3d2553c55c80a60162c578ed1d21fc6c01)
#### Monday 2023-01-23 18:22:53 by Akshay Kamath

Boy or Girl

Those days, many boys use beautiful girls' photos as avatars in forums. So it is pretty hard to tell the gender of a user at the first glance. Last year, our hero went to a forum and had a nice chat with a beauty (he thought so). After that they talked very often and eventually they became a couple in the network.

But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man! Our hero is very sad and he is too tired to love again now. So he came up with a way to recognize users' genders by their user names.

This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.

Input
The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.

Output
If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).

Link:https://codeforces.com/problemset/problem/236/A

---
## [CandleJaxx/Skyrat-tg](https://github.com/CandleJaxx/Skyrat-tg)@[38226f155d...](https://github.com/CandleJaxx/Skyrat-tg/commit/38226f155d94035bf1a0693d4a54502bd4031bfe)
#### Monday 2023-01-23 18:25:09 by SkyratBot

[MIRROR] converts contraband file into poster file, makes holiday posters work (kind of) [MDB IGNORE] (#18323)

* converts contraband file into poster file, makes holiday posters work (kind of) (#72131)

## About The Pull Request

The first part of this is just something that bothered me when I was
messing around with something that I will PR in the new year,
contraband.dm and dmi is ONLY posters. There's nothing else in there and
there are plenty of official posters, and if with #71717 we will also
add holiday posters to the mix then I think that its time to retire
contraband and make it poster.

Some small things I did while messing with it was change some variables
that were single letters into actual variable names, but overall this
part of the pr is not a player facing change.

That said, speaking of #71717 I think that it didn't work? Or didn't
work the way that it was supposed to? All of the spawned posters aren't
instances of festive posters, they are instances of normal posters, so
the code on initialize was not doing anything and the only reason the
holiday_none poster was showing up was because of the proc in randomize
spawning the posters in as those other posters. Because it didn't
actually _become_ poster/official/festive it never could do the proc
that turns it into a poster for the holiday that is actually occurring.

But then when I made it work and it turned into the generic posters I
decided that it would be better if instead of 30% of all posters being a
half finished mess, that if there wasn't a holiday poster it just
wouldn't replace them at all. I have poster Ideas and Dreams so I will
try to help with adding to more holiday posters but not in this PR.

What IS in this PR though, is a new traitor poster that appears during
the holidays.

![dreamseeker_MxxBzXIxiy](https://user-images.githubusercontent.com/116288367/208793262-9d4a45dc-f7bb-4208-b3c3-78cb68cf9af5.png)

This is a generic evil holiday poster that will replace normal evil
posters in the evil poster objective, because I agree with #72003 that
it should be a feature.

## Why It's Good For The Game

Contraband file is just posters already, this is easier for people to
find the posters.
I like holiday posters and think that we should have them and add more,
it is a fun easy thing to add to a lot of the microholidays to make them
more visible in addition to the name generation, but I don't want to see
the unfinished holiday poster so I do think that it's better to only
have them spawn if the holiday actually has a poster. Looking forward to
febuary!

## Changelog

:cl:
add: during holidays the spread syndicate propaganda through posters
objective has a chance of spawning evil holiday poster
fix: framework for holiday posters is more functional and modular
code: contraband.dm file and contraband.dmi file are both now poster.dm
and poster.dmi
/:cl:

* converts contraband file into poster file, makes holiday posters work (kind of)

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>

---
## [RoOLeary/busylittlepixels](https://github.com/RoOLeary/busylittlepixels)@[56c25ca504...](https://github.com/RoOLeary/busylittlepixels/commit/56c25ca5048cd0bcc9bcb782b1431891f80fd591)
#### Monday 2023-01-23 18:41:18 by Ronan

rid this lovely Next.js instance of shitty, horrible Prismic. Gonna do this the old fashioned way

---
## [patrickthefriendlystarfish/harry-potter-gen-z](https://github.com/patrickthefriendlystarfish/harry-potter-gen-z)@[433662f486...](https://github.com/patrickthefriendlystarfish/harry-potter-gen-z/commit/433662f4863e9dbfc28ef17a42bd4df4691f87bc)
#### Monday 2023-01-23 19:46:48 by patrickthefriendlystarfish

Just something I found funny

Sorry If this shows up twice, I tried to suggest and edit but I think I did it wrong. I changed "speedy af" on line 30 to "fast as fuck boi" because I thought it would be kinda funny

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[29a99e8937...](https://github.com/TaleStation/TaleStation/commit/29a99e8937e515d9b94407d549941008d7fec3b3)
#### Monday 2023-01-23 19:58:51 by TaleStationBot

[MIRROR] [MDB IGNORE] Magnitis is more aggressive, uses throw_at instead of Move at higher stages (#4207)

Original PR: https://github.com/tgstation/tgstation/pull/72739
-----
## About The Pull Request

I got this disease yesterday and was super disappointed by the actual
effects. Rather than suffer an unending waves of metal objects being
thrown at my head, I noticed that stuff on the bridge kept getting
disorganized, shrugged, and moved on.

Now, stages 3/4 of Magnitis will use throw_at instead of just moving
objects to the infectee. This can hurt or even kill the victim in
extreme cases. Remember to duck!

The messages about electrical shocks will now appear when a magnetic
pulse occurs. Some of the disease messages have been slightly altered to
fit this.

Also, while we're on the subject -- Is there a joke behind Magnitis'
agent "Fukkos Miracos"? Why does Magnitis make you ponder upon the
nature of miracles? Why did it make you feel like "clowning around"?
This stuff was written over a decade ago and I get the feeling it's
referencing something that is beyond me.
## Why It's Good For The Game

Gives an old disease a bit of a facelift. Makes it more _dynamic_ and
_engaging_.
## Changelog
:cl: Rhials
balance: The Magnitis disease will now hurl objects at infectees at
higher stages. Watch your head!
/:cl:

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d0732abf1f...](https://github.com/TaleStation/TaleStation/commit/d0732abf1fc8a36fea41661536c92164c8e960ec)
#### Monday 2023-01-23 19:58:51 by TaleStationBot

[MIRROR] [MDB IGNORE] Water will now make you wet (#4208)

Original PR: https://github.com/tgstation/tgstation/pull/72844
-----
## About The Pull Request
Water, when exposed to a mob either via `TOUCH` or `VAPOR` application,
will now apply wet stacks to said mob according to the amount of water
used. For touch application, the ratio is 0.5 wet stack per unit of
water, whereas for vapor application (so for foam and sprays), that
ratio is lowered to 0.1 wet stack per unit of water. Yes, that would
mean that you could now put someone out by spraying enough water at them
with a spray bottle (usually around 50-150u), and I think that is quite
simply hilarious.

As a reminder, wet stacks decay slowly over time, however obviously
raising your fire stacks (so being exposed to something that's on fire,
for instance) will speed up that decay, once
https://github.com/tgstation/tgstation/pull/72843 is merged. I separated
them in two PRs because honestly the fact that being wet made you more
flammable just sounds like a fuckup of the year if I've ever heard one.

I also updated the unit test of water's `expose_mob()` proc, to check
that wet stacks were being applied properly, hopefully making sure that
there's no regression on that part in the future.

## Why It's Good For The Game
The number one thing you think of when you think of the word wet is
water. Water should make you wet, it only makes sense.

## Changelog

:cl: GoldenAlpharex
balance: Water now makes you wet on touch and vapor application, with
vapor being much less effective than touch. Yes, that means you can now
spend two minutes putting someone out with a spray bottle full of water!
/:cl:

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[4dac916458...](https://github.com/TaleStation/TaleStation/commit/4dac916458a5eb84d56f24091a9dddf3f9a54d41)
#### Monday 2023-01-23 19:58:51 by TaleStationBot

[MIRROR] [MDB IGNORE] Being wet no longer causes you to be EXTRA flammable (#4209)

Original PR: https://github.com/tgstation/tgstation/pull/72843
-----
## About The Pull Request
Making it a separate PR because I think that's a very funny fuckup, who
knows, maybe one of the fuckups of the year, even.

Being wet no longer causes you to be even more flammable, and instead
properly lets you dry up instead of catching on fire even faster when
receiving fire stacks.

What caused this was that there was some double-negatives happening,
which meant that both fire and wet stacks would be increased together
when both were present at once, rather than both being reduced and one
of the two cancelling out the other.

## Why It's Good For The Game
Being wet shouldn't make you go up in flames faster. Now it will
actually protect you from flames according to your amount of wet stacks,
as intended.

## Changelog

:cl: GoldenAlpharex
fix: Being wet no longer causes you to be EXTRA flammable, and instead
properly protects you from catching on fire. If you're wet enough, of
course.
/:cl:

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [google/boringssl](https://github.com/google/boringssl)@[0d5b608614...](https://github.com/google/boringssl/commit/0d5b6086143d19f86cc5d01b8944a1c13f99be24)
#### Monday 2023-01-23 20:29:58 by David Benjamin

Maintain a frame pointer in aesni-gcm-x86_64.pl and add SEH unwind codes

Some profiling systems cannot unwind with CFI and benefit from having a
frame pointer. Since this code doesn't have enough register pressure to
actually need to use rbp as a general register, this change tweaks
things so that a frame pointer is preserved.

As this would invalidate the SEH handler, just replace it with proper
unwind codes, which are more profiler-friendly and supportable by our
unwind tests. Some notes on this:

- We don't currently support the automatic calling convention conversion
  with unwind codes, but this file already puts all arguments in
  registers, so I just renamed the arguments and put the last two
  arguments in RDI and RSI. Those I stashed into the parameter stack
  area because it's free storage.

- It is tedious to write the same directives in both CFI and SEH. We
  really could do with an abstraction. Although since most of our
  functions need a Windows variation anyway.

- I restored the original file's use of PUSH to save the registers.
  This matches what Clang likes to output anyway, and push is probably
  smaller than the corresponding move with offset. (And it reduces how
  much thinking about offsets I need to do.)

- Although it's an extra instruction, I restored the original file's
  separate fixed stack allocation and alloca for the sake of clarity.

- The epilog is constrained by Windows being extremely picky about
  epilogs. (Windows doesn't annotate epilogs and instead simulates
  forward.) I think other options are possible, but using LEA with an
  offset to realign the stack for the POPs both matches the examples in
  Windows and what Clang seems to like to output. The original file used
  MOV with offset, but it seems to be related to the funny SEH handler.

- The offsets in SEH directives may be surprising to someone used to CFI
  directives or a SysV RBP frame pointer. All three use slightly
  different baselines:

  CFI's canonical frame address (CFA) is RSP just before a CALL (so
  before the saved RIP in stack order). It is 16-byte aligned by ABI.

  A SysV RBP frame pointer is 16 bytes after that, after a saved RIP and
  saved RBP. It is also 16-byte aligned.

  Windows' baseline is the top of the fixed stack allocation, so
  potentially some bytes after that (all pushreg and allocstack
  directives). This too is required to be 16-byte aligned.

  Windows, however, doesn't require the frame register actually contain
  the fixed stack allocation. You can specify an offset from the value
  in the register to the actual top. But all the offsets in savereg,
  etc., directives use this baseline.

Performance difference is within measurement noise.

This does not create a stack frame for internal functions so
frame-pointer unwinding may miss a function or two, but the broad
attribution will be correct.

Change originally by Clemens Fruhwirth. Then reworked from Adam
Langley's https://boringssl-review.googlesource.com/c/boringssl/+/55945
by me to work on Windows and fix up some issues with the RBP setup.

Bug: b/33072965, 259
Change-Id: I52302635a8ad3d9272404feac125e2a4a4a5d14c
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/56128
Reviewed-by: Adam Langley <agl@google.com>
Commit-Queue: David Benjamin <davidben@google.com>

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[df1b43d49e...](https://github.com/willior/Action_RPG_1/commit/df1b43d49e598018c7b722cf1317204b5dfeb8d4)
#### Monday 2023-01-23 21:21:03 by willior

fixing Enemy despawn/spawn system

each Enemy should have a VisilbityOnScreenNotifier2D child. right now, each instance of it is pre-made in-editor. we should remove it, and instead automatically instance/add one/connect its signal dynamically.
created "despawn_notifier" scene, which automatically gets instantiated and added at the end of EnemyClass._ready(). when the despawn_notifier is added to an enemy, on _ready(), it calls:

connect("screen_exited", Callable(get_parent(), "despawn_offscreen"))

... connecting its "screen_exited" signal to its parent's (enemy body) "despawn_offscreen" method. the despawn_notifier rect size is 32x32.

when enemy.despawn_offscreen() is called, first we check if the enemy's charmed, because charmed enemies shouldn't despawn - they should follow the Player. so that functionality has been refactored, but each enemy will probably have to be reconfigured (just testing with the basic Bat class for now). so when an enemy goes offscreen, an "enemy_spawner" is instantiated in its place. the enemy_spawner has a layer property (on despawn_offscreen(), we call new_enemy_spawner.layer = layer). the enemy_spawner is added to the parent of the body that called despawn_offscreen(), which in this case should/is always going to be an "Enemies" node that is a child of the current layer's TileMap.
when an Enemy is added to the SceneTree, at the end of its _ready() method, it calls:

call_deferred("add_child", DESPAWN_NOTIFIER.instantiate())

which adds a despawn_notifier child to the enemy. the despawn_notifier rect size is 16x16, half the size of the enemy_spawner. in other words, in order for an enemy to despawn, it has to be double the distance outside the screen than if it were to spawn (despawn = far; spawn = close). i have a feeling that these values should be bigger, and/or that at some point we will want to customize them based on the sizes of enemies, but we will worry about that another day because it works fine for what we have now.

semi-related: need to configure PlayerSpawns to handle/assign layer values when Player zones.

another note: i will gradually be changing the current naming conventions. most importantly, all filenames/folders should be in lowercase with underscores representing spaces in order to facilitate OS compatibility in the future. secondarily, all constant variables should be UPPERCASE_UNDERSCORED. instantiated scene variables should be lowercase_underscored; right now, many are SnakeCase. but that's less important.

it's important to remember the purpose of each Global layer-related method. the PhysicsLayer setters do just that; the z_index setter does just that. the change_floor() function, however, does both, depending on the layer received. right now, the only place where change_floor() is called is on player.climb_end(), which is called when a player exits a ladder.
in order to properly set the layer behaviour of objects, we need to make sure both their collision & z-indexes are getting set properly. on Player, i don't think this should be a problem, because the player will be getting their layer from PlayerSpawners (for now, i've coded functionality into the Camera2D so that it also has a 'layer' parameter; if the Player is spawned WITHOUT a PlayerSpawner, ie. it defaults to the Camera position, it also gets its layer value from the Camera's layer value). on each body's _ready() method, we call both set_collision_layer_mask(self, layer) and set_z_index_by_layer(self, layer), splitting the collision behaviour and the z-index setting into two different functions.

...holy fucking christ. disregard everything about z_index setting. objects (players, enemies, pickups) placed on layers (TileMaps) have a RELATIVE z-index, meaning bodies' z_indexes are summed with that of their parent. in other words, when an object has a TileMap parent, its z_index becomes that of the TileMap's, which gets set based on its layer. basically... z_indexes don't need to be set for objects. like, at all, i think. the only time we manually set it is when a player climbs a ladder: climb_start() adds 10 to the z_index; climb_end() subtracts 10, ensuring the player is drawn on top of the ladder regardless of of which layer it's on/from which layer the player enters it.
i've completely mangled my brain. i need to finish this commit before it gets more out of hand than it already has.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3071e2a6df...](https://github.com/treckstar/yolo-octo-hipster/commit/3071e2a6df633c66d5e940b263fadd398fab9fee)
#### Monday 2023-01-23 21:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [PhilippGoecke/postgres](https://github.com/PhilippGoecke/postgres)@[7fed801135...](https://github.com/PhilippGoecke/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Monday 2023-01-23 21:24:09 by Tom Lane

Clean up inconsistent use of fflush().

More than twenty years ago (79fcde48b), we hacked the postmaster
to avoid a core-dump on systems that didn't support fflush(NULL).
We've mostly, though not completely, hewed to that rule ever since.
But such systems are surely gone in the wild, so in the spirit of
cleaning out no-longer-needed portability hacks let's get rid of
multiple per-file fflush() calls in favor of using fflush(NULL).

Also, we were fairly inconsistent about whether to fflush() before
popen() and system() calls.  While we've received no bug reports
about that, it seems likely that at least some of these call sites
are at risk of odd behavior, such as error messages appearing in
an unexpected order.  Rather than expend a lot of brain cells
figuring out which places are at hazard, let's just establish a
uniform coding rule that we should fflush(NULL) before these calls.
A no-op fflush() is surely of trivial cost compared to launching
a sub-process via a shell; while if it's not a no-op then we likely
need it.

Discussion: https://postgr.es/m/2923412.1661722825@sss.pgh.pa.us

---
## [Wuerfel21/spin2cpp](https://github.com/Wuerfel21/spin2cpp)@[903c71ebd8...](https://github.com/Wuerfel21/spin2cpp/commit/903c71ebd887b231162a579d1bd0b13a7445c7fa)
#### Monday 2023-01-23 21:24:14 by Ada Gottensträter

Merge branch 'W21-fix-stupid-fucking-bullshit' into W21-refactor-lblaux

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[38055c066d...](https://github.com/newstools/2023-new-york-post/commit/38055c066dc264e9604b60fff7548277d92f881c)
#### Monday 2023-01-23 21:43:44 by Billy Einkamerer

Created Text For URL [nypost.com/2023/01/23/dear-abby-im-cheating-on-my-boyfriend-he-has-no-idea/]

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[b7f8fe3514...](https://github.com/pytorch/pytorch/commit/b7f8fe351427aa01a45c0b521ccaa9885a61b9b7)
#### Monday 2023-01-23 22:11:22 by Brian Hirsh

Update base for Update on "add torch.autograd._set_view_replay_enabled, use in aot autograd"

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc albanD soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.




[ghstack-poisoned]

---
## [smxi/acxi](https://github.com/smxi/acxi)@[ca474f076d...](https://github.com/smxi/acxi/commit/ca474f076d2b15a881d77566a49807cfebb44d3e)
#### Monday 2023-01-23 23:07:32 by Harald Hope

new version, 3.6.00

The initial mp3 based review of tagging led to a major update: the new TagList
class/package for --taglist. This sends acxi to 3.6.00 since this is a
significant set of new features, and creates an entire new type of
functionality, which also blends very well with newer and existing
tagging/prefill type features.

The preceding changes were started with a more basic MP3 tag update, which added
tags that are same in id3v2.3 and id3v2.4 and have FLAC equivalents. Also used
this as an excuse to also review and add some Vorbis tags that make sense for
acxi to include in auto.tag and tagging/prefill features.

Also went through many features, documentation, etc, fixed logic errors,
inconsistent logic/docs errors, and added more public documention.

--------------------------------------------------------------------------------
SPECIAL THANKS:

1. Once again, to the people who helped make free / libre audio possible, and in
particular, the people who worked so hard for so long at xiph.org to provide the
world with the codecs and tools we now use to listen to and work on audio.

2. To fourtysixandtwo, the acxi packager for Slackware (slackbuilds). The new
--taglist option was his suggestion. This is turning out to be really good and
useful already, since it allows for easy bulk testing of entire sets of
recordings at once, which acxi can then be used to correct.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. SYNC: Because MP3 tagging changed too much between versions, only
id3v2.3/id3v2.4 tags that are the same between versions AND have Vorbis
equivalents are supported.

Good tag FLAC > MP3 id3v2.x mapping resources:

https://wiki.hydrogenaud.io/index.php?title=Tag_Mapping
https://docs.mp3tag.de/mapping/
https://docs.mp3tag.de/mapping-table/

2. AUTOTAG: The tag SUBTITLE in Vorbis/FLAC is super specific, and should be
avoided. https://web.archive.org/web/20120429102447/http://reallylongword.org/\
vorbiscomment/

"SUBTITLE: This field is intended for use with FLAC, in order to connect
specific titles with an embedded cue sheet. A single file can effectively
contain multiple works, indexed by TRACK and INDEX in the case of cue sheets,
and they can be specified using subscripts like “SUBTITLE[TRACK 3]” or
“SUBTITLE[TRACK 7:INDEX 2]”. This should only be used for the case of multiple
works in the same file and not for cases where a single work has multiple
titles."

3. TAGLIST: With certain Vorbis tags when output to Perl, that contain cp-1252
windows characters, Perl simply crashes, or appears to be crashing, when those
get output to screen. This happens currently only with -L [acfi], and basically,
the crash happens when the data is being printed out. You can still find which
track it was to manually correct the tags with acxi, but as far as I know, there
is no way to trap this error and handle it more elegantly since it either just
hangs, or crashes, depending on whether print to screen or Dumper print to
screen. Dumper just crashes when it hits that string.

--------------------------------------------------------------------------------
BUGS:

1. TAG: In --tag, it was changing directory to SOURCE_DIRECTORY, but failed to
remove that from the file string, so tag updates failed unless you were using
-s ./. I hadn't noticed that because I almost always use -s./ with -T.

This led to things like --glob failing too, since it was never working from the
right directory in terms of the path/filename metaflac received.

2. OPTIONS: --nlink would never have worked because it was missing the 'n'
('link').

3. INFOFIX: Bug with date fix, was always showing true for test for dd-mm-yyyy
type, which could lead to failure to then update those dates.

--------------------------------------------------------------------------------
FIXES:

1a. SYNC: For mp3 tagging, was using DATE, didn't check for YEAR, but mp3 is very
likely to fail if you put a date in that value. Now checks for YEAR first, and
falls back to using year (YYYY) extracted from DATE.

Note that DATE is supported somewhat, but syntax differs between:

DATE:
Vorbis: DATE id3v2.3: TDAT; id3v2.4: TXXX:DATE
or
RECORDING DATE:
Vorbis: DATE: id3v2.2: TYE+TDA(+TIM) id3v2.3: TYER+TDAT(+TIME[22]) id3v2.4: TDRC

Docs don't agree, so not using DATE in mp3 except to extract year. Note that
--ty handles the year so we don't need to worry about what the literal syntax
is.

I don't want to get into detecting idv2 subversion, this is a messy non-free
codec and it shows by how poorly they did tagging version to version, as well as
how focused on corporate interests their efforts were.

1b. SYNC: sync was not showing cmd message for --dry, but also was poor code,
repeated, switched to use --dbg 5 command debugger or in --dry mode, to show
command with --dbg 5, or the simple tool command with --dry. Previously didn't
show anything, just 'Would have run:'. That was an oversight, must have messed
that test mode up a long time ago. But now works much better because you can
either see simple mode, or full command debugging mode, which integrates that
to the new $dbg[5] command debugger globally.

1c. SYNC: Never showed that mkdir and copy file were running in test mode, now
shows Test mode: for all 3 syncing actions if verbosity > 0.

2. PREFILL: Some of the prefill field names didn't fully match the listed
possible values. Also made all 2 word type field names support space, -, _, or
no space.

3. TAGLIST/SYNC: Added --no-utf8-convert to main::get_flac_tags(), this is for
all types, mp3, replaygain, and full tag lists.

4. INFOFIX: Was missing a date variant: dd-month-yyyy

5. SYNC/AUTOTAG/TAGLIST: Flac tag reader wasn't escaping file name, which led to
name with $ failing. Also, the mp3 tag string generator was passing the file
name in double quotes, which meant that the $ string was being treated as a
scalar and would have been empty as well. Or maybe caused perl to exit with
error since non declared variable was being attempted.

6. AUTOTAG/PREFILL: Removed ISRC tag from main body of auto.tag, that is a per
track always file, it is a unique idenitifier (or idenfiers in rare cases, like
musicbrainz) per file. I had always thought it was a per recording, not track,
id, but that is wrong.

7. IMAGES: -RI to trigger --image-remove has not worked in a long time, that's
now corrected so -I accepts no value with -RI, -I remove, -I image, or -RI image
as originally intended.

8a. OUTPUT: Added $line_small when no info.txt file found for --infofix, forgot
that.

8b. OUTPUT: Made $line_small more consistent across -Z, -X, and -L to separate
directory processing items.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. TAGLIST: New features: --taglist/-L. Depending on switches, can generate full
report of all tags per FLAC file in directory, a condensed version of those
tags, or data for creating an info.txt file. As with -X, w writes the data to
the file(s).

* a: switch output file from taglist.tag to auto.tag, and change tag:value
separator from '=' to '%:'

* c: generates condensed data from flac tags for tag list. For tags that do not
occur in every file, adds tags before block of tags that use them, and either
replaces them with next value. or if file does not have that tag, UNSETs the
tag.

* f: generates full taglist data. This is default if no args used. Adds UNIQUE
value TAGBLOCK which forces non cascade of tags per file. This is what you want,
so don't change that.

* i: generates info file data from flac tags for screen/info.txt.

* s: skips file exist tests, so will always run in each directory. Not used with
'w'.

* w: writes a, c, i, or f data to respective info.txt, taglist.tag, or auto.tag
files.

i + [cf] can be used together. a activates c by default, unless you specify f. c
and f can't be used together. s can't be used with w.

In latest testing, -Lc is generating the same set of condensed tags the original
files contain, minus some corrected tags, like having 'ALBUM ARTIST' and
ALBUMARTIST tags in the same file, or 'TRACKTOTAL' and 'TOTALTRACKS'. This was
seen in musicbrainz picard tagging at times.

2. AUTOTAG: AutoTag::process_tags() now handles multiline tag values. Which
should be avoided because very few media players support those correctly. But
needed since --taglist a/c/f support multiline tag values.

3. AUTOTAG/AUTOTAG-CREATE: Added --unique, which allows setting one time list
of tags to use only 1x in the file following that tag in the auto.tag file. This
can be used with -A, -S, -M. This will add that list of single use tags to an
existing auto.tag file with -A. Adds that set of tags to the per track tag list,
which are handled differently than block type tags, which can apply to > 1 file
per set.

Only supported for auto.tag creation with -C/-S/-M, or to force the list into
the tagging with -A if it was not set in auto.tag already. The TAGBLOCK value
tells -A to discard all previously found tags after each file processed. This is
only useful with -Lf generated auto.tag files that have complete sets of tags
per file.

-Lf sets a UNIQUE value TAGBLOCK automatically.

-La/-Lc UNSETs tag after last file that used that tag if the previous value is
not replaced by a new one and the next file did not contain that tag in the case
of multi use of a tag situations, so you don't need to do anything there.

4. AUTOTAG/PREFILL/TAGLIST: Added --autotag-file/--atf/--af for one time changes
of auto.tag file name. This was an oversight, but never had cause for it until
testing -La exposed the utility of being able to change auto.tag name to
something else.

5. AUTOTAG/PREFILL: To auto.tag generator, added CONDUCTOR, MIXER, PUBLISHER,
REMIXER, and variants for prefill, like:

CONDUCTOR: Conductor, Conducted by.
MIXER: Mixed by, Mixer, Mastered by, Masterer.
PUBLISHER: Publisher, Label
REMIXER: Remixer, remixed by, remasterer, remastered by.

6. AUTOTAG/TAGLIST: Added WORK, SUBTITLE, TITLESORT tags to list of supported
tags for tagging, but not to auto.tag because those are made for very specific
purposes and are unlikely to be used correctly. See Known Issues 2. Also added a
number of track file specific tags like REPLAYGAIN*, ACOUSTID*, etc, to the
track tags list for -Lc, -La, and -A. This means that track specific tags that
should never be carried over to next file are now protected much better. While
hard to get a complete list of tags that must only occur per file, never common
between files, very good progress was made to tighten this down.

7. IMAGES: Added --image-remove as synonym for -R, --remove-images

8. SYNC: Significantly expanded MP3 tags. Mapped all acxi tags in auto.tag/--tag
that have native mp3 id3v2 tags. Now supported:

ALBUM ALBUMARTIST ARTIST ARTISTSORT COMMENT COMPILATION COMPOSER CONDUCTOR
COPYRIGHT DATE DESCRIPTION DISKNUMBER DISCSUBTITLE DISKTOTAL GENRE ISRC LABEL
MEDIA MOOD MOVEMENTNAME ORGANIZATION PUBLISHER REMIXER SOURCEMEDIA SUBTITLE
TITLE TITLESORT TRACKNUMBER TRACKTOTAL YEAR

Note that because id3v2.x either doesn't have comparable DATE, LOCATION, OPUS,
PERFORMER, PRODUCER, VENUE tags, or v2.3 name is different from v2.4, those tags
are not supported.

9. VERSION: Added $self_patch to allow for checking development patch versions,
like pinxi uses. Helpful to make sure you have the right version. Also added to
--help (and date). This can be helpful during active development.

acxi --version
acxi version: 3.5.06-14 (2023-01-10)

10a. OPTIONS: Added --glob as alternative to --source-glob/-g.

10b. OPTIONS: Added --config/--configuration, to show you current active
configuration values. Shows first to last found, last overrides previous.

11. OUTPUT: Added new print line type: $line_result. This is used to separate
result blocks from processing blocks, before was using $line_small for both
types. this is used in -X, -L, --config, and -C/-S/-M --dry. See CHANGES 2.

--------------------------------------------------------------------------------
CHANGES:

1. CONFIG: Configuration item TAG_FILE has been changed to AUTOTAG_FILE, but
TAG_FILE will keep working. This is because we needed non-ambiguous names with
new TAGLIST_FILE configuration item.

2. OUTPUT: Changed print line small:

-----------------------------------------------------------------

to print line result:

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

for blocks of results in --config, -L, -C/-M/-S --dry, -X. This makes it
easier to tell the results apart from the processing blocks.

3. AUTOTAG-CREATE: -C, -S, -M should not be allowed to run external to the
directory that contains the flac files, that's too risky, so disabled that. I
think that was an oversight.

4. DEBUG: Removed --debug, replaced with specific --dbg x(,y) options globally.
See CODE 3a, 3b.

5. SYNC: Changed default output type to '', ogg is deprecated, and acxi should
not promote it as default. I don't want to assume what people might have been
using before. Added $OUTPUT_TYPE set test for sync to force explicit set in
config file or with -o. Added --config so people can easily check their configs.

--------------------------------------------------------------------------------
DOCUMENTATION:

1a. MAN: Forgot to list AIFF as input type for FLAC output type.

1b. MAN: Added MIXER and REMIXER to --prefill tags. Also cleaned up and made
more consistent prefill tag listing.

1c. MAN: Updated man page debugger section for --dbg xx triggers.

1d. MAN: Added more granular man docs for --dbg

1e. MAN: Fixed typo for config file path, had $HOME/.conf/ not .config/.

2. OPTIONS: Updated top part to have better examples with long and short forms.

3a. MAN/OPTIONS: updateed for -R/-I cleanups and corrections, and to make actions/
choices more clear.

3b. MAN/OPTIONS: Updated to add --glob.

4. MAN/OPTIONS/README.txt/: added for new --taglist, --taglist-file, --unique
options.

5. AUTOTAG-FILE: Sample auto.tag file, updated to add new tags and comments.

6a. DOCS: Created docs/acxi-values.txt to document internal acxi values.

* @dbg - the old --debug was too generic to be useful in real development.

* %run, %test, scalar assignments - document internal use of these variables.

* verbosity levels, and triggering switches.

* configuration items. Always see man for full explanations.

6b. DOCS: Overall, made sure man, help, acxi-values.txt, and internal logic are
the same. Surprising number of oddities had crept in, cleaning those up as they
get discovered.

--------------------------------------------------------------------------------
CODE:

1a. TAG DATA: Refactored flac2mp3_cmd() to make more flexible. Made it return
hash ref, not hash.

1b. TAG DATA: Extended main::get_flac_tags() to return 'all' tags in flac file,
for new package TagList. Changed old 'standard' to 'flac-mp3', since that was
used only to get flac to mp3 tags. Totally rewrote get_flac_tags as well, to be
more robust and dynamic.

2. Switched to qw(...) in some tag lists that are being updated frequently.

3a. DEBUG: Added --dbg [x-xx] for granular debugging. Added dbg switch docs in
docs/acxi-values.txt.

3b. DEBUG: Changed all previous $b_debug to more granular $dbg[x] tests, and
added many commented out say debugging items now that they can be switched off
and on in a more granular fashion.

4. OPTIONS: Major refactor of OptionsHandler, which had gotten messy and hard
to follow/read/use. Also got rid of the hack I used to turn off features by
setting to 0 in each major option item. Now all that is handled in
OptionsHandler::set_switches() and OptionsHandler::verify_selections(), and
options themselves only switch on $run and $test switches and assign values.

5a. SYNC: Changed to explicit sync switched on only if no other actions conflict
in OptionsHandler::set_switches(). This was previously always set to 1, true, on
top of acxi by default, now it's only set to true if no conflicting options are
used.

5b. SYNC: Refactored SyncCollection::convert_file(), that had a lot of
repetetive code, and also switched it to use $dbg[5] show $cmd debugger for both
active and --dry mode, or just the tool name/path in --dry mode. See FIX 10.

6. IMAGE: Redid $run{'image-embed'} and $run{'image-remove'} logic, and made
more predictable and understandable, which is how the failure had crept in.

7. VALIDATION: Validation had a legacy $b_error in every sub which is redundant
since $error_message can be tested t/f in all cases, removed all those.

---
## [git/git](https://github.com/git/git)@[69bbbe484b...](https://github.com/git/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Monday 2023-01-23 23:16:45 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Demon-Jake/HeavenStudio](https://github.com/Demon-Jake/HeavenStudio)@[54c4899f9d...](https://github.com/Demon-Jake/HeavenStudio/commit/54c4899f9d31999a946e006c6c9b8235bdc1c778)
#### Monday 2023-01-23 23:17:58 by AstrlJelly

Double Date Initialization (#198)

* starting out with double date stuff :D

not even the background is finished
i just wanna get this on my fork so that it's safe

* double date getting more initialized

no animations, one block, nothing actually functions. but the boy is put in place, and the girl is almost put in place! just wanted to merge this with the main branch to play catchy tune

* initialization done!!!!!

gonna fix up the code, see what i can take out, see what i can standardize, see what i need to add. loving this so far, even with all of its annoyances

* ughhhh animation stuff.

this is gonna take me a day or two to even comprehend

Co-authored-by: minenice55 <star.elementa@gmail.com>

---

