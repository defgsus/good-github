## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-05](docs/good-messages/2023/2023-12-05.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 3,337,031 were push events containing 4,641,942 commit messages that amount to 311,629,247 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 85 messages:


## [Generalcamo/Aurora.3](https://github.com/Generalcamo/Aurora.3)@[13eb8af093...](https://github.com/Generalcamo/Aurora.3/commit/13eb8af093447e13b6555a741d6cd9e3a9dc3fbc)
#### Tuesday 2023-12-05 00:12:26 by RustingWithYou

air konyang ship (#17540)

it's a shuttle now, im gonna kms

smaller so it can fit

desperately cramming into shuttle guidelines

changelog & placeholder comments

chairs

name & mapping fixes

dme fix

carpet

new airlocks

entry points?

cries, shits

a

unit test group

fuck

ghuh

hguh

hate

fixes stupid problems

area flags

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[1e9edd6a49...](https://github.com/Monkestation/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Tuesday 2023-12-05 00:34:37 by Kittynoodle

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[349adbb438...](https://github.com/Rhials/tgstation/commit/349adbb438d5ca216b8f76c5251a1bf90473e0ce)
#### Tuesday 2023-12-05 00:35:38 by Ghom

[NO GBP] Fixing elevation furthermore (#80099)

## About The Pull Request
fixes #80059
fixes #80085.

The tram transportation doesn't use `forceMove()`, instead it just
changes the location of the objects directly. What's more, it doesn't
call `oldloc.Exited()` or `loc.Entered()` but only for areas. The
abstract exited/entered signals are from `Moved()` though, which is
called.

https://github.com/tgstation/tgstation/blob/df4bc6d948576a2ec32a90c23c93ec90e54e3933/code/modules/transport/transport_module.dm#L519-L527

About beds, well, I just happened to put a minus symbol where it
shouldn't be.

## Why It's Good For The Game
Truly one of the fuckups of the year. Now tested. I'll make a unit test
later.


## Changelog

:cl:
fix: Fixed some oopsie whoopsie with elevation, trams and beds causing
people to visually ascend or descend to heaven or hell.
/:cl:

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[223dc74ef1...](https://github.com/meemofcourse/Shiptest/commit/223dc74ef1f528e2c29b0e62271ddaf7b68d79d8)
#### Tuesday 2023-12-05 00:49:37 by retlaw34

Eoehoma Firearms (& friends) (#2315)

## About The Pull Request


![Screenshot_5451](https://github.com/shiptest-ss13/Shiptest/assets/58402542/08f9b0ee-15db-4091-a974-6d887cd85259)

Holy shit, this should not have taken a year to make

Adds the E-10, E-11, E-40, E-50, and E-60 to the game. Weapons
manufactured by defunct firearms company Eoehoma Firearms.

Founded in 77 FS, Eoehoma was a early pioneer of ‘hybrid’ Solarian and
Kalixcian laser weapons. The company went bankrupt due to increasingly
poor and risky decision making, and all of it's patents were bought out
by Nanotrasen. While Nanotrasen's Emitters bear a striking resemblance
to the E-50, otherwise Nanotrasen has not produced any of Eoehoma's old
weapons, instead focusing on Sharplite designed weapons.

Other changes:
- NT and Sharplite weapons have different fire sounds from each other
- Laser weapons buffed to 20 -> 25 damage
- Pulse shots don't destroy walls and are now 50 -> 40 damage
- Emitter shots now do 30 -> 60 damage
- Various grammar fixes
- Removes some non-lore compliant mentions
- Adds a manufacturer indicator to many guns
- Ports https://github.com/tgstation/tgstation/pull/60353
- Resprites various laser weaponry, notably the pulse guns.
- Deathsquad and ERT/LP hardsuits have been redone

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/c5df7029-95da-4041-b8b1-e4cfd35436dd)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/f72a3672-e996-4fdd-a68d-4553655f1a0c)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/7bd2dc53-ab29-49e8-8f90-87d4c72583f9)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/4bdc6493-4c94-49d0-995b-2a450d738211)
ceredits to tetrazeta for the unfinished deathsquad sprite, i simply
finished it and touched it up

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/517b72e3-c72b-4875-a6fb-84c017105908)

One of the last things i remember the old leads planned was to buff
lasers to make them stand up to the various ballistics better. Also
allows Pulse Rifles to be more used in events by nerfing them to not be
comedically overpowered. Now they are just Overpowered.

More ruin content and such. I'm sure the maptainers will make good use
of this stuff.

And sprites, i fucking love sprites

## Changelog

:cl: retlaw34, tetrazeta
add: Eoehoma Firearms, a new guns manufacturer!
add: ERT and "Asset Protection" Hardsuits have gotten a new look!
add: New laser fire sounds

balance: Lasers now do slightly more damage
balance: Pulse rifles don't destroy walls anymore and do slightly less
damage, and have lost their stun mode.
balance: Emitters do 60 damage and create turf fires on hitting a
non-supermatter object.
fix: Various laser weapons that had broken autofire (E-TAR and the Tesla
Cannon) now work

spellcheck: Grammar on some descriptions was corrected.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: retlaw34 <58402542+retlaw34@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[4d4aa72e33...](https://github.com/meemofcourse/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Tuesday 2023-12-05 00:49:37 by lizardqueenlexi

Removes "fat" status and everything related. (#2516)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

As the title says, eating too much no longer makes you "fat". You suffer
no slowdown or mood debuff from eating too much, and in general, the
game will not take every opportunity to make fun of you.

Notable removals/changes:
- The "fat sucker" machine is totally gone.
- Shady Slim's cigarettes have been removed (since they only existed to
interact with this mechanic).
- Lipoplasty surgery is gone.
- The nutrition setting of scanner gates is gone.

There are a couple of other removals too, like Gluttony's Wall, that I
think were already not in use on this codebase.

One thing I'm not completely satisfied with was the change to mint
toxin, which now does quite literally nothing. I don't think this is
especially a problem, it just makes its existence a bit vestigial.

Also includes an UpdatePaths script to delete all removed objects, just
in case.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/105025397/a1dd0981-94fc-4766-a34d-cce31a42b412)

Basically, removes some shitty "jokes" about fat people. It's an
extremely mean-spirited feature that serves no actual purpose, and
punishes you for clicking on a burger one time too many. It could
potentially be replaced later with a less mean-spirited "overeating"
mechanic, but I'm dubious as to whether that would be any fun either.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the "fat" status - overeating now has no negative effects.
del: Removed lipoplasty surgery.
del: Removed the fat sucker machine.
tweak: Scanner gates no longer have a "nutrition" option available.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Litberries/lobotomy-corp13](https://github.com/Litberries/lobotomy-corp13)@[aee88dbf1f...](https://github.com/Litberries/lobotomy-corp13/commit/aee88dbf1f49f56eb6db836939354aef09b70aae)
#### Tuesday 2023-12-05 01:01:06 by The Bron Jame Offical

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
## [Litberries/lobotomy-corp13](https://github.com/Litberries/lobotomy-corp13)@[2defb31817...](https://github.com/Litberries/lobotomy-corp13/commit/2defb31817005f7790e9586ace0c4e77c23d7f06)
#### Tuesday 2023-12-05 01:01:06 by vampirebat74

Adds Red Shoes (#901)

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes suit check in assimilate() proc

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes dismembering

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

breach is more dangerous

compiles

bug fix

fixes simple mob

bug fixes

Panic fixed!!!!

stuff

wayward records

Update code/modules/paperwork/records/info/he.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

attribute bonus

requested changes

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[07d551dac9...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/07d551dac9deb44f73b052ee591d8f78de4fff25)
#### Tuesday 2023-12-05 01:05:34 by distributivgesetz

Removes Clone Damage (#80109)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Does what it says on the tin. We don't have any "special" sources of
clone damage left in the game, most of them are rather trivial so I
bunched them together into this PR.

Notable things removed:
- Clonexadone, because its entire thing was centered around clone damage
- Decloner gun, it's also centered around cloning damage, I couldn't
think of a replacement mechanic and nobody uses it anyways
- Everything else already dealt clone damage as a side (rainbow knife
deals a random damage type for example), so these sources were removed

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Consider the four sources of normal damage that you can get: Brute,
Burn, Toxins and Oxygen. These four horsemen of the apocalypse are very
well put together and it's no surprise that they are in the game, as you
can fit any way of damaging a mob into them. Getting beaten to death by
a security officer? Brute damage. Running around on fire? Burn damage.
Poisoned or irradiated? Toxin damage. Suffocating in space? Brute, burn
and oxygen damage. Technically there's also stamina damage but that's
its own ballpark and it also makes sense why we have a damage number for
it.

Picture this now: We have this cool mechanic called "clone pods" where
you can magically revive dead people with absolute ease. We don't want
it to be for free though, it comes at a cost. This cost is clone damage,
and it serves to restrain people from abusing cloning.

Fast forward time a bit and cloning is now removed from the game. What
stays with us is a damage number that is intrinsically tied to the
context of a removed feature. It was a good idea that we had it for that
feature at the time, but now it just sits there. It's the odd one out
from all the other damage types. You can easily explain why your blade
dealt brute damage, but how are you going to fit clone damage into any
context without also becoming extremely specific?

My point is: **clone damage is conceptually a flawed mechanic because it
is too specific**. That is the major issue why no one uses it, and why
that makes it unworthy of being a damage stat.
Don't take my word for it though, because a while ago we only had a
handful of sources for this damage type in the game. And in most of the
rounds where you saw this damage, it came from only one department. It's
not worthwhile to keep it around as a damage number. People also didn't
know what to do with this damage type, so we currently have two ways of
healing clone damage: Cryotubes as a roundstart way of healing clone
damage and Rezadone, which instantly sets your clone damage to 0 on the
first tick. As a medical doctor, when was the last time you saw someone
come in with clone damage and thought to yourself, "Oh, this person has
clone damage, I cannot wait to heal them!" ?

Now we have replacements for these clone damage sources. Slimes? Slime
status effect that deals brute instead of clone. Cosmic heretics? Random
organ damage, because their mechanics are already pretty fleshed out.
Decloning virus? The virus operated as a "ticking timebomb" which used
cloning damage as the timer, so it has been reworked to not use clone
damage. What remains after all this is now a basically unused damage
type. Every specific situation that used clone damage is now relying on
another damage type. Now it's time to put clone damage to rest once and
for all.

Sure, you can technically add some form of cellular degradation in the
future, but it shouldn't be a damage number. The idea of your cells
being degraded is a cool concept, don't get me wrong, but make it a
status effect or maybe even a wound for that matter.

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
del: Removed clone damage.
del: Removed the decloner gun.
del: Removed clonexadone.
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Moribox/lobotomy-corp13](https://github.com/Moribox/lobotomy-corp13)@[07a5135fd3...](https://github.com/Moribox/lobotomy-corp13/commit/07a5135fd31c40f7928d39721fc3d7425e551682)
#### Tuesday 2023-12-05 01:24:01 by The Bron Jame Offical

Carbon Claw (#1646)

new content babey

i ahve made a severe lapse in my judgement and I do not expect to be forgiven. yadda yadda something reaping what i've sown something

Claw stuff

Claw sounds

CLAW ARMORRRRRRR

claw antag

please work

some of egors fixes

visual updates

new antag things

justice mod

fuckin, 1 god damn character change

Spans and rebase

more changes

what the hell

what the hell!!!!!

---
## [MoonTheBird/Shiptest](https://github.com/MoonTheBird/Shiptest)@[7c1f796bdf...](https://github.com/MoonTheBird/Shiptest/commit/7c1f796bdffe04cdc5b2d061a6220ebd402cab63)
#### Tuesday 2023-12-05 01:37:49 by Moon

gut the printing posters mechanic from the library computer

fuck you library

---
## [lintangtimur/overthrow3-source](https://github.com/lintangtimur/overthrow3-source)@[a2b715348b...](https://github.com/lintangtimur/overthrow3-source/commit/a2b715348b0056cc987e72357911b3f0002eab4e)
#### Tuesday 2023-12-05 01:56:27 by lintangtimur

2.2.2.0
ANCIENT APPARITION:
• Chilling Touch's attack range talent decreased from 300 --> 160
• Chilling Touch's cooldown & manacost upgrade increased from 8% --> 10%

BEASTMASTER:
• Wild Axes hit radius/path width upgrade increased from 30/20 --> 35/25
• Call of the Wild Boar/Hawk's cooldown & manacost upgrade increased from 8% --> 10%
• Call of the Wild Boar's base health/damage upgrade increased from 250/25 --> 300/30
• Inner Beast's radius upgrade increased from 200 --> 300 (max count decreased from 10 --> 6)
• Primal Roar's cooldown & manacost upgrade increased from 8% --> 10% (max count decreased from 14 --> 10)
• Primal Roar's shout width upgrade increased from 40 --> 60

BROODMOTHER:
• Insatiable Hunger's cooldown & manacost upgrade increased from 8% --> 9% (max count increased from 6 --> 7)
• Silken Bola's cooldown & manacost upgrade increased from 8% --> 12%
• Silken Bola's impact damage upgrade increased from 50 --> 70
• Spawn Spiderlings/Spinner's Snare's cooldown & manacost upgrade increased from 8% --> 10%
• Spawn Spiderlings' hp/hp buff upgrade increased from 250/50 --> 300/60
• Fixed Spawn Spiderlings' spiderling damage upgrade not working

EMBER SPIRIT:
• Searing Chain's cooldown & manacost upgrade increased from 8% --> 10%
• Searing Chain's radius upgrade increased from 40 --> 50
• Flame Guard's cooldown & manacost upgrade increased from 8% --> 12%
• Flame Guard's radius upgrade increased from 35 --> 40
• Fire Remnant's cooldown & manacost upgrade increased from 8% --> 10%
• Fire Remnant's radius upgrade increased from 40 --> 50

HOODWINK:
• Sharpshooter/Decoy's cooldown & manacost upgrade now has a max count of 20

JAKIRO:
• Dual Breath's cooldown & manacost upgrade increased from 10% --> 11%
• Dual Breath's start/end radius upgrade increased from 35/35 --> 40/40
• Ice Path's radius upgrade increased from 30 --> 35
• Liquid Fire/Frost's cooldown & manacost upgrade increased from 12% --> 15%
• Liquid Fire/Frost's radius upgrade increased from 45/45 --> 60/60

KUNKKA:
• Torrent/Torrent Storm's cooldown & manacost upgrade increased from 8% --> 10% (max count decreased from 10 --> 8)
• Tidebringer/Tidal Wave's cooldown & manacost upgrade increased from 8% --> 10%
• Tidebringer/Tidal Wave's cleave range/radius upgrade increased from 55/30 --> 75/60
• X Marks the Spot's cooldown & manacost upgrade increased from 8% --> 10%
• X Marks the Spot's enemy/allied delay upgrade increased from 0.6/1.2 --> 0.75/1.5 (max count from 5 --> 4)
• Ghostship's width/rum bonus speed upgrade increased from 30/3% --> 35/5%

MARCI:
• Dispose's cooldown & manacost upgrade increased from 12% --> 15%
• Dispose's impact damage upgrade increased from 140 --> 150
• Rebound's landing radius upgrade increased from 40 --> 45
• Rebound's damage upgrade increased from 100 --> 125

MEEPO:
• Earthbind's cooldown & manacost upgrade now has a max count of 10
• Earthbind/Dig's duration upgrade rescaled from 0.75/0.5 --> 0.6/0.6 in FFA (max count increased from 4 --> 5)

MIRANA:
• Starfall's cooldown & manacost upgrade increased from 8% --> 11%
• Sacred Arrow's Scepter search radius upgrade increased from 30 --> 35
• Sacred Arrow's cooldown & manacost upgrade increased from 8% --> 10%
• Sacred Arrow's distance for max stun/bonus damage upgrade increased from -300 --> -375 (max count decreased from 5 --> 4)
• Leap's initial/final cone radius upgrade increased from 80/80 --> 90/90
• Leap's movement bonus upgrade upgrade increased from 10% --> 15%

NAGA SIREN:
• Replaced Ensnare's duration upgrade with a +180 range upgrade for Reel In (linked to Reel In's pull speed upgrade)

NATURE'S PROPHET:
• Sprout/Curse of the Oldgrowth's cooldown & manacost upgrade increased from 8% --> 9%
• Sprout's damage upgrade increased from 8 --> 10
• Sprout/Curse of the Oldgrowth's damage radius/tree radius upgrade increased from 30/30 --> 35/35
• Nature's Call's cooldown & manacost upgrade increased from 8% --> 10% and no longer grants +10 treant duration (max count decreased from 10 --> 8)
• Nature's Call's treant damage upgrade increased from 45 --> 50 but no longer grants movespeed
• Nature's Call's treant health upgrade decreased from 700 --> 500 and now also grants +20 treant movespeed
• Fixed Nature's Call's +2 treants summoned talent incorrectly displaying as +5 treants summoned
• Wrath of Nature's cooldown & manacost upgrade increased from 8% --> 9%
• Wrath of Nature's damage upgrade increased from 60 --> 65
• Wrath of Nature's added damage per bounce upgrade increased from 3% --> 3.5%

QUEEN OF PAIN:
• Fixed Shadow Strike having a 2nd damage per tick upgrade instead of a damage interval upgrade
• Blink's Shard damage upgrade increased from 30 --> 40

SLARK:
• Dark Pact's radius upgrade increased from 50 --> 70
• Dark Pact's damage upgrade increased from 90 --> 100
• Pounce's leash duration upgrade increased from 0.5 --> 0.75 (max count decreased from 5 --> 3)
• Essence Shift now has an epic +1 agility gained upgrade

TROLL WARLORD:
• Battle Trance's cooldown & manacost upgrade's max count decreased from 20 --> 15
• Battle Trance's duration upgrade's max count decreased from 10 --> 5

UNDYING:
• Decay's cooldown & manacost upgrade increased from 8% --> 10%
• Soul Rip's cooldown & manacost upgrade increased from 8% --> 10%
• Soul Rip's damage per damage/heal per unit upgrade increased from 10 --> 12
• Soul Rip's max units/rip radius upgrade increased from 2/130 --> 4/260 (max count decreased from 10 --> 5)
• Flesh Golem's damage amplification upgrade increased from 4% --> 5%
• Flesh Golem's strength multiplier upgrade increased from 4% --> 5%

ZEUS:
• Thundergod's Wrath's cooldown & manacost upgrade now has a max count of 20

---
## [crawl/crawl](https://github.com/crawl/crawl)@[b247575874...](https://github.com/crawl/crawl/commit/b247575874e538bfb1af799ec40c5d5b44d00969)
#### Tuesday 2023-12-05 02:17:37 by regret-index

Frederick buffs and spell revisions

Frederick's current killratio, even for a lategame unique, is currently
very sad- over the past 16 months of recent versions it's a paltry 0.27%.
Spellforged Servitor is a cool gimmick, but with various player magic
overhauls it's meant a fair bit of special-casing for spells the player can
no longer cast, and the other conjurations are all relatively common spells
from a multitude of other lategame enemies currently available. An update
can help deal with all of these matters at once.

Frederick now loses Iron Bolt, Bolt of Cold, and Force Lance for the new
spells of Plasma Beam and Bombard, while keeping Spellforged Servitor
which can cast those both. We seem to be fine with these spells on player
ghosts, anyway, and it can introduce interesting complicated ally targetting
tactics as another distinct gimmick alongside the Servitor amplifying this.
Since Plasma Beam does extremely high damage in monster hands, he gets a bit
of an HD nerf. (It's more resistable than his prior spellset, at least.)
Since Bombard is knocking him away from melee more (and since phials of
floods / scrolls of silence neuter him a lot more than other uniques), he
gets a bit more health and a bit of a damage buff. Hopefully he should
catch up to all the surrounding power creep here for another 8 years.

(In converted saves his servitor won't do anything, but also, a single
unique having 1/4 spells not work is probably not worth the compat tag.
TODO: adjust another unique to use ice magic to compensate for this
contributing to uniques fire bias?...)

---
## [axelzonvolt/lizardsmashingkeyboard](https://github.com/axelzonvolt/lizardsmashingkeyboard)@[389d1e5669...](https://github.com/axelzonvolt/lizardsmashingkeyboard/commit/389d1e566990682f173066df4c16f25b3a1858c0)
#### Tuesday 2023-12-05 02:31:54 by Erika Fox

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
## [axelzonvolt/lizardsmashingkeyboard](https://github.com/axelzonvolt/lizardsmashingkeyboard)@[88e683cec6...](https://github.com/axelzonvolt/lizardsmashingkeyboard/commit/88e683cec669624228d5204d7e3da06e6075d158)
#### Tuesday 2023-12-05 02:31:54 by zevo

Massive Ruin Fixes + Removals PR (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR is made so I can stop getting angry at the ruins beyond saving
that are still ingame. My criteria for a ruin being removed is if
another ruin already does its niche better, if the ruin is outdated
and/or the ruin is excessively small or unbalanced. For ruins that dont
meet this criteria but are still outdated, they will be getting balance
fixes and touch ups or a total remap.

This PR is a draft for now because I will need to update the PR
changelog and description as I make changes and communicate with the
maptainers on what stays and what goes.

Adds departmental RND lootdrop spawners for circuit imprinters,
protolathes and techfabs. Excludes omnisci and basic boards from the
drops.
Fixed a space tile under a door and replaced the omnilathe with a
medical lathe on dangerousresearch
Fixed the whitesands saloon not spawning which may have caused some
sandplanets to spawn without a ruin
Fixed harmfactory's nonfunctional traps to now be as lethal as intended.
Also changed the loot in the vault to better reflect the ruin's theme
and difficulty (cargo techfab board instead of omnilathe, adv plasma
cutter instead of combat medkit, less gold more cash, kept the cyberarm
implant).
Fixed provinggrounds magical SMES FINALLY by adding a terminal on the
back. The map should finally function as intended.
Fixed a few dirs on fire extinguisher cabinets and blast door assemblies
in singularity_lab
Removed mechtransport.dmm for being small and bad
Removed some leftover gasthelizards.dmm cruft (VILE)
Removed nucleardump for being an utter mess of an oldcode ruin
Removed gondolaasteroid for being large and empty besides gondolas.
better suited for a jungle planet IMO.
Removed Jungle_Spider. Literally just a box with spiders and cloning
equipment. Small, bad, hard to find, unjustified loot.
Removed Golem_Hijack. Like jungle spider but it was free rnd, an AI
core, a full BSRPED and three golem corpses. With no enemies or
obstacles.
Removed rockplanet_clock for being a tiny lootbox that doesnt fit with
the lore. Also had a quantumn pad.
Removed whitesands_surface_youreinsane. Its a silly little reference to
an old event that unfortunately resulted in a subpar ruin. Could return
as a wasteplanet greeble ruin, but it has to go for now.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Normally I'm all for remapping instead of removing ruins, but some ruins
are very much beyond saving. Clearing out space for better ruins to take
the spotlight is always nice. Some older ruins are fine but are missing
certain things or have loot that worked fine in the past, but doesn't
reflect the balance we want for ruins in the present.

I will be PR'ing ruins to replace the ones I remove.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: departmental RND lootdrop spawners for imprinters, protolathes and
techfabs
fix: dangerous_research.dmm now no longer has a space tile under a door
and a medical lathe instead of an omnilathe
fix: whitesands_surface_camp_saloon can now spawn again after its remap
into a functional ruin
fix: harmfactory.dmm's traps now work and loot has been adjusted to fit
the ruin better
fix: provinggrounds.dmm now has a working SMES and power
fix: singularity_lab fire extinguishers and a few poddoors now have
correct dirs
del: mechtransport.dmm and associated code
del: gasthelizards areas
del: nucleardump.dmm and associated code
del: gondolaasteroid.dmm and associated code
del: jungle_spider.dmm and associated code
del: whitesands_golem_hijack.dmm and associated code
del: rockplanet_clock.dmm and associated code
del: whitesands_surface_youreinsane.dmm and associated code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: zevo <95449138+Zevotech@users.noreply.github.com>

---
## [fyl080801/TavernAI](https://github.com/fyl080801/TavernAI)@[d3a4f43fbb...](https://github.com/fyl080801/TavernAI/commit/d3a4f43fbba708267059c19d10605e6b080d2f92)
#### Tuesday 2023-12-05 02:33:52 by FunkEngine

"Just closing the barn door a bit..."

(This first section is the TL;DR. with regards to the Sharp/WEBP vulns etc.) Closing the wide-open barn door here... Common sense applied etc. PNG is once again the default storage and export format for cards. While currently the 'Tavern_Card_V2' spec is not yet fully implemented (Or even nailed down, let be honest here.) but that is a thing in the works... At least we're back to the 'Tavern_Card_V1' spec again, now.

Nudging Sharp min required version up to 0.32.6, as 0.31.3 is a confirmed vulnerable version, and installs by default unless the user manually forces an audit, at which point (now, in the last few days.) some people will be unable to run tavern, due to major breaking changes in 0.33...
I chose specifically not to bump to 0.33.0 (which came out the other day) due to said major breaking changes, what with a sizable majority of our users (Or at least based on the reported user-agents that land on our GitHub page!) are running older systems. (I include myself in this group, although there are allegedly some using frighteningly deprecated systems than I am!)

0.32.6 is... For the moment at least, secure and compatible with the widest possible cross-section of our current and potential users.

While I sort of already had my sleeves rolled up and the long gloves on... I also noticed our own internal versioning was desynchronized at some point, and nudged the values in package/package-lock .jsons to match 1.5.2 which is our present official version.
((Honestly Humi, I'm almost tempted to say this push/commit should effectively be a '1.5.3' roll-up at this point, or similar update-alert triggering release should be planned for a 2023 End-of-the-Year roll-up in ~4 weeks time. To land us at 1.5.3, if not start us at straight up 1.6.0 at the changeover from 2023 to 2024.  Something to think about.))

Adjusted the "default defaults" (settings) to better reflect the contemporary median capabilities of the models in popular use. (context max etc.) To give a better first-impression on newer users. Also trying to get the string literal 'Pygmalion' out of as much as possible to prevent our colab from being flagged. As I find such minor references I either redact them, deprecate them,  or modify them. (Delete whole-cloth, make the Pygmalion one into the non-default option, and change to 'Pyg' or 'Classic-6B' etc, respectively. In this push I redacted both a single code comment with the string in it, and have set the name of the default preset used back to the Default-TavernAI settings from Classic-Pygmalion-6b which the settings.json file had set, and updated the actual settings values inside of both so that even people who switch back to the pyg-classic 'preset' out of force of habit will benefit from modern models and inference APIs, while officially 'deprecating' the named Pygmalion settings.)

In that same vein, or similar at least I have slightly changed the message printed to console by default during auto-launching, such that it no longer inadvertently confuses people by creating a clickable link to an inaccessible location when used as part of the colab notebook(s). It only appears when auto-run is enabled, so if you're running locally you're not clicking the 127.0.0.1 link in the first place... But it confuses so many people when colab prints it as a clickable URL in the output console. One less thing to confuse users.

This is both a QoL and newbie-onboarding change-decision, and will be slightly more relevant in a followup commit that further enhances, refines, and streamlines the TavernAI colab user experience that's in the oven at the moment. (Slightly over half-baked as I type this up, and it is starting to smell good.)  Look for that possibly as soon as Monday.

Still trying my best to end 2023 on a high note here for us all, folks. :)
--FunkEngine

(Also) Just about made a fool of myself this morning...
https://github.com/FunkEngine2023/FunkEngine2023.github.io/assets/123712145/5324b650-9e0e-42ee-b6ba-635a3ecfd37c

And hey look I've been baking this commit for over 36 hours now, that was yesterday morning!

Fixed issues with start.bat. Added proper *#%(*% shortcut to open a PowerShell window already set and in the relevant CWD so that there's literally no excuse anymore to not put their hands on the wheel for once...

Then I fixed the bat even more better-er... Fully deprecated the string literal 'Pygmalion" from the code... I don't live in fear of Google... I just don't want to give them any plausible justification to throw us under the bus... (I mean they continue adding "Verboten!" code to the signatures dictionary... SDWUI and ComfyUI being the more notable ones since Pyg took one for the team, and became the lesson for us all in the process.

Round about that time I had also finished fixing up the readme.md with a bit more detail about the process, and adding icons for the downloads...

Then I went down a brief rabbit-hole and literally got a one touch solution as far as "making the TavernAI go *brrrrrrrrrr*" goes...  Plus I left all the prior solutions there in place, and in better condition than they possibly have ever been.  Not sure if I want to go back and mangle markdown to update the readme before I finally push this long overdue boat of a commit down the slipway...

The short answer is: To run TavernAI there's a shortcut right there in the directory, called "TAVERN_CONSOLE" and you just double click it and it takes care of the whole bpm install and standing node up with server.js...  In actual proper PowerShell!

Finishing up testing on several various test environments to make sure that the .bat, the TAVERN_CONSOLE shortcut, and the "CONSOLE" shortcut all function port-ably as  I intend them to. (The "CONSOLE" just opens a PowerShell window in the CWD of wherever the shortcut is to launch it. This will enable things like manually `npm audit fix --force` for those who wouldn't have the slightest idea how to open a PowerShell otherwise.

Big QoL roll-up here. I'll leave merging the colab changes in for Monday or Tuesday.

And now here I am just after midnight pushing this on MONDAY MORNING. :3

-- 0200 approaches and I'm still not satisfied with the colab... It is still less broken than it previously was. I'll leave that for another day.  Happy Monday Morning to you all!

--FunkEngine. (Josh S.)

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[1a9043d797...](https://github.com/Ical92/tgstation/commit/1a9043d797325fe09cdb4e42d42f5d922c151ed9)
#### Tuesday 2023-12-05 02:39:27 by necromanceranne

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
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[91af16bcbf...](https://github.com/Ical92/tgstation/commit/91af16bcbfd2dd363a89d846ae2acd6d655083c2)
#### Tuesday 2023-12-05 02:39:27 by zxaber

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
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[a1e46c5d31...](https://github.com/Ical92/tgstation/commit/a1e46c5d31347887de95520eee31c00749379b9c)
#### Tuesday 2023-12-05 02:41:00 by Jacquerel

Basic Guardians/Holoparasites (#79473)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[100ede82bd...](https://github.com/RaShCat/FF-STG/commit/100ede82bd27e39fc8844464aeb2be82822862f5)
#### Tuesday 2023-12-05 04:37:41 by Iajret Creature

[MIRROR] Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun [MDB IGNORE] (#25365) (#908)

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun

---------

Co-authored-by: SkyratBot <59378654+SkyratBot@users.noreply.github.com>
Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [digisfresh1/Article](https://github.com/digisfresh1/Article)@[719a3a9452...](https://github.com/digisfresh1/Article/commit/719a3a94522511727a72ff2ad53a96b2707d4ecb)
#### Tuesday 2023-12-05 04:47:59 by digisfresh1

Create What Happens to Your Body If You Eat Eggs Everyday?

Most of us will answer – egg. They are loaded with so much nutrient, easy to prepare, available anywhere, and can be used in breakfast, lunch or dinner irrespective of meal time.

---
## [mattbruv/advent-of-code](https://github.com/mattbruv/advent-of-code)@[1500c97de4...](https://github.com/mattbruv/advent-of-code/commit/1500c97de4c51d445b2761fdac5ddf98aef5ce8d)
#### Tuesday 2023-12-05 05:11:37 by Matt P

finially finish part stupid fucking 1 of day 3, literally went insane

---
## [zoegrace20/MyMiniProjects](https://github.com/zoegrace20/MyMiniProjects)@[3b94503a76...](https://github.com/zoegrace20/MyMiniProjects/commit/3b94503a76cad8415e57cf7fc58a5fb444397c2f)
#### Tuesday 2023-12-05 05:34:15 by zoegrace20

Sigma Gamma Rho Website

I started on this website just to practice my website building skills. I have a friend who is apart of this sorority and she didn't totally love their website. That gave me some inspiration and motivation.

---
## [ivaxer/neon](https://github.com/ivaxer/neon)@[c7f1143e57...](https://github.com/ivaxer/neon/commit/c7f1143e570924eadd15053949647707ba042c5b)
#### Tuesday 2023-12-05 06:33:16 by Christian Schwarz

concurrency-limit low-priority initial logical size calculation [v2] (#6000)

Problem
-------

Before this PR, there was no concurrency limit on initial logical size
computations.

While logical size computations are lazy in theory, in practice
(production), they happen in a short timeframe after restart.

This means that on a PS with 20k tenants, we'd have up to 20k concurrent
initial logical size calculation requests.

This is self-inflicted needless overload.

This hasn't been a problem so far because the `.await` points on the
logical size calculation path never return `Pending`, hence we have a
natural concurrency limit of the number of executor threads.
But, as soon as we return `Pending` somewhere in the logical size
calculation path, other concurrent tasks get scheduled by tokio.
If these other tasks are also logical size calculations, they eventually
pound on the same bottleneck.

For example, in #5479, we want to switch the VirtualFile descriptor
cache to a `tokio::sync::RwLock`, which makes us return `Pending`, and
without measures like this patch, after PS restart, VirtualFile
descriptor cache thrashes heavily for 2 hours until all the logical size
calculations have been computed and the degree of concurrency /
concurrent VirtualFile operations is down to regular levels.
See the *Experiment* section below for details.

<!-- Experiments (see below) show that plain #5479 causes heavy
thrashing of the VirtualFile descriptor cache.
The high degree of concurrency is too much for 
In the case of #5479 the VirtualFile descriptor cache size starts
thrashing heavily.


-->

Background
----------

Before this PR, initial logical size calculation was spawned lazily on
first call to `Timeline::get_current_logical_size()`.

In practice (prod), the lazy calculation is triggered by
`WalReceiverConnectionHandler` if the timeline is active according to
storage broker, or by the first iteration of consumption metrics worker
after restart (`MetricsCollection`).

The spawns by walreceiver are high-priority because logical size is
needed by Safekeepers (via walreceiver `PageserverFeedback`) to enforce
the project logical size limit.
The spawns by metrics collection are not on the user-critical path and
hence low-priority. [^consumption_metrics_slo]

[^consumption_metrics_slo]: We can't delay metrics collection
indefintely because there are TBD internal SLOs tied to metrics
collection happening in a timeline manner
(https://github.com/neondatabase/cloud/issues/7408). But let's ignore
that in this issue.

The ratio of walreceiver-initiated spawns vs
consumption-metrics-initiated spawns can be reconstructed from logs
(`spawning logical size computation from context of task kind {:?}"`).
PR #5995 and #6018 adds metrics for this.

First investigation of the ratio lead to the discovery that walreceiver
spawns 75% of init logical size computations.
That's because of two bugs:
- In Safekeepers: https://github.com/neondatabase/neon/issues/5993
- In interaction between Pageservers and Safekeepers:
https://github.com/neondatabase/neon/issues/5962

The safekeeper bug is likely primarily responsible but we don't have the
data yet. The metrics will hopefully provide some insights.

When assessing production-readiness of this PR, please assume that
neither of these bugs are fixed yet.


Changes In This PR
------------------

With this PR, initial logical size calculation is reworked as follows:

First, all initial logical size calculation task_mgr tasks are started
early, as part of timeline activation, and run a retry loop with long
back-off until success. This removes the lazy computation; it was
needless complexity because in practice, we compute all logical sizes
anyways, because consumption metrics collects it.

Second, within the initial logical size calculation task, each attempt
queues behind the background loop concurrency limiter semaphore. This
fixes the performance issue that we pointed out in the "Problem" section
earlier.

Third, there is a twist to queuing behind the background loop
concurrency limiter semaphore. Logical size is needed by Safekeepers
(via walreceiver `PageserverFeedback`) to enforce the project logical
size limit. However, we currently do open walreceiver connections even
before we have an exact logical size. That's bad, and I'll build on top
of this PR to fix that
(https://github.com/neondatabase/neon/issues/5963). But, for the
purposes of this PR, we don't want to introduce a regression, i.e., we
don't want to provide an exact value later than before this PR. The
solution is to introduce a priority-boosting mechanism
(`GetLogicalSizePriority`), allowing callers of
`Timeline::get_current_logical_size` to specify how urgently they need
an exact value. The effect of specifying high urgency is that the
initial logical size calculation task for the timeline will skip the
concurrency limiting semaphore. This should yield effectively the same
behavior as we had before this PR with lazy spawning.

Last, the priority-boosting mechanism obsoletes the `init_order`'s grace
period for initial logical size calculations. It's a separate commit to
reduce the churn during review. We can drop that commit if people think
it's too much churn, and commit it later once we know this PR here
worked as intended.

Experiment With #5479 
---------------------

I validated this PR combined with #5479 to assess whether we're making
forward progress towards asyncification.

The setup is an `i3en.3xlarge` instance with 20k tenants, each with one
timeline that has 9 layers.
All tenants are inactive, i.e., not known to SKs nor storage broker.
This means all initial logical size calculations are spawned by
consumption metrics `MetricsCollection` task kind.
The consumption metrics worker starts requesting logical sizes at low
priority immediately after restart. This is achieved by deleting the
consumption metrics cache file on disk before starting
PS.[^consumption_metrics_cache_file]

[^consumption_metrics_cache_file] Consumption metrics worker persists
its interval across restarts to achieve persistent reporting intervals
across PS restarts; delete the state file on disk to get predictable
(and I believe worst-case in terms of concurrency during PS restart)
behavior.

Before this patch, all of these timelines would all do their initial
logical size calculation in parallel, leading to extreme thrashing in
page cache and virtual file cache.

With this patch, the virtual file cache thrashing is reduced
significantly (from 80k `open`-system-calls/second to ~500
`open`-system-calls/second during loading).


### Critique

The obvious critique with above experiment is that there's no skipping
of the semaphore, i.e., the priority-boosting aspect of this PR is not
exercised.

If even just 1% of our 20k tenants in the setup were active in
SK/storage_broker, then 200 logical size calculations would skip the
limiting semaphore immediately after restart and run concurrently.

Further critique: given the two bugs wrt timeline inactive vs active
state that were mentioned in the Background section, we could have 75%
of our 20k tenants being (falsely) active on restart.

So... (next section)

This Doesn't Make Us Ready For Async VirtualFile
------------------------------------------------

This PR is a step towards asynchronous `VirtualFile`, aka, #5479 or even
#4744.

But it doesn't yet enable us to ship #5479.

The reason is that this PR doesn't limit the amount of high-priority
logical size computations.
If there are many high-priority logical size calculations requested,
we'll fall over like we did if #5479 is applied without this PR.
And currently, at very least due to the bugs mentioned in the Background
section, we run thousands of high-priority logical size calculations on
PS startup in prod.

So, at a minimum, we need to fix these bugs.

Then we can ship #5479 and #4744, and things will likely be fine under
normal operation.

But in high-traffic situations, overload problems will still be more
likely to happen, e.g., VirtualFile cache descriptor thrashing.
The solution candidates for that are orthogonal to this PR though:
* global concurrency limiting
* per-tenant rate limiting => #5899
* load shedding
* scaling bottleneck resources (fd cache size (neondatabase/cloud#8351),
page cache size(neondatabase/cloud#8351), spread load across more PSes,
etc)

Conclusion
----------

Even with the remarks from in the previous section, we should merge this
PR because:
1. it's an improvement over the status quo (esp. if the aforementioned
bugs wrt timeline active / inactive are fixed)
2. it prepares the way for
https://github.com/neondatabase/neon/pull/6010
3. it gets us close to shipping #5479 and #4744

---
## [lzw29107/terminal](https://github.com/lzw29107/terminal)@[86fb9b4478...](https://github.com/lzw29107/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Tuesday 2023-12-05 06:46:51 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [newren/git](https://github.com/newren/git)@[f9d641f32d...](https://github.com/newren/git/commit/f9d641f32ddfbf5c580e0ca4d5981cb1f3002f8d)
#### Tuesday 2023-12-05 07:01:03 by Elijah Newren

completion: avoid user confusion in non-cone mode

It is tempting to think of "files and directories" of the current
directory as valid inputs to the add and set subcommands of git
sparse-checkout.  However, in non-cone mode, they often aren't and using
them as potential completions leads to *many* forms of confusion:

Issue #1. It provides the *wrong* files and directories.

For
    git sparse-checkout add
we always want to add files and directories not currently in our sparse
checkout, which means we want file and directories not currently present
in the current working tree.  Providing the files and directories
currently present is thus always wrong.

For
    git sparse-checkout set
we have a similar problem except in the subset of cases where we are
trying to narrow our checkout to a strict subset of what we already
have.  That is not a very common scenario, especially since it often
does not even happen to be true for the first use of the command; for
years we required users to create a sparse-checkout via
    git sparse-checkout init
    git sparse-checkout set <args...>
(or use a clone option that did the init step for you at clone time).
The init command creates a minimal sparse-checkout with just the
top-level directory present, meaning the set command has to be used to
expand the checkout.  Thus, only in a special and perhaps unusual cases
would any of the suggestions from normal file and directory completion
be appropriate.

Issue #2: Suggesting patterns that lead to warnings is unfriendly.

If the user specifies any regular file and omits the leading '/', then
the sparse-checkout command will warn the user that their command is
problematic and suggest they use a leading slash instead.

Issue #3: Completion gets confused by leading '/', and provides wrong paths.

Users often want to anchor their patterns to the toplevel of the
repository, especially when listing individual files.  There are a
number of reasons for this, but notably even sparse-checkout encourages
them to do so (as noted above).  However, if users do so (via adding a
leading '/' to their pattern), then bash completion will interpret the
leading slash not as a request for a path at the toplevel of the
repository, but as a request for a path at the root of the filesytem.
That means at best that completion cannot help with such paths, and if
it does find any completions, they are almost guaranteed to be wrong.

Issue #4: Suggesting invalid patterns from subdirectories is unfriendly.

There is no per-directory equivalent to .gitignore with
sparse-checkouts.  There is only a single worktree-global
$GIT_DIR/info/sparse-checkout file.  As such, paths to files must be
specified relative to the toplevel of a repository.  Providing
suggestions of paths that are relative to the current working directory,
as bash completion defaults to, is wrong when the current working
directory is not the worktree toplevel directory.

Issue #5: Paths with special characters will be interpreted incorrectly

The entries in the sparse-checkout file are patterns, not paths.  While
most paths also qualify as patterns (though even in such cases it would
be better for users to not use them directly but prefix them with a
leading '/'), there are a variety of special characters that would need
special escaping beyond the normal shell escaping: '*', '?', '\', '[',
']', and any leading '#' or '!'.  If completion suggests any such paths,
users will likely expect them to be treated as an exact path rather than
as a pattern that might match some number of files other than 1.

However, despite the first four issues, we can note that _if_ users are
using tab completion, then they are probably trying to specify a path in
the index.  As such, we transform their argument into a top-level-rooted
pattern that matches such a file.  For example, if they type:
   git sparse-checkout add Make<TAB>
we could "complete" to
   git sparse-checkout add /Makefile
or, if they ran from the Documentation/technical/ subdirectory:
   git sparse-checkout add m<TAB>
we could "complete" it to:
   git sparse-checkout add /Documentation/technical/multi-pack-index.txt
Note in both cases I use "complete" in quotes, because we actually add
characters both before and after the argument in question, so we are
kind of abusing "bash completions" to be "bash completions AND
beginnings".

The fifth issue is a bit stickier, especially when you consider that we
not only need to deal with escaping issues because of special meanings
of patterns in sparse-checkout & gitignore files, but also that we need
to consider escaping issues due to ls-files needing to sometimes quote
or escape characters, and because the shell needs to escape some
characters.  The multiple interacting forms of escaping could get ugly;
this patch makes no attempt to do so and simply documents that we
decided to not deal with those corner cases for now but at least get the
common cases right.

Signed-off-by: Elijah Newren <newren@gmail.com>

---
## [Manitec/crawl](https://github.com/Manitec/crawl)@[bca3d03946...](https://github.com/Manitec/crawl/commit/bca3d03946f17baf04eab8d0adc0c556bd83d797)
#### Tuesday 2023-12-05 07:04:49 by regret-index

Even more widespread vault review

Of note:

 * _lair_caniforms_friends gets a hell hog because it's also an elemental
   mammalian quadruped as fills the vault already and also because it's
   been struggling at the bottom of the lair kills list.

 * Lair endings with dragons have been each been tweaked. The swampy one
   gets a chance for an ice dragon over a fire dragon, the minivolcano has
   a 1/3 chance for two hell hogs, and the wurm / snail cave has been
   warped to place the dragon room in a plant corridor at a random end of
   the vault rather than with a runed door right at the start. (If we're
   already putting dragon bosses without runed doors in one end, we really
   don't need runed doors in front of the other dragons; it dilutes the
   warning capacity of runed doors to just shepard autoexplore. The
   minivolcano should be stabbed at in this regard, but that's harder to
   adjust...)

 * The Hall of Blades blade talisman has an explicit small chance to be
   a randart now, to make it less sad for later Elf visits and to continue
   to try to get people to open the vault up.

 * orc_legates has been taken out of the Elf:1 guaranteed minivault pool
   for being much more dangerous and dense than the others in that slot.
   Three minivaults made much later than the original set setting have
   been added to the tag to compensate.

 * Several iron golems escaping Dis to find the protection of Chei altars
   in Depths have been damned back to hell, with iron dragons watching
   over those altars to keep them from coming back.

 * Moved amcnicky_altar_lugonu_corruption and its out-of-Abyss lurking
   horrors from most of its main-game placement (outside of the themeless
   D and Depths) for extended placement instead. There's many excuses
   one can make for monsters from elsewhere invading a branch, and that
   doesn't really inherently justify diluting the entire game with
   monsters that'll mostly just force one to rest rather than kill.
   Lurking horrors in particular will be felt more in the Hells and Pan
   anyway.

 * Remaining teleport / flight islands in Cocytus:$ and Gehenna:$ have
   been covered with more liquids and no_tele_into, which should close
   Mantis #12466.

---
## [meow56/advent-of-code-2023](https://github.com/meow56/advent-of-code-2023)@[9f6310909c...](https://github.com/meow56/advent-of-code-2023/commit/9f6310909cb034ffd02985459e96236a5aaf049a)
#### Tuesday 2023-12-05 07:12:09 by meow56

Day 5-2

I love stupidly long if statements that meticulously work through every case. This is definitely the most efficient way to write code.

Also I was kinda expecting to fall into recursion hell, but it didn't really happen. Where are my performance issues...?

---
## [badarineo/OpenBSD](https://github.com/badarineo/OpenBSD)@[77e08d39e0...](https://github.com/badarineo/OpenBSD/commit/77e08d39e088d4e49062fab366289c5ea8b27f00)
#### Tuesday 2023-12-05 07:16:30 by tb

Fix EVP_CIPHER_CTX_iv_length()

In today's episode of "curly nonsense from EVP land" we deal with a quite
harmless oversight and a not too bad suboptimal fix, relatively speaking.

At some point EVP_CIPHER_{CCM,GCM}_SET_IVLEN was added. It modified some
object hanging off of EVP_CIPHER. However, EVP_CIPHER_CTX_iv_length() wasn't
taught about this and kept returning the hardcoded default value on the
EVP_CIPHER. Once it transpired that a doc fix isn't going to cut it, this
was fixed. And of course it's easy to fix: you only have to dive through
about three layers of EVP, test and set a flag and handle a control in a
couple methods.

The upstream fix was done poorly and we begrudgingly have to match the API:
the caller is expected to pass a raw pointer next to a 0 length along with
EVP_CIPHER_GET_IV_LENGTH and the control handler goes *(int *)ptr = length
in full YOLO mode. That's never going to be an issue because of course the
caller will always pass a properly aligned pointer backing a sufficient
amount of memory. Yes, unlikely to be a real issue, but it could have been
done with proper semantics and checks without complicating the code. But
why do I even bother to complain? We're used to this.

Of note here is that there was some pushback painting other corners of a
bikeshed until the reviewer gave up with a resigned

  That kind of changes the semantics and is one extra complexity level,
  but [shrug] ok...

Anyway, the reason this matters now after so many years is that rust-openssl
has an assert, notably added in a +758 -84 commit with the awesome message
"Docs" that gets triggered by recent tests added to py-cryptography.

Thanks to Alex Gaynor for reporting this. Let me take the opportunity to
point out that pyca contributed to improve rust-openssl, in particular its
libressl support, quite a bit. That's much appreciated and very noticeable.

Regress coverage to follow in subsequent commits.

Based on OpenSSL PR #9499 and issue #8330.

ok beck jsing

PS: A few macros were kept internal for now to avoid impact on the release
cycle that is about to finish. They will be exposed after release.

---
## [CodeCuriousMind/zero-hero-data-science](https://github.com/CodeCuriousMind/zero-hero-data-science)@[1e39036c35...](https://github.com/CodeCuriousMind/zero-hero-data-science/commit/1e39036c3569c73d31f0dd20ab52d394237586e3)
#### Tuesday 2023-12-05 07:39:36 by Björn

Add files via upload

Zero-Hero DataScience Toolkit," a comprehensive and meticulously curated collection of Python snippets and tools designed to take you from a beginner to a proficient data scientist. This toolkit is not just a collection of code; it's a gateway to mastering the art and science of data analysis, visualization, and machine learning.<br>

In the ever-evolving field of data science, the journey from zero to hero is both exciting and challenging. <br>
Whether you're starting to explore the basics of data handling or diving into the depths of complex machine learning algorithms,<br>
this toolkit serves as your reliable companion, offering you the necessary tools and insights every step of the way.<br>

## Project Description
The "Zero-Hero DataScience Toolkit" is crafted with the aim to simplify and streamline the process of learning and applying data science concepts. The toolkit encapsulates various facets of data science, from preliminary data handling to sophisticated data analysis techniques.

### What's Inside the Toolkit?
Data Handling and Preparation: Essential Python snippets for loading and preparing data, making the initial steps in data science smooth and straightforward.<br>

Tools and techniques to explore and understand your dataset, including handling missing values and duplicates, which are crucial for accurate analysis. <br>

### Data Manipulation:
A collection of snippets to manipulate datasets, including sorting, grouping, and pivot tables, empowering you to shape data according to analytical needs.

### Data Visualization: 
Visual tools to bring data to life, making complex insights easier to understand and communicate.

### Machine Learning: 
Introductory snippets for machine learning applications, guiding you through the basics of model creation, training, and evaluation.

## Who Is This Toolkit For?
<br>

#### Data Science Beginners:
If you're taking your first steps in data science, this toolkit provides the foundational blocks to build your skills.<br>

#### Intermediate Learners:
For those who have some experience but want to deepen their understanding and broaden their skillset in data science.<br>

#### Aspiring Data Heroes:
Individuals aiming to excel and become proficient in the field of data science.

---
## [LTVA1/YM2609](https://github.com/LTVA1/YM2609)@[0fc039771a...](https://github.com/LTVA1/YM2609/commit/0fc039771ad90e4efe231c2407c285c7660a3c18)
#### Tuesday 2023-12-05 08:34:48 by LTVA1

goddamn functions array fucking shit! Commit as is, it doesn't compile...

---
## [Megunight/dsci100-project](https://github.com/Megunight/dsci100-project)@[1960563146...](https://github.com/Megunight/dsci100-project/commit/1960563146aa02cdf431cb7f4e1818cbf92c729d)
#### Tuesday 2023-12-05 08:39:42 by Andrew

Added Text, Cleaned up data.

Added text and described graphs and method. Also had to do another initial split for a subgroup so our earlier code was missing a step. The only thing I'm unsure about is the results visualization at the end. I think it is okay but I need to get it verified with a friend by tomorrow (Dec 5 as of now). We are just missing the discussion and conclusion section. I want to further elaborate on the confusion matrix and results visualization. Please feel free to make edits and extra explanations. Let me know in Instagram if you make any changes please and thank you!

---
## [PastelPrinceDan/Skyrat-tg](https://github.com/PastelPrinceDan/Skyrat-tg)@[8d69a6b49d...](https://github.com/PastelPrinceDan/Skyrat-tg/commit/8d69a6b49df26a323e0a32f7a51ff7033fa5fd5a)
#### Tuesday 2023-12-05 08:48:16 by SkyratBot

[MIRROR] Codifies male goats not having an udder [MDB IGNORE] (#25030)

* Codifies male goats not having an udder (#79722)

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

Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

* Codifies male goats not having an udder

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

---
## [ezr-ondrej/images](https://github.com/ezr-ondrej/images)@[7152886364...](https://github.com/ezr-ondrej/images/commit/715288636474b85551fdf53478754d931c6fafa8)
#### Tuesday 2023-12-05 09:41:06 by Tomáš Hozza

distro/el9: refactor package sets to again use `@core` pkg group

Previously, we used a fixed package list from RHEL-9.0 times, instead of
the `@core` pkg group, for all images which used it on el8. The
motivation was that some packages got removed from the group in 9.0
(specifically tuned), which went almost unnoticed. The reasoning was that
a fixed list would give us more control over the package set and prevent
unexpected package removals.

However, with COMPOSER-2074 [1], it turned out that this also meant that
any new packages added to the `@core` group won't be automatically added
to any image which previously used the `@core` group. People still have
(anyhow incorrect) expectation that `@core` pkg group is always
installed on RHEL images and thus that adding a package to the group
will also add it to vanilla RHEL images.

We discussed this shortly within the team and reverting back to using
`@core` package group, instead of a fixed package list, seems like the
lesser evil.

Modify package set definitions, which used `coreOsCommonPackageSet()` to
use `@core` package group instead. Modify the exclude lists accordingly
to achieve almost the same image content as before. There are a few
exceptions:

 - `rhc` package is now installed, which is desired.
 - `insights-client` is now installed on some images where it was
   previously not. This is OK, since RHEL is aiming for a "connected
   experience" by default. This also results in a few additional
   packages to be pulled in as dependencies, specifically:
   - `python3-file-magic`
   - `policycoreutils-python-utils`
   - `tar`
   - `pciutils`
 - `initscripts-rename-device` is now installed. This sub-package has
   been split out of the `initscripts` package on el9, but it was not
   included in the `@core` group definition, when we created the fixed
   pkg list. However, it is now the default member of the group. The
   functionality was previously installed by default on el8 images via
   the `initscripts` package. After talking to the maintainer, I kept it
   in the images as a new package.

Affected images by this change:
 - ami
 - gce
 - gce_rhui
 - image_installer
 - oci
 - openstack
 - ova
 - qcow2
 - vmdk

Some of the listed images already contained `rhc` or `insights-client`,
but now, these are consistently installed on all of them. This is the
case since 9.2, when `rhc` was added to the `@core` group.

`initscripts-rename-device` has been added to all of these image types,
inlcuding on CentOS Stream 9 images.

[1] https://issues.redhat.com/browse/COMPOSER-2074

Signed-off-by: Tomáš Hozza <thozza@redhat.com>

---
## [burdwatcher/Skyrat-tg](https://github.com/burdwatcher/Skyrat-tg)@[94603a2a96...](https://github.com/burdwatcher/Skyrat-tg/commit/94603a2a9636ab5a9e8ded9247b490a5d6670da4)
#### Tuesday 2023-12-05 09:42:07 by SkyratBot

[MIRROR] Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) [MDB IGNORE] (#25102)

* Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much.

## Changelog

:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP)

---------

Co-authored-by: KingkumaArt <69398298+KingkumaArt@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[7076eac80e...](https://github.com/Offroaders123/Smart-Text-Editor/commit/7076eac80ecae0be9af24305f9cbcd48ef2eec27)
#### Tuesday 2023-12-05 09:42:32 by Offroaders123

Omnibox Button Scaling Removal

This didn't work on Retina displays, and I don't know how to account for those, since you can't reliably determine what the browser's initial zoom level is when the page starts. If we knew that, then we could deduce what the current one is, and account for that, but this isn't something heavy enough I want to account for, since it's such a small feature.

This removal simply means my custom Omnibox buttons will now scale up and down when zooming in and out of the page. This is not as usable in terms of the app's appearance when installed, with WCO enabled, but I also don't want to make it extra hacky just to support it. If there is a way to manage this consistently, without too much work, then I would like to try it out. But I'm not sure how zooming should work with WCO in general, I don't think that's something the API completely manages too well, I don't know how it *should* be managed either, since it's just part of the rendering for HTML in that area anyways.

I think I will rework the header a little bit more anyways, so this is another feature that I'm removing, to allow for easily moving on to something else if needed anyways. This was one of those polish kind of features anyways, to complete the header's look and make it consistently responsive.

Just bought Wooden Smoke tonight, been meaning to properly get it for the last few months now :)

---
## [cyyever/pytorch](https://github.com/cyyever/pytorch)@[ddf1cb7870...](https://github.com/cyyever/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Tuesday 2023-12-05 10:04:52 by voznesenskym

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
ghstack dependencies: #113926

---
## [sherinalexander/hello-world](https://github.com/sherinalexander/hello-world)@[89d419ab3c...](https://github.com/sherinalexander/hello-world/commit/89d419ab3c33ca4a5eda200555a685b60057c748)
#### Tuesday 2023-12-05 10:46:54 by Sherin S

meet sherin


Hello! I'm Sherin, a passionate individual with a love for simplicity . My journey, initially destined for journalism, took an unexpected turn into computer science engineering (CSE). Beyond the binary language of computers, I find joy in creating stories and documenting experiences through journaling. Organizing thoughts and projects is a source of satisfaction, and I also dedicate time to reading books for personal improvement.

Currently a student ambassador at MLSA. Despite the twists, my dream of journalism remains alive. Join me in this exciting fusion of dreams, code, and stories!

Feel free to connect if you share similar interests or want to chat about the magic of reading in the silence of a good book! 🚀

---
## [BladeburstNINJA/f13babylon](https://github.com/BladeburstNINJA/f13babylon)@[ccb9ce38a7...](https://github.com/BladeburstNINJA/f13babylon/commit/ccb9ce38a7e26763f93c089bd0a65c9e35b70243)
#### Tuesday 2023-12-05 11:02:55 by panzerr1944

no mans land; kebob changes (#166)

## About The Pull Request

![image](https://github.com/f13babylon/f13babylon/assets/76122712/cb2a0acd-9aa7-4a0c-bc3a-651c2b0104d4)
Kebab now has renegades. And it's loot increased / fixed.


https://github.com/f13babylon/f13babylon/assets/76122712/22a30f2e-354c-4988-8ac7-e39e9fce9c51

## Why It's Good For The Game
NML's town is no longer free loot. Rather, an optional bunker that the
other factions might jump you at. Kind of like normal bunkers in that
way, except with current NML rules you aren't going to lose your
everything. Just your life until someone revives you. I like the no gear
looting in NML rule, it's kinda funny.

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
ADDED MOBS:
1x pa claw
6x r. docs
3x r. snipers
2x r. meisters
4x r. defenders
6x r. soldiers
10x r. grunts
9x r. prospects
2x r. engies
3x r. guardians
(Total: 46)
REMOVED MOBS:
4x Legendary Ghouls
6x Legendary Mutants
2x Legendary Deathclaws
(Total: 12)
ADDED/EDITED LOOT:
2x Superhigh Ballistic Spawners
1x Mid-High E-Weapon Spawner
1x Mid-High Ballistic Weapon Spawner
1x Mid E-Weapon Spawner
1x Mid Ballistic Spawner
1x NVG Spawner
1x Gauss Rifle Spawner
1x Deluxe Stock Parts Spawner
1x (x10) Strange Seeds Spawner
1x Unique Weapon Spawner
1x High Ballistic Print
1x VHigh Ballistic Print
1x DC Medicine Journal
1x Chemistry Book
1x Random Armor Spawner
1x T4 Armor Spawner
1x Bowl of Fruit
CHANGED TERRAIN / WALLS / MISC:
Sandbags on the main road
Sandbags at the farm and graveyard
Indestructible Walls for south-side to prevent cheese
Replaced see-through airlock with high-sec one in clinic for d-claw
-
Everything else is unedited from current Kebab to my knowledge.

---
## [BladeburstNINJA/f13babylon](https://github.com/BladeburstNINJA/f13babylon)@[a2491a3c89...](https://github.com/BladeburstNINJA/f13babylon/commit/a2491a3c89e4fa54e2c112902162278493f10945)
#### Tuesday 2023-12-05 11:02:55 by Mazzinsanity

Enables Podpeople as a Roundstart Species (May need to be enabled on the box) (#194)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Makes a WEAKENED version of Podpeople selectable as a roundstart
species. Their maluses and bonuses are as follows:
- 1.25 damage modifiers for Brute/Burn
- Restore 2 hunger and heal 0.2 Brute, 0.2 Burn, 0.1 Toxin when in
light.
- Reverse effects in darkness.

Changes podpeople bloodtype to EZ Nutrient
## Why It's Good For The Game
This lets people play as anthropomorphic Broc flowers.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: enabled podpeople as a roundstart species
balance: rebalanced weak podpeople healing
tweak: changed podpeople bloodtype to EZ Nutrient
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ginsanjimi/ginsanjimi](https://github.com/ginsanjimi/ginsanjimi)@[96bf84acf7...](https://github.com/ginsanjimi/ginsanjimi/commit/96bf84acf7f046068d30d6f99b597c609ff27ecd)
#### Tuesday 2023-12-05 11:21:03 by ginsanjimi

Create Man City Draw EPL

Erling Haaland has escaped punishment by the English Football Association for his reaction to referee Simon Hooper's decision to halt play during Manchester City's 3-3 draw against Tottenham on Sunday, but the Premier League champions have been charged with failing to control the behaviour of their players.

City forward Haaland responded to a video clip on X of Hooper's decision not to allow Jack Grealish to race onto a through ball in the fourth minute of stoppage time at the end of the game, with the Norway international writing "Wtf."

FA sources have told ESPN, however, that Haaland's post did not breach rules in relation to regulations covering media comments and social media activity.

Haaland, the Premier League's leading scorer this season, has also avoided censure for angrily confronting Hooper on the pitch following the decision to blow the whistle when Grealish received the ball.

The incident involving Haaland and Hooper is central to City being charged with a breach of FA Rule E20.1 in terms of the conduct of their players.

Haaland led a group of players, including Rúben Dias and Mateo Kovacic, who surrounded Hooper to protest against the decision.

In a statement, the FA said: "Manchester City have been charged with a breach of FA Rule E20.1 after their players surrounded the match official during the Premier League fixture against Tottenham Hotspur on Sunday 3 December 2023.

"It's alleged that, during the 94th minute of the fixture, the club failed to ensure their players do not behave in a way which is improper.

"Manchester City have until Thursday 7 December 2023 to respond to the charge."

Sources have told ESPN that no further charges will be brought against the players or coaching staff from either side.

Video Assistant Referee causes controversy every week in the Premier League, but how are decisions made, and are they correct?

After each weekend we take a look at the major incidents, to examine and explain the process both in terms of VAR protocol and the Laws of the Game.

In this week's VAR Review: How Manchester City were robbed of the chance to win the game against Tottenham Hotspur, plus penalty decisions between Chelsea and Brighton & Hove Albion, and possible spot kicks for Arsenal and Nottingham Forest.

https://sketchfab.com/3d-models/renaissance-una-pelicula-de-beyonce-pelicula-af639ec00f2f4294a50bdd3c52342d9d
https://sketchfab.com/3d-models/ver-godzilla-minus-one-pelicula-hd-b481a1c32f0b4cd090a6a8355d04b43a
https://sketchfab.com/3d-models/ver-trolls-3-se-armo-la-banda-pelicula-hd-bca1aaa09fd74cbb8e951c7098648ed8
https://sketchfab.com/3d-models/ver-wish-el-poder-de-los-deseos-pelicula-hd-4be6460e4fd14e50ad135d0f13b6d3df
https://sketchfab.com/3d-models/ver-napoleon-pelicula-hd-9016012bb8e943f1b96919ed3da1f224
https://sketchfab.com/3d-models/ver-aquaman-y-el-reino-perdido-pelicula-hd-e934e130ac274ff19c46542c0685aaeb
https://sketchfab.com/3d-models/ver-the-shift-pelicula-hd-43fa823bc1474fd1bfe7ba4093ec85ba
https://sketchfab.com/3d-models/ver-venganza-silenciosa-pelicula-hd-ce2d0da793bd4512b9f6689f1ac2f151
https://sketchfab.com/3d-models/ver-viernes-negro-pelicula-hd-1634b43bb33f42ed9435c1a984260ee0
https://sketchfab.com/3d-models/ver-leo-pelicula-hd-2b95dd9f878448248ef64f7fe5d70392
https://sketchfab.com/3d-models/filme-renaissance-a-film-by-beyonce-dublado-89b5e823183c4783afe618dc897f6892
https://sketchfab.com/3d-models/filme-godzilla-minus-one-dublado-2036b38a2a6f438f8e1223386192b226
https://sketchfab.com/3d-models/filme-trolls-3-juntos-novamente-dublado-e4611586dfeb485c991fffc5f8b88cc4
https://sketchfab.com/3d-models/filme-wish-o-poder-dos-desejos-dublado-2f6ba355237747aaa1580a678d4dd731
https://sketchfab.com/3d-models/filme-napoleao-dublado-e4c772b91ebf4cc7847d9a4590905961
https://sketchfab.com/3d-models/filme-aquaman-2-o-reino-perdido-dublado-8c638a6d825646c5b72e6746c4101d91
https://sketchfab.com/3d-models/filme-the-shift-dublado-468c96de1f8142b5b6d8d7aa0ec1a33a
https://sketchfab.com/3d-models/filme-silent-night-dublado-9028b97383574fd9aa8109719b17f21a
https://sketchfab.com/3d-models/filme-feriado-sangrento-dublado-5fe7549b06644dcbb744c67248eeaaff
https://sketchfab.com/3d-models/filme-leo-dublado-ec726dfb28624424904563250f670729
https://sketchfab.com/3d-models/nezd-renaissance-a-film-by-beyonce-teljes-film-722ed57e89f44cf6a1993f31626633aa
https://sketchfab.com/3d-models/nezd-godzilla-minus-one-teljes-film-5834d7f5fe994da18472ab5dfcc90ee9
https://sketchfab.com/3d-models/nezd-trollok-egyutt-a-banda-teljes-film-9b1784bac84d4cb6b497b1c07b43211a
https://sketchfab.com/3d-models/nezd-kivansag-teljes-film-b881d6bb0fad412b9d58414295b91bf3
https://sketchfab.com/3d-models/nezd-napoleon-teljes-film-531f1b85c7c649fbb7b3dbd07cad007b
https://sketchfab.com/3d-models/nezd-aquaman-es-az-elveszett-kiralysag-teljes-5b97aa44cd304ba2973a7e214c5aa866
https://sketchfab.com/3d-models/nezd-the-shift-teljes-film-a06f9d63a4664da9a5bdd51eb708d368
https://sketchfab.com/3d-models/nezd-silent-night-teljes-film-c239ca3de34c4c839b7262c1ac491b81
https://sketchfab.com/3d-models/nezd-hullaadas-teljes-film-27db794c564c4cde9b861e3905f28cae
https://sketchfab.com/3d-models/nezd-leo-teljes-film-3a4ee3a3ad9748e9b0476761e6178071
https://sketchfab.com/3d-models/renaissance-a-film-by-beyonce-2023-af46b124773d4e53a323676f8e805141
https://sketchfab.com/3d-models/10-2023-a8329b687b4c4b7d887a85fb9eb7d5cf
https://sketchfab.com/3d-models/3-2023-67ed0666151b4b1583394f3045493c4e
https://sketchfab.com/3d-models/2023-a72d70d12e65416fa0481a4ab46259fe
https://sketchfab.com/3d-models/2023-b88a56f6e51146cf92abe28a829c9179
https://sketchfab.com/3d-models/2-2023-95026dc7ed2040c0a97eff9024c7faf6
https://sketchfab.com/3d-models/the-shift-2023-510fdfa3f3b7447e992d25ce2b126911
https://sketchfab.com/3d-models/2023-5cb4e17c75f94ab88e2a5a77ec03cce1
https://sketchfab.com/3d-models/thanksgiving-2023-3cf8ea3a03d64233a17ad2103c86b136
https://sketchfab.com/3d-models/2023-865fc9c5812246e3a0c790d4774b4da0
https://sketchfab.com/3d-models/renaissance-a-film-by-beyonce-2023-0e8055f04efb4d3b8ee013c944b710e1
https://sketchfab.com/3d-models/godzilla-minus-one-2023-b785b4b1ecce496a9aede13c08d4db32
https://sketchfab.com/3d-models/3-2023-920c184939f643148d83a9c1186c19f9
https://sketchfab.com/3d-models/2023-fbf0e50de28a4077bc0697d3bcbebeb4
https://sketchfab.com/3d-models/2023-126d296793f34032801f851e42cc7a88
https://sketchfab.com/3d-models/2023-3c50372cc93b4be595b45fe3a1d140f6
https://sketchfab.com/3d-models/the-shift-2023-e9be7ade7e5c4fe9bf53562144774a09
https://sketchfab.com/3d-models/2023-b78f5e6d04ae4fa9825eadddc3c3366d
https://sketchfab.com/3d-models/2023-d540e87ddea748f29d69e61f10b108f2
https://sketchfab.com/3d-models/leo-2023-e7e12c4f949a4e25988a9d06e72da72b

Man City 3-3 Tottenham Hotspur
Play stopped on Grealish counterattack
What happened: The game was into added time when Emerson Royal tripped Erling Haaland in the centre of the park. Referee Simon Hooper paused for a second as Haaland regained his feet, before the striker got to his feet and played Jack Grealish through for a run on goal. But Hooper stopped the play and brought it back for the free kick.

Review: It's not a decision that's covered by VAR, but it was by far the biggest refereeing incident of the weekend.

All referees will incorrectly stop play instead of giving the advantage to the attacking team a few times a season, but not in added time of the biggest game of the weekend when the scoreline is level.

Hooper plays the advantage, but changes his mind with the ball in flight as it is above Grealish and the Tottenham defenders. The referee mistakenly thinks the ball isn't of sufficient quality for Grealish to run on to, yet it becomes clear immediately after he has blown the whistle that the England international may have been through. Hooper's first instinct on the advantage was right, but he's then blown too early to pull it back having misjudged the pass. By that point it's too late.

Of course Hooper got this badly wrong, and we'll never know if Grealish would have got through for a shot on goal or if one off the three defenders, perhaps Ben Davies, would have made a challenge. The Spurs players stopped at the point of the whistle, which may give the impression that Grealish had a greater chance than he did have, but snuffing out the possibility of a match-winning chance is a big error.

Hooper had a good game up to this point, but the only discussion over his performance will be this mistake in a crucial situation.

Despite a high-profile error on the first weekend of the season, when Hooper failed to award an added-time penalty to Wolverhampton Wanderers at Manchester United, he is viewed as one of the most improved Premier League referees over the past year. Towards the end of last season he was given a number of key games, including this same fixture (which City won 4-2), the Merseyside derby and Manchester City vs. Liverpool. This season he was in charge for Tottenham Hotspur's controversial 2-1 win at home Liverpool, when there was a VAR error out of his control to disallow a Luis Díaz goal for offside. Last weekend he was the referee for Newcastle United vs. Chelsea, before being given this City-Spurs game.

Haaland was booked for dissent immediately after the incident, but the Football Association won't look at his furious reaction at the full-time whistle as well as his "WTF??" tweet in response to a video of it. Man City will be charged as the club failed to ensure their players do not behave in a way which is improper.

---
## [ChocolateBananas/app-dev](https://github.com/ChocolateBananas/app-dev)@[67bc6917c3...](https://github.com/ChocolateBananas/app-dev/commit/67bc6917c32384134ee797be3f26fecb9c074fbc)
#### Tuesday 2023-12-05 11:22:20 by ChocolateBananas

Update README.md

# **Alice in Borderland**

## Overview
"Alice in Borderland" is a Japanese science fiction thriller series based on the manga of the same name by Haro Aso. The show, available on Netflix, follows the story of a group of friends who find themselves in a mysterious parallel world where they must participate in deadly games to survive.

## Plot Summary
The series begins with Arisu and his friends accidentally being transported to a deserted Tokyo where they encounter a series of life-threatening challenges and puzzles. To stay alive, they must navigate through various games that test their wits, courage, and teamwork. As they delve deeper into this alternate reality, they uncover the mysteries behind the games and the purpose of their existence in Borderland.

## Characters
- **Arisu**: The main protagonist, a skilled gamer with a strategic mind.
- **Karube**: Arisu's friend and a former delinquent.
- **Chōta**: Another friend with a resourceful and analytical mindset.

## Favorite Moments
The intense game sequences, especially the strategic planning and unexpected twists, keep viewers on the edge of their seats. The evolving relationships among the characters and the unraveling of the overarching mystery add layers of intrigue.

## Quotes
> "In this world, the ones who aren't aware they're lost are the biggest lost ones of all." - Arisu

## Why I Love It
"Alice in Borderland" captivates with its suspenseful storyline, mind-bending challenges, and well-developed characters. The series effectively explores the psychological toll of survival and the bonds formed under extreme circumstances.

## Recommendation
If you enjoy psychological thrillers with a blend of mystery and strategic gameplay, "Alice in Borderland" is a must-watch. The series offers a unique and gripping take on survival in a parallel world filled with enigmatic challenges.

---
## [thepauljones/advent-of-code](https://github.com/thepauljones/advent-of-code)@[b4cde9ebb5...](https://github.com/thepauljones/advent-of-code/commit/b4cde9ebb5631ba7db5343a2442e53dfc983b34a)
#### Tuesday 2023-12-05 11:33:45 by Paul Jones

You unspeakable DICKHEAD, the values are first DESTINATION RANGE then
SOURCE RANGE. Your stupidity cost you lunch with your daughter. Remember
this on your deathbed, worm

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[c9d2c940d8...](https://github.com/timothymtorres/tgstation/commit/c9d2c940d87f5205bdf882280af074b132e1af6c)
#### Tuesday 2023-12-05 11:35:49 by Vekter

Ports feral cats and feral cat grenades from Hippie (#80031)

## About The Pull Request
Feral Cats are just a hostile variant of cats that will fuck you up if
they see you. They are added solely for the sake of feral cat grenades -
a new, interesting, and fuzzy way to get out of a jam or just wreak
havoc around you. Each one costs 5 TC and spawns 5 really pissed off
cats to chase down assistants in the hallway.

They don't currently ignore traitors or the person who threw them - I
haven't worked out how to do that with our faction system (Hippie gave
them the syndicate faction but traitors don't get that on our codebase).
If anyone wants to contribute or help me suss that out it'll be cool,
otherwise just don't be around if there's nobody else for them to maul.

## Why It's Good For The Game
They're funny.

## Changelog
:cl: Vekter
add: Added a new hostile variant of cats, "feral cats".
add: Added a new traitor item, "feral cat grenades". For 5 TC, you too
can throw a grenade at someone and make five cats maul them to death.
/:cl:

---
## [cyphar/runc](https://github.com/cyphar/runc)@[c32a8c34b0...](https://github.com/cyphar/runc/commit/c32a8c34b09efd001274e02ee3371192a9569185)
#### Tuesday 2023-12-05 11:45:09 by Aleksa Sarai

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
## [SWE-B5/SpottingSmallPrints](https://github.com/SWE-B5/SpottingSmallPrints)@[3b18914e48...](https://github.com/SWE-B5/SpottingSmallPrints/commit/3b18914e488aa00c76f987e42b78ea0a4ca196bd)
#### Tuesday 2023-12-05 12:06:46 by Philogex

Merge branch 'bitmap' of https://github.com/SWE-B5/SpottingSmallPrints into Level3
i hate my life

---
## [dubeyabhishek/libbpf](https://github.com/dubeyabhishek/libbpf)@[b064c40d94...](https://github.com/dubeyabhishek/libbpf/commit/b064c40d9460c34d8fb539cf0042b298b888cdd4)
#### Tuesday 2023-12-05 12:23:26 by Daniel Borkmann

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
## [dubeyabhishek/libbpf](https://github.com/dubeyabhishek/libbpf)@[d7e583a6ea...](https://github.com/dubeyabhishek/libbpf/commit/d7e583a6eac64a79c21f1a749e6b3d371b884365)
#### Tuesday 2023-12-05 12:23:26 by Daniel Borkmann

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
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[ef52047274...](https://github.com/OrionTheFox/tgstation/commit/ef520472740e57f253545c24c7526e45e47b5ec2)
#### Tuesday 2023-12-05 12:58:52 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:

---
## [BadIsMyUsername/f13babylon](https://github.com/BadIsMyUsername/f13babylon)@[ec2004b453...](https://github.com/BadIsMyUsername/f13babylon/commit/ec2004b453a5da2b81513777b420a23a845825e3)
#### Tuesday 2023-12-05 13:12:15 by Stutternov

Logistics Officer Buff!!!! (Fuck you, leftover Yellowstone change) (#280)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

Tl;dr - Took the explosive granter off the construction loadout of CE
(why did they have it, they already had the one with C4 with that
trait.......... leftover Yellowstone change) and gave it instead to the
Logistics Officer since they realistically should have it as they do gun
crafting.

Also - it makes it so LO's can make mortar rounds now. Also-also, took
away the X4 off CE since it's strong. Gave them 2 C4 instead.

## Why It's Good For The Game

LO buff omg

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
removes: Removed explosive crafting and BP off of CE construction
loadout.
removes: Removed X4 off of CE explosive loadout option, replaced it with
C4
add: Added explosive perk book to LO so they can craft mortars,
grenades, and be useful. (I will buff them more soon so NCR has to use
them more.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [BadIsMyUsername/f13babylon](https://github.com/BadIsMyUsername/f13babylon)@[e208ee981e...](https://github.com/BadIsMyUsername/f13babylon/commit/e208ee981e86227c2a19b6ae4e35f489be0b0de3)
#### Tuesday 2023-12-05 13:12:15 by SM45H

Khans map (My Git borked on last pr) (#285)

********* EDIT ***********
My last pr got closed because I was having errors with my github and had
to wipe it. The khamp is 90% the same as before. I removed the upper
level defense post and removed the lower sentry post's weather cover. I
added more trash piles in khamp, added an advanced workbench and two
advanced salvage spawns in the back thats protected with indestructible
walls so it cant be cheesed. I also made sure it was at the very end of
the bunker so it had to be earned. The back dungeon is much harder than
any other factions "down river". I also removed the wasteland medical
spawners, and replaced them with a few static meds. While I was mapping,
I fixed the church's zoning by heavens night, basically giving it a
roof.
********* EDIT ***********


Updated the khans, gave khamp character and flow, as well as beautifying
it. most of what was in the khamp as far as resources, was moved over
give or take a few things. moved the khans "down river" to the bunker
they use to run out of, filled with plenty of mobs. Most notable gear in
the back is one set of Khan armor(full helm and coat) as well as some
money and gunbook 3. Past servers, khans had a gun book down river. They
have to fight the khan killer ghoul and his little gang of attack
ghouls, and several mirelurks and a few mirelurk nests.

Gunpowder, metal, glass are with the spiders, and bbq sauce, mustard
packets, and hot sauce packets are guarded by mister handies and
cockroach. I added a few Easter eggs and funnies in khamp, that
including past khan dog, sunflower (forgor gurilla), a few batteries in
the river because, where else are you suppose to toss out your old car
batteries.

Khans base, while a bit bigger, does stay within the old dense rock
space they could mine out and stay within.





![image](https://github.com/f13babylon/f13babylon/assets/151568060/637ba21d-70f1-4eef-9ebc-2c8c31916b45)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/c0574a7a-aa19-456d-baf9-5116107ed8b9)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/fe2c4c81-f6ba-487a-a7c8-287bc8397ff1)

---
## [BadIsMyUsername/f13babylon](https://github.com/BadIsMyUsername/f13babylon)@[893e0e151c...](https://github.com/BadIsMyUsername/f13babylon/commit/893e0e151c05648fd712f75e24520fc77354ed39)
#### Tuesday 2023-12-05 13:12:15 by lolman360

robot update/rework (#204)

## About The Pull Request

does a lot of changes to robots
all changes TBD

robots are now much faster (0.3 slowdown instead of 1).
they are also somewhat tankier across the board to compensate for their
lack of armor (0 armor btw)

robot modules have been revisited:
medical assaultron was rolled into medical borg and is now an altskin.
mining borg now has a shovel, and its emag module is a rocketsledge that
mines better and has 12 less damage.
engiborg's emag module is also a rocketsledge (uncreative)
assaultron was rolled into secborg and is now an altskin.
vtec has been nerfed significantly from -1 slowdown to -0.25

gutsy flamethrower nerfed significantly: 1s firedelay, 33% lower
projectile count, actual energy cost

all robots now have the wastebot faction, since all selectable sprites
are fo13 robots anyways. this also makes slugs do 90 damage to them,
which is extremely funny and something i might remove. again, tbd



## Why It's Good For The Game

as long as they're pickable they should be functional

## Pre-Merge Checklist
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.


## Changelog

:cl:
add: new stuff to robots
del: old stuff from robots
tweak: robots can now patch nests
balance: robots are overall buffed (holy shit their slowdown was
dogshit)
/:cl:

---
## [BetaMasaheft/Manuscripts](https://github.com/BetaMasaheft/Manuscripts)@[c007da66c1...](https://github.com/BetaMasaheft/Manuscripts/commit/c007da66c1f1f72eec8fc29d00701424d7d8c22d)
#### Tuesday 2023-12-05 13:42:50 by Carsten Hoffmann

Update BMLacq679 (#2202)

I updated BMLacq679 by adding four newly created PRS ID in a1.
I created four PRS IDs for people mentioned in BMLacq679 as discussed in #2310.

I came to the conclusion that the person PRS14220HeggaYohannes is the father of PRS14221Menilek.

I am still puzzled as to whether it is possible to establish a family relationship for the others as well.
PRS14222TawaldaMadhen can be seen to be the heir or heiress of the former, if we accept this name in connection with አርስት (succession, inheritance, etc.).

PRS14223Maqaryos is mentioned as ራብአዊ, but it is not clear what ራብአዊ stands for. He could be the fourth in the line of succession (e.g. the great-grandson), or the fourth in the list of blessed people. It is unlikely that he is a high-ranking dignitary such as a patriarch or abbot, as he has no title to indicate this.

The text is given twice on two successive folios. There is some uncertainty about the name Həgga (ʾƏgziʾabəḥer) Yoḥannəs, as he is mentioned once as Həgga Yoḥannəs and the second time as Həgga ʾƏgziʾabəḥer Yoḥannəs. However, I think that the encircling of ʾƏgziʾabəḥer tells us that the name ʾƏgziʾabəḥer was a mistake of the scribe.

<img width="333" alt="Screenshot 2023_Maqaryos" src="https://github.com/BetaMasaheft/Persons/assets/40291787/7e788751-d953-40c9-9e5f-76fed47e960b">

NB. I did not understand how to reference an issue. When I press the 'reference' button in the taskbar, nothing changes except for the # that is introduced.

---
## [SergeBayet/poem](https://github.com/SergeBayet/poem)@[f53797eaf9...](https://github.com/SergeBayet/poem/commit/f53797eaf94942969dc5886f74ba0452f9f8c962)
#### Tuesday 2023-12-05 14:06:20 by Serge Bayet (seba)

[IMP] zen: verse about ambiguity and guess

Computers have made humans superstitious: To exorcise the demons in our
computers we perform the sacred ritual of turning them off and then on.
Supposedly this will fix any mysterious problem. However, computers are
not magic. If your code isn’t working, there is a reason and only
careful, critical thinking will solve it. Refuse the temptation to
blindly try solutions until something seems to work; often you have
merely masked the problem rather than solved it.

---
## [Gboster-0/lobotomy-corp13](https://github.com/Gboster-0/lobotomy-corp13)@[a6679e4b1d...](https://github.com/Gboster-0/lobotomy-corp13/commit/a6679e4b1d8234561fb5500fdd429ff611281daf)
#### Tuesday 2023-12-05 14:58:06 by IndieanaJones

Lets Player-Controlled Monkeys Make Noise When Using *Screech (#62206)

This PR lets player-controlled monkeys make screeching noises using *screech.

Under the hood, this PR also adds a new proc to emotes called, should_play_sound. What this does by default is the same check run_emote used to do with only_forced_audio, but now that it's in a proc you can override it if you want to. Though, let's be real here, this is only going to get used for this PR because the only reason you'd want to bypass that check is if you're doing something for monkeys. The amount of extremely specific circumstances which even warranted something like this could only stem from some stupid monkey/alien specific crap anyway, BUT JUST IN CASE YOU NEED IT, here it is.

Considering all the screeching AI monkeys do, it's a big shame that currently player monkeys can't do similar. 

Considering that monkeys are valid salad and that AI monkeys already screech a lot anyway, I don't think letting players get in on the fun is a bad idea. If need be, we can just tune up the sound cooldown on *screech but I don't think it's really that abusable to begin with.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [srifqi/minetest_game](https://github.com/srifqi/minetest_game)@[4bb4a2a818...](https://github.com/srifqi/minetest_game/commit/4bb4a2a8187d036325482bb727a65b899f8991bd)
#### Tuesday 2023-12-05 15:00:14 by Yaya - Nurul Azeera Hidayah @ Muhammad Nur Hidayat Yasuyoshi

Update Malay translations
1. Added missing translation to the following files:
  beds.ms.tr, creative.ms.tr, default.ms.tr, farming.ms.tr,
  fire.ms.tr, sethome.ms.tr
2. Changes some translation as per following:
  a. beds.ms.tr
    - Leave Bed changed from Bangun (wake up) to Tinggalkan Katil
      (leave bed, in literal sense) just because the button would
      be interpreted by some people as 'wake up on next morning'
      (ie. skipping night) instead of 'wake up interrupting current
      sleep progress' which is the intended meaning.
  b. boats.ms.tr
    - Boat cruise mode changed from Mod bot layar makan angin to
      Mod jelajah bot, the original translation is more like direct
      translation, and this has been changed to more natural one
      to make sure player know that the mode is a cruise control.
    - Reset changed from Set semula to Tetap semula, this is for
      standardizing with existing term used in various places.
  c. default.ms.tr
    - Page \@1 of \@2 changed from the short form to the long form.
    - Mese Crystal Fragment had missing word 'Kristal' re-added.
  d. dye.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.
  e. game_commands.ms.tr
    - respawn changed from lahir semula (reborn) to jelma semula
      (reappear), this is to make it consistent with the language
      used in multiple other games that had similar respawning
      system, and avoiding the religious context of life that is
      implied by the use of previous translation.
    - spawnpoint changed from titik permulaan (starting point) to
      titik jelma ((re)appear point), see previous point.
  f. tnt.ms.tr
    - Gun Powder changed from Serbuk Senjata Api (firearms powder)
      to Serbuk Letupan (explosion powder) because that is the
      proper translation, the latter is still the term used even
      when talking about actual firearm, the former didn't exist
  g. vessels.ms.tr
    - item changed from barang (thing) to item, this is mainly
      because some of the 'item' that could be stored are not
      some solid 'thing' where the word barang could be used for,
      so using the word item here keep it neutral.
  h. wool.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.

---
## [RafaelVince/app-dev](https://github.com/RafaelVince/app-dev)@[0bc3c463cb...](https://github.com/RafaelVince/app-dev/commit/0bc3c463cb8bbdb7d38472826e1e2504c001bd02)
#### Tuesday 2023-12-05 15:04:37 by RafaelVince

Update README.md

# Stranger Things

![Stranger Things](https://via.placeholder.com/600x300)

**Synopsis:**
"Stranger Things" follows a group of kids in 1980s Indiana who encounter supernatural mysteries after their friend disappears. They uncover a parallel dimension, a girl with special abilities, and government secrets.

**Main Characters:**
- **Eleven**: A girl with psychokinetic abilities.
- **Mike, Dustin, Lucas**: Friends investigating the mysteries.
- **Chief Jim Hopper**: Involved in uncovering secrets.

**Why It's Popular:**
- 80s nostalgia, horror, mystery, sci-fi blend.
- Strong characters, plot twists, young cast's performances.
- Memorable soundtrack and cinematography.

**Trivia:**
- Eleven is named after her experimental number, "011."
- The Upside Down was inspired by the Montauk Project conspiracy theories.
- The Duffer Brothers pitched the series to various networks, receiving rejections before Netflix picked it up.
- Millie Bobby Brown, who plays Eleven, shaved her head for the role.

**Fun Fact:**
Did you know the character of Eleven was initially meant to have a more limited role in the series, but the Duffer Brothers expanded her character due to Millie Bobby Brown's exceptional audition?

**Watch it on:** [Netflix](https://www.netflix.com/title/80057281)

---
## [nss-dev/nss](https://github.com/nss-dev/nss)@[2137313bb1...](https://github.com/nss-dev/nss/commit/2137313bb1d973790fdd15b3d568c94862a2b51f)
#### Tuesday 2023-12-05 16:19:09 by Martin Thomson

Bug 1549225 - Up front Signature Scheme validation, r=ueno

Summary:
This patch started as an attempt to ensure that a DSA signature scheme would not
be advertised if we weren't willing to negotiate versions less than TLS 1.3.
Then I realized that we didn't do the same for PKCS#1 RSA.

Then I realized that we were still willing to try to establish connections when
we had a certificate that we couldn't use.

Then I realized that ssl3_config_match_init() wasn't being run consistently.  On
resumption, we only ran it when we were PARANOID.  That's silly because we
weren't checking policies.

Then I realized that we were allowing ECDSA certificates to be used when the
named group in the certificate was disabled.  We weren't enforcing that
consistently either.  However, I also discovered that the check we have wouldn't
work without a tweak because in TLS 1.3 the named group is part of the signature
scheme; the configured named groups are only used prior to TLS 1.3 when
selecting ECDSA/ECDH certificates.

So that sounds like a lot of changes but what it boils down to is more robust
checking of the configuration prior to starting a connection.  As a result, we
should be offering fewer options that we're unwilling or unable to follow
through on.  A good number of tests needed tweaking as a result because we were
relying on getting past the checks in those tests.  No real problems were found
as a result; this just moves failures that might arise from misconfiguration a
little earlier in the process.

Differential Revision: https://phabricator.services.mozilla.com/D45966

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[8c0becb4f0...](https://github.com/nikothedude/tgstation/commit/8c0becb4f08ec50e00ed758022e18fb1381f4f25)
#### Tuesday 2023-12-05 17:02:59 by Da Cool Boss

Makes oculine taste slightly better (#79919)

## About The Pull Request
Changes oculine's taste from 'dull toxin' to 'earthy bitterness'.
Probably deserves the no GBP tag.
## Why It's Good For The Game
Oculine is a benign/helpful chem that naturally occurs in carrots. This
means it's in all carrot based food the chef cooks, and if the carrots
cross pollinate with another plant it's in those too. This is currently
a problem, because it means the chef's carrot sticks taste like poison
and this tends to freak out new players who don't know that's just what
oculine tastes like.

Oculine has no negative effects besides potentially triggering a medical
allergy quirk, it can't even be overdosed. So if you see a worrying "you
taste dull toxin" message, there's actually no reason to be concerned.
Still, I see players who are *convinced* the chef is poisoning their
carrot cakes fairly regularly. This should cut down on wasted multiver
and lynched chefs.

I changed it to "earthy bitterness" because that's what some species of
carrot taste like, and "bitterness" implies medicine. The paranoid can
still assume they're being dosed with morphine or something, but they're
not being misled into thinking this. For people chugging medicine
bottles from chemistry, oculine stands out a little less too.
## Changelog
:cl:
qol: Oculine now tastes bitter, and not like toxin.
/:cl:

---
## [shaban1819/Video-player](https://github.com/shaban1819/Video-player)@[d05a643280...](https://github.com/shaban1819/Video-player/commit/d05a64328069323e7625fae9d76c29e9d9948406)
#### Tuesday 2023-12-05 17:31:08 by shaban ali

Add files via upload

Welcome to the Awesome Video Player App – an Android application designed to meet all your video playback needs with a plethora of cool features and a slick user interface.

Features
Bass Boost Equalizer: Enhance your audio experience with the built-in bass boost equalizer.

Zoom In / Zoom Out: Get closer to the action or zoom out for a wider view during video playback.

Smooth Playback: Play all the popular video formats seamlessly, ensuring a smooth viewing experience.

Full HD Support: Enjoy videos in stunning Full HD resolution with 1080p playback.

Swipe Controls: Swipe gestures for adjusting volume and brightness make it easy to customize your viewing experience.

Subtitle Support: Watch videos with subtitles in your preferred language.

Playback Speed Control: Manage the playback speed of videos to suit your preference.

Picture-in-Picture Mode: Multitask with Picture-in-Picture mode, allowing you to play videos in a small window while using other apps.

Double Tap to Play/Pause: Conveniently control playback with a simple double-tap gesture.

Night Mode: Switch to Night Mode for comfortable video viewing in low-light conditions.

Video Library: Explore a section that showcases all videos on your device, with detailed information about each video's properties.

Video Properties: View essential information such as video name, path, size, length, duration, and resolution.

Share Videos: Share your favorite videos with friends directly from the app.

Search Videos: Easily find specific videos by searching with the video name.

Video Lock and Unlock: Secure your videos by locking and unlocking them.

Scaling Options: Choose from different scaling options, including Fullscreen, Zoom, and Fit.

Play Next/Previous Video: Effortlessly navigate through your video library with next and previous video functionality.

Sorting Options: Sort video files by name, date, length, and size in ascending or descending order.

Usage
Clone the repository, build the project with Android Studio, and install the APK on your Android device to start enjoying an enhanced video playback experience.

---
## [misterghast/tgstation-Ghastified](https://github.com/misterghast/tgstation-Ghastified)@[39d9c45b4a...](https://github.com/misterghast/tgstation-Ghastified/commit/39d9c45b4a7afc2a963de4249592a3d4ae6c4715)
#### Tuesday 2023-12-05 17:37:03 by san7890

Meat Hook Rework (Accidental Features) (#80002)

## About The Pull Request

Or, how I tried to kill `/datum/forced_movement` but got absolutely
clonged.

Actually, I did kill `/datum/forced_movement`. It was only used in one
spot so I just went ahead and cooked it into a special utility datum
that should only be used in one spot. We can optimize the code later or
something, but I like the way it is right now (pretty much status quo
without the potential of someone using a depreciated framework).

Alright, there were also like 3 `TODO`s (4 if you count the move loop
comment (which is ehhhh)). I naively tried to tackle them a very hard
way, but then I just realized I could use the fancy new datum I cooked
up and wow they're all solved now. The hook looks so fucking good now.

* The code is overall more streamlined, with all of the post-projectile
work being handled by a special datum (I wanted it to be handled by the
hook but the timings were all based on SSFastprocess so datum it is).
Forced movement is killed but we just salvaged whatever we needed from
it.
* More traits to ensure we don't cheese in a way we're not supposed to
* A very sexy chain will spawn when you drag your kill in (this wasn't
there before but I fixeded it :3)
* The firer will actually get grounded when they try and shoot the chain
out. They get grounded for 0.25 seconds unless they hit something. I
don't know how the timing is but I think it's fair.
* We also add a unique suicide act, because I noticed we did the
"magical" one previously, which big-league sucked.
* More traits to ensure less cheese! I like how nice it is now.
## Why It's Good For The Game

The meat hook really makes you _feel_ like Roadhog from Overwatch.
Resolves a bunch of old TODOs while getting rid of a completely obsolete
framework in a really neat way. I don't typically like mixing balances
and refactors but these TODOs were getting crusty man i just wanted to
get them out of the way
## Changelog
:cl:
balance: The Meat Hook will now "ground" you whenever you fire it out at
someone. You get a very small immobilization every time you fire, which
"upgrades" to a full immobilization whenever you actually hit an atom
and start to drag it in.
fix: A chain should now show up as you drag in something with the meat
hooks.
fix: Meat hooks should no longer play the "magical gun" suicide if you
were to use it, but instead do their own unique thing.
/:cl:

---
## [misterghast/tgstation-Ghastified](https://github.com/misterghast/tgstation-Ghastified)@[08ab5d2731...](https://github.com/misterghast/tgstation-Ghastified/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Tuesday 2023-12-05 17:37:03 by Mothblocks

Blood brothers is now a single person conversion antagonist (#79971)

## About The Pull Request
Instead of choosing 2-3 brothers, *one* person will be selected and
given a flash which can convert one other person over. In accordance to
the existing 10% chance for 3 members, there is a 10% chance that the
first person converted will receive a flash of their own.

Expectation is people will flash a friend or a robust guy or whatever.
My intent is primarily to see if this kind of blood brothers is more
enjoyable to play with/against, and if their inclusion in a round
increases the general chaos of it. My theory is that since most likely
blood brothers will be people who know each other, that it can become
more consistently interesting to the rest of the crew. That or they just
murderbone together idk

Fikou and head admins said they wanted this to replace rather than add
which I agree with.

## Why It's Good For The Game
Keeps the sandboxy aspect of blood brothers (no uplink) while likely
making it more enjoyable to play. Conversion is equally as simple as
revs for the user, and is just as intuitive to the one being converted
since there are no new mechanics thrown in your face.

Blood brothers is currently disabled everywhere on the main servers
except for MRP. I think this form will be more appealing to all
rulesets. If left enabled, Dynamic now has more antagonists to make
rounds diverse with and I want that

## Changelog

:cl:
add: Instead of teaming up random people together, blood brothers will
now start out with one player and let them convert a single other person
over to blood brother using a flash.
/:cl:

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[e40ed2a59b...](https://github.com/wrye-bash/wrye-bash/commit/e40ed2a59b28e74307157f7c438bb1b29736374f)
#### Tuesday 2023-12-05 18:03:04 by MrD

Squashed version of ut-353-pt1-578:

Refactoring in load order: TTT EEE lowercase todoS

Move  the logic of _filter_active in callers - they were doing the checks
anyways - then inline - we certainly want to thin LoGame API, _games_lo
is complex enough and flat is better (and shorter) than nested here.

_CleanPlugins(LoGame):

Clean/create logic is very hard to follow - let's confine it to games that
need it. We then need to clarify what happens with cached parameters vs
creating the plugins txt

EAFP for parsing mod file

Then I realized that since 96394dda9179188825cc184ea84d689bda667824
actually for Textfile games we only need to remove the master_path,
so _active_entries_to_remove is only needed in AsteriskGame - then
_clean_actives, which for Asterisk necessarily cleans
the whole plugins.txt, is inlined taking down tricky logic and lots
of comments trying to explain what goes on.

Oh lord_func:

I. Use the return value:

This necessitated returning from _update_cache -> refresh_lo (single
use)

quiet WIP:  EEE fix_load_order override

get_load_order had quiet=False effectively - added this as default to
fix_load/active and then in set_load_order quiet=True and set it only
in load_order.save_lo

Became clear that warn_missing_lo_act was only updated when quiet was
False which was when lo_deprint was called. This simplified the guts
of _game_lo at the expense of a local modInfos import - good.
Not sure about the _fix_load_order override - if fix_lo was None which
only happened in _restore_lo (quiet=True), it would not reorder the added
plugins but add them to the end - do we want that? I dropped the debug
message as anyway the lo_added will be printed.

Expose more LoadOrder attributes:

The index dicts contain all the info of load order/active changes - as
a bonus a couple one-line, one-use methods were removed. load_order.py
is the balt of load order handling and although (because of saved load
order handling) it does have a well defined role it still needs to be
kept at a minimum - more on this later.

TTT simplify/optimize _refresh_mod_inis

No need to clean up since we overwrite at the end - pruned also the OD.

Only the values of _plugin_inis was used - simplify and make easier to
track by exposing it and removing essentially no op ini_files (not the
.py module)

WIP refactor BP activations handling: EEE remove todo

count would decide on refreshing saves - probably if any mods got
activated we should DO. Moved the info handling higher up, I need to do
activations in parent.

Reduce occurrences of lo_activate (2)/cached_lo_save_active (1) - these
must be further confined. Note the decoupling from load_order (and Link)
in patcher_dialog.py

_modTimesChange -> unlock_lo TTT

Was unlocking in all except one case TTT - in those cases unlocking made
only sense if the game was a timestamp game - I am glad I kept
_modTimesChange and gladder I dropped it

Stashing a [!] as there are subtle changes in the logic - note that:

Mopy/bash/basher/mod_links.py: we wouldn't unlock - wouldn't that revert
the redates TTT?
Mopy/bash/basher/app_buttons.py: while we did unlock always we did not
forceRefresh - well it's a couple stats(), won't harm

The rest is fine - just one more use of using_txt_file, inside the same (DoSave)
scope - good sign.

Mopy/bash/basher/installers_links.py: the (not so) long term goal is to absorb
this into refresh - need to refactor base signature for this.

XXX FFF?+            forceActive=deleted or unlock_lo, unlock_lo=unlock_lo)

Mopy/bash/gui/popups.py: user_ok was essentially unused, was checked in show_modal

WIP setGhost return status change: RRR TTT drop notify bain?

This gets us rid of a few uglyStuff including a Path method (# RRR 368), and
one bare except - we might as well deprint out (and maybe tighten the
remaining except).

As seen in _refresh_from_data_dir we chop off the ghost extension so we
should not notify BAIN TTT cause data_sizeCrcDate is difficult to track,
hence WIP see next commit

Under # 219

isGhost -> is_ghost:

Now that autoGhost is (will) be gone

Some nit - in particular no need to create these (None, None, None) tuples

More undead pruning: TTT

Including one more modInfos local import - typing is badly needed here

Drop _reset_info_sets: TTT

Finally, this set up was a smell. This makes some calls like new_info
more expensive but no worries

TTT new_info: the _in_refresh param is obviously a temp hack :P

---
## [yevagami/Midstone-Flat-Eathers](https://github.com/yevagami/Midstone-Flat-Eathers)@[90a8304e12...](https://github.com/yevagami/Midstone-Flat-Eathers/commit/90a8304e1207bfaf164d21ea26f58a891c32dea2)
#### Tuesday 2023-12-05 18:09:51 by worflor

balance changes!

- differnet enemy types spawn in the mob spawner
- balanced each enemy type
- added more sound effects
- added a shield sound effect
- removed wait till you see me on my bike ;( ;-;

In a bustling town, Kiriko stands out not for her words but for the gleaming steel companion by her side – her beloved bike. The mundane rhythms of daily life pale in comparison to the thrill that courses through her when she envisions the phrase, "Wait till you see me on my bike." To Kiriko, this isn't just a string of words; it's a mantra that encapsulates her unbridled passion for the sleek two-wheeled marvel that accompanies her wherever she goes.

While others discuss matters of love, family, or ambitions, Kiriko's singular focus remains her bike. Its frame carries the weight of her dreams and aspirations, and its wheels roll through the moments that matter most to her. Friends may come and go, but the bond between Kiriko and her bike is unbreakable.

As the world swirls around her with its complexities, Kiriko finds solace in the simplicity of that phrase. It's not just about riding; it's about freedom, escape, and an unspoken connection between her and the open road. Whether navigating the crowded streets or cruising along quiet paths, Kiriko's bike is her steadfast companion, a vessel that carries her through life's twists and turns.

In a tale where passion takes the form of spinning wheels and the wind in her hair, Kiriko's story unfolds not in epic dialogues or grand gestures but in the quiet hum of her bike's wheels and the anticipation that builds with each utterance of those six words: "Wait till you see me on my bike."

---
## [Hex27/TerraformGenerator](https://github.com/Hex27/TerraformGenerator)@[11208bb06f...](https://github.com/Hex27/TerraformGenerator/commit/11208bb06fc77d135d1b27e20e22561385b91619)
#### Tuesday 2023-12-05 18:55:15 by Hex27

Its not crashing anymore

god i fucking hate concurrency

---
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[2fc0dfd8c1...](https://github.com/oxidecomputer/omicron/commit/2fc0dfd8c11f31e66cfaf8ee80586bb2ed607216)
#### Tuesday 2023-12-05 19:04:33 by Andrew J. Stone

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[73f7f80127...](https://github.com/treckstar/yolo-octo-hipster/commit/73f7f801273ee0edc1b0aa99f1ae706682d14b7c)
#### Tuesday 2023-12-05 19:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Crazybbsaber/AoC-23](https://github.com/Crazybbsaber/AoC-23)@[7d7ea654d2...](https://github.com/Crazybbsaber/AoC-23/commit/7d7ea654d235ccf504938ff9ba7d91f59418ff5f)
#### Tuesday 2023-12-05 19:42:16 by Crazybbsaber

It doesn't work, but here's Day 5 of AoC Part 2

It'll fuck your computer for nothing

---
## [katerd/aoc2023](https://github.com/katerd/aoc2023)@[6a97a3726f...](https://github.com/katerd/aoc2023/commit/6a97a3726fa749ee727583e170bd578617a6ecf4)
#### Tuesday 2023-12-05 20:12:06 by Kate Reidy

day 5 part 2 - Holy shit rayon is hilariously good

---
## [lachesis17/EQ-Plugin](https://github.com/lachesis17/EQ-Plugin)@[10c61a4fca...](https://github.com/lachesis17/EQ-Plugin/commit/10c61a4fca04dd3f7f8c83785271d8b18864f129)
#### Tuesday 2023-12-05 21:20:21 by Anton

BUILD IN RELEASE MODE.... OMG THE RELIEF OF FPS

HOLY SHIT THE PERFOMANCE IS SO MUCH BETTER

---
## [kmorel/lab-notebook](https://github.com/kmorel/lab-notebook)@[ab12655e4c...](https://github.com/kmorel/lab-notebook/commit/ab12655e4cbd1558eba9b3c1999bdb9ad654f55d)
#### Tuesday 2023-12-05 21:25:04 by Kenneth Moreland

Fix issue with two consecutive text file inclusions

If you had two text inclusions, the first text inclusion would
"eat" the newline required for the regex of the second text
inclusion. This fixes that problem by requiring a single newline
at the end. Thus, two sequential text inclusions work as long
as there is a space in between them.

I honestly don't remember why the text inclusion needs to consume
the newline at the end. Now it ensures that the text inclusion
is alone on the line, but it was not that way before. Nevertheless,
I am hesitent to remove that as I don't want to cause problems
with existing notes.

---
## [briossant/BAME-OCR](https://github.com/briossant/BAME-OCR)@[54e199fa63...](https://github.com/briossant/BAME-OCR/commit/54e199fa637073550cc096bcf25b57d3f16428cd)
#### Tuesday 2023-12-05 21:44:32 by antoine.lassagne

Rotation fuck you but you wotk so thank yougit add ImageProcessing/Rotation.c git add ImageProcessing/Rotation.c git add ImageProcessing/Rotation.c !

---
## [nrc-cnrc/gramble](https://github.com/nrc-cnrc/gramble)@[48d9b1d1cc...](https://github.com/nrc-cnrc/gramble/commit/48d9b1d1cc5678d7c5719a513abd41eff9c14d15)
#### Tuesday 2023-12-05 21:51:35 by littell

Letting Envs vary by the pass

There's an abstraction about components, passes, and envs that we weren't capturing, and in fact were doing something kind of silly.

This was making it tedious to adapt CalculateTapes in the way that solves the last commit's issues, so I figured it was high time to fix this.

(0) Before doing this I switched back to using top-level vocabs in generation, to return us to (mostly) green, so I could refactor in safety.

(1) Out of suspicion, I deleted `CollectionGrammar.mapChildren` (which is responsible for putting its symbols into env.symbolNS), which should have caused major failures left and right.  That's part of WHY mapChildren is a member, so that CollectionGrammar can put those there, because that's really important, right?  That's part of why we have a symbolNS in PassEnv, right?

Turns out, no.  Nothing failed because we never BOTH used mapChildren AND used those symbols from it.  All the remaining functions that use `env.symbolNS` that way aren't component-to-component Passes, so they can't use mapChildren anyway.  They were changing env.symbolNS and then recursing manually.

Meanwhile, there are places where we're manually changing parts of the environment before recursion, but not using Env, because Env is quite limited in what it can do.  If we need to do anything in a Pass that isn't push symbols onto the symbolNS, we can't use the boilerplate and thus have to manually recurse -- and as mentioned, pushing symbols isn't even something we need during the main passes.

So really, Env wasn't doing much.  It was really just a place to store Options.

(2) Stepping back, what we need Env to do is to assist in the tedious management of certain kinds of information during a recursion strategy: stuff that mostly stays intact through the traversal but occasionally changes.  Symbols, tape references, etc.

The reason Env wasn't very good at this is that different passes have different environmental needs -- they need different information, and change it in different ways.  But the way we create and compose them made it difficult for them to vary.  We start with a PassEnv at the very beginning and then thread it through ~20 passes.

(3) Do passes ever need to share an Env?

Sometimes!  ExecuteTests is a good example of this.  Now that staging is handled by Passes, and ExecuteTests does its own staging, that means ExecuteTests now has 4 or 5 "child" passes.  Those child passes are executed on nodes that aren't themselves roots, so they won't necessarily go through a CollectionGrammar to get something into a symbol table.  Therefore yes, they need to use their parent's env, which DID go through a CollectionGrammar.

On the other hand, we never have two "sibling" passes -- ones that happen one after another -- that need to share information.  We've been cautious to avoid that, we try to share that kind of information only by adding something to the tree.

So `Pass.compose` doesn't have to thread an env through both of its children.  NOT threading the env like this takes away the need for them to all be the same type.

(4) While Env-changing takes various forms, it's typically done in the same place -- immediately before recursing.  (I mean, if we changed it *after* recursing nothing would happen.  It's not like we return them, if we made a new env it would just be garbage collected when we leave the scope.)

So now there's a method `Env.update(g)`, basically meaning "Change the env in whatever way necessary using information from g".  By default it doesn't change anything; if you need to change something, inherit from Env and override this method.

For example, `SymbolEnv.update(g)` looks at g, and if it's a CollectionGrammar, it pushes those symbols into the `SymbolEnv.symbolNS` and returns the new env.  Otherwise it returns the original env.  This will be called automatically by mapChildren -- achieving what `CollectionGrammar.mapChildren` used to do, but now only when necessary, and when something else is necessary, `WhateverEnv.update(g)` can do that instead.

(5) Passes now have a method `.getEnv(opt)` that'll provide an empty instance of whatever kind of Env that pass needs, and the requests opts.

(6) On Friday-ish I got rid of `Pass.go()` for being both useless and poorly-named.  But we now need a top-level method in the same place.  We don't want to use `.transform(g, env)` everywhere because that's passing in an env, and except in special circumstances we AREN'T passing in envs, we're getting new ones with `.getEnv(opt)`.

So now there's a method `.getEnvAndTransform(g, opt)` that does what it says on the tin.  This is the method that CombinedPass calls instead of calling transform, and the main one we'll want to be calling elsewhere.

(7) I think we can simplify all this more in the future, but anything more than this is premature refactoring, we have to make sure this does what CalculateTapes is going to need, first.

---
## [mootjso/Fuji_Films](https://github.com/mootjso/Fuji_Films)@[a62660c82c...](https://github.com/mootjso/Fuji_Films/commit/a62660c82ca60f89cf6f0fc9661d7883f43d03aa)
#### Tuesday 2023-12-05 21:58:00 by Mo

Update ReservationHandler.cs

Product Owner requested to keep the comments serious without any jokes.

- Removed the lovely friendly comments to keep it more serious.

---
## [ElaraLang/h2jvm](https://github.com/ElaraLang/h2jvm)@[d2fb85b3b8...](https://github.com/ElaraLang/h2jvm/commit/d2fb85b3b87ad9440a3d438edb0b9947d26d8533)
#### Tuesday 2023-12-05 22:07:19 by Alexander Wood

oh nix you are funny sometimes i love you and dont hate you at all

---
## [jupyterkat/Shiptest](https://github.com/jupyterkat/Shiptest)@[09e95cdfbc...](https://github.com/jupyterkat/Shiptest/commit/09e95cdfbc8337b5b7a84a088c32b458ee1d996d)
#### Tuesday 2023-12-05 22:40:37 by Bjarl

Saloon rework (#1594)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Expands whitesands_surface_camp_saloon to cover a 30x30 footprint and
not be nearly as bad. The previous version had some really glaring
design flaws, like holes in the wall for a bar. On a planet with a
deadly atmosphere. Yeah. Also all the chairs faced the same direction.
![2022 10 31-11 32
50](https://user-images.githubusercontent.com/94164348/199083356-5fabd2c8-0298-4a31-a830-b63dbcd2737f.png)
You can see how it looks. It's not great. 
Here's the new version
![2022 10 31-11 36
20](https://user-images.githubusercontent.com/94164348/199083924-9537beb7-0c74-4c57-9422-60fe953ae0bc.png)
![2022 10 31-11 36
25](https://user-images.githubusercontent.com/94164348/199084468-32d94ec8-846f-42e7-ae33-dc0b52e8b9b8.png)

![dreamseeker_ePSrp5zNFp](https://user-images.githubusercontent.com/94164348/199085448-24879745-650f-4bdc-9b0c-f1d9706ab865.png)
Ignore the patches of error, it's purple grass and doesn't display the
icon in sdmm for some reason.

The major changes are:
Expanding the building's footprint out to 30x30
Moving the loot behind the building, but locking it behind a shovel of
some sort (of which you can go through the ruin to get).
Improving the loot a LITTLE

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] The map loads although I still haven't managed to get it to load
on the proper planet with the spawning verb

## Why It's Good For The Game
The old version was kinda bad. Between the clown and mime masks out
front. The small footprint, and the free guns (also out front). This
solves those issues kinda while making it bigger.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Camp_Saloon has been expanded, expect frontier luxuries if you find
it!
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
## [jupyterkat/Shiptest](https://github.com/jupyterkat/Shiptest)@[c21670412d...](https://github.com/jupyterkat/Shiptest/commit/c21670412dff10f4a3a1b1ab1e72f53294581d25)
#### Tuesday 2023-12-05 22:40:37 by Bjarl

New Ruin: The Beach Town (#1572)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a new beach ruin, the abandoned beachside town
![2022 10 10-18 20
10](https://user-images.githubusercontent.com/94164348/194977185-0f35d08e-64c1-459d-94b2-ec6b66137753.png)
![2022 10 10-18 20
00](https://user-images.githubusercontent.com/94164348/194977192-0b93346e-cea0-4fb2-8b66-5ae7319ec3f1.png)

![dreamseeker_Ht2YcvyQbH](https://user-images.githubusercontent.com/94164348/194977254-d0b25aba-ec6b-4e8b-bad5-949a9961cf07.png)

![dreamseeker_KAB6kPSLrP](https://user-images.githubusercontent.com/94164348/194977259-561f8d97-962e-4545-a4b7-1637ad1a7156.png)

![dreamseeker_8Xe7Cuq6NH](https://user-images.githubusercontent.com/94164348/194977262-fb125315-2508-4022-9eda-5ed5078442c9.png)

![dreamseeker_SKJXeK9SOt](https://user-images.githubusercontent.com/94164348/194977268-b4efcd99-0896-4209-8b83-c61c086bda65.png)

![dreamseeker_6Ak0bNoVe5](https://user-images.githubusercontent.com/94164348/194977270-367aaf92-5d6d-4cd8-9827-eba99ec92080.png)

The town is an mostly empty place formerly devoted to tourism and the
beloved art of "chilling out". Facets of the life of its inhabitants
before their disappearance included drinking, grilling, and swimming off
the coast of their fairly large beach. Many interesting things happened
on the boardwalk, and a landing pad was present to allow for small ships
to dock inside the town.

The loot list is sparse here. I intend for this to mostly be a setpiece
for roleplay instead of a loot pinata. There's a good selection of
hydroponics seeds and gear, 2 full bar kits, basic kitchen equipment, an
autolathe, a few PDAs, a lotta wood, and a jukebox. Also donuts.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] Ruin spawns, nothing is out of whack that shouldn't be.

## Why It's Good For The Game
Continues the trend of making planets more good by adding more content
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An oddly empty town has been spotted on beach planets in the area.
Check it out spacers.
add: Random donut spawners, never eat the same donut two days in a row!

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
## [jupyterkat/Shiptest](https://github.com/jupyterkat/Shiptest)@[babf89eb74...](https://github.com/jupyterkat/Shiptest/commit/babf89eb746741ba4f33f686b0c4750fe68e1603)
#### Tuesday 2023-12-05 22:40:37 by The-Moon-Itself

SubShips attempt 2 (#1627)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Accidentally destroyed my old PR for this, #1573, by completely botching
a merge from master to the point that it was easier to make a whole new
fork than try to save it, so here we are again. Here's the original
description:

Ports the parts of beestation/beestation-hornet#7152 that adds the
framework for ships to land on top of each other and not break
everything. A ship can only land on another ship if there's an open
docking port on the mothership that's large enough for the subship.
Here's a video of it in action on a modified dwayne-class:


https://user-images.githubusercontent.com/51838176/195471361-f9f0d145-d7c9-480e-ad4a-d18705f2590f.mp4

This system should be able to handle just about any orientation of ships
on top of each other, such as ships landed across areas, multiple ships
landed on a single ship, a single ship landed on multiple ships, a ship
that is only partially landed on another ship, a ship that is partially
landed on a ship that's partially landed on another ship, and so on.
Just make sure that you never try to land a ship on itself.

Something to note for this is that ships remember what's underneath them
via baseturfs, and there's a hardcoded check that will cause errors if a
baseturf list grows over 10 entries long. Because ship turfs have
typically 1-3 baseturfs, after about 3 ships stacked on top of each
other things will start to break.

You can also make maps with subships on them, to do this, follow these
steps:
1. make the subship as if it were a regular ship in its own map file
2. create a new /datum/map_template/shuttle subtype that points to your
subship map, these datums can be found in code/datums/shuttle.dm
3. On your main ship, place "subship dock" landmark in turf where you
want the bottomleft corner of the subship's bounding box to be, you can
also use the offset_x and offset_y vars on the landmark to offset this
corner if you need to place the landmark somewhere else.
4. Set the "subship_template" var on the landmark to the path of your
subship's map_template subtype
5. Optionally change the dir on the landmark to rotate the subship. for
reference, NORTH is no rotation, EAST is a 90 degree clockwise rotation,
etc.

You can put the stationary docking port anywhere on your map, as long as
it's on the ship. You can have its bounding box hang off the side of
your ship, but please try to keep the entirety of its bounding box
within the bounding box of map file, otherwise subships landing on your
main ship might accidentally clip through structures nearby your
mainship, including virtual z level borders.
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
Subships allow for many more creative designs and interesting dynamics
between and within ships, especially when a crew may need or want to
split its attention between multiple locations at the same time, or to
make interactions between ships easier when you just need to land a
smaller vessel inside of the other, cutting out the need to travel
through space turfs to get between two ships.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Subships are now possible
code: Lots of large changes to ship code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [antiface/SeasonsOfTheHeart](https://github.com/antiface/SeasonsOfTheHeart)@[fd5278e671...](https://github.com/antiface/SeasonsOfTheHeart/commit/fd5278e671fb14196def45b176775354b4ca0091)
#### Tuesday 2023-12-05 22:52:29 by A.G

Update README.md

Added content about the "Seasons of The Heart", like the main seasons, i.e. "Winters of The Soul", "Springtime of My Life", "Summer of The Heart", and "Autumn of Atonement", plus my "simple truths of the heart", namely, "The Heart Alone Knows Truth", "The Heart is of Resolve", "The Heart's Calling is To Love", "The Heart Alone Knows Peace", and "The Heart's Purpose is To Give". Need to re-arrange the content, though, so it is in the right order, an order that makes sense and looks good and refreshing, and illuminates.

---
## [YanniZ06/z-audio-backend](https://github.com/YanniZ06/z-audio-backend)@[24fdfa9675...](https://github.com/YanniZ06/z-audio-backend/commit/24fdfa96753077ff6ad5367d26fea978e4e63a3f)
#### Tuesday 2023-12-05 23:01:57 by YanniZ06

Restructuring, everything! (Im sorry :trollface: )

- SoundFXLoader has been renamed to Sound_FxBackend for more clarity on its functionality

- handles has been renamed to al_handles for more clarity

- put everything efx related into a folder named, suprise, "efx"

- gave Effects and Filters "load" and "unload" functions
-> unlike new and destroy these only handle the AL EFX extension side of operations and can be used for better memory management

- Seperate Folder dedicated to decoder

- Seperated MiniMP3 cpp code from actual MP3Decoder implementation
-> CPPContentMacro to obtain cpp file content and insert when necessary, if it worked at least
-> for now MiniMP3.hx with the code injected that MP3Decoder extends for better visiblity works aswell

- ZAudioHandler has been split up into various classes properly, all located inside the 'manager' folder

- New sound setting 'autoLoadFX' to control whether fx should automatically be loaded or not

- probably a bunch more im missing right now but its almost midnight so i cant remember

!!!! TODO:
- make sure filters are seperated between initialization and loading in similar to effects, if we will go the memory save route we will go all out!!

---
## [Wolf3s/pcsxr-360](https://github.com/Wolf3s/pcsxr-360)@[6cb5f8453f...](https://github.com/Wolf3s/pcsxr-360/commit/6cb5f8453f327d0e1762f53585faf967271a89b0)
#### Tuesday 2023-12-05 23:13:29 by Wolf3s

v2.1.0

* 2 Variants
    - Base 2.1.0 version.
    - CTR-Fix version.

* Changelog:
    - Just one build, no more old and new cdr plugin builds, everthing is in a single default.xex.
    - Fixed text encoding issues on the end of the text, when the game guide is loaded (Byte order mark issues).
        Still, remember to set any gameguide text on notepad to unicode big endian format (File->save as, then change from ansi to unicode big endian, then save the gameguide.txt).

    - Compatibillity
        - CDDA games are working fine and the compatibility was maintained (Noticiable in games like Dead or Alive Series).
        - Added cpu bias option.
            Turning this option "on" will make the emulator run faster, setting the bias in the core to "3", but it will underclock the psx cpu.
            It's good for some games that dont use the full psx power, most 2d games or some 3d games with less cpu demand like brigandine.
            Heavy cpu games (tekken 2,3) will suffer from a lot of slowdowns.

    - UI
        - Added option to exit to dash on main menu (right thumb click button).
        - Added linear filter options (again).
        - Fixes the "B" (Back) button, now it correctly returns to the main menu.
            On previous version, this button was used to load the profile settings, sorry for my stupidity :P.

    - Regression/Freeze Fixes:
        - Soul Calibur (when you finish the game).
        - Tomb Raider 3 (when entering on ingame menu and try to return to the game again).
        - Brave Fencer Musashi (voices).
        - Valkirie Profile (BGM).
        - Front Mission 3 (Random freezes in the main menu and during battles, when your wanzer or the enemy wanzer has the legs smashed).

---
## [TheOldRealms/TOR_Core](https://github.com/TheOldRealms/TOR_Core)@[405f716420...](https://github.com/TheOldRealms/TOR_Core/commit/405f71642027480d790db27ea4a9a79386ca8efd)
#### Tuesday 2023-12-05 23:25:03 by Linus Tiemann

vampire count done

required charge is doubled
Spell damage is not able to charge ability anymore
new blood changed life regeneration perk to winds of magic
added feral line: physical damage and health+ health regeneration
Changed lordly 1 from movement speed to companion limit
arkayne is not regenerating winds of magic anymore. Instead it allows to charge ability by Spell damage with 90% reduced power.

Fixed and reworked completely mistform. It will not take horses with you and the collider box is much more sharp. It should not be able anymore to drop out of the ability "sphere".

---
## [anatman-org/prime](https://github.com/anatman-org/prime)@[6c8c8dd74f...](https://github.com/anatman-org/prime/commit/6c8c8dd74f76c783dc6d3fa6d63cb1068e0187cf)
#### Tuesday 2023-12-05 23:25:09 by Thornton Prime

everything is stinking without you
and i miss you when you're gone

everything like this ...

bullshit that is assembled by my brain
when i'm not paying attention

it is the real fiction

the only thing that was real
was the coincidenting

all the words
all the ideas
all the falling-together puzzle pieces

fell together in my zombie brain

all that was auto-pilot

i was always just thinking

Her

---
## [SkuratovichA/ims](https://github.com/SkuratovichA/ims)@[9eaa9ce8bd...](https://github.com/SkuratovichA/ims/commit/9eaa9ce8bd60c3e9c6a918c55d9ae4cc22839f70)
#### Tuesday 2023-12-05 23:26:14 by Aliaksandr Skuratovich

Implement differential equations & run the simulation (#4)

* implement differential equations struct, map stupid functions

two soltions:
1. either do macros (not desired)
2. do some weird stuff with FunctionN and otcher stuff.

Decided to do a smarter solution, because macros will be a hell to debug.
fucking c++ :)

* fuck prettier

* refactor

* simulation is runnable

---
## [Rystic/ATLA-restored](https://github.com/Rystic/ATLA-restored)@[ba162adace...](https://github.com/Rystic/ATLA-restored/commit/ba162adace3bb96f77c8d92d1d12eb5aa4bbf50a)
#### Tuesday 2023-12-05 23:45:41 by Stocky Kruegar

description for changelog

-Color coded Bender text for Bloodlines
-Filled in Roku, Sozin & Aang's, Chaejin(saowan), Kuvira's  bloodlines
-Fixed missing icons for several bloodlines including above
-Removed duplicates loc & (mainly sand society & avatar events )
-Fixed missing opinion localizations
-Added in missing Sun Warrior, Saowan Bloodlines
-Added image to tea society event
-Fixed tribal sand loc
-Sun Warriors now receive the 'Sun Warrior'  bloodline if they meet all prereqs (sun warrior faith, culture firebender etc), this is obviously inherited but just added incase the AI's dynasty dies out.
-One Nation Empire Bloodline now has its correct flag

---
## [SpartanKadence/Citadel-Station-13-Kade](https://github.com/SpartanKadence/Citadel-Station-13-Kade)@[fb9c40f675...](https://github.com/SpartanKadence/Citadel-Station-13-Kade/commit/fb9c40f6752f19e293da244c45e48dabb9236320)
#### Tuesday 2023-12-05 23:54:18 by SpartanKadence

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

