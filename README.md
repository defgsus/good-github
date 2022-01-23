## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-22](docs/good-messages/2022/2022-01-22.md)


1,477,828 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,477,828 were push events containing 2,061,134 commit messages that amount to 137,349,235 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [Robbbert/messui](https://github.com/Robbbert/messui)@[a49e215466...](https://github.com/Robbbert/messui/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Saturday 2022-01-22 00:14:08 by Firehawke

Apple II updates for January 2022 (#9189)

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Earth Science: Interplanetary Travel (cleanly cracked) [4am, Firehawke]
Isaac Newton and F.I.G. Newton (cleanly cracked) [4am, Firehawke]
Return to Reading: The Call of the Wild (cleanly cracked) [4am, Firehawke]
The German Hangman (cleanly cracked) [4am, Firehawke]
Legionnaire (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Bridge Tutor with Precision and Scientific Bidding (cleanly cracked) [4am, san inc, Firehawke]
The French Hangman (cleanly cracked) [4am, Firehawke]
The Russian Hangman (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Mickey's Space Adventure [4am, Firehawke]
The Environment Life Dynamic [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Stellar Power [4am, Firehawke]

New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Ken Uston's Professional Blackjack (Version 1.12) (cleanly cracked) [4am, Firehawke]
Dinosaur's Lunch (cleanly cracked) [4am, Firehawke]
Race Car Keys (cleanly cracked) [4am, Firehawke]
Functional Harmony: Basic Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Diatonic Seventh Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Borrowed and Altered Chords (cleanly cracked) [4am, Firehawke]
Building Reading Skills: The Letter-Sound Farm (cleanly cracked) [4am, Firehawke]
Follow Me (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

The German Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Russian Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Spanish Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Exploring Library Land (cleanly cracked) [4am, Firehawke]
Library Treasure Hunt (cleanly cracked) [4am, Firehawke]
Expedition U.S.A.! (cleanly cracked) [4am, Firehawke]
Codes and Cyphers (cleanly cracked) [4am, san inc, Firehawke]
Ripley's Believe It Or Not: Beginning Library Research Skills (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Glutton [4am, Firehawke]

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[eb384bd2d7...](https://github.com/Paxilmaniac/Skyrat-tg/commit/eb384bd2d72a5b23dd9785cc06815049d507d3d5)
#### Saturday 2022-01-22 00:53:54 by Useroth

Telemetry 'n shit (#10810)

* Refactors dbcore and limits the maximum amount of concurrent async queries to a variable amount (#59676)

Refactors dbcore to work off a subsystem if executed async and limits the maximum amount of concurrent async queries to 25.

This has been tested locally on a mysql docker image and there were no crashes (as long as you didn't run it with debug extools) + data was getting recorded fine.
Why It's Good For The Game

May or may not resolve terry crashes, however, each query creates a new thread which takes up 2mb, preventing the game from using that 2mb. This can lead to ooms if they stack up, e.g. due to poor connectivity. This solves that issue.

maintainer note: this did not actually resolve the crashes, but has value anyway. Crashes were sidestepped fixed by finding out Large Address Awareness works

cl
refactor: Refactors dbcore.dm to possibly resolve the crashes that happen on Terry.
/cl

* Fixes an oversight in database code and cleans up telemetry (#64177)

As it is right now, we never actually clear the temporary list processing_queries
So if the subsystem is for some reason unable to complete a run, we will just whip right back around to it again
If it's been long enough, this could even cause horrific log spam. There was just now a manuel round with roughly 30k undeleted query errors. not good.

But what was actually not deleting you may ask?
Well

When you create a db request, a 5 minute timer starts. after those 5 minutes are up, the request is qdeleted by the db subsystem
This is to prevent the creation of unused requests, and to handle requests that are never cleaned up

Telemetry code was creating all of its db requests inside a for loop that could check tick, and then later
attempting to call them in series

Since requests by default sleep, this almost always lead to undeleted queries, which harddel'd given long enough periods

I've fixed this by moving the data gathering away from the query creation
Why is it good for the game

I was working on atmos code, happy, safe in my delusion, when suddenly I got a ping from tattle freaking out over 200 undeleted queries a second
This resolves that issue, so I can once again live in peace
Changelog

cl
admin: Telemetry code will spam you with undeleted query logs much less often now!
server: Improved how the db subsystem handles undeleted queries, should never have an incident like that again
/cl

* Fixes an error in telemetry queries (#64205)

* Hardsynced time_track.dm with upstream

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[a2fa7799f3...](https://github.com/jlsnow301/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Saturday 2022-01-22 01:02:47 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[9c3f3b0b9e...](https://github.com/EaW-Team/equestria_dev/commit/9c3f3b0b9eee2b6932ebd4bff8e705e1a6c8316a)
#### Saturday 2022-01-22 01:21:25 by FettiFireware

Holy shit I can finally push this. Bartering Table 0.1

God kill me

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Saturday 2022-01-22 02:17:43 by Albert Liu

Add PresetService (User Presets Step 3) (#1164)

Final feature demo:

![Kapture 2022-01-13 at 23 36 00](https://user-images.githubusercontent.com/12578068/149469927-b62bfa43-4701-4498-a489-565aea36da2c.gif)

---------------------------

This PR is extracted from #1041 as step 2 of the User Preset feature.

rebase of picked commits pertaining to PresetServiceService onto Albert-UserDictionaryService

PresetService provides the ability to save and "apply" collections of settings (represented by objects) that a user might find convenient to save and apply as a group. These groups are called Presets.

PresetService uses DictionaryService to store presets (it creates kind of a *view* in the database sense, of the user dictionary, that only includes Presets)

Changes from last review (for Yicong)
 - Code comments
 - fixed subscription memory leak by using takeUntil(observable), where said observable completes on NgOndestroy
 - DictionaryService now attempts to init whenever client logs in (sorry, you'll have to re-review my changes to DictionaryService)
 - PresetService now has public ready promise/value member 
   - This indicates that its init isn't complete until DictionaryService's init is complete (which is async, and cant be awaited in the constructor)
 - DeletePreset now built into PresetService (don't know why I ever didn't have that)
 - Revert Changes to Styles.scss to fix Karma test runner interface (I originally changed them as a workaround for an ng-zorro component that's no longer used)

 Note: for this step, I had less time and more complex code to test. I'm not sure I caught all the bugs, but it passes unit tests.
The quality of the code in this pr is lesser, in my opinion, so You'll have to be a little more careful on my behalf.



Co-authored-by: Zuozhi Wang <zuozhiw@gmail.com>
Co-authored-by: Yicong Huang <17627829+Yicong-Huang@users.noreply.github.com>

---
## [BakaKaito/Mergebot.NET](https://github.com/BakaKaito/Mergebot.NET)@[ef9d96585d...](https://github.com/BakaKaito/Mergebot.NET/commit/ef9d96585da09614c4dad5869680cb739e1042f7)
#### Saturday 2022-01-22 02:30:10 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [vode-code/CEV-Eris](https://github.com/vode-code/CEV-Eris)@[c3fb43155f...](https://github.com/vode-code/CEV-Eris/commit/c3fb43155f41f2f0409bd4269b1a10546f6d3a97)
#### Saturday 2022-01-22 04:10:51 by Wouju

Reality Complicator, i luv me terror button (#6836)

* Yeah we're back

* Revert "Yeah we're back"

This reverts commit ddb5b5ed146c154be8cc6089621f6b332eb3086f.

* complicatorium

* map shit

* Update code/game/objects/items/complicator.dm

Co-authored-by: hyperioo <64754494+hyperioo@users.noreply.github.com>

---
## [watchexec/cargo-watch](https://github.com/watchexec/cargo-watch)@[8bf93b44e3...](https://github.com/watchexec/cargo-watch/commit/8bf93b44e3dafea90f4006cf885d2855c213e702)
#### Saturday 2022-01-22 04:32:20 by Félix Saparelli

Disable rpms for now

https://github.com/cat-in-136/cargo-generate-rpm/issues/21

fuck you aesni

---
## [WorshipMeOrElse/find-the-gorts](https://github.com/WorshipMeOrElse/find-the-gorts)@[6f4ed2c39b...](https://github.com/WorshipMeOrElse/find-the-gorts/commit/6f4ed2c39bb52005ef5b128da8f51361aaee3d02)
#### Saturday 2022-01-22 04:47:01 by WorshipMeOrElse

optimized touchscript and localpartscript

holy shit this took half the entire fucking day

now all I have to do is optimize the reposcripts

fuck you gamma

---
## [metalgearsloth/RobustToolbox](https://github.com/metalgearsloth/RobustToolbox)@[d66e660a39...](https://github.com/metalgearsloth/RobustToolbox/commit/d66e660a39196041ead1cf0fcf922ab8b28c774f)
#### Saturday 2022-01-22 05:52:30 by metalgearsloth

holy shit this is disgusting now I remember why I hate transformcomp

---
## [GuildedThorn/PocketMine-MP](https://github.com/GuildedThorn/PocketMine-MP)@[d9c70cb176...](https://github.com/GuildedThorn/PocketMine-MP/commit/d9c70cb176c25bd67f7cab384428d6a9165f4539)
#### Saturday 2022-01-22 05:59:36 by Dylan K. Taylor

start.cmd: prevent idiotic behaviour when paths contain characters such as brackets
god I hate this shit so much

---
## [saboooor/Pup](https://github.com/saboooor/Pup)@[d72bc6240c...](https://github.com/saboooor/Pup/commit/d72bc6240c857eb1ecec3d725e5df054ad407383)
#### Saturday 2022-01-22 07:02:05 by Saboor

fuck colorthief it's been really fucking problematic holy fucking shit i'll do this later fuck this i'd rather just use random colors instead ffs

---
## [Daedliy/BorderShapes](https://github.com/Daedliy/BorderShapes)@[0f90b83f31...](https://github.com/Daedliy/BorderShapes/commit/0f90b83f31d0a2b9006b9c5553ded4a89d942923)
#### Saturday 2022-01-22 07:22:19 by Kewl Sage

some things from cumcord

Welcome to the cum zone - Only cum inside anime girls - Quivering clit, double jointed pussy - Fresh balls, elegant ejaculation - First the kiss, then the cum - My dick is in love with pain - Co-op cock torture - Stuff my dick into a furnace - Stitch my cock shut - Pressure cook my greasy balls - Cumblast me and make it snappy - Cum, cum, cum, cum, cum, cum, cum, cum - Cum, cum, cum, cum, cum, cum, cum, cum - Cum, cum, cum, cum, cum, cum, cum, cum - Cum, cum, cum, cum, cum, cum, cum, cum - What's all the cummotion? - My dad fell into a cum shaft - My dad glazed my face with cum - Fertilize a baby with hunk spunk - Cum spunk in my trunk - Cum craving 👎🏿 - Cum drippin' cunt - Cummy Rae Jepsen - Cum me maybe - Cummy bottom boy - Night of the living cum - Nefarious cum mastermind - Cum makes me fearless - Cum crammer, cock slammer - Cum slammed ya mum - Mail your mums pieces of my dick - Bazinga! - Chug the cum, fug ya mum - Fuck my asshole full of cum - Three little words - Get fucked, nerd - Cum stuffer, jenkem huffer - Fuck my cum puddle - Bottom stuffer, semen huffer - Would love a gator to fuck me - Undercooked baby pig penises - Help my dogs get a huge boner - Water bong full of cat cum - Accidentally fucked my own ass - I barely had any dicks inside me - Who ate all my cum? A mystery - Cum detective hot on the trail - Bees make honey, I make cummy

---
## [newstools/2022-punch-nigeria](https://github.com/newstools/2022-punch-nigeria)@[a7a30eb8ad...](https://github.com/newstools/2022-punch-nigeria/commit/a7a30eb8addb643f09e8a2278e352015ee3d12a4)
#### Saturday 2022-01-22 07:37:24 by Billy Einkamerer

Created Text For URL [punchng.com/how-violent-gang-stabbed-my-brother-to-death-during-enugu-church-bazaar-lagos-based-man/]

---
## [newstools/2022-punch-nigeria](https://github.com/newstools/2022-punch-nigeria)@[9de4649146...](https://github.com/newstools/2022-punch-nigeria/commit/9de464914635dce4ec7fe7321c00afd763050c1b)
#### Saturday 2022-01-22 07:42:30 by Billy Einkamerer

Created Text For URL [punchng.com/i-suspect-boyfriend-took-my-daughters-blood-for-ritual-after-killing-her-edo-man/]

---
## [asynts/pico-os](https://github.com/asynts/pico-os)@[d8f3eec557...](https://github.com/asynts/pico-os/commit/d8f3eec5574a14a4e382612e71a5c959f89ff800)
#### Saturday 2022-01-22 10:57:13 by Paul Scharnofske

Boot: Correctly load the boot loader from GDB

I thought that when we used 'load' from GDB, this would be equivalent to
putting things into flash and pushing reset, but this is not the case.

Instead, it loads everything to the load-memory-address and then jumps
to the entry address.  This means that the boot loader could be executed
at '0x10000000' or '0x20000000' depending on context.

This is really ugly in my opinion and I will do it slightly differently.
Instead, there is a special 'boot_0_openocd_entry' function which is
marked as entry point.  GDB will call this function which relays to
'boot_1_reset', while the reset will trigger it directly.

Therefore, in theory, both contexts would result in the same behaviour
which is much easier to reason about.  However, this doesn't quite work
at the moment, because of some issues with the linker (refer to 0003).

---
## [YumeMichi/kernel_oneplus_sm8250](https://github.com/YumeMichi/kernel_oneplus_sm8250)@[6c130130cf...](https://github.com/YumeMichi/kernel_oneplus_sm8250/commit/6c130130cfc241333bf98688214b14f0694fa31e)
#### Saturday 2022-01-22 11:18:40 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [xameryn/CatJam](https://github.com/xameryn/CatJam)@[ad6a01ff3d...](https://github.com/xameryn/CatJam/commit/ad6a01ff3d43eb42455953e42c83ba11c3548f81)
#### Saturday 2022-01-22 12:14:17 by Science-Bird

Overall command loop restructure, send message/return function, various cleanup, undefined $pref fix, also fuck you it's "unknown commands" now

---
## [SwiftOS-ROM/android_frameworks_base](https://github.com/SwiftOS-ROM/android_frameworks_base)@[1ba101f82e...](https://github.com/SwiftOS-ROM/android_frameworks_base/commit/1ba101f82eae4e54293428480fbcbfd1c58359c8)
#### Saturday 2022-01-22 12:22:22 by Steve Howard

Improve accelerometer-based orientation sensing.

There were three main complains about orientation sensing:
* Switching to landscape when putting a device down on a table (or picking it up)
* Changing orientation due to road bumps or vehicle vibrations while in a car dock
* Switching to upside-down too easily

This change includes three primary enhancements.

First, we run the accelerometer output through a lowpass filter before considering its orientation.  This avoids glitches due to brief phone movement, particularly when the phone hits a table.  The filter uses a very low default time constant of 200ms to retain responsiveness (note the samping period is ~200ms, so the effect of this filtering is pretty mild).  At tilt angles beyond 45 degrees, however, we increase the time constant to 600ms, which helps greatly with avoiding glitches picking the phone up from a table.  It does introduce some sluggishness when rotating while the phone is tilted back, i.e. being used in one's lap.

It's also worth mentioning that the accelerometer output on Sapphire appears to be pre-lowpass-filtered with a time constant of around 500ms, making this less necessary on that device, but the added effect doesn't noticeably degrade user experience in my opinion.

Second, we check the magnitude of the raw accelerometer output.  If it deviates from the strength of gravity by more than one m/s^2, we distrust the data, since that implies the device is under external acceleration and the sensor data doesn't accurately reflect orientation.  This helps avoid glitches due to shocks and vibrations, as in the car dock scenario.  However, rather than ignore the data entirely, we filter it with a very high time constant (5 sec).  As a result, if the device is rotated while vibrating, even if we never pick up a clean sample, we will eventually detect the orientation switch.  Of course, with a sampling period of 200ms, we're prone to aliasing, but that seems like a highly unlikely corner case.

Third, we restrict transitions to upside-down orientation to a much narrower range, both in terms of orientation and tilt.  This should prevent upside-down mode from activating in most cases where it's not desired.

I also updated a lot of stale documentation, added a lot of documentation, and cleaned up a lot of the code, so as to make this (often subtle) code as transparent as possible.

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[818c3b4a74...](https://github.com/repinger/exynos9611_m21_kernel/commit/818c3b4a74b34f42f3fda32b3fb20b44204eac70)
#### Saturday 2022-01-22 13:53:52 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>

---
## [envoylabs/whoami-ui](https://github.com/envoylabs/whoami-ui)@[ce405baf67...](https://github.com/envoylabs/whoami-ui/commit/ce405baf679d9971288a61c78a69f76171c42855)
#### Saturday 2022-01-22 15:38:25 by the-frey

Basic messaging (#96)

* basic msg list

* maybe cracked the cofx thing

* whatever, fuck it

* resolve the stupid type issues

* Make short token page work - needs refactor

* i am once again asking for you to bloody compile

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[86a061f649...](https://github.com/cyberitsolutions/bootstrap2020/commit/86a061f649c7d7e19e5389896e277daf5d3d59b8)
#### Saturday 2022-01-22 15:50:44 by Trent W. Buck

inkscape doc: remove unusable 0.91 extension hooks

16:23 <twb> 16:22 <twb> So now that the help URLs are implemented in C++ instead of python "extensions", I can't see how to change the URLs from https://X to file:///Y without recompiling the entire inkscape package
16:24 <twb> https://sources.debian.org/src/inkscape/1.1.1-2%7Ebpo11+1/src/verbs.cpp/#L2051-L2101
16:27 <twb> I put "echo "$@" >/tmp/delete-me" at the top of /usr/bin/xdg-open, and Inkscape > Help > Manual does not cause /tmp/delete-me to exist
16:27 <twb> So can't hook it there
16:29 <twb> ron: I want you to say "yes, I accept this regression".  Inkscape's documentation is all online.  To keep [REDACTED] happy, we hacked it so Inkscape's Help menu would open local copies we downloaded.  I can still download, but I cannot hack the menu anymore.
16:29 <twb> ron: so if $site wants inkscape help to work in Debian 11, they will need to have internet, and whitelist stuff in squid access rules
16:30 <twb> The only "show stopper" one I think is really annoying is: https://inkscape.org/doc/keys-1.1.x.html
16:30 <ron> ah, I'm fine with whitelisting the inkscape doc
16:30 <twb> OK cool
16:30 <ron> implying they must have net access
16:30 <ron> [REDACTED] misses out
16:30 <ron> boo hoo
16:31 <twb> The other compromise thing I could do is make a start menu item "Inkscape Documentation" that just opens chromium.
16:31 <twb> That's not hard
16:31 <mike> twb: Did you try exo-open instead of xdg-open? That's the other one I see pop up every now and then
16:32 <twb> AFAIK xdg-open is what runs exo-open
16:32 <twb> I was doing a quick-and-dirty test on my gnome environment so I didn't test that
16:33 <mike> xdg does call exo, but doesn't mean things can't call it directly
16:34 <twb> fair
16:34 <mike> It definitely honours XFCE's "preferred applications" setting. Inkscape opened Chrome, then I changed it from Chrome to Chromium and Inkscape opened Chromium
16:34 <twb> I don't *really* want to intercept every call to xdg-open/exo-open anyway
16:37 <mike> twb: Got this by stracing it: [pid 174670] execve("/bin/sh", ["/bin/sh", "-e", "-u", "-c", "export GIO_LAUNCHED_DESKTOP_FILE_PID=$$; exec \"$@\"", "sh", "exo-open", "--launch", "WebBrowser", "http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php"], 0x5596c8443910 /* 54 vars */ <unfinished ...>
16:37 <mike> Which then called this: [pid 174670] execve("/usr/bin/exo-open", ["exo-open", "--launch", "WebBrowser", "http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php"], 0x564af10ac068 /* 55 vars */) = 0
16:37 <twb> mike: ah thanks
16:37 <twb> So OK we can fix this
16:37 <mike> Not worth digging any deeper into that path
16:38 <mike> We could wrap exo-open, yeah
16:38 <mike> Not sure I like it, but it's viable

---
## [JudeForNothing/RebekahCurse](https://github.com/JudeForNothing/RebekahCurse)@[c6fdeda88e...](https://github.com/JudeForNothing/RebekahCurse/commit/c6fdeda88e30c1e14b9253e19de1b9787e31fd81)
#### Saturday 2022-01-22 16:35:53 by JudeForNothing

Rebekah 2.actual 8

When Soul Heart Personality Rebekah teleports and losing the damage buff, she no longer does the poof effect
Soul Heart Rebekah teleporting in now has dust sucking in effect
Changed starting portrait sprite of Rebekah
Fixed bug where Eternal Fire attacks actualy shoot like a shotgun, this is actually not intended!
Love Love particles should now only release at dying vulnerable enemies
Hugs and Roses now physically appears on Red Personality
-splash particles are now on the gun instead directly on top of Rebekah
Special Beam of Soul now has a different color

---
## [polygoblyn/MonkeStation](https://github.com/polygoblyn/MonkeStation)@[040b7ff839...](https://github.com/polygoblyn/MonkeStation/commit/040b7ff839d51d4db2ce1747f92312e0925bccd2)
#### Saturday 2022-01-22 16:56:28 by Zonespace

Adds Flavor Text (#48)

* lgtm

* aaaAAAA

* might be better idk

* flavor-examine

* info

* haaa fuck you github

---
## [rorydale/pointbreakradio](https://github.com/rorydale/pointbreakradio)@[25c0b04a56...](https://github.com/rorydale/pointbreakradio/commit/25c0b04a56bf2554f2c332dac51cef8faef7446e)
#### Saturday 2022-01-22 17:21:20 by Rory Dale

2022-01-22

Saturday, January 22nd, 2022 - the Meat Loaf show! With the unpleasant and yet inevitable arrival of another notification of an artist passing, came many messages from friends and family asking about a Meat Loaf show, which demonstrates how far reaching his appeal was. A guilty pleasure for some, and a top ten artist for others, Meat Loaf was certainly musical Marmite. I love the theatricality and the pure performance, but I didn't know too much outside of the Bat Out of Hell record - which is one of my absolute favourites! Today's show is a play-through of Meat Loaf from his earliest recordings to his last album. Here's to hoping that he and Jim Steinman are working on new material together again.

---
## [newstools/2022-the-citizen](https://github.com/newstools/2022-the-citizen)@[0ba3c6825f...](https://github.com/newstools/2022-the-citizen/commit/0ba3c6825fabc7b836285c2278f7f14df9489b6a)
#### Saturday 2022-01-22 17:26:04 by Billy Einkamerer

Created Text For URL [www.citizen.co.za/news/south-africa/crime/2984502/police-officer-gets-23-years-in-jail-for-murder-of-ex-girlfriend-and-her-boyfriend/]

---
## [eRJx/supertux](https://github.com/eRJx/supertux)@[9c636e2e35...](https://github.com/eRJx/supertux/commit/9c636e2e3526f5d07e43a5ff015fc308538d1aa8)
#### Saturday 2022-01-22 17:32:58 by Ocelot

Level Improvements

Level improvements to Bonus Island III. This is part of my project to make all Bonus Islands have possible perfect objectives.

- Big Tux can now get to the secret in "Cave Run" where previously he would hit his head.
- "You can't Climb Higher than the Clouds" fixed unrealistic level target time.
- Enemy fixes in "Another Cold Day" stopping enemies from killing themselves.
- Lantern position fixed in "Cold Cavern" as well as 1 bad enemy placement at the end.
- Fixed unrealistic Target times for "Crystal Sunset", " Crystal Fields", "The Dark Castle" and the other "The Dark Castle", "Deep, deeper...", "...deepest!", "Circles", "Entering the castle", "After the Glaciers", "Snowfall alert", "My Penny is over the ocean", "To rain or not to rain..." (both variants), and "Under the Ice".
- Fixed the snowball that killed itself via enemy cramming in "Out on the Crystal Fields"
- Sleeping spiky replaced with igel due to the spiky being woken up by spawning in anyway, and it just falls off and kills itself... Also removed a fireball which killed you within a second of spawning in the level "The Dark Castle" (Forest variant) which is just unfair.
- Added light fade in scripts to "The Dark Castle" (Antarctic variant) because the old scripts were sudden, and were very sore. Also fixed a visual inconsistency.
- Added a target time for "Circles" and also moved the Power-Up due to it blocking the way forcing the player to swap power-ups.
- "Don't Miss your ride" Adjusted the end to make it less annoying to get to the secret using the spring.
- "Going Down" Stopped enemies from killing themselves inside their chambers, also fixed the coins during the descent as some were extremely difficult to get all in one go (you need to collect all coins in one go to get the perfect coin objective).
- "Entering the castle" fixed a basic visual bug with the spikes underwater.
- Fixed the scripts in "Flower Bonus".
- "After the Glaciers" Fixed the rotation and position of sleeping spikys,  due to the jump over it being very tough and killing the spiky without taking damage having a small window of timing.
- Fixed the secret requiring a damage boost in "In the Spring".
- Fixed the awkward secret in "Some light in the darkness would be fine, Thanks!" (inconsistency with the green spikes, the top could be stood on but the sides were dangerous).
- Visual inconsistencies in "Snowfall alert" have been fixed with the spikes.
- Removed the spikes at the bottom of "Holes, a day on Ice" due to enemies dying off-screen and making a lot of noise throughout the entire level, making it very annoying and painful to play.
- Fixed impossible secret and soft-locking platforms in the second sector of "The Toilette zone". Also removed the secret that also acted as a shortcut due to it hindering perfect completion.. not making it impossible but just a lot more annoying.
- "My Penny is over the ocean" snowball enemy replaced with pink snow.
- Removed the zeekling, wisp, some coins, and reworking the platform node to be less obnoxious in "Red Alert! The forest is burning!" Also removed a couple springs in the secret to allow all coins to be easily collected instead of doing awkward duck jumps.
- Made the roof in "Sewer escape" just a bit higher since coyote time was removed, so the jumps from those ledges are very hard and very punishing.
- Made some changes to how you get on the secret elevator in "Three Frosty Icebergs" due to tux being crushed in rare occasions. Also edited a visual bug at the goal.
- Removed an impossible sleeping spiky in "Under the Ice". Also adjusted the ceiling height in the underground section to allow for a jump to be possible as Big Tux.

---
## [Lagi7/war1gus](https://github.com/Lagi7/war1gus)@[72ec33d530...](https://github.com/Lagi7/war1gus/commit/72ec33d530cce8e3a7644c12e58c59c77e97ce6b)
#### Saturday 2022-01-22 18:50:28 by Lagi7

change default preferences

fog of war default ON - playing without FoW is cheating, and feels .... oooold

Fullscreen ON - if you start with windows, on big monitor player see tiny, tiny screen... and need to do Chinese eyes to change options (OR think "you know what... F.. that, im gonna play smth else") - the default res is 400x300.

show order OFF - flashy lines and dots, MAYBE grants an edge in game, dont want to argue. But they are ugly & artificial. And create an impression that war1gus is in forever Debug mode.

maximum select 50 - i read dozens of articles why starcraft is awesome/balanced/desing intendions ... with 12 limited selection group. Lets get real, war1gus is not gonna be another esport in Kazakhstan. Let newbie that dl for nostalgia has his wow moment "hey I  can select all my troops !! thats great!."

speed max 75 -  if I want to see units stutter, to have perfect mico i will lower the speed myself. Its again to make a great First Impression "Oh how smooth is this game now!". Besides noone ever slow down RTS games - git gud or get rekt.

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[756c5cb3ec...](https://github.com/DrDiasyl/tgstation/commit/756c5cb3ece45bd1726742e02a82e1e3c24a1fc1)
#### Saturday 2022-01-22 19:02:18 by DrDiasyl

(Probably finally) fixes the bullshit error

Deleted ""unique trenchcoat and fedora"" from detective's closet in Deltastation. I will not fucking make curator jacket togglable for this variable changed shit on Deltastation which is not even meet anywhere else!

---
## [ShadiestGoat/DiscordChatExporter](https://github.com/ShadiestGoat/DiscordChatExporter)@[8abbd79900...](https://github.com/ShadiestGoat/DiscordChatExporter/commit/8abbd79900f77c7de184e9d42772ea296158d7c0)
#### Saturday 2022-01-22 19:09:53 by ShadiestGoat

Changelog:

Now the initial welcome thing is present for all chan types
No longer panics when mimetype isn't an image in html export
Start work on changing system msgs
Media name now uses better mimetype things
Content type has a default now (fuck you discord)
Embeded images use thumbnail's url now
Moved embed to attachment thing to earlier in the unmarshal
HTML output improved overall

---
## [RedFlamer/Reworked-Enemy-AI](https://github.com/RedFlamer/Reworked-Enemy-AI)@[ef15a76035...](https://github.com/RedFlamer/Reworked-Enemy-AI/commit/ef15a760352194e467e3b70b566ac7be8691bc37)
#### Saturday 2022-01-22 19:24:36 by RedFlame

Fuck knows honestly

Don't remember most of the changes i've made

---
## [Catarina-Lima/Watch-Your-Back](https://github.com/Catarina-Lima/Watch-Your-Back)@[96adb001e2...](https://github.com/Catarina-Lima/Watch-Your-Back/commit/96adb001e22895fae119c8c32e43cc5e39e8a000)
#### Saturday 2022-01-22 19:48:18 by natercia

i am in misery

there aint nobody who can comfort me oh yeah why wont you answer me the silence is slowly killing me oh yeah girl you really got me bad you really got me bad

feitos a alavanca que desativa fogo e apanhar a chave / abrir porta

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6d6eae2382...](https://github.com/mrakgr/The-Spiral-Language/commit/6d6eae23824f49b745d28d6272bc7c3c67ecf2f2)
#### Saturday 2022-01-22 20:01:49 by Marko Grdinić

"11:50am. Let me finally start. I like slacking way too much.

https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials

Let me start going through this. I want to immerse myself for half an hour.

12:05pm. Oh, the play bar can in fact be minimized. I tried it before and failed. I guess it is worth going through the course.

12:40pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1319984/posts/4428149

This stuff on selection is something I had to look up myself. Let me deal with this course and then I will do something more interesting. I should just give it a shot myself.

12:50pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1319984/posts/4428234

Let me stop here for the morning session. I was not particularly focused and took two breaks, but I'll go through this course today. It is not at all hard. After that I'll definitely do some modeling myself. There is only so much watching I can bear before I get the urge to dive into it.

2:05pm. Done with breakfast and chores. Let me resume the course. Let me just get it out of the way and then I'll get some modeling done. I want to solidify my knowledge.

2:20pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1319984/posts/4428265

Ctrl + middle click on a parameter resets it to its default. Interesting.

I have to absorb these basics to have an easier time working in Houdini. It won't be long. Once I master this I can do some modeling on my own.

2:35pm. Wow, it is possible to highlight values in expressions and use the value ladder there. I admit, something like this would not have occured to me. The basics course is tedious, but I definitely would not think of trying this out on my own.

2:45pm. It seems it is possible to use the middle mouse to just drag in a specific axis. All the stuff in these videos is so useful.

If I was just starting out, I'd look down on this, but the ability to contorl your steps precisely is great. It is only this month that I really came to an understanding of how useful snapping really is and it felt like I got a new power.

Aghhh...I am looking at the video for camera handles and it has the ability to control the depth of field with the handles. That would have made more sense to manipulate in the previous tutorial instead of resizing the objects.

https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273889/posts/4479427

Let me watch this. It is tough to maintain one's concentration, but I have to do it if I am going to master 3d art. Trying to enter into the fray without knwoing your tool is foolish. Let me spend doing this today and the fun stuff will start tomorrow.

This is interesting. In Blender I'd do this by setting the 3d cursor on the origin and rotating around it.

...I need to follow this particular tutorial.

4pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273889/posts/4485494

This covers snapping to faces, though Huodini calls it different than Blender. In Houdini this is alignment. With Blender I had issues of objects sinking into the face and haven't figured out how to deal with that.

4:10pm. Let me play with this for a bit. I am not following what he is saying.

4:35pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273889/posts/4428284

That lesson was a handful. It is not easy to fit 5h of lessons into a single day, but I'll do my best. I can still keep going.

4:50pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273889/posts/4591036

It seems that Houdini has the equivalent of stored views in Blender.

It really has everything. It is such an overwhelming program.

4:55pm. How do I enter construction plane manipulation mode? The slash is not working for me.

Ah, it is the key right next to the shift and the period keys. I never used this key for the slash.

5:20pm. Time for lunch. I am taking a break anyway.

https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273889/posts/4428290

I'll resume this soon. I am honestly dying of tedium despite learning a lot. I just have to get through this.

5:40pm. Done with lunch. Let me resume.

5:45pm. Focus me, close the Baki thread. It is time for quickplanes.

5:50pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273889/posts/4428292

This is boring, but the kind of knowledge this is giving me is exactly what I wanted from this course. These core basics are what I need if I want to be effective at using Houdini. I am really itching to do something real at this stage though.

5:55pm. Instead of dwelling on it, let me go through the snapping parts. I need to get this over with. If needed I'll leave the last two modules for tomorrow, but I should finish snapping today.

6:25pm. https://www.hipflask.how/products/houdini-made-easy-01-the-core-essentials/categories/1273889/posts/4700071

I am dying of boredom here. I've decided, how about I finish the snapping section and just skip the rest for the time being. Knowing how to use the viewport is absolutely essential, but I already know enough about the rest in order to be able to model properly.

Two more vids left. And think I'll call it a day after that. Maybe I'll do some slight modeling if I feel like it. I think I should at least take a look at the structure of the petal that I did.

7pm. I am trying to model here an failing. No matter how good Houdini is, it is useless to me if it does not have good modeling support.

I can't fucking go into select mode, and then select a point, then go to the move tool, then move the handle with the mouse every time. This is ridiculous.

https://www.youtube.com/watch?v=dUaMSl4htV8
Houdini | Edit Points

Let me check this out. I might want to ask how editing is done online.

7:20pm. Sigh, the modeler plugin for Houdini is 100$. There are a bunch of videos on it online.

https://www.youtube.com/watch?v=HwhDBOrK03I
Modeler 2021 Tutorial - Modeling A Mailbox From Scratch

Let me watch this for a bit.

Right now I am considering dropping Houdini or maybe using it together with Blender. I'll look into mixing Blender and Houdini tomorrow, let me watch this just for a bit.

7:40pm. https://youtu.be/HwhDBOrK03I?t=422

So far, this plugin seems just like Blender. Sensible shortcuts to do simple things. This is something Houdini should be good at out of the box.

What I want is either Blender with geo nodes whose instances can be parameterized or Houdini with good modeling capabilities. But if I had to pick one or the other between good modeling and good procedural capabilities, I'd pick the first. Imagine if Photoshop only had a bunch of filters, but poor capability to draw or paint. That is what Houdini is. It has literally everything, but the most basic stuff.

https://www.youtube.com/watch?v=PukQ4TQbg5s
Houdini to Blender Workflow

> NOTE: You must have a Houdini Indie License or greater to export alembic files. In other words, the free apprentice version will not work. However, my Indie license only cost $269 , which is way cheaper than I thought it would be.

What about the other way around?

7:55pm. https://youtu.be/v5KNW9_Vkl0
Simple Workflow with Blender and Houdini

Let me watch this just for a bit.

https://youtu.be/v5KNW9_Vkl0?t=91

Actually, this is not a bad idea at all. If I have the very basic features like leaves and flower petals, Houdini would not be bad at connecting them. Where I ran into trouble is doing primitive destructive operations.

https://youtu.be/v5KNW9_Vkl0?t=241

Hmmmm, this could actually be really good.

8:20pm. https://youtu.be/NtT8HZ60NBU
Non-Destructive Modeling Workflow

That previous video has won me over. I am going to backtrack a bit and export the petal and the leaf. Then I am going to import them and try making the flower out of them in Houdini.

What I want is not that complicated, I just need to compose functions together to get the scene that I want. In Blender this is currently impossible because it does not have parameterized instances.

What is not that complicated, imagine having 5 different houses and distributing them randomly on a grid. Just a few variations would allow me to get an infinite number of different layouts. It is perfectly fine if I model the things in Blender and import them into Houdini. I am going to try that tomorrow.

Now let me watch the above just for a bit.

8:45pm. Let me close for the day here. There is no way around it, I just have to go for it.

I can't spend forever learning Houdini. And in fact, I do not need to. What I learned in the last few days was enough to grasp its essential features, and today I learned how to layout objects. I can't let a small snag that the two programs have hinder my path.

Tomorrow I am going to do that flower properly. After after that I'll move on the rest of the scene. I'll import the fence logos and the rest as well.

8:50pm. I probably don't need to do this, but I want to. If the result is not that good I'll go back to doing it in pure Blender, but for now, I'll do as I wish here. I need to establish my workflow as an illustrator. I need to cover up for my weaknesses and push procedural generation as much as possible.

8:55pm. I won't give up. I won't lose much by trying out Houdini either way.

9pm. Let me gather my will during the night, and tomorrow I will let it explode. I had enough of these tedious tutorials. I need to just go forward. Ultimately, 3d is substitute for sketching. I should not lose sight of that."

---
## [saem/nimskull](https://github.com/saem/nimskull)@[f35b5bf2d4...](https://github.com/saem/nimskull/commit/f35b5bf2d447c10b6a104ef0649115a266e8dea6)
#### Saturday 2022-01-22 20:13:40 by haxscramper

Make compiler report structured

Full rework of the compiler message handling pipeline. Remove old-style message generation that was
based purely on strings that were formatted in-place, and instead implement structured logging where
main compiler code only instantiates objects with required information.

Explanation of changes for this commit will be split into several sections, matching number of edit
iterations I had to make in order for this to work properly.

* File reorganization

In addition to the architectural changes this PR requires some type definition movements.

- PNode, PSym and PType definitions (and all associated types and enums) were moved to the
  ast_types.nim file which is then reexported in the ast.nim
- Enum defininitions for the nilability checking were moved to nilcheck_enums.nim and then
  reexported
- Enum definitions for the VM were moved to to vm_enums.nim

* New files

- Main definition of the report types is provided in the reports.nim file, together with minor
  helper procedures and definition of the ReportList type. This file is imported by options, msgs
  and other parts of the compiler.
- Implementation of the default error reporting is provided in the cli_reporter.nim - all
  disguisting hardcoded string hacks were moved to this single file. Now you can really witness the
  "error messages are good enough for me" thinking that prevailed in the compiler UX since it's
  inception.

* Changed files

Most of the changes follow very simple pattern - old-style hardcoded hacks are replaced with
structural report that is constructed in-place and then converted to string /when necessary/. I'm
pretty sure this change already puts me close to getting CS PHD - it was *unimaginably hard* to
figure out that hardcoding text formatting in place is not the best architecture. Damn, I can
probably apply to the nobel prize right now after I figure that out.

** Changes in message reporting pipeline

Old error messages where reportined via random combinations of the following:

- Direct calls to `msgs.liMessage` proc - it was mostly used in the helper templates like
  `lintReport`
- `message`
- `rawMessage`
- `fatal`
- `globalError` - template for reporting global errors. Misused to the point where name completely
  lost it's meaning and documentation does not make any sense whatsoever. [fn:global-err]
- `localError` - template for reporting necessary error location, wrapper around `liMessage`
- `warningDeprecated` - used two times in the whole compiler in order to print out error message
  about deprecated command switches.

Full pipeline of the error processing was:

- Message was generated in-place, without any colored formatting (was added in `liMessage`)
  - There were several ways message could be generated - all of them were used interchangeably,
    without any clear system.
    1. Some file had a collection of constant strings, such as `errCannotInferStaticParam = "cannot
       infer the value of the static param '$1'"` that were used in the `localReport` message
       formatting immediately. Some constants were used pretty often, some were used only once.
    2. Warning and hint messages were categorized to some extent, so and the enum was used to
       provide message formatting via `array[TMsgKind, string]` where `string` was a `std/strutils`
       formatting string.
    3. In a lot of cases error message was generated using hardcoded (and repeatedly copy-pasted)
       string
- It was passed down to the `liMessage` (removed now) procedure, that dispatched based on the global
  configuration state (whether `ignoreMsgBecauseOfIdeTools` holds for example)
- Then message, together with necessary bits of formatting (such as `Hint` prefix with coloring) was
  passed down to the `styledMsgWriteln(args: varargs[typed])` template, whcih did the final dispatch
  into
- One of the two different /macros/ for writing text out - `callStyledWriteLineStderr` and
  `callIgnoringStyle`.
  - Dispatch could happen into stdout/stderr or message writer hook if it was non-nil
- When message was written out it went into `writeLnHook` callback (misused for
  `{.explain.}` [fn:writeln-explain]) (hacked for `compiles()` [fn:writeln-compiles]) and was
  written out to the stdout/stderr.

It is now replaced with:

- `Report` object is instantiated at some point of a compilation process (it might be an immediate
  report via `localError` or delayed via `nkError` and written out later)
- `structuredReportHook` converts it to string internally. All decitions for formatting, coloring
  etc. happen inside of the structured report hook. Where to write message, which format and so on.
- `writeLnHook` /can/ be used by the `structuredReportHook` if needed - right now it is turned into
  simple convenience callback. In future this could even be replaced with simple helper proc, for
  now I left it as it is now because I'm not 100% sure that I can safely remove this.

** Changes in the warning and hint filtering

Report filtering is done in the particular *implementation* of the error hook -
`options.isEnabled()` provides a default predicate to check whether specific report can be written
out, but it must still be called manually. This allows to still see all the reports if needed. For
example, `cli_reporter.reportHook()` uses additional checks to force write some reports (such as
debug trace in `compiles()` context).

Most of the hint and warning were already categorized, altough some reports had to be split into
several (such as `--hint=Performance` that actually controlled reports for `CopiesToSink` and
`CannotMakeSink`, `--hint=Name` that controlled three reports).

None of the errors were categorized (reports from the `nkError` progress was incorporated, but in
I'm mostly describing changes wrt. to old reporting system) and all were generated in-place

** Minor related changes

- List of allowed reports is now stored in the `noteSets: array[ConfNoteSet, ReportKinds]` field of
  the `ConfigRef`, instead of *seven* separate feilds. Access is now done via getter/setter procs,
  which allows to track changes in the current configuration state.
- Renamed list of local options to `localOptions` - added accessors to track changes in the state.
- Move all default report filter configuration to `lineinfos.computeNotesVerbosity()` - previously
  it was scattered in two different places: `NotesVerbosity` for `--verbosity:N` was calculated in
  `lineinfos`, foreignPackageNotesDefault was constructed in `options`
- Changed formatting of the `internalAssert` and `internalError` messages
- Removed lots of string formatting procs from the various `sem*` modules - ideally they should
  *all* be moved to the `cli_reporter` and related.

-------

Additional notes

[fn:global-err] As I said earlier, `globalError` was misused - it is still not possible to fully get
rid of this sickening hack, since it is used for /control flow/ (you read this correct - it is an
error reporting template, and it is used for control flow. Wonderful design right?).

So, in short - `globalError` can raise `ERecoverableError` that can be caught in some other layer
(for example `sem.tryConstExpr` abuses that in order to bail out (pretty sure it was done as an
'optimization' of some sort, just like 'compiles') when expression fails to evaluate at
compile-time [fn:except])

[fn:except] https://github.com/nim-works/nimskull/pull/94#issuecomment-1006927599

[fn:writeln-explain] Of course you can't have a proper error reporting in the nim compiler, so this
hook was also misused to the point of complete nonsense. Most notable clusterfuck where you could
spot this little shit is implementation of `{.explain.}` pragma for concepts. It was implemented via
really 'smart' (aka welcome to hell) solution in

https://github.com/nim-works/nimskull/commit/74a80988d9289e8147a791c4b0939d4287baaff3 (sigmatch
~704) and then further "improved" in
https://github.com/nim-lang/Nim/commit/fe48dd1cbec500298f7edeb75f1d6fef8490346c by slicing out parts
of the error message with `let msg = s.replace("Error:", errorPrefix)`

For now I had to reuse similar hack - I *do* override error reporting hook in order to collect all
the missing report information. In the future it would be unnecessary - when concept is matched it's
body will be evaluated to `nkError` with reports that are written out later.

[fn:writeln-compiles] when `compiles()` check is executed, all error output is temporarily disabled
(both stderr and stdout) via setting allowed output flags to `{}` (by default it is set to

---
## [newstools/2022-information-nigeria](https://github.com/newstools/2022-information-nigeria)@[1ca0e5d6df...](https://github.com/newstools/2022-information-nigeria/commit/1ca0e5d6df648de1f5ce5473eb770d8cd61b3009)
#### Saturday 2022-01-22 20:52:41 by Billy Einkamerer

Created Text For URL [www.informationng.com/2022/01/lover-boy-donates-kidney-to-his-girlfriends-mother-only-for-her-to-marry-someone-else-a-month-later.html]

---
## [Vishalcj17/android_kernel_qcom_sm8350](https://github.com/Vishalcj17/android_kernel_qcom_sm8350)@[cc0e809a5d...](https://github.com/Vishalcj17/android_kernel_qcom_sm8350/commit/cc0e809a5dacb366f3962498ce5b1d8161783122)
#### Saturday 2022-01-22 22:35:31 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---

