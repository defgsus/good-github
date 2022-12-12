## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-11](docs/good-messages/2022/2022-12-11.md)


1,734,052 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,734,052 were push events containing 2,336,831 commit messages that amount to 142,142,296 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [theycallmetommy/pirates](https://github.com/theycallmetommy/pirates)@[bb09705ff9...](https://github.com/theycallmetommy/pirates/commit/bb09705ff92407e89c1353911aac7cf27be40a3d)
#### Sunday 2022-12-11 00:23:48 by Thomas Fodera

so many fucking changes

-added more examples to the insults
-added a score tracker to insult fights
-added Macaque Island Treasure Coins

Coins are gained from insult fights and currently have no use, but will be used to buy drinks from the tavern... once I add the drinks

-added drink framework, and a few example drinks that currently do nothing

Next up, i'm going to be adding a drink that makes a crewmate lucky, a drink that cures a sick crewmate, and a drink that gives the player a new opening insult

-added a debug command to the port to give all insults
-added command to check coins
-fixed unintended crash when trying to show field description after fight
-implemented Sword Master boss fight

The fight works as intended, but it's a bit of a bitch to actually win if you get unlucky. Maybe having a Lucky crewmate should increase your odds, to give a use for the Lucky drink.

---
## [copperwater/xNetHack](https://github.com/copperwater/xNetHack)@[e8edc00a52...](https://github.com/copperwater/xNetHack/commit/e8edc00a5258fcb1ba2f9dd667551432453a26c5)
#### Sunday 2022-12-11 00:32:23 by copperwater

Allow cursed gain level in Sokoban to bypass a floor

Quite a lot of players see Sokoban as a tedious slog they nevertheless
have to finish in order to get some good prizes. This change alleviates
that slog, but still enforces a few key things:
- you are cheating on Sokoban, so you get the normal Luck penalty
  (unless the level was already completed)
- you don't get to skip part or all of the next puzzle, because you are
  placed on that level's downstairs
- the potion obviously has no effect on the final level, so you still
  need to solve that puzzle and get through the treasure zoo to claim
  the final prize
- it costs what may be a valuable escape item elsewhere

Notes:
- Not very many players will have cursed gain level at all by the time
  they reach Sokoban, let alone more than one of it. Someone who
  returns to Sokoban in the midgame might have more. I think it leads to
  interesting choices.
- Someone who skips a level then falls back down a hole may wind up in a
  strange location, but I don't believe anything odder than a position
  one could get into by poor boulder and scroll of earth management.

---
## [MrSableye/clovermon-showdown](https://github.com/MrSableye/clovermon-showdown)@[dc8905d5e0...](https://github.com/MrSableye/clovermon-showdown/commit/dc8905d5e0e9f789dcb0bad7be64b46fa848382c)
#### Sunday 2022-12-11 01:15:41 by Mr. Sableye

Moves Emplyin to OU (thought I forgot you? FUCK YOU STOP HITTING SE AGAINST MY FAIRIES YOU BITCH)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e766444468...](https://github.com/tgstation/tgstation/commit/e766444468445f084d3714b515003d3f40bbce69)
#### Sunday 2022-12-11 01:30:56 by LemonInTheDark

Changes our map_format to SIDE_MAP (#70162)


## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [esureos/Grasscutter](https://github.com/esureos/Grasscutter)@[88bc5c4c54...](https://github.com/esureos/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Sunday 2022-12-11 01:40:42 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[df5a689a58...](https://github.com/TaleStation/TaleStation/commit/df5a689a580c6763075a4853ada899d01743e435)
#### Sunday 2022-12-11 02:11:52 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic Mob Carp: Retaliate Element (#3605)

* Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

* Basic Mob Carp: Retaliate Element

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[02f229c051...](https://github.com/TaleStation/TaleStation/commit/02f229c05191b967f54e348dff6770673fe370ca)
#### Sunday 2022-12-11 02:11:52 by TaleStationBot

[MIRROR] [MDB IGNORE] Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. (#3595)

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. (#71674)

## About The Pull Request

- The chaplain choice beacon now uses a radial to select the armor set,
instead of a list, giving the user a preview of what each looks like.


![image](https://user-images.githubusercontent.com/51863163/205417930-f5ceab11-6974-48a9-a871-abcb8228bcf2.png)

- Lots of additional cleanup to choice beacon code in general. Less copy
pasted code.
- All beacons now speak from the beacon with their message, instead of
some going by "headset message". Soul removed

## Why It's Good For The Game

I always forgot when selecting my armor which looks like what, and
choosing an ugly one is a pain since you only get one choice. This
should help chaplains get the armor they actually want without needing
to check the wiki.

## Changelog

:cl: Melbert
qol: The chaplain's armament beacon now displays a radial instead of a
text list, showing previews of what all the armor sets look like
qol: (Almost) all choice beacons now use a pod to send their item,
instead of just magicking it under your feet
code: Cleaned up some choice beacon code. 
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

* Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup.

* Update choice_beacon.dm

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Jolly <70232195+Jolly-66@users.noreply.github.com>

---
## [zyro670/NotForkBot.NET](https://github.com/zyro670/NotForkBot.NET)@[696d2d4f71...](https://github.com/zyro670/NotForkBot.NET/commit/696d2d4f71c3f30e7e41b2496c22958ffa8ccbc5)
#### Sunday 2022-12-11 03:47:55 by Koi

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
## [simonw/disaster-data](https://github.com/simonw/disaster-data)@[5e8654efc6...](https://github.com/simonw/disaster-data/commit/5e8654efc6dfff8cb39c300baccd2de3152b1fec)
#### Sunday 2022-12-11 04:21:59 by disaster-scrapers

fema/shelters: 7 shelters removed

7 shelters removed:
  Mt. Enon Baptist Church in Dayton, OH (OPEN)
    https://www.google.com/maps/search/39.7551139,-84.2208322
    population = 0

  St. Bernadette Catholic Parish in Lakewood, CO (OPEN)
    https://www.google.com/maps/search/None,None
    population = 0

  Arapahoe County Fairgrounds in Aurora, CO (OPEN)
    https://www.google.com/maps/search/None,None
    population = 2

  Ann & Chuck Dever Center in Englewood, FL (OPEN)
    https://www.google.com/maps/search/26.924404,-82.314119
    population = 37

  Del Tura Shelter in North Fort Myers, FL (OPEN)
    https://www.google.com/maps/search/26.738655,-81.912434
    population = 151

  God's Grace Community Church in Houston, TX (OPEN)
    https://www.google.com/maps/search/None,None
    population = 0

  Moore County Parks and Recreation in Carthage, NC (OPEN)
    https://www.google.com/maps/search/35.303695,-79.416233
    population = 16

---
## [Patpat141214/app-dev](https://github.com/Patpat141214/app-dev)@[7b61e80ac4...](https://github.com/Patpat141214/app-dev/commit/7b61e80ac4435041841e38dfe8e03958fde8d432)
#### Sunday 2022-12-11 05:03:03 by Patpat141214

Update README.md

Violet Evergarden is a masterpiece that will make you feel once again through its brilliant storytelling and excellent presentation of emotions. The story revolves around our protagonist, Violet Evergarden, and her adventures of learning to understand others' emotions as well as her own.

Violet Evergarden is beautifully crafted in many senses. The emotional ups-and-downs that Violet experiences are truly touching and sincere, almost as if one was there by her side sympathising with her. Emotions throughout the series are displayed with a sense of truth and sincerity, hence making the story profoundly beautiful. Despite her unfortunate background and differences, there were still many kind individuals around her who continued to support her, befriend her, and even help her when she needed it the most. The story tugs at the heartstrings that many of us have long forgotten due to our extended lack of exposure to impactful content such as Violet Evergarden. Every story they have to offer is packed with emotional content and presented alluringly, which brings me to my next point - visuals.

---
## [nervere/vgstation13](https://github.com/nervere/vgstation13)@[e6156a8d91...](https://github.com/nervere/vgstation13/commit/e6156a8d91d8a24ebe6437f07198713f76946fc1)
#### Sunday 2022-12-11 07:46:36 by samo priimek

pulse demon tweaks (#33690)

* remove the stupid maxcharge tweak

* sneed

* comment unused stuff

* revert everything

* prevent you from killing yourself stupidly

* suck SMES faster, gain maxcharge when sucking APC's

* remove the capacity upgrade

* tweak the ability costs and upgrades

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[cf4a194e86...](https://github.com/OrionTheFox/Skyrat-tg/commit/cf4a194e86d53d57397f6de4febbea0de9c6ef57)
#### Sunday 2022-12-11 08:04:19 by SkyratBot

[MIRROR] Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! [MDB IGNORE] (#17828)

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.

<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.

![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @ MrMelbert about it and he gave me the go-ahead, as can be seen
here:

![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [01ste02/AoC2022](https://github.com/01ste02/AoC2022)@[71748d5a4b...](https://github.com/01ste02/AoC2022/commit/71748d5a4b225c472f23ecf46a6f4e3c65b5d9b5)
#### Sunday 2022-12-11 08:18:26 by Oskar Stenberg

Day 7. Advent of Bash going strong - but I will start slipping down from place 12 now. It took me 20 minutes to sort and find the smallest directory needed. Bash has limitations in places I do not like to admit, but it works. I'll be damned if it doesn't work. It still feels like a good idea and experience to write these challenges in bash - even though the language is not really made for it - but the portability of it is amazing. No compiler to install, and can run on most systems by default. I believe that all my solutions so far would be sh-compatible as well..

---
## [Imashitheadthatducks/FNF-PsychEngine](https://github.com/Imashitheadthatducks/FNF-PsychEngine)@[5fa1411931...](https://github.com/Imashitheadthatducks/FNF-PsychEngine/commit/5fa1411931c81cce489029ef0a7f48bce76570cd)
#### Sunday 2022-12-11 09:05:10 by Imashitheadthatducks

baby face paint

Anyone who spends more than 5 minutes in my presence knows that I never stop talking about how much I love busty, curvy, voluptuous anime ladies. Anyone who starts "digging for dirt" on me quickly learns that a pedophile narrative is never going to hold up, since I can't go longer than 60 seconds without talking about big boobs and thick booties.

Hah uhm- You look absolutely stunning tonight - I just thought I'd let you know that haha... so uh- what do you like to do- in your free time? Yeah I'm actually a- I'm actually a game developer, I've been making this game- it's called yandere simulator an-and a- and it's gotten a pretty - big following on the internet... uh- so basically in this game you play as - a yandere who - it's-it's a japanese term for a girl who loves her senpai so wha- senpai, it-it's a direct translation of upperclassmen, it's a term you would use in school, a-anyways, it's been kind of westernized as this term for - y'know a girls crushy calls him "senpai, senpai!" and uhm, hehe, so uh - you have your senpai and you have to eliminate any op- you have to eliminate- hah... ah- like, anything - anyone standing in-- mumbling sounds uhm... haha..- haha- I-I think our guy is coming... What's up guys welcome to pizza hut you guys ready to order? I'll take uhh, I'll take the breadsticks. Alright breadsticks anything else? What do you want beautiful? You don't want anything? That's fine. She'll uh- she'll share the breadsticks with me- Alright man i'll be back in a moment thank very much! Thank you- Really don't want anything? That's fine. I'll let you share your breadsticks with me- excuse me, I'll let you take some of my breadsticks haha... tongue clack I just wanna say um... inhale you look absolutely stuning tonight. Your eyes they're so- they're so beautiful... I... I think I love you…

BABY FACE PAINT X

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[70bcd3b6fb...](https://github.com/cmss13-devs/cmss13/commit/70bcd3b6fbcf17b4c26640321f23c83da0ab80a3)
#### Sunday 2022-12-11 09:56:31 by carlarctg

Queen eye shuffles weed sprites when passing over them. (#1901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Queen eye shuffles weed sprites when passing over them.

Fixed some single letter vars so the mantainer agenda can't delay this
PR from merging.



<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game


> Queen eye shuffles weed sprites when passing over them.

It's a way for marines to know there's an entire queen eye looking over
them. Basically means an MD isn't 100% necessary to know the queen will
broadcast the location of your flank to the entire hive.

https://streamable.com/kmnd72

It's more subtle than i wanted it to be, but WCYD. Also doesn't work on
corner sprites.

Also, it looks fucking creepy as hell! It's awesome.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

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

:cl:
add: Queen eye shuffles weed sprites when passing over them.
fix: Fixed some single letter vars so the mantainer agenda can't delay
this PR from merging.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Abhilash-T-R/Abhi](https://github.com/Abhilash-T-R/Abhi)@[c9d124fd3e...](https://github.com/Abhilash-T-R/Abhi/commit/c9d124fd3efae2f306296409386e94f53fa706ec)
#### Sunday 2022-12-11 10:43:28 by Abhilash-T-R

Merge pull request #1 from Yashwanthkumaram/main

fuck you

---
## [cmgchess/chess-openings](https://github.com/cmgchess/chess-openings)@[9f7632e84e...](https://github.com/cmgchess/chess-openings/commit/9f7632e84ebf35b79b8d3c08af9b95943cc54e59)
#### Sunday 2022-12-11 10:49:23 by Alexandru Duca

Scandinavian Defense: Portuguese Gambit

- Removed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. f3 Bf5` named `Scandinavian Defense: Portuguese Variation, Portuguese Gambit`.
- Renamed `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` from `Scandinavian Defense: Portuguese Variation` to `Scandinavian Defense: Portuguese Gambit`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` named `Scandinavian Defense: Portuguese Gambit, Banker Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` named `Scandinavian Defense: Portuguese Gambit, Classical Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` named `Scandinavian Defense: Portuguese Gambit, Correspondence Refutation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` named `Scandinavian Defense: Portuguese Gambit, Elbow Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` named `Scandinavian Defense: Portuguese Gambit, Jadoul Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` named `Scandinavian Defense: Portuguese Gambit, Lusophobe Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` named `Scandinavian Defense: Portuguese Gambit, Melbourne Shuffle Variation`.
- Added `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` named `Scandinavian Defense: Portuguese Gambit, Wuss Variation`.

This line `1. e4 d5 2. exd5 Nf6 3. d4 Bg4` in the Scandinavian Defense has many different names across chess literature. Selby Anderson released the book [Center Counter Defense: The Portuguese Variation](https://www.amazon.com/Center-Counter-Defense-Portuguese-Variation/dp/1886846103) in the year 1997 and, apparently, named it `Portuguese Variation`. In his book [Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943), [David Smerdon](https://en.wikipedia.org/wiki/David_Smerdon) called this line `Portuguese Complex`, but he noted that it was also called `Portuguese Opening` as well as `Jadoul Variation` [Section 1]. It's called `Portuguese Gambit` in Wikipedia's [list of chess gambits](https://en.wikipedia.org/wiki/List_of_chess_gambits#Scandinavian_Defense) and `Portuguese Variation` as well as `Jadoul Variation` in Wikipedia's article on the [Scandinavian Defense](https://en.wikipedia.org/wiki/Scandinavian_Defense#2...Nf6). (Unfortunately, I was unable to check the sources Wikipedia provides because I couldn't find the referenced books.)

Since Selby Anderson's book predates all other sources, there is an argument to name this line `Portuguese Variation`. However, Black delays taking back the pawn on d5 twice (first time with `2... Nf6` and second time with `3... Bg4`). This gives White the opportunity to secure the extra pawn with e.g. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4 Bg6 6. c4`. Additionally, Selby Anderson may not have been aware of the dubious nature of this variation ([Stockfish gives White +0.8](https://lichess.org/7CAhQOCs)). Furthermore, David Smerdon repeatedly refers to this line as a gambit despite calling it `Portuguese Complex`. Because of this, I argue that this line should be called the `Portuguese Gambit`.

[Smerdon's Scandinavian](https://www.amazon.com/Smerdons-Scandinavian-David-Smerdon/dp/1781942943) is currently the most extensive book on the `Portuguese Gambit`. It categorizes all major responses from White after `1. e4 d5 2. exd5 Nf6 3. d4 Bg4`. Smerdon also offers creative names for all variations covered by his theory. Here are the variations sorted by chapter:
1. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. c4` is called `The Banker`. (White "banks" the extra pawn with the immediate `5. c4`.)
2. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. c4` is called `The Jadoul`. (Named after [Michel Jadoul](https://de.wikipedia.org/wiki/Michel_Jadoul) who is one of the earliest exponents of the Portuguese Gambit [Introduction, Inspirational Game #1].)
3. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. Bb5+ Nbd7 6. Nc3` is called `The Melbourne Shuffle`. (Played by many australian IMs from Melbourne [Chapter 3]. It is named after a [rave dance](https://en.wikipedia.org/wiki/Melbourne_shuffle) which originated in Melbourne.)
4. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. f3 Bf5 5. g4` is called `The Correspondence Refutation`. (A line against the `Portuguese Gambit` successfully employed the correspondence community [Chapter 4].)
5. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Be2` is called `The Wuss`. (Apparently, `4. Be2` is a wimpy move and only a [wuss](https://www.merriam-webster.com/dictionary/wuss) would play it.)
6. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ Nbd7 5. Be2` is called `The Lusophobe`. (According to Wikipedia, [Lusophobia](https://en.wikipedia.org/wiki/Lusophobia) is irrational hostility, racism or hatred towards Portugal, the Portuguese people or the Portuguese language and culture. David Smerdon is making a joke by referring to the line `4. Bb5+ Nbd7 5. Be2` as "Anti-Portuguese" or "effective against the Portuguese Gambit".)
7. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Bb5+ c6` is called `The Elbow`. (Given the effectivness of the line `4. Bb5+ Nbd7 5. Be2`, occasionally playing `4... c6` may discourage players from studying it while preparing against you. Playing `4... c6` is a metaphor for hitting your well prepared opponent with your elbow [Chapter 7].)
8. `1. e4 d5 2. exd5 Nf6 3. d4 Bg4 4. Nf3` is called `The Classical`. (Refers to the fact that the move `4. Nf3` is principled [Chapter 8].)

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[00d3780c38...](https://github.com/Huffie56/cmss13/commit/00d3780c382c704f24e5c6f24aa36d88d509b7ea)
#### Sunday 2022-12-11 12:20:49 by carlarctg

PDT/L Buff (#1757)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

PDT/L kits now fold into cardboard.

Added many spare PDT/L kits and batteries to req. (Marines dropped them
off at req once they realized they were shitty milsurp knockoffs)

Made minibatteries tiny.

Added boldwarning span macro.

Improved locator tube sprites: Now has a pop-out battery slot at the top
that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.

Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Fixed a bug in which a string referenced a null var.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

When I saw the PDT/L kit, I was very interested. It seemed like a great
way to encourage teamwork and buddying up with some fun lore flavor on
the side. However, trying it out, it really feels bare-bones. I get it's
supposed to be 'crappy' because Boots magazine subscriber items suck and
so do the lives of every private on the corps, but the way that's
implemented really ruins the extremely cool concept that is being able
to locate your fellow buddies across the battlefield, so you don't need
to continually say HEY WHERE ARE YOU over comms in the many times you'll
get split up.

Thus I've heavily buffed them around the board, which you may think is
going way too far, and to an extent, you're _right._ It's intentional.
This is a really cool item that actively encourages teamwork and that's
why I would rather swing the buff hammer too hard than give it a paltry
buff and some qol that ultimately nobody cares about. It's the same as
the spotter kit. It's nuts, but needs teamwork to actually be useful.
And this should be encouraged.

If it is still deemed too strong, there are things we can do to
laterally nerf it without closing the PR outright. Making the tube not
work if the bracelet holder's dead, having it needs comms to work come
to mind, but there are surely others.

> Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.

The intention here is to let marines actually resupply their kits once
they run dry, and if they're proactive, maybe grab some and bring them
to FOB with them. Despite the description, the cells cannot easily be
recharged as power cell chargers are different from rechargers, they are
effectively Bay12 legacy that is VERY hard to come across.

'What if someone carries like 5 of them in their bag? That'd completely
nullify the power drain part.'

The stinger here is 'in the bag'. There are not enough reasons to carry
bags and satchels in this game right now as the sheer amount of storage
for goods marines have make them a one-man-army with two primaries. If a
marine forgoes a shotgun that might save them from a 1-pounce capping
runner for 5 spare LT batteries, a default medkit, and two flare boxes,
they are well within their rights to do so.

> Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)

This lets req drop them off at FOB if they eventually figure out they
can drop unvended surplus there. If this somehow happens, marines who
never even glanced at the kit in loadout or prep will notice it exists
and maybe, just maybe, use them!

> Made minibatteries tiny.

You may think this contradicts my earlier point about sacrificing
storage value, but _actually_ think about it. All webbing types, armor
slots, pouches, belts, even the helmet, all share the common attribute
of not caring about item size. If it's small or medum it still takes 1
out of the 3 slots in medium armor. Any storage item that isn't a
satchel, effectively. Every spare battery taken directly in the average
marine's inventory is one slot less for 5 shotgun shells, one magazine,
one unga juice flask, binoculars. What this means in the end is simply
that marines may carry one to two spare batteries in their helmet (I
think) at the cost of Drip which few marines will trade for, and satchel
marines don't have to sacrifice a lot of space for the spare battery.
Plus, it makes sense, why wouldn't a small AA rechargeable battery be
tiny.

> Improved locator tube sprites: Now has a pop-out battery slot at the
top that shows up if emptied. The main green stripe is now a battery
indicator with appropiately-faded-out yellow warning and blinking red
danger sprites. The small notch at the bottom is now a bracelet
indicator that turns off without a battery and blinks red if the
bracelet was somehow destroyed.

This looks so sick!

> Added a ton of sounds to interactions with the PDT/L kit. Beeps on
scanning, buzzes on errors, clicks on handling.

Adding sounds to items should be standarized, I think. There are so many
cool sounds in the sound/machines folder that go unused. Personally i
felt like these small stupid sounds added a LOT to the atmosphere of
this tiny locator tube and bracelet. Alien Isolation is known for its
sounds, we should strive to emulate that.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
add: Added vendable spare batteries for the locator tube in its vendors,
alongside one spare in every PDT/L kit.
qol: PDT/L kits now fold into cardboard.
add: Added many spare PDT/L kits and batteries to req. (Marines dropped
them off at req once they realized they were shitty milsurp knockoffs)
balance: Made minibatteries tiny.
refactor: Added boldwarning span macro.
imageadd: Improved locator tube sprites: Now has a pop-out battery slot
at the top that shows up if emptied. The main green stripe is now a
battery indicator with appropiately-faded-out yellow warning and
blinking red danger sprites. The small notch at the bottom is now a
bracelet indicator that turns off without a battery and blinks red if
the bracelet was somehow destroyed.
qol: The locator tube and PDT bracelet now share a serial number, easily
viewed via examination. This lets you see which PDT/L kits are paired.
soundadd: Added a ton of sounds to interactions with the PDT/L kit.
Beeps on scanning, buzzes on errors, clicks on handling.
fix: Fixed a bug in which a string referenced a null var.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[ce39f048bf...](https://github.com/Huffie56/cmss13/commit/ce39f048bf5eb25e2a93d7355327ccacc0504b01)
#### Sunday 2022-12-11 12:20:49 by carlarctg

Buffed, resprited, enhanced Oppressor. (#1732)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

**Resprited Oppressor! Pics here:**


![image](https://user-images.githubusercontent.com/53100513/204121775-9f4acd11-d818-46e8-81d3-c38bdfdabf5c.png)

Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Oppressor can hook over the M2C and M56D again.

Oppressor can hook over ledges. (UNIMPLEMENTED)

Tail stab's main ability usage is moved to a different proc for future
custom tail stabs.

Redesigned Tail Stab for Oppressor. Tail seize now utilizes a projectile
and beams to fire a 3-tile reaching tail hook, that pulls in AND DOES
NOT STUN marines. (It slows them for 0.5 seconds)

![Screenshot_20221127-032533~2](https://user-images.githubusercontent.com/53100513/204122365-e1ee57f7-1b9d-443e-a45c-dceec07a88d3.png)

Oppressor's abduct has had its effect strings changed to imply coiling
and uncoiling of the tail. Captured targets will now have a beam of the
Oppressor's tail attached to them (Purely visual) until they reach the
Praetorian, alongside an overlay of the vice grip on their legs.

Added a proc, .ammo/on_bullet_generation(), for the ammo datum to apply
effects to the generated bullet/projectile.

Added the bound_beam variable to projectiles. Could be used in the
future for things like harpoon guns, lasers, etc.

Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

Videos tomorrow.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Re-added animated telegraphs for Abduction. They've been tweaked to
always have the default border - that way, the weird way byond handles
short-lived animated objects doesn't make the telegraph absurdly small.
It can always be easily seen.

Animated telegraphs looked really cool, but (I presume) were removed
because BYOND sometimes freezes or starts animations midway through when
short lived animated objects show up, for some reason. I effectively
made it so these are irrelevant by slapping on the border - The animated
effects are just a bonus and will not impact visibility, and in fact
enhance it.

> Oppressor can hook over the M2C and M56D again.

Everyone I've talked to agrees that there really is no reason for these
weapons to protect from abduction. The player can just.. move out of the
way, or even rest if they're in a crowded spot. It's also very
frustrating to see it get in the way of *other* abducts that bonk into
it. The player is going immobile in range of a xenomorph that punishes
immobility.

> Oppressor can hook over ledges. (UNIMPLEMENTED)

Couldn't replicate this issue for some reason... So uh. I dunno.

> Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)

Geeves approved.

This looks so fucking awesome. The slow is barely a thing, so I wouldn't
fret about slow creep. The reaching hook does no damage, only pulls
targets closer. This isn't necessarily super strong, but it's mega cool
and fits with Oppressor's theme of dislocation. I also changed the
windup from 1s to 0.5s so it can be utilized during combat, but this
could be reverted if it's too strong somehow.

> Fixed non-damaging projectiles causing a blood spurt. (It was checking
flags && FLAG instead of flag & flag, remember to use CHECK_BITFIELD
folks!)

This looked stinky on the tail seize.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Carlarc, Mikola Wei

imageadd: Resprited Oppressor, sprites made by Mikola Wei.
imageadd: Re-added animated telegraphs for Abduction. They've been
tweaked to always have the default border - that way, the weird way
byond handles short-lived animated objects doesn't make the telegraph
absurdly small. It can always be easily seen.
balance: Oppressor can hook over the M2C and M56D again.
refactor: Tail stab's main ability usage is moved to a different proc
for future custom tail stabs.
add: Redesigned Tail Stab for Oppressor. Tail seize now utilizes a
projectile and beams to fire a 3-tile reaching tail hook, that pulls in
AND DOES NOT STUN marines. (It slows them for 0.5 seconds)
imageadd: Oppressor's abduct has had its effect strings changed to imply
coiling and uncoiling of the tail. Captured targets will now have a beam
of the Oppressor's tail attached to them (Purely visual) until they
reach the Praetorian, alongside an overlay of the vice grip on their
legs.
refactor: Added a proc, .ammo/on_bullet_generation(), for the ammo datum
to apply effects to the generated bullet/projectile.
refactor: Added the bound_beam variable to projectiles. Could be used in
the future for things like harpoon guns, lasers, etc.
fix: Fixed non-damaging projectiles causing a blood spurt. (It was
checking flags && FLAG instead of flag & flag, remember to use
CHECK_BITFIELD folks!)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

Co-authored-by: harryob <me@harryob.live>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a3e7c70f6d...](https://github.com/tgstation/tgstation/commit/a3e7c70f6da0fc7ea9929ddb39beddcf3113707f)
#### Sunday 2022-12-11 12:31:11 by necromanceranne

Bodypart code cleanup, robotic limbs can actually be disabled through damage again. (#71739)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Cleans up various variables and code comments in bodypart code so that
it is easier to understand (hopefully) what the fuck is happening there.

Fixes a hilarious oversight. For what may have been an entire 2 year
span, robotic limbs were unable to be disabled whatsoever. Good stuff.

## Why It's Good For The Game

Lost all your limbs and now have only surplus prosthetics?
Congratulations! You're now more durable than even someone with proper
robotic limbs, as your arms do not contribute anything more than 10
damage (or 15 stamina) to your overall damage taken. Furthermore, taking
the maximum amount of damage is actually entirely meaningless to you.

Laugh as someone attempting to shoot your arms does almost no meaningful
damage once you hit the cap! It's all sunk cost! You can't have it blown
off anyway, because dismembering surplus limbs is gone!

Who knew getting into a horrible bluespace/goliath accident could have
such an impact on your combat prowess. Thanks Nanotrasen!

Anyway, these vars are ugly.

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
code: Makes a lot of the bodypart variables clearer as to what they do.
Includes more detailed code comments.
fix: Robotic limbs are no longer immune to being disabled through
reaching maximum damage.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Kazakazara/tgstation](https://github.com/Kazakazara/tgstation)@[5b4ba051a0...](https://github.com/Kazakazara/tgstation/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Sunday 2022-12-11 12:38:59 by LemonInTheDark

Builds logic that manages turfs contained inside an area (#70966)

## About The Pull Request

Area contents isn't a real list, instead it involves filtering
everything in world
This is slow, and something we should have better support for.

So instead, lets manage a list of turfs inside our area. This is simple,
since we already move turfs by area contents anyway

This should speed up the uses I've found, and opens us up to using this
pattern more often, which should make dev work easier.

By nature this is a tad fragile, so I've added a unit test to double
check my work

Rather then instantly removing turfs from the contained_turfs list, we
enter them into a list of turfs to pull out, later.
Then we just use a getter for contained_turfs rather then a var read

This means we don't need to generate a lot of usage off removing turf by
turf from space, and can instead do it only when we need to

I've added a subsystem to manage this process as well, to ensure we
don't get any out of memory errors. It goes entry by entry, ensuring we
get no overtime.
This allows me to keep things like space clean, while keeping high
amounts of usage on a sepearate subsystem when convienient

As a part of this goal of keeping space's churn as low as possible, I've
setup code to ensure we do not add turfs to areas during a z level
increment adjacent mapload. this saves a LOT of time, but is a tad
messy

I've expanded where we use contained_turfs, including into some cases
that filter for objects in areas. need to see if this is sane or not.

Builds sortedAreas on demand, caching until we mark the cache as
violated

It's faster, and it also has the same behavior

I'm not posting speed changes cause frankly they're gonna be a bit
scattered and I'm scared to.
@Mothblocks if you'd like I can look into it. I think it'll pay for
itself just off `reg_in_areas_in_z` (I looked into it. it's really hard
to tell, sometimes it's a bit slower (0.7), sometimes it's 2 seconds
(0.5 if you use the old master figure) faster. life is pain.)

## Why It's Good For The Game

Less stupid, more flexible, more speed

Co-authored-by: san7890 <the@san7890.com>

---
## [Evolution-X/frameworks_base](https://github.com/Evolution-X/frameworks_base)@[69a013f3c8...](https://github.com/Evolution-X/frameworks_base/commit/69a013f3c85e4942cef7746cee7caeadb4924edf)
#### Sunday 2022-12-11 14:12:53 by Joey Huab

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

---
## [ferminhg/rust](https://github.com/ferminhg/rust)@[7a49959ea4...](https://github.com/ferminhg/rust/commit/7a49959ea4aa3dbe3f5dd23a1de909196d62ea13)
#### Sunday 2022-12-11 14:25:50 by Remo Senekowitsch

xorcism: remove rstest dependency (#1590)

rstest uses proc macros, which make the tests timeout due to long
compile times. Replace rstest with a custom declarative macro.

Brings test time from 7.5 seconds to 0.8 seconds on my machine.

Drawbacks:
* more indentation
* module structure of tests is flipped around

both of those seem minor to me. 

Although declarative macros can be hard to read for those unfamiliar, 
that was already somewhat the case with rstest's magic in my opinion. So
I personally don't think it's worse in terms of the students being able to
understand the tests.

The only other alternative I see is to disable the online tests 
altogether and leave a note about that in the exercise description. That
probably wouldn't be that bad, since people solving this hard exercise
most likely have a solid local setup. But it would still be cool to run
the tests online as well.

https://github.com/exercism/rust/issues/1513

---
## [Malii47/GucluSarp](https://github.com/Malii47/GucluSarp)@[50fc9a6fdf...](https://github.com/Malii47/GucluSarp/commit/50fc9a6fdfee3acbbf32fbb267b65246afec7dfb)
#### Sunday 2022-12-11 14:41:39 by Malii47

STUPID FUVKING GAME STUPID FUCKING SOUND EFFECTS

-NOW THERE IS A OUTPUT IN CONSOLE DEPENDS ON IF ENEMY STUNNED BY GETTIN ATTACKED OR DEFLECTED OR ONLY DEFLECTED

---
## [PhilGanney/btnCode](https://github.com/PhilGanney/btnCode)@[3627e57998...](https://github.com/PhilGanney/btnCode/commit/3627e57998a9c712ee823aa7d0598fa7249afd3c)
#### Sunday 2022-12-11 14:42:21 by Phil Ganney

Take 2: Transitions should not effect resizing

.. but they should still happen elsewhere!!

(that last commit, I tried to fix a new issue with resizing the text area, and sort of fixed it, but not how I thought I was fixing it! I was actually wiping over the transition rule on everything, not adding an additional rule. It also turns out that it is the height and width properties changing that need to be instant. - I really did not think those changes through thoroughly! - one of those fixes where you say "oh yeah I remember how CSS actually works" and then promptly facepalm

---
## [a-person-you-dont-know123/garrysmod-chatsounds](https://github.com/a-person-you-dont-know123/garrysmod-chatsounds)@[1cbfb34565...](https://github.com/a-person-you-dont-know123/garrysmod-chatsounds/commit/1cbfb34565efcd1405ad86e143857a018222ffbb)
#### Sunday 2022-12-11 15:50:42 by Sensuka

attempt number 2

lol

Add files via upload

Delete barbecue bacon burger.ogg

Delete bbq bacon burger.ogg

Delete billy earl.ogg

Delete cause clearly the last ass whopping you got wasnt good enough bitch.ogg

Delete get the fuck off my shit you stankin bitch.ogg

Delete im gonna beat the shit out of you if you dont stop fucking with me.ogg

Delete im gonna beat the shit out of you.ogg

Delete im gonna beat your ass.ogg

Add files via upload

Add files via upload

---
## [casswedson/Cataclysm-DDA](https://github.com/casswedson/Cataclysm-DDA)@[8e39d6f97c...](https://github.com/casswedson/Cataclysm-DDA/commit/8e39d6f97c358c72a3dacc7c2f3ce955ecb30e81)
#### Sunday 2022-12-11 16:39:51 by casswedson

fix: edge case ci error exit (#62660)

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

Co-authored-by: casswedson <casswedson@users.noreply.github.com>

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[ef7768b85d...](https://github.com/GeoB99/reactos/commit/ef7768b85d1c34c78cf769773bcfa35005c69771)
#### Sunday 2022-12-11 19:03:52 by George Bișoc

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
## [Kohl1998/bootstrap-portfolio](https://github.com/Kohl1998/bootstrap-portfolio)@[114a4d076f...](https://github.com/Kohl1998/bootstrap-portfolio/commit/114a4d076fd57adb2da2215058ddd638e94235a9)
#### Sunday 2022-12-11 19:26:15 by kohlvbusiness98@gmail.com

Merge branch 'main' of github.com:Kohl1998/bootstrap-portfolio

For this application I built a webpage where I could showcase projects I have built using only HTML & CSS.

The reason I wanted to have my own web page is because I wanted to have a one-stop shop for potential employeers, who could visit my portfolio to see all my deployed applications. Also, I want to be able to show friends & family my projects.

During the process I learnt how to using flex-box grids to display my projects & how to use the justify-content property within CSS.

I setup a remote repo on Github to work from, which I then cloned to my local repository so I can have the two in sync.

Afterwards, I used vscode which is an integrated development environment which allowed me to update the software code.

Lastly, once I was done I pushed all the updates to my remote repository from my local repo using commits, and once I was happy I deployed the changes to the live website.

```md
    ![alt text](starter/css/images/Deployed-Portfolio.svg)
    ```

I used 'Slack' for support - https://slack.com/intl/en-gb

Please refer to the LICENSE in the repo.

For this application there is a navigation bar within the header which includes more in depth information, which you can access by clicking any of the links to jump straight to the section. Also, there is the open to scroll down the page using the scroller.

Lastly, my personal social media can be accessed by clicking on the 'contact me' link in the header naviagtion.

https://kohl1998.github.io/Personal-Portfolio/ Please enter a commit message to explain why this merge is necessary,

---
## [stgraber/lxd](https://github.com/stgraber/lxd)@[de0d151a2c...](https://github.com/stgraber/lxd/commit/de0d151a2cc9bd8cef31431e126649e2b6a18be7)
#### Sunday 2022-12-11 21:35:43 by Thomas Parrott

lxd/instance/drivers/driver/qemu: Fix macvlan NICs losing connectivity on LXD restart

Switch to using monitor.SendFile() rather than monitor.SendFileWithFDSet(), as there
appears to be some rather strange behaviour going on with QEMU when used with macvtap
NICs.

If you pass the macvtap file handles using monitor.SendFileWithFDSet() it will use a
separate FD set for each file handle. This works fine, and I can see the correct file
handles opened by the QEMU process. But when LXD is restarted (the monitor connection
is closed), the file handles are closed by QEMU, causing the connectivity to break.

I have experimented with using the same FD set for all file handles associated to a
particular macvtap NIC. This didn't fix the issue.

I also tried hard coding the FD set ID to 0. This meant that the macvtap NIC would
share an FD set with the root disk device. Interestingly this solved the issue.
However it made me uncomfortable as the root disk is only configured by referencing
the FD set ID itself, rather than a particular FD inside the set. So I don't think
that sharing an FD set with multiple devices is a good idea.

However it got me thinking that perhaps the fact that the root disk is referencing
the FD set by ID (i.e using file=/dev/fdset/0 in its config) meant that QEMU somehow
realised that the FD set should be persisted even after the monitor has disconnected.

I confirmed that using the same FD set (even if a different ID than 0) for macvtap NICS
as the root disk device fixed the issue.

But because of my discomfort at that scenario (explained above) I instead looked for
a different solution. Before introducing multi-queue macvlan support for VMs we were
using monitor.SendFile() which worked fine. However I had switched to using the
monitor.SendFileWithFDSet() function as the former didn't support accessing the specific
FD number that was created inside QEMU. I thought we needed this because all the
documentation around using multi-queue macvtap devices showed the use of numeric FDs.

However on further exploration it turns out that we can infact use monitor.SendFile,
and by sending each file handle with a unique name we can then refer to those file
handles using the same names in `fds` setting for the macvtap devices.

Note: Because the `fds` list is colon separated one cannot use colons in the file
handle names. And I also experienced issues with connectivity when using dashes in
the file handle names. So I opted for using full-stops instead.

Fixes #11201

Signed-off-by: Thomas Parrott <thomas.parrott@canonical.com>

---
## [AllyTally/VVVVVV](https://github.com/AllyTally/VVVVVV)@[86d90a1296...](https://github.com/AllyTally/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Sunday 2022-12-11 22:52:10 by Misa

Add color support to Windows console output, properly

This adds color support to the output of the console on Windows. Now if
you're using Windows 10 build 1511 or later (I think it's build 1511
anyway; they added more VT sequence support in later versions), you will
see colors by default. This isn't due to Windows helping in any way;
this commit has to specifically enable it with SetConsoleMode() because
by default, Windows won't enable color support unless we enable it. (Or
if it's enabled in the registry, but having to go through the registry
to enable basic shit like that is completely fucking stupid.)

I tested this in my Windows 10 virtual machine and it's completely
working.

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[ebc0227176...](https://github.com/jlsnow301/tgstation/commit/ebc0227176b5213f379eefc3f5c6aa7be2d09c0a)
#### Sunday 2022-12-11 23:27:04 by Tastyfish

Makes dog a basic mob [MDB IGNORE] (#70799)


About The Pull Request

    Made a basic version of the pet base called /mob/living/basic/pet. It's significantly more stripped down from the old simple_animal one, because its half collar stuff and...

    Made the collar slot a component that you could theoretically remove from a pet to disable the behavior, or add to any other living mob as long as you set up the icon states for the collar (or not, the visuals are optional).
        The corgi's collar strippable slot is now generally the pet collar slot, and in theory could be used for other pet stripping screens.

    I also gutted the extra access card code from /mob/living/basic/pet as it's only being used by corgis. Having a physical ID is now just inherent to corgis, as they're the only ones that could equip it anyway.

    Ported the make_babies() function from simple_animals to a new subtree and associated behavior, called /datum/ai_planning_subtree/make_babies that uses blackboards to know the animal-specific info.
        Note that it's marginally improved, as the female walks to the male first instead of bluespace reproduction.

    Tweaked and improved the dog AI to work as a basic mob, including making /datum/idle_behavior/idle_dog fully functional.

    Made a /datum/ai_planning_subtree/random_speech/dog that pulls the dynamic speech and emotes to support dog fashion.

I've tested base collars across multiple pet types.

For dogs, I've tested general behavior, fetching, reproduction, dog fashion, and deadchat_plays, covering all the oddities I'm aware of.

image
Why It's Good For The Game

Very big mob converted to a basic mob.
Changelog

cl
fix: Lisa no longer uses bluespace when interacting with Ian.
refactor: A large portion of dog code was re-written; please report any strange bugs.
/cl

---
## [keydon/adventOfCode](https://github.com/keydon/adventOfCode)@[1ecac8e58b...](https://github.com/keydon/adventOfCode/commit/1ecac8e58ba35fa5973acc9d721001a0943109fe)
#### Sunday 2022-12-11 23:33:43 by Lukas Bugaj

--- Day 11: Monkey in the Middle ---

As you finally start making your way upriver, you realize your pack is much lighter than you remember. Just then, one of the items from your pack goes flying overhead. Monkeys are playing Keep Away with your missing things!

To get your stuff back, you need to be able to predict where the monkeys will throw your items. After some careful observation, you realize the monkeys operate based on how worried you are about each item.

Figure out which monkeys to chase by counting how many items they inspect over 20 rounds. What is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans?

--- Part Two ---
You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.

Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?

---

