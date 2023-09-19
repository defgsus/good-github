## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-18](docs/good-messages/2023/2023-09-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,322,314 were push events containing 3,548,369 commit messages that amount to 291,215,425 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[a321623971...](https://github.com/ZephyrTFA/tgstation/commit/a321623971250cc9e0abee5377cffef2de784b4e)
#### Monday 2023-09-18 00:35:06 by ArcaneMusic

Conveyor Belts are now easier to extend and have screentips (#78278)

## About The Pull Request

Conveyor belt **stacks** now have a better examine text.

Using a conveyor belt stack on a placed conveyor belt now extends the
conveyor belt by 1 tile, linking to it's ID automatically, and makes for
much easier building of conveyor belt setups.

Conveyor belts now come jam packed with screentips.

I've also added the default tile place sound to the usage of conveyor
stacks to provide a tiny bit of audio feedback when placing new conveyor
belts.

## Why It's Good For The Game

Conveyor belts are just mind-numbingly annoying to use in a regular
round, and trying to set up a new conveyor belt setup is confusing if
you don't have ultra specific information about how to make one before
you even start. Hell, I remember I had to add the *real* construction
steps to the wiki like 6 years ago and I STILL hear people getting
confused about how these works.

This improves their ease of use, while also making everyone sleep a
little easier for those of us who use them.

## Changelog

:cl:
qol: Conveyor belts now have screentips and a better examine tip to
teach you how to set one up properly.
qol: Using a conveyor belt stack on a placed conveyor belt will extend
the conveyor belt to the output of that conveyor belt.. You can use this
to place fully integrated conveyor belts much easier now.
/:cl:

---
## [Greenjoe12345/Aurora.3](https://github.com/Greenjoe12345/Aurora.3)@[652a3d02d4...](https://github.com/Greenjoe12345/Aurora.3/commit/652a3d02d4260aea7f34c64814f409a677b063a0)
#### Monday 2023-09-18 00:41:58 by Wowzewow (Wezzy)

Adds Storage Container Animations (#17329)

* Much ado about the Bagginses

* god i hate manually mapped shit

* Update code/game/objects/items/weapons/storage/storage.dm

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>

* fixes

* yes

* Update code/game/objects/items/weapons/storage/bags.dm

Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---------

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>
Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[dd8d13d8bc...](https://github.com/lessthnthree/tgstation/commit/dd8d13d8bcc6f1fbd6bcdd534a044f7d30c800d7)
#### Monday 2023-09-18 00:52:33 by carlarctg

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
## [567Turtle/cmss13](https://github.com/567Turtle/cmss13)@[5c4b13863f...](https://github.com/567Turtle/cmss13/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Monday 2023-09-18 00:56:56 by ihatethisengine

Larva surge is limited by marines/xenos ratio (#3592)

# About the pull request

Xenos after hijack now get larva based on marines/xenos ratio. Instead
of infinite larva, larva surge will try to increase the initial amount
of xenos on hijack to 50% of marines forces over time (with a minimum of
5 larvas, if xenos already have good numbers).

# Explain why it's good for the game

Initially, if I remember correctly, larva surge was brought into the
game to discourage marines from early meta-evacuations, which is fair.
But consequently, it really hurt the hijack sequence. Even if marines
evac fair and square, larva surge still comes in action and makes
situation for marines even worse, utterly discouraging everything but
either boomrushing the Alamo or holding lifeboats to evac.

This resulted in hijacks being very repetitive and boring. More than
that, larva surge is extremely busted on lowpop due to the fact you can
get around 20 xenos from nothing, making lowpop hijack even less
interesting. So with this change marines will still get punished for
evaccing with good numbers, but won't be penalized as much for honest
evacuations.

So hopefully, we will see more variety of hijacks and more interesting
stories!

P.S. if you have a better formula, let me know.


# Testing Photographs and Procedure
<details>
My friend @Diegoflores31 tested this for me, thanks!
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: larva surge is limited by marines/xenos ratio
fix: xenos no longer get free larva from abandoned facehuggers during
hijack
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: fira <loyauflorian@gmail.com>

---
## [SkullNightMegaFan/DarkRoot](https://github.com/SkullNightMegaFan/DarkRoot)@[1bc2c3e386...](https://github.com/SkullNightMegaFan/DarkRoot/commit/1bc2c3e386ae223337e6369d81f43b04bc3d5624)
#### Monday 2023-09-18 00:58:25 by BrentonFigures-Mormon

Minor Edit to Assest List

Joy did a fantastic job with the assest list, very thankful for their hard week. I know we can get way more done, but these are the bare essentials for the game. In addition, life happens. This game isn't a dedicated project, it's for a class. Of course, we're going to elevate the concept and make it awesome, but it's not a guaranteed time commitment. I want to focus on finished and functional before worrying about putting out the next big hit.

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[3c661fb538...](https://github.com/vampirebat74/lobotomy-corp13/commit/3c661fb5388400a09d848460399d73dbd4ffa852)
#### Monday 2023-09-18 01:56:15 by Mr.Heavenly

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

---
## [lovegaoshi/azusa-player-mobile](https://github.com/lovegaoshi/azusa-player-mobile)@[397b1bf6e9...](https://github.com/lovegaoshi/azusa-player-mobile/commit/397b1bf6e92063418fcc82beb513b096c0b4a72f)
#### Monday 2023-09-18 02:03:04 by unknown

feat: draw over other apps permission

havent decided where to put them yet but very useful nonetheless!
use checkDrawOverAppsPermission somewhere in settings. i fucking hate wechat and their pactise of putting a permanant notification asking for this permission to be enabled. no means fucking no you piece of shit

---
## [yonatan007ziv/WhatsDown](https://github.com/yonatan007ziv/WhatsDown)@[e4002e889d...](https://github.com/yonatan007ziv/WhatsDown/commit/e4002e889d75df37f5a92a1b00c5a07da0297f6d)
#### Monday 2023-09-18 02:06:50 by Yonatan Ziv

finally using DI Container correctly for the server

No more dumb ServiceLocator :space_invader:
todos:
- implement IDatabaseExtractor (implements pure queries) and IDatabaseAnalyzer (uses the extractor and analyzes according to the program's needs)
- Hashing and Salting services (salt using MD5 probably)
- make goofy ahh xaml frontend look better

probably need to refactor the Factory for the client, I have no idea it's like 5 am just do some magic refactoring for the server because currently it's kinda shit, the wpf is good though I think

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[cff11bb8fa...](https://github.com/treckstar/yolo-octo-hipster/commit/cff11bb8faaa07a74c83dc3b7b22025767b4784e)
#### Monday 2023-09-18 02:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[2fc01ad8be...](https://github.com/FalloutFalcon/Shiptest/commit/2fc01ad8be958492a38b3200023b8aa0c4bad9f5)
#### Monday 2023-09-18 02:23:44 by Skrem_7

Skrem's Quick Ballistic Glanceover (#2354)

## About The Pull Request

If maintainers want me to shorten the changelog, I can, I tend to start
there so I know what to talk about up here.

What started as a PR meant to buff up rubber rounds ended up turning
into a general passover I gave to much of the syntax and presentation of
ballistics. PR doesn't actually change that much function-wise, but it
changes a lot of lines due to a lot of changed pathing to better
establish consistency within ballistic code as well as overviewing a lot
of descriptions, names, and inherit moments.

Functionally, less-lethals and sniper rounds have been changed the most
by this PR. To a lesser extent, .38 special and shotgun rounds have been
tweaked. Finally, the PR stamps out a missing sprite bug with the WT-550
magazines, buffs up the surplus rifle (yeah, that old thing), tinkers
with some projectile speeds, makes match rounds slightly better, and
goes over A LOT of descriptions. I apologize for the massive wall of
text that's to follow.

Will take a look at energy weapons when I feel like it (might kill
disablers, I don't like mapping though).

## Why It's Good For The Game

### Slug and Pellet Changes
The pellet changes are actually just systemizing what was supposed to be
intentional design according to code comments, it just hadn't reached
every single pellet-based shotgun projectile. The improvised shell buff
is to make it not a potential complete whiff because RNG mechanics are
generally bad and not fun to play with.

### Less-Lethal Changes
Several implementations of less-lethal (rubber) ammunition on shiptest
are strictly worse than their standard alternatives. While this isn't a
PvP server, it feels very not-fun meta-wise to POTENTIALLY arm for SOME
insubordination and still fire what may as well be a round that bleeds
someone out (as they'll cause bleeding anyway). Increasing the stamina
damage on each of these makes it so they actually have a vague trade-off
(maybe stamina damage can do something like slow simplemobs in the
future, I don't know, I'd love to do it but simplemob code makes me
screech).

To make them not directly better in PvP and not the staple of taking
down the Super Scary Syndicate Shocktrooper Guy, they've had their
negative AP doubled. Not as good against combatants, but still perfectly
adept, if not better at general riot control against civilians. Makes
sense and puts them in their niche a little better.

### .38 Changes
The .38 special round relatively has more "power" and "velocity"
compared to the 9mm round, though it does not quite reach the levels
that .45 automatic or 10mm does in the IRL server. Furthermore, .38
special was specifically designed not to over-penetrate targets so as to
minimize the chance of collateral damage in police work. These are the
ultimate justifications behind giving it the worst AP out of all the
pistol calibers (-30, instead of -20) while still raising its damage to
25.

This should make the Winchester a better staple for taking out weaker
enemies such as legions or unarmored hermits, but it'll perform worse
against goliaths, frontiersmen, and the like. All-in-all, a more
"early-game" caliber, if you will, which is kinda what it's always been.

### Projectile Speed and Match Changes
Match rounds don't really exist as far as I've seen. That being said,
they're meant to be of higher quality, so their getting slightly higher
AP and speed makes sense, even if they're mostly just a meme round.

The speed increase of DMR/sniper rounds is primarily meant to
differentiate them better from AR rounds beyond having 20 more AP.
Assault rifles so far have pretty much dominated with better magazine
size, fire rate, and the exact same force as the DMR calibers, just
doing less damage against armored targets (doesn't matter too much when
you can just vomit rounds). I'd like to buff up the DMR damage even more
(sniper is fine), but I'd rather get some feedback on changing them to
35 baseline before doing so.

The speed decrease on shotguns is meant to cement them as CQC weapons.
Slugs are heavy. Shotguns are meant for close range. It's not much, but
it's thematically a good way to keep them in their lane, not that
they're even that problematic, hence only the slight change.

### Sniper Rifle Knockdown Change
Having a big-ass bullet that does 70 damage with 50 AP hit you is
already a middle finger. Making it potentially knock off an arm or a leg
is another middle finger. Being hardstunned for ten seconds after is the
icing on the cake. Changed it to a knockdown because we hate ranged
tasers.

### Surplus Rifle Fire Rate Buff
This thing is a joke. I haven't even seen it on the server, but I'd
rather make it vaguely competitive considering 10mm isn't super deadly
and only otherwise exists on the stechkin or the one Inteq SMG that you
never see (Colossus-only).

It's still clunky and terrible, but it should be less comedic and more
of a potential option if you have NOTHING else (will never happen).

### Boarder Magazine Change
Top-loading magazine fits into a standard assault rifle? No. Doesn't
make sense. Someone should probably just kill this gun, it's stupid and
looks stupid last I checked.

### WT-550 Magazine Fix
Don't think I've seen anyone use this weapon, I've only printed out
their magazines to dump AP rounds into my NT-SVG carbine. Noticed they
were invisible then. Someone increased their capacity to 30 without a
care for how its update_icon works. Not cool. Anyway, fixes are good.
Moving on.

### Syntax, Description, Spelling, and Overall Presentation Changes
Something very important when maintaining code is generally keeping
consistency in how things are not only presented, but how they're stored
as well. While I'd love to do EVEN more in the method of refactoring to
better align how so much of gun code works, this was something I wanted
to keep as a one-day project, so I mostly tinkered with pathing,
inherits, and groupings.

In the avenue of spelling and description changes, that's just 1)
Cleaning up errors that PR authors and maintainers missed and 2) Making
things more concise and just... better. Some of the SolGov descriptions
were a real headache to look at, and not because of the frequent
spelling and syntax errors.

Whoever misspelled and caused an entire series of items to be
/obj/item/gun/ballistic/automatic/assualt may wish to avoid any crows
for the next three months.

Perfectly willing to adjust or reel back some of my descriptions if
someone can offer something better than what I've written out if there's
some soul they REALLY want to keep.

## Changelog

:cl:
tweak: The NT 'Boarder' ARG now loads standard P-16 magazines, rather
than the M-90gl toploaders.
balance: .38 special does 25 damage up from 20. AP has been reduced to
-30 from -20.
balance: Standardizes pellet projectiles to lose 10% damage of both
types per tile across the board. Improvised pellets no longer have a
hardcapped 1-8 tile range.
balance: Less-lethal rounds now do 50% more stamina than the force of
their lethal counterparts, with 25% the normal force and double the
negative AP. If the round had positive or zero AP, it was subtracted by
20.
balance: Shotgun slugs do 40 damage, down from 60, but have zero AP,
rather than -10. FRAG-12 and meteor slugs have had their damage adjusted
to reflect their relative force.
balance: Surplus rifle fire_delay has been cut to 1 second from 3.
balance: .50 BMG knocks down instead of hardstunning.
balance: Any DMR, match, or sniper round now travels slightly faster
than other bullets. Shotgun slugs and pellets now travel slightly slower
than other bullets.
balance: Match rounds have had their AP slightly increased.
fix: Fixed WT-550 magazines not displaying properly.
spellcheck: Went over (almost) every single ballistic description,
including the guns themselves, magazines, ballistic casings, and speed
loaders/stripper clips to not only have better consistency and
readability, but also be more clear on the general effectiveness of each
caliber.
spellcheck: Assualt is gone.
code: Repaths/renames most ballistic ammo pathing to maintain
consistency or take advantage of inherits, when possible.
/:cl:

---
## [Drillur/LORED](https://github.com/Drillur/LORED)@[9d12851347...](https://github.com/Drillur/LORED/commit/9d1285134730a546de65f6266b15a7ffa18fdb87)
#### Monday 2023-09-18 02:54:07 by Drillur

EARNINGS REPORT FINISHED

WOOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!!!!
YEAAAAAAAAHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Now the player can look at the highlights (or entire report) with cheeky character dialogue every time they come back to the game! It's cute and funny.

At the bottom, you can say either "Thank you!" or "Shut up." There is no purpose to that. But it will grant Joy or Grief.

All right, that took a long time! What's next? Idk! I have to go to bed! Cya later!

---
## [ubipred/QFG5Patcher](https://github.com/ubipred/QFG5Patcher)@[fc376aa507...](https://github.com/ubipred/QFG5Patcher/commit/fc376aa5074ac33e13aa7a63dccaeac54923f0ab)
#### Monday 2023-09-18 03:50:22 by ubipred

QFG5Patcher patch v1.0.1.20

- Added a home-made translation tool, so that QFG5 can be translated into new languages! :)
- Added fan-made czech subtitles & texts for QFG5! (Entirely translated by gtpmax. Thank you for your amazing contribution my friend ♥)
- Fix exception causing the tool to be almost unusable for new users
- Huge refactoring of the QFG5Patcher's localization system
    --> QFG5Patcher language can now be changed at runtime!
- Fix missing dependencies for the setup bootstrap, since Microsoft has removed them from its website
- [QFG5] Fix crash when opening the keyboard mapping menu, this bug was introduced in QFG5Patcher v1.0.1.18
- Fix intro video download failing due to deprecation of SSL on the hosting server (added support of TLS 1.2)
- Added support for QFG5 Demo
- Customization options added!
    --> Added a CHEAT MENU with options to :
        - Disable Weight system
        - Disable hunger system
        - Activate Unlimited Health
        - Activate Unlimited Stamina
        - Activate Unlimited Mana
        - Activate Game's time speed modifier (to accelerate, slow down or even reverse the clock)
    - Add a customization field to let the user define the maximum skill points limit. (default was 550 for Strength and Defense, and 500 for everything else)

---
## [Mannilie/BattleForge](https://github.com/Mannilie/BattleForge)@[563ac4abdf...](https://github.com/Mannilie/BattleForge/commit/563ac4abdfab950e0a3b3d2c23d3a208f82ed52f)
#### Monday 2023-09-18 05:17:33 by Manny Vaccaro

Upgraded materials of packs to URP (fuck you bryan)

---
## [zecKR/zechub](https://github.com/zecKR/zechub)@[d0e6c4e52a...](https://github.com/zecKR/zechub/commit/d0e6c4e52a56469c12efaab400e1ec754114e230)
#### Monday 2023-09-18 05:45:13 by Hardaeborla

zecweekly58.md

# ZecWeekly #58

Brazilian Crypto Streamer Loses Funds, Ripple's legal team opposes SEC Appeal, FTX's SOL Should Be Distributed to Customers






Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello Zcash enthusiasts! Welcome to an exciting week where we bring you the latest cryptocurrency and Zcash Ecosystem updates. This week's newsletter includes a detailed tutorial on Zcash addresses, highlights from the second round of the minor grant program by the Zcash Foundation, and updates from the Zcash Community.

Join ZecHub as a newsletter contributor and earn rewards. Click the link to learn more. 👇
[Create ZecWeekly Newsletter](https://wiki.zechub.xyz/ZecWeekly-newsletter) 

---

## This Week's Education Piece 
If you're new to Zcash, you'll discover two transaction types known as transparent and shielded. For those following recent Zcash developments, you may also be quite familiar with Unified Address on the Zcash Network. The key question is how these addresses function on Zcash, especially in the context of transactions on the Zcash blockchain. 

Learn more about this via the link below 👇👇
[Visualizing Zcash Addresses](https://wiki.zechub.xyz/visualizing-zcash-addresses) 






## Zcash Updates


#### ECC & ZF Updates

[Zooko Will Be Speaking at Mainnet 2023 Event](https://twitter.com/MessariCrypto/status/1696289078743060668?t=BoeIGgLj-1E5a0gG3EmSyg&s=19) 


[Watch All Zcon4 Events Here](https://twitter.com/ZcashFoundation/status/1697683679017910761?t=O1BOX3KBRlhMa5O-1UySCw&s=19) 

[Download ZF August Newsletter Here](https://zfnd.org/zcash-foundation-august-2023-newsletter/) 

[Check Out What Happens To Your Private Data](https://twitter.com/ZcashFoundation/status/1696220390081630649?t=kR1czvJRrTwyRow3VUZhGg&s=19) 





#### Zcash Community Grants Updates

[ZF Minor Grants Program Round 2 Is Live](https://twitter.com/ZcashFoundation/status/1697683688543182961?t=q99lgXcT5yTvodQwXnTYgA&s=19) 

[Set Your Reminder For Zcash Dev Fund 2024](https://twitter.com/zerodartz/status/1696520352665604280?t=GUqwlspErtJtqlpQbH_Rgw&s=19) 


[Join Zcash Community Grants on Discord](https://twitter.com/ZcashCommGrants/status/1696965307376586818?t=wcyWJ76a1EBEM3NqX9WsaQ&s=19) 



#### Community Projects

[ZecHub Prop Is Up](https://twitter.com/dismad8/status/1696938238555074730?t=0Yb3-ZUaHnlXFIC5O459FQ&s=19) 

[Donate to "Taking Zcash To Schools" Program](https://twitter.com/OGA4SKY/status/1697400463170122019?t=YZY9lJs0TELKwXsA4Bz83g&s=19) 

[Using Zingo for Your Business](https://twitter.com/ZingoLabs/status/1696211862470230294?t=Krkokr7jE2hsgDuf0rn0og&s=19) 

[DWeb Camp Set To Happen in Ubatuba](https://twitter.com/zcashbrazil/status/1697612560969695382?t=Fcq2nX6Ed2Q52YUgZx_72g&s=19) 

[Taking Zcash To Schools In Nigeria](https://twitter.com/OGA4SKY/status/1696970219296600519?t=CWr0KJify-LyleO59bQvzg&s=19)

[ZFAVClub to Support DWeb Camp Event in Brazil](https://twitter.com/ZFAVClub/status/1697614302838919574?t=CTegZAaM3xLuszXeS78BpQ&s=19) 

[Connect, Participate and Share Your Podcast] (https://twitter.com/ZcastEsp/status/1697256155272368545?t=Crhrt2iQgRZ54ZxI1mczjQ&s=19) 

[Rise of Zec Chapter 6 by @zcashCrusader](https://twitter.com/ZcashCrusader/status/1696758204569735236?t=pCZ8EDpVvF_-_cEi7wb0ng&s=19) 

[PayWithZcash Proposal](https://twitter.com/zcashesp/status/1697271330771468600?t=W9rd0BmuO0IpDxojXxviJQ&s=19) 

[1st Edition of Free2Z Night](https://twitter.com/gordonesroo/status/1696578807254118624?t=wCEEiZAP7Kev63zJv4Kb7w&s=19) 

[Follow and learn more about Zcash Book Club](https://twitter.com/zcashesp/status/1697268356716359990?t=-bJB-XkhEf2Pi7RRemq38g&s=19) 

[Strategies Used by Free2Z to Record their Podcast](https://twitter.com/zcashesp/status/1697781752125698088?t=zzsWn-8jdFMebCdBEEL40g&s=19) 









 #### News & Media
[Brazilian crypto streamer loses funds due to accidental private key exposure - Cointelegraph](https://cointelegraph.com/news/brazilian-crypto-streamer-loses-50k-by-exposing-private-key) 

[Ripple legal team opposes SEC appeal over XRP decision - Cointelegraph](https://cointelegraph.com/news/ripple-legal-team-opposes-sec-appeal-over-xrp-decision)

[Solana Co-Founder Says FTX's SOL Should Be Distributed to Customers - Decrypt](https://decrypt.co/154663/solana-cofounder-says-ftx-sol-should-distributed-customers) 

[Digital rupee gets big usability boost through Yes Bank integration with UPI - Cointelegraph](https://cointelegraph.com/news/digital-rupee-gets-big-usability-boost-through-yes-bank-integration-with-upi) 

[Large Bitcoin Holders Accumulate $1.5B Worth of BTC as Price Wavers - Coindesk](https://www.coindesk.com/markets/2023/09/01/large-bitcoin-holders-accumulate-15b-worth-of-btc-as-price-wavers/?utm_medium=referral&utm_source=rss&utm_campaign=headlines) 

[Balancer protocol exploited for $900K as DeFi hacks mount - Cointelegraph](https://cointelegraph.com/news/balancer-protocol-exploited-for-900k-as-defi-hacks-mount-finance-redefined) 

[Robinhood Buys Back Sam Bankman-Fried’s Seized Shares Worth $600 Million - Decrypt](https://decrypt.co/154656/robinhood-buys-back-sam-bankman-fried-seized-shares) 

## Some Zcash Tweets
[Zcash is the Future](https://twitter.com/splitcoincom/status/1696582966867312770?t=fPvCQCwlU8bDgfiJz8SeQg&s=19) 

[Difference Between Monero and Zcash] (https://twitter.com/MKjrstad/status/1695814999405379672?t=tHO0cqpINCiv1XoqGr5s4w&s=19) 

[Zcash Shielded Assets is climbing!](https://twitter.com/zooko/status/1697306927813005653?t=FSMSsqrSuGKgf2-HkBI9Qg&s=19) 

[Top 5 Cryptos to Mine at Home](https://twitter.com/Cindy_Chando/status/1697849959968583840?t=UhAqpp31c6GNJg9gI9x0RQ&s=19) 

[Is Privacy The New Normal?](https://twitter.com/techmindsmentor/status/1697838511922241631?t=tczFIS7hSR-iZtCF-YID9A&s=19) 

[Bull Run for Privacy Coins?] (https://twitter.com/NagatoDharma/status/1697609324003045867?t=0EOMchNKit9pOuCnueCKog&s=19) 

[Bitcoin and Zcash in relation to z-address and t-address](https://twitter.com/ruzcash/status/1697830481381790120?t=lwf_XUkmsB3PuWapHXBXWQ&s=19) 

[Arnott Makes Donation with Zcash](https://twitter.com/aarnott/status/1697753434097938653?t=VlF4plbfsFoasDliSPvTIg&s=19) 

[I am a Zebra Man](https://twitter.com/yoditarX/status/1697739731595899157?t=ccumO9xFA8dMDFsqCBTEsg&s=19) 


[Zcash Featured by Zellic "Intro to ZK"](https://twitter.com/zellic_io/status/1697710984486678707?t=yFMnvjm8_5fS_Q2Lbk9s0Q&s=19) 

[Privacy will be always a trending & narrative](https://twitter.com/michae2xl/status/1697699658355609978?t=rkWQVQWaQaUvjDwy1Nc4BQ&s=19) 


[HODL Zcash] (https://twitter.com/SaveZcash/status/1697665858472972681?t=DxcueTnn7L9qvaVxAExqeg&s=19) 







## Zeme of the Week
[https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19](https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19) 


## Jobs in the Ecosystem

[2z Logo Designer] (https://free2z.cash/birdify/zpage/hiring-need-2z-logo-with-transparency) 

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [ogbigboss/a-wrinkle-in-rhythm](https://github.com/ogbigboss/a-wrinkle-in-rhythm)@[94bfdbbe8a...](https://github.com/ogbigboss/a-wrinkle-in-rhythm/commit/94bfdbbe8a5e00c2b7429f2775755605d4b6d59a)
#### Monday 2023-09-18 05:52:31 by Anand Mallik

look, I've been purposefully avoiding the news for nearly 18 months now in the hopes that it woudl help make me irrelevant to it. anyway I'll see what you CNBC and MSNBC fucks have to flash before my eyes in the afternoon or morning, I'm sure my dad will keep it on at some point before MNF

---
## [truongvantuan/NootedRed](https://github.com/truongvantuan/NootedRed)@[334dc21935...](https://github.com/truongvantuan/NootedRed/commit/334dc219356ac9931d9829aa46a7b50fee02b47e)
#### Monday 2023-09-18 06:48:17 by Visual Ehrmanntraut

Linux, fuck you

Fixes #167
Signed-off-by: Visual Ehrmanntraut <30368284+VisualEhrmanntraut@users.noreply.github.com>

---
## [yarigo/react](https://github.com/yarigo/react)@[ac1a16c67e...](https://github.com/yarigo/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Monday 2023-09-18 06:58:24 by Sebastian Markbåge

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
## [PestoVerde322/tgstation](https://github.com/PestoVerde322/tgstation)@[c968edab30...](https://github.com/PestoVerde322/tgstation/commit/c968edab306659606da4f39bc178851a5a24405c)
#### Monday 2023-09-18 07:27:40 by carlarctg

Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#77277)

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

---
## [PestoVerde322/tgstation](https://github.com/PestoVerde322/tgstation)@[dc6ddd821b...](https://github.com/PestoVerde322/tgstation/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Monday 2023-09-18 07:27:40 by Cheshify

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
## [Merek2/coyote-bayou](https://github.com/Merek2/coyote-bayou)@[a85eb92f6e...](https://github.com/Merek2/coyote-bayou/commit/a85eb92f6e80e4a5a6e94e95a9d382ca2e2baad8)
#### Monday 2023-09-18 07:43:43 by Tk420634

Turns down (for what) welding sound

yeah that bitch loud as shit

---
## [argrath/NetHack](https://github.com/argrath/NetHack)@[38cda5ad52...](https://github.com/argrath/NetHack/commit/38cda5ad52f47a810c44171e9081d0275401c516)
#### Monday 2023-09-18 08:41:33 by Michael Meyer

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
## [NPC1314/Skyrat-tg](https://github.com/NPC1314/Skyrat-tg)@[83f1f4b8bc...](https://github.com/NPC1314/Skyrat-tg/commit/83f1f4b8bca760df1d31219baf0252419d5255ea)
#### Monday 2023-09-18 08:45:45 by SkyratBot

[MIRROR] Polymorphic Inverter tweaks [MDB IGNORE] (#23162)

* Polymorphic Inverter tweaks (#77675)

## About The Pull Request

Fixes #77649

You can no longer use the belt to turn into any kind of carbon mob,
sorry gamers it was a cool dream but it leads to too many problems.
Also I made space dragon "there's an alive guy in my stomach" code now
work on signals instead of on Life tick which is slightly more efficient
and also resolves an issue with the funny belt.

## Why It's Good For The Game

Too much room for weird edge cases as a result of doing this (messing
with monkey DNA, producing infinite xeno organs, blocking legit xeno
queens from being created) which had no graceful solution.
Moving stuff off Life if it can be event based is nice.

## Changelog

:cl:
fix: Turning into a space dragon with the polymorphic inverter will no
longer leave you existing in two places
balance: You can no longer use the belt to transform into monkeys or
xenomorphs, for technical reasons.
/:cl:

* Polymorphic Inverter tweaks

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [alexxShandsome/MenuMaApp](https://github.com/alexxShandsome/MenuMaApp)@[c329320171...](https://github.com/alexxShandsome/MenuMaApp/commit/c329320171b1110303103e01eaec03c166e9e63d)
#### Monday 2023-09-18 09:24:20 by alexxShandsome

order: fucking stupid piece of shit, can do a simple href flawlessly in vite

---
## [brunerm99/nushell](https://github.com/brunerm99/nushell)@[fed4233db4...](https://github.com/brunerm99/nushell/commit/fed4233db4d81de00068ffa7cf1c0d09506bc150)
#### Monday 2023-09-18 09:37:52 by David Matos

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
## [lmichel/pyvo](https://github.com/lmichel/pyvo)@[a1a831d286...](https://github.com/lmichel/pyvo/commit/a1a831d28619ecb553399f819de68a2511288a23)
#### Monday 2023-09-18 10:50:45 by Markus Demleitner

Switching Interface, Capability and friends to new xsi:type handling.

Since this is a rather ugly hack, a few words of background:

It turns out that astropy.utils.xml completely discards all namespace
information.  That you can parse Registry/capability documents with it
in the first place is just because we only have local elements with
elementFormDefault=unqualified.  Ah well.

Given that, we can either do XML processing ourselves, properly managing
namespaces (which wouldn't be a terrible amount of work).  Or we ignore
namespaces and namespace prefixes, too.  Since I can't think of anywhere
that would be trouble in the current VO, this commit opts for the second
option.

---
## [MiriamCristinaZ/Portfolio](https://github.com/MiriamCristinaZ/Portfolio)@[60e7bbc4ff...](https://github.com/MiriamCristinaZ/Portfolio/commit/60e7bbc4ff926e8f1105bed2d773b9c32f56c4ac)
#### Monday 2023-09-18 11:11:49 by MiriamCristinaZ

Create README.md

# Welcome to My Coding Portfolio 🚀

Explore a world of innovation and creativity! Dive into my collection of coding projects that showcase my passion for technology and problem-solving. From web development and data analysis to software applications and more, this portfolio is a testament to my dedication and expertise.

👨‍💻 **About Me:**
I'm a motivated developer with a deep love for crafting elegant solutions to real-world challenges. My journey in the world of code is a testament to my relentless pursuit of excellence.

🌟 **What You'll Find Here:**
- **Web Development:** Stunning websites and web applications that bring ideas to life.
- **Data Analysis:** Insights drawn from data that drive informed decisions.
- **Software Projects:** Innovative software solutions designed to make life easier.
- **Collaboration:** Open-source contributions and teamwork that make a difference.

🤝 **Let's Connect:**
I'm always eager to collaborate and take on new challenges. Feel free to reach out for projects, discussions, or just a friendly chat.

📬 **Contact:** [Email Me](mailto:miriam.cristina23@yahoo..com)
🌐 **Portfolio Website:** [Explore More](file:///C:/Users/44779/Desktop/mynewwebsite/index.html)

Thanks for visiting, and I hope you enjoy exploring my world of code! 🌈

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[25b1203a97...](https://github.com/tgstation/tgstation/commit/25b1203a971ab7091abbe75cacfce1ba28b62a78)
#### Monday 2023-09-18 11:32:46 by Jacquerel

You can do revival surgery on Ian (#78288)

## About The Pull Request

Allows you to perform revival surgery on any mob which is organic or
looks humanoid.
This means yes: Corgis, Goliaths, ~~Syndicate mobs~~ not those because
they spawn human corpses and delete themselves.
No: Slimes, Ghosts, General Beepsky.

Splits revival surgery into a subtype used for "mobs" and a subtype for
"mobs with brains" as the former don't have any brains to damage.

Additionally by special request, Ian can now wear an eyepatch and will
automatically put one on if he is brought back from death.

![image](https://github.com/tgstation/tgstation/assets/7483112/eff91bf6-4f80-4d8b-9062-1a5d4af85d39)

## Why It's Good For The Game

Currently you revive dead pets either by creating a magical reagent out
of holy water or by buying a mining item which also brainwashes them,
however reasonably our skilled medical team should be able to put a dog
back together and now can.
When you fuck up one of the stages of Tend Wounds on a kitten and stab
it to death with your scalpel, now you can fix it.
Expands the possibilities of vetinerary roleplay.

## Changelog

:cl:
add: Many kinds of mobs can now be brought back to life through revival
surgery.
add: Dogs can wear eyepatches.
/:cl:

---
## [alphastrata/bevy](https://github.com/alphastrata/bevy)@[44f677a38a...](https://github.com/alphastrata/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Monday 2023-09-18 11:59:09 by Sélène Amanita

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
## [techwithnikki/Tour](https://github.com/techwithnikki/Tour)@[268c7cf2f7...](https://github.com/techwithnikki/Tour/commit/268c7cf2f7c3899cbc628fac7892cebc6ed92793)
#### Monday 2023-09-18 12:09:45 by Nikita Kumar

Add files via upload

Creating a tour and travel booking website is a bit different from developing a mobile app, but many of the same principles apply. Here are the steps to create a tour and travel booking website:

1. **Market Research and Planning:**
   - Determine your target audience and their preferences.
   - Research competitors in the travel booking industry.
   - Define your unique selling points (USPs) and business model.
   - Create a business plan and budget.

2. **Concept and Design:**
   - Create wireframes and mockups of your website's user interface (UI).
   - Design a user-friendly and visually appealing interface.
   - Plan the user experience (UX) for easy navigation.

3. **Choose a Domain and Hosting:**
   - Select a domain name that reflects your brand and is easy to remember.
   - Choose a reliable web hosting provider to host your website.

4. **Website Development:**
   - Develop the website using a web development framework or content management system (CMS) like WordPress, Joomla, or Drupal.
   - Implement responsive design to ensure your website works well on various devices and screen sizes.

5. **Features and Functionality:**
   - Implement core features such as search and booking functionality.
   - Include filters for destinations, dates, and preferences.
   - Integrate payment gateways for secure transactions.
   - Include user profiles and booking history.
   - Implement a rating and review system.
   
6. **Content Creation:**
   - Create high-quality content for destinations, tours, and travel tips.
   - Use compelling images and videos to showcase destinations.
   - Optimize content for search engines (SEO) to improve visibility.

7. **Booking System Integration:**
   - Integrate a booking system or reservation software to manage bookings and availability.
   - Ensure that the booking process is user-friendly and secure.

8. **Testing:**
   - Thoroughly test the website for functionality, usability, and security.
   - Fix any bugs or issues identified during testing.

9. **Launch:**
   - Prepare marketing materials and strategies for the website launch.
   - Ensure that the website is accessible to users.
   - Consider offering promotions or discounts to encourage bookings.

10. **User Support and Maintenance:**
    - Provide customer support for inquiries and issues.
    - Regularly update the website to improve performance and add new features.
    
11. **Marketing and Promotion:**
    - Create a marketing plan to attract users to your website.
    - Use digital marketing, social media, and partnerships to reach your audience.
    
12. **Feedback and Improvement:**
    - Gather feedback from users to understand their needs and pain points.
    - Use this feedback to continuously improve your website.

13. **Legal and Compliance:**
    - Ensure your website complies with data protection and privacy regulations.
    - Draft terms and conditions, privacy policy, and refund policies.

14. **Monetization:**
    - Determine how you will make money from the website, e.g., through booking fees, commissions, or premium features.

15. **Scale and Expand:**
    - As your website gains users, consider expanding your offerings to include more destinations, travel types, or additional services.

Remember that building and maintaining a successful travel booking website requires ongoing effort and attention to user experience, content quality, and marketing strategies. Providing a seamless booking experience and valuable information to travelers is key to your website's success.

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[f3a10af417...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/f3a10af4172b175bb0f896c3f0a00b432092f109)
#### Monday 2023-09-18 12:49:08 by Ruchit

(note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye

---
## [fabiankachlock/zwoo](https://github.com/fabiankachlock/zwoo)@[fbd0583293...](https://github.com/fabiankachlock/zwoo/commit/fbd058329329bfe9160dd300dfd8ac5fbd89f9d1)
#### Monday 2023-09-18 14:37:13 by fabiankachlock

Merge branch 'main' of https://github.com/fabiankachlock/zwoo into fix/i-hate-my-life

---
## [RengaN02/PsychonautStation](https://github.com/RengaN02/PsychonautStation)@[d1a7e2066c...](https://github.com/RengaN02/PsychonautStation/commit/d1a7e2066c449e1620fc6a93f1028539b82803a4)
#### Monday 2023-09-18 14:56:34 by LovliestPlant

Misc mapping fixes and QoL additions (#78176)

## About The Pull Request

fix: #78135
fix: #78059

This PR remaps Birdshot's disposals room, makes several small fixes on
Icebox and Metastation, adds cell timers to isolation cells where such
cells are present (they don't open the door, effectively just an in-game
timer) (in-cell flashes are now controlled with the timer, where
applicable); and adds translator glove modules to the stacks of
"accessibility" modules found in most security, medical, and engineering
storage rooms. (adds these stacks in their entirety to Northstar).

Specific changes are as follows:
Birdshot
- Adds a roll of package paper to the cargo office
- Translator module [med,sec]
- Accessibility modules [eng]
- Recycler remap

Delta
- Translator module [med,sec,eng]
- Isolation cell timer

Icebox
- Translator module [med,sec,eng]
- Remove duplicate hand labeler on the rack near brig cells
- Adds a hand labeler to armory desk in gear room
- Isolation cell timer

Meta
- Translator module [med,sec,eng]
- Isolation cell timer
- Mends a broken corpse disposal pipe from aux surgery to the morgue

Northstar
- Accessibility modules [med,sec,eng]
- Nudges the binoculars off of the mass driver controls in ordnance
- Fixes the SM starting out hotwired (Rewires the SM room)

Tram
- Translator module [med,sec,eng]
- Isolation cell timers
## Why It's Good For The Game

Bug fixes with respect to Birdshot's recycler, Meta's corpse disposal,
Northstar starting out hotwired, and Icebox's duplicated hand labeler.

Nudging Northstar's ordnance binoculars should make it a bit easier to
find the mass driver controls.

Adding some packaging paper to Birdshot to make the techs' lives a
little easier with a little less round-start fuss.

Adding a hand labeler to Icebox's gear room brings it in line with other
maps in terms of rounds-start gear and locker labeling potential.

For players with characters running the Mute/Signer quirks, stock
MODsuits are a pain to use. Suit gauntlets will replace their translator
gloves. Unless they're able to get a suit put together ahead of time,
they'll be stuck doing the retract gauntlets > send radio message >
Extend Gauntlets shuffle. Adding a translator glove module to the stack
of similar items (plasma fixation module / therma regulator) should
alleviate that issue some.

Getting abandoned in an isolation cell sucks, and setting timers on your
phone or some such is a hassle. Adding cell timers to isolation cells
should go some way to alleviating those frustrations.
## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->
<!-- To our mappers and spriters: Posting screenshots of content INSIDE
EDITORS (aseprite, PDN, SDMM, ect) is NOT valid proof of testing. Please
make sure that you COMPILE the game and provide PROOF you tested your
edits. -->

<details>
<summary>Screenshots/Videos</summary>

### Birdshot

Disposal Room Remap

![bird_jani_v2](https://github.com/tgstation/tgstation/assets/107971606/aecc805f-08c9-469c-9963-860822c75f63)
Cargo Packing Paper

![tg-bird-packingPaper](https://github.com/tgstation/tgstation/assets/107971606/c0330acf-c64e-4dc4-9879-c7d8ae6047c4)
Engineering Accessibility Modules

![tg-bird-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/ab055b28-2b40-453e-8850-1ceffb9c55ea)
Medbay Translator

![tg-bird-acc-med](https://github.com/tgstation/tgstation/assets/107971606/ecad5352-692d-4559-a1d3-4ee387fe449c)
Security Translator

![tg-bird-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/045fa684-29f8-4112-ba58-59b90c135103)

### Deltastation

Engineering Translator

![tg-delta-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/9289e303-e37a-4c11-b4c9-a6803cddcfd8)
Medbay Translator

![tg-delta-acc-med](https://github.com/tgstation/tgstation/assets/107971606/9a36819b-fbc4-4403-a0dd-199ba1c29cb3)
Security Translator

![tg-delta-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/1d62d0d1-c564-4bfd-ad53-e41147682cba)
Isolation Cell Timer

![tg-delta-iso](https://github.com/tgstation/tgstation/assets/107971606/2c1579f4-d1a9-4d98-8e81-29b1cf0719d7)

### Icebox

Engineering Translator

![tg-ice-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/9805b72e-cad6-4ddd-a7fd-adc271e6a341)
Medbay Translator

![tg-ice-acc-med](https://github.com/tgstation/tgstation/assets/107971606/8ab57572-0193-40c5-87ee-df95c7e5f9d8)
Security Translator

![tg-ice-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/e234a98f-f429-4ed0-b465-3b795b1ff0bc)
Isolation Cell Timer

![tg-ice-iso](https://github.com/tgstation/tgstation/assets/107971606/9a0a7dc1-e369-46c8-8061-9c4635a63b5a)
Gear Room Hand Labeler

![tg-ice-label-armory](https://github.com/tgstation/tgstation/assets/107971606/36a58996-ac69-4978-8c79-eaa2478ce457)

### Metastation

Engineering Translator

![meta-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/edbc746a-0c9c-4953-a744-1af064126c34)
Medbay Translator

![meta-acc-med](https://github.com/tgstation/tgstation/assets/107971606/a9b24f61-515e-40d1-b657-2a4b16920e51)
Security Translator

![meta-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/55b91615-765e-42fe-adab-1a12e145ef48)
Isolation Cell Timer

![tg-meta-iso](https://github.com/tgstation/tgstation/assets/107971606/3bf6825c-0242-4332-ba71-db953a2e3902)

### Northstar

Engineering Accessibility Modules

![tg-north-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/d32c1787-31e6-4ef7-964c-26eb87025888)
Medbay Accessibility Modules

![tg-north-acc-med](https://github.com/tgstation/tgstation/assets/107971606/fa3883f5-1e95-490a-b0b0-18ac08583221)
Security Accessibility Modules

![north-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/d9308760-ac2f-4ae2-b91e-9d8dbcaaf0fd)
Supermatter Rewiring

![sm_annotate_2](https://github.com/tgstation/tgstation/assets/107971606/7c127678-6a55-454b-8e82-b615b41f0bcd)
Ordnance Binoculars

![tgqol_Northstar_Binos](https://github.com/tgstation/tgstation/assets/107971606/ce214728-48bf-436d-981e-bac40f8ca205)

### Tramstation

Engineering Translator

![tg-tram-acc-eng](https://github.com/tgstation/tgstation/assets/107971606/55b9993b-60b7-4e04-9073-0c8b3e7d9189)
Medbay Translator

![tg-tram-acc-med](https://github.com/tgstation/tgstation/assets/107971606/f4ac7a88-e3b1-4e4a-9914-70620c625b75)
Security Translator

![tg-tram-acc-sec](https://github.com/tgstation/tgstation/assets/107971606/8460cacb-a30a-45d0-b2bd-6c8666434055)
Isolation Cell Timer

![tg-tram-iso](https://github.com/tgstation/tgstation/assets/107971606/334be379-f6e6-45f0-93e9-b0e2f5d30b94)

</details>

## Changelog
:cl:
qol: [Deltastation, Icebox, Metastation, Tramstation] Adds cell timers
to isolation cells. (they do not auto-open the doors)
qol: [Birdshot, Deltastation, Icebox, Metastation, Northstar,
Tramstation] Adds translator glove modules to the stacks of
"accessibility" (e.g. plasma fixation / thermal regulator) modules found
in security, medical, and engineering storage rooms.
qol: [Birdshot] Adds a roll of packaging paper to the cargo office.
qol: [Icebox] Adds a hand labeler to security's gear room.
qol: [Northstar] Nudges the set of binoculars covering the mass driver
controls in ordnance over a few inches.
fix: [Birdshot] Remaps the janitor's closet such that the recycling
machine will now work.
fix: [Icebox] Removes a duplicated hand labeler from the rack near
security's brig cells.
fix: [Metastation] Patches a broken corpse disposal pipe running from
aux surgery to the morgue.
fix: [Northstar] Fixes the SM being hotwired at round-start (partially
rewires the SM room, moves the APC to the North wall).
/:cl:

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[23a9fedbe1...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/23a9fedbe1d0bccb890a6434149074f624cbe13c)
#### Monday 2023-09-18 15:21:57 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: pix106 <sbordenave@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [parashar52/Evaluation-Project](https://github.com/parashar52/Evaluation-Project)@[3955b72cf3...](https://github.com/parashar52/Evaluation-Project/commit/3955b72cf3f5194c75e4a8b20e843d52ed6c3f5f)
#### Monday 2023-09-18 15:48:49 by Rahul Sharma

Add files via upload

Baseball Case Study
Project Description
This dataset utilizes data from 2014 Major League Baseball seasons in order to develop an algorithm that predicts the number of wins for a given team in the 2015 season based on several different indicators of success. There are 16 different features that will be used as the inputs to the machine learning and the output will be a value that represents the number of wins. 
-- Input features-
1.	W - This indicates the number of Wins credited to a pitcher: number of games where pitcher was pitching while their team took the lead and went on to win, also the starter needs to pitch at least 5 innings of work.
2.	R - This indicates Runs scored. A run is scored when a player advances around first, second and third base and returns safely to home plate, touching the bases in that order, before three outs are recorded and all obligations to reach base safely on batted balls are met or assured: number of times a player crosses home plate.
3.	AB - This means At bat or time at bat. It's is a batter's turn batting against a pitcher: plate appearances, not including bases on balls, being hit by pitch, sacrifices, interference, or obstruction.
4.	H - This means Hit. It's also called a "base hit", is credited to a batter when the batter safely reaches or passes first base after hitting the ball into fair territory, without the benefit of either an error or a fielder's choice: reaching base because of a batted, fair ball without error by the defense.
5.	2B - This means the act of a batter striking the pitched ball and safely reaching second base without being called out by the umpire, without the benefit of a fielder's misplay (see error) or another runner being put out on a fielder's choice. A double is a type of hit (the others being the single, triple and home run) and is sometimes called a "two-bagger" or "two-base hit": hits on which the batter reaches second base safely without the contribution of a fielding error.
6.	3B - This measns a Triple.It's is the act of a batter safely reaching third base after hitting the ball, with neither the benefit of a fielder's misplay nor another runner being put out on a fielder's choice. A triple is sometimes called a "three-bagger" or "three-base hit": hits on which the batter reaches third base safely without the contribution of a fielding error.
7.	HR - This means Home runs. It's scored when the ball is hit in such a way that the batter is able to circle the bases and reach home plate safely in one play without any errors being committed by the defensive team. A home run is usually achieved by hitting the ball over the outfield fence between the foul poles (or hitting either foul pole) without the ball touching the field: hits on which the batter successfully touched all four bases, without the contribution of a fielding error.
8.	BB - This means Base on balls (also called a "walk"). It occurs in baseball when a batter receives four pitches that the umpire calls balls, and is in turn awarded first base without the possibility of being called out: hitter not swinging at four pitches called out of the strike zone and awarded first base.
9.	SO - Also denoted as "K" means Strikeout. It occurs when a batter accumulates three strikes during a time at bat. It usually means that the batter is out: number of batters who received strike three.
10.	SB - This means Stolen base. It occurs when a runner advances to a base to which they are not entitled and the official scorer rules that the advance should be credited to the action of the runner: number of bases advanced by the runner while the ball is in the possession of the defense.
11.	RA - This means Run Average. It refer to measures of the rate at which runs are allowed or scored.
12.	ER - This means Earned run. It refers to any run that was fully enabled by the offensive team's production in the face of competent play from the defensive team: number of runs that did not occur as a result of errors or passed balls.
13.	ERA - This means Earned Run Average. It refers to the average of earned runs allowed by a pitcher per nine innings pitched (i.e. the traditional length of a game). It is determined by dividing the number of earned runs allowed by the number of innings pitched and multiplying by nine: total number of earned runs (see "ER" above), multiplied by 9, divided by innings pitched.
14.	CG - This means Complete Game. It's the act of a pitcher pitching an entire game without the benefit of a relief pitcher. A pitcher who meets this criterion will be credited with a complete game regardless of the number of innings played: number of games where player was the only pitcher for their team.
15.	SHO - This means Shutout. It refers to the act by which a single pitcher pitches a complete game and does not allow the opposing team to score a run: number of complete games pitched with no runs allowed.
16.	SV - This means Save. It's credited to a pitcher who finishes a game for the winning team under certain prescribed circumstances: number of games where the pitcher enters a game led by the pitcher's team, finishes the game without surrendering the lead, is not the winning pitcher, and either (a) the lead was three runs or fewer when the pitcher entered the game; (b) the potential tying run was on base, at bat, or on deck; or (c) the pitcher pitched three or more innings.
17.	E - This means Errors. It's an act, in the judgment of the official scorer, of a fielder misplaying a ball in a manner that allows a batter or baserunner to advance one or more bases or allows a plate appearance to continue after the batter should have been put out. The term error is sometimes used to refer to the play during which an error was committed: number of times a fielder fails to make a play he should have made with common effort, and the offense benefits as a result.

-- Output: Number of predicted wins (W)
To understand the columns meaning, follow the link given below to understand the baseball statistics: https://en.wikipedia.org/wiki/Baseball_statistics
For downloading the dataset, use the link given below. 

Dataset Link-
•	https://github.com/dsrscientist/Data-Science-ML-Capstone-Projects/blob/master/baseball.csv

Avocado Project
Project Description
This data was downloaded from the Hass Avocado Board website in May of 2018 & compiled into a single CSV. 
The table below represents weekly 2018 retail scan data for National retail volume (units) and price. Retail scan data comes directly from retailers’ cash registers based on actual retail sales of Hass avocados. 
Starting in 2013, the table below reflects an expanded, multi-outlet retail data set. Multi-outlet reporting includes an aggregation of the following channels: grocery, mass, club, drug, dollar and military. The Average Price (of avocados) in the table reflects a per unit (per avocado) cost, even when multiple units (avocados) are sold in bags. 
The Product Lookup codes (PLU’s) in the table are only for Hass avocados. Other varieties of avocados (e.g. greenskins) are not included in this table.
Some relevant columns in the dataset:
•	Date - The date of the observation
•	AveragePrice - the average price of a single avocado
•	type - conventional or organic
•	year - the year
•	Region - the city or region of the observation
•	Total Volume - Total number of avocados sold
•	4046 - Total number of avocados with PLU 4046 sold
•	4225 - Total number of avocados with PLU 4225 sold
•	4770 - Total number of avocados with PLU 4770 sold

Inspiration /Label 
The dataset can be seen in two angles to find the region and find the average price .
Task: One of Classification and other of Regression
Do both tasks in the same .ipynb file and submit at single file. 

Dataset Link-
•	https://github.com/dsrscientist/Data-Science-ML-Capstone-Projects/blob/master/avocado.csv.zip

HR Analytics Project- Understanding the Attrition in HR
Project Description
Every year a lot of companies hire a number of employees. The companies invest time and money in training those employees, not just this but there are training programs within the companies for their existing employees as well. The aim of these programs is to increase the effectiveness of their employees. But where HR Analytics fit in this? and is it just about improving the performance of employees?
HR Analytics
Human resource analytics (HR analytics) is an area in the field of analytics that refers to applying analytic processes to the human resource department of an organization in the hope of improving employee performance and therefore getting a better return on investment. HR analytics does not just deal with gathering data on employee efficiency. Instead, it aims to provide insight into each process by gathering data and then using it to make relevant decisions about how to improve these processes.
Attrition in HR
Attrition in human resources refers to the gradual loss of employees overtime. In general, relatively high attrition is problematic for companies. HR professionals often assume a leadership role in designing company compensation programs, work culture, and motivation systems that help the organization retain top employees.
How does Attrition affect companies? and how does HR Analytics help in analyzing attrition? We will discuss the first question here and for the second question, we will write the code and try to understand the process step by step.
Attrition affecting Companies
A major problem in high employee attrition is its cost to an organization. Job postings, hiring processes, paperwork, and new hire training are some of the common expenses of losing employees and replacing them. Additionally, regular employee turnover prohibits your organization from increasing its collective knowledge base and experience over time. This is especially concerning if your business is customer-facing, as customers often prefer to interact with familiar people. Errors and issues are more likely if you constantly have new workers.


Dataset Link-
•	https://github.com/dsrscientist/IBM_HR_Attrition_Rate_Analytics

---
## [AlghoulDEV/Alghoul-OS-1.0](https://github.com/AlghoulDEV/Alghoul-OS-1.0)@[c710b6a066...](https://github.com/AlghoulDEV/Alghoul-OS-1.0/commit/c710b6a066ba0b2bc50abff92e9d499beef99e9c)
#### Monday 2023-09-18 17:02:00 by alghoul_dev

Alghoul_OS_1.0.py

Welcome to Alghoul OS!

Explore and Enjoy Your Operating System:

Main Menu: When you start Alghoul OS, you'll be greeted by a main menu. Just press the Enter key to begin.

Apps: Choose from a variety of applications that are just a click away. Whether you want to download YouTube videos, translate text, count symbols, generate random numbers, set a timer, or automate sending messages, you're in control.

Games: Enjoy some fun games right here! Try your skills with "Card Clicker," and challenge your knowledge with "Guess the Flag."

Settings: Personalize your experience. Change the text color, select your preferred language, or explore system information.

YouTube Downloader: Want to save your favorite YouTube videos? Simply enter the video URL and choose where to save it.

Text Translator: Translate text to your preferred language. It's easy and quick!

Symbol Counter: Need to count symbols in a text? We've got you covered.

Randomizer: Get random numbers within a range of your choice.

Timer: Set up a countdown timer for any task you need to keep track of.

Auto Sender: Simplify repetitive tasks by automating text message sending.

How to Use:
To get started, just follow the prompts and enter your choices. To return to the main menu at any time, type "back" or "<-". You're in charge, so explore and enjoy Alghoul OS to the fullest!

Note: To exit Alghoul OS, type "stop," "0," "false," "close," "end," "exit," or "4" when prompted for input.

Start exploring and have fun with Alghoul OS!

---
## [Mjoonlight/MythosOfMoonlight](https://github.com/Mjoonlight/MythosOfMoonlight)@[aa109d6541...](https://github.com/Mjoonlight/MythosOfMoonlight/commit/aa109d6541b25298fa831153a59487531ba30a59)
#### Monday 2023-09-18 17:36:03 by Ebon1

guys wuh wun is ur favit Huggywuggy, Seek, Scary Bluue, Zumbo Sauce, BanBan, uh Nabnab, um I forgot his name the fwog dude and... um yeah, Slo Saleen, Babaleena, Stinga Flin, Opila Bowd, and Awesome Huggywuggy, this is me, but like I don't wanna use it, and blue and uh i mean um, Kissymissy, Killywvilly, um ChooChoo Charwuls, right Boxy Boo but like not evil, and we have Evil-a Boxy boo🧛 we have squidgame Huggywuggy, we have baby Haggywaggy, and Bluue, and Freddy Fazbear oink oinky oink oink🐷 we have Ceepy Green, we have um, happy Huggywuggy look how happ- he is, and we have um WHAT DA HELL BCH💥 BCH💥 we hav um nobody cares huggywu-

---
## [rive-app/rive-android](https://github.com/rive-app/rive-android)@[ae7d2eacc1...](https://github.com/rive-app/rive-android/commit/ae7d2eacc11c3b934df6985edad46d12230665a2)
#### Monday 2023-09-18 17:52:05 by HayesGordon

feat: add events on Android

Adds events on Android.

Topics for discussion and other considerations:
- Listeners
- URL events and us handling it automatically
- I opted to always return `properties` as a value (non nullable) and instead just return an empty map
- I'm also exposing a `data` on the `RiveEvent` which just returns all of the information as a map. Maybe not that useful but I left it in as I added that first for debugging.

Todo:

- [ ] Tests

## Listeners
Instead of adding it to the current `Listener` interface I instead created a new HashSet called `eventListeners` and expose two new methods `addEventListener` and `removeEventListener`.

For the following reasons:
- I think it'll be annoying to have to override all of the methods in the interface just to be able to use events
- Events replace some of these current handlers. `notifyStateChanged` is deprecated in Flutter and I'm assuming it should be for all of the runtimes.
- On Flutter (and similar discussion for web) we're exposing `addEventListener`/`removeEventListener` so there will be consistency.
- Our Interface approach makes deprecations difficult as you can't deprecat an overridden method (Or you can but it won't propagate down to the users. Same issue for iOS)

I'm not sure if there is a better way to structure the code considering that in its current form there is only one method in the interface: `notifyEvent`. But maybe that should be a consideration where instead of `notifyEvent` we expose:
- notifyURLEvent
- notifyGeneralEvent

The problem here is the same as above. If we ever add a new method it'll be a breaking change (unless we invoke the methods on the interface), and deprecations become difficult.

## URL Events
- Should we do this automatically for users? Or are examples enough? If we automatically open a browser when these events are triggered then should we expose a way to disable it from the animation object? You may want to disable it during debugging or some other reason.
- Is the `target` property needed on Android?

Diffs=
1f0ccae8d feat: add events on Android (#5894)

Co-authored-by: Gordon <pggordonhayes@gmail.com>
Co-authored-by: Umberto Sonnino <umberto@rive.app>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[696a8ab1fa...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/696a8ab1fa7d90f309b4f869fbedb73557665a05)
#### Monday 2023-09-18 18:37:43 by SkyratBot

[MIRROR] Only double HCR for impressive greentexts [MDB IGNORE] (#23778)

* Only double HCR for impressive greentexts (#78383)

There were a few exploits with free antags that would double your score.
This happened to me once by accident, but anyone could essentially
guarantee a point doubling.

I've changed the whole thing to only work for:
- Traitor
- Changeling
- Heretic
- Blood brother
- Headrev
- Wizard (you could get this with die of fate)
- Obsessed
- Magic and gun survivalists
- Holding the greentext book (because a cripple fighting for their life
for the greentext just seems funny and is rare enough)

Notably, revolutionairies, cult converts and brainwashed now no longer
pay out. Cult is pointless since you can't greentext without gibbing
(trust me I tried) and revolutionairy takes no effort other than having
strong teammates and doing nothing. There are a lot of other antags this
excludes, but those are mostly midrounds and non-humans (which are by
default excluded)

:cl:
balance: Only traitor, changeling, heretic, blood brother, headrev,
wizard, obsessed, magic/gun survivalists and greentext book holders can
now double their hardcore random score
qol: Redtexting as antag with hardcore random score will pay you default
points, instead of none (normal survival rules)
fix: End report screen will properly report hardcore random survival in
case of station destruction
/:cl:

* Only double HCR for impressive greentexts

---------

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [JRDead/tgstation](https://github.com/JRDead/tgstation)@[7f1d53e719...](https://github.com/JRDead/tgstation/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Monday 2023-09-18 19:08:16 by Ben10Omintrix

convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

---
## [JRDead/tgstation](https://github.com/JRDead/tgstation)@[b22ff1a4eb...](https://github.com/JRDead/tgstation/commit/b22ff1a4ebfd0a1dd1b75d6979edc73e6f4556b2)
#### Monday 2023-09-18 19:08:16 by Sealed101

Laser pointer update: Shining Through Walls Edition (feat. fixes!) (#77007)

# _PR PSA_


![augh](https://github.com/tgstation/tgstation/assets/75863639/6dc87fc7-65a3-4b7c-9b8d-a1432cacbe93)


## About The Pull Request
Cleans up code for laser pointers, fixing some bugs like the
forever-charging state or affecting dead cats along the way.
Remaining charge is now available upon examine.
Canonizes #45834 by implementing an upgrade to the laser pointers:
installing a bluespace crystal into a laser with tier 3 or higher laser
diode lets it shine through walls. Using an upgraded laser uses twice
the charge of a normal one. Of course, you can only shine it on
something if you can see the target behind the wall, like via x-ray or
thermals. Mesons don't count, however.
If one tries to jam a crystal into a pointer with a tier 1/2 laser (or a
tier 1/2 laser in a pointer with an installed crystal), _something_ will
get teleported, crushing the crystal.
You can uninstall the crystal with wirecutters or a hemostat. The
pointer will _hint_ on closer examination (`examine_more`) at a
possibility of a crystal being installed if you upgrade the laser
(different messages for tier 1/2/3,4).
Removes one stupid 1% increase for a recharge chance per process tick if
your laser was in a full recharge state because it was insignificant and
irrelevant.

i've had a branch for this for almost 9 months and i was always laying
it off for some day later. today i just completely fucked the branch.
whoops. i'm not even sure at this point what else did i fix while here,
double whoops

## Why It's Good For The Game
Closes #45834 - Canonizes a bug into a feature.
Fixes #77003 - lol
Cleaner code, possibly more robust even.
Seeing the remaining charge was not available at all and the only hint
was when you tried shining the pointer on something. That sucks.

## Changelog
:cl:
add: you can upgrade laser pointers with a bluespace crystal to let them
shine through walls at double the power cost, if the laser in the
pointer is of tier 3 or higher.
qol: laser pointer charge can be seen by examining it
fix: fixed laser pointers luring dead cats when shone upon
code: laser pointer code cleaned up a tad
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[56b37a6e3c...](https://github.com/Kapu1178/daedalusdock/commit/56b37a6e3c54cee460ae4b1c70970698a5e9370c)
#### Monday 2023-09-18 19:24:48 by Kapu1178

Random things on my todo list, mostly github related (#607)

* Makes the Haunted Eight Ball work(?) (better?) (#78196)

From my recollection the haunted eight ball has been "broken" for like 3
or 4 years. So uh... yea

Makes the Haunted Eight Ball actually, like, work good.

- Fixes all votes counting to 0

- Fixes votes being reported as their vote key and not a flavor message

- Allows ghosts to change their vote

- General small code cleanup

- Calls parent in topic so stat panel clicks work

- Fixes #41718 , again? If it was actually ever fixed, not sure

:cl: Melbert
qol: Haunted 8-ball no longer requires the ghost orbit the petitioner to
submit votes
qol: Haunted 8-ball ghosts can now change their vote after submitting it
fix: Haunted 8-ball no longer always reports "yes"
fix: Haunted 8-ball no longer always reports default "yes", "no", or
"maybe" and now gives a proper eight ball response
fix: Haunted 8-ball can be picked up via the stat panel
/:cl:

* Replace DreamAnnotate action with a python script (#78225)

This PR removes the "Annotate Lints" job step and merges it with the
"Run Linters" step above. To achieve this, I wrote a python script that
should be identical to the action. I even added the ability to read the
output from a file to the script if we ever needed that, but I decided
to have the job step pipe the output into the script instead.

It always bugged me a bit that we had to check the results for a
separate step if we wanted to see the linter results for dm code. I also
noticed a few people getting confused as to why their CI failed on
linters.

Turns out that the action is just a few lines that match the
dreamchecker output and reformat it to a format that GitHub can annotate
code with. It's so brain dead simple that it shouldn't need to be a
whole new step, and for the previous two reasons.

not playerfacing

* Split Run Linters step into multiple steps (#78265)

Splits the big "Run Linters" step into multiple steps. Also since all of
these steps are independent of eachother, I've made them all run
regardless of if the job is currently failing.

<details>
<summary>Proof of testing:</summary>

Fail in install tools, all linting steps are skipped:
https://github.com/distributivgesetz/tgstation/actions/runs/6151628214/job/16692089726
Fail in Run DreamChecker, other steps continue to run:
https://github.com/distributivgesetz/tgstation/actions/runs/6151664705/job/16692203569?pr=2
</details>

<details>
<summary>Pictured: me breaking CI for a day</summary>

https://github.com/tgstation/tgstation/assets/47710522/ea12ad30-2b69-4aa3-9642-7d0818eab2d1

</details>

Going through the Run Linters step has always been a slog. Finding an
error is like finding a needle in a haystack. Seeing what command
exactly went wrong is going to go a long way in helping people find out
which linters have failed.

nothing playerfacing

* Fix some odd vscode highlighting errors in workflow files  (#78274)

few errors which were odd and annoying

stealing PRs from san7890, they wanted to do this

nothing playerfacing

* fuck

* fuck 2

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>

---
## [RipGrayson/TerraGov-Marine-Corps](https://github.com/RipGrayson/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/RipGrayson/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Monday 2023-09-18 19:53:22 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[4b8de7b79f...](https://github.com/Ghommie/tgstation/commit/4b8de7b79f0a343dc587d0d17eb9361ecc7103c1)
#### Monday 2023-09-18 20:20:23 by san7890

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
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[4c40010f2a...](https://github.com/Danielkaas94/DTAP/commit/4c40010f2acc652adaae216de82948399e262605)
#### Monday 2023-09-18 20:36:16 by Daniel Kaas Bundgaard Jørgensen

🦋😇 Wings For Marie 😇🦋

You believed.
You believed in movements none could see
You believed in me.

A passionate spirit.
Uncompromised
Boundless and open.
A light in your eyes, then, immobilized.

Vacant, broken.
Fell at the hands of
Those movements that I wouldn't see.
'Cause it was you who prayed for me so
What have I done to be a son to an angel?
What have I done to be worthy?

Day light dims leaving cold fluorescence.
Difficult to see you in this light.
Please forgive this selfish question, but
What am I to say to all these ghouls tonight?

She never told a lie.
Well might've told a lie,
But never lived one.
Didn't have a life.
Didn't have a life.
But surely saved one.
Saved one.

See? I'm alright, now
It's time for us to let you go.

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[fcc176b6d5...](https://github.com/Danielkaas94/DTAP/commit/fcc176b6d5349ef3549e5be4b111eaa65406ae84)
#### Monday 2023-09-18 20:38:09 by Daniel Kaas Bundgaard Jørgensen

1️⃣0️⃣,0️⃣0️⃣0️⃣ Days (Wings Pt. 2)

We listen to the tales and romanticize,
How we'd follow the path of the hero.

Boast about the day when the rivers overrun,
How we rise to the height of our halo.

Listen to the tales as we all rationalize,
Our way into the arms of the savior.

Feigning all the trials and the tribulations.
None of us have actually been there,
Not like you...

Ignorant siblings in the congregation.
Gather around spewing sympathy,
Spare me...

None of them can even hold a candle up to you.
Blinded by choice, these hypocrites won't see.

But enough about the collective Judas.
Who could deny you were the one who illuminated
Your little piece of the divine?

And this little light of mine, a gift you passed on to me
I'm gonna let it shine
To guide you safely on your way.

Your way home...

Oh, what are they gonna do when the lights go down?
Without you to guide them all to Zion?
What are they gonna do when the rivers overrun
Other than tremble incessantly?

High is the way,
But our eyes are upon the ground.
You are the light and the way.
They'll only read about.
I only pray heaven knows,
When to lift you out.

10,000 days in the fire is long enough.
You're going home...

You're the only one who can hold your head up high.
Shake your fist at the gates saying,
"I've come home now!
Fetch me the spirit, the son and the father.
Tell them their pillar of faith has ascended.

It's time now!
My time now!
Give me my
Give me my wings!"

Give me my [5x]

Give me my wings

You are the light, the way,
That they will only read about.

Set as I am in my ways and my arrogance.
Burden of proof tossed upon the believers.
You were my witness, my eyes, my evidence,
Judith Marie, unconditional one.

Daylight dims leaving cold fluorescence.
Difficult to see you in this light.
Please forgive this bold suggestion.
Should you see your maker's face tonight,
Look him in the eye.
Look him in the eye and tell him,
"I never lived a lie, never took a life,
But surely saved one.

Hallelujah
It's time for you to bring me home."

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[4792a8e19d...](https://github.com/Helg2/tgstation/commit/4792a8e19dc6885a2f6e8d25f1086505624e7a6c)
#### Monday 2023-09-18 21:11:37 by carlarctg

Nerfs Confusion symptom for diseases (#77991)

## About The Pull Request

Removed the threshold for confusion symptom that adds illiteracy to the
disease.

Clamps confusion symptom's confusion to a maximum of 30 seconds.

Confusion as a debuff no longer guarantees random movement if you're
resting.

## Why It's Good For The Game

> Removed the threshold for confusion symptom that adds illiteracy to
the disease.

This virus makes you unable to actually treat yourself when cured, which
is frankly bonkers. Viruses are too virulent and it's rare that a doctor
actually gets to a biosuit in time to inoculate themselves, and if they
forget internals they're screwed anyways. People should be able to fix
their own got damn disease, this is asinine.

> Clamps confusion symptom's confusion to a maximum of 30 seconds.

The lack of clamping literally makes this symptom send your confusion
level to the fucking atmosphere, you can easily get upwards of 5 minutes
of confusion left because it doesn't clamp, adds 16 seconds per
activation, which is made even worse by the fact that confusion gets
stronger the more duration confusion has on you.

> Confusion as a debuff no longer guarantees random movement if you're
resting.

This remedies the last bit by not making it a literal guarantee that you
can't move in any direction after...... *3* triggers of confusion. It
should be obvious to anyone how absurd this is.

Honestly, it's plain as day that the only reason any of this ended up
like it is because of poor coding and oversights. This is just bringing
things down to their designed level.

## Changelog

:cl:
del: Removed the threshold for confusion symptom that adds illiteracy to
the disease.
balance: Clamps confusion symptom's confusion to a maximum of 30
seconds.
qol: Confusion as a debuff no longer guarantees random movement if
you're resting.
/:cl:

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[a5aef3b823...](https://github.com/Helg2/tgstation/commit/a5aef3b823dd3b8b5bfe40d68bbc0f89b403f79a)
#### Monday 2023-09-18 21:11:37 by MrMelbert

Replaces Ascended Blade Heretic stun imminuty with a stun absorption effect (it's not as cool as it sounds)  (#78060)

## About The Pull Request

Instead of being completely immune to stuns after ascension, blade
heretics now have a stun absorption. This is the effect that His Grace
and the Bastard Sword use.

It functions similarly, in that it stops you from being hardstunned, but
the difference it is they are only immune to a limited amount of stuns
for a limited amount of time before it recharges.

Currently that number is 45 seconds of stuns, with a 2 minute recharge,
meaning if you take more than 45 seconds of stun effects you will stop
being immune.

Bear in mind this still provides full immunity to being stamcrit*, as
stam doesn't contribute towards "seconds stunned" number.

*Unless you used all 45 seconds of stun immunity then you will no longer
be immune until you recharge.

Also to compensate, I gave them a slightly modifier protecting against
knockdowns.

## Why It's Good For The Game

I forgot Stun Absorptions were a thing entirely when making this even
though I refactored the darn things.

Anyways, the reason why I'm doing this is that Stun Absorptions are just
a slightly more fair, less overt way of providing stun immunity, and I
think it fits the theme more.

You're supposed to be a master duelist, but being able to take on a
dozen people at once is not entirely intended (even though this is the
ascension, I know). Stun Absorptions lend better to that, since you run
out of stun juice eventually before you have to pull back.

Though ultimately this doesn't change very much, as we use very few
hardstuns now-a-days:

- A flashbang will contribute about 10 seconds of stun time
- A flash is similar to a flashbang
- Bodythrows and tackles are less than 5 seconds
- Beepsky, 10 seconds
- Stamcrit, 0 seconds, but you are still slowed by stamina damage
- A banana peel, default is roughly 6 seconds. <-- (This is why I gave
them a knockdown modifier)

However it does mean you can't really tank an AI stun turret all day.
That's Rust's thing. Go play Rust Heretic.

## Changelog

:cl: Melbert
balance: Ascended Blade Heretics no longer have blanket stun immunity,
they now have 45 seconds of stun absorption that recharges after 2
minutes - think His Grace. This doesn't affect stamcrit (still immune to
that) (assuming you haven't consumed all of your immunity charge) but
does affect hard CC such as slips, flashbangs, or beepsky.
balance: Ascended Blade Heretics now have a 0.75 modifier to incoming
knockdowns.
/:cl:

---
## [stberr19/GlobalPopulationTrends](https://github.com/stberr19/GlobalPopulationTrends)@[bc74703947...](https://github.com/stberr19/GlobalPopulationTrends/commit/bc7470394763ea85f1edf5bcf943052f31df524c)
#### Monday 2023-09-18 21:30:10 by Simon Berry

Add files via upload

After cleaning and creating SQL queries, I used the queries to make temp tables which I then uploaded to Tableau to analyze further. The visuals get me closer to answering the questions I had.
In the dashboard, in the top left, we have a visual regarding population growth rates, where the bluer a country is, the more it's growing, and the more orange a country is, the more it's losing population. It appears that the region of the world growing the quickest is Sub-Saharan Africa, with central Asia also becoming more developed. However, Eastern Europe seems to be becoming less populated.
In the center left, there's a visual pertaining to urbanization. Similarly, the bluer a country is, the more of a percentage that's moving to urban areas, and the more orange a country is, the more of a percentage that's leaving cities and heading to rural areas. We can immediately spot a distinct correlation between urbanization rates and population growth. This is because almost all the countries that gained population also had more of its population heading to urban areas, and vice versa. Going off of that, we can observe that urbanization rates are high in Sub-Saharan Africa and low in Eastern Europe, as well as Venezuela, who also experienced population loss. We can generally observe that, with some exceptions, more people are moving to urban areas than rural areas.
In the bottom left, we look into life expectancy changes in terms of years. Orange countries have lower life expectancies than it did in 2017 while blue countries have higher life expectancies. The first thing we notice is that life expectancies are generally lower than they were in 2017. However, there are two areas which defy these trends: Sub-Saharan Africa and East Asia. While East Asia certainly did not have quite as strong urbanization rates or population growth as Sub-Saharan Africa did, it did see more of its people moving to urban areas and their countries growing in population.
In the top right, we observe countries in terms of a birth to death ratio, where bluer countries have significantly higher deaths compared to births than countries in turquoise. While Sub-Saharan Africa is also observing more births compared to deaths, two more regions to consider are the Middle East and Central Asia, which also have more people being born than dying. Eastern Europe seems to be having more people die than those being born, which may be part of the reason why its population is decreasing.
Finally, in the bottom right, we analyze infant mortality rates compared to fertility rates. Bluer countries represent those countries with a large infant mortality rate compared to fertility rate. Bluer countries may observe more births, but may not have the adequate resources to make sure the babies live long, fulfilling lives ahead of them. The two areas that would appear to be the case are Sub-Saharan Africa and Southeast Asia. However, with life expectancies increasing in both regions, along with more urbanization and population growth, it appears that both regions could become very developed in the future if trends continue.
In conclusion, we see that Sub-Saharan Africa and Southeast Asia are becoming more developed areas of the world, while Eastern Europe is becoming less developed than it once was.

---
## [gitgitgadget/git](https://github.com/gitgitgadget/git)@[8f23432b38...](https://github.com/gitgitgadget/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Monday 2023-09-18 21:55:03 by Johannes Schindelin

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
## [peff/git](https://github.com/peff/git)@[9da37c6a60...](https://github.com/peff/git/commit/9da37c6a6082791306da6ae2043c2895deed5e41)
#### Monday 2023-09-18 22:03:54 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [Sadhorizon/Paradise](https://github.com/Sadhorizon/Paradise)@[acb7352265...](https://github.com/Sadhorizon/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Monday 2023-09-18 22:30:02 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---

