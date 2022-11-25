## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-24](docs/good-messages/2022/2022-11-24.md)


2,036,176 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,036,176 were push events containing 3,010,522 commit messages that amount to 217,040,232 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [Zenitheevee/Skyrat-tg](https://github.com/Zenitheevee/Skyrat-tg)@[f4335e5184...](https://github.com/Zenitheevee/Skyrat-tg/commit/f4335e5184da0a4643bab601ae11c59e9d411a6e)
#### Thursday 2022-11-24 00:10:31 by SkyratBot

[MIRROR] Fishing Odds Code Improvements and Rescue Hooks [MDB IGNORE] (#17697)

* Fishing Odds Code Improvements and Rescue Hooks (#71415)

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

* Fishing Odds Code Improvements and Rescue Hooks

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [pizie11/orbstation](https://github.com/pizie11/orbstation)@[84a85c827d...](https://github.com/pizie11/orbstation/commit/84a85c827d71b3326b482444a204711de38cf518)
#### Thursday 2022-11-24 00:12:13 by lizardqueenlexi

Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

---
## [Gofawful5/TOPIASTATION](https://github.com/Gofawful5/TOPIASTATION)@[25d4afc869...](https://github.com/Gofawful5/TOPIASTATION/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Thursday 2022-11-24 00:23:07 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[86a4c42483...](https://github.com/TaleStation/TaleStation/commit/86a4c4248392001b781bbf89244c89fb29fd27aa)
#### Thursday 2022-11-24 00:57:21 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes antag hud icons disappearing if mesons were equipped (#3370)

* Fixes antag hud icons disappearing if mesons were equipped (#71155)

## About The Pull Request

They sit on plane 0, IE the darkness plane. So if say, the darkness
plane was alpha'd away (which we have to do with see_blackness), then so
goes the hud element. stupid stupid stupid stupid

## Why It's Good For The Game

Fixes a derivation of #68087
Not all of it, since most of that came about pre plane cube and likely
has to do with z'd image shenanigines. I got it to replicate once
randomly but then it stopped. v annoying. There is a linked issue report
that mentions mesons however, which this does resolve.

## Changelog
:cl:
fix: You can now see antag hud icons AND see through walls. WOW
/:cl:

* Fixes antag hud icons disappearing if mesons were equipped

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[b979583140...](https://github.com/TaleStation/TaleStation/commit/b9795831401580576f10c094c4bb8354607bd6d0)
#### Thursday 2022-11-24 00:57:40 by TaleStationBot

[MIRROR] [MDB IGNORE] JSON Savefiles | Player Saves use JSON (#3245)

* JSON Savefiles | Player Saves use JSON (#70492)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
TODO:

- [x] DOCUMENT SHIT
- [x] UPDATE DOCUMENTATION

## About The Pull Request

Adds a new datum, which is intended to be a replacement for the stock
savefile type, json_savefile
As you can imagine, this is essentially just a wrapper around a json
file for reading/writing/manipulation that is intended to be a dropin
replacement for savefiles
It also have the ability to import stock savefiles and parse them into a
json tree

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Permission obtained from MSO and Mothblocks.

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
Not player facing, tested locally exhaustively to ensure it doesnt break
shit
:cl:
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

* JSON Savefiles | Player Saves use JSON

* some updates

* ok i think i fixed it :)

* loadouts touch

* you fucker

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [ASI-Factory/PCSX2-Fork-With-Plugins](https://github.com/ASI-Factory/PCSX2-Fork-With-Plugins)@[4d73147121...](https://github.com/ASI-Factory/PCSX2-Fork-With-Plugins/commit/4d731471214898389c6b39e459595b54e1b89ce3)
#### Thursday 2022-11-24 01:50:34 by RedDevilus

GameDB: Fixes to multiple games yet again

- Thrillville + Thrillville Off The Rails: Mad TFF / deinterlace 8 to stop shaking the whole game
- Forgotten Realm Demon Stone: Get rid of more blur
- ATV Offroad Fury 3: MTVU disabled which was an odd find to improve FPS
- Crimson Tears: Wild arms + Full Sprite for reducing bloom misalignment + note that Blending TFF might be better especialy when you use Software.
- Final Fantasy X: Texture in Rt for fixing endgame summons like Anima and The Magus Sisters
- No One Lives Forever: Mipmap full + trilinear + full blending needed to fix lighting

---
## [gadget-inc/dateilager](https://github.com/gadget-inc/dateilager)@[4348da1c34...](https://github.com/gadget-inc/dateilager/commit/4348da1c3488187e0d209ebd89a69ffa5adad753)
#### Thursday 2022-11-24 02:04:42 by Harry Brundage

Recover from arbitrary errors writing files by removing the thing we're about to write

I encountered a sequence of changes that DL didn't expect where I was creating a symlink at a path that was previously a folder full of files. There's a bunch of other annoying cases like this, where we should be able to go from any state on disk to any new incoming object type. The existing strategy did a bit of checking to see if stuff wasn't quite right, but I think we aught to be a bit more robust. The recovery strategy is always the same if we have a new incoming object: delete whatever is there so we can just write the new thing on top. If we're gonna do that, I think we can do it a bit more blindly. Instead of checking ahead of time for erroneous conditions (which also requires another syscall every write), we just blindly try to do the thing we need to do, and if it fails, remove whatever is there and try again. That way, we don't need to anticipate whatever fucked up case is on disk at the time and instead just blow it away. I also like this because it makes the fast path a bit faster where we do less checking up front and just let the kernel tell us we're doing something weird.

---
## [kenshen112/pcsx2](https://github.com/kenshen112/pcsx2)@[87abacc632...](https://github.com/kenshen112/pcsx2/commit/87abacc63264f9cf554cddf02973e0fc9cd2af77)
#### Thursday 2022-11-24 02:23:27 by RedDevilus

GameDB: Fix multiple games + maintenance

- Area 51: Half Pixel Normal vertex for lighting and other places
- Shrek 2: Basic mipmapping which kinda half fixes the sun missing
- Galaxy Angel II: Normal vertex which reduces misalignment
- Forgotten Realms - Demon Stone: Clamping Mode extra + preserve which will solve the occasional SPS + missing demo entry.
- Spyro Dawn of dragon: SW clut + sprite which doesn't make you vomit from the overbloomification and looks similar to the software renderer
- Castlevania Curse of darkness half sprite which will enlarge the font similar to software renderer + some missing fixes that were available on the Europe and America versions but not Japanese.
- Drakengard 1 + 2 (Also know as Drag-on Dragoon) : Partial (no hashcache) to avoid slow transitions and other areas. Adds missing Japanese Drakengard 1
- Urban reign: Partial texture preloading to fix performance issues in the gameplay
- Onimusha Warlord: Partial preloading to fix performance issues
- Sniper Elite: Fix sky lighting
- Maintenance that add spaces in the titles for Disc1of1 to Disc 1 of 1 and more...

---
## [ani2796/minioo-compiler](https://github.com/ani2796/minioo-compiler)@[845b87e835...](https://github.com/ani2796/minioo-compiler/commit/845b87e83551d08cb002e6ba61cdea71366e8ba6)
#### Thursday 2022-11-24 02:24:21 by Anirudh Sriram

Happy thanksgiving!

I thank the following people for making my life better:
- My parents and my brother
- Samriddhi
- My friends
- My professors
- my extended family

I hope to have a refreshing holiday, and if you're reading this, I wish
you the very best :)

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[24ae11ad6f...](https://github.com/Stalkeros2/Skyrat-tg/commit/24ae11ad6f6af9c0b6dab12986b95943f0cdf1f8)
#### Thursday 2022-11-24 03:11:20 by SkyratBot

[MIRROR] Adds a reagent injector component and BCI manipulators to all circuit labs [MDB IGNORE] (#17617)

* Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a reagent injector component and BCI manipulators to all circuit labs

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

---
## [mbernier/bdfs_sheet](https://github.com/mbernier/bdfs_sheet)@[2b59eeeacc...](https://github.com/mbernier/bdfs_sheet/commit/2b59eeeaccc4babca072d319740d34400c7e2b83)
#### Thursday 2022-11-24 03:30:35 by Matt Bernier

unit testing, caching for worksheetData, cleaned up inheritance problems

Added the ability to write and run unit tests with pytest, `pytest` will cause them to run
worksheetdata now pulls the data once, stores it locally - next is to reparse this data from cache rather than from worksheet
inheritence is a pain in the ass - was overwriting and doing stupid shit, cleaned that up

---
## [tydavis/git](https://github.com/tydavis/git)@[f1c903debd...](https://github.com/tydavis/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Thursday 2022-11-24 03:31:17 by Ævar Arnfjörð Bjarmason

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
## [gennyble/tep](https://github.com/gennyble/tep)@[4dbc6c80be...](https://github.com/gennyble/tep/commit/4dbc6c80bea07beb758605560a5c6f7c196ff465)
#### Thursday 2022-11-24 03:49:18 by Genevieve Zenla

Libify also fuck you that I can't seperate bin and lib dependencies

---
## [boost-entropy-typescript/apollo-server](https://github.com/boost-entropy-typescript/apollo-server)@[3fd7b5f261...](https://github.com/boost-entropy-typescript/apollo-server/commit/3fd7b5f26144a02e711037b7058a8471e9648bc8)
#### Thursday 2022-11-24 04:22:35 by Trevor Scheer

Update `@apollo/utils.keyvaluecache` dependency (#7187)

Previous releases of the `@apollo/utils.keyvaluecache` package
improperly specified the version range for its `lru-cache` dependency.

Fresh installs of our packages should receive the patch update since
it's careted, so this issue can be worked around by forcing the update
if you're using a lockfile. We should update it anyway since `2.0.0` is
invalid.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [Joker-V2/kernel_xiaomi_violet](https://github.com/Joker-V2/kernel_xiaomi_violet)@[4a645335f5...](https://github.com/Joker-V2/kernel_xiaomi_violet/commit/4a645335f5fc5378aab695e059cb709e570d3070)
#### Thursday 2022-11-24 04:49:51 by Peter Zijlstra

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
## [Harshil-Jani/git](https://github.com/Harshil-Jani/git)@[c793cdc630...](https://github.com/Harshil-Jani/git/commit/c793cdc6309283ed1d032a4b8cb2de3fdadabe83)
#### Thursday 2022-11-24 05:19:58 by Jeff King

branch: gracefully handle '-d' on orphan HEAD

When deleting a branch, "git branch -d" has a safety check that ensures
the branch is merged to its upstream (if any), or to HEAD. To do that,
naturally we try to resolve HEAD to a commit object. If we're on an
orphan branch (i.e., HEAD points to a branch that does not yet exist),
that will fail, and we'll bail with an error:

  $ git branch -d to-delete
  fatal: Couldn't look up commit object for HEAD

This usually isn't that big of a deal. The deletion would fail anyway,
since the branch isn't merged to HEAD, and you'd need to use "-D" (or
"-f"). And doing so skips the HEAD resolution, courtesy of 67affd5173
(git-branch -D: make it work even when on a yet-to-be-born branch,
2006-11-24).

But there are still two problems:

  1. The error message isn't very helpful. We should give the usual "not
     fully merged" message, which points the user at "branch -D". That
     was a problem even back in 67affd5173.

  2. Even without a HEAD, these days it's still possible for the
     deletion to succeed. After 67affd5173, commit 99c419c915 (branch
     -d: base the "already-merged" safety on the branch it merges with,
     2009-12-29) made it OK to delete a branch if it is merged to its
     upstream.

We can fix both by removing the die() in delete_branches() completely,
leaving head_rev NULL in this case. It's tempting to stop there, as it
appears at first glance that the rest of the code does the right thing
with a NULL. But sadly, it's not quite true.

We end up feeding the NULL to repo_is_descendant_of(). In the
traditional code path there, we call repo_in_merge_bases_many(). It
feeds the NULL to repo_parse_commit(), which is smart enough to return
an error, and we immediately return "no, it's not a descendant".

But there's an alternate code path: if we have a commit graph with
generation numbers, we end up in can_all_from_reach(), which does
eventually try to set a flag on the NULL commit and segfaults.

So instead, we'll teach the local branch_merged() helper to treat a NULL
as "not merged". This would be a little more elegant in in_merge_bases()
itself, but that function is called in a lot of places, and it's not
clear that quietly returning "not merged" is the right thing everywhere
(I'd expect in many cases, feeding a NULL is a sign of a bug).

There are four tests here:

  a. The first one confirms that deletion succeeds with an orphaned HEAD
     when the branch is merged to its upstream. This is case (2) above.

  b. Same, but with commit graphs enabled. Even if it is merged to
     upstream, we still check head_rev so that we can say "deleting
     because it's merged to upstream, even though it's not merged to
     HEAD". Without the second hunk in branch_merged(), this test would
     segfault in can_all_from_reach().

  c. The third one confirms that we correctly say "not merged to HEAD"
     when we can't resolve HEAD, and reject the deletion.

  d. Same, but with commit graphs enabled. Without the first hunk in
     branch_merged(), this one would segfault.

Reported-by: Martin von Zweigbergk <martinvonz@google.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[590847bdf7...](https://github.com/ZephyrTFA/tgstation/commit/590847bdf742b1e53f05ea700d48ec0676cdcf43)
#### Thursday 2022-11-24 06:10:29 by Andrew

Biogenerator tweaks, leather makes more belts and clothing (#71175)

## About The Pull Request

### Revamped the biogenerator UI:


https://user-images.githubusercontent.com/3625094/200973283-b703f21b-c747-493e-98d9-043eef86d410.mp4

### Changed biogenerator icon to use layers and see the biomass level:


https://user-images.githubusercontent.com/3625094/201396065-caeaa412-6676-46f6-875e-efa2dca34985.mp4

### Biogenerator rebalance:

- Now you don't need the beaker to print solid products.
- Biogenerator now accepts all food, not just plants.
- Biogenerator now treats all nutriment subtypes as nutriments, so
vitamins and proteins also turn into biomass.
- Biomass now has the same units as other reagents (you get 5 biomass
from 5 nutrient with tier 1 parts).
- Doubled the cost of all items and reagents. (biomass generation
reduced by 10 and prices - by 5)
- Chemicals output amounts are now in units and you can select how much
you want to output exactly. It will not let you specify more than the
size of container or above 50 units with one button click.
- Reduced the amount of stored items and introduced a limit to the
biomass, both tied to the matter bin tier.

### Recipes changes:

Made biogenerator more dumb by moving the clothing out from the
biogenerator designs, and extending leather recipes instead.

The biogenerator is a grinder/recycler style machine so it doesn't make
sense that it outputs clothing.
Also you need to make leather to craft the toolbelt, while you can't do
the same to craft job-specific belts.
Now you can print leather in biogenerator and craft the leather clothing
by using the leather in-hand.
And the rice hat is now crafted from bamboo, instead of biogenerator.

Also added paper to the biogenerator recipes as it makes stuff from
cellulose and barely anyone knows that you can craft paper from 1 log
and 50 water. And paper is needed in large quantities to craft some
items, like paper frames.

And it doesn't output a pack of rolling paper. It's dumb now. It prints
the rolling paper sheets instead.

## Why It's Good For The Game

Biogenerator had terrible UX and backend logic. I didn't improve much on
BE though, but now it should be less frustrating to use.

Also I hate how biogenerator is superior to all other means of obtaining
its products. It doesn't make sense to grow and grind wheat, for
instance, when you can just throw shit into biogenerator and get the
flour fast. And the costs are ridiculous - you can get a couple of
bottles of fertilizers just from one medium potato.

It honestly begs for more nerfing, at least to make the nutriment -
chemicals exchange rate 1:1.

The reason for the biomass cap is because people use it as a sink for
veggies and generate infinite biomass. Maybe the limit will make them
care more about the part upgrade and offload some of the veggies to the
fridge for the Cook.

Also it was weird that biogenerator could tailor some things, while
others have to be crafted in-hand. Now you can print leather and craft
all types of belts and leather clothing.

## Changelog
:cl:
refactor: biogenerator UI revamped
qol: biogenerator no longer requires beaker for materials, monkey cubes
and nori
balance: biogenerator accepts all food, not just plants
balance: biogenerator treats all nutriment subtypes as nutriments
(vitamins, protein, etc.)
balance: biogenerator product prices doubled
balance: biogenerator biomass storage is limited depending on the level
of matter bins
balance: cowboy boots recipe moved from crafting to leather recipes
balance: leather clothing & belt recipes moved from biogenerator to
leather recipes
balance: rice hat recipe moved from biogenerator to bamboo recipes
balance: biogenerator now outputs rolling paper sheets instead of a pack
add: biogenerator can now print paper
imageadd: biogenerator icons now use overlays, have emissive layer and
indicate the biomass volume
/:cl:

---
## [BiCffQ/trojan](https://github.com/BiCffQ/trojan)@[8665db29a3...](https://github.com/BiCffQ/trojan/commit/8665db29a309aa822b094952e0939de23cf93713)
#### Thursday 2022-11-24 08:39:48 by BiCffQ

Create License

 DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

---
## [DataDog/dd-trace-rb](https://github.com/DataDog/dd-trace-rb)@[e65a90939e...](https://github.com/DataDog/dd-trace-rb/commit/e65a90939e5d255dfea8e64a7ab38d81f75c0ab4)
#### Thursday 2022-11-24 08:58:55 by Ivo Anjo

[PROF-6556] Leave SIGPROF signal handler after disabling profiling

**What does this PR do?**:

This PR changes the teardown behavior of the `CpuAndWallTimeWorker`
collector to NOT remove its SIGPROF signal handler, and instead
leave behind an empty one.

**Motivation**:

While doing other experiments with signal handling, I discovered that
if the Ruby VM receives a SIGPROF signal without having a signal handler
setup, it defaults to the awful UNIX/POSIX behavior of instantly dieing
with a confusing "Profiling timer expired" message (that has nothing to
do with our profiler).

I reasoned that because signal handling is asynchronous, the following
theoretical situation may happen:
1. `CpuAndWallTimeWorker` sends SIGPROF signal
2. `CpuAndWallTimeWorker` notices request to shut down
3. `CpuAndWallTimeWorker` removes SIGPROF signal handler during teardown
4. Process receives SIGPROF, causing it to die.

I strongly suspect this may never happen in practice, but as
documented in the comment I added, the cost of my suspicion being
wrong is really high, so just-in-case I decided to instead leave
behind an empty signal handler.

**How to test the change?**:

Change includes test coverage. Additionally, you can doublecheck
the change in behavior by doing something like:

```
$ DD_TRACE_DEBUG=true DD_PROFILING_ENABLED=true DD_PROFILING_FORCE_ENABLE_NEW=true bundle exec ddtracerb exec pry
D, [2022-11-23T09:31:54.278186 #22975] DEBUG -- ddtrace: [ddtrace] (components.rb:384:in `startup!') Profiling started
[1] pry(main)> Datadog.configure { |c| c.profiling.enabled = false };;
D, [2022-11-23T09:32:08.580276 #22975] DEBUG -- ddtrace: [ddtrace] (profiler.rb:29:in `shutdown!') Shutting down profiler
[3] pry(main)> Process.kill("SIGPROF", Process.pid)
```

and you'll see that the Ruby process stays alive. If you do the
same thing to a process with no profiler, you'll see the process die
when you send it the SIGPROF signal.

---
## [freemo/about](https://github.com/freemo/about)@[3e36832c64...](https://github.com/freemo/about/commit/3e36832c64911f7748c2cd67ff4a93ed89e48f69)
#### Thursday 2022-11-24 09:15:40 by Jeffrey Phillips Freeman

Update blocked_instances.md

QOTO is **not** a free speech zone and has never engaged in harassment, it has strict rules against harassment and its rules explicitly state as such. Please review the public timeline, you wont find a single example backing up this slander.

You are almost certainly falling victim to the misinformation campaign perpetuated by the known **nazi** described in this post:

https://jeffreyfreeman.me/eugen-rochko-ceo-of-mastodon-found-to-support-nazis-agenda/

Quotes from the ToC of qoto:

> All cultures welcome
>
> Hate speech and harassment strictly forbidden.
>
> hate-based speech such as sexist, racist, or homophobic speech will not be tolerated, be kind to each other.
>
> QOTO aims to provide a community where our users do not fear being punished for their personal opinions. We do not allow people to disseminate ideologies that are abusive or violent towards others. Demonstrating support for or defending ideologies known to be violent or hateful is a bannable offense. This includes, but is not limited to: racial supremacy, anti-LGBTQ or anti-cis-gender/anti-straight, pro-genocide, child abuse or child pornography, etc. While we recognize questions and conversation regarding these topics are essential for a STEM community, in general, doing so in bad faith will result in immediate expulsion.
>
> What will get you banned: … Hate-based racism, sexism, and other hateful speech…

---
## [msm8917-dev/android_kernel_samsung_msm8917](https://github.com/msm8917-dev/android_kernel_samsung_msm8917)@[6bbece5ae4...](https://github.com/msm8917-dev/android_kernel_samsung_msm8917/commit/6bbece5ae49efc274a832461d087c14a21ecc34d)
#### Thursday 2022-11-24 09:41:48 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

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

---
## [toddhodes/AnimationThrowdown](https://github.com/toddhodes/AnimationThrowdown)@[8490ac33d8...](https://github.com/toddhodes/AnimationThrowdown/commit/8490ac33d8eea6e09a3e8e46d8d37d378bcfd539)
#### Thursday 2022-11-24 09:47:51 by Todd Hodes

end of musical, start animal

CM
+3 | Katz
+1 | Horseback Cotton | 20

PC
+   2 L Dreamland Band: 6**
+   2 L Hormone-iums Tina: 6**

Archer
+2 | Krieger's Clone Brothers | 85
+2 | Magic Breath Strips | 75

+  13 L Krieger: 6**

---
## [exhq/neOwOfetch](https://github.com/exhq/neOwOfetch)@[849bb1286f...](https://github.com/exhq/neOwOfetch/commit/849bb1286f9ab54003eb184b66c95d1e8990d3b9)
#### Thursday 2022-11-24 10:14:50 by echo

HOLY FUCKIJNG SHIT BINARY DOWNLOAD11!!!!1!!111!!!!11!1!

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[7d04edb6e2...](https://github.com/Thunder12345/tgstation/commit/7d04edb6e2927330906a7af89664b7a5ab3aa48c)
#### Thursday 2022-11-24 10:29:28 by Profakos

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
## [erikgrinaker/cockroach](https://github.com/erikgrinaker/cockroach)@[1d04cec7c5...](https://github.com/erikgrinaker/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Thursday 2022-11-24 10:59:01 by craig[bot]

Merge #91394 #91627

91394: changefeedccl: roachtest refactor and initial-scan-only r=samiskin a=samiskin

Epic: https://cockroachlabs.atlassian.net/browse/CRDB-19057

Changefeed roachtests were setup focused on running a workload for a specific duration and then quitting, making it difficult to run an `initial_scan_only` test that terminated upon Job success.

We as a team have also noticed a greater need to test and observe changefeeds running in production against real sinks to catch issues we are unable to mock or observe from simple unit tests.  This is currently a notable hassle as one has to set up each individual sink and run them, ensure the changefeed is pointing to the right URI, and then be able to monitor the metrics of this long running process.  

This change refactors the cdcBasicTest into distinct pieces that are then put together in a test.  This allows for easier experimentation with live tests, allowing us to spin up a cluster and a workload, run one or more changefeeds on it, set up a poller to print out job details,have an accessible grafana URL to view metrics, and wait for some completion condition.

Changing the specialized `runCDCKafkaAuth`, `runCDCBank`, and `runCDCSchemaRegistry` functions were left out of scope for this first big change.

The main APIs involved in basic roachtests are now:
- `newCDCTester`: This creates a tester struct to run the rest of the APIs and initializes the database
- `tester.runTPCCWorkload(tpccArgs)`: Starts a TPCC workload from the last node in the cluster
- `tester.runLedgerWorkload(ledgerArgs)`: Starts a Ledger workload from the last node in the cluster
- `tester.runFeedLatencyVerifier(changefeedJob, latencyTargets)`: starts a routine that monitors the changefeed latency until the tester is `Close`'d
- `tester.waitForWorkload`: waits for a workload started by `setupAndRunWorkload` to complete its duration
- `tester.startCRDBChaos`: This starts a Chaos routine that periodically shuts nodes down and brings them back up
- `tester.newChangefeed(feedArgs)`: starts a new changefeed on the cluster and returns `changefeedJob` object
- `changefeedJob.waitForCompletion`: waits for a changefeed to complete (either success or failure)
- `tester.startGrafana`: Sets up a grafana instance on the last node of the cluster and prints out a link to a grafana, this automatically runs unless `--skip-init` is provided.  If `--debug` is not used, `StopGrafana` will be called on test teardown to publish prometheus metrics to the artifacts directory.

An API that is going to be more useful for experimentation are:
- `changefeedJob.runFeedPoller(ctx, stopper, onInfo)`: runs a given callback every second with the changefeed info

Roachtests can be ran locally with the `--local` flag or on an existing cluster without destroying it afterwards with `--cluster="my-cluster" --debug`

Ex: After adding a new test (lets say `"cdc/my-test"`) to the `registerCDC` function you can keep running 
```bash
./dev build cockroach --cross # if changes made to crdb
./dev build roachtest         # if changes made to the test

./bin/roachtest run cdc/my-test --cluster="my-cluster" --debug
```
as you try out different changes or options.  If you want to try a set of steps against different versions of the app you could download those binaries and use the `--cockroach="path-to-binary"` flag to test against those instead.

If you want to set up a large TPCC database on a cluster and reuse it for tests this can be done with roachtests's `--wipe` and `--skip-init` flags.

Release note: None

91627: upgrade: introduce "permanent" upgrades r=andreimatei a=andreimatei

This patch introduces "permanent" upgrades - a type of upgrade that is
tied to a particular cluster version (just like the existing upgrades)
but that runs regardless of the version at which the cluster was
bootstrapped (in contrast with the existing upgrades that are not run
when they're associated with a cluster version <= the bootstrap
version). These upgrades are called "permanent" because they cannot be
deleted from the codebase at a later point, in contrast with the others
that are deleted once the version they're tied drops below
BinaryMinSupportedVersion).

Existing upgrades are explicitly or implicitly baked into the bootstrap
image of the binary that introduced them. For example, an upgrade that
creates a system table is only run when upgrading an existing,
older-version, cluster to the new version; it does not run for a cluster
bootstrapped by the binary that introduced the upgrade because the
respective system tables are also included in the bootstrap metadata.
For some upcoming upgrades, though, including them in the bootstrap
image is difficult. For example, creating a job record at bootstrap
time is proving to be difficult (the system.jobs table has indexes, so
you want to insert into it through SQL because figuring out the kv's for
a row is tedious, etc). This is where these new permanent upgrades come
in.

These permanent upgrades replace the `startupmigrations` that don't have
the `includedInBootstrap` field set. All such startupmigrations have
been copied over as upgrades. None of the current `startupmigrations`
have `includedInBootstrap` set (except one but that's dummy one since
the actual migration code has been deleted), so the startupmigrations
package is now deleted. That's a good thing - we had one too many
migrations frameworks.

These permanent upgrades, though, do not have exactly the same semantics
as the startupmigrations they replace. To the extent that there is a
difference, the new semantics are considered more desirable:
- startupmigrations run when a node that has the code for a particular
  migration startups up for the first time. In other words, the
  startupmigrations were not associated with a cluster version; they were
  associated with a binary version. Migrations can run while old-version
  nodes are still around.  This means that one cannot add a
  migration that is a problem for old nodes - e.g. a migration creating a
  job of a type that the old version wouldn't recognize.
- upgrades are tied to a cluster version - they only run when the
  cluster's active version moves past the upgrade's version. This stays
  the case for the new permanent migrations too, so a v2 node will not
  immediately run the permant migrations introduced since v1 when it joins
  a v1 cluster. Instead, the migrations will run when the cluster version
  is bumped. As such, the migrations can be backwards incompatible.

startupmigrations do arguably have a property that can be desirable:
when there are no backwards compatibility issues, the v2 node can rely
on the effects of the startupmigrations it knows about regardless of the
cluster version. In contrast, with upgrades, not only is a node unable
to simply assume that a particular upgrade has run during startup, but,
more than that, a node is not even able to look at a version gate during
the startup sequence in order to determine whether a particular upgrade
has run or not (because, in clusters that are bootstrapped at v2, the
active cluster version starts as v2 even before the upgrades run). This
is a fact of life for existing upgrades, and now becomes a fact of life
for permanent upgrades too. However, by the time user SQL traffic is
admitted on a node, the node can rely on version gates to correspond to
migrations that have run.

After thinking about it, this possible advantage of startupmigrations
doesn't seem too useful and so it's not reason enough to keep the
startupmigrations machinery around.

Since the relevant startupmigrations have been moved over to upgrades,
and the two libraries use different methods for not running the same
migration twice, a 23.1 node that comes up in a 22.2 cluster will re-run
the several permanent upgrades in question, even though they had already
run as startupmigrations. This is OK since both startupmigrations and
upgrades are idempotent. None of the current permanent upgrades are too
expensive.

Closes https://github.com/cockroachdb/cockroach/issues/73813

Release note: None
Epic: None

Co-authored-by: Shiranka Miskin <shiranka@cockroachlabs.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[460ab7adf5...](https://github.com/OrionTheFox/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Thursday 2022-11-24 11:46:14 by SkyratBot

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
## [ttgedeon/devops-course](https://github.com/ttgedeon/devops-course)@[ba6538e854...](https://github.com/ttgedeon/devops-course/commit/ba6538e8541489653695a7e68abb298a53014915)
#### Thursday 2022-11-24 12:35:18 by ttgedeon

The trip resume

I'm really happy to tell you that my trip has been the perfect moment
for me in my training that spanned on multiple years. I've been longing
for such enriching experiences all of my life and you just gave it to me.
I'll be gratefull to you all of my life🚕

---
## [Empire-Strikes-Back/Doc](https://github.com/Empire-Strikes-Back/Doc)@[fef53e893e...](https://github.com/Empire-Strikes-Back/Doc/commit/fef53e893e1560716444ca698f54f45fafceb21a)
#### Thursday 2022-11-24 12:41:55 by Doc

tell me you have a box fo severed human toes somewhere? - no

unlike TheViper I don't want to die off of posessions and members of the household

like Rich Roll briefly before he died was light

I hear Jesus - and I know abouthave and abundance, store, basketfuls and leftovers and breaking breads and fishes, under feet

let me not store any git history but one last commit which  defines now
I follow Jesus - I know about wide and narrow gate
let me have the namespace beer - so that garden and gardener and guests can run us programs in any city where caesar's drink is wine or beer
let my release be just one latest release named Doc.jar - simple as Rocket repairing Melano by spraying some magic gun in the air

:Brad-Lee-Cooper Zach
:Zach-Galifianakis Zaach
:Brad it's the first time I am part of something
:Zach if you wanted to be part of something why not jsut join the boyscouts?!

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[c39fffc1c9...](https://github.com/git-for-windows/git/commit/c39fffc1c90b174fe4ff40e0ce9f597e3d57778f)
#### Thursday 2022-11-24 12:49:17 by Ævar Arnfjörð Bjarmason

tests: start asserting that *.txt SYNOPSIS matches -h output

There's been a lot of incremental effort to make the SYNOPSIS output
in our documentation consistent with the -h output,
e.g. cbe485298bf (git reflog [expire|delete]: make -h output
consistent with SYNOPSIS, 2022-03-17) is one recent example, but that
effort has been an uphill battle due to the lack of regression
testing.

This adds such regression testing, we can parse out the SYNOPSIS
output with "sed", and it turns out it's relatively easy to normalize
it and the "-h" output to match on another.

We now ensure that we won't have regressions when it comes to the list
of commands in "expect_help_to_match_txt" below, and in subsequent
commits we'll make more of them consistent.

The naïve parser here gets quite a few things wrong, but it doesn't
need to be perfect, just good enough that we can compare /some/ of
this help output. There's no cases where the output would match except
for the parser's stupidity, it's all cases of e.g. comparing the *.txt
to non-parse_options() output.

Since that output is wildly different than the *.txt anyway let's
leave this for now, we can fix the parser some other time, or it won't
become necessary as we'll e.g. convert more things to using
parse_options().

Having a special-case for "merge-tree"'s 1f0c3a29da3 (merge-tree:
implement real merges, 2022-06-18) is a bit ugly, but preferred to
blessing that " (deprecated)" pattern for other commands. We'd
probably want to add some other way of marking deprecated commands in
the SYNOPSIS syntax. Syntactically 1f0c3a29da3's way of doing it is
indistinguishable from the command taking an optional literal
"deprecated" string as an argument.

Some of the issues that are left:

 * "git show -h", "git whatchanged -h" and "git reflog --oneline -h"
   all showing "git log" and "git show" usage output. I.e. the
   "builtin_log_usage" in builtin/log.c doesn't take into account what
   command we're running.

 * Commands which implement subcommands such as like
   "multi-pack-index", "notes", "remote" etc. having their subcommands
   in a very different order in the *.txt and *.c. Fixing it would
   require some verbose diffs, so it's been left alone for now.

 * Commands such as "format-patch" have a very long argument list in
   the *.txt, but just "[<options>]" in the *.c.

   What to do about these has been left out of this series, except to
   the extent that preceding commits changed "[<options>]" (or
   equivalent) to the list of options in cases where that list of
   options was tiny, or we clearly meant to exhaustively list the
   options in both *.txt and *.c.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Conga0/Mo_Creeps](https://github.com/Conga0/Mo_Creeps)@[92edf4f1fe...](https://github.com/Conga0/Mo_Creeps/commit/92edf4f1fe2f4fd31a15824c5a19124d7ec31a41)
#### Thursday 2022-11-24 13:32:03 by Conga Lyne

New Creep, Various Fixes, new item spawn

Fixed Reflective Weirdo having the wrong name ingame
Fixed rare Cool Minecart Hisii looking weird if Worse Enemies was enabled
Fixed Minecart Hisii not having status effect icons show up correctly
Fixed Particle Reduction setting not showing up in Mod Settings correctly
Fixed Delusional Shotgunner shooting the wrong projectile if playing with worse enemies
Fixed Toxic Immunity not properly removing toxic material immunity
Giant Toxic Worms are no longer health buffed in the tower, I enjoyed the feeling of having giant super buffed worms chasing after you in the tower, it made my heart pump with excitement; but at the same time, at the risk of sounding egotistical, I know not everyone may have the same level of experience in Noita that I do to create god wands from junk and a trigger. I think this will ultimately be for the best balance wise for less experienced players. Worry not though diehards, this update should introduce a new boss to test your mettle.
Abandoned Orchestra's Meteor attack is now more consistent, it will always fire two meteors but they'll be 90 degrees of you, homing towards you simultaneously
Added Skoude Twitch Event by request
Added Hungry Orb to the Fungal Caverns spawn pool
Removed something ominous from the Conjurer menu
Lowered chance to encounter secret potions in Pandora's Chest
New Creep: Ailment Drone

---
## [Trilbyspaceclone/sojourn-station](https://github.com/Trilbyspaceclone/sojourn-station)@[8620d970b0...](https://github.com/Trilbyspaceclone/sojourn-station/commit/8620d970b0aaa8d632e83a4dcc35547826f555df)
#### Thursday 2022-11-24 14:11:17 by DimmaDunk

Shields, sounds, holsters and more (#4169)

* Shields, sounds, holsters and more

- Better sound for blocking with shields, also sounds for stopping projectiles with them (and breaking)
- Ports the double belt pistol holder (pouch) and throwing knives rig (pouch) from Eris. With belt-worn sprites made by me.
- Adds the belt pistol holster and knife rig to the marshal vendors and absolutist printing disk
- Ports the Bulldozer shield from Eris, tweaks its recipe to include an actual closet
- Makes suit sensors spike in danger if someone's toxloss is at 70 or higher, since that is the point of liver failure
- On the same note, reduces the amount of organ damage from MSOF as it was too punishing, allowing for a better window of opportunity to save someone from dying
- Makes deployable barriers needed to be anchored to be able to brace your gun on it
- Adds most types of holsters to marshals vendors, ups their quantity
- Soteria Gauze and Ointment buffed on par with Church ones, to justify their convoluted hand-crafting method
- Makeshift AK and Luty added to random handmade guns to spawn
- Rangers get the double holster instead of the single one
- Adds a generic katana to loadout for four points
- Adds better sounds for the following emotes: male and female *sigh, *whistle (more variety), female *urah
- Adds snort and awhistle (targeted) emotes
- Makes a lot of audible emotes actually check if you're muzzled instead of magically being executed despite mouth coverage
- Adds some of the missing emotes to the *help list
- Adds hissing, meowing, and purring sound for cats, they will hiss at any ghosts they detect now!
- Fixes Mana from Heaven invisible sprite
- Claw and Baton energy drinks added overdose that causes organ damage at 60 units consumed
- Fixes incorrect Claw RED and BLUE sprites
- Claw Blue made actually made tastier
- Case Closer baton now contains atomic coffee instead of espresso (Marshal buff)
- Hay Fever claw energy improved citric formula
- Attempts to port Shields blocking projectiles functionality from Eris, but fails miserably (Tested not to work, but leaving the groundwork just in case)

* Nerfs liver failure damage even further

Random number 2 to 6 damage per tick

* Adds *zartan emote

Whistling of "For he's a jolly good fellow", GI Joe reference.

* Armor pen fix

Certain powered hammers were not properly inheriting armor pen somehow

* Preppers fairness

- Removes Sentinel Seeker from the random prepper mob spawn list
- Makes Sentinel Seeker a low spawner on par with Renders and nightmare stalkers as it shares similar stats with them
- Replaces certain prepper mob spawns with various low-chance Sentinel Seeker spawns on areas of high loot concentration (mech bays, prepper armory, near the excelsior disks, etc)
- Removes a trap spawner on the same room as Outsider spawn, as it can sometimes be a mine impossible to traverse on the only exit way
- Replaces hardspawn of Sentinel Seeker in Preppers medbay with a low chance for one, compensates by adding two more ranged mobs to the area

* Louder emotes

- Some female emotes were too low
- Typo fixes on bear rawr proc

* Apply suggestions from code review

This is a BYOND joke

Co-authored-by: Trilbyspaceclone <30435998+Trilbyspaceclone@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8c6dfd2a1d...](https://github.com/treckstar/yolo-octo-hipster/commit/8c6dfd2a1dc8b4e98afd86c854ebfe7195d1a9ab)
#### Thursday 2022-11-24 14:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Ariemakesthebest/FoxOS-Kernel](https://github.com/Ariemakesthebest/FoxOS-Kernel)@[8a4fbf88ec...](https://github.com/Ariemakesthebest/FoxOS-Kernel/commit/8a4fbf88ecec1d9fa5d44de8128dab15c5467473)
#### Thursday 2022-11-24 14:41:31 by Ariel Karson

Fuck you VSC
No longer do you put an error on my screen because of your stupid cargo test

---
## [infernoplus/PortJob](https://github.com/infernoplus/PortJob)@[ea7aaa9ee9...](https://github.com/infernoplus/PortJob/commit/ea7aaa9ee918ecb0c526624fc0b91430791eb048)
#### Thursday 2022-11-24 14:50:42 by InfernoPlus

Completely rewrote many parts of the project. We are now using a file resource handling class called Cache and MassConvert. MassConvert is a more efficent and large scale asset conversion class and Cache is a manager that keeps track of every file and the details for it. Interior cell generation is broken in this commit simply because I haven't re-enabled it. It works fine but I pulled the code out while working on asset stuff. Super simple object generation is now working in this commit. Doors get generated and placed. There is probably other stuff in this commit I forgor but it's k. Gaming. Oh yeah Overrides are a thing now too. And I think Layint and Interior cell merging is in this commit. Fuck bruh.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d27bbf8fe7...](https://github.com/TaleStation/TaleStation/commit/d27bbf8fe7154af2184fd275814a9369167857b6)
#### Thursday 2022-11-24 15:29:43 by Jolly

this is the most hacky way to do shit you have no fucking idea man (#3379)

---
## [Un10ck3d/rocket-stuff](https://github.com/Un10ck3d/rocket-stuff)@[6092e3837c...](https://github.com/Un10ck3d/rocket-stuff/commit/6092e3837c016773c6b2653e3e3a19fb66d420aa)
#### Thursday 2022-11-24 16:49:14 by Jonathan

ITS FINALY FUCKING WORKING OMFG THIS ACTUALLY SUCKS... ACTUALLY IT DOSNT IM JUST STUPID

---
## [adambujak/FALCON](https://github.com/adambujak/FALCON)@[ce60fbf68a...](https://github.com/adambujak/FALCON/commit/ce60fbf68adda4d05a71d9f95c063b549b7c4f76)
#### Thursday 2022-11-24 18:59:08 by Devin Bell

added beast attitude shit, quaternions are my bitch

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[2ea019f67a...](https://github.com/willior/Action_RPG_1/commit/2ea019f67a65c5f0bec41dd08dd7b9c7a1ec432b)
#### Thursday 2022-11-24 21:56:56 by willior

beta 5: more fixes; Crow re-integrated

fixed an issue where the player's IdleUp animation wasn't getting played. somehow, the animation track that set Sprite2D.frame had disappeared.
cleaned up HUD elements. the FormulaUI labels (quantity/level/ingredients) have been fixed. still need to fix the costs.
finally, re-integrated the Crow enemy, which was simple. first, re-named all "velocity" references to "movement". then, set the proper collision mask values on set_flying(value). also moved setting eye.frame to _physics_process(delta), as it doesn't need to update more than 60fps.

i should note that i tried opening the project in beta 6 and encountered many new errors. some were related to Animations (which as far as i can tell aren't going to be fixed until beta 7). i also got this error when attempting to set player resources on _ready():
Cannot use subscript operator on a base of type "null"
the error was in reference to how we set our player's techbook, pouch, and formulabook. i'll briefly explain how the system works:
on Player._ready(), we check if Global.get_attribute(inventory_ref) != null. "inventory_ref" is a string that acts as an identifer for each player's inventory (Player's inventory_ref = "inventory" and Player2's inventory_ref = "inventory_2"), which we store inside of a global dictionary, Global._attributes, when we change from one map scene to another (ie., when we collide with an Exit).
so, put simple, _attributes is the dictionary inside of which we store data when we change scene. 2 kinds of data are stored:
1. "spawn_point": spawn_number (int);
each map has a number of "spawn_points", which are numbered positions at which players can spawn. when we change scene (ie., collide with an Exit), the next scene needs to know where to spawn the player. so the Exit provides the _attributes dictionary with a "spawn_number".
2. "inventory": new_inventory (array);
when we spawn our player, we need to set their pouch (ingredients), their formulabook (formulas learned/equipped), and techbook (techs learned/equipped). on Player._ready(), we check if global._attributes != null, and grab the relevant values, if they exist. here is an example, setting the pouch:

pouch.set_ingredients(Global.get_attribute(inventory_ref)[0].get_ingredients())

"pouch" is the Player's pouch variable, meant to store his pouch resource.
"set_ingredients()" is a pouch method whose argument is an array of ingredients - an ingredient, in this case, is a size 2 dictionary: it has an ingredient_reference (which points to the ingredient resource, which contains ingredient data such as name and icon texture), and a quantity (which is an integer).
"Global.get_attribute(inventory_ref)[0]" is a Global method who argument is an _attributes key, which we store in inventory_ref (remember: player's inventory_ref = "inventory" and player2's inventory_ref = "inventory_2"). then, [0] is the index of the array (0: pouch; 1: formulabook; 2: techbook) returned by Global.get_attribute(). in this case, it returns a pouch resource. maybe a simple example to illustrate...
when Player 1 spawns, we know his inventory_ref = "inventory". so on _ready(), to set his pouch, he calls pouch.set_ingredients(Global.get_attribute("inventory")[0].get_ingredients()). Global._attributes is a dictionary with the "inventory" key; the value of _attributes.get("inventory") = [player.pouch, player.formulabook, player.techbook]. we know [0] is the pouch resource, and we know the pouch resource has a "get_ingredients()" method, which returns pouch._ingredients. our Players get initialized with a pouch resource already, so all it needs is to set its ingredients:

pouch.set_ingredients(Global.get_attribute(inventory_ref)[0].get_ingredients())

the operations could probably be split up more to make the code more readable. but, it works. like magic.

in the future, as a challenge, i could try converting the _attributes dictionary into simply an array. that way, it'd be keyless, and so no slow string comparisons would take place. the issue is that it's less scaleable/readable. what i mean is:

Global._attributes.get("spawn_point") will return an integer. we know that the integer is the value of the key "spawn_point";
Global._attributes.get("inventory") will return an array of Player Resources (a pouch, a formulabook, and a techbook, which we refer to collectively as an "inventory")

i'm proposing changing it to...

Global._attributes[0] returns the integer we currently refer to as "spawn_point".
Global.attributes[1] returns what we currently refer to as "inventory".
Global.attributes[2] returns what we currently refer to as "inventory_2", etc.

this is not a problem, currently. the game runs & loads extremely fast as it is. just something to consider.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[bee47a7d89...](https://github.com/tgstation/tgstation/commit/bee47a7d89c7548d85e5fa358cfb3b731035ab27)
#### Thursday 2022-11-24 22:00:34 by nevimer

Adds Some Supermatter Effects  (#67866)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This pull request adds a variety of Supermatter delamination effects to
make the crystal a bit more fun to watch and stare at. The initial
filter effects and animations are from Baystation12, but I have adapted
it to make it fun to watch!

It'll be a bit hard to explain in text, so this is the text explanation.

For normal running conditions, the Supermatter will emit pretty golden
rays, and a large campfire like that glow that grows and shrinks based
on it's power level.

![dreamseeker_vnw1BL7DNy](https://user-images.githubusercontent.com/77420409/174471609-7be70234-5eae-4839-b551-1c28145d6b60.gif)


For high power conditions, such as high O2 or CO2 amounts, the
Supermatter's rays will glow red and it will emit red light, aswell as
turn red (like before, unchanged).

https://user-images.githubusercontent.com/77420409/174471693-e191ee47-1a01-4b76-8570-9d12b994c2d4.mp4

When the conditions for a cascade, singularity, or a tesla are met, the
colours and rays emitting from the crystal will change to match!


https://user-images.githubusercontent.com/77420409/174471747-dffb3beb-dd38-42a1-a97b-7262dabd60af.mp4


https://user-images.githubusercontent.com/77420409/174471765-af1927e8-a48e-4fd5-a35c-6b3aa53c5add.mp4

Also, I've added more sucking power to the crystal during its final
countdown for DRAMATIC EFFECT. If the singularity conditions are met,
the supermatter will SUCK THINGS INTO IT, even if they are bolted to the
GROUND. Just like a singularity! It's REALLY COOL.
https://streamasaurus.com/sharing/singularity_full.mp4 <--17MB video.
UPDATE 1: New rays for the singulo


https://user-images.githubusercontent.com/77420409/174933219-0118748a-02da-40f8-9b99-06009e197cc8.mp4
UPDATE 2:
Singularity delamination final countdown effect??: 


https://user-images.githubusercontent.com/77420409/175421220-66bae109-204d-44ee-8a67-c18ce8eff3ba.mp4





When the supermatter has reached the FINAL COUNTDOWN but does NOT meet
the criteria for a singularity, it will simply YOINK everything
unwrenched towards, like a gravitational anomaly, range based on power
at the time. Not as crazy as the singularity. Most things will get
slapped against walls.

Here, have another cool delamination demo showing the criteria's
swapping mid countdown!
https://streamasaurus.com/sharing/modeswapping.mp4 <-- 17.5MB

I am likely missing something important from this body as I am drowsy
making this! I will update this body with anything I forgot to note that
I did.

## Why It's Good For The Game

The supermatter is a a very cool thing, but it could be cooler. I think
the visual experience could do with a bit of an upgrade, as visual
feedback is really cool and impressive to watch! You could tell more
about the crystal without looking at the console, but not everything or
precise numbers.

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
add: The Supermatter crystal will now emit rays of light, varying on
it's power level and situation.
code: improves a formatting and comment spelling
fix: The Causality field now actually shows up!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[e8be775da4...](https://github.com/Gofawful5/Skyrat-tg/commit/e8be775da4892a20186105a69bdc8b0832fba1cb)
#### Thursday 2022-11-24 22:42:57 by Paxilmaniac

Adds a collection of some kinda random greyscaled, recolorable clothes options (#16961)

* that's a few dmis

* a few sprite changes

* i hate making greyscale configs

* oh the misery

* 2:29 AM

* a few small things

* adds the stuff around more

* amazing work boss, this is why you're the best

---

