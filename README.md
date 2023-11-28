## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-27](docs/good-messages/2023/2023-11-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 4,424,873 were push events containing 5,552,721 commit messages that amount to 308,624,297 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 72 messages:


## [Matt-Caspermeyer/H3B](https://github.com/Matt-Caspermeyer/H3B)@[485294ec40...](https://github.com/Matt-Caspermeyer/H3B/commit/485294ec40abdb2b616e86898c34aba799a530c6)
#### Monday 2023-11-27 00:19:10 by Matt-Caspermeyer

Alpha Release 2011-11-26

Heroes of Might and Magic 3 Babies (HOMM3 Babies) Mod / Micro / Mini Expansion Pack for King's Bounty: The Legend
-----------------------------------------------------------------------------------------------------------------

Created by: Matt Caspermeyer (matt.caspermeyer@cox.net)
-------------------------------------------------------

You are free to use any part of my work in your projects so long as you give me credit.

Version: Alpha 2011-11-26
-------------------------

* mod_homm3_babies.kfs
  & UNIT_FEATURES.LUA
    ^ Ghosts Soul Drain now increases units by the amount of units killed instead of damage
    ^ Thanks to Fatt_Shade for suggesting this!
  For all the wife_babies text files thanks to both Fatt_Shade and Erkilamrl!
  & FEANORA_BABIES.TXT - fixed some child bonus errors
  & GERDA_BABIES.TXT - fixed some child bonus errors
  & MIRABELLA_BABIES.TXT - fixed some child bonus errors
  & XEONA_BABIES.TXT - fixed some child bonus errors

Updates:

Version: Alpha 2011-11-25
-------------------------

Updates:

* mod_homm3_babies.kfs
  & UNIT_FEATURES.LUA
    ^ Fixed the massive damage bug in the implementation of one of the Enchanted Hero spell casts.
    ^ Removed that from the bugs list below.
    ^ This is a *HUGE* buxfix and I've been trying to track this down for months and finally found it - yay!
  & SPELLS.TXT - fixed Enchanted Hero so it cannot be cast on the Undead or Plants
  & WIFES.TXT - fixed Mirabella's missing Griffin morale bonus - thanks Fatt_Shade!

Version: Alpha 2011-11-23
-------------------------

Updates:

* New KFS Organization - *.LNG files are in their own KFS (ZIP)
  & mod_homm3_babies_eng_lng.kfs - contains the ENG_*.LNG English Language Localization files
  & mod_homm3_babies_en_lng.kfs - contains the EN_*.LNG English Language Localization files
  & The files are collectively refered to as mod_homm3_babies_en(g)_lng.kfs.
* mod_homm3_babies_en(g)_lng.kfs (this refers to both KFS *.LNG files)
  & EN(G)_SPELLS.LNG - fixed a few spells descriptions that were incorrect
  & EN(G)_HOMM3_BABIES_RINA.LNG - updated baby descriptors for Vidomina, Lord (Death) Haart, Isra, Thant, and Finneas.
  & EN(G)_SKILLS.LNG - updated Glory skill description
* mod_homm3_babies.kfs
  & NECROMANT.ATOM - experimental change making all 3 of the Necromancer's skills reloadable (kind of more like the Human Archmage).
  & TEMPLATES.LNG - removed Necro Call bonus for Necromancy Skill Template
  & SKILLS.LUA - commented out the sp_lead_unit bonuses for all Undead units
  & SPELLS.LUA - code cleanup
  & SKILLS.TXT
    ^ Corrected a few skill values - thanks to Fatt_Shade for the Dark Commander errors!
    ^ Glory's Leadership Reduction Requirement no longer applies to Undead since it is in the Paladin tree.
    ^ Ranged Specialist - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%).
    ^ Archmage - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%).
    ^ Necromancy - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%)
  & SPECIAL_PARAMS.TXT - commented out the sp_lead_(group) bonuses since they are now longer used
  & SPELLS.TXT - updated mana_cost for a few spells for ARENA.LUA - spell_auto_cast function that AI uses
  & RINA_BABIES.TXT - made some minor tweaks to some of her babies (Vidomina, Lord (Death) Haart, Isra, Thant, and Finneas).
  & WIFES.TXT - Zombie Rina didn't have Black Knights in her Undead sp_lead_unit bonuses.
  & XEONA_BABIES.TXT - fixed an error with Dace - thanks to Fatt_Shade for finding this!
* mod_tougher_eheroes.kfs
  & 276213879.hero - error in Martin Vodash's attack value (was 5 should have been 8)

Version: Alpha 2011-11-19
-------------------------

Fixes:

* LOGIC_HERO.LUA had an error in it where for Easy and Normal difficulty level, the level up didn't work correctly.

Thanks to erkki (Erkilmarl) for helping find and fix this bug!

Changes:

* Updated Sleem's Cloud of Poison such that the early levels mana increase is less and for the 2nd upgrade you need Sleem to be higher level to get it.
  & I recently updated Sleem's Cloud of Poison before restarting my new game and as I played the previous values didn't feel right.

Additions:

* I've added the en_ language files for those users of the game with the alternate English locality files.

Version: Alpha 2011-11-13
-------------------------

Crash Fixes:

* Rina had a mispelling in one of her child names in wifes.txt. This would cause a crash to desktop when Rina was having a baby.

Version: Alpha 2011-11-11
-------------------------

This archive contains all the files for the HOMM3 Babies mod / micro / mini expansion pack for King's Bounty: The Legend. This work will be referred to loosely as the mod in the rest of this document.

There are many changes to the game, but at this time I do not have them listed here. In the future, this file will list those changes. In the mean time, visit the YouTube video page: http://youtu.be/JE0VbSnfYkM and the King's Bounty: The Legend Mod forum for more information: http://forum.1cpublishing.eu/showthread.php?p=360731#post360731.

Installation:
-------------

1. This mod is not compatible with any other mods since I've most likely modified a file that another mod uses.
  a. You will need to remove all mods from your King's Bounty: The Legend "mods" folder before installation of this mod.
  b. Ensure that the "mods" folder exists, it is typically located here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
    i. If the "mods" folder does not exist then create it below the "data" folder using the path above as a guide.
2. Extract the 4 *.KFS files included in this archive to the King's Bounty: The Legend folder.
  a. This folder is typically here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
  b. If the "mods" folder does not exist, then see note 1ai above.
  c. The 4 KFS files are:
    i.   mod_homm3_portraits.kfs - stand alone game picture resources containing all *.DAT and *.DDS files that may be used in other mods.
    ii.  mod_tougher_eheroes.kfs - stand alone tougher heroes containing all *.HERO files that may be used in other mods.
    iii. mod_homm3_babies.kfs - core HOMM3 babies mod files containing all *.ACT, *.ATOM, *.CHAT, *.LUA, and *.TXT files modified for this mod.
    iv.  mod_homm3_babies_eng_lng.kfs ***OR*** mod_homm3_babies_en_lng.kfs - updated *.LNG files
      1) Use mod_homm3_babies_eng_lng.kfs for your English localization with eng_*.lng
      2) Use mod_homm3_babies_en_lung.kfs for your English localization with en_*.lng
      3) DO NOT USE BOTH FILES!!! Just one or the other!!!
  d. All 4 KFS files are needed for the complete HOMM3 babies mod experience!
3. Run the game
  a. Start a new game to play!
  b. It is not recommended to continue your current game, please restart.
  c. For your first play through:
    i.   Please do not use any cheats (i.e. Save Game Scanner, etc.)
    ii.  Please do not use with any other mods (probably won't work anyway)
    iii. You'll be able to experience the mod as I intended it to be played.

Uninstallation:
---------------

1. Simply delete the 3 KFS files from your "mods" folder:
  a. mod_homm3_portraits.kfs
  b. mod_tougher_eheroes.kfs
  c. mod_homm3_babies.kfs
2. Done!

Notes:
------

1. This mod was developed using the Gamer's Gate V1.7 version of King's Bounty: The Legend.
2. I have not tried it with other versions.
3. This mod uses the English localizations using the "eng_" prefix for the localization files.
  a. Other versions may have other prefixes and so you may be able to get this mod to work with your localization version by changing the prefixes of the *.LNG localization files.
    i.   The *.LNG files are located inside mod_homm3_babies.kfs.
    ii.  Simply rename mod_homm3_babies.kfs to mod_homm3_babies.zip and extract files if you wish to attempt this.
    iii. Currently, you're on your own if you want to get it to work with a different localization, but if you'd like to help with localizations in your country then please let me know.
  b. In the future I hope to be able to have feedback from users to help me with the different English localization variants.

Issues / Bugs:
--------------

Since this is an alpha release of this mod, it is quite possible that your game with crash or you'll find bugs in this mod. Please provide me feedback on any issues that you are having with my mod so that I can make improvements and make your playing experience more enjoyable.

If you have any problems during play, here are some pointers:

1. If it is a game crash, note which action caused the crash.
2. If the game appears to lock up, ALT-TAB back to Windows to see if there is a pop-up.
  a. If there is a pop-up window, note the message and then click OK to proceed.
  b. After you click OK, the game will most likely crash exit to Windows.
  c. If the game does not crash after you click OK, it is highly recommended to quit your game rather than continue since behavior may be strange.
3. Save your game often just in case!
4. If the game crashes right after a battle and you've asked your wife for children then it is due to a spelling error in one of that wife's children.
  a. I just ran into this problem where I had a mispelling in one of Rina's children.

Crash List
----------

1. I've had crashes with a failure to allocate more memory a couple of times.
  a. The solution is to reload your most recent save game and simply continue.
  b. Let me know if you see this problem, but currently I have no idea how to resolve it (I probably would need 1CC or Katauri Interactive's help with this one).

Bug List - there is one bug that I'm not sure if I've squished or not:
--------

1. Damage causing effects (i.e. burning and poison):
  a. If an AI unit is killed by a damage causing effect and if the next unit to move is another AI unit, then their damage causing effect is skipped if they have one.
  b. I worked and worked trying to fix this bug, but to no avail.
    i.  I'm pretty sure that it is a bug with the game itself as I don't think they intended for damaging effects to kill units.
    ii. As such, I don't know how to fix this bug, but if you have any ideas then please let me know!

If you notice any other problems or issues, then please let me know!

It is my intent to make this mod as bug free and enjoyable as possible!

Updates:
--------

1. As this version of the mod is in an alpha state, there are still changes that are being done; however:
  a. The mod is stable enough to play the game completely through - enjoy!
  b. Every change has been checked at least once, but I'm in the quality assurance phase rechecking the code.
  c. I'm about to start a new Paladin game to check gameplay some more.
2. At this stage, changes should not require you to restart your game - simply install the new files and continue playing.
3. Updates will most likely occur on a bi-monthly basis depending on severity and other factors.
4. Once the quality assurance phase is completed and sufficient feedback is garnered, the project will transition to the beta release phase.
5. The beta release phase will have all features properly implemented and all controllable bugs fixed.
  a. Changes will be focused on editing data files (i.e. *.ATOM, *.TXT) to improve game balance and user enjoyability.
  b. Once the beta phase has garnered sufficient feedback, the project will transition to the official release phase - more information on that once the beta phase is reached.

Modders:
--------

1. I've made many changes under the hood that only modders or code aficionados would notice.
2. I've added comments where warranted to the areas in the game that I've changed.
  a. Feel free to look at these comments and provide me feedback if you know of a better way to implement something.
  b. Certain comments have the word "HACK" where I did not know how to do it a better way - once again if you know a better way to implement this feature then please let me know!
3. I've unified many *.LUA functions (i.e. like SPELLS_POWER.LUA) so that they all use the same bonus system, etc.
4. I've made common functions for dealing with redundant code.
  a. The original *.LUA files had lots and lots of redundant code.
  b. I've replaced most of the redundant code in the *.LUA functions I've edited to reduce error and provide code consistency.
5. I've beautified the sections of the *.LUA files I've changed to make reading the code much, much easier.
6. The changes I've made really form the basis of a new code base from which you can create new mods.

Copyright Issues:
-----------------

1. This work contains images from the Heroes of Might and Magic 3 game and those images are copyrighted.
2. The picture for Orcelyn Ordy I found via the web, but I have not been able to find out who created that source image.
  a. If you have any information about who created this picture please let me know and I'll give credit to the author.
3. I created all the new ability icons.
4. All of my effort is being freely distributed to the public domain.
  a. Please give me credit if you use any portion of my work in your projects - thanks! :-)
  b. Feel free to use this code base as a starting point for your own mod!

THANK YOU!!!
------------

1. Thanks to all the people posting in the King's Bounty forums, especially those with modding tips!
2. Thanks for trying out my mod and providing feedback!

/C\/C\ Matt Caspermeyer

---
## [thecsw/thecsw.github.io](https://github.com/thecsw/thecsw.github.io)@[8c005e4591...](https://github.com/thecsw/thecsw.github.io/commit/8c005e45912f973a9b1e2634df94696a409f6a70)
#### Monday 2023-11-27 00:21:36 by Ubuntu

[ASTRIE] Added a new fortune: ** 330; 12023 H.E.

There are few of us who have not sometimes wakened before dawn, either after one of those dreamless nights that make us almost enamored of death, or one of those nights of horror and misshapen joy, when through the chambers of the brain sweep phantoms more terrible than reality itself, and instinct with that vivid life that lurks in all grotesques, and that lends to Gothic art its enduring vitality, this art being, one might fancy, especially the art of those who minds have been troubled with the malady of reverie. Gradually white fingers creep through the curtains, and they appear to tremble. In black, fantastic shapes, dumb shadows crawl into the corners of the room, and crouch there. Outside, there is the stirring of the birds among the leaves, or the sound of men going forth to their work, or the sigh and sob of the wind coming down from the hills and wandering round the silent house, as though it feared to wake the sleeper, and yet must needs call forth Sleep from her purple cave. Veil after veil of thin, dusky gauze is lifted, and by degrees the forms and colors of things are restored to them, and we watch the dawn remaking the world in its antique pattern. The wan mirrors get back their mimic life. The flameless tapers stand where we had left them, and beside them lies the half-cut book that we had been studying, or the wired flower that we had worn at the ball, or the letter we had been afraid to read, or that we had read too often. Nothing seems to us changed. Out of the unreal shadows of the night comes back the real life that we had known. We have to resume it where we had left off, and there steals over us a terrible sense of the necessity for the continuance of energy in the same wearisome round of stereotyped habits, or a wild longing, it may be, that our eyelids might open some morning upon a world that had been refashioned anew in the darkness for our pleasure, a world in which things would have fresh shapes and colors, and be changed, or have other secrets, a world in which the past would have little or no place, or survive, at any rate, in no conscious form of obligation or regret, the remembrance even of joy having its bitterness, and the memories of pleasure their pain.

― Oscar Wilde, /The Picture of Dorian Gray/

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[81a7c75583...](https://github.com/Thunder12345/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Monday 2023-11-27 00:37:05 by necromanceranne

Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more) (#79517)

## About The Pull Request

It's been a hot minute hasn't it?

When I initially reworked Sleeping Carp, we didn't have combat mode. Now
that we do, and that Sleeping Carp has substantially less defensive
power to justify having to make a choice between deflection and
attacking, it's probably about time we updated this aspect back to what
it was before my rework. Sorta.

Now, we can have all the deniability of the previous method, while also
letting you reliably protect yourself from ranged attacks at all times
while it matters. Because of this, I increased the price up to 17 TC
because of this change just to be on the safe side. The higher uptime of
projectile immunity while also being able to attack during that time
makes this a lot stronger overall.

Secondly, Sleeping Carp presently just isn't as good as a good ol'
baton. It takes a lot more hits to accomplish the same task that a baton
can. Many people feel like they can't even reasonably fight anyone for
fear of the baton, or they would rather use a baton and kill someone at
their leisure. So we've updated some of the moves in order to facilitate
Sleeping Carp as a substantial contender for 1v1 fighting, and lessen
the need for a baton by adding a lot more Stamina damage overall to the
various attacks;

**Keelhaul**: Now a Shove Shove combo. Does literally zero lethal
damage, but now temporarily blinds and dizzies the target as well as its
previous effects. The amount of lethal damage it did was...extremely
small, so this isn't a particularly big loss.

**Grabs and Shoves**: Deal some amount of stamina damage (20). You need
to be in combat mode in order to perform these special attacks (more
deniability). Grabbing someone while they have 80 Stamina damage or more
will cause them to fall unconscious. Yes, I really did just want to add
a Vulcan Nerve Pinch, what do you want from me?

That's it actually. Oh, I guess they are heavy sleepers now too. Because
its funny.

## Why It's Good For The Game

I often get told (read: thrown various insults and slurs at me while
mentioning this as the justification) that Sleeping Carp is not very
strong anymore since it lost all that invisible armor I added way back +
I removed the stuns in my initial rework. This made some people upset (I
think at least one person wished for my death).

So, having given it at least 2 years, I wanted to recapture parts of
what made the older Sleeping Carp (before my rework) strong, some of the
benefits of the new version, and introduce a brand new aspect; nonlethal
takedowns. This makes it beneficial for pacifists, as well as for
kidnapping.

This should not meaningfully make Sleeping Carp any stronger against the
things that typically ruin its day. I suspect in a straight joust with a
baton, Sleeping Carp will still struggle. But against what should be its
strong points (lone targets and ranged weapons), it will be strong once
again rather than clumsily unable to do very much at all.

## Changelog
:cl:
balance: Harnessing Shoreline Quay (bluespace energy, probably), a
mystical energy (total bullshit) that permeates the Astral Waterways
(bluespace quantum dimensions, probably), Sleeping Carp users can now
once against deflect projectiles with their bare hands when focused in
on battle (in combat mode).
balance: The Keelhaul technique is now nonlethal (a philosophical
acknowledgement of the familial bond of sleep and death), but causes the
target to become temporarily blind and dizzy along with its previous
effects.
balance: Sleeping carp users, while in combat mode, deal Stamina damage
with their grabs and shoves. If the target of their grab has enough
Stamina damage (80), they are knocked unconscious from a well placed
nerve pinch.
balance: Sleeping carp users find it very hard to wake up once they fall
asleep....
/:cl:

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[1a9043d797...](https://github.com/Thunder12345/tgstation/commit/1a9043d797325fe09cdb4e42d42f5d922c151ed9)
#### Monday 2023-11-27 00:37:05 by necromanceranne

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
## [LeeroysHub/RM-Flipper](https://github.com/LeeroysHub/RM-Flipper)@[0a8cfd4ed3...](https://github.com/LeeroysHub/RM-Flipper/commit/0a8cfd4ed3d51366dba25e75097521c5d540173a)
#### Monday 2023-11-27 00:42:30 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[4d4aa72e33...](https://github.com/FalloutFalcon/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Monday 2023-11-27 00:43:28 by lizardqueenlexi

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
## [mooso/nope-the-hoop](https://github.com/mooso/nope-the-hoop)@[1efddf9882...](https://github.com/mooso/nope-the-hoop/commit/1efddf988217dc7763a4213970798a90d34c6385)
#### Monday 2023-11-27 00:45:36 by Mostafa Elhemali

Proper async support to proto

I was very unhappy with my hacky async-over-sync protocol on the server,
mainly the presumption that when the asyn stream was readable it would
always have at least one message in there, so I bit the bullet and added
proper async support in proto under a feature flag so the client can
stay with no dependency on tokio.

This involved some amount of code and logic duplication between sync
and async, but overall it's much cleaner I think. Now the async path
provides a clean Stream over messages with fewer assumptions and
cleaner interface. Also this allowed me to get rid of FRAME_SIZE and
just prefix every message with its size. I did cap it to 512 though
because I got paranoid about evil clients trying to get the server to
allocate a lot. Damn evil clients.

---
## [marcusm0606/2D-Final-Game](https://github.com/marcusm0606/2D-Final-Game)@[5ef58bc977...](https://github.com/marcusm0606/2D-Final-Game/commit/5ef58bc977e9338e9715648f8783c804ecfd0873)
#### Monday 2023-11-27 00:47:19 by marcusm0606

using this update to note bugs i need to fix

1. When you select main menu from pause you are paused when loading into level
2. resume button not implimented
3. sound effects for bomb and sniper are cursed
4. no background music
5. needs to fix health it starts with display at 10 but actually have 50 and only updates after hit so just make starting display 50 for the player.
6. note i scrapped a turret and only have 3 now i need to impliument upgrades possibly when clicked on a small menu comes up over turret to either upgrade damage for a really high price or to upgrade fire rate for a more reasonable price. shouldnt actually take very long to implement
 7.  another note for time reasons i will proabably keep same wave spawner layout throughout levels for now but i will change this for myself in the future i plan to continue this a little further than the assignment you have given me.
i plab to update the levels to  a different design but dont know if i will get to it

i added pause menu bomb turret sniper turret fixed ui for shop and redid my wave spawner to kinda balance the game even tho upgrades arent implemented i feel they will fit nicely if i can balance their price
need to add art to main menu level selector and finish the win screen for when level 3 is beaten

---
## [fricklerhandwerk/nix.dev](https://github.com/fricklerhandwerk/nix.dev)@[1a4dd3b44f...](https://github.com/fricklerhandwerk/nix.dev/commit/1a4dd3b44fb002ca1882de85a1b69960d2192c35)
#### Monday 2023-11-27 00:52:15 by fricklerhandwerk

host Nix reference manual on nix.dev

this is the most cursed setup you will see any time soon.

we're dumping the Nix manual unchanged into the build tree *after*
building. the reason is that we'd want to link to it from our table of
contents, but because Sphinx does not allow adding arbitrary files to
the build output in arbitrary locations (only `_static` works). but we
want to place the manual behind a particular URL, and the alternative of
maintaining URL rewrites (e.g. in nginx) is not accessible here because the
infrastructure is managed somewhere else.

now that the files won't appear in their desired locations at Sphinx
build time, we can't use relative links to reference them, therefore we
have to resort to pointing to the web URL the manual will appear at.
this is terrible and I'm sorry. please fix this if you have a better
idea. once we use URLs though, we have to avoid linkchecking, since
those files may not be there before deploying them.

figuring all of this out took way longer than anyone would wish.

Co-authored-by: Alejandro Sanchez Medina <alejandrosanchzmedina@gmail.com>

---
## [DogeDogIs/Paradise](https://github.com/DogeDogIs/Paradise)@[6a109ade7f...](https://github.com/DogeDogIs/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Monday 2023-11-27 01:00:53 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [lolman360/f13tbd](https://github.com/lolman360/f13tbd)@[830db814f3...](https://github.com/lolman360/f13tbd/commit/830db814f3104bfe595db02eea0759766eb2cd10)
#### Monday 2023-11-27 01:11:00 by GreytidePanda

Expanded Mall (#171)

## About The Pull Request
The northwest mall was an area scraped together from an older mall
building and expanded on by me well over a year ago, but it was always
unfinished as I left Sunset before I submitted the final version. You
can really tell this if you look at some of the suspiciously empty rooms
on the upper levels.

The finished version has been sitting on my harddrive for a long time so
I've copied it in and made a few changes to fit the server. I'm not sure
if the mall is staying with future map changes, but at least for now I
want to be judged on my completed work.

- References to 'Mall of Wyoming' are now 'Mall of Utah'
- A lot of rooms are now less claustrophobic and use their space better
- More loot and detail (no crazy loot - it was always intended as a
fairly beginner friendly zone)
- Now far more vertical - an underground parking lot, and accessible
roof
- Removed the 'requires_power' flag from the mall area tag - no other
ruin uses it
- Fixed the instrument shop shutter not working (I can't believe this
bug has existed for over a year)

## Why It's Good For The Game
Better locations are always good for the game!

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog
:cl:
add: The Mall of Utah now offers an even bigger shopping experience.
/:cl:

---
## [LASA-Game-Development-Club/NamePending](https://github.com/LASA-Game-Development-Club/NamePending)@[b939018887...](https://github.com/LASA-Game-Development-Club/NamePending/commit/b939018887e0a2e7c32384e0a564e40e7e0ce43c)
#### Monday 2023-11-27 02:09:43 by CMDRZero

The God Help Me Patch

Moved local version to 2020.3.14f1 to fix bug. Played around with sample scene and my gosh, missiles are a pain to avoid. Have fun, took me about 20 minutes to beat this sample scene.

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[73bdd7341a...](https://github.com/Zergspower/Skyrat-tg/commit/73bdd7341acdf6f5b7d38a484a1dba8106438c56)
#### Monday 2023-11-27 02:45:36 by SkyratBot

[MIRROR] TGUI Destructive Analyzer [MDB IGNORE] (#25005)

* TGUI Destructive Analyzer (#79572)

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

* TGUI Destructive Analyzer

* Modular

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[1f1cdc609d...](https://github.com/Zergspower/Skyrat-tg/commit/1f1cdc609df04a4749b2f3f5d5500551c86021a8)
#### Monday 2023-11-27 02:45:36 by Nerevar

[FIX] Fixes Kick Damage (#24996)

* holy shit yeah

* Update code/modules/mob/living/carbon/human/_species.dm

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[22b8f2b965...](https://github.com/treckstar/yolo-octo-hipster/commit/22b8f2b965c7b099d4448438cec99ca49c003446)
#### Monday 2023-11-27 03:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [khonsulabs/gooey](https://github.com/khonsulabs/gooey)@[2201f2c83b...](https://github.com/khonsulabs/gooey/commit/2201f2c83b87efd7bf2eab76d65d9118b0ab7d3d)
#### Monday 2023-11-27 03:31:32 by Jonathan Johnson

Ranged sliders, advance_focus, allow_blur

Closes #60

Stepping in sliders is a compromise due to the flexibility of the
current slider implementation. I don't want to force types to implement
Add, and I don't like forcing types to require a Step (ie, what's the
appropriate value for f32 to specify as its next value?). Using a
percentage combined with lerp keeps the implementation fairly
straightfoward, although I remember experiencing this type of
configuration in another UI framework a long time ago and thinking it
was a little annoying to work with.

Ultimately, setting actual step boundaries can be done by customizing
the type that the slider is operating over. I feel like that's a much
more powerful design than I've experienced in previous frameworks, so
I'm hoping this percent step behavior is a reasonable compromise.

---
## [mazzinsanity/f13babylon](https://github.com/mazzinsanity/f13babylon)@[ccb9ce38a7...](https://github.com/mazzinsanity/f13babylon/commit/ccb9ce38a7e26763f93c089bd0a65c9e35b70243)
#### Monday 2023-11-27 04:12:55 by panzerr1944

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
## [mazzinsanity/f13babylon](https://github.com/mazzinsanity/f13babylon)@[a2491a3c89...](https://github.com/mazzinsanity/f13babylon/commit/a2491a3c89e4fa54e2c112902162278493f10945)
#### Monday 2023-11-27 04:12:55 by Mazzinsanity

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
## [gnoswap-labs/gno](https://github.com/gnoswap-labs/gno)@[24d89a4f5d...](https://github.com/gnoswap-labs/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Monday 2023-11-27 04:56:18 by Morgan

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
## [re621/dnpcache](https://github.com/re621/dnpcache)@[9917c10301...](https://github.com/re621/dnpcache/commit/9917c103015682700ec06bf870854624353c300f)
#### Monday 2023-11-27 05:28:30 by bitWolfy

Remove 923 artists from the DNP list.

Removed: w00my, haven_(artist), gipbandit, loki_the_vulpix, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, darkfool., huwon, tsukikibaokami, carnalcove, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurobait, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sincerity_gender, anima-virtuosa, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, koriaris, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, rexisminimalis, delkon, connisaur, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [Lazr1026/Kurisu](https://github.com/Lazr1026/Kurisu)@[9e35541d41...](https://github.com/Lazr1026/Kurisu/commit/9e35541d41ded2e07a938ef8acfc9b70916c1090)
#### Monday 2023-11-27 05:42:41 by eip

github said i added this but i didnt mean to so i removed it

and then it turned out it needed it anyway
fuck you github

---
## [Coolguysixtyfour/coolguystation-tg](https://github.com/Coolguysixtyfour/coolguystation-tg)@[0c17553a96...](https://github.com/Coolguysixtyfour/coolguystation-tg/commit/0c17553a9629aa72cd62339e60e28e2c9e7f114c)
#### Monday 2023-11-27 05:54:12 by lizardqueenlexi

Basic Constructs: Artificer (#79015)

## About The Pull Request

Really getting into the meat of the constructs now. Artificers have
become basic mobs.

On the whole, this was a pretty rote conversion, with no significant
gameplay changes other than the switch to using healing hands rather
than a unique heal ability. The player experience as an artificer is
more or less identical.

The _interesting_ part comes with the AI for the seldom-used "hostile"
variant. Hostile artificers, being squishy and laughably weak, are now a
dedicated "medic" role for constructs. They will perform triage, always
seeking the most wounded construct (or shade!) to give healing to. They
will not attack at all, but they _will_ flee with great speed if
attacked and not busy healing. If they are healing another construct,
they will remain even if they are beaten to death.

I've added some more AI functionality that may come in handy in the
future, and done some refactoring to keep things from getting out of
hand:
- A planning subtree for finding targets that will always select the
most heavily wounded living target that the mob can see (or rather, the
one with the least health). Useful again for medical triage, or for
making a particularly cruel mob that always attacks whoever is easiest
to kill. I plan to use this for NPC wraith constructs when I convert
them.
- Targeting datums can now check a blackboard key to see if they should
only target wounded mobs. This is particularly useful for "medic" type
mobs such as this one.
- I've refactored the "minimum stat" behavior of targeting datums to be
stored in a blackboard key. This removes the need to have unique
subtypes for each different minimum stat we might want. Which... for the
most part, weren't even used, leading to proliferation of several
completely identical targeting datums in a bunch of different files.
Hopefully this change will make things cleaner.

In addition, this PR fixes a pair of bugs from #78807 that I didn't
catch:
- Healing constructs can now actually heal shades. Turns out I forgot to
add the correct biotype.
- Healing hands, when set to print the target's remaining health, no
longer does so as a visible message.

The one thing I didn't do that I kind of wanted to is make NPC
artificers heal themselves when wounded and not busy doing something
else, but it ended up being kind of annoying to make a mob willingly
target itself. NPC artificers never had this behavior before, so I
consider it okay, but maybe I'll circle back to it later.
## Why It's Good For The Game

Another basic conversion, another 5 items off the checklist. Very little
should change in-game, though I think the new NPC AI could make for
interesting challenges in ruins or bitrunning or something.
## Changelog
:cl:
refactor: Artificer constructs have been converted to the basic mob
framework. This should change very little about them, but please report
any bugs. NPC artificers are now smarter, and will focus on healing
nearby wounded constructs - if you see them, take them out first!
/:cl:

---
## [Coolguysixtyfour/coolguystation-tg](https://github.com/Coolguysixtyfour/coolguystation-tg)@[31afabc9af...](https://github.com/Coolguysixtyfour/coolguystation-tg/commit/31afabc9afae2252fc22958d07f12f7148d6963d)
#### Monday 2023-11-27 05:54:12 by Jacquerel

Adds missing default biotypes to some damage procs (#79102)

## About The Pull Request

I noticed by complete coincidence because I happened to glance at the
channel a bunch of people complaining about blobbernauts not taking any
damage when leaving the blob in manuel round end chat.
Did anyone report this bug, even after prompting? No. Not even the game
admin who was playing as the blob.

Makes you wonder how many other bugs people are perfectly willing to
spend 15 minutes posting "i fucking hate coders" about without actually
telling anyone they exist. Sucks to be them I guess.

Anyone the cause is that some of these procs didn't have a default
biotype, so they would never take the toxin damage they were being
assigned. Now they will.

## Changelog

:cl:
fix: Blobbernauts will once again take damage when not on blob tiles.
/:cl:

---
## [Coolguysixtyfour/coolguystation-tg](https://github.com/Coolguysixtyfour/coolguystation-tg)@[ece51a1a9d...](https://github.com/Coolguysixtyfour/coolguystation-tg/commit/ece51a1a9d6896a54b878563d9c33002bc8f3688)
#### Monday 2023-11-27 05:54:12 by nikothedude

[NO GBP] Fixes scream for me, and also fixes literally EVERY INSTANCE of non-random puncture wounds (#79043)

## About The Pull Request

Closes https://github.com/tgstation/tgstation/issues/79017

So turns out, I

1. Had a pair of inverted more/less than operators in a crucial area. I
DONT KNOW HOW THIS WORKED. SHIT is a FUCKING mystery.
2. Used a non-existant define which DM converted into a string because
Byond
## Why It's Good For The Game

bugsgs badagfd
## Changelog
:cl:
fix: Scream for me, the spell, now works
fix: Non-random puncture wounds can now be applied
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Aditya06Prasad/Blogging-Website](https://github.com/Aditya06Prasad/Blogging-Website)@[2aebf9dff1...](https://github.com/Aditya06Prasad/Blogging-Website/commit/2aebf9dff18c532d36c52d8c5420ed61267d46fd)
#### Monday 2023-11-27 05:56:41 by Aditya Prasad

Update README.md

Hey there! So, guess what? I just launched my very own blogging website, and I'm super excited to share it with you!

This website is like my online diary but cooler. It's where I spill my thoughts on everything from everyday life to deep stuff happening in the world. And the best part? You can join in too! It's not just about me – I want to hear your stories and thoughts as well.

Navigating the site is a breeze. I've made sure it's easy to find what you're looking for. Whether you're into personal stories, lifestyle tips, or just want to dive into some interesting reads, there's a little something for everyone.

---
## [Atash22/Atash22](https://github.com/Atash22/Atash22)@[07c379fdb6...](https://github.com/Atash22/Atash22/commit/07c379fdb64fe70dad17896848b3d52f0179859a)
#### Monday 2023-11-27 05:57:10 by Atash22

Update README.md

Hi, I’m @Atash22, a dedicated Front-End Developer with a passion for creating engaging and user-friendly web experiences.

👀 My interests lie in the core technologies of web development: HTML, CSS, JS, and React. I find joy in transforming ideas into visually stunning and functional websites, and I'm particularly excited about the endless possibilities that React offers for building dynamic user interfaces.

🌱 Currently immersed in the world of Front-End Development, I'm on a journey of continuous learning and improvement. Every project is a chance to enhance my skills and contribute to the ever-evolving web landscape.

💞️ I’m actively seeking collaboration on projects that align with my skills and interests. If you have an exciting venture in need of a Front-End Developer, I'm eager to bring my expertise to the table.

---
## [box-project/box](https://github.com/box-project/box)@[0384de9712...](https://github.com/box-project/box/commit/0384de9712e741083ef23df4e6326aa697662815)
#### Monday 2023-11-27 07:06:06 by Théo FIDRY

fix: Migrate from amphp/parallel-functions to amphp/parallel (#1216)

In #723 I disabled the parallelization by default as building the Box PHAR with parallelization was x1000 slower than without. 

Since then, a number of things changed in PHP-Scoper and in preparation to adapt the way the parallelization is done, a few things changed in Box too. I am not sure what element made a difference but according to PHPBench, enabling parallelization was reducing the build time from `13.932s` to `9.243s` so a ~33% speed improvement.

I however gave it more though I as thinking serializing closures is a bad idea of a source of too many problems. Currently using parallelization in Box results in errors due to data being `readonly`. I do not remember exactly in what part `laravel/serializable-closure`  messes up but I also remembered it was a limitation of the library (and in fairness, the library is really not at fault, it tries really hard to hack its way through to patch a very annoying PHP limitation, so it does what it can).

But I kept finding those issues too annoying and I think the solution is also quite simple: to use AMPHP at a level lower which would avoid to have to serialize closures altogether.

Closes #552.
Closes #602 (the memory issue seems gone according to the PHPBench results).
Closes #1160 (superseded).

With those changes, we get the following results:

| subject                                      | memory   | mode   | rstdev | stdev    |
| - | - | - | - | - |
| with PHP-Scoper; no parallel processing | 940.391mb | 13.932s | ±0.88%  | 122.973ms |
| with PHP-Scoper; parallel processing | 47.957mb | 6.668s | ±0.64% | 42.899ms |

**In other words the parallelization goes from `9.243s` to `6.668s`, so a further ~28% improvement making it ~52% faster than without parallelization.**

---
## [rust-lang/miri](https://github.com/rust-lang/miri)@[0b1e434b2b...](https://github.com/rust-lang/miri/commit/0b1e434b2bac8e79909357df3f627c8a728cdbe4)
#### Monday 2023-11-27 07:13:06 by bors

Auto merge of #117611 - Nadrieril:linear-pass-take-4, r=cjgillot

Rewrite exhaustiveness in one pass

This is at least my 4th attempt at this in as many years x) Previous attempts were all too complicated or too slow. But we're finally here!

The previous version of the exhaustiveness algorithm computed reachability for each arm then exhaustiveness of the whole match. Since each of these steps does roughly the same things, this rewrites the algorithm to do them all in one go. I also think this makes things much simpler.

I also rewrote the documentation of the algorithm in depth. Hopefully it's up-to-date and easier to follow now. Plz comment if anything's unclear.

r? `@oli-obk` I think you're one of the rare other people to understand the exhaustiveness algorithm?

cc `@varkor` I know you're not active anymore, but if you feel like having a look you might enjoy this :D

Fixes https://github.com/rust-lang/rust/issues/79307

---
## [cyphar/runc](https://github.com/cyphar/runc)@[4387977389...](https://github.com/cyphar/runc/commit/43879773898db4cd10aee9006422e260286d5c41)
#### Monday 2023-11-27 07:41:41 by Aleksa Sarai

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
## [Anchaaa/Faerun](https://github.com/Anchaaa/Faerun)@[10250fdf8d...](https://github.com/Anchaaa/Faerun/commit/10250fdf8d2fd880f6dd4236b2bc6b4ae45e5bc0)
#### Monday 2023-11-27 08:17:40 by neutrondecay

More tweaks

* Kingdom of Elturgard breaks up properly when Zariel takes Elturel
* Female Grand Dukes get their title
* Aylin loses her nickname at the right time, and get her girlfriend back

---
## [alphagov/signon](https://github.com/alphagov/signon)@[434430cbd6...](https://github.com/alphagov/signon/commit/434430cbd69c91e50382a28471f3d487500fc238)
#### Monday 2023-11-27 08:19:08 by James Mead

Extract page for mandating 2SV for a user

Trello: https://trello.com/c/caETStGa

This is a step on the journey to move the edit user page to use the
GOV.UK Design System. The new design calls for separate pages for
different operations on a user and this is the next one.

The `require_2sv` checkbox was previously only displayed on the "edit
user" page (from `app/views/users/_form_fields.html.erb`) when
`User#require_2sv?` was `false` and thus it was only ever possible to
use this checkbox to *mandate* 2SV; it was not possible to use it to
*unset* the `User#require_2sv` attribute.

Unlike in commits like this one [1] where we first split out the new
page and then separatly moved the new page to use the Design System,
here I've created the new page using the Design System in one go,
because there wasn't much markup in the "edit user" page to extract.

The new `app/views/users/two_step_verification_mandations/edit.html.erb`
template is based on other similar pages which we've recently extracted,
e.g. `app/views/users/two_step_verification_resets/edit.html.erb`. I
decided not to include a checkbox on the new page, because as mentioned
above, this page should only ever be needed to *mandate* 2SV.

The new `Users::TwoStepVerificationMandationsController` is closely
based on the relevant bits of code from `UsersController`, even though
some of it is probably overkill in the new context, i.e. the use of
`UserUpdate`. However, I thought it was worth keeping this step as small
as possible. I've hard-coded `user_params` to `{ require_2sv: true }`,
since there's no checkbox in the form.

I'm using `UserPolicy#mandate_2sv?` for the authorization in the new
`Users::TwoStepVerificationRequirementsController`, because that seems
to make the most sense. You could argue that I should also check
`UserPolicy#edit?` & `UserPolicy#update?` like I did in
`Users::OrganisationsController` in this commit [2], but I've gone off
that idea (sorry, @chrisroos!). Instead I've matched what I did in
`Users::TwoStepVerificationResetsController` in this commit [3].

There weren't *any* tests in `UsersControllerTest` for this behaviour,
so I had to write `Users::TwoStepVerificationMandationsControllerTest`
from scratch, but I based it closely on other similar controller tests.
Luckily there was an integration test
(`test/integration/managing_two_step_verification_test.rb`) covering the
behaviour which I've been able to fixup to work with the new UI.

Rather than creating a combinatorial explosion of tests in
`Users::TwoStepVerificationRequirementsControllerTest` relating to
whether a user with all the different roles can edit another user with
all the different roles, I've resorted to stubbing `UserPolicy.new` and
`UserPolicy#mandate_2sv?`. Although this is a bit ugly, since
`UserPolicy` is thoroughly tested in `UserPolicyTest`, it seems like a
pragmatic option.

I'm using the `error_summary` component in combination with identical
code we've used elsewhere on the off-chance there's a validation error,
because the controller action does re-render the form in that case. Note
that in normal operation there are unlikely to be validation errors on
this page, but since it's theoretically possible I thought it was worth
adding the error summary. We might want to consider changing this to
work more like `Users::TwoStepVerificationResetsController` which raises
an exception if there is a validation error. This makes sense
particularly given that the only validation on `User#require_2sv` only
applied on record creation.

[1]: https://github.com/alphagov/signon/commit/899a8a16356ad3b9e3434feaf99f5e5f2bf8a243
[2]: https://github.com/alphagov/signon/commit/bf207efe2769c0ae48102b40bb6df8e4f7ce7770
[3]: https://github.com/alphagov/signon/commit/1baf6856c34f857d71466ec3cb11e974a141175d

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[2011c229f9...](https://github.com/cmss13-devs/cmss13/commit/2011c229f9a37de8fa67a74d8e40974515724cde)
#### Monday 2023-11-27 08:22:23 by stalkerino

Readds skull facemask and facepaint (#5042)

# About the pull request
It readds two items that were removed in the past for no valid reason
(in my opinion), since it was a targeted PR against a specific player I
do not think it should've been removed.

# Explain why it's good for the game

It looks nice and fits the atmosphere, adding it will help players
customize their characters without being too loud.
The removal reason of "You'd get laughed at for wearing it IRL" is
invalid, a lot of military and law enforcement people wear skull masks,
punisher emblems and etcetra - this is especially evident in America
(We're UA)

https://discord.com/channels/150315577943130112/746325423289401395/1168350579307860078

https://discord.com/channels/150315577943130112/827156857566265375/1145494273568022588
https://files.catbox.moe/4o3ag1.png

https://discord.com/channels/150315577943130112/604397850675380234/1094357565317586964
-- the person who made it admitting it was targeted.


# Testing Photographs and Procedure
I don't think it needs testing
</details>


# Changelog
:cl: stalkerino
add: readds skull facepaint and skull balaclava (blue and black)
/:cl:

---
## [Teuhon-Rakennusyhtio/Jumpnaut](https://github.com/Teuhon-Rakennusyhtio/Jumpnaut)@[e92c204df1...](https://github.com/Teuhon-Rakennusyhtio/Jumpnaut/commit/e92c204df15c22b78acaf3c1afb9bb568cb38cad)
#### Monday 2023-11-27 08:31:24 by Alex Yli-Paavalniemi

Now the settings menu kinda works but not really I brought back the fucking hindenburg's accident of a script for the settings menu and is about as shit as when the fucker crashed in france or whtever country that shit was flying in

---
## [Kentanglu/Sea_Kernel-Fog](https://github.com/Kentanglu/Sea_Kernel-Fog)@[54459e6bbb...](https://github.com/Kentanglu/Sea_Kernel-Fog/commit/54459e6bbbd0473ee22e0f6484ce624f63d4f157)
#### Monday 2023-11-27 08:36:45 by Angelo G. Del Regno

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

---
## [aoleary/G4-Titan-Kernel](https://github.com/aoleary/G4-Titan-Kernel)@[29d1a35f97...](https://github.com/aoleary/G4-Titan-Kernel/commit/29d1a35f97c7038d8f8c4c2436266b371eacc53a)
#### Monday 2023-11-27 08:38:09 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

[ Upstream commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d ]

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Change-Id: If4290e58a2c34a7f69e2aa8e9ec0b07f15792d21

---
## [ealap/ripgrep](https://github.com/ealap/ripgrep)@[082245dadb...](https://github.com/ealap/ripgrep/commit/082245dadb3854238e62b91aa95a46018cf16ef1)
#### Monday 2023-11-27 08:49:59 by Andrew Gallant

cli: replace clap with lexopt and supporting code

ripgrep began it's life with docopt for argument parsing. Then it moved
to Clap and stayed there for a number of years. Clap has served ripgrep
well, and it probably could continue to serve ripgrep well, but I ended
up deciding to move off of it.

Why?

The first time I had the thought of moving off of Clap was during the
2->3->4 transition. I thought the 3.x and 4.x releases were great, but
for me, it ended up moving a little too quickly. Since the release of
4.x was telegraphed around when 3.x came out, I decided to just hold off
and wait to migrate to 4.x instead of doing a 3.x migration followed
shortly by another 4.x migration. Of course, I just never ended up doing
the migration at all. I never got around to it and there just wasn't a
compelling reason for me to upgrade. While I never investigated it, I
saw an upgrade as a non-trivial amount of work in part because I didn't
encapsulate the usage of Clap enough.

The above is just what got me started thinking about it. It wasn't
enough to get me to move off of it on its own. What ended up pushing me
over the edge was a combination of factors:

* As mentioned above, I didn't want to run on the migration treadmill.
This has proven to not be much of an issue, but at the time of the
2->3->4 releases, I didn't know how long Clap 4.x would be out before a
5.x would come out.
* The release of lexopt[1] caught my eye. IMO, that crate demonstrates
exactly how something new can arrive on the scene and just thoroughly
solve a problem minimalistically. It has the docs, the reasoning, the
simple API, the tests and good judgment. It gets all the weird corner
cases right that Clap also gets right (and is part of why I was
originally attracted to Clap).
* I have an overall desire to reduce the size of my dependency tree. In
part because a smaller dependency tree tends to correlate with better
compile times, but also in part because it reduces my reliance and trust
on others. It lets me be the "master" of ripgrep's destiny by reducing
the amount of behavior that is the result of someone else's decision
(whether good or bad).
* I perceived that Clap solves a more general problem than what I
actually need solved. Despite the vast number of flags that ripgrep has,
its requirements are actually pretty simple. We just need simple
switches and flags that support one value. No multi-value flags. No
sub-commands. And probably a lot of other functionality that Clap has
that makes it so flexible for so many different use cases. (I'm being
hand wavy on the last point.)

With all that said, perhaps most importantly, the future of ripgrep
possibly demands a more flexible CLI argument parser. In today's world,
I would really like, for example, flags like `--type` and `--type-not`
to be able to accumulate their repeated values into a single sequence
while respecting the order they appear on the CLI. For example, prior
to this migration, `rg regex-automata -Tlock -ttoml` would not return
results in `Cargo.lock` in this repository because the `-Tlock` always
took priority even though `-ttoml` appeared after it. But with this
migration, `-ttoml` now correctly overrides `-Tlock`. We would like to
do similar things for `-g/--glob` and `--iglob` and potentially even
now introduce a `-G/--glob-not` flag instead of requiring users to use
`!` to negate a glob. (Which I had done originally to work-around this
problem.) And some day, I'd like to add some kind of boolean matching to
ripgrep perhaps similar to how `git grep` does it. (Although I haven't
thought too carefully on a design yet.) In order to do that, I perceive
it would be difficult to implement correctly in Clap.

I believe that this last point is possible to implement correctly in
Clap 2.x, although it is awkward to do so. I have not looked closely
enough at the Clap 4.x API to know whether it's still possible there. In
any case, these were enough reasons to move off of Clap and own more of
the argument parsing process myself.

This did require a few things:

* I had to write my own logic for how arguments are combined into one
single state object. Of course, I wanted this. This was part of the
upside. But it's still code I didn't have to write for Clap.
* I had to write my own shell completion generator.
* I had to write my own `-h/--help` output generator.
* I also had to write my own man page generator. Well, I had to do this
with Clap 2.x too, although my understanding is that Clap 4.x supports
this. With that said, without having tried it, my guess is that I
probably wouldn't have liked the output it generated because I
ultimately had to write most of the roff by hand myself to get the man
page I wanted. (This also had the benefit of dropping the build
dependency on asciidoc/asciidoctor.)

While this is definitely a fair bit of extra work, it overall only cost
me a couple days. IMO, that's a good trade off given that this code is
unlikely to change again in any substantial way. And it should also
allow for more flexible semantics going forward.

Fixes #884, Fixes #1648, Fixes #1701, Fixes #1814, Fixes #1966

[1]: https://docs.rs/lexopt/0.3.0/lexopt/index.html

---
## [jessey-git/oiio](https://github.com/jessey-git/oiio)@[b8723ec691...](https://github.com/jessey-git/oiio/commit/b8723ec6918b9204d040c495eba8c8d21484df53)
#### Monday 2023-11-27 09:29:01 by Larry Gritz

fix(oiiotool): --autocc bugfix and color config inventory cleanup (#4060)

The important bug fix is in oiiotool image input when autocc is used,
where we reversed the sense of a test and did the autocc-upon-input if
the file's color space was equivalent to the scene_linear space
(pointlessly), and skipped the conversion if they were different (oh no,
big bug!).

Along the way:

* Add missing try/catch around OCIO call that should have had it.

* Some very ugly SPI-specific recognize-by-name color space heuristics.
I hate this, sorry, but it solves a really important problem for me.

* A bunch of additional debugging messages during color space inventory,
enabled only when debugging, so nobody should see these but me.

* A couple places where we canonicalize the spelling of
"oiio:ColorSpace".

Note that there is still an issue with the color space classification
using OCIO 2.3+'s identification of built-in equivalents by name. These
are shockingly expensive. I will return to this later.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[a955791561...](https://github.com/cmss13-devs/cmss13/commit/a955791561d5aeab0ff0640923fe1192ad377830)
#### Monday 2023-11-27 12:30:43 by fira

/tg/ Status effects part 1 - fluid status updates (#4828)

![image](https://github.com/cmss13-devs/cmss13/assets/604624/38cdd1a0-e13c-4d69-b893-49cea2a8113f)
CM Dev figured it out 9 years ago and nobody listened and kept tacking
illogical conditions

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

Builds on previous "prelude" PRs in the following steps:
 * Ports /tg/ body_position and mobility_flags
* Fixes some interaction requirements to use stun/mobility rather than
lying/knocked_down
* Ports /tg/ granular status updates, ie. status propagating through
handlers and signals. This includes changes to resting, buckling, and
lying down human transforms.
 * Wires our status effect system to it directly
* Removes `update_canmove` from existence completely as not needed
anymore

Because step 1 and 2 require updating all the gameplay logic using them,
this PR modifies a lot of files.

Part 2 will move the actual status effects to /tg/ status_effects,
resolving our timing problems.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Testing Checklist!</summary>

- [x] Basic Movement
- [x] Admin Freeze Prevents Movement
- [x] Resting, Getting Up
- [x] Xenos change icon when resting
- [x] Buckling, including bed rotation and propelled chairs
- [x] Crawling Movement including sprite movement
- [x] Aggressive, Choke Grabbing, and Fireman carry apply rotation
- [x] Xeno Pounce and Abduct properly freeze both target and caster 
- [x] Double dropship seats density update
- [x] Explosive knockout on Humans
- [x] Xeno burrow density and movement interactions
- [x] Xeno nest interactions, specifically confirm density changes work
- [ ] Xeno nest bullet hits doublecheck with snowflake trait check
- [x] Combat Xeno ~~knockouts~~ knockdown and sprite updates
- [x] ~~Sleeping, Waking up, Usage of items while sleeping~~ - Can't
really test this we have almost no sleep code
- [x] Arbitrary buckling rotations
- [x] Admin-set transforms work with buckling/lying
- [ ] All the broken objects that will only be found out in Testmerge

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
code: Ported basic /tg/ Status Backend.
add: Human transform changes such as lying down, knock down, buckling,
are now animated.
fix: Some statuses will now take effect immediately instead of waiting
for a life tick, notably Resting.
balance: Many interaction requirements were changed to eg. fail upon
stuns rather than if lying down.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [nicball/nicpkgs](https://github.com/nicball/nicpkgs)@[d6b0789fdf...](https://github.com/nicball/nicpkgs/commit/d6b0789fdf2af9eb5ed6bf123371a45c4b7cdfd3)
#### Monday 2023-11-27 12:30:56 by Nick Ballard

I'll mention this again, if you're git-blaming this, don't come slap me personally. This code straight ported from another project and we WILL refactor this in the future. This is a temporary solution. OK I guess you can slap me for porting this as is, but still.

Fixed what was broken.

Committing in accordance with the prophecy.

tl;dr

omg what have I done?

I hate this fucking language.

mergederp

What happens in vegas stays in vegas

---
## [PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane)@[47e74e16d0...](https://github.com/PennyLaneAI/pennylane/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Monday 2023-11-27 13:40:18 by Matthew Silverman

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
## [mootjso/Fuji_Films](https://github.com/mootjso/Fuji_Films)@[a62660c82c...](https://github.com/mootjso/Fuji_Films/commit/a62660c82ca60f89cf6f0fc9661d7883f43d03aa)
#### Monday 2023-11-27 14:00:07 by Mo

Update ReservationHandler.cs

Product Owner requested to keep the comments serious without any jokes.

- Removed the lovely friendly comments to keep it more serious.

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[800ad77ed2...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/800ad77ed29fd7c68ddc0cac3112f45e1e1c3015)
#### Monday 2023-11-27 14:33:49 by DBGit42

Adds Affection Aversion quirk (#25194)

* Adds Affection Aversion quirk

Stops affection modules. Very simple.

* I hate you, github

May or may not do anything. Stop giving me a merge conflict. Stop it.

* Revert "I hate you, github"

This reverts commit 6515023cc3f72d97d90bbdf982857b1d2724b1cf.

* Attempts to revert traits.dm

Because something went TERRIBLY wrong with my fork and/or my editor and I'm not sure why.

* Added quirk proper now that my fork is unfucked

Why did this even happen?

* These lists are alphabetized

* Same here

---------

Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [MrNotime00/FeeReport](https://github.com/MrNotime00/FeeReport)@[b134ea8894...](https://github.com/MrNotime00/FeeReport/commit/b134ea8894f8f82c0bba888ed7ddca088cd64827)
#### Monday 2023-11-27 15:27:00 by Venumadhav Vavilala

Add files via upload

Imagine a playful journey through a world of words, where a whimsical oracle predicts your next linguistic adventure. Enter the enchanting realm of the Word Predictor—a linguistic sorcerer that conjures words based on your every keystroke.

In this captivating project, we've woven the magic of Java to create a predictive text marvel. Picture this: as you type a letter, a cascade of words dances forth, each selected from an extensive lexicon that spans from "Apple" to "Zigzag." Your keyboard becomes a wand, and with each stroke, the oracle unveils a tapestry of suggestions—spellbinding, isn't it?

Behind the scenes, our Word Predictor harnesses the power of a mystical trie data structure, a sort of linguistic crystal ball. It seamlessly navigates through a forest of letters, unlocking secret paths to reveal words you might not have dreamed existed.

But there's more! We've enriched this experience by infusing a treasure trove of words—each a gem in its own right. From the celestial "Galaxy" to the mouthwatering "Pizza," every letter harbors a world of possibilities. It's not just a prediction; it's a voyage into the extraordinary.

And as you embark on this linguistic escapade, our creation doesn't just stop at suggestions; it adapts. With a user-friendly touch, you can explore, pause, and even gracefully exit the enchanted realm by simply uttering the magic word: "exit."

So, dive into this enchanting project, where words are not just letters strung together but portals to realms of imagination. The Word Predictor awaits, ready to turn your keyboard strokes into a symphony of language and take you on an unpredictable, delightful journey through the world of words.

---
## [symnnnnn/app-dev](https://github.com/symnnnnn/app-dev)@[eff28e451a...](https://github.com/symnnnnn/app-dev/commit/eff28e451a88a1009a835d60a6f5b8aaf15e9709)
#### Monday 2023-11-27 15:31:37 by symnnnnn

Update README.md

Stranger Things is an American science fiction horror drama television series created by the Duffer Brothers for Netflix. 

Spirited Away is a manifestation of fears and anxieties as seen through the lens of its young lead female character, Chihiro.

---
## [Mobilpadde/dot](https://github.com/Mobilpadde/dot)@[6a4561b044...](https://github.com/Mobilpadde/dot/commit/6a4561b04475033a4333cf6b119c935dab223849)
#### Monday 2023-11-27 15:34:10 by Mads Bram Cordes

Add more plugins

vscode
thefuck
you-should-use

Also set code

---
## [winglang/wing](https://github.com/winglang/wing)@[edd91d42e5...](https://github.com/winglang/wing/commit/edd91d42e570089b614dafad3f02601686b22c82)
#### Monday 2023-11-27 15:34:34 by Mark McCulloh

feat(sdk): inflights are not required to be resources (#4993)

## Huh?

The primary goal of this PR is to reduce the input required to create an inflight function in TS (See https://github.com/winglang/wing/issues/4842) without necessarily overhauling the compiler (yet). Ideally, the minimum information required for an inflight is simply the code itself. However, because inflights are currently modeled as resources, they require a scope and id.

So the first change was to make a new non-resource interface, IInflight, encompassing the inflight contract. The most important part of this contract is that inflights must be liftable, a behavior currently unique to resources and certain other primitives. So I extracted the lift-related functions from IResource and slapped them on the new ILiftable (which both IInflight and IResource now extend).

But that created a new problem: lifting itself also currently requires a scope. The only usage of the scope was to be able to resolve tokens. This did not seem like a good enough reason to require scope, so I changed token resolution to be more of a global concern rather than a tree-level concern. This is dangerous, but it's mostly only dangerous when you try to deal with tokens in a multi-app scenario, which would be dangerous with our current approach anyways. So this is something we'll have to add some extra handling for eventually anyways.

## Results

The primary outcome of this can be seen in the SDK unit tests, where the `Testing.makeHandler()` now only requires the code and (optional) bindings. This is basically 1 or 2 steps away from an ideal TS experience.

## But wait nothing changed in winglang

The original purpose of representing inflights as resources was to ease the implementation of lifting in the compiler and generally unify the logic of inflights between inflight closures and inflight methods of preflight classes. This hasn't changed in this PR. Luckily, the class instance emitted by the wing compiler for inflights still satisfies IInflight. It just has some extra hidden resource stuff that is simply unused. Assuming this PR is wanted, I will do a followup to change the compiler as well. This will be a more complicated change and I think it's useful to basically get the backend working first.

## Changes

- `Testing.makeHandler` now takes only code text and bindings. 9 billion tests were updated for this contract. `convertBetweenHandlers` changed similarly
- TokenResolvers are now globally registered and not tied to specific apps
- wingc adds a _hash private field to inflight closure resource classes to match the new IInflight (just an md5 hash)
- Many of the resources that deduped functions based on `addr` now do so with `_hash` instead
- Removed many occurrences of `this.node.id` used in resource ids when it's not necessary. The only time this should be necessary is if the resources is being created in the scope of this.node.scope instead
- Added a `Counter` concept to help with the many places that we want to add a subresource many times and a simple incrementing number will suffice for uniqueness and clarity
  - This was needed because the inflight `addr` was often relied upon to make this unique, but that will no longer be viable. I think it's better this way anyways

*By submitting this pull request, I confirm that my contribution is made under the terms of the [Wing Cloud Contribution License](https://github.com/winglang/wing/blob/main/CONTRIBUTION_LICENSE.md)*.

---
## [itsHanibee/kernel_xiaomi_chime](https://github.com/itsHanibee/kernel_xiaomi_chime)@[60956715a5...](https://github.com/itsHanibee/kernel_xiaomi_chime/commit/60956715a5c62d0e0c40fb045d4bdf897b35549d)
#### Monday 2023-11-27 15:57:20 by hani

techpack/data: `I AM THE STORM THAT IS APPROACHING.. PROVOKING`

* OH. MY. GOD..
- Fuck Qualcomm so much, no more mobile data panics after 2 years of this fucking issue.

Signed-off-by: hani <itshanibee@gmail.com>

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[ef52047274...](https://github.com/BlueMemesauce/tgstation/commit/ef520472740e57f253545c24c7526e45e47b5ec2)
#### Monday 2023-11-27 16:16:59 by necromanceranne

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
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[c63b233f42...](https://github.com/GoldenAlpharex/tgstation/commit/c63b233f42a46d9373fd41b3f69edde3d2d48002)
#### Monday 2023-11-27 16:17:49 by _0Steven

Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[492ed90f28...](https://github.com/GoldenAlpharex/tgstation/commit/492ed90f28dfd213e9438509653727f788efcebd)
#### Monday 2023-11-27 16:17:49 by necromanceranne

Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs. 

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

---
## [bonjorno7/TIC-80](https://github.com/bonjorno7/TIC-80)@[7c0a5253ef...](https://github.com/bonjorno7/TIC-80/commit/7c0a5253ef8dbe32408c7846ced9f363ee307bb7)
#### Monday 2023-11-27 16:34:31 by bonjorno7

Implement trim on save

I'm not too experienced with C so this was tough, but I got it working.
It trims spaces at the end of lines, and newlines at the end of the file (except for the last one, if there's space for it).
It also updates the cursor position and selection.

I increment src after the done check so that its value is correct after the loop; not actually using it after the loop in this version but just in case.
That check by the way uses a stored variable because the loop overwrites the buffer, so checking the value of end at the bottom of the loop doesn't work.
I don't zero out garbage data after the terminator because it's apparently unnecessary.
After trimming whitespace it calls history and update; hopefully those are the right functions in the right order.

One small note: if your selection was entirely trimmed, you're left with a zero length selection.
I can fix this by detecting if position and selection are equal, and then setting selection to null.
I chose not to do this however, because it's easy to create a zero length selection by hand, and the user might in some cases do so intentionally.
If you want to get rid of zero length selections entirely, that should probably be fixed elsewhere, rather than in this function.

Another note: trimming only happens with Ctrl + S, not with typing save in the console.
Perhaps I should fix this, though I think it has advantages too; I think ideally the trimming should only happen when you can see it happening, which you can't if you're in the console.
Also while writing this code it was nice to be able to undo and save my file without running the trimming code, though I suppose now that the code works properly I won't need it anymore.

---
## [llviteritti/netket](https://github.com/llviteritti/netket)@[34bd4adde1...](https://github.com/llviteritti/netket/commit/34bd4adde13df35b65f4f055a750dda242fdfa20)
#### Monday 2023-11-27 16:49:44 by Filippo Vicentini

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
## [Roundsquared/Weather-App](https://github.com/Roundsquared/Weather-App)@[9943b6e707...](https://github.com/Roundsquared/Weather-App/commit/9943b6e707ce35f40c8a76f1da952466e4dca33a)
#### Monday 2023-11-27 17:11:18 by Cedric Sumner

Added time formatting to the script

Localtime returned by api was in year first format, which was really
ugly, so I formatted it to be dd/mm/yyyy, and I added a fxn that
checks if it's the morning or evening. It's in 24h time, I'll roll
with it for now, but I might end up changing it later.

---
## [lyz-code/blue-book](https://github.com/lyz-code/blue-book)@[069dda3f9e...](https://github.com/lyz-code/blue-book/commit/069dda3f9e9e61cf94543891fd10e2c718618b73)
#### Monday 2023-11-27 17:12:56 by Lyz

feat(ansible_snippets#Ansible lint skip some rules): Ansible lint skip some rules

Add a `.ansible-lint-ignore` file with a line per rule to ignore with the syntax `path/to/file rule_to_ignore`.

fix(mkdocstrings): Correct the watch directive

`watch` is a list of directories to watch while serving the documentation. So if any file is changed in those directories, the documentation is rebuilt.

feat(emojis): Add new emojis

```
(╥_╥)
(*≧▽≦)ﾉｼ))
```

feat(zfs#Remove all snapshots of a dataset): Remove all snapshots of a dataset

```bash
zfs list -t snapshot -o name path/to/dataset | tail -n+2 | tac | xargs -n 1 zfs destroy -r
```

feat(orgmode#The orgmode repository file organization): The orgmode repository file organization

How to structure the different orgmode files is something that has always confused me, each one does it's own way, and there are no good posts on why one structure is better than other, people just state what they do.

I've started with a typical [gtd](gtd.md) structure with a directory for the `todo` another for the `calendar` then another for the `references`. In the `todo` I had a file for personal stuff, another for each of my work clients, and the `someday.org`. Soon making the internal links was cumbersome so I decided to merge the personal `todo.org` and the `someday.org` into the same file and use folds to hide uninteresting parts of the file. The reality is that I feel that orgmode is less responsive and that I often feel lost in the file.

I'm now more into the idea of having files per project in a flat structure and use an index.org file to give it some sense in the same way I do with the mkdocs repositories. Then I'd use internal links in the todo.org file to organize the priorities of what to do next.

Benefits:

- As we're using a flat structure at file level, the links between the files are less cumbersome `file:./project.org::*heading`. We only need to have unique easy to remember names for the files, instead of having to think on which directory was the file I want to make the link to. The all in one file structure makes links even easier, just `*heading`, but the disadvantages make it not worth it.
- You have the liberty to have a generic link like `Work on project` or if you want to fine grain it, link the specific task of the project
- The todo file will get smaller.
- It has been the natural evolution of other knowledge repositories such as blue

Cons:

- Filenames must be unique. It hasn't been a problem in blue.
- Blue won't be flattened into Vida as it's it's own knowledge repository

feat(orgmode#Synchronizations): Syncronize orgmode repositories

I use orgmode both at the laptop and the mobile, I want to syncronize some files between both with the next requisites:

- The files should be available on the devices when I'm not at home
- The synchronization will be done only on the local network
- The synchronization mechanism will only be able to see the files that need to be synched.
- Different files can be synced to different devices. If I have three devices (laptop, mobile, tablet) I want to sync all mobile files to the laptop but just some to the tablet).

Right now I'm already using [syncthing](syncthing.md) to sync files between the mobile and my server, so it's tempting to use it also to solve this issue. So the first approach is to spawn a syncthing docker at the laptop that connects with the server to sync the files whenever I'm at home.

I've investigated the next options:

- [Mount the whole orgmode repository with syncthing](orgmode.md#mount-the-whole-orgmode-repository-with-syncthing)
- [Mount a specific directory to sync](orgmode.md#mount-a-specific-directory-to-sync)
- [Use the org-orgzly script](orgmode.md#use-the-org-orgzly-script)

fix(rtorrent): Deprecate it in favour of qbittorrent

Use [qbittorrent](qbittorrent.md) instead.

feat(velero#Create a backup): Create a backup

If you already have schedules select the one you want to use:

```bash
velero schedules get
```

Then create the backup with:

```bash
velero backup create --from-schedule selected-schedule
```

You can see the other options to create backups in `velero backup create --help`

feat(zfs_storage_planning): Analyze the Exos X18 of 16TB disk

| Specs                        | IronWolf           | IronWolf Pro         | Exos 7E8 8TB | Exos 7E10 8TB | Exos X18 16TB |
| ---------------------------- | ------------------ | -------------------- | ------------ | ------------- | ------------- |
| Technology                   | CMR                | CMR                  | CMR          | SMR           | CMR           |
| Bays                         | 1-8                | 1-24                 | ?            | ?             | ?             |
| Capacity                     | 1-12TB             | 2-20TB               | 8TB          | 8TB           | 16 TB         |
| RPM                          | 5,400 RPM (3-6TB)  | 7200 RPM             | 7200 RPM     | 7200 RPM      | 7200 RPM      |
| RPM                          | 5,900 RPM (1-3TB)  | 7200 RPM             | 7200 RPM     | 7200 RPM      | 7200 RPM      |
| RPM                          | 7,200 RPM (8-12TB) | 7200 RPM             | 7200 RPM     | 7200 RPM      | 7200 RPM      |
| Speed                        | 180MB/s (1-12TB)   | 214-260MB/s (4-18TB) | 249 MB/s     | 255 MB/s      | 258 MB/s      |
| Cache                        | 64MB (1-4TB)       | 256 MB               | 256 MB       | 256 MB        | 256 MB        |
| Cache                        | 256MB (3-12TB)     | 256 MB               | 256 MB       | 256 MB        | 256 MB        |
| Power Consumption            | 10.1 W             | 10.1 W               | 12.81 W      | 11.03 W       | 9.31 W        |
| Power Consumption Rest       | 7.8 W              | 7.8 W                | 7.64 W       | 7.06 W        | 5.08 W        |
| Workload                     | 180TB/yr           | 300TB/yr             | 550TB/yr     | 550TB/yr      | 550TB/yr      |
| MTBF                         | 1 million          | 1 million            | 2 millions   | 2 millions    | 2.5 millions  |
| Warranty                     | 3 years            | 5 years              | 5 years      | 5 years       | 5 years       |
| Price                        | From $60 (2022)    | From $83  (2022)     | 249$ (2022)  | 249$ (2022)   | 249$ (2023)   |

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[5f504d1de7...](https://github.com/pytorch/pytorch/commit/5f504d1de74a5189f93e65aa9283fc4607b8631c)
#### Monday 2023-11-27 17:20:44 by Pedro Caldeira

Check for boolean values as argument on pow function.  (#114133)

Hello everyone! 😄
Also @lezcano , nice to meet you! :)

Sorry if I miss anything, this is my first time around here. 🙃

This PR basically makes the same behaviour for cuda when using `torch.pow`. Basically Python considers True as 1 and False as 0. I just added this check into `pow` function. From what I understood, when I do `.equal` for `Scalar` that is boolean, I'm sure that types match so that won't cause more trouble.

I know that the issue suggest to disable this case but that could be a little more complicated, in my humble opinion. And that can create some compability problems too, I guess.

My argument is that code below is correct for native language, so I guess it does makes sense sending booleans as Scalar.

```
$ x = True
$ x + x
2
```

This was my first test:
```
Python 3.12.0 | packaged by Anaconda, Inc. | (main, Oct  2 2023, 17:29:18) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.pow(torch.tensor([1, 2], device='cuda'), True)
tensor([1, 2], device='cuda:0')
>>> torch.pow(torch.tensor([1, 2]), True)
tensor([1, 2])
>>> torch.pow(torch.tensor([1, 2]), False)
tensor([1, 1])
>>> torch.pow(torch.tensor([1, 2], device='cuda'), False)
tensor([1, 1], device='cuda:0')
```

I've run `test_torch.py` and got following results, so my guess is that I didn't break anything. I was just looking for a test that uses linear regression, as suggested.

```
Ran 1619 tests in 52.363s

OK (skipped=111)
[TORCH_VITAL] Dataloader.enabled		 True
[TORCH_VITAL] Dataloader.basic_unit_test		 TEST_VALUE_STRING
[TORCH_VITAL] CUDA.used		 true

```
(I can paste whole log, if necessary)

If this is a bad idea overall, dont worry about it. It's not a big deal, it's actually a two line change 😅  so can we talk of how do things in a different strategy.

For the record I've signed the agreement already. And I didn't run linter because it's not working 😞 . Looks like PyYaml 6.0 is broken and there's a 6.0.1 fix already but I have no idea how to update that 😅

Fixes #113198

Pull Request resolved: https://github.com/pytorch/pytorch/pull/114133
Approved by: https://github.com/lezcano

---
## [Sebjen0209/Share-Money-Now](https://github.com/Sebjen0209/Share-Money-Now)@[c141c72336...](https://github.com/Sebjen0209/Share-Money-Now/commit/c141c7233697ef67a2228f9f1c1b623369e0370b)
#### Monday 2023-11-27 17:24:12 by vork10

Finally fixed stupid ass debt system

suck my wheener kotlin

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[a911b4db9d...](https://github.com/pytorch/pytorch/commit/a911b4db9d82238a1d423e2b4c0a3d700217f0c1)
#### Monday 2023-11-27 17:28:15 by voznesenskym

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
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[f367771f57...](https://github.com/cmss13-devs/cmss13/commit/f367771f5799b87257d92cb79db71bcd85b62f75)
#### Monday 2023-11-27 18:50:29 by Birdtalon

Eggsac carrier revival (#4716)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

[Forum Thread](https://forum.cm-ss13.com/t/eggsac-carrier-revival/4711)

# About the pull request

The concept of this PR is to find a middle ground between the current
eggsac carrier and the pre #4459 eggsac carrier.

This PR will make the following changes. (From this point "normal weeds"
can be substituted for "off hive weeds" Placing eggs on hive weeds is
**unchanged**.)

- Eggsac carrier can once again place eggs on normal weeds.
- Eggsac carrier can only place 4 eggs at once on normal weeds.
- If the Eggsac places more than 4 eggs on normal weeds, their oldest
placed egg will die. No hugger release.
- Eggs placed on normal weeds have a maximum lifetime of 5 MINUTES after
which they will die. No hugger release.
- Eggs placed on normal weeds have a 1 MINUTE life whilst the carrier is
further than 14 tiles away from them.
- If the carrier dies, all of their sustained eggs die.

# Explain why it's good for the game

Eggsac carrier at the moment is in a bit of a poor place and has gone
from being very strong to quite poor. Considering the limitation of
having to place only on hive weeds.
The majority of feedback I read against eggsac carrier was with the
quantity of eggs able to be placed, as well as the locations they can be
placed in, all across the map and with impunity.

This PR aims to address those concerns to make the eggsac both less
infuriating to play against while still being satisfying to play as a
frontline support or as a stealthy trapper.

Eggs can no longer be placed all over the map because of the 4 egg limit
off weeds, so the carrier has to think where they want to impact the
map. The carrier also has to stay within a reasonable distance to where
they are impacting with their eggs which localises their impact to their
immediate play area. The carrier also has to be more reactive to current
events as they cannot place an egg which then becomes useful 30 minutes
later.

Killing the carrier also has a small reward as in addition to removing a
xeno from the game, the eggs they are sustaining are cleared. If a
carrier is supporting the front and dies, the marines don't then have to
clear X number of eggs AFTER the kill.

# Testing Photographs and Procedure

1. Spawn as egg carrier.
2. Plant egg on normal weeds.
3. Move 15+ tiles away.
4. Wait 1 minute
5. OR Wait 5 minutes within 14 tiles.
6. Kill the carrier.

The 5 minute lifetime of the eggs will also clear the eggs in the case
that the carrier is admin deleted, or some other weird stuff happens
which doesn't result in a death. This will also catch carriers
de-evolving

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
add: Eggsac carrier can now place eggs on normal weeds to a maximum of 4
eggs.
add: Eggsac carrier eggs on normal weeds have an expiry date.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [mauvealerts/comprehensive-rust](https://github.com/mauvealerts/comprehensive-rust)@[c6af2a0d37...](https://github.com/mauvealerts/comprehensive-rust/commit/c6af2a0d3732ce8860c65ba7d1ebb23e58947619)
#### Monday 2023-11-27 19:09:47 by Martin Geisler

Mention how long each course day is (#1155)

Most classes run with 2.5 hours for the morning session and 2.5 hours
for the afternoon session.

I have tried running the course as 2 × 2.5 hours and 2 × 3 hours. My
experience was that people ended up getting really worn out after
spending 6 hours in total on Rust (7 hours including a lunch break).
However, the experience varies from group to group, so this is just a
recommendation.

---
## [esselfe/moonbase-core](https://github.com/esselfe/moonbase-core)@[f9e9967baa...](https://github.com/esselfe/moonbase-core/commit/f9e9967baa6204f76e052ab78ed759d137bbb69c)
#### Monday 2023-11-27 20:23:47 by Dave Brown

pciutils: Add hard dependency on wget

Even though nothing in core is supposed to be downloading anything from
the Internet as part of its build (because if you're building an ISO, by
definition you'll have an incomplete system), pciutils thinks that it's
special and insists on downloading a new pci.ids file just in case it's
changed in the last half hour or so.

(The pci.ids file chagnes on average once a month. It's not that
special.)

So until there's a better fix, just add another layer of stupid, ugly
hackwork on top of the existing pile of problems.

---
## [NoeSilent/catwalkstation](https://github.com/NoeSilent/catwalkstation)@[91af16bcbf...](https://github.com/NoeSilent/catwalkstation/commit/91af16bcbfd2dd363a89d846ae2acd6d655083c2)
#### Monday 2023-11-27 20:44:00 by zxaber

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
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[d0cfd909e0...](https://github.com/Danielkaas94/DTAP/commit/d0cfd909e060245b67ea0b0fffdd8661d89bb4e4)
#### Monday 2023-11-27 21:07:48 by Daniel Kaas Bundgaard Jørgensen

✝️☪️✡️☸️🗼 Tower Of Faith 🗼☸️✡️☪️✝️
Ooooh, the lonely boys
In their towers of faith
Ooooh, the lonely boys
Locked in their towers of faith

The prophet reclined
On the Golan Heights

Ohhh, the lonely boys

He said, this land is my land
To the Shiites

Ooooh, the lonely boys

And Jehova looked up from the sea of Galilee beneath
He said, I see you, you thief

This land is my land
And this sand is my sand
And this band is my band
Oh the lonely boys
Lookin' over their shoulder
Checkin out every boulder in the park
Where the gates are closed from hate
After dark

And the Pope rolled up in his armored van
He fell on his knees and kissed the land
He said something that I did not understand
It was in polish
Then up stepped an aide
He said, I will translate
Here is what His Holiness said:
'I am the Chief Jesuit.'
'This land is Jesus' land.'
'And that is all'
'All that there is to it.'
Hail Mary
Mother of God

And in New York City
The business man in his mohair suit
In the world trade center
Puffs on his cheroot
And he said,
Well I don't care who owns the desert sands
My brief
Is with the hydrocarbons underneath
And the sea of battle rages
Around the ancient tombs
And mother nature licks her wounds
And the lonely boys locked in their towers of faith
Who are nervous in the park
When the gates are closed after dark

Ooooh, the lonely boys
In their towers of faith
Ooooh, the lonely boys
Locked in their towers of faith

---
## [temporalio/temporal](https://github.com/temporalio/temporal)@[1be76e3583...](https://github.com/temporalio/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Monday 2023-11-27 21:33:16 by Tim Deeb-Swihart

Replace gogo/protobuf with google/protobuf (#5032)

**What changed?**

gogo/protobuf has been replaced with Google's official go compiler. 

**Why?**

gogo/protobuf has been deprecated for some time and the community is
moving on, building new tools (like vtproto) atop google's v2 compiler.

**How did you test it?**

`make test`

**Potential risks**

1. The change from embedded gogo-generated-structs to
google-generated-pointers-to-structs created a risk of nil pointer
exceptions. I've fixed all the ones our tests found but it's possible
there are more lurking in the new code.
2. This change may cause our performance to decrease. Certainly
encoding/deconding of proto objects will become slower, but the overuse
of pointers by the google compiler may negatively affect our overall
performance. We'll need to keep an eye on the GC stats
3. This breaks the HTTP API. We will not support [shortand payload
encoding](https://github.com/temporalio/proposals/blob/master/api/http-api.md#payload-formatting)
in this first pass; that will come once this initial work is in testing.

**Breaking changes for developers**

- `*time.Time` in proto structs will now be
[timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/protobuf@v1.31.0/types/known/timestamppb#section-documentation)
- `*time.Duration` will now be
[durationpb.Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb)
- V2-generated structs embed locks, so you cannot dereference them. `go
vet` will scream at you about this. If you need a copy, use
`proto.Clone`.
- If the performance of this sucks then I will either update our code
generator to add shallow-clone methods or hand-roll the ones we need
- Proto enums will, when formatted to JSON, now be in
`SCREAMING_SNAKE_CASE` rather than `PascalCase`. We decided (in
discussion with the SDK team) that now was as good a time as any to rip
the bandage off.
- Proto objects, or objects embedding protos, cannot be compared using
`reflect.DeepEqual` or _anything_ that uses it. This includes `testify`
and `mock` equality testers!
- You will need to use the `common/testing/protorequire`,
`common/testing/protoassert`, or `common/testing/protomock` packages
instead. I've implemented proto-compatible matchers and assertions there
for all cases I've encountered
- If you need `reflect.DeepEqual` for any reason you can use
`go.temporal.io/api/temporalproto.DeepEqual` instead

Note that history loading will not be impacted by the JSON changes: I
rewrote history loading to dynamically fix incoming history JSON data
(like all our other sdks); you can find this code in [my fork of our go
API](https://github.com/tdeebswihart/temporal-api-go/blob/master/internal/temporalhistoryv1/load.go)
alongside its tests.

**🚨Sharp Edges Introduced🚨**

Beware `*timestamppb.Timestamp.AsTime()`. If you need to extract a time
value from a proto time (timestamppb) **always** make sure to check
whether it's nil first. When the proto object is `nil` `AsTime()` will
return a non-zero time at the proto epoch: UTC midnight on January 1,
1970.

I've made this mistake multiple times during this transition and each
time it's been a pain to debug

**Is hotfix candidate?**

No.

---
## [keenomvictor/Contribute](https://github.com/keenomvictor/Contribute)@[e32e09d048...](https://github.com/keenomvictor/Contribute/commit/e32e09d04855b612640df9f7810b4b6742301009)
#### Monday 2023-11-27 21:33:39 by Victor Keenom

Create CREATIVE WEB


Personal data we collect
Microsoft collects data from you, through our interactions with you and through our products. You provide some of this data directly, and we get some of it by collecting data about your interactions, use, and experiences with our products. The data we collect depends on the context of your interactions with Microsoft and the choices you make, including your privacy settings and the products and features you use. We also obtain data about you from third parties.

If you represent an organization, such as a business or school, that utilizes Enterprise and Developer Products from Microsoft, please see the Enterprise and developer products section of this privacy statement to learn how we process your data. If you are an end user of a Microsoft product or a Microsoft account provided by your organization, please see the Products provided by your organization and the Microsoft account sections for more information.

You have choices when it comes to the technology you use and the data you share. When we ask you to provide personal data, you can decline. Many of our products require some personal data to provide you with a service. If you choose not to provide data -required to provide you with a product or feature, you cannot use that product or feature. Likewise, where we need to collect personal data by law or to enter into or carry out a contract with you, and you do not provide the data, we will not be able to enter into the contract; or if this relates to an existing product you are using, we may have to suspend or cancel it. We will notify you if this is the case at the time. Where providing the data is optional, and you choose not to share personal data, features like personalization that use such data will not work for you.

Learn more
Top of page
How we use personal data
Microsoft uses the data we collect to provide you with rich, interactive experiences. In particular, we use data to:

Provide our products, which includes updating, securing, and troubleshooting, as well as providing support. It also includes sharing data, when it is required to provide the service or carry out the transactions you request.
Improve and develop our products.
Personalize our products and make recommendations.
Advertise and market to you, which includes sending promotional communications, targeting advertising, and presenting you with relevant offers.
We also use the data to operate our business, which includes analyzing our performance, meeting our legal obligations, developing our workforce, and doing research.

In carrying out these purposes, we combine data we collect from different contexts (for example, from your use of two Microsoft products) or obtain from third parties to give you a more seamless, consistent, and personalized experience, to make informed business decisions, and for other legitimate purposes.

Our processing of personal data for these purposes includes both automated and manual (human) methods of processing. Our automated methods often are related to and supported by our manual methods. For example, to build, train, and improve the accuracy of our automated methods of processing (including artificial intelligence or AI), we manually review some of the predictions and inferences produced by the automated methods against the underlying data from which the predictions and inferences were made. For instance, with your permission and for the purpose of improving our speech recognition technologies, we manually review short snippets of voice data that we have taken steps to de-identify. This manual review may be conducted by Microsoft employees or vendors who are working on Microsoft’s behalf.

Learn more
Top of page
Reasons we share personal data
We share your personal data with your consent or to complete any transaction or provide any product you have requested or authorized. We also share data with Microsoft-controlled affiliates and subsidiaries; with vendors working on our behalf; when required by law or to respond to legal process; to protect our customers; to protect lives; to maintain the security of our products; and to protect the rights and property of Microsoft and its customers.

Please note that, as defined under certain U.S. state data privacy laws, “sharing” also relates to providing personal data to third parties for personalized advertising purposes. Please see the U.S. State Data Privacy section below and our U.S. State Data Privacy Laws Notice for more information.

Learn more
Top of page
How to access and control your personal data
You can also make choices about the collection and use of your data by Microsoft. You can control your personal data that Microsoft has obtained, and exercise your data protection rights, by contacting Microsoft or using various tools we provide. In some cases, your ability to access or control your personal data will be limited, as required or permitted by applicable law. How you can access or control your personal data will also depend on which products you use. For example, you can:

Control the use of your data for personalized advertising from Microsoft by visiting our opt-out page.
Choose whether you wish to receive promotional emails, SMS messages, telephone calls, and postal mail from Microsoft.
Access and clear some of your data through the Microsoft privacy dashboard.
Not all personal data processed by Microsoft can be accessed or controlled via the tools above. If you want to access or control personal data processed by Microsoft that is not available via the tools above or directly through the Microsoft products you use, you can always contact Microsoft at the address in the How to contact us section or by using our web form.

We provide aggregate metrics about user requests to exercise their data protection rights via the Microsoft Privacy Report.

Learn more
Top of page
Cookies and similar technologies
Cookies are small text files placed on your device to store data that can be recalled by a web server in the domain that placed the cookie. We use cookies and similar technologies for storing and honoring your preferences and settings, enabling you to sign in, providing interest-based advertising, combating fraud, analyzing how our products perform, and fulfilling other legitimate purposes. Microsoft apps use additional identifiers, such as the advertising ID in Windows described in the Advertising ID section of this privacy statement, for similar purposes.

We also use “web beacons” to help deliver cookies and gather usage and performance data. Our websites may include web beacons, cookies, or similar technologies from Microsoft affiliates and partners as well as third parties, such as service providers acting on our behalf.

Third party cookies may include: Social Media cookies designed to show you ads and content based on your social media profiles and activities on our websites; Analytics cookies to better understand how you and others use our websites so that we can make them better, and so the third parties can improve their own products and services; Advertising cookies to show you ads that are relevant to you; and Required cookies used to perform essential website functions. Where required, we obtain your consent prior to placing or using optional cookies that are not (i) strictly necessary to provide the website; or (ii) for the purpose of facilitating a communication.

Please see the Learn more section below for information about our use of third party cookies, web beacons and analytics services, and other similar technologies on our websites and services. For a list of the third parties that set cookies on our websites, including service providers acting on our behalf, please visit our third party cookie inventory. On some of our websites, a list of third parties is available directly on the site. The third parties on these sites may not be included in the list on our third party cookie inventory.

You have a variety of tools to control the data collected by cookies, web beacons, and similar technologies. For example, you can use controls in your internet browser to limit how the websites you visit are able to use cookies and to withdraw your consent by clearing or blocking cookies.

Learn more
Top of page
Products provided by your organization—notice to end users
If you use a Microsoft product with an account provided by an organization you are affiliated with, such as your work or school account, that organization can:

Control and administer your Microsoft product and product account, including controlling privacy-related settings of the product or product account.
Access and process your data, including the interaction data, diagnostic data, and the contents of your communications and files associated with your Microsoft product and product accounts.
If you lose access to your work or school account (in event of change of employment, for example), you may lose access to products and the content associated with those products, including those you acquired on your own behalf, if you used your work or school account to sign in to such products.

Many Microsoft products are intended for use by organizations, such as schools and businesses. Please see the Enterprise and developer products section of this privacy statement. If your organization provides you with access to Microsoft products, your use of the Microsoft products is subject to your organization's policies, if any. You should direct your privacy inquiries, including any requests to exercise your data protection rights, to your organization’s administrator. When you use social features in Microsoft products, other users in your network may see some of your activity. To learn more about the social features and other functionality, please review documentation or help content specific to the Microsoft product. Microsoft is not responsible for the privacy or security practices of our customers, which may differ from those set forth in this privacy statement.

When you use a Microsoft product provided by your organization, Microsoft’s processing of your personal data in connection with that product is governed by a contract between Microsoft and your organization. Microsoft processes your personal data to provide the product to your organization and you, and in some cases for Microsoft’s business operations related to providing the product as described in the Enterprise and developer products section. As mentioned above, if you have questions about Microsoft’s processing of your personal data in connection with providing products to your organization, please contact your organization. If you have questions about Microsoft’s business operations in connection with providing products to your organization as provided in the Product Terms, please contact Microsoft as described in the How to contact us section. For more information on our business operations, please see the Enterprise and developer products section.

---
## [JOE1904/NLP_research](https://github.com/JOE1904/NLP_research)@[6c4860eed5...](https://github.com/JOE1904/NLP_research/commit/6c4860eed58ae95d4b807dc8f47897b8ebea90fd)
#### Monday 2023-11-27 21:35:36 by Joan Job

New York City, often hailed as the "Capital of the World," is a dazzling mosaic of culture, commerce, and innovation. This iconic metropolis, situated at the southern tip of New York State, has earned a reputation as a global hub, defining the epitome of urban living. With a storied past that traces its roots back to the early 17th century, New York City has evolved into a dynamic and influential force, leaving an indelible mark on the world stage.  The city's skyline is a testament to human ambition and architectural prowess. Towering structures like the Empire State Building and One World Trade Center pierce the heavens, symbolizing the resilience and determination of a city that has weathered challenges and emerged stronger. The glittering lights of Times Square and the iconic Brooklyn Bridge further contribute to the city's unmistakable silhouette.  Central Park, an oasis of greenery amidst the concrete jungle, provides a serene escape for New Yorkers and visitors alike. This expansive urban park, designed by Frederick Law Olmsted and Calvert Vaux, offers a retreat from the frenetic pace of city life. Its meandering pathways, scenic lakes, and cultural attractions make it a cherished sanctuary for recreation and relaxation.  New York City's neighborhoods are microcosms of diversity, each with its distinct personality. From the artistic enclaves of Greenwich Village to the historic charm of Harlem, the city's boroughs are a vibrant tapestry of cultures and traditions. The subway system, a lifeline connecting these varied communities, ensures that the pulse of the city beats with unbridled energy.  Cultural institutions such as the Metropolitan Museum of Art and the Broadway theater district contribute to the city's status as a global cultural epicenter. The aroma of diverse cuisines wafts through the air, from the street vendors' carts to Michelin-starred restaurants, offering a culinary journey around the world.  New York City's resilience is embedded in its DNA, exemplified by its recovery from significant challenges, including the tragic events of September 11, 2001. The city's ability to rebuild and reinvent itself stands as a testament to the spirit of its inhabitants.  In the realm of finance, Wall Street serves as the epicenter of global economic activity. The New York Stock Exchange, nestled in the Financial District, symbolizes the city's role as a financial powerhouse. Beyond finance, the city fosters innovation in technology, media, and fashion, solidifying its status as a multifaceted economic engine.  New York City, with its iconic yellow taxis, diverse communities, and unmatched cultural offerings, remains an unparalleled destination. Whether strolling through Central Park, exploring the historic neighborhoods, or taking in the skyline from the High Line, every corner of the city tells a unique story. In the heartbeat of The Big Apple, every moment is an invitation to be part of the unparalleled energy and excitement that define New York City.

---
## [EdgeLordExe/Yogstation](https://github.com/EdgeLordExe/Yogstation)@[f39d74c3a6...](https://github.com/EdgeLordExe/Yogstation/commit/f39d74c3a66c41a5ebb468dc3d61b0787f8327be)
#### Monday 2023-11-27 21:44:19 by Waterpig

Invisible touch - this time for real (#20742)

* This was surprisingly easy

* Well this might be funny

* Hm

* Oh boy it's working

* I might be going insane

* Checks moved

---
## [pgcentralfoundation/pgrx](https://github.com/pgcentralfoundation/pgrx)@[733827aaab...](https://github.com/pgcentralfoundation/pgrx/commit/733827aaabf8bc29b3b029eb4fffe47ac34a2757)
#### Monday 2023-11-27 22:26:27 by Jubilee

Cut pgrx v0.11.1 (#1408)

Hello. Welcome to pgrx v0.11.1, a bugfix release that hopefully
addresses a very annoying persistent problem for users, especially ones
that were trying to use pgrx with Postgres 16! My changes in
b992f55eac931c49f72f142741fac7f2922b078c now steer bindgen towards
including the exact compiler-header directory that we require, instead
of relying on clang-sys to guess the right directory in ways that can go
horribly wrong. Unfortunately, this may make our build step more brittle
in certain cases. Please report issues as they arise, so that we can
continue to refine our build system, and eventually fix this in bindgen
proper!

This new behavior can still be disabled by setting
`PGRX_BINDGEN_NO_DETECT_INCLUDES`, as it is still a form of
autodetecting includes, but if this release fixes your build that was
previously relying on that or any other easily-removed hack, please let
us know!

Also, thanks to LuminousMonkey, you can now use pgrx on illumos, an
operating system descended from Solaris, with no changes to your source
code!

---
## [whataboutism-alos/pariahstation](https://github.com/whataboutism-alos/pariahstation)@[23aef65ad5...](https://github.com/whataboutism-alos/pariahstation/commit/23aef65ad58754e8327151ece4c0efa6d810e1ed)
#### Monday 2023-11-27 23:04:01 by SabreML

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607) (#704)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [whataboutism-alos/pariahstation](https://github.com/whataboutism-alos/pariahstation)@[c77fb1e795...](https://github.com/whataboutism-alos/pariahstation/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Monday 2023-11-27 23:04:01 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[790a82a3b1...](https://github.com/Buildstarted/linksfordevs/commit/790a82a3b138972dc9c38ae33059bc9c61b66b7c)
#### Monday 2023-11-27 23:09:22 by Ben Dornis

Updating: 11/27/2023 11:00:00 PM

 1. Added: Analyzing the Monoprice Blackbird HDCP 2.2 to 1.4 Down Converter
    (https://tomverbeure.github.io/2023/11/26/Monoprice-Blackbird-4K-Pro-HDCP-Converter.html)
 2. Added: Why I'm proud to be a non-code open source contributor and you should be too - OpenSource.net
    (https://opensource.net/non-code-open-source-contributions/)
 3. Added: Drinking distilled water
    (https://www.nayuki.io/page/drinking-distilled-water)
 4. Added: Mr. Jeff versus 20 Trillion Dollars
    (https://www.adama-platform.com/2023/11/26/jeff-vs-20-trillion.html)
 5. Added: Pomodoros and leverage ratios
    (https://hiandrewquinn.github.io/til-site/posts/pomodoros-and-leverage-ratios/)
 6. Added: devlead - Mattias Karlsson's Blog - Introducing BRI
    (https://www.devlead.se/posts/2023/2023-11-27-introducing-bri)
 7. Added: How Codebase Structure Shapes System Predictability
    (https://jorzel.github.io/how-codebase-structure-shapes-system-predictability/)
 8. Added: Connor's Blog
    (https://cedwards.xyz/instance-metadata-service-risks/)
 9. Added: The Sport of Indie Hacking
    (https://www.coryzue.com/writing/sport-of-indie-hacking/)
10. Added: Is Mastodon and the Fediverse good enough yet?
    (http://www.jaruzel.com/blog/is-mastodon-and-the-fediverse-good-enough-yet)
11. Added: Meta Quest 3—The Ugly and the Awesome – inconsequence
    (https://loewald.com/blog/2023/11/meta-quest-3-the-ugly-and-the-awesome/)
12. Added: Chopping the monolith in a smarter way
    (https://blog.frankel.ch/chopping-monolith-smarter-way/)
13. Added: Email notification for SSH logins » andreas.heigl.org
    (https://andreas.heigl.org/2023/11/17/email-notification-for-ssh-logins/)
14. Added: The Ultimate Beginner's Guide to Obsidian
    (https://www.dsebastien.net/the-ultimate-beginners-guide-to-obsidian/)
15. Added: The extent of GitOps
    (https://vaidik.in/the-extent-of-gitops/)
16. Added: Shadow DOM is for hiding your shame
    (https://tess.oconnor.cx/2023/11/shadow-dom)
17. Added: Build for yourself, all else will follow
    (https://parsam.io/build-for-yourself)
18. Added: Yusuf Aytas - The Power of Consistency
    (https://www.yusufaytas.com/the-power-of-consistency/)
19. Added: Understanding Chromes Coverage Panel
    (https://dainemawer.com/articles/understanding-chromes-coverage-panel)
20. Added: Demystifying Web Push Notifications
    (https://pqvst.com/2023/11/21/web-push-notifications/)
21. Added: I Have No Self-Control - What Should I Do?
    (https://durmonski.com/self-improvement/i-have-no-self-control/)
22. Added: Why the local development experience matters (a lot)
    (https://blog.moritzhaarmann.de/why-the-local-development-experience-matters-a-lot.html)
23. Added: Get more out of design reviews
    (https://grillopress.github.io/2023/11/26/get-more-out-of-design-reviews.html)
24. Added: Why do companies hire people to be idle a lot of the time?
    (https://ntietz.com/blog/why-do-companies-hire-people-to-be-idle-a-lot-of-the-time/)
25. Added: Fine-tuning Won't Add New Knowledge To Your Model
    (https://dylancastillo.co/fine-tuning-vs-rag/)
26. Added: Being popular
    (http://terrychay.com/article/popularity.shtml)
27. Added: Steve Bray: Why I joined Cloudflare
    (https://blog.cloudflare.com/steve-bray-why-i-joined-cloudflare/)
28. Added: trains.fyi
    (https://trains.fyi/)

Generation took: 00:09:09.3767623
 Maintenance update - cleaning up homepage and feed

---
## [sseshadri26/Boelter-Hall-Horror-Game](https://github.com/sseshadri26/Boelter-Hall-Horror-Game)@[4eec86d0a9...](https://github.com/sseshadri26/Boelter-Hall-Horror-Game/commit/4eec86d0a97995518dc531e29b5970db2c1c93ad)
#### Monday 2023-11-27 23:42:52 by Sudarshan Seshadri

Added *polish*

ahhhhhhh dont you love not spending time with family over thanksgiving and instead working on boelter for no god damn reason?
i sure do
anyways i fixed some visual bugs and modified that one infinite room to be a little cooler
and fixed a bug relating to portals and changed the map screen a bit and added the map to the cafe
and added another sign pointing to the cafe
and modified an incorrect room number
and adjusted some materials
i need to fucking stop
and/or work on another floor lmao
imma call this a vertical slice to make myself feel better

---
## [ashton314/rhombus-prototype](https://github.com/ashton314/rhombus-prototype)@[053523c4d8...](https://github.com/ashton314/rhombus-prototype/commit/053523c4d8d2b7475d8c0ec663bf6945b356a1f5)
#### Monday 2023-11-27 23:43:42 by Wing Hei Chan

revise `pattern` shorthand

Now that we allow a block before alts, the `pattern` syntax class
clause is redundant and arguably disfavored.  Not only that, it also
ties the meaning of the corresponding (unquote) binding operator to
it.  I think it'd be better that the syntax class clause simply be
removed, and the (unquote) binding operator be changed into an actual
shorthand for an inline syntax class matching.

My experience is that inline syntax classes are quite useful for the
same reason complex patterns in `syntax/parse` are useful, but using
them unfortunately requires an unnaturally large amount of rightward
shift.  Moreover, supplying `open` with inline syntax classes is
common but, again, looks ugly.  Therefore I believe `pattern` can
serve a better purpose this way.

Interestingly, syntax class clause macros originally can supply
spliced patterns through `pattern`.  This use is kept through changing
the expected expansion to a block optionally followed by alts.

A remaining problem is that the handling of repetitions *above* the
quasiquote doesn't seem to cover attributes.  Although this is not
directly related to `pattern` per se, the issue may be apparent when
the `pattern` binding is used in a composite binding form.  Again, the
fix should be generalizable.

---

