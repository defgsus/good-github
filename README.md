## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-09](docs/good-messages/2022/2022-02-09.md)


1,720,142 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,720,142 were push events containing 2,747,079 commit messages that amount to 220,780,041 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [aospa-pasco/kernel_xiaomi_ginkgo](https://github.com/aospa-pasco/kernel_xiaomi_ginkgo)@[89af3da90e...](https://github.com/aospa-pasco/kernel_xiaomi_ginkgo/commit/89af3da90eeeea86e2f11f4805ad8bc31f9ebb54)
#### Wednesday 2022-02-09 00:07:55 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>

---
## [BakaKaito/Mergebot.NET](https://github.com/BakaKaito/Mergebot.NET)@[00b446c92c...](https://github.com/BakaKaito/Mergebot.NET/commit/00b446c92c95d828cdd8573b66aecb86e7d56d4c)
#### Wednesday 2022-02-09 00:40:47 by Koi

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
## [Scacer/RL_Tetris](https://github.com/Scacer/RL_Tetris)@[599aa4e369...](https://github.com/Scacer/RL_Tetris/commit/599aa4e36992cf0926ff40d409503b75c1d06646)
#### Wednesday 2022-02-09 00:47:56 by Scacer

HOLY SHIT IT TOOK FOREVER BUT I GOT IT TO A REASONABLE STATE ALREADY

keep this up you idiot, if you don't I'll kill you

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[d504fe76f4...](https://github.com/Stalkeros2/Skyrat-tg/commit/d504fe76f4935518b45f3ba1ec6d935af5f16b55)
#### Wednesday 2022-02-09 01:04:57 by SkyratBot

[MIRROR] Fixes harddels in pinned module code, cleans up a musty pattern that I want to die [MDB IGNORE] (#11319)

* Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

* Fixes harddels in pinned module code, cleans up a musty pattern that I want to die

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[07564773c2...](https://github.com/git-for-windows/git/commit/07564773c2569d012719ab9e26b9b27251f3d354)
#### Wednesday 2022-02-09 01:05:00 by Ævar Arnfjörð Bjarmason

compat: auto-detect if zlib has uncompress2()

We have a copy of uncompress2() implementation in compat/ so that we
can build with an older version of zlib that lack the function, and
the build procedure selects if it is used via the NO_UNCOMPRESS2
$(MAKE) variable.  This is yet another "annoying" knob the porters
need to tweak on platforms that are not common enough to have the
default set in the config.mak.uname file.

Attempt to instead ask the system header <zlib.h> to decide if we
need the compatibility implementation.  This is a deviation from the
way we have been handling the "compatiblity" features so far, and if
it can be done cleanly enough, it could work as a model for features
that need compatibility definition we discover in the future.  With
that goal in mind, avoid expedient but ugly hacks, like shoving the
code that is conditionally compiled into an unrelated .c file, which
may not work in future cases---instead, take an approach that uses a
file that is independently compiled and stands on its own.

Compile and link compat/zlib-uncompress2.c file unconditionally, but
conditionally hide the implementation behind #if/#endif when zlib
version is 1.2.9 or newer, and unconditionally archive the resulting
object file in the libgit.a to be picked up by the linker.

There are a few things to note in the shape of the code base after
this change:

 - We no longer use NO_UNCOMPRESS2 knob; if the system header
   <zlib.h> claims a version that is more cent than the library
   actually is, this would break, but it is easy to add it back when
   we find such a system.

 - The object file compat/zlib-uncompress2.o is always compiled and
   archived in libgit.a, just like a few other compat/ object files
   already are.

 - The inclusion of <zlib.h> is done in <git-compat-util.h>; we used
   to do so from <cache.h> which includes <git-compat-util.h> as the
   first thing it does, so from the *.c codes, there is no practical
   change.

 - Until objects in libgit.a that is already used gains a reference
   to the function, the reftable code will be the only one that
   wants it, so libgit.a on the linker command line needs to appear
   once more at the end to satisify the mutual dependency.

 - Beat found a trick used by OpenSSL to avoid making the
   conditionally-compiled object truly empty (apparently because
   they had to deal with compilers that do not want to see an
   effectively empty input file).  Our compat/zlib-uncompress2.c
   file borrows the same trick for portabilty.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Helped-by: Beat Bolli <dev+git@drbeat.li>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [EuSouAFazer/tgstation](https://github.com/EuSouAFazer/tgstation)@[906fb0682b...](https://github.com/EuSouAFazer/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Wednesday 2022-02-09 01:07:37 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [OpenXRay/xray-16](https://github.com/OpenXRay/xray-16)@[986f2139a8...](https://github.com/OpenXRay/xray-16/commit/986f2139a8a596c7dd81343c20be809760352cdb)
#### Wednesday 2022-02-09 01:14:13 by Xottab_DUTY

BE AWARE OF A FORCE PUSH SOON

Don't update to this and previous two commits.

Damn it, I fucking hate polluting commit history with non-pure commits followed with fixes commits.

But I will sleep first and then disintegrate this.

---
## [Bunnificent/ajw_Learning-SocialNetworkAnalysis](https://github.com/Bunnificent/ajw_Learning-SocialNetworkAnalysis)@[de52e3af83...](https://github.com/Bunnificent/ajw_Learning-SocialNetworkAnalysis/commit/de52e3af838cd4f899c9d4a0f1cfd21b24ae85e8)
#### Wednesday 2022-02-09 01:51:28 by Audra Jamai

2.8.22
Merge branch 'main' of https://github.com/Bunnificent/ajw_Learning-SocialNetworkAnalysis

2.8.22
added document files and imported 4.CSV datasets: "index by name-PDT"; "index by ingredient-PDT", Dead & Co, cocktail recipies"; "Smuggler's Cove cocktail index by drink name"

"PDT-index by name" is fucked up, it only imported into one colomn and needs a lot of cleaning.

---
## [mayorsporky42/Mizuchi](https://github.com/mayorsporky42/Mizuchi)@[125857e935...](https://github.com/mayorsporky42/Mizuchi/commit/125857e935210ac6c058cd8e529322ec62502358)
#### Wednesday 2022-02-09 02:21:50 by mayorsporky42

More memes added from Discord

Memes added: Jin slider, Keras Selyrian is right behind you, Keras Ancestry Test, baby; sword for scale, Internal Tengine error, corin blood stealer, Styles of Keras, Cockatrice lies, book titles, ishy angel devil, patrick lightning is a weapon, Keras dual sword body pillow, keras mask, AA I'd die for you, AA children yelling mcdonalds, can I copy your homework AA, AA distinguished gay, airfryer keras, Kerek Shrelyrian, Keras impaled, baby sword sword baby for scale

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Wednesday 2022-02-09 03:00:07 by Albert Liu

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
## [libressl-portable/openbsd](https://github.com/libressl-portable/openbsd)@[70eaeb7b5e...](https://github.com/libressl-portable/openbsd/commit/70eaeb7b5e6c3ca76de6484bc11d0ab38c903093)
#### Wednesday 2022-02-09 03:16:43 by beck

After much horrible and painful slogging through asn1 code,
this fixes the source of connection problems with ssl/tls connections
between sparc64 and other things.

The punchline, we just found a bug in floating point emulation
on sparc64 when this script produces off-by-one output on sparc64.

This fix is annoyingly easy for the effort expended.

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[50dda99a89...](https://github.com/repinger/exynos9611_m21_kernel/commit/50dda99a8976bf4b53db4b9cae9680932ec58b2a)
#### Wednesday 2022-02-09 04:08:43 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

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
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[57a500cec7...](https://github.com/LemonInTheDark/tgstation/commit/57a500cec72176e1b4e6a27623b74a839937cb99)
#### Wednesday 2022-02-09 04:35:54 by LemonInTheDark

Moves atmos pressure movement to moveloops

I'm dismayed by how pressure movement works currently. Tying it directly
to atmos itself is particularly troublesome, since atmos doesn't always
fire consistantly.

It working based off probabilities also makes it feel kinda crappy. So
lets do move loops instead.

They're going to be more expensive just by default, since we're well,
making things move more often, but I think smooth movement even under
load is worth it.

Oh and I'm adding code that ensures that negative pressure is treated as
pressure in the opposite direction, rather then negative force.
Hopefully this makes things a bit nicer.

---
## [gaelicWizard/bash-it](https://github.com/gaelicWizard/bash-it)@[ee4598e7b3...](https://github.com/gaelicWizard/bash-it/commit/ee4598e7b3636a9572f90f4b1509fa3234c48e94)
#### Wednesday 2022-02-09 05:06:39 by John D Pell

lib/search: code style cleanup

Couldn't even `shellcheck` until I did a first pass...too much noise! ♥

lib/search: `shellcheck`

SC2076
SC2091
SC2004
SC2086
SC2207

lib/search: fix `_bash-it-flash-term()`

1. `$text_black` isn't a parameter provided by _Bash It_. Typo?
2. `$bold_yellow` is meant for prompt strings and putputs `\[`; ditto `$bold_red`.
3. The color was never returned to normal after.

lib/search: fix usage statement `_bash-it-search()`

SC2154

lib/search: `shfmt`

My apologies to future `git blame` hunters ♥

lib/search: code cleanup

Improve `_bash-it-erase-term()`, `_bash-it-flash-term()`, `_bash-it-rewind()`, `_bash-it-search-result()`, and `_bash-it-search-component()`. Minor tweaks to `_bash-it-is-partial-match()`, and `_bash-it-search()`.

pathmunge tests

main: Glob for *.bash properly when path contains spaces

- `shfmt`, `shellcheck`
- Clean up legacy/compatibility code to simpler control flow
- Move theme stuff down to where themes are handled
- Don't use `**` as _Bash It_ has never before set `globstar`; this eliminates varying behavior by environment; this alsö fixes users having any not-enabled themes under their custom dir.
- Lose weird Mac-specific alternate shell startup file (Bash loads startup files on Mac the same as it does on any other *nix system.)
- Place `composure.sh` init all in one place

main: adopt `_bash-it-log-prefix-by-path()`

lib/reloader: adopt `_bash-it-log-prefix-by-path()`

lib/appearance: `shellcheck` && `shfmt`

reloader: `shellcheck` && `shfmt`

Rewrite globbing per `shellcheck`'s SC2013 recommendations, and standardize whitespace.

lib/preview: `shfmt` && `shellcheck`

Fix theme file path globbing when $BASH_IT contains any spaces.

My apologies to future `git blame` hunters ♥

uninstall: `shellcheck` && `shfmt`

lint: add lib to clean_files.txt

lib/theme: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/colors: `shellcheck` && `shfmt`

Alsö, clean up `__color_rgb` to just use a regular if block.

lib/p4helpers: `shfmt`

My apologies to future `git blame` hunters ♥

lib/githelpers: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/theme: don't redefine battery_char()

Combine the two definitions for `battery_char()` so the second one doesn't just overwrite the first one. Do one or the other, not both.

Don't evaluate if `battery_percentage()` is available at load time, evaluate it at run time.

lib/command_duration: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/theme: `shellcheck` SC2154

These variables are referenced by themes already linted.

lib/theme.githelpers: unbound varbl

lib/theme: don't use `date` for `$THEME_CLOCK_FORMAT`

main: simplify flow of lib loader loop

Eliminate the separate loop for `vendor/init.d` since it's just as easy to glob it in the `lib` loop.

lib: delete `appearance.bash`

This adds *three* lines to `bash_it.sh`, and two to `plugin/base`. Just not worth an extra file requiring special handling.

main: load custom theme

Allow for simpler directory strucutre when loading theme from `$CUSTOM_THEME_DIR`/`$BASH_IT_CUSTOM`

make aliases load very late

...and update all the tests...

preexec: add helper functions to loader

Define the helper functions for `bash-preexec.sh` immediately after importing it, rather than in `lib/theme`.
- `__check_precmd_conflict()` and `save_append_prompt_command()` are generally useful and not theme-specific.
- Add matching `__check_preexec_conflict()` like `__check_precmd_conflict()`, and alsö `safe_append_preexec()`.

preexec: work around upstream

Alsö, move `set +T` in here.

test/theme: make fewer assumptions

Literally copying a line from the source to be tested is perhaps not the best way to test that code. 😉

That said, we do want to verify that the function was actually loaded.

TODO: actually test the function.

install: use `.bashrc` and notify user

The logic to guess whether to use `.bash_profile` or `.bashrc` was buggy and wrong. Just use `.bashrc` and either automatically fill in a `.bash_profile`, or notify the user that they need to edit their `.bash_profile`.

completions/sqlmap: use `_command_exists`

Addresses bash-it/bash-it#1632

completion/fabric: no need for `_command_exists`

If we're already inside the completion handler for `fab`...then it's a bit silly to check if `fab` is installed.

plugins/go: simplify _bash-it-gopath-pathmunge()

plugin/history: no need to set a trap
Instead of globbally clearing `$HISTTIMEFORMAT` and setting a return trap to re-enable it, just make it local to the function.

Also, set the defaults in a way that is happy with read-only parameters.

aliases/general: minor fixes

- Don't define some aliases if the target isn't installed, use _command_exists to check instead of `type` and `which`.
- Use `$EDITOR` for the editor for aliases about editing, excep the `sudo` ones because maybe you want those specifically?
- Fix `ls` aliases to match their common definitions (-A instead of -a: don't show '.' and '..' when displaying hidden files).

themes/base: use `type -P` instead of `which`

Avoid external binary `which`. Use built-in `type -P` instead. Uppercase `-P` forces a path search to avoid hashed matches and functions/aliases and whatnot.

completion/grunt: shellcheck

completion/subversion: load system completion

Load the completion script from the subversion package installed on the system, instead of bundling a copy. This addresses Bash-it/bash-it#1818.

NOTE: If `completions/system` is enabled, then it will load this same file anyway automatically.

plugins/battery: lint

plugins/xterm: not just Xterm

plugins/thefuck: lint

plugins/todo: lint

plugin/base: use `_bash-it-component-item-is-enabled()`

completion/git: use `_completion_exists()`

plugins/alias: remove old `SC2154` flag

This is no logner needed because the `local` keyword was moved higher up in the function.

---
## [OctoSix/awesome-flutter](https://github.com/OctoSix/awesome-flutter)@[73e15b8df1...](https://github.com/OctoSix/awesome-flutter/commit/73e15b8df13eea815cb38617f9636cf228df6082)
#### Wednesday 2022-02-09 05:29:45 by Pooja Bhaumik

Added "I want to learn Flutter. How to start?" article

Added this article - https://medium.com/flutter-community/i-want-to-learn-flutter-how-to-start-ffb4145f9b26 under the "Begin With" category. This is a step by step guide for learning Flutter for super beginners, personalized with my own trial and error experiences. And also contains a list of useful tips & plenty of amazing resources from the flutter community. Already has 1.2K claps on Medium

---
## [mvaisakh/oneplus7](https://github.com/mvaisakh/oneplus7)@[8911bd28ce...](https://github.com/mvaisakh/oneplus7/commit/8911bd28ce91e1d0613b12364e28786b07ab8de5)
#### Wednesday 2022-02-09 05:51:19 by alk3pInjection

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
## [Project-Awaken-Twelve/android_packages_apps_Launcher3](https://github.com/Project-Awaken-Twelve/android_packages_apps_Launcher3)@[3d6645361d...](https://github.com/Project-Awaken-Twelve/android_packages_apps_Launcher3/commit/3d6645361d933884fe4ed338a147f4c7ced60e10)
#### Wednesday 2022-02-09 06:44:41 by Alex Cruz

Launcher3: Restart with change only on exit

This change allow the user to change everything they have to inside the
homescreen activity and only restart on exit. Previously this was a pain
in the fucking ass because you had to go in and set each option one by one
with a restart inbetween. At least now is not that big of a pain.

- Restart on destroy (hitting the back button, actionbar arrow)
- Restart when a chance is made and the home button is pressed

** Thanks "Jack" for code to detect home button
https://stackoverflow.com/a/27956263

- Cleaned up restart code

eyosen adapted to 10

Change-Id: I4962916ae0bd59d08247b59de585a97a2b9da3a1

---
## [BoltManGuy/UI_Scaler](https://github.com/BoltManGuy/UI_Scaler)@[4745c25ae5...](https://github.com/BoltManGuy/UI_Scaler/commit/4745c25ae53fa594fdf281c55ab26c0e6081843c)
#### Wednesday 2022-02-09 06:53:39 by BoltManGuy

refactor functions into local because APPARENTLY its not contained within the script otherwise and fucks up other files with same function names omg how can this be so stupid whos fault is this

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1f23d3d7ad...](https://github.com/tgstation/tgstation/commit/1f23d3d7ad87eebf74b1c9dc51867c5c21edf547)
#### Wednesday 2022-02-09 07:58:48 by Jeremiah

Should fix shuttles leaving without sections(#64764)

Should(tm)

This was a suggestion by @Mothblocks and it seemed easy to implement

Fixes #64546 (Icebox evac will sometimes leave without sections)
Fixes #64653 (You might have fixed the kilo whiteship by making it move, but you didn't fix all of it)

Uh people won't just randomly get yeeted into space with half of a shuttle.
Kinda funny for people watching but not if you die of pressure loss or get stuck on the station
Runtime man bad

(Sleeping in here in general is like admitting that we're ok with missing a few atoms, which is what this runtime is. S just missing is better then overtime. Supposedly --Lemon)

---
## [Empire-Strikes-Back/Mando](https://github.com/Empire-Strikes-Back/Mando)@[e610f3710b...](https://github.com/Empire-Strikes-Back/Mando/commit/e610f3710bac9568a98fd0d962e9e4fc546e82e6)
#### Wednesday 2022-02-09 09:02:08 by Mando

Jon Stewart: no, you come across to people as a big bear of a deep shit, i feel like people see and they're like - oh my God, i'm better than that guy! and they look at you and they say - that fat fuck! they taught him how to stand with the monkey and hold a baby - and now look at him go!  Galifianakis: thanks, man

---
## [0mp/dwm](https://github.com/0mp/dwm)@[67d76bdc68...](https://github.com/0mp/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-02-09 10:25:27 by Chris Down

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
## [nutanix-cloud-native/openshift-api](https://github.com/nutanix-cloud-native/openshift-api)@[5b82635ef1...](https://github.com/nutanix-cloud-native/openshift-api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Wednesday 2022-02-09 13:08:23 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [nicholastay/personal-web](https://github.com/nicholastay/personal-web)@[94bd11e624...](https://github.com/nicholastay/personal-web/commit/94bd11e6242954ad804bef9ef54e8d12fa28c66e)
#### Wednesday 2022-02-09 13:36:02 by Nicholas Tay

Old IE fixes (lol)

Had to whip out the underscore hack again for now. Also, not sure if
rems are working in IE5 on W98 - I think it isn't, but elements look
okay for now. Just had to fix some spacing back to using px (kinda
sucks, but yeah).

tbh I still don't quite get em/rem, just using it as I heard it's nice.

---
## [Daninnocent/PoyoEngine](https://github.com/Daninnocent/PoyoEngine)@[3fad59de8d...](https://github.com/Daninnocent/PoyoEngine/commit/3fad59de8dd10d14c606a1d96bb58161d8682af7)
#### Wednesday 2022-02-09 14:25:22 by Danintooshit

well fuck you im about to sleep can you go any faster

---
## [dankan1890/mame](https://github.com/dankan1890/mame)@[a49e215466...](https://github.com/dankan1890/mame/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Wednesday 2022-02-09 14:59:15 by Firehawke

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
## [NextWork123/kernel_xiaomi_sm8250-1](https://github.com/NextWork123/kernel_xiaomi_sm8250-1)@[198cce6886...](https://github.com/NextWork123/kernel_xiaomi_sm8250-1/commit/198cce6886461c52fbb92da66f169245c6a882bf)
#### Wednesday 2022-02-09 17:42:55 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Warcraft-GoA-Development-Team/Warcraft-Guardians-of-Azeroth-2](https://github.com/Warcraft-GoA-Development-Team/Warcraft-Guardians-of-Azeroth-2)@[a5946f267b...](https://github.com/Warcraft-GoA-Development-Team/Warcraft-Guardians-of-Azeroth-2/commit/a5946f267be861fb53cb265317e24ec064fc5b6a)
#### Wednesday 2022-02-09 18:17:26 by Loralius

holy site modifiers; amani, pandaren, jinyu doctrines

Ula-Tek and Karazhan now grant positive opinion from rulers of different faiths. Arcane is now shunned by Amani. Pandaren and Jinyu ignore life magic.

---
## [apache/couchdb](https://github.com/apache/couchdb)@[77f34a1bbc...](https://github.com/apache/couchdb/commit/77f34a1bbc7c76aefa59777da21e2e76e79f7ec8)
#### Wednesday 2022-02-09 18:18:53 by Adam Kocoloski

Refactor Jenkins to dynamically generate stages

This is one of those situations where you go in to make a small change,
see an opportunity for some refactoring, and get sucked into a rabbit
hole that leaves you wondering if you have any idea how computers
actually work. My initial goal was simply to update the Erlang version
used in our binary packages to a modern supported release. Along the
way I decided I wanted to figure out how to eliminate all the copypasta
we generate for making any change to this file, and after a few days of
hacking here we are. This rewrite has the following features:

* Updates to use Debian 11 (current stable) as the base image for
  building releases and packaging repos.

* Defaults to Erlang 23 as the embedded Erlang version in packages. We
  avoid Erlang 24 for now because Clouseau is not currently compatible.

* Dynamically generates the parallel build stages used to test and
  package CouchDB on various OSes. This is accomplished through a bit
  of scripted pipeline code that relies on two new methods defined at
  the beginning of the Jenkinsfile, one for "native" builds on macOS
  and FreeBSD and one for container-based builds. See comments in the
  Jenkinsfile for additional details.

* Expands commands like `make check` into a series of steps to improve
  visibility. The Jenkins UI will now show the time spent in each step
  of the build process, and if a step (e.g. `make eunit`) fails it will
  only expand the logs for that step by default instead of showing the
  logs for the entire build stage. The downside is that if we do make
  changes to the series of targets underneath `check` we need to
  remember to update the Jenkinsfile as well.

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

This is a cherry-pick of 9b6454b with the following modifications:

- Drop the MINIMUM_ERLANG_VERSION to 20
- Drop the packaging ERLANG_VERSION to 23
- Add the weatherreport-test as a build step
- Add ARM and POWER back into the matrix using a new buildx-based
  multi-architecture container image.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f0beec55ee...](https://github.com/mrakgr/The-Spiral-Language/commit/f0beec55eef3e20c14e634ae6c20e39852256255)
#### Wednesday 2022-02-09 18:27:32 by Marko Grdinić

"11am. Now that I've started gaming again, I've started getting up late again. Well, let me chill and I will start.

12:45pm. Let me start the day. I am done with breakfast and chores.

https://www.youtube.com/watch?v=JmELOJ1jIPo
Blender 3.2 Alpha Is Here!

Let me watch this. I'll get 3.2 when it is time to get back to Blender.

https://youtu.be/JmELOJ1jIPo?t=546

It might have been better for to try this addon for the logos.

1pm. Done with that vid, let me start my Houdini adventure for today.

1:15pm.

```
exp(fit01(rand(ch("../seed")),log(0.5),log(2)))
```

I hate how Houdini does not check if the vars are proper.

1:40pm.

```vex
vector p0 = point(1,'P',0);

@P -= p0;
@P *= exp(fit01(rand(ch("../seed")),log(1),log(4)));
@P += p0;
```

I suppose this will have to do.

But this only works if the auxiliary output has a single point. If this gets passed in something more, it will break completely.

...Ah, crap, that just scales the stalk properly, but the packed points get moved off it. It does not properly.

1:45pm.

```vex
point("../origin_point/",0,"P",0)
```

I figured it out. I just had to do this in the transform node to set the pivot to the first point. Great!

```
vector p0 = point(0,'P',primpoint(0,@primnum,0));

@P -= p0;
@P *= prim(0,'orig_perim',@primnum) / prim(0,'perimeter',@primnum);
@P += p0;
```

I should get rid of this attribute wrangle as well.

No, let me not mess with what works properly.

2pm. I put in a bunch of variation.

Forgot to turn off the points Houdini crashed.

2:05pm. Wow, it is a jungle out there. I need to scale it down.

2:25pm. Hmmm, ok. I think this suffices as far as vines are concerned.

Let me add a sphere into the bulb.

2:35pm. Added a sphere. What I am doing right now is reflecting on the making of this.

I think I got it worng. Instead of conceptualizing it as vines -> branch -> flower, in other words as object hierarchies, what I should have do is conceptualize it as pass hierarchies.

vines -> vine_stalk_group -> branch -> branch_stalk_group -> flower -> flower_stalk_group.

Each object would produce a group I could distribute on. That would have made things so much easier and more efficient. For flowers I could have just produced 30 different flowers to distribute thme on the branches. For the wines I could have also made 10 different branches as well.

Instead of doing that, I made the mistake of both underestimating the computational demand of my current apporach as well as not recognize the fact that Houdini is a first order language rather than a higher order one. It may be worth it to just scrap this and do it all from the start.

2:45pm. No, it would take too long. I'll just keep the lessons in mind for my next project.

It does not really matter apart from taking longer to compute. I'll just turn the wines off until it is time to plug them in.

2:50pm. Let me just back in the glory of this. I'll take a screenshot and post in the Houdini general.

2:55pm. Actually, no. Before I move on, I should investigate my pass idea. Can I distribute object while merging their point groups together?

///

I am happy with how this came out, but under the hood I messed up the architecture. I imagined it as big vines -> branches -> flowers, in other words as an object hierarchy. But instead what I should have done is each of the the phases produce a group that the later ones can distribute on, in other words vines -> vine_stalk_group -> branch -> branch_stalk_group -> flower -> flower_stalk_group

This would have brought out the performance benefits of parallelism and made the node tree easy to deal with. I won't bother redoing it from the start, but I am going to have to look into whether Copy To Points can merge point groups of the objects it is copying. I expect it should since this is such an obvious approach to take given Houdini's design. I just did not realize that Houdini is a first order language until yesterday.

///

3:30pm. Scatter and Align has the ability to tag each of the points with a primnum. That would make things a lot easier than using iteration wouldn't it? I could use that as a random seed.

3:40pm. This nesting of groups is a really powerful concept I should have figured earlier.

But things are looking up. I can actually smell cigarete smoke now. And I've realized that Tabitha, that female super mutant from the Fallout NV radio broadcast can't possibly be female due to super mutants being infertile and genderless.

My brain is starting to work again.

3:45pm. Ok, I'll leave the pool water for last.

3:50pm. Ok, let me eat a fruit, and then I am going to start. Right now I can't make up my mind what I want to do. I need to kick myself in the ass and do the props. Table, chain, menu holder, sunbed, towel rack. I should also decorate the pool a bit.

4:05pm. Ok, let me do it. What I need to do here is check out the Labs tools. There is probably a node for common propers in there somewhere.

...Houdini is somewhat buggy. It crashed on me just now.

4:05pm. There is something called labs obj importer. Maybe it would work better than the native one.

4:20pm. Unless I want to model the chair and the table myself, I should take a look at reusing some assets. Let me do it.

https://www.orbolt.com/asset/theis::furnitures

Oh, this is free.

4:25pm. I should take a look at some of the existing assets. Esp if they are free. Now, why doesn't launch in Houdini work?

4:35pm. Grrhhhh...I got the file manually, and installed it, but now I have no idea how to use it. For some reason it is not an HDA, but an OTL.

Why is everything in Houdini so complicated. It feels like nothing works out of the box.

Well, let me just plow onward. Maybe there is an Orbolt tutorial out there.

https://www.orbolt.com/asset/Boolean_Fracture::Boolean_cutting::1.1

Oh, this is free for apprentice, but costs for the licensed versions. This is a really good licensing scheme.

///

Is there an alternative to using the Launch in Houdini option?
An alternative way to launch in Houdini and sync your account is by opening this page in Houdini's browser (choose Help -> Show Help Pane inside Houdini to open the browser) and clicking Launch in Houdini from there, in order to bypass the url launcher.

Alternatively, you may sync your orbolt account by clicking 'sync' from the Asset Browser pane.
After any of these steps are performed, you should be able to install this (and all other) copy protected HDA files.

///

> Alternatively, you may sync your orbolt account by clicking 'sync' from the Asset Browser pane.

Where is the asset browser pane?

> [11652:11288:0209/164254.450:ERROR:device_event_log_impl.cc(208)] [16:42:54.442] Bluetooth: bluetooth_adapter_winrt.cc:1060 Getting Default Adapter failed.

Getting random errors as I do this.

Why is it not accepting the pasword? I literally copy pasted it from Chrome's settings.

4:45pm. Ah, I found the asset browser. It literally just sends me into Chrome.

4:50pm.. Let me ask in the Houdini general.

5:05pm. Ok, the asset it super lazy. I have a slider that allow me to pick between few different type of furniture. That is as far as its customizability goes.

5:10pm. https://www.orbolt.com/asset/theis::tj_bench

This bench looks good. It fits the theme more than the bistro chair and table that I have in Blender.

Orbolt is really a ghost town. There is not much point in looking for props there.

5:20pm. The bench table is lazily done, but I'll make use of it.

I think that for the rest, I should just do them myself.

Either that, or import the from Blender.

5:30pm. I am feeling the intertia that I usually do when programming new things. Instead of jumping into it, I seem to be hanging back and agonizing over my choices.

Let me redo the wines after all. I am going to get rid of the pomp. I am going to get rid of all the complicated stuff and distribute the objects as I should have.

7:05pm. Done with lunch.

Here is what I have now. I've turned the stalk straightening node tree into a HDA. That just gives me a curve that I can deform using a slider.

Then I have the stalk producing node tree, which I've also turned into a HDA. The process of going over it made me realize why it did not occur to me to treat scattering as separate passes. It is because I wanted to do the curve related scaling right there.

Right now, instead of distributing the leaves, I just output the primitive group of the body. That will simplify things greatly down the road.

I suppose you really need experience for these kinds of optimizations. Thinking about it gets easier once you've been down the block a few times.

7:15pm. It just occured to me. Instead of blasting points above `P.y>5` I should create a group using a selection and pass that into scatter. This is for the main two vines.

7:20pm. i definitely need to remember to try that. I'll leave it for tomorrow. Right now, bath and then gaming in that order. It is 2022 and I've been playing Fallout New Vegas for the first time. I got the game back in 2015 in anticipation of getting my new PC, but never had the chance to play it. I was literally too busy with programming. But now it is finally time to reward myself.

Honestly, I thought it would be boring, but it is easy to get into it.

I can't lose sight of my goals. Cultivate art skills, make money, get the AI chip, infer better learning algos, cause the Singularity.

I have no idea whether I am going to get noticed for those Reddit posts on the Groq/Tenstorrent subs, or whether I will literally cultivate my art skills enough to make Heaven's Key and make money that way. Either way, it seems like I will have enough time.

If I cannot manage to do this, only death and destruction awaits me. And not the good kind of death and destruction I bring to other people.

Thought I've veered from the main path quite a bit, I need to keep pushing forward. At some point I'll get back to Spiral and programming."

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[01341ca95f...](https://github.com/Perkedel/Kaded-fnf-mods/commit/01341ca95ff948b3cdecc646f91cdaaae22e99a3)
#### Wednesday 2022-02-09 18:43:06 by Joel Robert Justiawan

[skip ci] pegsel

the sans appears. also try Surge XT if you need inspiration for the voice of your OC.

uneinsteal delay on that we're pecking ending the song!!! that!!! yess.

disable quantization also if Haxe script load. well uh if you wish to force quantize no matter what, feel free to do so. WHoah we also shortenfuscated the check stepmania & modchart too in Note.hx yey!!!!

reveal the true purpose of Last Funkin Moments. why did Last Funkin Moments exist? how did JOELwindows7 ended up suspending the development of Hexagon Engine in favour of modding FNF? When the true release of Godot 4 come? Godot 4 is still alpha right now. We should upgrade Hexagon Engine project now as soon as the Godot development feature freeze (leaving only Bugfix) declared at some point, I think... I just want to make sure it is definitely defined like this now and it stays like that for the foreseable future, because obviously it's production, please No breaking change era right? yeah. that.

We really stop Hexagon Engine development and no more small development ever since Godot 4 alpha release. we must wait. really wait.

Install Force quantization even if any modchart loaded. stage modchart does not cancel quantization even not forced.

hi NateAnim8! Friends! welcome back.

only left 2.

It was Thomas' (the spy) idea to face reveal! Please don't trash! wtf man?! I want them back!!! like Whitty does.

okay, I'm sorry if we procrastinated, only progressed few for this Heartbreaking. We are lastly hunting VST plugin which plays MIDI, and every MIDI playback workflow with just VSTs and the host. yeah, failed, nobody has the perfect tool. This VSTHost https://www.hermannseib.com/english/vsthost.htm by Herman Seibb is proprietary gratis, the Open source variant is outdated. kushview Element the VST hoster, Open Source, but the binary prebuilt is PUECKING EXPENSIVE!!! I have to get scammed myself (yep broke the rule, bought that thing. In Perkedel, there is norma, do not pay for tools) just to try it after failure compiling due to out of disk space, because compiling one expands disk usage drastically, not to mention how many SDKs do I have to obtain in order for it to work authentically. btw, buying that one only grants 1 version. download expires in 14 days after checkout. you gotta subscribe to grant you new version when come. SO no lifetime purchase which upgrades for free?? ah shuck! THAT, is pecking Adobe. SO, `You know the rule, and SO! Do I... SAY GOOD` yea you know the drill. Careful though, AAX from AVID is kinda karen, its licensing yess! Nah, Sparsdat don't care. let's go shall we yeah! Remember though, it is sacrifice investment to help everyone here around the world.

James Baxter. oh that animator at Cartoon Network (Adventure Time). nah, just random thought.

Hey, where is the Happy Birthday me?!??! why didn't anyone said that?? whatever, that attention doesn't matter. that's just increase age, nothing else. idk yeah.

Okay, if you made mod for this mod, pls just upload the Polymod files. not the executable, no!

Since nobody wants Windows CE anymore, Industries should've moved to Android. liek wtf, that's also mobile embedded operating system and you can even crazily customize it, and if you don't even have to Google Play... nvm, BUT the license is not that hard, you've been doing this for Microsoft alright? Not that different. Also it's best to just skip straight to legit Linux distro instead. Debian or Arch, your choice.

blender brain hemoragic stroke meme CGmatter mobius strip fasteh side spin then explodos spark particle

unfortunately folks, we still unable to find JUCE to Haxe integration to this day. sadd.

also what if FNF was made with JUCE? okay hear me out, JUCE framework is just bunch of class. therefore you still have to harness C++ all by yourselves. and damn, I haven't been taught C++ object oriented and instead my case of college back then went Java. And then to C# because Unity. yeah that's good, but I did not get C++ object oriented!!! now I have to learn one all by myself. UGH!!!

MIMEtype & —

---
## [R2Northstar/NorthstarLauncher](https://github.com/R2Northstar/NorthstarLauncher)@[26154a9dba...](https://github.com/R2Northstar/NorthstarLauncher/commit/26154a9dba1625cecf6e4a14e15192a9fb35eca0)
#### Wednesday 2022-02-09 19:07:13 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [ArchchancellorMustrumRidcully/moofit-recipes](https://github.com/ArchchancellorMustrumRidcully/moofit-recipes)@[c8f0db3231...](https://github.com/ArchchancellorMustrumRidcully/moofit-recipes/commit/c8f0db3231670429427b9668bb8ba53ae76d7997)
#### Wednesday 2022-02-09 19:08:16 by macmule

Update Storyboarder.download.recipe

Amended regex so that the arm64 version is not downloaded by default.. figured this was favourable as the intel version can run on arm under rosetta.. and not vice versa

```
Processing /Users/ben/Git/other-recipes/moofit-recipes/Wonderunit/Storyboarder.download.recipe...
WARNING: /Users/ben/Git/other-recipes/moofit-recipes/Wonderunit/Storyboarder.download.recipe is missing trust info and FAIL_RECIPES_WITHOUT_TRUST_INFO is not set. Proceeding...
GitHubReleasesInfoProvider
{'Input': {'GITHUB_TOKEN_PATH': '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',
           'asset_regex': '^Storyboarder-.*?[^-arm64]\\.dmg$',
           'github_repo': 'wonderunit/storyboarder'}}
GitHubReleasesInfoProvider: No value supplied for CURL_PATH, setting default value of: /usr/bin/curl
GitHubReleasesInfoProvider: No value supplied for GITHUB_URL, setting default value of: https://api.github.com
GitHubReleasesInfoProvider: Matched regex '^Storyboarder-.*?[^-arm64]\.dmg$' among asset(s): latest-linux.yml, latest-mac.yml, latest.yml, Storyboarder-3.0.0-arm64-mac.zip, Storyboarder-3.0.0-arm64.dmg, Storyboarder-3.0.0-arm64.dmg.blockmap, Storyboarder-3.0.0-linux-amd64.deb, Storyboarder-3.0.0-linux-amd64.snap, Storyboarder-3.0.0-linux-x86_64.AppImage, Storyboarder-3.0.0-mac.zip, Storyboarder-3.0.0.dmg, Storyboarder-3.0.0.dmg.blockmap, Storyboarder-Setup-3.0.0.exe, Storyboarder-Setup-3.0.0.exe.blockmap
GitHubReleasesInfoProvider: Selected asset 'Storyboarder-3.0.0.dmg' from release 'v3.0.0'
{'Output': {'release_notes': '## What’s New?\r\n'
                             '\r\n'
                             '**Localization**\r\n'
                             'Built-in support for American English, Russian, '
                             'and Chinese (Simplified). Use the Language '
                             'Editor to add your own! Share language files '
                             'with friends! Invent a new language! Translate '
                             'Storyboarder into your own secret twin '
                             'language!\r\n'
                             '\r\n'
                             '**Emotions**\r\n'
                             'Slap some personality on those faces with custom '
                             'emotions you draw yourself! (And we really mean '
                             'it, you have to draw them yourself. We ran out '
                             'of time to add more examples).\r\n'
                             '\r\n'
                             '**Hair**\r\n'
                             "Are your Characters due for a new 'do? Hoist "
                             'luscious locks upon their heads using custom '
                             'hair attachments, now in a fancy new tab! Please '
                             'make and share further hair!\r\n'
                             '\r\n'
                             'Runs on **Apple Silicon** (for your fancy new '
                             'Mac you lucky duck)  \r\n'
                             "It's still an Intel app, but it should run "
                             'without issue now with Rosetta 2.\r\n'
                             '\r\n'
                             'Better **UI Scaling** Options\r\n'
                             '\r\n'
                             '**Insert Images** via **Drag & Drop or Paste** '
                             'in Shot Generator\r\n'
                             '\r\n'
                             '**Introducing stbr.link**\r\n'
                             'Storyboarder used to run a VR server on your '
                             "local computer, but it didn't use secure HTTPS, "
                             'and that stopped working in all the VR-capable '
                             'browsers. So, now Shot Generator VR routes '
                             'connections through stbr.link, a server operated '
                             'by Wonder Unit. You can share the link with '
                             'friends, and they can browse your scenes in VR, '
                             'hosted by your computer, in multi-user mode. '
                             'stbr.link does *not* store or have access to any '
                             'of your data other than the basics it needs to '
                             'setup connections between computers -- once '
                             "you've connected to peers, your Shot Generator "
                             'scenes, models, and images are transferred '
                             'peer-to-peer. But keep in mind that anyone with '
                             'the correct link can download Shot Generator '
                             'files from your computer while VR is running.\r\n'
                             '\r\n'
                             '### Added\r\n'
                             '- Shot Generator: Insert Image via Drag/Drop or '
                             'Paste #2143\r\n'
                             '- Storyboarder: Localization #2099\r\n'
                             '- Storyboarder: zh-CN Localization #2125\r\n'
                             '- Shot Generator: Remember Window Size #2112\r\n'
                             '- Shot Generator: Scale UI Automatically on '
                             'Window Resize #2115\r\n'
                             '- IK support for custom characters that have the '
                             'same set of bones as built-in characters. '
                             '#2044\r\n'
                             '- Shot Generator: Character Rotation Gizmo, Add '
                             'Rotation Podium #2098\r\n'
                             '- VR now uses https://stbr.link where multiple '
                             'users can connect #2129\r\n'
                             '\r\n'
                             '### Fixed\r\n'
                             '- Scale UI Save/Restore #2113\r\n'
                             '- Scale UI Min/Max Based on Screen Resolution '
                             '#2114\r\n'
                             '- Shot Generator never-ending camera movement '
                             'bug #2150\r\n'
                             '- Better lock to prevent overwrite in multi-user '
                             'VR #2152\r\n'
                             '- VR Pose Capture bug fix #2172\r\n'
                             '- Storyboarder: Video Export #2107\r\n',
            'url': 'https://github.com/wonderunit/storyboarder/releases/download/v3.0.0/Storyboarder-3.0.0.dmg',
            'version': '3.0.0'}}
URLDownloader
{'Input': {'url': 'https://github.com/wonderunit/storyboarder/releases/download/v3.0.0/Storyboarder-3.0.0.dmg'}}
URLDownloader: No value supplied for prefetch_filename, setting default value of: False
URLDownloader: No value supplied for CHECK_FILESIZE_ONLY, setting default value of: False
URLDownloader: Storing new Last-Modified header: Wed, 17 Feb 2021 16:15:13 GMT
URLDownloader: Storing new ETag header: "d7e9c2137f269d3e1d16fae1d150d09c"
URLDownloader: Downloaded /Users/ben/Library/AutoPkg/Cache/com.github.amsysuk-recipes.download.Storyboarder/downloads/Storyboarder-3.0.0.dmg
{'Output': {'download_changed': True,
            'etag': '"d7e9c2137f269d3e1d16fae1d150d09c"',
            'last_modified': 'Wed, 17 Feb 2021 16:15:13 GMT',
            'pathname': '/Users/ben/Library/AutoPkg/Cache/com.github.amsysuk-recipes.download.Storyboarder/downloads/Storyboarder-3.0.0.dmg',
            'url_downloader_summary_result': {'data': {'download_path': '/Users/ben/Library/AutoPkg/Cache/com.github.amsysuk-recipes.download.Storyboarder/downloads/Storyboarder-3.0.0.dmg'},
                                              'summary_text': 'The following '
                                                              'new items were '
                                                              'downloaded:'}}}
EndOfCheckPhase
{'Input': {}}
{'Output': {}}
CodeSignatureVerifier
{'Input': {'input_path': '/Users/ben/Library/AutoPkg/Cache/com.github.amsysuk-recipes.download.Storyboarder/downloads/Storyboarder-3.0.0.dmg/Storyboarder.app',
           'requirement': 'identifier "com.wonderunit.storyboarder" and anchor '
                          'apple generic and certificate '
                          '1[field.1.2.840.113635.100.6.2.6] /* exists */ and '
                          'certificate leaf[field.1.2.840.113635.100.6.1.13] '
                          '/* exists */ and certificate leaf[subject.OU] = '
                          'UVHK77PMAM'}}
CodeSignatureVerifier: Mounted disk image /Users/ben/Library/AutoPkg/Cache/com.github.amsysuk-recipes.download.Storyboarder/downloads/Storyboarder-3.0.0.dmg
CodeSignatureVerifier: Verifying code signature...
CodeSignatureVerifier: Deep verification enabled...
CodeSignatureVerifier: Strict verification not defined. Using codesign defaults...
CodeSignatureVerifier: /private/tmp/dmg.wVhNMS/Storyboarder.app: valid on disk
CodeSignatureVerifier: /private/tmp/dmg.wVhNMS/Storyboarder.app: satisfies its Designated Requirement
CodeSignatureVerifier: /private/tmp/dmg.wVhNMS/Storyboarder.app: explicit requirement satisfied
CodeSignatureVerifier: Signature is valid
{'Output': {}}
Receipt written to /Users/ben/Library/AutoPkg/Cache/com.github.amsysuk-recipes.download.Storyboarder/receipts/Storyboarder.download-receipt-20210804-122839.plist

The following new items were downloaded:
    Download Path
    -------------
    /Users/ben/Library/AutoPkg/Cache/com.github.amsysuk-recipes.download.Storyboarder/downloads/Storyboarder-3.0.0.dmg
```

---
## [mihirzala/Airbnb_analysis_R](https://github.com/mihirzala/Airbnb_analysis_R)@[6fdcb488bd...](https://github.com/mihirzala/Airbnb_analysis_R/commit/6fdcb488bdca69e8f5c479439ff1fa35948a0d66)
#### Wednesday 2022-02-09 19:59:21 by DataDrinker

Add files via upload

Introduction 

Airbnb is an online marketplace that connects people who want to rent out their homes with people looking for accommodation in that locale. It has massively disrupted the travel accommodation and rental market in the past decade. NYC being the most populous city in the United States, and one of the most popular tourism and business places globally, we decided to explore and visualize NYC Airbnb dataset using R and Tableau.    

Airbnb has been providing unique opportunities for both entrepreneurs and travelers. For the first part of our analysis, we explored various aspects of Airbnb, such as room types, accommodations, location, amenities for entrepreneurs that are looking to host their property on Airbnb as well as factors that can help travelers make best choice for their stay. 

For the second part, we decided to explore the Super Host status of Airbnb hosts. We explored the data to see if the conditions set by Airbnb for Superhost status are strictly followed for all the hosts? We also analyzed the concentration of Superhosts in NYC map and looked deep to see how being a Super Host holds value as a consumer and entrepreneur. 

 

Data Preprocessing 

The dataset we used is from ‘Inside Airbnb’, containing 37,713 records and 74 attributes. We preprocessed the data and removed 29 attributes that were either redundant or out of scope for our analysis. We transformed attributes like host_response_time, host_response_rate, price by removing special characters and converted their data type from character to numeric. As major part of our analysis focuses on Superhost status, we removed 31 NA records from ‘host_is_superhost’ attribute to get clean dataset for effective analysis. 

 

Exploratory Data Analysis 

Listing and Price Comparison for all 5 boroughs (Aayush) 

 

What if a person wants to become a host by using your existing property or wants to rent out a property and then list it on Airbnb. 

This analysis shows us AVG pricing for a listing throughout NYC. We can make assumptions from this analysis that 

Average listings price is the highest for Manhattan (211.72 USD) followed by Brooklyn (136.43). One possible reason for high average price in Manhattan could be that whole apartments/home are the most common type of listings there (we will see an analysis on this in the upcoming slides). 

Bronx has the cheapest listings with an average price of 105.75 USD. 

 

 

This analysis shows us the price comparison of different types of rooms that are offered throughout NYC. 

Analysis: Average price is the highest for hotel rooms followed by Entire home/apartment which is quite expected because of the services offered by a hotel and security when compared it to an entire home/ apartment. Therefore, according to this analysis, shared rooms have a higher average price because the number of rooms available throughout NYC is less and the frequency at which they are booked is lower.  

 

This graphical analysis shows us the type of listing available in each borough ranging from entire home, private room, shared room, or hotel room.  

Assumptions:  

Private rooms are the most common listing type in all neighborhoods except Manhattan where entire Home/apartment is the most common type. 

Hotel rooms are the least common in all neighborhoods (reason: hotel rooms have a quota to certain number of rooms on Airbnb but the prices are usually higher because of the services offered by the hotel). 

 

This analysis shows us what are the top 10 most expensive neighborhoods for an Airbnb and if a person is planning to be a host, this is how they should price the property. 

In reference to the previous analysis where we compared prices of all the 5 boroughs, avg price might be higher in Manhattan but when we look at this analysis the most expensive neighborhood is not in Manhattan. This can be because of the size of property and the area, for example properties in Fort Wadsworth, has views of Manhattan skyline.  

 

This analysis shows us what are the 10 most common amenities a host should offer. For example, Wi-Fi, heating, kitchen, essentials and these are some of the important factors which matter to the customers as some of these are advertised in listing descriptions 

Comparing the price range of private rooms in neighborhoods (Mihir) 

This graph shows the comparison of private rooms. By seeing the boxplot graph, we can state that Manhattan and Brooklyn are the two neighborhoods who have the highest number of private rooms with the price range from $50 to $1000. In Manhattan, Brooklyn, and Queens we can see the major number of private rooms and In Bronx compared to other 3 have less rooms and Staten Island have a smaller number of private rooms with price range near $50 to somewhere $600. Where we can have the lowest range as well, but the number of private rooms is less in that price range. 

Types of rooms can accommodate most people 

In this visualization, we see that which type of rooms can accommodate more people? So, a shared room in Manhattan can accommodate more than 15 people after that Brooklyn can accommodate not more than 7 people. Shared rooms in Queens can allow 5 people. But, in Staten Island it only accommodates 1 person and in Bronx which can accommodate only 2 people, whereas private rooms in Queens and Staten Island can accommodate a smaller number of people but other Three neighborhoods can accommodate more people. Hotel rooms in Manhattan, Queens, and Brooklyn can hardly accommodate more than 3 people as they range from 0. In entire home/apt we can see in every neighborhood more than 15 people can accommodate. 

 
 

 

 

Someone comes to New York City and searching for beds with their appropriate budget. 

For example, if someone plans to visit NYC for vacation and they are searching for rooms with 2, 2.5 or 3 beds where they can live for months or for few days with their appropriate budget, so here is a boxplot on beds and price which states that in Bronx prices range start from $200 to near $500 but in Brooklyn and Manhattan we can see the difference in price because of the views and the more tourist's sites these both neighborhood has the highest price range and highest rooms. In Queens there are rooms which cost from $200 to $600 and Staten Island only rooms cost around $250 to $300.  

 

Do the criteria set by Airbnb for Superhost are strictly followed?  (Madhura) 

While looking for an Airbnb, we are often hit with a few different selections that often have the same amenities and descriptions, however the differentiating factor is the fact that the listing has superhost status or not. This is where we come in to see what it means to be a superhost.  

The creation of the Airbnb Superhost program was a response to the lack of consistent experiences on the platform. 
Airbnb's earlier rating system proved an inadequate way of deciphering between professional quality operators and novice hosts. With 80% of Airbnb properties achieving at least a 4.5-star rating, it was difficult for a guest to confidently select a premium property. The Superhost program fills this void by creating a more comprehensive quality metric that considers a host's entire portfolio of properties. 

Based on Airbnb website, there are 4 criteria that a host must meet to become a Super Host: 

4.8+ overall rating: Superhosts have a 4.8 or higher average overall rating based on reviews from their Airbnb guests in the past year. 

90% response rate: Superhosts respond to 90% of new messages within 24 hours 

<1% cancellation rate: Superhosts cancel less than 1% of the time. This means 0 cancellations for hosts with fewer than 100 reservations in a year. 

10+ stays: Superhosts have completed at least 10 stays in the past year or 100 nights over at least 3 completed stays. 

Out of these, we were able to get data for just two criteria focused on ratings and response from the host. 

For NYC dataset, we found about Host vs. Superhost distribution to be 80%-20%. Out of total 37682 hosts, just 7353 qualifies to be a Superhost. 

  

 

 

4.8 or higher overall ratings 

 

The scatter plot has hosts placed across ratings on the X-axis. The teal color dots in the box here represents superhost that have ratings less than 4.8. To explore deeper, the bar chart shows that there are around 1681 superhosts i.e., about 23% of the superhost don't qualify for this criteria.  

Respond to guests within 24 hours and maintain a response rate 90% or higher 

 

Based on this plot, it is clear that some Superhosts highlighted in box do not exactly follow this criteria. They are either not ‘responding within 24 hours’ or have ‘lesser than 90% response rate’. 

 

Upon taking a deeper look, a small fraction of superhosts i.e., 10 superhosts we are taking “a few days or more” to respond. Also, about 5% of superhosts are having lesser than 90% response rate. 

 

Exploring Superhost Across Boroughs (Alexs)  

 

As a resident within the New York City area, we all know that Manhattan is the heart of the city. It is filled with all the exciting adventure, the historical buildings, train stations and many different tourist attractions that bring them to New York City repeatedly. With our initial interest of looking at the Airbnb data through the spectacle of being a super host or not, we must first understand the dispersion of other data Metrix in comparison. This is intended to fight or prove some common assumption we have about Airbnb in our city. First, we look at the pricing data  

As we explore the pricing data in comparison to many different boroughs, while we do see a density forming within the lower tips of the Manhattan borough, we see also a wider scatter of high-priced Airbnb in the other residential area which is very interesting. We see places in Jamaica as well the tip Staten Island, which is interesting since these areas are the further from other location as well has a very long commute to the city. Then this made me wonder about the super host spread in the city, hoping that the super host would care about their listing more we would assume that the majority would be located where the money maker is, the city. 

 

But then, we were proven wrong, with the number of super hosts spreading around the city. This is a very interesting phenomenon which puts the questions of what the host’s game plan are owning these Airbnb around the city and becoming super host, while the big proportion of the Manhattan borough is not super hosted. If we check the proportion of the data, with Staten Island and the Bronx having the highest proportion of super hosted listings, this validates the idea we had about the Airbnb host having different kind of strategy that they are applying to their listings. Further but cheaper or they accumulate more people that are more loyal and just stay with them due to the host. For that reason, we were more curious, the host that has more listings place within the city would care more about their locations and listings. 

 

But although this number shows a visible characteristic of that behavior, we still see a very large host which owns more than 5 different listings not being a super host. And that begs the question why do people who have more listings not want to be super host? We associate with taking a proactive approach such as getting verified on social media and getting a certain badge on our eBay shop as a sign of slightly higher importance, but this is not displaying 100% on the dataset. Can there possibly be other motives by the host? 

  

Table

Description automatically generated 

 

We were able to find some clues that could have something to do with a flat monthly profit strategy. By using a 30-day minimum stay, hosts do not need to care about being super host or not as they need one person to book their Airbnb for the entire month. Do not get me wrong, this move has its advantages and disadvantages. With the host applying this revenue cap, regardless of the time of year, they cannot potentially earn more, their only move is to increase the prices per night before they book the listing. This revenue cap is remarkably interesting as it is displayed within a group that is not a super host. For the super host, their limit is endless, the blue bar shows their minimum estimated revenue and as more people come during the holidays, they can become very much more profitable than the other strategy.  

 

Conclusion 

As we go through many of the dataset provided by Airbnb, we see much different convincing evidence that were able to prove how popularity of certain areas would affect pricing as well as other aspects of listings. However, it also disproved many kinds of speculation that one would have when they hear about Airbnb in New York City. Superhost was a concept within the system that we were interested in, and it played a role. Even though we found a small number of violations, but they exist. Maybe there are some other exception rules to superhost criteria which are not known. But based on data findings, it is probably safe to say both the requirements laid out by Airbnb themselves might not be strictly followed. Also, Superhost is a factor that allows you to determine the true intention of the host, whether they are trying to provide a better experience to a person or just pursuing Airbnb as a business venture. None the less, it was a remarkably interesting find.

---
## [mrcreepysos/pd2promod](https://github.com/mrcreepysos/pd2promod)@[ebefa06a77...](https://github.com/mrcreepysos/pd2promod/commit/ebefa06a77934a3d54c04403ed1e78c6ce074fe1)
#### Wednesday 2022-02-09 20:54:10 by mrcreepysos

nerf enemy health across the board

bruh holy shit 4 shot headshot tasers with 160dmg rifles
mfw zerker was too fucking good

dozer crit mul was increased to 3.2 (normal headshot multiplier)
tasers are at 1800 health now, medics went down to 1200, shields are at 600
spoocs went down to 2400

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[a916a5d9de...](https://github.com/microsoft/terminal/commit/a916a5d9de450bc6a008d257d3c5c5cfd27e07ec)
#### Wednesday 2022-02-09 21:48:00 by Mike Griese

Make sure the infobar is inserted before the tab content, not on top of (#11609)

Fixes #11606

This is weird, but the infobars would appear totally on top of the
TerminalPage when `showTabsInTitlebar:false`. This would result in the infobar
obscuring the tabs.

Now, the infobars are strictly inserted after the tabs, before the content. So
when they appear, they will reduce the amount of space usable for the control.
That is a little annoying, but preferable to the tabs totally not existing.

Relevant conversation notes from #10798:

> > If the info bar is not local to the tab, then its location between the tab
> > bar (when the title bar is hidden) and the terminal panes feels
> > misleading. Should it instead be above the tab bar or below the terminal
> > panes?
>
> You're... not wrong here. It's maybe not the best place for it, but _on top_
> of the tabs would look insane, and probably wouldn't even work easily, given
> the way we reparent the tab row into the titlebar.
>
> In the pane itself would make more sense, but that runs abreast of all sorts
> of things like #9024, #4998, which might make more sense.

I'm just gonna go with this now, because it's _better_ than before, while we
work out what's _best_.

![gh-11606-fix](https://user-images.githubusercontent.com/18356694/138729178-b96b7003-0dd2-4521-8fff-0fd2a5989f22.gif)

---
## [textbase-sms/next.js](https://github.com/textbase-sms/next.js)@[91146b23a2...](https://github.com/textbase-sms/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Wednesday 2022-02-09 22:53:58 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---

