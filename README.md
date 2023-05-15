## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-14](docs/good-messages/2023/2023-05-14.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,901,296 were push events containing 2,828,391 commit messages that amount to 137,904,365 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [hexagon-geo-surv/linux-stable](https://github.com/hexagon-geo-surv/linux-stable)@[1bba82fe1a...](https://github.com/hexagon-geo-surv/linux-stable/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Sunday 2023-05-14 00:18:13 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[56d960a763...](https://github.com/necromanceranne/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Sunday 2023-05-14 00:23:24 by GoldenAlpharex

Wintercoats can now be zipped and unzipped through alt-click and separates the hood sprites from the jacket sprites (#74886)

## About The Pull Request
The title says it all, really.

~~Initially, I was only going to do it for all wintercoats, but then I
figured I might as well bring it down to all of `/hooded`, just so other
suits could benefit from it, since that behavior came from there anyway.
Does that mean that it does nothing for some of them? Yes, it does. Does
that justify having another variable to tell whether or not that should
be possible? In my humble opinion, not really, but I'm not against it if
it's requested.~~

~~That functionality was intentionally removed from the Void Cloak, as
there would be balance implications (since bringing up the hood makes
the whole cloak invisible, which you could skirt by just "zipping" it,
which also makes it invisible.~~

~~The sprites were already there, so this change was very simple to do.
Simply unties the zipped up look from the fact that the hood is up.
However, toggling the hood forces the zipping/unzipping, just so there's
no balance implications involved. It's just simpler that way.~~

So, I ended up going back and changing the sprites so that the hoods
would no longer be baked into the jacket's sprites, so that they could
be done as overlays instead, which ended up solving my problem with
hoods not being there on zipped-up versions.

For now, it's been made on winter coats only, but it shouldn't be that
difficult to bring it back down to the `/hooded` level. I just didn't
want to bother touching up the sprites down there, as it already took me
like 2-3 hours touching up the sprites of the winter coats alone.

I also took the decision to make it so EVA winter coats used the regular
winter coat's sprites, because they had special ones that just looked
like worse versions of the original, without anything special going on
for them. It was just a straight downgrade compared to the base sprite,
in my opinion.

There's still issues with the custom winter coat, in that the hood isn't
made into an overlay for it yet (and that'll require an extra bit of
logic to make it work, too), but it was already an issue before, the
hood is always present on the current version of the custom winter coat.

There's still a handful (sadly, most) of the winter coats that don't
properly reflect on their obj sprites when they're opened versus when
they're closed, but that's due to an initial spriter oversight, and not
to my doing. The open versions were just left as closed on many of them,
and I simply don't have the patience nor the appropriate skills to edit
that many coats that way.

## Why It's Good For The Game
Now you can be stylish with or without the hoodie!

![image](https://user-images.githubusercontent.com/58045821/233544697-cc821c3a-d965-4d96-af44-c44ff866496f.png)

![image](https://user-images.githubusercontent.com/58045821/233544711-da956b6b-44c4-4903-a34f-4d2890abc781.png)

![image](https://user-images.githubusercontent.com/58045821/233544717-b5221b04-0e6d-4931-83d0-d56fdac60ec3.png)


According to ChatGPT, with one small tweak (thanks Opera GX for the
suggestion):

> Zipped and unzipped through alt-click, winter coats can now be. Hmm,
stylishly warm, you shall be. Feel like a Spaceman, you will. Use the
Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.

## Changelog

:cl: GoldenAlpharex, ChatGPT for the first changelog entry (slightly
edited)
qol: Zipped and unzipped through alt-click, winter coats can now be.
Hmm, stylishly warm, you shall be. Feel like a Spaceman, you will. Use
the Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.
image: Winter coats no longer have their hood baked into their jacket's
sprite, both in item form and when worn.
fix: Updated the Icebox EVA winter coats (the Endotherm winter coats) to
use the same sprites as the regular winter coats.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[3fdd716da5...](https://github.com/necromanceranne/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Sunday 2023-05-14 00:23:24 by Cheshify

Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[43473a4dac...](https://github.com/necromanceranne/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Sunday 2023-05-14 00:23:24 by san7890

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [baiyuqing/redis](https://github.com/baiyuqing/redis)@[0e5b813ef9...](https://github.com/baiyuqing/redis/commit/0e5b813ef94b373f82bc75efcf3405f2c81af3dc)
#### Sunday 2023-05-14 01:53:22 by yoav-steinberg

Multiparam config set (#9748)

We can now do: `config set maxmemory 10m repl-backlog-size 5m`

## Basic algorithm to support "transaction like" config sets:

1. Backup all relevant current values (via get).
2. Run "verify" and "set" on everything, if we fail run "restore".
3. Run "apply" on everything (optional optimization: skip functions already run). If we fail run "restore".
4. Return success.

### restore
1. Run set on everything in backup. If we fail log it and continue (this puts us in an undefined
   state but we decided it's better than the alternative of panicking). This indicates either a bug
   or some unsupported external state.
2. Run apply on everything in backup (optimization: skip functions already run). If we fail log
   it (see comment above).
3. Return error.

## Implementation/design changes:
* Apply function are idempotent (have no effect if they are run more than once for the same config).
* No indication in set functions if we're reading the config or running from the `CONFIG SET` command
   (removed `update` argument).
* Set function should set some config variable and assume an (optional) apply function will use that
   later to apply. If we know this setting can be safely applied immediately and can always be reverted
   and doesn't depend on any other configuration we can apply immediately from within the set function
   (and not store the setting anywhere). This is the case of this `dir` config, for example, which has no
   apply function. No apply function is need also in the case that setting the variable in the `server` struct
   is all that needs to be done to make the configuration take effect. Note that the original concept of `update_fn`,
   which received the old and new values was removed and replaced by the optional apply function.
* Apply functions use settings written to the `server` struct and don't receive any inputs.
* I take care that for the generic (non-special) configs if there's no change I avoid calling the setter (possible
   optimization: avoid calling the apply function as well).
* Passing the same config parameter more than once to `config set` will fail. You can't do `config set my-setting
   value1 my-setting value2`.

Note that getting `save` in the context of the conf file parsing to work here as before was a pain.
The conf file supports an aggregate `save` definition, where each `save` line is added to the server's
save params. This is unlike any other line in the config file where each line overwrites any previous
configuration. Since we now support passing multiple save params in a single line (see top comments
about `save` in https://github.com/redis/redis/pull/9644) we should deprecate the aggregate nature of
this config line and perhaps reduce this ugly code in the future.

---
## [enso-org/enso](https://github.com/enso-org/enso)@[4b7afbfd36...](https://github.com/enso-org/enso/commit/4b7afbfd3619c22b6b31f2840fa807f0af41fb57)
#### Sunday 2023-05-14 04:35:25 by Ilya Bogdanov

Fix blank input port (#6614)

Fixes #6485

Conflicting requirements for the widget tree caused the issue:
1. The span tree node had a connection, and the text of the `number1` label was changed to white (as per the `Connected` color state)
2. The node configuration did not consider it a valid port because the span tree kind was `Operation`, which is not a port usually. So the port shape was not displayed, making the label blend with the node background.

I fixed the issue by considering the existence of the current connection for `Operation` nodes. Remember that it does not turn the node into a port, so after removing the connection, it's not possible to connect it back. That makes sense, in my opinion, as the resulting AST is invalid anyway. But at least we can see the label on the invalid node.


https://github.com/enso-org/enso/assets/6566674/23934966-8f72-4675-abe3-78a3f0c0cda4

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[7c24731530...](https://github.com/Koi-3088/ForkBot.NET/commit/7c24731530302399de0bc0930c4366da15f3a1c6)
#### Sunday 2023-05-14 05:21:16 by Koi

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
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[21363d07a5...](https://github.com/OrionTheFox/Skyrat-tg/commit/21363d07a5eec9fbce5be2f17cd1693319906d61)
#### Sunday 2023-05-14 07:13:15 by SkyratBot

[MIRROR] De-holes holy arrows [MDB IGNORE] (#20985)

* De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

* De-holes holy arrows

---------

Co-authored-by: Thunder12345 <Thunder12345@users.noreply.github.com>

---
## [agam778/kernel_xiaomi_sm8250](https://github.com/agam778/kernel_xiaomi_sm8250)@[eb7e4e0a9f...](https://github.com/agam778/kernel_xiaomi_sm8250/commit/eb7e4e0a9fd040371ee35e101ae94073a0a1fa5b)
#### Sunday 2023-05-14 08:04:41 by Agampreet Singh

 touchscreen: focaltech_touch: Rename gesture macros

- Fuck you xiaomi.
- Also don't register KEY_GESTURE_U anymore.

---
## [jdlcdl/seedsigner](https://github.com/jdlcdl/seedsigner)@[d2a657f2d4...](https://github.com/jdlcdl/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Sunday 2023-05-14 08:23:38 by Marc G

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
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[fc1471c818...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Sunday 2023-05-14 08:37:25 by SkyratBot

[MIRROR] Deadchat Announcement Variety Pack 1 [MDB IGNORE] (#20957)

* Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat.
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

* Deadchat Announcement Variety Pack 1

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [Jalesen/tgstation](https://github.com/Jalesen/tgstation)@[2b2cb3dff6...](https://github.com/Jalesen/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Sunday 2023-05-14 08:55:11 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[13164ca7fe...](https://github.com/LumberKing/Tianxia/commit/13164ca7feaa09195de5afde9f0b8f305ac8f82c)
#### Sunday 2023-05-14 09:12:25 by Silversweeper

CleanSlate merge-related commit of assorted stuff

Commit made just to make the CleanSlate merge easier. Lots and lots of WIP stuff.

General:
- Optimization tweaks.

Artefact spawns:
- Fixed some issues with artefacts not spawning for the right character.

CBs:
- Fixed Child of Destiny CI empire creation issue.

Cultures:
- Removed unused Buryat culture.

Scripted effects and triggers:
- MoH improvements.
- Tributaries of pretender emperors no longer get to interact with the Treasure Fleet.

Societies:
- Jain MO T4 power now also boosts kejawen_opinion.
- Updated WotRS and Hwarang startup_populate blocks.

Traits:
- Muslim members of the Hermetics can now get the Scholar trait; fixes vanilla issue where they can discard other lifestyles and get nothing in return.
- Wako characters can now gain Pirate trait upgrades, as can some specific Pirate trait holders.
- Yupaychaspa characters now approve of Left-handed.

Decisions:
- Minor fixes to the decisions to become CI.
- Invited commanders are now Japanese Feudal if inviter is Japanese Feudal.
- Added a decision for Yamato/Japanese Pirates/etc. living on the coast to culture swap to Wako.
- Split off mr-related culture conversion into a separate file.

Events:
- The Imperial Family no longer generates new members on game start even if the game is set to do that. They're very special.
- Wars no longer interrupt the Treasure Fleet preparation.
- Reworked Treasure Fleet preparation events.
- Chinese influence group laws now impact Treasure Fleet preparation.
- Non-DW vassals of China can now also attempt major sabotage against the Treasure Fleet.
- Children might now potentially sneak off to join the Treasure Fleet, within reason.
- The Treasure Fleet is now twice as likely to sink in the harbour if the EoC happens to be Swedish (a small increase overall).
- The Treasure Fleet's initial destination is now always one of Korea, the Ma-i-an Archipelago (a.k.a. the Philippines), and Champa.
- Added sanity checks for agnatic/enatic trait inheritance (Sayyid (+ Mirza), Saoshyant Descendant, Amaterasu Descendant) when set_father/set_mother is triggered; traits match perceived father/mother, as in the case of a hidden bastard.
- Added santiy check on Jimmu's bloodline inheritance, inheritance of other Imperial Family bloodlines, inheritance of Divine Ancestry bloodlines, and inheritance of Confucius' bloodline when set_father/set_mother is triggered (matching perceived parents). Fixes vanilla stupidity where bloodines that should not be universal are treated as such, as well as denounced children getting to keep these bloodlines.
- Fixed missing propagation/cleanup of Amaterasu Descendant on bastard denouncement.
- Fixed vanilla bug where the father could remove enatic trait inheritance by denouncing a child.
- Fixed vanilla bug where denounced Sayyid children of a Sayyid mother lost Sayyid without getting Mirza.
- Characters preparing a Treasure Fleet or preparing to join a Treasure Fleet no longer are expected to mourn (it risks breaking stuff).
- Added many new events that can happen during the Treasure Fleet's voyage, including trait-specific events and ways for childhood traits to evolve.
- Bloodline commanders/heroes/knights are now Japanese Feudal if bloodline member is Japanese Feudal.
- Bloodline mystics can now end up with a few more religions if it is randomized.
- More sanity checking of vanilla tumbling and celibacy/mourning celibacy/chastity.
- Hedge knights now respect orientation.
- Fixed incorrect bio father in "virgin birth" event; it's not tied to the supernatural game rule, so it isn't supernatually the father's child. Vanilla issue.
- Feast lovers and tumble attempts now respect orientation.
- Even if it is a romantic gesture your spouse will not become your lover if you name a star after them unless you have compatible orientation. Vanilla stupidity fix.
- While your spouse might be pleased if you save them from drowning, their and your orientation still matters as far as becoming a lover goes. Vanilla stupidity fix.
- Varangian lovers impregnating your daughters now need both the right "equipment" and the right orientation. Vanilla stupidity fix.
- Gifting a horse to an incompatible spouse no longer makes them your lover. Vanilla stupidity.
- Lovers created for witch hunts are now compatible. Vanilla stupidity.
- Fixed lovers brought in by your (adult) children when in seclusion potentially having the wrong orientation. Vanilla stupidity.
- Sleeping with someone at a brothel during a crusade now actually involves doing that. Vanilla stupidity.
- While diamonds are forever your spouse will not love you for gifting them a cursed diamond if either of you have an incompatible orientation. Vanilla stupidity fix.
- The Family Focus can no longer cause love to bloom between incompatible spouses. Vanilla stupidity.
- Sleeping with someone in a cabin in the woods now comes with a pregnancy risk even if you don't bring them to court. Vanilla bug.
- Swimming is no longer Int-based.
- Deserted islands can now contain a few more kinds of swords.
- Reverted some celibacy fixes that were a bit too generously applied.
- Added logic for Boon refusal.
- Taoist vassals no longer get upset over Immortal lieges.
- Characters ineligible for the Religious Liberation CB -- e.g. CI characters -- will no longer get religious liberation opportunities.
- Martial now matters when the Treasure Fleet is fighting.
- The Treasure Fleet might now experience a mutiny.
- The Kraken is now rather more formidable.
- The EoC should now be informed of the Treasure Fleet's arrival somewhere regardless of whether he's got any provinces nearby.
- The Treasure Fleet should no longer affect Grace if it's about to be aborted, seeing as it could be associated with a non-existent imperial dynasty.
- Updated artefact logic for crown jewels to account for new religions.
- Updated and expanded on Treasure Fleet port events.
- Pilgrimages to western Catholic sites are now unlocked by starting after they become pilgrimage sites, as opposed to assuming that the relevant destinations are important after a certain year in another timeline. Vanilla fix.
- Fixed poorly scripted tumbling logic for TF feast guests.
- Fixed AI logic for some Tributes/Boons.
- Expanded on what can happen when visiting a port on the Treasure Fleet's voyage.
- Strategists now potentially get opportunities to make contingency plans for taking control of the Treasure Fleet's military forces and/or invading the local area, which might be helpful should they decide to actually attempt to carry out such plans.
- The attempt to launch a Treasure Fleet invasion can now fail, with severe penalties attached. Low Martial and/or Intrigue characters beware.

Graphics:
- Restored old (pre-JD) China CoA; it's a bit fancier.

History:
- Made some more Han and Korean characters Confucian, and added branch traits for a few.
- Added branch traits for some Taoists.
- Kibi Makibi now becomes Confucian towards the end of his life.
- Jiang Gongfu now becomes a Taoist monk in 792.
- Zhang Chujin has dealt with his doppleganger.
- Abe clan improvements and related title history tweaks.

Localization:
- Fixed "tenants" in Samaritan SRS. Vanilla error.
- The mysterious "Southern Coast of Busaro" is now properly known as the "Southern Coast of Busaso". That's only been in the mod since late 2018...

---
## [ouztsa/evals](https://github.com/ouztsa/evals)@[99623db9c3...](https://github.com/ouztsa/evals/commit/99623db9c33c5d000664d2e7b2fe3571335b7ff2)
#### Sunday 2023-05-14 09:51:07 by Andrew Kondrich

add more logging (#964)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
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
  INSERT_EVAL_HERE
  ```
</details>

---
## [PINKUNOBARA/rev2palettetool](https://github.com/PINKUNOBARA/rev2palettetool)@[6c1aef6f87...](https://github.com/PINKUNOBARA/rev2palettetool/commit/6c1aef6f878f36f239f61e3beac7208fd895c072)
#### Sunday 2023-05-14 10:15:56 by PINKUNOBARA

XRDTOOL MK.2210

Changed the UI and hotkeys, also made the window smaller.

Sorry for not making this earlier, I have been sick everyday for a few months now and I am currently experiencing a terrible headache, I am pretty much disabled at this point so the will to work on this stuff is not a lot.

Well enjoy it until the next update comes and breaks it again.

---
## [KoJIT2009/Skyrat-tg](https://github.com/KoJIT2009/Skyrat-tg)@[c2d75696c8...](https://github.com/KoJIT2009/Skyrat-tg/commit/c2d75696c8d0012027bf97a15b2c0e332416b497)
#### Sunday 2023-05-14 10:46:31 by SkyratBot

[MIRROR] Nerfs the firing speed of Syndicate/Russian mobs [MDB IGNORE] (#21047)

* Nerfs the firing speed of Syndicate/Russian mobs (#75247)

## About The Pull Request

Nerfs their firing speed from once every 0.2 seconds to once every 2.5
seconds

## Why It's Good For The Game

1. The mob that is NOT a 'burst' type mob, is firing every 0.2 seconds.
Kinda defeats the point of having them as two separate mobs, so this
aims to fix that.
2. Russian mobs. Turns out that letting them fire their strong-ass gun
every 0.2 seconds was kinda not a good idea. I had assumed making them a
Syndicate mob would be safe, and it technically is, it's just that
Syndicate mob is fucked itself.

## Changelog

:cl:
balance: Default Syndicate and Russian gunners now fire every 2.5
seconds instead of every 0.2
/:cl:

* Nerfs the firing speed of Syndicate/Russian mobs

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [fjrXTR/android_kernel_xiaomi_rosemary](https://github.com/fjrXTR/android_kernel_xiaomi_rosemary)@[1b2ecd8dbe...](https://github.com/fjrXTR/android_kernel_xiaomi_rosemary/commit/1b2ecd8dbe0e3a8e99cc3f5aaaaee4ab88c39a50)
#### Sunday 2023-05-14 11:30:57 by Peter Zijlstra

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
Signed-off-by: Momo Belia Deviluke <fajarslebew31@gmail.com>

---
## [leejy12/terminal](https://github.com/leejy12/terminal)@[6ad8cd0a63...](https://github.com/leejy12/terminal/commit/6ad8cd0a630ab927629841a14d433c3bc19a1509)
#### Sunday 2023-05-14 12:18:53 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388. 

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated). 

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

---
## [razielanarki/terminal](https://github.com/razielanarki/terminal)@[21464fe41c...](https://github.com/razielanarki/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Sunday 2023-05-14 12:23:36 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [MixusMinimax/grpc-example](https://github.com/MixusMinimax/grpc-example)@[614f511637...](https://github.com/MixusMinimax/grpc-example/commit/614f511637b4478630b7e03aec34874b21829a00)
#### Sunday 2023-05-14 13:07:21 by Maxi Barmetler

Fuck shit cock ass piss crap shite shaft tarnation

---
## [rlawoehd187/android_kernel_lge_msm8998](https://github.com/rlawoehd187/android_kernel_lge_msm8998)@[cc30e749fe...](https://github.com/rlawoehd187/android_kernel_lge_msm8998/commit/cc30e749fe55d65f6c2532653f8156f9c465d504)
#### Sunday 2023-05-14 13:35:38 by Christian Brauner

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
Signed-off-by: electimon <electimon@gmail.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[d728da3e02...](https://github.com/realforest2001/forest-cm13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Sunday 2023-05-14 14:06:34 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [ublue-os/startingpoint](https://github.com/ublue-os/startingpoint)@[c7deb7d6fe...](https://github.com/ublue-os/startingpoint/commit/c7deb7d6fe3aa4256d7a79123ffc250a24165263)
#### Sunday 2023-05-14 15:18:19 by Arcitec

fix: friendlier experience in the "yafti" first boot template

- The first screen's "Pick some applications to get started" has been replaced with a friendly welcoming message.

- The second screen's difficult-to-understand "WARNING: This will modify your Flatpaks if you are rebasing!" has been replaced with an explanation of what it actually does.

- The application setup screen is now titled "Application Installer", since the previous title sounded too much like a silly rhyme. It's a minor change.

- All Flatpaks now default to system-wide install thanks to the great work of bsherman at https://github.com/ublue-os/yafti/pull/82. This saves tons of disk space for multi-user systems.

- The "system application" category have been split up into GNOME apps and every other system app, so that people on other desktop environments don't get all the GNOME apps.

- Apps that had too vague descriptions have been renamed to their full names, such as "Backup -> Deja Dup Backups".

- All app lists have been sorted alphabetically.

- Non-inclusive language in descriptions has been changed.

- Added SteamTinkerLaunch as a suggestion for the Steam category, which is the best tool for managing Steam game configurations and Proton installations, albeit very advanced since it can do practically anything the gamer needs. :)

---
## [4hands44/cmss13](https://github.com/4hands44/cmss13)@[a2d5ca6e69...](https://github.com/4hands44/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Sunday 2023-05-14 15:40:16 by QuickLode

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
## [Youtubeboy139/tgstation](https://github.com/Youtubeboy139/tgstation)@[1b5c0489a4...](https://github.com/Youtubeboy139/tgstation/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Sunday 2023-05-14 15:53:01 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [Youtubeboy139/tgstation](https://github.com/Youtubeboy139/tgstation)@[f2fd69a49a...](https://github.com/Youtubeboy139/tgstation/commit/f2fd69a49a7d9308eb695c0368163d2f63a53a54)
#### Sunday 2023-05-14 15:53:01 by ArcaneMusic

Minerals have been refactored so costs and minerals in items are now in terms of mineral defines. (#75052)

Ladies, Gentlemen, Gamers. You're probably wondering why I've called you
all here (through the automatic reviewer request system). So, mineral
balance! Mineral balance is less a balance and more of a nervous white
dude juggling spinning plates on a high-wire on his first day. The fact
it hasn't failed after going on this long is a miracle in and of itself.

This PR does not change mineral balance. What this does is moves over
every individual cost, both in crafting recipes attached to an object
over to a define based system. We have 3 defines:

`sheet_material_amount=2000` . Stock standard mineral sheet. This being
our central mineral unit, this is used for all costs 2000+.
`half_sheet_material_amount=1000` . Same as above, but using iron rods
as our inbetween for costs of 1000-1999.
`small_material_amount=100` . This hits 1-999. This covers... a
startlingly large amount of the codebase. It's feast or famine out here
in terms of mineral costs as a result, items are either sheets upon
sheets, or some fraction of small mats.

Shout out to riot darts for being the worst material cost in the game. I
will not elaborate.

Regardless, this has no functional change, but it sets the groundwork
for making future changes to material costs much, MUCH easier, and moves
over to a single, standardized set of units to help enforce coding
standards on new items, and will bring up lots of uncomfortable balance
questions down the line.

For now though, this serves as some rough boundaries on how items costs
are related, and will make adjusting these values easier going forward.

Except for foam darts.

I did round up foam darts.

Adjusting mineral balance on the macro scale will be as simple as
changing the aforementioned mineral defines, where the alternative is a
rats nest of magic number defines. ~~No seriously, 11.25 iron for a foam
dart are you kidding me what is the POINT WHY NOT JUST MAKE IT 11~~

Items individual numbers have not been adjusted yet, but we can
standardize how the conversation can be held and actually GET SOMEWHERE
on material balance as opposed to throwing our hands up or ignoring it
for another 10 years.

---
## [polyamAdmin/mastodon](https://github.com/polyamAdmin/mastodon)@[baba605c06...](https://github.com/polyamAdmin/mastodon/commit/baba605c0640aecffb3caab9adcda99c83cf9261)
#### Sunday 2023-05-14 16:12:31 by polyamAdmin

Run `yarn run eslint --fix`

I hate prettier and this shit looks awful.

Signed-off-by: polyamAdmin <117664621+polyamAdmin@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2fa801e5c8...](https://github.com/mrakgr/The-Spiral-Language/commit/2fa801e5c84bdb5ab12ee41b1ec6fb8f634f096e)
#### Sunday 2023-05-14 16:42:12 by Marko Grdinić

"8:20am. What I want to do is just start work on Helix. So that is what I am going to do.

I am going to start the typescript miniseries, and leave deploying this project for later.

8:30am. Let me chill for a while first.

Web development is trying to teach me something.

8:45am. Let me get started. I do not feel like reading Manga.

9:05am. For this video I am going to do the voice acting myself.

///

Hi, for this video I am going to take on the voice acting duties myself.
The last two videos killed me mentally.
I know that I announced the deployment video last time, but I just don't feel like doing that.

In my channel I want to show you guys the right path towards functional web development.
But I finally realized something that should be obvious.
Fable, and I am guessing any other functional languages, are not serious competitors to Typescript.

///

9:15am. https://www.youtube.com/watch?v=_p16mwfE9as
If you only learn ONE Shortcut... Make it this one! Davinci Resolve

Alt key.

How do you drag just the audio parts of a clip again?

Using the shift key.

///

https://youtu.be/pmx6wUv7Muk
2 Ways to MUTE Part of any AUDIO in DaVinci Resolve

Time to learn a bit more about Resolve.

https://youtu.be/pmx6wUv7Muk?t=31

Ah, right. Why am I using ranges when I could be cutting it directly?

///

I don't mean to say they are bad languages in isolation.
They have good libraries.
And Typescript has many disadvantages, that Fable doesn't have like its syntax, and the lack of global type inference and pattern matching.

But just what happened last time?
Fable could be the best language in the world for all we care, but what good does that give us when it doesn't even had a queue in its standard library?

If we were programming in Typescript, it would have been absolutely trivial to get it from somewhere.
In Fable, we'd have to create the bindings for it.

Instead of implementing a Mailbox on my own, I wanted to do the smart thing of importing some channel library.
And I tried that at first.

///

Holy shit...

https://www.npmjs.com/package/typescript-queue?activeTab=readme
> separate PromiseQueue implementation that supports async/await, async iteration with for await, and efficient caching for asynchronous peek/poll operations

10:10am. My god, my own talking skills are so horrible.

Comparing myself to somebody like Prime makes me want to kill myself.

Can't I install some module into my brain that does this for me.

I just can't maintain the right mental state for it. Let me write it all down.

10:30am. Oh, OBS + DR editing is actually quite comfortable.

Right now I do not even need to write things down thanks to the puase button being so good.

Maybe I could try working like this for a bit.

11:40am. Made the intro, it is really heavy going for me.

12pm. > training weights, cinematic landscape

The Bing image generator is quite good.

I narrated this video on my own, without necessarily having to constantly go back and repeat myself.

There is some backtracking and mincing of words, but it is just too annoying to have to get it right 100%. 80% should be my target from here on out.

Yeah, talking skills are not my forte, but I can just change my approach.

I'll aim for mid quality in my own narration. I'll just have to accept my speech inferiority and go forward with what I have in the future.

https://youtu.be/skHA9ejpDMk
VN Compiler. Why using Fable is too difficult. (Pt. 1)

I feel so tired today. Because of Fable bindings I went from being on top of the world, to burnout in like 5 minutes. It feels like I've gotten scammed by it.

12:45pm. https://www.reddit.com/r/fsharp/comments/13h8vj7/vn_compiler_why_using_fable_is_too_difficult_pt_1/

///

I won't lie, just thinking about having to deal with Fable bindings has caused me from to go from being on top of the world to full burn out at the flip of a switch. My stress has gone through the roof. Bindings were the main issue for me back in 2020 as well, and I went with TS for the VS Code extension for my language despite my preferences. But, there are alternative approaches we can try.

How many of you are doing web development in F#, but without Fable? Have any of you done codegen libraries for translating F# types to TS, as well as generating HTTP proxies?

This is the approach I'll want to try next, but if there are such libraries out there, I'd prefer to cover them instead.

///

12:55pm. Let me have breakfast.

Things feel so fucked up now. But I'll start work on Helix at least and have some fun doing that.

2:05pm. https://www.tabletmag.com/sections/news/articles/destined-live-quiet-times-progress-walter-russell-mead-via-meadia

Let me read this and I'll see if the weather is good enough for me to do the chores.

2:35pm. Let me do the chores.

2:55pm. Let me resume, though I am so tired right now that I am not sure if I'll get anything done. Change is stressful.

3:30pm.

https://pixabay.com/music/beats-spirit-blossom-15285/

///

You can see how it looks in the document here.
It is actually rather tedious to take this document and upload it to a site like Royal Road where we've been posting it.
What we'd do first is export it as an html project.

///

6:15pm. I nearly lost the project again. It seems renaming the project in Resolve can make it unsaveable.

I only managed to recover by renaming it back to the original. Shit.

That gave me a scare.

Two videos ago I was depressed so I aborted it forcefully after rendering it, but this one I definitely don't want to stop here.

6:15pm. 6:15m in. I'll close for the day here. I am too tired.

6:35pm. I won't check the F# sub. I couldn't stand getting into an argument right now.

The most important thing is to grasp momentum from here on out. I need to just keep going and going until I finish the Helix project.

As for the Leduc one, I can post it online whenever. I can figure out payments as I go along too, no need to make an useless art galery.

Enough of the toy projects.

I'll just do what I want."

---
## [selliott512/freedoom](https://github.com/selliott512/freedoom)@[8c076fcba9...](https://github.com/selliott512/freedoom/commit/8c076fcba9bb94637d22431b21b862a481fff01f)
#### Sunday 2023-05-14 16:55:44 by mc776

levels: minor Phase 2 fixes. (#964)

* levels: minor Phase 2 fixes.

Mostly for addressing #694.

Map05
Realigned grey hex textures around soulsphere switch. Now the odd one out is the door.

Map09
Fixed up the lighting in the start room.
Reflagged some secret doors as secret rather than hidden.
Consolidated the two W1 Floor to LAC triggers around the yellow key.
The red key rocket launcher sequence could potentially mess someone up who - given the hatchling closet, quite reasonably - avoids grabbing the rocket launcher. It seems needlessly convoluted, but it is a funny prank how the switch makes the red key disappear entirely for a bit. Instead of untangling this I'm just going to add some health bonuses around the rocket launcher so the player will eventually go there.
Tried to mitigate the worst of the various crimes against texture alignment in the crate maze, adding a light source in the process. It would take a *lot* of work to make it actually look good, a lot more than can be done in a batch bugfix PR.

Map10
Lower unpegged sector 70 (red door leading outside) door tracks.
Added matching midtexes to the insides of the fences around the lights by the door leading to the final corridor.
Line 839 (south-southeast red armour behind waterfall) flagged secret and the lines on the other side flagged hidden.

Map11
Realigned grey hexes in corridor around minigunner switch room.
Added an evil eye right in front of the shootwall secret.

Map12
Change line 330 midtex to the new MIDSPCSM with no offset.
Lower-unpegged line 4787 doortrack.

Map13
Sectors 243 no longer uses mismatching TLITE6_5 flat. (Sector 170 actually looks okay ingame.)
Realigned line 260.

Map15
Line 163 W1 changed to WR to prevent a potential softlock.
Aligned COMPSPAN on sector 561 to match surroundings.
Fixed some textures in the green corridor in the west overlooking the nukage. Also set those zombies in there to ambush since that seems to be the intention based on their placement, and made that big block thingy on the east end of that corridor a more normal-looking door.
Touched up greyhex near sector 491.
Flagged linedef 5293 secret.
Sectors 145 and 116 (rock fringe around nukage around red key platform) consolidated into one sector, made non-damaging, and without the invisible blocking lines.

Map16
Changed Line 1089 to SR instead of S1. (Switch that opens the secret to the east)
Realigned all the SUPPORT3s in that little painlord corridor while shrinking the "ribs" a bit; also widened the little exit atrium so the space between the lights is as wide as the door. (After looking at the others I am not going to widen any more corridors at this time.)
Grossly simplified the twisty yellow key corridor, and lowered the ceiling of the outside of the door so the yellow door stripe would fit properly. One doortrack needed to be given the DOORTRAK texture. The remaining "ribs" are recessed further inside the wall so they do not impede movement at all.
Lowered the ceiling above the other yellow marked door as well. The corridor around the corner has been expanded slightly.

Map22
Flagged line 830 secret.

Map23
Fixed candle placement on east end of zombieman corridor.
Consolidated some identical sectors around the big "AGM" floor and lowered the torch platforms so they wouldn't clip into the ceiling.
Raised the ceilings on the techpillars right after the first long lift. The walls in front of them now match their surroundings.
Removed lower unpegged from lines 2066, 2082, 2062, 2075. ("Door"tracks for the route across those pillars in the southeast - they're actually lifts not doors)
SSG secret fixed. (And marked.)

Map28
Lines 2326, 622 lagged secret.
Realigned lines 4594 and 4671.
Realigned scrolling textures around sector 517.
Touched up monster closet around sector 399, changing to to 8 about HAF fast and making the closet a bit taller so there'd be a better natural threshold between those areas. The doortracks were fine, if a bit complex.
Raised sector 474 ceiling to match marble brick seams.
Made sector 147 (cubes hanging over hot rocks) do damage and sectors 91 and 115 (teleport pads) not.

Map29
Swapped out the textures on the sides of the big green skull pad.

* levels: fix up map23 southeast secret textures.

I messed up the texture replacement around the green torch, the extreme sudden darkness ruined the blue AGM text, the pillar lift-doors needed a better division between the tekwall and red rock, and that huge swathe of DOORTRAK hurt to look at in vanilla.

* levels: map07 aesthetic fixes.

Replaced BIGDOOR1 on sector 50 as it was giving tutti-frutti.

Fixed the textures on the lifts in the green area beyond the outdoor area.

Miscellaneous texture alignment fixes and added some more thresholds between materials.

---
## [Fivestones-Tech/FivestonesPizza](https://github.com/Fivestones-Tech/FivestonesPizza)@[8c7de2dbe2...](https://github.com/Fivestones-Tech/FivestonesPizza/commit/8c7de2dbe22688bec478f7ca68e47d5b958faee4)
#### Sunday 2023-05-14 18:39:06 by Ogunaike Matthew Folawe

Pizza Website

Our amazing pizza will satisfy your cravings!

Customers can view and order from your pizza menu online with a pizza website, enhancing ease and accessibility. It also serves as a platform for promoting your business and cultivating a loyal client base via promotions, reviews, and social media integration.

I hope you're not already salivating because it looks as good as it tastes.

Show us your first time eating pizza and your thoughts in the comments area.

Let's work together on any project. I'm available to work.

---
## [TypeVar/Shiptest](https://github.com/TypeVar/Shiptest)@[84a2a8f394...](https://github.com/TypeVar/Shiptest/commit/84a2a8f394a0296ecc527f23c0da470b30280c0c)
#### Sunday 2023-05-14 18:39:55 by Bjarl

Die Of Fate Change (#1760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
replaces the die of fate's d20 effect (spawn you as wizard) with spawn
wizard clothes and magic mirror under you.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'm sick of wizards spawning without admin intervention
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
balance: You can't be turned into a wizard by the die of fate, instead
getting a magic mirror and wizard clothes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [4Gos23/Dynamic-Well](https://github.com/4Gos23/Dynamic-Well)@[9ea6f109b6...](https://github.com/4Gos23/Dynamic-Well/commit/9ea6f109b6032f42ecd8912026ac056e1605eaa7)
#### Sunday 2023-05-14 18:41:50 by 4Gos23

Create README.md Bringing unity and peace to our people joining together as one under God's flag. Uniting to overcome the systems that are attempting  to allow evil to overrun the Earth. The only way we can fight against these systems which are not personalities but principalities, and principalities are evil it means like legions and evil spirits.You must read the book the Bible.., it will tell you how to fight against these demons that attack us every day. Come here and find answers to questions that no one else can answer for you not even AI..

---
## [Outta-my-way-burrocrat/Divergences-HPM](https://github.com/Outta-my-way-burrocrat/Divergences-HPM)@[d8f35ccf1c...](https://github.com/Outta-my-way-burrocrat/Divergences-HPM/commit/d8f35ccf1c389a83306912cc051fdc69be5be6d3)
#### Sunday 2023-05-14 19:23:02 by Capitanloco6

Mesoameriga Patch

- Major content expansion for Mesoameriga
- Reworked the way the Congress of Andagoya works. RNG has been removed and the outcome will be fixed by your decisions, which now have actual consequences
-- Choice to revoke or maintain church privilege. Revoking church privilege removes education and administration maluses, but contributes to separatism score
-- Choice to revoke or maintain army privilege. Revoking army privilege contributes to your success score in the Congress, but will eventually lead to the revolt of a military junta
-- Choice to abolish or maintain slavery. Maintaining slavery contributes to your success score in the Congress, but will eventually lead to a slave revolt in Sonora
--- The resulting slave nation, Liberia, is playable and has expansion decisions to liberate the afroarcadian pops in Lusitania, the Caribbean and the Eastern Arcadian Seaboard.
-- Choice to abolish or maintain the caste system. Maintaining discrimination against the natives contributes to your success score in the Congress, but will eventually lead to the revolt of the indigenous League of Cemanahuac
- If the League of Cemanahuac is victorious, a dissolution event allows the player to choose between several new playable tags: the Nahua, Totonacs, Huastecs, Otomí, Mixtecs, Zapotecs, Mixe, Quiche and Yucatecs
- Nahua content. Choose between monarchical and republican paths
-- Monarchical Nahua path: restore Tenochtitlan, conquer Coatzacoalcos, deal with the criollos in Puebla-Veracruz and reclaim the lands of the Triple Alliance
-- Republican Nahua path: restore Cholollan, integrate the criollos and establish sister republics in Mesoameriga
- Otomí content. Rehabilitate the Valenciana mine, irrigate the Mezquital Valley, deal with the caciques, abolish the cargo system, integrate the criollos and reclaim the spoils of the Huayacocotlan campaign
- Huastecs, Yucatecs and Quiche. All three can form the League of Mayapan. Mayapan can break the power of the hacendados, build a transpeninsular railway, reform the administration to disempower the Batabo’ob and fund expeditions to find the lost cities of Yucatan
- Mixe content. An event will introduce the rivalry between the current Mixe King Chapital and the powerful cacique Eneedzaa, who serves as Minister of Development. Eneedzaa gives a powerful education bonus, but over time will keep adding more maluses to represent his oppressive methods. A decision can be taken to deal with Eneedzaa, giving up the education bonuses in exchange for accepting Mexican
- Mixe content. Integrate the Zoque and reclaim the Olmec lands.
- Mixtec content. Liberate the Mixteca Baja, extend to Coo Yuu irrigation system and reclaim the lands of Yucu Dzaa
- Zapotec content. Reclaim your cultural heritage at Lyobaa, revitalise the cochineal dye industry and reclaim the lands of Dani Baan.
- Totonac content. Rebuild the Three Hearts, reunify Totonacapan, promote mining in the former vanilla plantations and reclaim Teotihuacan
- Kurdistana Azad rebels now should persist longer on the map
- Removed pop demand effects form socialist and fascist modifiers that could potentially stop country-level demand of goods
- Fixed bug where dismantlement would release utility tags - Ainu Mosir no longer starts with any colonial provinces
- Athesia is now properly flagged as a New World nation
- Fixed Tarim provinces
- Tweaked Rwanda-Burundi RGOs to prevent pop starvation
- Miscellaneous localisation fixes
- Mesoamerigan natives are no longer forbidden from taking the Land of Opportunity decision. This is also now available for countries in Australia-New Zealand
- Foreign Smugglers and Legation Quarter modifiers for non-western nations now apply at the country rather than province level - Added an event for Gran Colombia to sell Para if it becomes an exclave following revolution in Granada

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[527fb7b003...](https://github.com/tgstation/tgstation/commit/527fb7b0030d13fc11939d88030b1dc4772742a6)
#### Sunday 2023-05-14 19:52:46 by DrTuxedo

ELEVATOR MUSIC: True Elevator Experience (#75388)

## About The Pull Request
Adds elevator music into the game that is played by an elevator panel.


https://github.com/tgstation/tgstation/assets/42353186/1a801604-3990-46ae-a96a-b3766b102d62

It's done by using loop sound, with a Kevin MacLeod "Local Forecast -
Elevator" (UNDER CC ATTRIBUTIONS 4.0, and we anyway used some other
Kevin MacLeod music) chopped into 8 small pieces.
The elevator panel has a variable which allows playing music but can be
changed in the map editor if you don't want it to play at certain
places.

(It also doesn't ignore walls, this means you can't hear the music
through wall or when elevator is closed)
## Why It's Good For The Game
Gives elevators more flavour and love, especially when people mostly
prefer stairs to those "laggy crushing machines."
Because of this people might instead hop into an elevator just to hear
meme elevator music, which is relaxing and might create comedic
situations (although elevators don't move that fast)
## Changelog
:cl: DrDiasyl aka DrTuxedo
sound: Nanotrasen have started installing music players in the elevators
to boost workers' morale.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [MI439-CLO/android_frameworks_base](https://github.com/MI439-CLO/android_frameworks_base)@[f2465af251...](https://github.com/MI439-CLO/android_frameworks_base/commit/f2465af25156e95e8d4931157c986e0040e90c6f)
#### Sunday 2023-05-14 22:37:16 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Jprimero15 <jprimero15@aospa.co>

---
## [AstrlJelly/HeavenStudio](https://github.com/AstrlJelly/HeavenStudio)@[f4ce182bf9...](https://github.com/AstrlJelly/HeavenStudio/commit/f4ce182bf995a7c6e4755ec7a6b83229cd76870b)
#### Sunday 2023-05-14 23:41:22 by AstrlJelly

oh my god i hate mr. downbeat

this "force" option is not very intuitive to use. nor is it coded amazingly. but i do not care. if you really wanna use it then mess around and see what works

---

