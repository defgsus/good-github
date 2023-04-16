## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-15](docs/good-messages/2023/2023-04-15.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,919,972 were push events containing 2,680,050 commit messages that amount to 150,915,738 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [jamespack/terminal](https://github.com/jamespack/terminal)@[21464fe41c...](https://github.com/jamespack/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Saturday 2023-04-15 00:08:24 by Mike Griese

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
## [pulsar-edit/pulsar](https://github.com/pulsar-edit/pulsar)@[5bba792f42...](https://github.com/pulsar-edit/pulsar/commit/5bba792f42fb66e72fde35222c6912278e9ef879)
#### Saturday 2023-04-15 00:23:16 by Andrew Dupont

Fix insane amounts of tree re-parsing

This is partly something that I copied directly from `TreeSitterLanguageMode`,
but I don't think it's ever quite worked right.

First, the part that's entirely my fault: in trying to keep track of when the
tree is dirty and when it isn't — to at least bring our attention to how often
we're doing off-schedule parses — I marked each `LanguageLayer` with
`this.treeIsDirty = true` the first time `handleTextChange` ran after a
transaction, and would mark them with `this.treeIsDirty = false` after the tree
parse at the end of a transaction.

But not every layer runs `update` after every transaction — only the ones whose
markers were encroached on by the buffer changes! It would _appear_ that as long
as those distant layers are kept up-to-date on changes via `Tree#edit`, they
don't really need to be re-parsed immediately, and can wait until a change that
would actually affect their contents.

At any rate, since some layers didn't get calls to `update`, they also didn't
have their `treeIsDirty` flag reset, and thought that they had dirty trees even
at rest. Combined with my recent realization that off-schedule parses can't be
retained on injection layers, this resulted in a _whole lot of_ “re-parsing”
warnings, even at rest. Even simply when _scrolling_ the editor.

Now, at the end of a transaction, we'll loop through the current injection
layers and set `treeIsDirty` to `false` to be sure.

The other part that doesn't seem right is present in `TreeSitterLanguageMode`:
every single language layer gets `handleTextChange` called with every single
buffer edit (as is necessary), but every single layer keeps track of the
accumulated changes via the `editedRange` property — a range that can only ever
grow over time _until_ the layer's tree is re-parsed. And since we've
demonstrated that some layers may not actually get re-parsed until much later,
we can end up with a situation where (e.g.) a two-line injection on line 500
will eventually invalidate 1000 lines of highlighting _if_ the user makes two
edits: one on line 1 and one on line 1000. Even if they're minutes apart in
separate transactions.

Thus I'm nearly certain that this is wrong as well. If the edits of a
transaction do not result in a given layer being re-parsed, then the fact that a
certain range of the buffer was edited in that transaction ceases to be
relevant, and certainly should not be grown to include the ranges of changes in
_later transactions_. Hence: at the end of a transaction, all language layers
should also have their `editedRange` property set to `null` (if it wasn't
already).

I haven't investigated yet, but I suspect that it _used_ to be the case that
every layer was re-parsed on every transaction. That would explain why this
may have once made sense.

In other news, my idea for the foldable cache to contain ranges rather than
booleans… was silly. The cache is smart enough to shift lines around along with
buffer changes… but for cached ranges to be useful, we'd have to translate the
ranges along with each buffer change, and that's just too much work, especially
when fold captures are so cheap.

---
## [cozy/cozy-drive](https://github.com/cozy/cozy-drive)@[399a96980e...](https://github.com/cozy/cozy-drive/commit/399a96980e464cf6d6f9e60cbbe0a756f6b0cd45)
#### Saturday 2023-04-15 00:25:16 by Crash--

fix: Scroll to top

 Since we are not able to restore the scroll correctly,
 and force the scroll to top every time we change the
 current folder. This is to avoid this kind of weird
 behavior:
 - If I go to a sub-folder, if this subfolder has a lot
 of data and I scrolled down until the bottom. If I go
 back, then my folder will also be scrolled down.

 This is an ugly hack, yeah.

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[3ced3047b8...](https://github.com/ARF-SS13/coyote-bayou/commit/3ced3047b8c32a3e631519f6b117fdc6bf0630d8)
#### Saturday 2023-04-15 00:39:18 by Tk420634

Merge pull request #1949 from ARF-SS13/I-hate-github-a-lot

Fuck you, Vertibird.  Go where I put you

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[7b5b198aa8...](https://github.com/ARF-SS13/coyote-bayou/commit/7b5b198aa80b88426d1150184c78ecd5fa0816b8)
#### Saturday 2023-04-15 00:39:18 by Tk420634

Fuck you, Vertibird.  Go where I put you

You fucking animal of a thing

---
## [BakaKaito/MergeBot.NET](https://github.com/BakaKaito/MergeBot.NET)@[efb36a0816...](https://github.com/BakaKaito/MergeBot.NET/commit/efb36a0816b7203dd8a192105ac1acbf3b823667)
#### Saturday 2023-04-15 00:50:17 by Koi

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
## [clayne/cppfront](https://github.com/clayne/cppfront)@[10241cd6a5...](https://github.com/clayne/cppfront/commit/10241cd6a59040d7408fda674bcdd918bd67c4e2)
#### Saturday 2023-04-15 01:01:48 by Herb Sutter

Checking in various improvements done in the last few evenings

Replace `store_as_base` with generated aggregate bases - better fix for #336, thanks @JohelEGP for the suggestion! This way we also don't need to obfuscate the name anywhere beyond the constructor(s), as the right member object name just enters the class's scope

If the user didn't write a constructor, provide a default constructor

If the user didn't write a 'that' constructor, suppress Cpp1's compiler-generated copying and assignment

Clean up emission of the just-mentioned generated/=deleted constructors, more naturally line up inside the class body following the indentation for other members that the original source code uses

Rename file `load.h` to `io.h` (`file.h` was another candidate), just because it has been bothering me for a year now that except for that one file all the headers were in natural alphabetical order by compilation phase... as of this commit we now have them all in alpha order and phase order: common.h -> io.h -> lex.h -> parse.h -> [*] -> sema.h -> cppfront.h

    [*] coming next here: reflect.h, which will also be in both alpha order and compilation order

Guard `out.construct` with `if constexpr` in case the type is not copy assignable and that path is never requested

Rename `cpp2::error` to `cpp2::error_entry` to quiet a new(? why?) GCC message about shadowing the former name with `parser::error`... I get why the warning is there, but this is a slightly annoying warning to have to satisfy just to compile high-warning-clean on GCC... oh well

Change semantics of emitting `.h2` files: In `-p` pure mode do the existing split of phases 0 and 1 into `.h` and phase 2 into a separate `.hpp`, but in mixed mode put all phases into the `.h`

---
## [e1esd/CST2208](https://github.com/e1esd/CST2208)@[4179a6df8a...](https://github.com/e1esd/CST2208/commit/4179a6df8a7e561cfd9734ea469e65489e298999)
#### Saturday 2023-04-15 02:28:45 by Esha

Add files via upload

Diabetes is one of the most frequent diseases worldwide and the number of diabetic patients are growing over the years. The main cause of diabetes remains unknown, yet scientists believe that both genetic factors and environmental lifestyle play a major role in diabetes.

A few years ago research was done on a tribe in America which is called the Pima tribe (also known as the Pima Indians). In this tribe, it was found that the ladies are prone to diabetes very early. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients were females at least 21 years old of Pima Indian heritage. Here, we are analyzing different aspects of Diabetes in the Pima Indians tribe by doing Exploratory Data Analysis and building a classification Model.

Dataset Information:

Below is the attribute information:

Pregnancies: Number of times pregnant
Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
Blood pressure: Diastolic blood pressure (mm Hg)
SkinThickness: Triceps skinfold thickness (mm)
Insulin: 2-Hour serum insulin (mu U/ml) test
BMI: Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction: A function that scores the likelihood of diabetes based on family history
Age: Age in years
Outcome: Class variable (0: the person is not diabetic or 1: the person is diabetic)
This project is focused on Exploratory Data Analysis and Model Training using Python.

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[edabb9be67...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/edabb9be679c65f176532670b339d9adc859e664)
#### Saturday 2023-04-15 02:37:49 by SkyratBot

[MIRROR] Stops station blueprints from expanding areas of non atmos adjacent turfs. [MDB IGNORE] (#20480)

* Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

* Stops station blueprints from expanding areas of non atmos adjacent turfs.

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[66cb695343...](https://github.com/tgstation/tgstation/commit/66cb695343721087437e651d07268e284e25763d)
#### Saturday 2023-04-15 02:45:21 by carlarctg

IV drips' default transfer rate is no longer zero. (#74724)

## About The Pull Request

Set default IV transfer rate to maximum (5) instead of 0.
## Why It's Good For The Game

> Set default IV transfer rate to maximum (5) instead of 0.

When you hook someone onto an IV drip, you naturally expect that to be
the end of the process - you hooked someone to a drip, and now you can
go about your day. Them needing to fiddle with buttons is bad for
several reasons:

- It is unintuitive.
IV drips don't look like machines. Their sprite doesn't reflect the fact
that you need to fiddle with the settings before they can work the same
way any other machine or computer might. And to be honest, they
shouldn't.
- It is separate from how every other server currently has it.
Yes, yes, I know that argument is very flawed and full of holes. But
what I'm trying to say with it is, effectively speaking, an extension of
the above point. In other servers, you drag-click someone to an IV drip
and there we go, it's functional. In TG, it just-so-happens to not be
functional due to what is almost definitely a recent oversight, which
very much can, has, and will lead to unnecessary frustration.
- There is no practical reason for it to be set at 0.
Imagine if chem dispensers started at +0 units and needed to be set to
+5 to continue. Or if bottles had a transfer rate of 0u. Or if guns
started with their safeties on. Even if it made sense, it would just be
frustrating and needless, and wouldn't improve the game in any
significant manner enough to offset frustration. We're here for fun, not
perfect balance or realism/verisimilitude after all.
- It's an oversight.
It was changed in #71217. Before that, it was always set to the maximum,
5u. However, presumably due to confusion (Variables that can be adjusted
ingame usually are set to zero/the minimum possible) it ended up being
changed to this.

Apparently an argument can be made that this is fine because fumbling to
get medical aid done is a part of the game. I disagree heavily - blood
bags are already stored in the cold room, something only 2/5 of the
roles in medbay even have access to, with the paramedic, virologist,
chemist all being unable to reach it. This is already enough 'fumbling'
that's necessary. If someone moved the blood bags outside the cold room
next to the IV drips, then all the better - it's a reward for medbay
being prepared.

However I wouldn't mind if someone asked me to make it so the default
transfer rate is, well, something below maximum. It's common practice in
a lot of parts of SS13 to have things set in an unoptimized state so
players can go around improving them, such as air alarms, cryogenics,
etc. Just as long as it's not literally unusable otherwise, as the
'minimum basic setup' should just be slapping on a blood bag!
## Changelog
Dunno what to put here TBH. Can't tell if it's qol, fix, balance, etc.

:cl:
qol: Set default IV transfer rate to maximum (5) instead of 0.
/:cl:

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[2e5bfe5be6...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Saturday 2023-04-15 02:57:20 by LemonInTheDark

Refactors and optimizes breath code (Saves 12% of carbon/Life()) (#74230)

## About The Pull Request

### How things work

As things currently stand, when a mob breaths several things happen
(simplified to focus on the stupid)

We assert the existance of all possible breathable gases, and pull
partial pressures for them
Then we walk through all possible interactions lungs could have with
these gases, one by one, and see if they're happening or not
As we go we are forced to cleanup potential alerts caused by the
previous breath, even if those effects never actually happen
At the end we clear out all the unused gas ids, and handle the
temperature of the breath.

### What sucks

There's I'd say 3 different types of gas reactions.

- You can "need" a gas to survive. o2, n2 and plasma all fall into this
category
- A gas can do something to you while it's in your system. This applies
to most gas types
- Variation on the previous, some gases do cleanup when they're not in
your system, or when there isn't much of them in the first place

The main headache here is that second one, constantly cleaning up
potential side effects sucks, and fixing it would require a lot of dummy
variables

There's other suckage too.

Needing to constantly check for a gas type even if it isn't there is
stupid, and leads to wasted time It's also really annoying to do
subtypes in this system.
There is what amounts to a hook proc you can override, but you can't
override the reaction to a gas type.
It also just like, sucks to add new gases. one mega proc smells real
stupid.

### Improvements

In the interest of speed:

- I'd like to build a system that doesn't require manually checking for
gas
- Reacting to gas "disappearing" should be promoted by the system,
instead of being hacky.
- I would like to avoid needing to assert the existence of all possible
gases, as this is slow on both the assert and the garbage collect.

In the interest of dev ergonomics:

- It should be easy to define a new gas reaction 
- It should be easy for subtypes to implement their own gas reactions.
The current method of vars on the lung is all tangled up and not really
undoable as of now, but I'd like to not require it
- It should be possible to fully override how a gas is handled

### What I've Done

Lungs have 3 lists of proc paths stored on them

Each list handles a different way the lung might want to interact with a
gas.
There's a list for always processing on a gas (we use this for stuff
that's breathed), a list for handling a gas in our breath, and a list
for reacting to a gas previously being in our breath, but not any more.

Lungs fill out these lists using a helper proc during Initialize()
Then, when it comes time to breath, we loop over the gas in the breath
and react to it.
We also keep track of the previous list of partial pressures, which we
calculate for free here, and use that to figure out when to call the
loss reactions.

This proc pattern allows for overrides, easy reactions to removals,
lower indentation code and early returns, and better organization of
signal handlers

It's also significantly faster. Ballpark 4x faster

### Misc

Removes support for breathing co2, and dying from n2 poisoning. 
They were both unused, and I think it's cringe to clutter these procs
even further

Added "do we even have oxyloss" checks to most cases of passive
breathing.
This is a significant save, since redundant adjustoxy's are decently
expensive at the volume of calls we have here.

Fixes a bug with breathing out if no gas is passed in, assigning a var
to another var doesn't perform a copy

Rewrote breathe_gas_volume() slightly to insert gas into an immutable
mix stored on the lung, rather then one passed in
This avoids passing of a gas_mixture around just to fill a hole. 

I may change my mind on this, since it would be nice to have support for
temperature changing from a hot/cold breath.
Not gonna be done off bodytemp tho lord no.

Uses merge() instead of a hard coded version to move the gas ids over. 
This is slightly slower with lower gas counts but supports more things
in future and is also just easier to read.

## Why It's Good For The Game

Faster, easier to work with and read (imo)

Profiles: 

[breath_results_old.txt](https://github.com/tgstation/tgstation/files/11068247/breath_results_old.txt)

[breath_results_pre_master.txt](https://github.com/tgstation/tgstation/files/11068248/breath_results_new.txt)

[breath_results_new.txt](https://github.com/tgstation/tgstation/files/11068349/breath_results_new.txt)

(These profiles were initially missing #73026. Merging this brings the
savings from 16% to 12%. Life is pain)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Wolf860215/Piotr-](https://github.com/Wolf860215/Piotr-)@[56cb5559b5...](https://github.com/Wolf860215/Piotr-/commit/56cb5559b54382318349a2197765aa002b2d5936)
#### Saturday 2023-04-15 02:59:27 by Wolf860215

Create I need money for my life and my family and friends who have a lot of fun with me and my family will always love you and your family 8README.md

---
## [The-Moon-Itself/Shiptest](https://github.com/The-Moon-Itself/Shiptest)@[0410075cc8...](https://github.com/The-Moon-Itself/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Saturday 2023-04-15 03:20:19 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[b5dc4835a6...](https://github.com/thgvr/Shiptest/commit/b5dc4835a6af4fc2ee07e2d26e86382b3d0fb1ab)
#### Saturday 2023-04-15 04:19:50 by Bjarl

New Ruin: Singularity Research Lab (#1612)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds the Singularity Research Lab, formerly a cutting edge science
station, now overrun with kudzu, it is a space ruin.
<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->
![2022 11 25-10 46
03](https://user-images.githubusercontent.com/94164348/204041197-027d9a73-8707-4a00-ad5c-1afcfeff13e0.png)
![2022 11 25-10 46
14](https://user-images.githubusercontent.com/94164348/204041200-98d1a2ac-112c-4c4f-b1ff-d0c1e5a59e81.png)
![2022 11 25-10 46
06](https://user-images.githubusercontent.com/94164348/204041203-4e84a947-8ec9-476d-ae8e-aa9bc17c101a.png)

The two areas of note are the singularity reactor, which is assembled,
and would just need a hand if someone were to want to start it, and the
research lab. The Research lab contains the fruits of the now deceased
science staff's labors, assorted energy weapons. Unfortunately, it also
contains the deceased science staff.

![dreamseeker_HFLqhdKLV5](https://user-images.githubusercontent.com/94164348/204038725-1dd396cd-4961-40e1-bd7a-b60b69a33eaf.png)
Other areas of the base were not so lucky, and are thoroughly infested

![image](https://user-images.githubusercontent.com/94164348/204039090-c85eb551-af84-4000-b1d9-14b15c987680.png)
The engineering team attempted to hold back the vines, and quickly
discovered that fire was not sufficient.

![dreamseeker_IrJikGDXKw](https://user-images.githubusercontent.com/94164348/204039133-273f0a19-c9b7-467e-a06a-05e0a951e4e6.png)
And what used to be the recreation area is completely gone

Notably, the hangar is empty. I plan on making a patch to put a
subshuttle inside it once that rolls around.

Notable loot includes:
3 energy SMGs
3 Flamethrowers
The Ion Projector, a self charging Ion weapon.
An Antique Laser
2 Energy PDWs
2 Accelerator Laser Cannons
4 engineering hardsuits
An engineering lathe and circuit imprinter
A particle accelerator
A singularity generator
6 emitters
1 energy shotgun
Kudzu Seeds
Basically Everything You'd Need For an R&D Set Up
A sense of pride and accomplishment



I feel like this has some rough spots but I've got no idea where to
start, so into the review -> testing -> feedback process it goes

- [x] The ruin spawns when the spawn ruin verb doesn't runtime.
## Why It's Good For The Game
More ruin variety. This one spawns in space and does a few things that I
haven't seen yet. Mainly a singularity, cool semi-hidden asteroid base
that could in theory, be turned into a player lair.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An abandoned Nanotrasen Asteroid Facility has been spotted in the
area. Salvage teams are advised to steer clear, or at least bring a
knife.
add: kudzu zombie subtype. 
fix: vent iconstates.
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
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [scalr-automation/terraform-scalr-flat-mirror4](https://github.com/scalr-automation/terraform-scalr-flat-mirror4)@[8bccd7cc0e...](https://github.com/scalr-automation/terraform-scalr-flat-mirror4/commit/8bccd7cc0e6737234008f7d792206b45898967a6)
#### Saturday 2023-04-15 04:25:18 by scalr-dungeon-master

Merge pull request #26280 from scalr-automation/ahead-coach-enjoy-blood

[Cr-6221] Friend Mr product personal.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[205ea3dad7...](https://github.com/tgstation/tgstation/commit/205ea3dad711fa541f93adc7f2053250d3e3c777)
#### Saturday 2023-04-15 05:01:07 by Bloop

Fixes spoon overlay not updating every time (#74687)

## About The Pull Request

After bludgeoning myself one too many times with a spoon, here we are.

The spoon overlay wasn't updating to reflect that soup had been
consumed, which led to trying to eat it again and then pain.

Why do spoons hurt so much?

## Why It's Good For The Game

Less spoon related injuries.

## Changelog

:cl:
fix: spoon overlays will now update when you eat from them to reflect
that food = gone. it really is gone, you can stop beating yourself with
the spoon. oh god please stop--
/:cl:

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[96799e2488...](https://github.com/KingDragoness/ProjectHypatios/commit/96799e248826166f5500a4e41f2c49061e665a97)
#### Saturday 2023-04-15 07:12:29 by KingDragoness

Hypatios 1.5.0b4 (Mobius Core chamber+intro overhaulled, Ongoing graphical touchup)
DONE (April 15)
• Chamber 4 modularable parts pipe, walls, red metals
• Chamber 4 overhaul and polishing
o Deadline: 28 April (the last of overhauling the old chambers, completing means 1.5.0 is done)
o Intro is too crowded and need more space
o Chamber/fight area overhauled, added poison water and metal floors
 Your typical poison evil lab
o “MOBIUS CORE” level will be your one-stop, always be visited level for farming and roguelike level
o Secret area removed temporarily due to no use right now
• Enemy test: “EnemyTest_Swarm.cs”
o Check if damaging 50-100 enemies would overwhelm the game systems. (SAFE)
• “MicroDroneControllerSystem” monobehaviour script in [CORE] to handle microbot system (shooting, basic obstacle avoidance and flocking)
• New Enemy: MicroDrone
o Flocking AI group
o MicroDrone usually swarms in 20-50.
o Weak, only has 50 HP but its number will quickly overwhelm the player quickly.
o Fire every 1-1.5 second, deal 3 damage.
• Chamber 4 random spawn area rectangle
• Glowing bird annoying idle keep repeating
• ACCIDENTALLY swapped Animation controller for prompt restart with prompt tutorial
• SentryPDA self-destruct shorten from 3s to 2s.
• Bug: Sentry gun deals zero damage to Sentinel
• Bug: Sentry gun cannot damage GlowingBird
o Caused by pass token as reference rather than new instance
• Bug: Sentry gun aiming wrong target most of time!!!
• Consumables status effect (for kThanid serums)
o Gives the player status effect
• Wall run animated
• InstantiateRandomObject added “TableSpawnPrefab”
• Bug: Intermezzo repeating dialogue bug
• Bug: Trivia UI reduce map extent to 60 x 60.
o Bug pan WASD + Mouse
• Balancing: Disable restart button when falling from the air/IsNotGrounded
o Also restart button will opens up a prompt of are you sure to restart
• Emperor dialogue needed to be fixed at the first encounter
• Emperor sprite cutscene is shit
• Polishing: Remove marketkeeper in Chamber 3
• Bug: Exit door at level 1 is not properly textured
• Bug: Wall run skip level 1 is not UV scrolling
• Bug: Death screen perk upgrade bug:
o Max HP bonus becomes percentage Max HP

---
## [Irawans-Android-Lab/tmp_kernel](https://github.com/Irawans-Android-Lab/tmp_kernel)@[2da958ff24...](https://github.com/Irawans-Android-Lab/tmp_kernel/commit/2da958ff24cebc6986c4f58411a18d1bcb479ce7)
#### Saturday 2023-04-15 07:27:50 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: Pranav Vashi <neobuddy89@gmail.com>
Signed-off-by: dodyirawan85 <40514988+dodyirawan85@users.noreply.github.com>

---
## [ParisNeo/gpt4all-ui](https://github.com/ParisNeo/gpt4all-ui)@[cbf446b3e2...](https://github.com/ParisNeo/gpt4all-ui/commit/cbf446b3e28f4e53791f968c20b6888b4c40c9e8)
#### Saturday 2023-04-15 07:29:31 by Richard Rosario

Update README.md (This really bugged me sorry lol)

got rid of the doubling of "GitHub Repository" as the hyperlink text does the job of rendering the text and providing the link. I'm sure it was a typo no biggie, honestly a super trivial edit I'm aware but it was driving me crazy!

*from this:*
If you are interested in learning more about this groundbreaking project, visit their Github repository [github repository](https://github.com/nomic-ai/gpt4all), where you can find comprehensive information regarding the app's functionalities and technical details. Moreover, you can delve deeper into the training process and database by going through their detailed Technical report, available for download at [Technical report](https://s3.amazonaws.com/static.nomic.ai/gpt4all/2023_GPT4All_Technical_Report.pdf).

*To this:*

If you are interested in learning more about this groundbreaking project, visit their [github repository](https://github.com/nomic-ai/gpt4all), where you can find comprehensive information regarding the app's functionalities and technical details. Moreover, you can delve deeper into the training process and database by going through their detailed Technical report, available for download at [Technical report](https://s3.amazonaws.com/static.nomic.ai/gpt4all/2023_GPT4All_Technical_Report.pdf).

---
## [Garen7/tgstation](https://github.com/Garen7/tgstation)@[296c996434...](https://github.com/Garen7/tgstation/commit/296c996434f34084fa2ef035541a2c82cbfce460)
#### Saturday 2023-04-15 07:45:44 by MrMelbert

Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following: 

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [momentum-mod/website](https://github.com/momentum-mod/website)@[2a6e9087b9...](https://github.com/momentum-mod/website/commit/2a6e9087b969a613d27920013727adfa7dfbe2a4)
#### Saturday 2023-04-15 10:15:12 by tsa96

chore: Remove rimraf

I fucking hate rimraf. Everyone should have a working install of rm if they're using Git. Doing FS stuff in Node is fucking insane.

---
## [Charlese2/space-station-14](https://github.com/Charlese2/space-station-14)@[581e8a0d12...](https://github.com/Charlese2/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Saturday 2023-04-15 10:54:20 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [zhiguohe/dolly](https://github.com/zhiguohe/dolly)@[af91832c66...](https://github.com/zhiguohe/dolly/commit/af91832c663025b9d5b3bd0e01be125b91a51799)
#### Saturday 2023-04-15 11:16:02 by Matthew Hayes

Add response generation for examples from blog post (#27)

This adds response generation code and runs it over the examples from the [blog post](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html).

A few of the sample outputs:

**Instruction:** Write a love letter to Edgar Allan Poe.

> My love for you is as eternal and enduring as the starlit nights, as deep as the ocean depths, as strong as the wind, and as sweet as the summer breeze. My heart has been yours since the first day I saw you, and it will remain yours forever. I can see you now and my heart fills with longing for our embrace, as I long to be with you forever.

**Instruction:** Explain to me the difference between nuclear fission and fusion.

> Nuclear fission is the splitting of a nucleus, which is a heavy atom, such as uranium, into two separate nuclei, while nuclear fusion is the joining of two nuclei to form a single nucleus, such as hydrogen and helium. Fission occurs when the nucleus absorbs a neutron, leaving a remnant of the nucleus. Fusion occurs when the two nuclei come together and form a single nucleus. Fission is a nuclear reaction and fusion is a nuclear reaction.

**Instruction:** Write a tweet announcing Dolly, a large language model from Databricks.

> Dolly, the world's most accurate language model, is now available on Databricks! 🎉 🎉 🎉

**Instruction:** I'm selling my Nikon D-750, write a short blurb for my ad.

> I'm selling my Nikon D-750, an amazing camera. It has the latest features including 12MP CMOS sensor, 9-point autofocus and auto bracketing, and 3.0x optical zoom. It also has a cool Image Stabilizer system and a dual SD card slot. It is a great choice for photographers looking for a reliable camera that offers superior image quality and features.

**Instruction:** Give me a list of 5 science fiction books I should read next.

> 1. The Hitchhiker's Guide to the Galaxy by Douglas Adams 
> 2. Ender’s Game by Orson Scott Card 
> 3. 1984 by George Orwell 
> 4. Star Wars by George Lucas 
> 5. The Hitchhiker's Guide to the Galaxy by Douglas Adams

---
## [psydox/libgdx](https://github.com/psydox/libgdx)@[e1d1fdc5fb...](https://github.com/psydox/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Saturday 2023-04-15 13:59:22 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [system-zero/system-zero](https://github.com/system-zero/system-zero)@[785fff630c...](https://github.com/system-zero/system-zero/commit/785fff630cee95eab4a30952965eb4fe8827fb60)
#### Saturday 2023-04-15 14:24:54 by why not yet another not

Add an initial FILE (file pointer) implementation, that is a higher interface
than file descriptors, alas with an overhead.

We've tried to minimize this overhead a bit, though it is really an introduction.

And quite probably the implementation might misbehave at points and with variation
types of data arguments. The worst case missing of information. This needs time
to think for things to check for a quite broad variable set of conditions, as it
is easy for many things to go wrong with I/O. Quite probably the code will do it
right, but an unknown external factor can influence the result. So because it is
the heaviest responsibility to do the communication stuff (the outside and inside
type of things) for your ecosystem, this will get time. But we do not really have
so much time to wait, and so we had to do something.

And merely because it is very convenient with streams and many packages they need
the functionality, and so delayed the migration to libc.

This was possible thanks to the implementation from neatlibc and a little bit help
from the friends of minibase and dietlibc.

We've also had to modify the vsnprintf() implementation to accept a callback function
to send its byte. By default it writes the byte to its buffer first argument.

fprintf() though, that requires to parse directives and a variable set of arguments,
and prefers to use vsnprintf(), it sets its own callback that does its thing.

This function is to decide to either store this byte in a temp buffer (instead of
calling sys_write() repeatedly), or call fflush() (if the buffer is full, or the
character is a new line character, or the buffer type is in an unbuffered state
(like the standard error stream is by default)). This means that the standard error
stream it writes imediatelly the byte to its underlying file descriptor.

And does its stuff, by working with its filePointer (FILE) structure. It gets its
pointer, by accessing and casting the userdata (void *) field, from the low level format function
(that actually does the parsing) first argument.

This function has been exposed as str_format() and its structure as fmtType.

We really like this vsnprintf() because of its really hard work to deal with all
this complexity, and we would like to keep it forever. I took the currage and the
irresponsibility to migrate some of the code to our style. Really sorry about that,
but you may like to know that i only did it, because it helps me concentrate when
dealing with an application myriad types of challenges. And a same usual symbol
names and a routinally (almost) same set of actions and logic flow helps a lot of
bits.

So there is nothing wrong with your style (in any case its only a style, what it
matters at the end, its the code, and this specific function obviously got a lot
of work and care, and I feel grateful).

Thank you all anyway.

This commit is incomplete but it is late night, and i've to wake up early, and i
really got really tired - but happy.

Rrrreally it needs a lot of work yet, but it is functional!

Have a good now!

---
## [Tsurupeta/Foundation-19](https://github.com/Tsurupeta/Foundation-19)@[6bf6cdb77f...](https://github.com/Tsurupeta/Foundation-19/commit/6bf6cdb77f582598b90e63fa44a922fd033ae3d0)
#### Saturday 2023-04-15 15:37:17 by harry

fixes panic bunker adjacent shitcode (#769)

* ugly as hell

* idiot

* think before i commit (never)

---
## [PixelOS-Devices/kernel_xiaomi_sdm845](https://github.com/PixelOS-Devices/kernel_xiaomi_sdm845)@[5f28a67064...](https://github.com/PixelOS-Devices/kernel_xiaomi_sdm845/commit/5f28a670642b291ddb6baa77c7b2eb455b652c35)
#### Saturday 2023-04-15 16:10:01 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[7df4885117...](https://github.com/shiptest-ss13/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Saturday 2023-04-15 16:20:21 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [FIT4002-TEAM9/Leaf](https://github.com/FIT4002-TEAM9/Leaf)@[ab67538c11...](https://github.com/FIT4002-TEAM9/Leaf/commit/ab67538c11092303dfa171c214735577032b04d1)
#### Saturday 2023-04-15 16:39:39 by Antony

Custom drawer list

- implemented custom drawer options
- however, you need at least one drawer.screen, meaning I cannot just use my custom options
- Accessing current navigation state is kinda a pain in react native
- I think we should maybe implement a basic navigation system that we can then integrate with the rest of the model

---
## [dashpay/dash](https://github.com/dashpay/dash)@[f54ec9cde7...](https://github.com/dashpay/dash/commit/f54ec9cde71ae1b48bbf748c38d70883cda5f87d)
#### Saturday 2023-04-15 17:13:48 by fanquake

Merge bitcoin/bitcoin#21711: guix: Add full installation and usage documentation

fac4814106c796b8786dd90053513cc35142dfe5 doc/release-process: Add torrent creation details (Carl Dong)
5d24cc3d82dad6812f8370c3ccc7c2b5a6c12c11 guix/INSTALL: Guix installs init scripts in libdir (Carl Dong)
5da2ee49d5b44de803b671aedbdd14e5c1d71ea9 guix/INSTALL: Add coreutils/inotify-dir-recreate troubleshooting (Carl Dong)
318c60700b7bbb7ec09a29bf037e7c2787646be6 guix: Adapt release-process.md to new Guix process (Carl Dong)
fcab35b2292f9221eaba521740e8b3b2511a8b78 guix-attest: Produce and sign normalized documents (Carl Dong)
c2541fd0ca99481a5a792a8f2772925d64fb0491 guix: Overhaul README (Carl Dong)
46ce6ce3782dfbd8f9d26dc2ba0f284755e75f2d tree-wide: Rename gitian-keys to builder-keys (Carl Dong)
fc4f8449f34e32b0b9ac9d218d6c3264b02467ba guix: Update various check_tools lists (Carl Dong)
263220a85c1df218431fafbda07c8b23ccc4ce4d guix: Check for a sane services database (Carl Dong)

Pull request description:

  Based on: #21462

  Keeping the README in one file so that it's easy to search through. Will add more jumping links later so navigation is easier.

  Current TODOs:
  - [x] Shell installer option: prompt user to re-login for `/etc/profile.d` entry to be picked up
  - [x] Binary tarball option: prompt user to create `/etc/profile.d` entry and re-login
  - [x] Fanquake docker option: complete section
  - [x] Arch Linux AUR option: prompt to start `guix-daemon-latest` unit after finishing "optional setup" section
  - [x] Building from source option: Insert dependency tree diagram that I made
  - [x] Building from source option: redo sectioning, kind of a mess right now
  - [x] Optional setup: make clear which parts are only needed if building from source
  - [x] Workaround 1 for GnuTLS: perhaps mention how to remove Guix build farm's key
  - [x] Overall (after everything): Make the links work.

  Note to self: wherever possible, tell user how to check that something is true rather than branching by installation option.

ACKs for top commit:
  fanquake:
    ACK fac4814106c796b8786dd90053513cc35142dfe5 - going to go ahead and merge this now. It's a lot of documentation, and could probably be nit-picked / improved further, however, that can continue over the next few weeks. I'm sure more (backportable) improvements / clarifications will be made while we progress through RCs towards a new release.

Tree-SHA512: dc46c0ecdfc67c7c7743ca26e4a603eb3f54adbf81be2f4c1f4c20577ebb84b5250b9c9ec89c0e9860337ab1c7cff94d7963c603287267deecfe1cd987fa070a

---
## [glmdgrielson/words](https://github.com/glmdgrielson/words)@[7615c211af...](https://github.com/glmdgrielson/words/commit/7615c211af488866084f1c116eb8f7b6a287fae5)
#### Saturday 2023-04-15 17:17:30 by glmdgrielson

Add new scene

I'm going to have to do some thoughts about why the general 147 way of
life might not be for everyone and/or why the noble's way of life
continues to be the way it is.

Thank you to skarik for advice and for letting me think out my ideas.

---
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[df247be72a...](https://github.com/kugamo/cmss13/commit/df247be72a87e69e8841ad754633329c87a7883d)
#### Saturday 2023-04-15 17:49:45 by brian

reduces platform and handrail projectile coverage significantly (#2995)

# About the pull request

Does exactly what the title implies: reduces platform and handrail
projectile coverage significantly.
Platforms 60% -> 0%
Handrails 35% -> 10%

# Explain why it's good for the game

When a platform and handrail are combined, that totals at a 95% chance
of blocking a bullet passing through that tile. Platform corners also
catch bullets. That's some hogwash if you ask me. It makes areas like
Sorokyne's Mining platform entrance nearly un-defendable for marines
since they can't shoot past what is effectively an invisible bullet
wall. When I made Sorokyne, this was not the intent of the area. New
Varadero has similar problems.

You may ask, why not change those areas instead? My answer: Sod off,
they look awesome, and I don't want to code a check on projectiles to
determine if you're shooting 'up' at a ledge which would be the logical
simulationist fix. Also handrails aren't supposed to block bullets
unless they're reinforced (not that anyone uses that mechanic though).
How do I know this? I willed this mechanic into existence for Strata
with shitcode. I was there when it was written.

Both xenos that spit and marines that shoot will benefit from this
change.

Oh yeah and corners won't catch bullets anymore.

# Changelog

:cl: Triiodine
balance: Reduced projectile coverage of platforms from 60% to 0%.
balance: Reduced projectile coverage on handrail types from 35% to 10%.
Sandstone handrails are unaffected and remain at 35% projectile
coverage.
balance: Sandstone handrails can no longer be reinforced.
/:cl:

---------

Co-authored-by: Chadwick B. Dunlop <fake@fake.mail>

---
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[4e86fc8df2...](https://github.com/kugamo/cmss13/commit/4e86fc8df2247dcb18b14e473d6ab6cca3c7567d)
#### Saturday 2023-04-15 17:49:45 by victorjosephespinoza

Let (whitelisted) ghosts join in as Working Joes (#2963)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

https://forum.cm-ss13.com/t/make-it-so-ghosted-players-can-spawn-in-as-working-joes/588
Adds a ghost verb so ghosts can now join the game as working joes.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Like it was said in the forum post, Joes are pretty much harmless, their
impact on the round is pretty much minimal, so adding this wouldn't
imply any balance change whatsoever.

The intent of adding something like this to the server is mainly trying
to get more attention to the role. Which is barely played at the moment,
however, if dead players could now respawn as them, I believe it might
get more activity.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
Unsure of what kind of debugging I could provide in here, request any in
the comments and I'll do it.

There's a high chance that something is not treated as it should. This
is probably the first PR where I had to look and understand what I was
writing, despite the fact that a lot of the code is taken from the pred
initialization. So yeah, if you would have placed something somewhere
else, or differently, go ahead and tell me.

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

:cl:H20Begod
add: Added a new verb for ghosts to join in as working joes (ONLY
WHITELISTED GHOSTS).
code: Edited max spawns of the working joes to 3.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [SymmetricDevs/Supersymmetry](https://github.com/SymmetricDevs/Supersymmetry)@[ea770d1f3e...](https://github.com/SymmetricDevs/Supersymmetry/commit/ea770d1f3e9c049737c6acd58fbca8a291c64497)
#### Saturday 2023-04-15 18:20:01 by Rainbuu

Lignite coal for torches (#127)

* Lignite coal for torches

blame someone on discord. its only 2 torches per recipe because lignite sucks ass

* Anthracite torches

how the fuck do you spell this

---
## [TheLoneTec/VilesMods](https://github.com/TheLoneTec/VilesMods)@[20dbfe14f2...](https://github.com/TheLoneTec/VilesMods/commit/20dbfe14f215be9e5b73fa22199e5724b8035657)
#### Saturday 2023-04-15 18:24:23 by Vile

WYP balance update, other updates (see below)

AMUSE BOUCE
- Hearths are now flickable

HARDCORE RENOVATIONS
- Upper diagonal walls (thanks to TheLoneTec)
- 'Walls' can be made of more materials (like plastic)

HELL BENT FOR LEATHER TANNING
- Balance adjustments to matierals and beds for Warm Soft Beds

MATERIALS SCIENCE
- Removed an experimental apparel def (bunker gear) that shouldn't have been there in the first place.
- Fixed bronze recipe
- Nerfed plastics (they were too powerful for quick weapons)
- Added unique adjectives for anodized Al
- Crucible steel now counts as a corrosion-resistant metal to make chemistry station more attainable (for now... testing)
- Fixed bog iron recipe
- Mineable Sphalerite (Zinc) will be a bit more common in new maps

METALLURGY
- Some production buildings have smaller or zero penalty for being outdoors.
- Halved charcoal production efficiency, making it more valuable as an ingredient than a fuel
- Kiln Fix removed - the problem should be fixed in CoreSK

WOOD YOU PLEASE
- Greatly increased firewood production efficiency
- Made other fuels and extract recipes faster
- Riven boards recipe more efficient
- Riven boards now made with logs
- Acacia wood won't cause an error if you're not using Biomes:FTGU mod
- Chopping blocks have zero penalty for being outdoors.
- Added new workGiver def for wood splitting (so chopping block/spot is a separate job from mailling planks)

VILE'S TWEAKS
- Removed the realistic darkness patch

---
## [IvanIsCoding/rustworkx](https://github.com/IvanIsCoding/rustworkx)@[e025356b04...](https://github.com/IvanIsCoding/rustworkx/commit/e025356b046a807e848a7c0ee2a32490927d46da)
#### Saturday 2023-04-15 18:26:10 by Matthew Treinish

Update tox configuration to use tox >= 4.4.0 (#851)

* Update tox configuration to use tox >= 4.4.0

Tox 4.0.0 was released in December 2022 [1] and was a major rewrite of
the internals of the package that included numerous backwards
incompatible changes [2]. Along with that major rewrite was a long
period of instability in the package with a flurry of 47 releases [3]
since 4.0.0 (which has only been 3-4 months). At the time of the 4.0.0
release we pinned the tox version in CI with #761 to avoid this
instability as our tox configuration was not compatible with tox 4.x.y
and tox was actually not compatible with how we had things configured
more generally. The hope was that tox would stabilize more, fix the
issues that plagued the tox 4 release series and we'd be able to relax
that pin without requiring bumping our minimum tox version to ensure
users could use either the old version or the new version locally.
However, since #761 that hope hasn't been realized the divergence
between tox 3 and tox 4 has only widened and at least personally I'm not
convinced of an improvement in stability to the tox 4 release series.
That being said however, this is becoming a developer pain as by default
when setting up a new build environment pip will install the latest
version of tox and we don't have an effective mechanism to pin the tox
version for users as you need to install tox manually as it's the
primary python development entrypoint we use. The only only avenue to
address this would be documentation updates in the CONTRIBUTING.md file,
which we didn't update at the time in #761 because it was meant to be
a version temporary pin that has turned out to not be so temporary.

Since it's been >3 months since we first pinned the tox version and that
pin was meant to be temporary this commit removes that pin and bumps our
minimum supported tox version to be 4.4.0, which despite not being
compatible with tox < 4 as we originally hoped, at least seems to work
fine with install rustworkx after updating the configuration file. This
should hopefully ease the onboarding experience for developers when
working with rustworkx and trying to bootstrap a local development
environment. Longer term I expect we'll look at moving off of tox,
as it no longer seems like a project we can rely on (especially as
a key component for our development and CI infrastructure) for rustworkx
and instead look at something like `nox` which I've heard good things
about and know that PyO3 had moved to it a year or two ago.

Fixes #812

[1] https://pypi.org/project/tox/4.0.0/
[2] https://tox.wiki/en/latest/upgrading.html
[3] https://pypi.org/project/tox/#history

* Stop using tox for retworkx backwards compat jobs

Tox's isolated builder mechanism seems to be incompatible with our
environment variable based package naming mechanism that we use to build
the legacy retworkx package. This is causing CI to fail on the backwards
compat jobs that are installing retworkx (which depends on rustworkx) to
ensure that our backwards compatibility shim works as expected. Instead
of trying to force tox to do the correct thing, it's just easier to stop
using it for that one CI job and instead just manually install and run
the tests.

---
## [Jacob-Jeffries/social_backend](https://github.com/Jacob-Jeffries/social_backend)@[83328184bc...](https://github.com/Jacob-Jeffries/social_backend/commit/83328184bc81cf67ea252a9838cceaac29d9b51f)
#### Saturday 2023-04-15 20:33:15 by Jacob Jeffries

God FUCK, finally found my error in the reaction virtual - this took 4 fucking god damn hours!

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[7f8874df29...](https://github.com/Bjarl/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Saturday 2023-04-15 22:13:02 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
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
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [samicrusader/Histoire](https://github.com/samicrusader/Histoire)@[951df013eb...](https://github.com/samicrusader/Histoire/commit/951df013ebbaa9d4e935658ec03cfa4ca2172d34)
#### Saturday 2023-04-15 22:21:44 by samicrusader

fix: please just use my fucking font-size for God's sake

---
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[09e95cdfbc...](https://github.com/Apogee-dev/Shiptest/commit/09e95cdfbc8337b5b7a84a088c32b458ee1d996d)
#### Saturday 2023-04-15 22:32:24 by Bjarl

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
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[c21670412d...](https://github.com/Apogee-dev/Shiptest/commit/c21670412dff10f4a3a1b1ab1e72f53294581d25)
#### Saturday 2023-04-15 22:32:24 by Bjarl

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
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[babf89eb74...](https://github.com/Apogee-dev/Shiptest/commit/babf89eb746741ba4f33f686b0c4750fe68e1603)
#### Saturday 2023-04-15 22:32:24 by The-Moon-Itself

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
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[c3b78761d2...](https://github.com/LemonInTheDark/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Saturday 2023-04-15 22:42:36 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[b5ebf5c942...](https://github.com/LemonInTheDark/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Saturday 2023-04-15 22:42:36 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[20b3f4ca5c...](https://github.com/re621/dnpcache/commit/20b3f4ca5c079de25a2010d2ee623cd17e0295b8)
#### Saturday 2023-04-15 23:24:27 by bitWolfy

Add 1081 artists to the DNP list.

Added: lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, peshky, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---

