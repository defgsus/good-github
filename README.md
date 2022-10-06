## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-05](docs/good-messages/2022/2022-10-05.md)


2,094,213 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,094,213 were push events containing 3,147,393 commit messages that amount to 246,304,976 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [sjp38/linux](https://github.com/sjp38/linux)@[bd343f365d...](https://github.com/sjp38/linux/commit/bd343f365df59de2b9cbc2ac55d3d77534b0f10c)
#### Wednesday 2022-10-05 00:20:27 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[f923f61011...](https://github.com/TheBoondock/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Wednesday 2022-10-05 00:39:11 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[844574b621...](https://github.com/k21971/EvilHack/commit/844574b62157db544c1b9af1683b8cba4b0cc12f)
#### Wednesday 2022-10-05 00:50:56 by k21971

Sanctum/ascension run revamp: part 1 (sanctum).

This is the first part of the sanctum/ascension run revamp for EvilHack.
The plan is this: instead of the player having to trek all the way back
out through Gehennom and the dungeon to escape and enter the elemental
Planes, they will instead make their way from the bottom of Gehennom
(the Sanctum) up through Purgatory, and then be deposited in the dungeon
on the same level as their quest home entrance (this is in case the
player needs to chat with their quest leader again). They then traverse
the few remaining dungeon levels to the Planes. Purgatory will only be
2-3 levels at most, but will be just as difficult as the Sanctum, if not
more so. It won't be an easy trek back out to the Planes, but it will be
a much shorter and less tedious one.

Part one focuses on the Sanctum, and the west side of the map has been
redesigned to accommodate the changes. Once the player acquires the
Anulet of Yendor (for Infidels, imbue the Idol of Moloch), a gate is
formed in the west wall of the inner sanctum, leading to a previously
unreachable part of the map. At the same time that this gate magically
appears, the stairs leading back up out of the sanctum are removed, and
all other forms of leaving the sanctum (branchporting, levelporting, or
quaffing a cursed potion of gain level) are suppressed. The only way to
leave the sanctum and continue is through the newly formed gates, and to
face the monsters within.

In this new section resides Lucifer, the most powerful demon prince of
them all. He guards the magic portal that leads to Purgatory. His
entourage are four named balrogs waiting outside his inner chamber.
Lucifer will not engage until the player attacks or moves next to him.
His attacks, while not as severe as Demogorgon's illness attack or
Graz'zt's stealing ability, are stong enough to be taken seriously.
Lucifer also spawns with 666 hit points, so he won't be an easy or quick
kill, even with silver weapons.

There's room for improvement here, such as the com_pager() dialogue, or
what gear Lucifer could spawn with, and so on. I added the branch port
location to Purgatory in the .des file, but as of this commit, it isn't
active yet since the Purgatory branch hasn't been created. Once
Purgatory is created - if the player needs to go back there for any
reason once they've exited and are back in the regular dungeon, they
will have the ability to travel back down to the bottom of Gehennom and
enter the Sanctum via the stairs formed during the invocation, and then
through the portal to Purgatory again.

In this commit, there's also a bugfix concerning u.uachieve.amulet and
when an Infidel actually imbues the Idol of Moloch.

---
## [zyro670/NotForkBot.NET](https://github.com/zyro670/NotForkBot.NET)@[97d1c85670...](https://github.com/zyro670/NotForkBot.NET/commit/97d1c856704c1c87f102ab512303491675df8085)
#### Wednesday 2022-10-05 01:22:30 by Koi

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
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[14c96d05b8...](https://github.com/JohnFulpWillard/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Wednesday 2022-10-05 01:46:05 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[99b8d6b494...](https://github.com/JohnFulpWillard/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Wednesday 2022-10-05 01:46:05 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [AeroAstroid/TheBrainOfTWOWCentral](https://github.com/AeroAstroid/TheBrainOfTWOWCentral)@[77ffb5a311...](https://github.com/AeroAstroid/TheBrainOfTWOWCentral/commit/77ffb5a311c828134d4c28fec4ae92b31bc76539)
#### Wednesday 2022-10-05 03:32:43 by Purplegaze

give me power (the sequel)

[man's voice] Once upon a time in a kingdom far, far away, the king and queen were blessed with a beautiful baby girl. And throughout the land, everyone was happy... until the sun went down and they saw that their daughter was cursed with a frightful enchantment that took hold each and every night. Desperate, they sought the help of a fairy godmother who had them lock the young princess away in a tower, there to await the kiss... of the handsome Prince Charming. [horse whinnies] It was he who would chance the perilous journey through blistering cold and scorching desert traveling for many days and nights, risking life and limb to reach the Dragon's keep. [crows caw] For he was the bravest, and most handsome... in all the land. And it was destiny that his kiss would break the dreaded curse. He alone would climb to the highest room of the tallest tower to enter the princess's chambers, cross the room to her sleeping silhouette, pull back the gossamer curtains to find her... [gasps] What? - Princess... Fiona? - No! [sighs relief] Oh, thank heavens. Where is she? - She's on her honeymoon. - Honeymoon? With whom? - She's on her honeymoon. - Honeymoon? With whom? [ Counting Crows: Accidentally In Love] So she said what's the problem, baby? What's the problem? I don't know Well, maybe I'm in love Think about it every time I think 'bout it Can't stop thinking 'bout it How much longer will it take to cure this? Just to cure it, cause I can't ignore it If it's love, love Makes me wanna turn around and face me But I don't know nothing bout love Oh, come on, come on - [screams] - Turn a little faster Come on, come on The world will follow after Come on, come on Everybody's after love So I said I'm a snowball running Running down into this spring that's coming all this love Melting under blue skies belting out sunlight Shimmering love Well, baby, I surrender To the strawberry ice cream Never ever end of all this love Well, I didn't mean to do it But there's no escaping your love These lines of lightning mean we're never alone Never alone, no, no Come on, come on Jump a little higher Come on, come on If you feel a little lighter Come on, come on We were once upon a time in love Hyah! We're accidentally in love Accidentally in love Accidentally in love Accidentally in love Accidentally in love Accidentally in love Accidentally in love Accidentally I'm in love, I'm in love, I'm in love, I'm in love I'm in love, I'm in love Accidentally in love I'm in love I'm in love It's so good to be home! - [distant singing] - [giggling] Just you and me and... [Donkey sings] - Two can be as bad as one... - Donkey? Shrek! Fiona! Aren't you two a sight for sore eyes! Give us a hug, Shrek, you old love machine. [chuckles] And look at you, Mrs. Shrek. How 'bout a side of sugar for the steed? Donkey, what are you doing here? Taking care of your love nest for you. Oh, you mean like... sorting the mail and watering the plants? - Yeah, and feeding the fish! - I don't have any fish. You do now. I call that one Shrek and the other Fiona. That Shrek is a rascally devil. Get your... Look at the time. I guess you'd better be going. Don't you want to tell me about your trip? Or how about a game of Parcheesi? Actually, Donkey? Shouldn't you be getting home to Dragon? Oh, yeah, that. I don't know. She's been all moody and stuff lately. I thought I'd move in with you. You know we're always happy to see you, Donkey. But Fiona and I are married now. We need a little time, you know, to be together. Just with each other. Alone. Say no more. You don't have to worry about a thing. I will always be here to make sure nobody bothers you. - Donkey! - Yes, roomie? You're bothering me. Oh, OK. All right, cool. I guess... Me and Pinocchio was going to catch a tournament, anyway, so... Maybe I'll see y'all Sunday for a barbecue or something. He'll be fine. Now, where were we? [giggles] Oh. I think I remember. - Donkey! - [Fiona yelps] I know, I know! Alone! I'm going! I'm going. What do you want me to tell these other guys? [fanfare] [ theme to Hawaii Five-O] Enough, Reggie. [clears throat] "Dearest Princess Fiona. "You are hereby summoned to the Kingdom of Far, Far Away for a royal ball" in celebration of your marriage "at which time the King will bestow his royal blessing..." upon you and your..." uh..."Prince Charming. "Love, the King and Queen of Far, Far Away. aka Mom and Dad.""" Mom and Dad? - Prince Charming? - Royal ball? Can I come? - We're not going. - [both] What? I mean, don't you think they might be a bit... shocked to see you like this? [chuckles] Well, they might be a bit surprised. But they're my parents, Shrek. They love me. And don't worry. They'll love you, too. Yeah, right. Somehow I don't think I'll be welcome at the country club. Stop it. They're not like that. How do you explain Sergeant Pompous and the Fancy Pants Club Band? Oh, come on! You could at least give them a chance. To do what? Sharpen their pitchforks? No! They just want to give you their blessing. Oh, great. Now I need their blessing? If you want to be a part of this family, yes! Who says I want to be part of this family? You did! When you married me! Well, there's some fine print for you! [exasperated sigh] So that's it. You won't come? Trust me. It's a bad idea. We are not going! And that's final! Come on! We don't want to hit traffic! [Gingy] Don't worry! We'll take care of everything. [all cheer] - Hey, wait for me. Oof! - [glass breaks] [sighs] [ Chic: Le Freak] Hit it! Move 'em on! Head 'em up! Head 'em up, move 'em on! Head 'em up! Rawhide! Move 'em on! Head 'em up! Move 'em on! Move 'em on! Head 'em up! Rawhide! Ride 'em up! Move 'em on! Head 'em up! Move 'em on! Rawhide! Knock 'em out! Pound 'em dead! Make 'em tea! Buy 'em drinks! Meet their mamas! Milk 'em hard! Rawhide! Yee-haw! - [Donkey] Are we there yet? - [Shrek] No. - [Donkey] Are we there yet? - [Fiona] Not yet. - [Donkey] OK, are we there yet? - [Fiona] No. - [Donkey] Are we there yet? - [Shrek] No! - [Donkey] Are we there yet? - [Shrek] Yes. - Really? - No! - Are we there yet? - [Fiona] No! - Are we there yet? - [Shrek] We are not! - Are we there yet? - [Shrek & Fiona] No! - Are we there yet? - [Shrek mimics] - That's not funny. That's really immature. - [Shrek mimics] - This is why nobody likes ogres. - [Shrek mimics] - Your loss! - [Shrek mimics] - I'm gonna just stop talking. - Finally! This is taking forever, Shrek. There's no in-flight movie or nothing! The Kingdom of Far, Far Away, Donkey. That's where we're going. Far, far... [softly] away! All right, all right, I get it. I'm just so darn bored. Well, find a way to entertain yourself. [sighs] [deep sigh] [clicks tongue] [popping] - [popping] - [exasperated sigh] For five minutes... Could you not be yourself... [shouts]... for five minutes! - [popping] - [shrieks] Are we there yet? - [chuckles] Yes! - Oh, finally! [fanfare] [ Lipps, Inc: Funkytown] Wow! It's going to be champagne wishes and caviar dreams from now on. Hey, good-looking! We'll be back to pick you up later! Gotta make a move to a town that's right for me We are definitely not in the swamp anymore. [whistle] Halt! Well, I talk about it, talk about it, talk about it, talk about it Hey, everyone, look. Talk about, talk about movin'... Hey, ladies! Nice day for a parade, huh? You working that hat. [Donkey] Swimming pools! Movie stars! [cheering] [applause] [fanfare] Announcing the long-awaited return of the beautiful Princess Fiona and her new husband. Well, this is it. - This is it. - This is it. This is it. [fanfare] [fanfare and cheering stop] [gasps] [tweeting] [baby wails] Uh... why don't you guys go ahead? I'll park the car. [chuckles] So... you still think this was a good idea? Of course! Look. Mom and Dad look happy to see us. - [softly] Who on earth are they? - [softly] I think that's our little girl. That's not little! That's a really big problem. Wasn't she supposed to kiss Prince Charming and break the spell? Well, he's no Prince Charming, but they do look... [softly] Happy now? We came. We saw them. Now let's go before they light the torches. - They're my parents. - Hello? They locked you in a tower. That was for my own... Good! Here's our chance. Let's go back inside and pretend we're not home. Harold, we have to be... Quick! While they're not looking we can make a run for it. Shrek, stop it! Everything's gonna be... A disaster! There is no way... - You can do this. - I really... - Really... - don't... want... to... be... Here! Mom... Dad... I'd like you to meet my husband... Shrek. Well, um... It's easy to see where Fiona gets her good looks from. [chuckles nervously] [gulps] [belches] - Excuse me. - [Shrek & Fiona laugh] Better out than in, I always say, eh, Fiona? [both giggle] [Shrek] That's good. I guess not. What do you mean, "not on the list"? Don't tell me you don't know who I am. What do you mean, "not on the list"? Don't tell me you don't know who I am. What's happening, everybody? Thanks for waiting. - I had the hardest time finding this place. - No! No! Bad donkey! Bad! Down! No, Dad! It's all right. It's all right. He's with us. - He helped rescue me from the dragon. - That's me: the noble steed. Waiter! How 'bout a bowl for the steed? Oh, boy. [slurps] - Um, Shrek? - Yeah? Oh, sorry! Great soup, Mrs Q. Mmm! No, no. Darling. [chuckles nervously] Oh! So, Fiona, tell us about where you live. Well... Shrek owns his own land. - Don't you, honey? - Oh, yes! It's in an enchanted forest abundant in squirrels and cute little duckies and... [laughing] What? I know you ain't talking about the swamp. An ogre from a swamp. Oh! How original. I suppose that would be a fine place to raise the children. - [splutters] - [chokes] It's a bit early to be thinking about that, isn't it? - Indeed. I just started eating. - Harold! - What's that supposed to mean? - Dad. It's great, OK? - For his type, yes. - My type? I got to go to the bathroom. - Dinner is served! - Never mind. I can hold it. Bon appetit! Oh, Mexican food! My favorite. Let's not sit here with our tummies rumbling. Everybody dig in. Don't mind if I do, Lillian. I suppose any grandchildren I could expect from you would be... Ogres, yes! Not that there's anything wrong with that. Right, Harold? Oh, no! No! Of course, not! That is, assuming you don't eat your own young! Dad! No, we usually prefer the ones who've been locked away in a tower! - Shrek, please! - I only did that because I love her. Aye, day care or dragon-guarded castle. You wouldn't understand. You're not her father! It's so nice to have the family together for dinner. - Harold! - Shrek! - Fiona! - Fiona! - Mom! - Harold... Donkey! [glissando] Your fallen tears have called to me So, here comes my sweet remedy I know what every princess needs For her to live life happily... [both gasp] Oh, my dear. Oh, look at you. You're all grown up. - Who are you? - Oh, sweet pea! I'm your fairy godmother. - I have a fairy godmother? - Shush, shush. Now, don't worry. I'm here to make it all better. With just a... Wave of my magic wand Your troubles will soon be gone With a flick of the wrist and just a flash You'll land a prince with a ton of cash A high-priced dress made by mice no less Some crystal glass pumps And no more stress Your worries will vanish, your soul will cleanse Confide in your very own furniture friends We'll help you set a new fashion trend - I'll make you fancy, I'll make you great - The kind of girl a prince would date! They'll write your name on the bathroom wall... "For a happy ever after, give Fiona a call!" A sporty carriage to ride in style, Sexy man boy chauffeur, Kyle Banish your blemishes, tooth decay, Cellulite thighs will fade away And oh, what the hey! Have a bichon frisé! ' Nip and tuck, here and there to land that prince with the perfect hair Lipstick liners, shadows blush To get that prince with the sexy tush Lucky day, hunk buffet You and your prince take a roll in the hay You can spoon on the moon With the prince to the tune Don't be drab, you'll be fab Your prince will have rock-hard abs Cheese soufflé, Valentine's Day Have some chicken fricassee! Nip and tuck, here and there To land that prince with the perfect hair Stop! [chuckles] Look... Thank you very much, Fairy Godmother, but I really don't need all this. [gasps and mutterings of disapproval] - Fine. Be that way. - We didn't like you, anyway. - [knocking] - [Shrek] Fiona? Fiona? [dog barks] Oh! You got a puppy? All I got in my room was shampoo. Oh, uh... Fairy Godmother, furniture... [giggles] I'd like you to meet my husband, Shrek. Your husband? What? What did you say? When did this happen? Shrek is the one who rescued me. - But that can't be right. - Oh, great, more relatives! She's just trying to help. Good! She can help us pack. Get your coat, dear. We're leaving. - What? - I don't want to leave. When did you decide this? - Shortly after arriving. - Look, I'm sorry... No, that's all right. I need to go, anyway. But remember, dear. If you should ever need me... happiness... is just a teardrop away. Thanks, but we've got all the happiness we need. Happy, happy, happy... [laughs] So I see. Let's go, Kyle. - Very nice, Shrek. - What? I told you coming here was a bad idea. You could've at least tried to get along with my father. I don't think I was going to get Daddy's blessing, even if I did want it. Do you think it might be nice if somebody asked me what I wanted? Sure. Do you want me to pack for you? You're unbelievable! You're behaving like a... - Go on! Say it! - Like an ogre! Here's a news flash for you! Whether your parents like it or not... I am an ogre! - [yelps] - [roars] And guess what, Princess? That's not about to change. I've made changes for you, Shrek. Think about that. That's real smooth, Shrek. I'm an ogre! [mimics Shrek roaring] [sniffling] I knew this would happen. [Lillian] You should. You started it. I can hardly believe that, Lillian. He's the ogre. Not me. I think, Harold, you're taking this a little too personally. This is Fiona's choice. But she was supposed to choose the prince we picked for her. I mean, you expect me to give my blessings to this... thing? Fiona does. And she'll never forgive you if you don't. I don't want to lose our daughter again, Harold. Oh, you act as if love is totally predictable. Don't you remember when we were young? We used to walk down by the lily pond and... - they were in bloom... - Our first kiss. It's not the same! I don't think you realize that our daughter has married a monster! Oh, stop being such a drama king. Fine! Pretend there's nothing wrong! La, di, da, di, da! Isn't it all wonderful! I'd like to know how it could get any worse! - Hello, Harold. - [gasps] - What happened? - Nothing, dear! Just the old crusade wound playing up a bit! [chuckles] I'll just stretch it out here for a while. You better get in. We need to talk. Actually, Fairy Godmother, off to bed. [yawns] Already taken my pills, and they tend to make me a bit drowsy. So, how about... we make this a quick visit. What? Oh, hello. Ha-ha-ha! So, what's new? You remember my son, Prince Charming? Is that you? My gosh! It's been years. When did you get back? Oh, about five minutes ago, actually. After I endured blistering winds, scorching desert... I climbed to the highest room in the tallest tower... Mommy can handle this. He endures blistering winds and scorching desert! He climbs to the highest bloody room of the tallest bloody tower... And what does he find? Some gender-confused wolf telling him that his princess is already married. It wasn't my fault. He didn't get there in time. Stop the car! [crash] Harold. You force me to do something I really don't want to do. [gasps] Where are we? Hi. Welcome to Friar's Fat Boy! May I take your order? My diet is ruined! I hope you're happy. Er... okay. Two Renaissance Wraps, no mayo... chili rings... - I'll have the Medieval Meal. - One Medieval Meal and, Harold... - Curly fries? - No, thank you. - Sourdough soft taco, then? - No, really, I'm fine. Your order, Fairy Godmother. This comes with the Medieval Meal. There you are, dear. We made a deal, Harold, and I assume you don't want me to go back on my part. [sighs deeply] Indeed not. So, Fiona and Charming will be together. - Yes. - Believe me, Harold. It's what's best. Not only for your daughter... but for your Kingdom. What am I supposed to do about it? Use your imagination. [whooshing] [whinnies] Oh... Come on in, Your Majesty. [piano plays, people talk] I like my town With a little drop of poison Nobody knows... [barman belches] [clears throat] Excuse me. Do I know you? No, you must be mistaking me for someone else. Uh... excuse me. I'm looking for the Ugly Stepsister. Ah! There you are. Right. You see, I need to have someone taken care of. - Who's the guy? - Well, he's not a guy, per se. Um... He's an ogre. [crowd gasp] Hey, buddy, let me clue you in. There's only one fellow who can handle a job like that, and, frankly... he don't like to be disturbed. he don't like to be disturbed. Where could I find him? [knock on door] Hello? Who dares enter my room? Sorry! I hope I'm not interrupting, but I'm told you're the one to talk to about an ogre problem? You are told correct. But for this, I charge a great deal of money. Would... this be enough? You have engaged my valuable services, Your Majesty. Just tell me where I can find this ogre. [ Eels: I Need Some Sleep] [snoring] [chimes] Everyone says I'm getting down too low Everyone says you've just gotta let it go You just gotta let it go I need some sleep Time to put the old horse down I'm in too deep And the wheels keep spinning round Everyone says you've just gotta let it go Everyone says you've just gotta let it go Dear Knight, I pray that you take this favor as a token of my gratitude. [plays tune] Dear Diary... Sleeping Beauty is having a slumber party tomorrow, but Dad says I can't go. He never lets me out after sunset. Dad says I'm going away for a while. Must be like some finishing school. Mom says that when I'm old enough, my Prince Charming will rescue me from my tower and bring me back to my family, and we'll all live happily ever after. Mrs. Fiona Charming. Mrs. Fiona Charming. Mrs. Fiona Charming. [echoing] Mrs. Fiona Charming. [knock on door] Sorry. I hope I'm not interrupting anything. No, no. I was just reading a, uh... a scary book. I was hoping you'd let me apologize for my despicable behavior earlier. - Okay... - I don't know what came over me. Do you suppose we could pretend it never happened and start over... - Look, Your Majesty, I just... - Please. Call me Dad. Dad. We both acted like ogres. Maybe we just need some time to get to know each other. Excellent idea! I was actually hoping you might join me for a morning hunt. A little father-son time? I know it would mean the world to Fiona. [sighs] Shall we say, : by the old oak? [birds twitter] [Shrek] Face it, Donkey! We're lost. We can't be lost. We followed the King's instructions exactly. "Head to the darkest part of the woods..." "Past the sinister trees with scary-looking branches." - The bush shaped like Shirley Bassey! - We passed that three times already! You were the one who said not to stop for directions. Oh, great. My one chance to fix things up with Fiona's dad and I end up lost in the woods with you! Don't get huffy! I'm only trying to help. I know! I know. - I'm sorry, all right? - Hey, don't worry about it. I just really need to make things work with this guy. Yeah, sure. Now let's go bond with Daddy. [purring] [purring] Well, well, well, Donkey. I know it was kind of a tender moment back there, but the purring? What? I ain't purring. Sure. What's next? A hug? Hey, Shrek. Donkeys don't purr. What do you think I am, some kind of a... Ha-ha! Fear me, if you dare! [hisses] Look! A little cat. - Look out, Shrek! He got a piece! - It's a cat, Donkey. Come here, little kitty, kitty. Come on, little kitty. Come here. Oh! Come here, little kitty. - [screaming] - Whoa! - Hold on, Shrek! I'm coming! - Come on! Get it off! Get it off! Oh, God. Oh... No! - Look out, Shrek! Hold still! - Get it off! Shrek! Hold still! - Did I miss? - No. You got them. Now, ye ogre, pray for mercy from... Puss... in Boots! I'll kill that cat! Ah-ha-ha! [coughs] [wheezes] [retches] [coughs] - [chuckles] Hairball. - Oh! That is nasty! What should we do with him? Take the sword and neuter him. Give him the Bob Barker treatment. Oh, no! Por favor! Please! I implore you! It was nothing personal, Señor. I was doing it only for my family. My mother, she is sick. And my father lives off the garbage! The King offered me much in gold and I have a litter of brothers... Whoa, whoa, whoa! Fiona's father paid you to do this? The rich King? Sí. [screams] Well, so much for Dad's royal blessing. Don't feel bad. Almost everybody that meets you wants to kill you. Gee, thanks. Maybe Fiona would've been better off if I were some sort of Prince Charming. That's what the King said. Oh, uh... sorry. I thought that question was directed at me. Shrek, Fiona knows you'd do anything for her. Well, it's not like I wouldn't change if I could. I just... I just wish I could make her happy. Hold the phone... Happiness. A tear drop away. Donkey! Think of the saddest thing that's ever happened to you! Aw, man, where do I begin? First there was the time that old farmer tried to sell me for some magic beans. Then this fool had a party and he have the guests trying to pin the tail on me. Then they got drunk and start beating me with a stick, going "Piñata!!" What is a piñata, anyway? No, Donkey! I need you to cry! Don't go projecting on me. I know you're feeling bad, but you got to... Aaaahhh! You little, hairy, litter-licking sack of... What? Is it on? Is it on? [clears throat] This is Fairy Godmother. I'm either away from my desk or with a client. But if you come by the office, we'll be glad to make you an appointment. Have a "happy ever after." Oh... Are you up for a little quest, Donkey? That's more like it! Shrek and Donkey, on another whirlwind adventure! Ain't no stoppin' us now! Whoo! We're on the move! - Stop, Ogre! I have misjudged you. - Join the club. We've got jackets. On my honor, I am obliged to accompany you until I have saved your life as you have spared me mine. The position of annoying talking animal has already been taken. Let's go, Shrek. Shrek? - Shrek! - Aw, come on, Donkey. Look at him... in his wee little boots. You know, how many cats can wear boots? Honestly. - Let's keep him! - Say what? [purrs] Ahh! Listen. He's purring! - Oh, so now it's cute. - Come on, Donkey. Lighten up. Lighten up? I should lighten up? Look who's telling who to lighten up! Lighten up? I should lighten up? Look who's telling who to lighten up! [giggles] Shrek! [barks] [barks] Shrek? They're both festive, aren't they? What do you think, Harold? Um... Yes, yes. Fine. Fine. [sighs] Try to at least pretend you're interested in your daughter's wedding ball. Honestly, Lillian, I don't think it matters. How do we know there will even be a ball? Mom. Dad. - Oh, hello, dear. - What's that, Cedric? Right! Coming. Mom, have you seen Shrek? I haven't. You should ask your father. Be sure and use small words, dear. He's a little slow this morning. - Can I help you, Your Majesty? - Ah, yes! Um... Mmm! Exquisite. What do you call this dish? That would be the dog's breakfast, Your Majesty. Ah, yes. Very good, then. Carry on, Cedric. - Dad? Dad, have you seen Shrek? - No, I haven't, dear. I'm sure he just went off to look for a nice... mud hole to cool down in. You know, after your little spat last night. Oh. You heard that, huh? The whole kingdom heard you. I mean, after all, it is in his nature to be... well, a bit of a brute. Him? You know, you didn't exactly roll out the Welcome Wagon. Well, what did you expect? Look at what he's done to you. Shrek loves me for who I am. I would think you'd be happy for me. Darling, I'm just thinking about what's best for you. Maybe you should do the same. [both whisper] No, really? [both laugh] [Shrek] Shh... Oh... [hooter blasts] Oh, no. That's the old Keebler's place. Let's back away slowly. That's the Fairy Godmother's cottage. She's the largest producer of hexes and potions in the whole kingdom. Then why don't we pop in there for a spell? Ha-ha! Spell! [Puss in Boots shrieks with laughter] [Puss in Boots] He makes me laugh. Hi. I'm here to see the... The Fairy Godmother. I'm sorry. She is not in. Jerome! Coffee and a Monte Cristo. Now! [sighs] Yes, Fairy Godmother. Right away. Look, she's not seeing any clients today, OK? That's OK, buddy. We're from the union. The union? We represent the workers in all magical industries, both evil and benign. Oh! Oh, right. Are you feeling at all degraded or oppressed? Uh... a little. We don't even have dental. They don't even have dental. Okay, we'll just have a look around. Oh. By the way. I think it'd be better if the Fairy Godmother didn't know we were here. - Know what I'm saying? Huh? - Huh? Huh? Huh? - Stop it. - Of course. Go right in. [voices and grinding machines] [explosion] A drop of desire. [giggles] Naughty! A pinch of passion. [laughs] And just a hint of... lust! [laughs] - [Shrek] Excuse me. - [gasps] Sorry to barge in like this... What in Grimm's name are you doing here? Well, it seems that Fiona's not exactly happy. Oh-ho-ho! And there's some question as to why that is? Well, let's explore that, shall we? Ah. P, P, P... Princess. Cinderella. Here we are. Lived happily ever after. Oh... [laughs] No ogres! Let's see. Snow White. A handsome prince. Oh, no ogres. Sleeping Beauty. Oh, no ogres! Hansel and Gretel? No! Thumbelina? No. The Golden Bird, the Little Mermaid, Pretty Woman... No, no, no, no, no! You see, ogres don't live happily ever after. All right, look, lady! Don't you point... those dirty green sausages at me! Your Monte Cristo and coffee. Oh! Sorry. Ah... that's okay. We were just leaving. Very sorry to have wasted your time, Miss Godmother. Just... go. Come on, guys. [whistles tune] TGIF, eh, buddy? Working hard or hardly working, eh, Mac? Get your fine Corinthian footwear and your cat cheeks out of my face! Man, that stinks! You don't exactly smell like a basket of roses. - Well, one of these has got to help. - I was just concocting this very plan! Already our minds are becoming one. Whoa, whoa. If we need an expert on licking ourselves, we'll give you a call. Shrek, this is a bad idea. Look. Make yourself useful and go keep watch. Puss, do you think you could get to those on top? No problema, boss. In one of my nine lives, I was the great cat burglar of Santiago de Compostela. Ha-ha-ha-ha! Shrek, are you off your nut? Donkey, keep watch. Keep watch? Yeah, I'll keep watch. I'll watch that wicked witch come and whammy a world of hurt up your backside. I'll laugh, too. I'll be giggling to myself. - What do you see? - Toad Stool Softener? I'm sure a nice BM is the perfect solution for marital problems. - Elfa Seltzer? - Uh-uh. - Hex Lax? - No! Try "handsome." Sorry. No handsome. Hey! How about "Happily Ever After"? Well, what does it do? It says "Beauty Divine." In some cultures, donkeys are revered as the wisest of creatures. Especially us talking ones. [gasps] Donkey! That'll have to do. We've got company. Can we get on with this? Hurry! Nice catch, Donkey! Finally! A good use for your mouth. [ Pete Yorn: Ever Fallen In Love] Come on! You spurn my natural emotions You make me feel like dirt and I'm hurt And if I start a commotion I run the risk of losing you and that's worse Ever fallen in love with someone, ever fallen in love In love with someone, ever fallen in love In love with someone you shouldn't have fallen in love with Ever fallen in love with someone, ever fallen in love In love with someone, ever fallen in love With someone you shouldn't have fallen in love with Fallen in love with Ever fallen in love with someone you shouldn't have fallen in love with I don't care whose fault it is. Just get this place cleaned up! And somebody bring me something deep fried and smothered in chocolate! - Mother! - Charming. Sweetheart. This isn't a good time, pumpkin. Mama's working. Whoa, what happened here? - The ogre, that's what! - What? Where is he, Mom? I shall rend his head from his shoulders! I will smite him where he stands! He will rue the very day he stole my kingdom from me! Oh, put it away, Junior! You're still going to be king. We'll just have to come up with something smarter. Pardon. Um... Everything is accounted for, Fairy Godmother, except for one potion. What? Oh... I do believe we can make this work to our advantage. "Happily Ever After Potion. Maximum strength. For you and your true love." "If one of you drinks this, you both will be fine. Happiness, comfort" and beauty divine." - You both will be fine? - I guess it means it'll affect Fiona, too. Hey, man, this don't feel right. My donkey senses are tingling all over. Drop that jug o' voodoo and let's get out of here. It says, "Beauty Divine." How bad can it be? [sneezes] See, you're allergic to that stuff. You'll have a reaction. And if you think that I'll be smearing Vapor Rub over your chest, think again! Boss, just in case there is something wrong with the potion... allow me to take the first sip. It would be an honor to lay my life on the line for you. Oh, no, no. I don't think so. If there'll be any animal testing, I'll do it. That's the best friend's job. Now give me that bottle. How do you feel? I don't feel any different. I look any different? You still look like an ass to me. Maybe it doesn't work on donkeys. - Well, here's to us, Fiona. - Shrek? - You drink that, there's no going back. - I know. - No more wallowing in the mud? - I know. - No more itchy butt crack? - I know! - But you love being an ogre! - I know! But I love Fiona more. Shrek, no! Wait! [gurgling] [farts] Got to be... I think you grabbed the "Farty Ever After" potion. Maybe it's a dud. Or maybe Fiona and I were never meant to be. Or maybe Fiona and I were never meant to be. [thunder rumbles] Uh-oh. What did I tell you? I feel something coming on. I don't want to die. I don't want to die. I don't want to die! Oh, sweet sister, mother of mercy. I'm melting! I'm melting! It's just the rain, Donkey. [chuckles] Oh. Don't worry. Things seem bad because it's dark and rainy and Fiona's father hired a sleazy hitman to whack you. [hisses] lt'll be better in the morning. You'll see... The sun'll come out... Tomorrow [yawns] Bet your bottom... Bet my bottom? I'm coming, Elizabeth! Donkey? Are you all right? - Hey, boss. Let's shave him. - D-Donkey? [groans] [Puss In Boots shrieks] There you are! We missed you at dinner. What is it, darling? Dad... I've been thinking about what you said. And I'm going to set things right. Ah! Excellent! That's my girl. It was a mistake to bring Shrek here. I'm going to go out and find him. And then we'll go back to the swamp where we belong. [Lillian] Fiona, please! Let's not be rash, darling. You can't go anywhere right now. [rain patters] [Both] Fiona! Look, I told you he was here. Look at him! Quiet. Look at him. [Shrek groans] Good morning, sleepyhead. [Shrek shouts] [All] Good morning! We love your kitty! - [Shrek] Oh... My head... - Here, I fetched a pail of water. Thanks. Uhh! Aahh! Oh... A cute button nose? Thick, wavy locks? Taut, round buttocks? I'm... I'm... - Gorgeous! - I'll say. I'm Jill. What's your name? - Um... Shrek. - Shrek? Wow. Are you from Europe? - You're tense. - I want to rub his shoulders. - I got it covered. - I don't have anything to rub. Get in line. Get in line. - Have you seen my donkey? - Who are you calling donkey? - Donkey? You're a... - A stallion, baby! I can whinny. [whinnies] I can count. Look at me, Shrek! I'm trotting! That's some quality potion. What's in that stuff? "Oh, don't take the potion, Mr. Boss, it's very bad." Pah! "Warning: Side effects may include burning, itching, oozing, weeping. Not intended for heart patients" or those with... nervous disorders." I'm trotting, I'm trotting in place! Yeah! What? Señor? "To make the effects of this potion permanent, "the drinker must obtain his true love's kiss by midnight." Midnight? Why is it always midnight? - Pick me! I'll be your true love! - I'll be your true love. I'll be true... enough. Look, ladies, I already have a true love. [all] Oh... And take it from me, Boss. You are going to have one satisfied Princess. And let's face it. You are a lot easier on the eyes. Inside you're the same old mean, salty... - Easy. ...cantankerous, foul, angry ogre you always been. And you're still the same annoying donkey. - Yeah. - [sighs] Well... Look out, Princess. Here comes the new me. First things first. - We need to get you out of those clothes. - [all gasp] - Ready? - Ready! - [Donkey screams] - Driver, stop! Oh, God! Help me, please! My racing days are over! I'm blind! Tell the truth. Will I ever play the violin again? You poor creature! Is there anything I can do for you? Well, I guess there is one thing. Take off the powdered wig and step away from your drawers. - Not bad. - Not bad at all. [both laugh] Father? Is everything all right, Father? Thank you, gentlemen! Someday, I will repay you. Unless, of course, I can't find you or if I forget. - [whinnies] - [Puss in Boots, in angry Spanish] [ Butterfly Boocher: Changes] [ Butterfly Boocher: Changes] Oh, yeah Turn and face the strange Ch-Ch-Changes Don't wanna be a richer one Ch-Ch-Ch-Ch-Changes Turn and face the strange Ch-Ch-Changes Just gonna have to be a different man Time may change me But I can't trace time Halt! Tell Princess Fiona her husband, Sir Shrek, is here to see her. Still don't know what I was looking for And my time was running wild, a million dead-end streets Every time I thought I'd got it made It seemed the taste was not so sweet - [screams] - Ch-Ch-Ch-Ch-Changes Turn and face the strange - Shrek? - Ch-Ch-Changes Don't wanna be a richer one Time may change me But I can't trace time Fiona? Hello, handsome. Shrek! - Princess! - Donkey? Wow! That potion worked on you, too? What potion? Shrek and I took some magic potion. And well... Now, we're sexy! Shrek? [purrs] For you, baby... I could be. - Yeah, you wish. - Donkey, where is Shrek? He went inside looking for you. Shrek? Fiona! Fiona! You want to dance, pretty boy? Are you going so soon? Don't you want to see your wife? Fiona? Shrek? Aye, Fiona. It is me. What happened to your voice? The potion changed a lot of things, Fiona. But not the way I feel about you. Fiona? - Charming? - Do you think so? [laughs] Dad. I was so hoping you'd approve. - Um... Who are you? - Mom, it's me, Shrek. I know you never get a second chance at a first impression, but, well, what do you think? [Shrek in distance] Fiona! Fiona! Fiona! - Fiona! - Fiona, Fiona! Ho-ho-ho! Oh, shoot! I don't think they can hear us, pigeon. [sighs deeply] Don't you think you've already messed her life up enough? I just wanted her to be happy. And now she can be. Oh, sweetheart. She's finally found the prince of her dreams. But look at me. Look what I've done for her. It's time you stop living in a fairy tale, Shrek. She's a princess, and you're an ogre. That's something no amount of potion will ever change. But... I love her. If you really love her... you'll let her go. [ Nick Cave: People Ain't No Good] [ Nick Cave: People Ain't No Good] Shrek? Señor. What's going on? Where are you going? You wouldn't have had anything to do with this, would you, Harold? People just ain't no good I think that's well understood There you go, boys. Just leave the bottle, Doris. Hey. Why the long face? It was all just a stupid mistake. I never should have rescued her from that tower in the first place. I hate Mondays. I can't believe you'd walk away from the best thing that happened to you. What choice do I have? She loves that pretty boy, Prince Charming. Come on. Is he really that good-looking? Are you kidding? He's gorgeous! He has a face that looks like it was carved by angels. - Oh. He sounds dreamy. - You know... shockingly, this isn't making me feel any better. Look, guys. It's for the best. Mom and Dad approve, and Fiona gets the man she's always dreamed of. Everybody wins. Except for you. I don't get it, Shrek. You love Fiona. Aye. And that's why I have to let her go. Excuse me, is she here? She's, uh... in the back. Oh, hello again. Fairy Godmother. Charming. You'd better have a good reason for dragging us down here, Harold. Well, I'm afraid Fiona isn't really... warming up to Prince Charming. - FYI, not my fault. - No, of course it's not, dear. I mean, how charming can I be when I have to pretend I'm that dreadful ogre? No, no, it's nobody's fault. Perhaps it's best if we just call the whole thing off, okay? - [both] What? - You can't force someone to fall in love! I beg to differ. I do it all the time! Have Fiona drink this and she'll fall in love with the first man she kisses, which will be Charming. - Umm... no. - What did you say? I can't. I won't do it. Oh, yes, you will. If you remember, I helped you with your happily ever after. And I can take it away just as easily. Is that what you want? Is it? - No. - Good boy. Now, we have to go. I need to do Charming's hair before the ball. He's hopeless. He's all high in the front. He can never get to the back. You need someone to do the back. Oh. Thank you, Mother. [Donkey] Mother? Um... Mary! A talking horse! The ogre! Stop them! Thieves! Bandits! Stop them! (Announcer) The abs are fab and it's gluteus to the maximus here at tonight's Far, Far Away Royal Ball blowout! The coaches are lined up as the cream of the crop pours out of them like Miss Muffet's curds and whey. Everyone who's anyone has turned out to honor Princess Fiona and Prince Shrek. And, oh my, the outfits look gorgeous! Look! Hansel and Gretel! What the heck are the crumbs for? And right behind them, Tom Thumb and Thumbelina! - Oh, aren't they adorable! - [screaming] [woman] Here comes Sleeping Beauty! Tired old thing. Who's this? Who's this? Who is this? Oh. It's the one, it's the only... It's the Fairy Godmother! Hello, Far, Far Away! Can I get a whoop whoop? May all your endings be happy and... Well, you know the rest! We'll be right back with the Royal Far, Far Away Ball after these messages. I hate these ball shows. They bore me to tears. Flip over to Wheel Of Torture! I'm not flipping anywhere, sir, until I see Shrek and Fiona. Whizzes on you guys. Hey, mice, pass me a buffalo wing! No, to your left. Your left! - Tonight on "Knights"... - Now here's a good show! We got a white bronco heading east into the forest. Requesting backup. It's time to teach these madcap mammals their "devil may mare" attitudes just won't fly. Why you grabbing me? Police brutality! I have to talk to Princess Fiona! - We warned you! - Ow! Ow! Did someone let the cat out of the bag? You capitalist pig dogs! [shrieks] - Catnip! - That's not mine. Find Princess Fiona! I'm a donkey! Tell her Shrek... I'm her husband, Shrek! Quick! Rewind it! I'm her husband, Shrek! Ow! [knock on door] Darling? Ah. I thought I might find you here. How about a nice hot cup of tea before the ball? I'm not going. The whole Kingdom's turned out to celebrate your marriage. There's just one problem. That's not my husband. I mean, look at him. Yes, he is a bit different, but people change for the ones they love. You'd be surprised how much I changed for your mother. Change? He's completely lost his mind! Why not come down to the ball and give him another chance? You might find you like this new Shrek. But it's the old one I fell in love with, Dad. I'd give anything to have him back. Darling. That's mine. Decaf. Otherwise I'm up all night. Thanks. I got to get out of here! I got to get out of here! You can't lock us up like this! Let me go! What about my Miranda rights? You're supposed to say I have the right to remain silent. Nobody said I have the right to remain silent! You have the right to remain silent. What you lack is the capacity. I must hold on before I, too, go totally mad. Shrek? Donkey? Too late. Gingy! Pinocchio! Get us out of here! Oh... [ Theme from Mission Impossible] Fire in ze hole! [explosion, rumbling] Look out below! Quick! Tell a lie! - What should I say? - Anything, but quick! Say something crazy like I'm wearing ladies' underwear! I am wearing ladies' underwear. - Are you? - I most certainly am not! It looks like you most certainly am are! - I am not! - What kind? - It's a thong! - Oww! They're briefs! - Are not. - Are too! - Are not! - Are too! Here we go. Hang tight. [Donkey] Wait, wait, wait! Ow! Ow! Hey, hey, hey! Ow! - Excuse me? - What? Puss! Pardon me, would you mind letting me go? - Sorry, boss. - Quit messing around! We've got to stop that kiss! I thought you was going to let her go. I was, but I can't let them do this to Fiona. Boom! That's what I like to hear. Look who's coming around! It's impossible! We'll never get in. The castle's guarded. There's a moat and everything! Folks, it looks like we're up chocolate creek without a Popsicle stick. - What? - Do you still know the Muffin Man? Well, sure! He's down on Drury Lane. Why? Because we're gonna need flour. Lots and lots of flour. Gingy! Fire up the ovens, Muffin Man! We've got a big order to fill! [evil chuckle] [Gingy] It's alive! [rattling] [gasping] [whinnies] Run, run, run, as fast you can! [screaming] Go, baby, go! There it is, Mongo! To the castle! [Shrek] No, you great stupid pastry! Come on! [all shout] [Donkey] Mongo! Down here! Look at the pony! That's right! Follow the pretty pony! Pretty pony wants to play at the castle! [Mongo] Pretty pony. Ladies and gentlemen. Presenting Princess Fiona and her new husband, Prince Shrek. [applause, cheering] Shrek, what are you doing? I'm just playing the part, Fiona. Is that glitter on your lips? Mm. Cherry flavored. Want to taste? - Ugh! What is with you? - But, Muffin Cake... [piano plays] C Minor, put it in C Minor. Ladies and gentlemen. [applause, cheering] I'd like to dedicate this song to... Princess Fiona and Prince Shrek. Fiona, my Princess. Will you honor me with a dance? Where have all the good men gone And where are all the gods? [all chant] Dance! Where's the streetwise Hercules To fight the rising odds? Since when do you dance? Fiona, my dearest, if there's one thing I know, it's that love is full of surprises. Late at night I toss and I turn And I dream of what I need Hit it! I need a hero All right, big fella! Let's crash this party! Man the catapults! Aim! Fire! - Brace yourselves! - Ooh! Purty! [groaning] Not the gumdrop button! [enraged howling] Incoming! Ha-ha! All right! Somewhere after midnight In my wildest fantasy Go, Mongo! Go! Man the cauldrons! After you, Mongo. - That's it! Heave-ho! - Watch out! Shrek! More heat, less foam! Up where the mountains Meet the heavens above Out where the lightning Splits the sea I could swear there is someone Somewhere watching me Heave! Ho! [Gingy, slow-motion] No...! [Mongo groans] [whistles] Come on! [cheering] Look out! - Be good. - [weeping bitterly] [sobbing] He needs me! Let me go! Donkey! Puss! Go! Go! Your lady needs you! Go! Today, I repay my debt. [all] Aww... [growling] On guard! He's gotta be strong And he's gotta be fast And he's gotta be fresh From the fight - I need a hero - Stop! [Donkey whinnies] - Hey, you! Back away from my wife. - Shrek? You couldn't just go back to your swamp and leave well enough alone. - Now! - Pigs und blanket! Pinocchio! Get the wand! I see London! I see France! Whah! I'm a real boy! Ah! Ah! Aaahhh! Catch! Donkey! Oh! I'm a real boy. Aah! Oh! - Ha! - Ah. That's mine! Pray for mercy, from Puss... And Donkey! She's taken the potion! Kiss her now! No! - Hi-ya! - [crowd gasp] - Fiona. - Shrek. Harold! You were supposed to give her the potion! Well, I guess I gave her the wrong tea. - [Charming] Mommy! - Mommy? [growls] I told you. Ogres don't live happily ever after. [screams] Woo! Ha! [breathes deeply] [gasping] Oh, Dad! [sobbing] - Is he...? - Yup. [croaking] He croaked. Harold? Dad? I'd hoped you'd never see me like this. - And he gave you a hard time! - Donkey! No, no, he's right. I'm sorry. To both of you. I only wanted what was best for Fiona. But I can see now... she already has it. Shrek, Fiona... Will you accept an old frog's apologies... and my blessing? Harold? I'm sorry, Lillian. I just wish I could be the man you deserve. You're more that man today than you ever were... warts and all. [ribbits] [clock chimes] [clock chimes] Boss! The Happily Ever After Potion! Midnight! Fiona. Is this what you want? To be this way forever? - What? - Because if you kiss me now... we can stay like this. You'd do that? - For me? - Yes. I want what any princess wants. To live happily ever after... with the ogre I married. Whatever happens, I must not cry! You cannot make me cry! [sobbing] [clock chimes] Whoa! No. No, no. Aaah! Ow. Oh, no. [sighs] [laughs] Hey. You still look like a noble steed to me. [giggles] Now, where were we? Oh. I remember. [giggling] [applause] Hey! Isn't we supposed to be having a fiesta? Uno, dos, quatro, hit it! [ Eddie Murphy/Antonio Banderas: Livin' La Vida Loca] [ Eddie Murphy/Antonio Banderas: Livin' La Vida Loca] Puss and Donkey, y'all... She's into superstitions Black cats and voodoo dolls - Sing it, Puss! - I feel a premonition That girl's gonna make me fall Here we go! She's into new sensations New kicks in the candlelight She's got a new addiction For every day and night She'll make you take your clothes off And go dancing in the rain She'll make you live her crazy life But she'll take away your pain Like a bullet to your brain Upside inside out Living la vida loca Hey gorgeous! Living la vida loca Her lips are devil red And her skin's the color of mocha She will wear you out - Living la vida loca - [Donkey] She livin' it loca! Living la vida loca - [Donkey] Say it one more time now! - Living the vida loca [Puss in Boots jamming] [Puss in Boots] Hey, Donkey, that's Spanish! She'll push and pull you down Living la vida loca She will wear you out Living la vida loca Living la vida loca She'll push and pull you down Living the vida loca Her lips are devil red And her skin's the color of mocha She will wear you out Living la vida loca Living la vida loca Living la vida loca Living la vida loca All by myself All by myself Don't wanna be All by myself anymore... Amigo, we are off to the Kit-Kat Club. Come on, join us. Thanks, compadre. I'm... I'm not in the mood. We will cheer you up! Find you a nice burro! [shrieking] Hey, baby! Hey, that's my girl! Yeah! All right! Baby, where you been? - [cries] - I'm sorry, too. I should've stayed. But Shrek had this thing he had to do. What? Say it one more time. What you talking about? Are you serious? - [cooing] - [gasping] - Papa! - [screaming] - [cooing, squealing] - [chuckling] Look at our little mutant babies! [Donkey] I got to get a job. [Donkey] I got to get a job.

---
## [MemeHoovy/FNF-Plasma-Engine](https://github.com/MemeHoovy/FNF-Plasma-Engine)@[998c3be3c7...](https://github.com/MemeHoovy/FNF-Plasma-Engine/commit/998c3be3c7ba5282216205f17377bf02a8d57ccc)
#### Wednesday 2022-10-05 04:41:03 by swordcube

using yoshi crafter flixel lib now, it's so much fucking faster holy shit

---
## [y124/y124.github.io](https://github.com/y124/y124.github.io)@[d54b6835fd...](https://github.com/y124/y124.github.io/commit/d54b6835fdf08638a1fe7eb6e7acff3f4591c766)
#### Wednesday 2022-10-05 05:46:02 by y124

Merge pull request #2 from dynamitegus/master

fuck your stupid tab key

---
## [cooljackal/pytorch](https://github.com/cooljackal/pytorch)@[afcc7c7f5c...](https://github.com/cooljackal/pytorch/commit/afcc7c7f5c7cef740241ff0abdae8d4f2ad22a03)
#### Wednesday 2022-10-05 06:17:51 by Andrew Gu

[FSDP] Generalize prefetching; lower unshard/reshard to handle (#83665)

### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`.

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading).

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.

### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)

  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)

  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>

Differential Revision: [D39293429](https://our.internmc.facebook.com/intern/diff/D39293429)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83665
Approved by: https://github.com/zhaojuanmao

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[91f02f2a6b...](https://github.com/necromanceranne/tgstation/commit/91f02f2a6b99c6eb5ae56fc3f7cfb903e703bc08)
#### Wednesday 2022-10-05 08:19:10 by John Willard

canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

---
## [masthowasli/symfony](https://github.com/masthowasli/symfony)@[338daf25c9...](https://github.com/masthowasli/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Wednesday 2022-10-05 09:56:50 by Nicolas Grekas

feature #46751 [VarExporter] Add trait to help implement lazy loading ghost objects (nicolas-grekas)

This PR was merged into the 6.2 branch.

Discussion
----------

[VarExporter] Add trait to help implement lazy loading ghost objects

| Q             | A
| ------------- | ---
| Branch?       | 6.2
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | -
| License       | MIT
| Doc PR        | -

This PR packages an implementation of [lazy loading ghost objects](https://www.martinfowler.com/eaaCatalog/lazyLoad.html) in a single `LazyGhostObjectTrait` (as a reminder, a lazy ghost object is an object that is created empty and that is able to initialize itself when being accessed for the first time.)

By using this trait, ppl can easily turn any existing classes into such ghost object implementations.

I target two use cases with this feature (but ppl are free to be more creative):
1. lazy proxy generation for service containers;
2. lazy proxy generation for entities.

In all cases, the generation itself is trivial using inheritance (sorry `final` classes.) For example, in order to turn a `Foo` class into a lazy ghost object, one just needs to do:
```php
class FooGhost extends Foo implements LazyGhostObjectInterface
{
    use LazyGhostObjectTrait;
}
```

And then, one can instantiate ghost objects like this:
```php
$fooGhost = FooGhost::createLazyGhostObject($initializer);
```

`$initializer` should be a closure that takes the ghost object instance as argument and initializes it. An initializer would typically call the constructor on the instance after resolving its dependencies:
```php
$initializer = function ($instance) use ($etc) {
    // [...] use $etc to compute the $deps
    $instance->__construct(...$deps);
};
```

Interface `LazyGhostObjectInterface` is optional to get the behavior of a ghost object but gives a contract that allows managing them when needed:
```php
    public function initializeLazyGhostObject(): void;
    public function resetLazyGhostObject(): bool;
```

Because initializers are *not* freed when initializing, it's possible to reset a ghost object to its uninitialized state. This comes with one limitation: resetting `readonly` properties is not allowed by the engine so these cannot be reset. The main target use case of this capability is Doctrine's EntityManager of course.

To work around the limitation with `readonly` properties, but also to allow creating partially initialized objects, `$initializer` can also accept two more arguments `$propertyName` and `$propertyScope`. When doing so, `$initializer` is going to be called on a property-by-property basis and is expected to return the computed value of the corresponding property.

Because lazy-initialization is *not* triggered when (un)setting a property, it's also possible to do partial initialization by calling setters on a just-created ghost object.

---

You might wonder why this PR is in the `VarExporter` component? The answer is that it reuses a lot of its existing code infrastructure. Exporting/hydrating/instantiating require using reflection a lot, and ghost objects too. We could consider renaming the component, but honestly, 1. I don't have a good name in mind; 2. changing the name of a component is costly for the community and 3. more importantly this doesn't really matter because this is all low-level stuff usually.

You might also wonder why this trait while we already have https://github.com/FriendsOfPHP/proxy-manager-lts and https://github.com/Ocramius/ProxyManager?

The reason is that the code infrastructure in ProxyManager is heavy. It comes with a dependency on https://github.com/laminas/laminas-code and it's complex to maintain. While I made the necessary changes to support PHP 8.1 in FriendsOfPHP/proxy-manager-lts (and submitted those changes [upstream](https://github.com/Ocramius/ProxyManager/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc+author%3Anicolas-grekas)), getting support for new PHP versions is slow and complex. Don't take me wrong, I don't blame maintainers, ProxyManager is complex for a reason.

But ghost objects are way simpler than other kind of proxies that ProxyManager can produce: a trait does the job. While the trait itself is no trivial logic, it's at least plain PHP code, compared to convoluted (but needed) code generation logic in ProxyManager.

If you need any other kind of proxies that ProxyManager supports, just use ProxyManager.

For Symfony, having a simple lazy ghost object implementation will allow services declared as lazy to be actually lazy out of the box (today, you need to install proxy-manager-bridge as an optional dependency.) \o/

Commits
-------

27b4325f78 [VarExporter] Add trait to help implement lazy loading ghost objects

---
## [newstools/2022-iol](https://github.com/newstools/2022-iol)@[bd5b454b93...](https://github.com/newstools/2022-iol/commit/bd5b454b938c2776dd2f009907bf063b85afe482)
#### Wednesday 2022-10-05 14:40:48 by Billy Einkamerer

Created Text For URL [www.iol.co.za/news/news/world/watch-this-woman-caught-her-boyfriend-cheating-with-alexas-help-e60e1331-547b-4096-b22a-f18015eacba5]

---
## [BladeburstNINJA/sunset-wasteland](https://github.com/BladeburstNINJA/sunset-wasteland)@[6c856e30fc...](https://github.com/BladeburstNINJA/sunset-wasteland/commit/6c856e30fceaa57e738ea1abfb6a989e77fa161e)
#### Wednesday 2022-10-05 15:39:51 by BadAtThisGame

Overheat warnings to both gatling guns (#742)

* The notorious

* Epic

* FUCK YOU

* I am going to beat you with a club

---
## [sonicthedutchhedgehog/sonic-1-github-madness](https://github.com/sonicthedutchhedgehog/sonic-1-github-madness)@[73a2c285bb...](https://github.com/sonicthedutchhedgehog/sonic-1-github-madness/commit/73a2c285bb4d391adb65e69049025f06e3e49044)
#### Wednesday 2022-10-05 15:45:48 by dg

you all are dicks (delete fuck you.png)

do you really think i don't regret saying that sort of thing?

---
## [iggy/terrarific](https://github.com/iggy/terrarific)@[55ea299879...](https://github.com/iggy/terrarific/commit/55ea29987946d44ec567e729377f96e19d5c77b7)
#### Wednesday 2022-10-05 16:05:39 by iggy

update deps to shut up Trivy

Trivy thinks we're vulnerable to CVE-2022-27664, but that's only if you're
running a server. Which we aren't, but it's annoying and causing the CI to
fail.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a2577296e6...](https://github.com/tgstation/tgstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Wednesday 2022-10-05 16:16:22 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [iswebdevru/rce-schedule-api](https://github.com/iswebdevru/rce-schedule-api)@[f82d26a36e...](https://github.com/iswebdevru/rce-schedule-api/commit/f82d26a36e3fd92ab55ce77c73743dc380f95b0d)
#### Wednesday 2022-10-05 17:12:09 by wardxela

fix: back to HYPEN FUCK YOU YOU GOT WRONG DOOR LEATHER MAN

---
## [MemeHoovy/FNF-Cool-Engine](https://github.com/MemeHoovy/FNF-Cool-Engine)@[49d05921e6...](https://github.com/MemeHoovy/FNF-Cool-Engine/commit/49d05921e68999ae1cabf55a452226ff503962fe)
#### Wednesday 2022-10-05 17:13:33 by XuelDev

XuelDev Commit | Squashed, Added Mod Menu and Fixed VideoState for Linux And Mac And Windows :)

* HOW THE FUCK?

* Holy Shit New Update :)

* FUCKKKK

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6aeb464d33...](https://github.com/treckstar/yolo-octo-hipster/commit/6aeb464d33a1adf4e892456980226a57d4247c33)
#### Wednesday 2022-10-05 17:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Vordenburg/Nyanotrasen](https://github.com/Vordenburg/Nyanotrasen)@[8f52eb9e0f...](https://github.com/Vordenburg/Nyanotrasen/commit/8f52eb9e0f7e246ddcadb7f96a948ceec27d7ee4)
#### Wednesday 2022-10-05 17:26:50 by ZeroDayDaemon

Psionic Content (#542)

* Psionic Content

* Address Reviews

* rane bitches too much

* Tonight, on unsolved mysteries, find out who gives a shit about bigfoot

UPDATE: apparently nobody gives a shit so fuck him.

UPDATE: Last night somebody broke in and stole $500 worth of shit at my house

That’s right $500 worth of BULLSHIT!!!

* Address reviews

---
## [ItzJustGig/projekt-kepler](https://github.com/ItzJustGig/projekt-kepler)@[be1cac3b13...](https://github.com/ItzJustGig/projekt-kepler/commit/be1cac3b13fdb7e5ec1f34f5765d33240be7a5f0)
#### Wednesday 2022-10-05 17:29:12 by gig

Bug Fix, Icer Ult, Ult rate tooltip

Bug fix regarding bonus stats
Blood Pumping, Courage, Mana Thirst, Bulls Rage, Fear Smell, Plasma Blade, Fighter Instinct, Zen Mode, Hunter's Dirk, Wild Instinct, Spectral Ring not counting Bonus Hp, Mana, Stamina, Sanity
Gale Glide bonus timing

Dot Physical Life Steal not counting bonus lifesteal
Effect Mitigation not counting bonus res

Effect Healing On Cap
AI Max Mana Detection
Apply Stat Mod On Max Hp, Mana, Sta, San
Get Max Heal Hp, Mana, Sta, San
not counting Bonus Hp, Mana, Stamina, Sanity

------
Added Mecha Shield
------
Ult Rate tooltop

---
## [RobertCNelson/ti-linux-kernel](https://github.com/RobertCNelson/ti-linux-kernel)@[adee8f3082...](https://github.com/RobertCNelson/ti-linux-kernel/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Wednesday 2022-10-05 19:01:26 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [RimiNosha/Skyrat-tg](https://github.com/RimiNosha/Skyrat-tg)@[a4bfe65cb1...](https://github.com/RimiNosha/Skyrat-tg/commit/a4bfe65cb1caece1e3e6a4635fa17d39f1aa3478)
#### Wednesday 2022-10-05 19:05:45 by SkyratBot

[MIRROR] Dimensional Anomaly [MDB IGNORE] (#15974)

* Dimensional Anomaly (#69512)

About The Pull Request

Everyone has been asking: "When will there be an anomaly like the bioscrambler, but for the space station? Please, we need more things which replace objects with different objects from the same typepath."
Well I made it and it looked like ass because non-tiling floor and walls look terrible, so then I made this instead.
Dimensional.mp4

The "dimensional anomaly" shifts matter into a parallel dimension where objects are made out of something else.
Like the Bioscrambler anomaly, it does not expire on its own and only leaves when someone signals it or uses an anomaly remover.
When it spawns it picks a "theme" and converts terrain around it until it covers a 7x7 square, then it teleports somewhere else and picks a new theme.

A lot of these themes are relatively benign like "meat", "fancy carpet", or "gold". Some of them are kind of annoying like "icebox" because it creates floor which slows you down, or "clown" because bananium is intentionally annoying. Some of them are actively dangerous, mostly "uranium" and "plasma".
The main problem this will usually cause for crewmembers is decreasing area security. When it replaces doors it replaces them with ones which don't have any access control, and it will also replace RWalls with normal and much more vulnerable walls which will make breaking and entering significantly easier until someone has taken the time to fix the damage. But also sometimes it will irradiate them, you never know.

The fact that sometimes the changes are benign (or provide uncommon materials) and might be happening in places you don't care about access to might encourage people to push their luck and leave it alone until it starts turning the captain's office into a bamboo room or repainting medbay a fetching shade of flammable purple, which I would consider a success.
Armour.mp4

If you successfully harvest the anomaly core you can place it into the reactive armour to get Reactive Barricade Armour, which shifts your dimension when you take damage and attempts to place some randomised (not terribly durable) objects between you and hopefully your attacker (it really just picks up to four random unoccupied tiles next to you). If you're EMPed then the changes it make to the environment will often be as unpleasant for you as they are for a pursuer, and significantly more likely to harm both of you rather than just provide obstacles.

Other changes:
I split anomalies out into their own dmi file, seems to be all the rage lately.
I moved the anomaly placing code into a datum instead of the event because I wanted to reuse it but if you have a better idea about where I could have put it let me know.
This also fixes a bug where the material spreader component wasn't working when I applied plasma materials to something, the extra whitespace was parsing as another argument for some reason and meant it would runtime.
Supermatter delamination was still pointing to Delimber anomalies instead of Bioscrambler.

* Dimensional Anomaly

* Fixes the upstream merge skew

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [n-borges/black](https://github.com/n-borges/black)@[0019261abc...](https://github.com/n-borges/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Wednesday 2022-10-05 19:23:58 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [ABuffaloHerd/cise-product-1](https://github.com/ABuffaloHerd/cise-product-1)@[83ad7355d6...](https://github.com/ABuffaloHerd/cise-product-1/commit/83ad7355d67be7e7b2f4de08168402fdd001dd27)
#### Wednesday 2022-10-05 19:38:32 by ABuffaloHerd

submit form update from alessandra fuck you node modules all you do is ruin everything

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[1810b85553...](https://github.com/IndieanaJones/tgstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Wednesday 2022-10-05 19:38:54 by tralezab

Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how 

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

---
## [haasn/mp](https://github.com/haasn/mp)@[f4e89dde36...](https://github.com/haasn/mp/commit/f4e89dde36644edec7d09856ac83140317f0b687)
#### Wednesday 2022-10-05 19:45:02 by Dudemanguy

wayland: simplify render loop

This is actually a very nice simplification that should have been
thought of years ago (sue me). In a nutshell, the story with the
wayland code is that the frame callback and swap buffer behavior doesn't
fit very well with mpv's rendering loop. It's been refactored/changed
quite a few times over the years and works well enough but things could
be better. The current iteration works with an external swapchain to
check if we have frame callback before deciding whether or not to
render. This logic was implemented in both egl and vulkan.

This does have its warts however. There's some hidden state detection
logic which works but is kind of ugly. Since wayland doesn't allow
clients to know if they are actually visible (questionable but
whatever), you can just reasonably assume that if a bunch of callbacks
are missed in a row, you're probably not visible. That's fine, but it is
indeed less than ideal since the threshold is basically entirely
arbitrary and mpv does do a few wasteful renders before it decides that
the window is actually hidden.

The biggest urk in the vo_wayland_wait_frame is the use of
wl_display_roundtrip. Wayland developers would probably be offended by
the way mpv abuses that function, but essentially it was a way to have
semi-blocking behavior needed for display-resample to work. Since the
swap interval must be 0 on wayland (otherwise it will block the entire
player's rendering loop), we need some other way to wait on vsync. The
idea here was to dispatch and poll a bunch of wayland events, wait (with
a timeout) until we get frame callback, and then wait for the compositor
to process it. That pretty much perfectly waits on vsync and lets us
keep all the good timings and all that jazz that we want for mpv. The
problem is that wl_display_roundtrip is conceptually a bad function. It
can internally call wl_display_dispatch which in certain instances,
empty event queue, will block forever. Now strictly speaking, this
probably will never, ever happen (once I was able to to trigger it by
hardcoding an error into a compositor), but ideally
vo_wayland_wait_frame should never infinitely block and stall the
player. Unfortunately, removing that function always lead to problems
with timings and unsteady vsync intervals so it survived many refactors.

Until now, of course. In wayland, the ideal is to never do wasteful
rendering (i.e. don't render if the window isn't visible). Instead of
wrestling around with hidden states and possible missed vblanks, let's
rearrange the wayland rendering logic so we only ever draw a frame when
the frame callback is returned to use (within a reasonable timeout to
avoid blocking forever).

This slight rearrangement of the wait allows for several simplifications
to be made. Namely, wl_display_roundtrip stops being needed. Instead, we
can rely entirely on totally nonblocking calls (dispatch_pending, flush,
and so on). We still need to poll the fd here to actually get the frame
callback event from the compositor, but there's no longer any reason to
do extra waiting. As soon as we get the callback, we immediately draw.
This works quite well and has stable vsync (display-resample and audio).
Additionally, all of the logic about hidden states is no longer needed.
If vo_wayland_wait_frame times out, it's okay to assume immediately that
the window is not visible and skip rendering.

Unfortunately, there's one limitation on this new approach. It will only
work correctly if the compositor implements presentation time. That
means a reduced version of the old way still has to be carried around in
vo_wayland_wait_frame. So if the compositor has no presentation time,
then we are forced to use wl_display_roundtrip and juggle some funny
assumptions about whether or not the window is hidden or not. Plasma is
the only real notable compositor without presentation time at this stage
so perhaps this "legacy" mechanism could be removed in the future.

---
## [justjoehere/undetected-chromedriver](https://github.com/justjoehere/undetected-chromedriver)@[ebafbe1db6...](https://github.com/justjoehere/undetected-chromedriver/commit/ebafbe1db6fe34dff142bfa74da49b011fa62418)
#### Wednesday 2022-10-05 20:08:59 by Leon

3.0.0 (#180)

*3.0.0
added lots of features and bugfixes

- You can now subscribe to Chrome Devtools Protocol Events like networking.
- splitted the project up in seperate modules now
- fixed locale (accept-language)
- you can enter your user-data-folder as property of
    ChromeOptions() now.
- The ChromeOptions had a makeover, and i took the one from alpha 4,
    people having troubles with mobile emulation and other bullshit,
    can try again now.
- fixed the logic where sometimes options did not
    respect the given values
- for headless (though still not supperted for undetectability),
    added some real cool features which need to be set in
    the options object):

    defaults:
    emulate_touch = True
    mock_permissions = True  # headless had notificationpermissions
                                setup in a distinguisable way.
    mock_chrome_global = False
    mock_canvas_fp = True  # patch fingerprint

EXTENSIONS ARE NOT SUPPORTED BY CHROME IN HEADLESS MODE
YET. IF YOU WANT TO USE THEM, CREATE A PROFILE AND INSTALL
EXTENSIONS BY USING A REGULAR CHROME SESSION FIRST.
ALSO LOGIN TO GMAIL WHILE YOU'RE ON A GENUINE SESSION.

WHEN FINISHED, COPY THE USERDATA FOLDER OF CHROME TO SOME KNOWN
LOCATION (and make maye 2 copies?). BY HAVING GMAIL LOGGED IN
FIXES ALSO THE UNSAFE BROWSER MESSAGE FROM GOOGLE (AT LEAST FOR
ME IT WORKS)


* 2.2.2

* fixed a number of bugs
- specifying custom profile
- specifying custom binary path
- downloading, patching and storing now (if not explicity specified)
    happens in a writable folder, instead of the current working dir.

Committer: UltrafunkAmsterdam <UltrafunkAmsterdam@github>

* tidy up

* uncomment block

* - support for specifying and reusing the user profile folder.
    if a user-data-dir is specified, that folder will NOT be
    deleted on exit.
    example:
        options.add_argument('--user-data-dir=c:\\temp')

- uses a platform specific app data folder to store driver instead
    of the current workdir.

- impoved headless mode. fixed detection by notification perms.

- eliminates the "restore tabs" notification at startup

- added methods find_elements_by_text and find_element_by_text

- updated docs (partly)

-known issues:
    - extensions not running. this is due to the inner workings
        of chromedriver. still working on this.
    - driver window is not always closing along with a program exit.
    - MacOS: startup nag notifications. might be solved by
        re(using) a profile directory.

- known stuff:
    - some specific use cases, network conditions or behaviour
      can cause being detected.

* Squashed commit of the following:

commit 7ce8e7a236cbee770cb117145d4bf6dc245b936a
Author: ultrafunkamsterdam <info@blackhat-security.nl>
Date:   Fri Apr 30 18:22:39 2021 +0200

    readme change

commit f214dcf33f26f8b35616d7b61cf6dee656596c3f
Author: ultrafunkamsterdam <info@blackhat-security.nl>
Date:   Fri Apr 30 18:18:09 2021 +0200

    - make sure options cannot be reused as it will
        cause double and conflicting arguments to chrome



    - support for specifying and reusing the user profile folder.
        if a user-data-dir is specified, that folder will NOT be
        deleted on exit.
        example:
            options.add_argument('--user-data-dir=c:\\temp')

    - uses a platform specific app data folder to store driver instead
        of the current workdir.

    - impoved headless mode. fixed detection by notification perms.

    - eliminates the "restore tabs" notification at startup

    - added methods find_elements_by_text and find_element_by_text

    - updated docs (partly)

    -known issues:
        - extensions not running. this is due to the inner workings
            of chromedriver. still working on this.
        - driver window is not always closing along with a program exit.
        - MacOS: startup nag notifications. might be solved by
            re(using) a profile directory.

    - known stuff:
        - some specific use cases, network conditions or behaviour
          can cause being detected.

---
## [skylord-a52/orbstation-andrea](https://github.com/skylord-a52/orbstation-andrea)@[3b2cf65d59...](https://github.com/skylord-a52/orbstation-andrea/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Wednesday 2022-10-05 20:15:11 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [plinkiac/Movie-Talk](https://github.com/plinkiac/Movie-Talk)@[e5f4254598...](https://github.com/plinkiac/Movie-Talk/commit/e5f4254598f5ca9b9f98362b4ea6b81a2fbd2e61)
#### Wednesday 2022-10-05 20:51:57 by Harry S. Plinkett

Update 2017-01-12 - Fuck You, It's January (2017).txt

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[756802b609...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/756802b609e97266775458b4c41f8c68091ae062)
#### Wednesday 2022-10-05 20:56:19 by InsightfulParasite

fixes

Moonstones now sorta work.

Moonlightstones now work and the sanity insurance status effect is now seperate from the item but the status effect procs the shattering of all items of the moonstone type on the person.
Still the code feels wonky but for its purpose it works. Sanity insurance doesnt work when killed by funeral.

added Quiphoth Field Projecter and Pets

added additional icons, battery powered gadget, and ordeal pets.

QLIPHOTH OVERLOAD

Its far from perfect but less than dangerous.
New status effect QLIHOTH OVERLOAD. Applys 167 stamina damage to enitites and applies a movment speed modifier.

Waypoints, Restingpot, Moonstones, and icon dump.

add: waypoints for each of the 10 departments.
add: Restingpot, some silly sprite that i felt looked calming so i made it a oddity.
add: Moonlight stones, M corp apparently developed these in the lore according to the project moon wiki. They protect against psychological attacks but until we can specify damage as psychological they currently act as a one time use safety net for when you go insane.
add: Dumped some oddity icons into Teguicons. Unsure if im allowed to do this.

---
## [danielzfranklin/bpack](https://github.com/danielzfranklin/bpack)@[1ca3515f66...](https://github.com/danielzfranklin/bpack/commit/1ca3515f6657a26941f6dcf67832337dc430322f)
#### Wednesday 2022-10-05 21:23:08 by Daniel Franklin

[mk] Run trivial fn on laptop w/ ugly hacks

I use autocxx to generate bindings for `mapnik::Map`, blocklisting
anything that autocxx couldn't automatically translate to quickly get to
a POC.

To prove I could generate bindings for, compile, link, and then run
something on my laptop I picked two incredibly trivial to call fns
(the default map constructor and a fn that serializes a map to
xml) and wrote a test case.

Read [mapnik-sys/dep_notes.md] for a writeup on the ugly hacks and how
to run the fn. The worst hack is a patch to `autocxx` that skips
by name two member fns that were giving me trouble.

I based this on the latest release of mapnik without thinking about it.
That release is about a year old, and I want to be working close to
HEAD.

 - Upgrade mapnik and fix breakage so trivial test passes
 - Run trivial test in browser via wasm - do any hacks necessary to get
   to POC

---
## [LCRERGO/dwm](https://github.com/LCRERGO/dwm)@[67d76bdc68...](https://github.com/LCRERGO/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-10-05 21:25:08 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [OpenImageIO/oiio](https://github.com/OpenImageIO/oiio)@[4ee35351f1...](https://github.com/OpenImageIO/oiio/commit/4ee35351f100c79738c77892fb8ccca8ddc004c9)
#### Wednesday 2022-10-05 23:03:42 by Aras Pranckevičius

DDS: alpha/luminance format fixes, add & enable more tests (#3581)

* DDS: fixes for A8, L8, A8L8 formats

While developing #3573 at one time I had them working properly, but then
while fixing the address sanitizer failure for 3-channel formats I
botched them again. Note to self: never again do a "yeah I'll add tests
later", since if I had all of them running all the time this would
not have happened. :facepalm:

* DDS: extend test coverage for more formats & channel size cases

With more test images recently added (https://github.com/OpenImageIO/oiio/pull/3459),
start using them for DDS tests. This covers now:
- Alpha, Luminance and Alpha+Luminance formats,
- RGB formats with rarer channel sizes (rgb10 a2, r3g3b2),
- Several "broken" DDS file cases
- Removed usage of sample-DXT1 since it is well covered by others.

---

